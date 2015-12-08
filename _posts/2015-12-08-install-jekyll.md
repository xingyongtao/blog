---
layout: default
title: 安装Jekyll
---
{{page.title}}
============

安装Jekyll
{% highlight bash %}
$ sudo gem install jekyll
{% endhighlight %}

如果遇到失败，换淘宝安装源：

{% highlight bash %}
	$ gem sources --remove https://rubygems.org/
	$ gem sources -a https://ruby.taobao.org/
	$ gem sources -l
	*** CURRENT SOURCES ***
	
	https://ruby.taobao.org
	# 请确保只有 ruby.taobao.org
{% endhighlight %}

接下来就可以安装Jekyll了：
{% highlight bash %}
	$ sudo gem install jekyll
{% endhighlight %}

另外，如果遇到如下错误，说明缺少依赖：
{% highlight bash %}
	extconf failed, exit code 1
{% endhighlight %}


如果是在 Ubuntu 上安装ruby-dev
{% highlight bash %}
	$ sudo apt-get install ruby-dev
	$ sudo gem install jekyll
{% endhighlight %}


如果是在 Mac 上，安装command-line tools
{% highlight bash %}
	$ xcode-select --install
	
	$ sudo gem install redcarpet
	$ sudo gem install pigments.rb
{% endhighlight %}

