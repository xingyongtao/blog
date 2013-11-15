---
layout: default
title: 设置nginx通过post参数转发请求
poststatic: static/nginx-post-upstream
---
{{ page.title }}
===============
{{ page.date | date_to_string }}

使用tornado起两个简单的server，输出端口和协议用来区分是哪个server哪个协议

[helloworld1.py]({{site.baseurl}}/{{page.poststatic}}/helloworld1.py)

	#helloworld1.py
	import tornado.ioloop
	import tornado.web
	
	PORT = 8888
	class MainHandler(tornado.web.RequestHandler):
	        def get(self):
	                self.write("PORT %d GET: Hello, world\n" % PORT)
	        def post(self):
	                data = self.get_argument("data")
	                self.write("PORT %d POST: data = %s\n" % (PORT, data))
	
	application = tornado.web.Application([
	        (r"/", MainHandler),
	])
	
	if __name__ == "__main__":
	        application.listen(PORT)
	        tornado.ioloop.IOLoop.instance().start()

[helloworld2.py]({{site.baseurl}}/{{page.poststatic}}/helloworld2.py)

	#helloworld2.py
	import tornado.ioloop
	import tornado.web
	
	PORT = 8889
	class MainHandler(tornado.web.RequestHandler):
	        def get(self):
	                self.write("PORT %d GET: Hello, world\n" % PORT)
        def post(self):
                data = self.get_argument("data")
                self.write("PORT %d POST: data = %s\n" % (PORT, data))
	
	application = tornado.web.Application([
	        (r"/", MainHandler),
	])
	
	if __name__ == "__main__":
	        application.listen(PORT)
	        tornado.ioloop.IOLoop.instance().start()

源码安装nginx，带上form-input-nginx模块，详细参见https://github.com/calio/form-input-nginx-module和http://hi.baidu.com/learsu/item/065a2934429fd8f0e7bb7a83

	tar -zxvf /somepath/nginx-1.4.3.tar.gz
	cd nginx-1.4.3/
	git clone http://github.com/simpl/ngx_devel_kit.git
	git clone http://github.com/calio/form-input-nginx-module.git
	./configure --add-module=ngx_devel_kit --add-module=form-input-nginx-module （注意模块顺序）
	make
	sudo make install

配置两个server一个是80端口，可以按参数转发GET请求（POST不能正确处理），另一个监听8080，可以按参数转发POST请求（不接受GET）

附nginx配置[nginx.conf]({{site.baseurl}}/{{page.poststatic}}//nginx.conf)

	...
	    upstream helloworld1 {
	        server localhost:8888 weight=3;
	        server localhost:8889;
	    }
	
	    upstream helloworld2 {
	        server localhost:8889;
	    }
	
	    upstream dt {
	        server localhost:8888 weight=3;
	        server localhost:8889;
	    }
	
	    upstream d2 {
	        server localhost:8889;
	    }
	...
	    server {
	        listen       80;
	        server_name  localhost;
	        ...
	        location / {
	            if ($arg_appid ~ "^a$") {
	                proxy_pass http://helloworld1;
	            }
	            if ($arg_appid ~ "^b$") {
	                proxy_pass http://helloworld2;
	            }
	            ...
	        }
	...
	    }
	
	    server {
	        listen       8080;
	        server_name  localhost;
	
	        ...
	
	        location / {
	            set_form_input $us data;
	            if ($request_method = POST) {
	                proxy_pass http://$us;
	            }
	            ...
	        }
	...

验证结果

	$ curl  http://localhost?appid=a
	PORT 8888 GET: Hello, world
	$ curl  http://localhost?appid=b
	PORT 8889 GET: Hello, world
	$ curl  http://localhost:8080?data=dt
	<html>
	<head><title>403 Forbidden</title></head>
	<body bgcolor="white">
	<center><h1>403 Forbidden</h1></center>
	<hr><center>nginx/1.4.3</center>
	</body>
	</html>
	$ curl  http://localhost:8080?data=d2
	<html>
	<head><title>403 Forbidden</title></head>
	<body bgcolor="white">
	<center><h1>403 Forbidden</h1></center>
	<hr><center>nginx/1.4.3</center>
	</body>
	</html>
	$ curl -d "data=dt" http://localhost:8080
	PORT 8888 POST: data = dt
	$ curl -d "data=d2" http://localhost:8080
	PORT 8889 POST: data = d2

