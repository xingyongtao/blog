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
