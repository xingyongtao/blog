---
layout: default
title: 安装Jekyll
---
{{page.title}}
============

	$ gem sources --remove https://rubygems.org/
	$ gem sources -a https://ruby.taobao.org/
	$ gem sources -l
	*** CURRENT SOURCES ***
	
	https://ruby.taobao.org
	# 请确保只有 ruby.taobao.org

	# Ubuntu
	sudo apt-get install ruby-dev
	sudo gem install jekyll

	# Mac
	xcode-select --install
	
	sudo gem install redcarpet
	sudo gem install pigments.rb

