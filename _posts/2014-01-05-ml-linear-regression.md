---
layout: default
title: \[机器学习\]线性回归costFunction计算和梯度下降算法更新公式
---
{{page.title}}
===============
这是斯坦福的机器学习课程学习笔记。

课后练习题里有Octave/MATLAB编程，其中涉及到costFunction的计算，课程中一再强调要同时更新参数\\(\theta_j\\),虽然课程中使用的是循环更新的方法，但是很明显MATLAB应该采用矩阵运算的方式，这样就不比关心样本个数和特征维数了，所以有必要把矩阵的写法推导一下。

线性回归的\\(J(\theta)\\)计算比较简单：

$$J(\theta)= {1 \over 2m \sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2}$$



Test:
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
