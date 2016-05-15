---
layout: default
title: GitHub Pages 升级 MathJax 到 2.6
poststatic: static/upgrade-mathjax
---
{{page.title}}
============
[本博客]({{site.baseurl}}/) 最近上传文章，老是提醒 Markdown 渲染引擎不再支持，让升级，升级后又让升级高亮，最后终于折腾成这样的配置：

	markdown: kramdown
	highlighter: rouge

然而，我打开后发现以前的 MathJax 公式，在chrome下全部都在末尾多了一个细细的竖线。

![末尾有细竖线的数学公式]({{site.baseurl}}/{{page.poststatic}}/vertical_tail.png)

无奈只好继续升级 MathJax。我此时使用的是 2.5，去官网查到的版本是 2.6。
下载后解压缩到原先2.5同级目录，并修改layout：

	<!--
	<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
	<script type="text/javascript"
		src="{{site.baseurl}}/third-party-depend/MathJax-2.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
	-->

	<script type="text/javascript"
		src="{{site.baseurl}}/third-party-depend/MathJax-2.6/MathJax.js?config=default"></script>

[果然搞定]({{site.baseurl}}/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/2014/01/05/ml-linear-regression.html)。
