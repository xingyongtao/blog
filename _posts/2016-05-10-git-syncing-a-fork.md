---
layout: default
title: GitHub 同步fork的简单步骤
---
{{page.title}}
============
这个是写给我自己的简单备忘，免得到处找了。

# 官方参考
### 设置remote
https://help.github.com/articles/fork-a-repo/
### 本地merge
https://help.github.com/articles/syncing-a-fork/
# clone 
```
$ git clone git@github.com:xingyongtao/docker.git
```
# 设置remote
```
$ git remote -v
origin	git@github.com:xingyongtao/docker.git (fetch)
origin	git@github.com:xingyongtao/docker.git (push)
$ git remote add upstream git@github.com:docker/docker.git
$ git remote -v
origin	git@github.com:xingyongtao/docker.git (fetch)
origin	git@github.com:xingyongtao/docker.git (push)
upstream	git@github.com:docker/docker.git (fetch)
upstream	git@github.com:docker/docker.git (push)
```
# 拉取原作者更新到本地
```
$ git fetch upstream
```
# merge
```
$ git merge upstream/master
```
# push
```
git push
```
