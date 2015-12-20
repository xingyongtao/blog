---
layout: default
title: GitHub Pages 提交文章的简单步骤
---
{{page.title}}
============
这个是写给我自己的简单备忘，免得到处找了。

	// 检出代码仓库
	git clone URL

	//或者更新代码仓库
	git fetch

	// 检出分支
	git checkout gh-pages

	// 编辑更改
	...
	...

	// 提交
	git add ...
	git commit [-m message]
	git push [origin gh-pages]

