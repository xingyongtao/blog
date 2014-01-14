---
layout: default
title: \[机器学习\]线性回归costFunction计算和梯度下降算法更新公式
---
{{page.title}}
===============
这是斯坦福的机器学习课程学习笔记。

课后练习题里有Octave/MATLAB编程，其中涉及到costFunction的计算，课程中一再强调要同时更新参数\\(\theta_j\\),虽然课程中使用的是循环更新的方法，但是很明显MATLAB应该采用矩阵运算的方式，这样就不比关心样本个数和特征维数了，所以有必要把矩阵的写法推导一下。

线性回归的\\(J(\theta)\\)计算比较简单：

$$J(\theta)=\frac{1}{2m}\sum\_{i=1}^m{(h\_\theta(x^{(i)})-y^{(i)})^2}$$

是一个矢量和自己转置相乘,

令

$$\delta=h\_\theta(X)-y=
\begin{bmatrix}
h\_\theta(x^{(1)})-y^{(1)} \\\\
h\_\theta(x^{(2)})-y^{(2)} \\\\
\vdots \\\\
h\_\theta(x^{(i)})-y^{(i)} \\\\
\vdots \\\\
h\_\theta(x^{(m)})-y^{(m)} 
\end{bmatrix}$$

则
$$J(\theta)=\frac{1}{2m}\delta^T\delta$$

其中\\(X\\)是所有样本的特征，是\\(m×(n+1)\\)的矩阵，即\\(X \in \mathbb{R}^{m×(n+1)}\\)。\\(h\_\theta(X)\\)和\\(y\\)都是\\(m×1\\)的向量，所以\\(\delta\\)也是\\(m×1\\)的向量。\\(J(\theta)\\)是一个实数。


写成MATLAB程序，大概是这个样子的：

{% highlight matlab %}
h = X * theta;
delta = h - y;
J = 1 / (2*m) * delta' * delta;
{% endhighlight %}

梯度下降的更新公式是：

$$\theta\_j:=\theta\_j-\alpha\frac{1}{m}\sum\_{i=1}^m{(h\_\theta(x^{(i)})-y^{(i)})x\_j^{(i)}}$$

其中，

$$\sum\_{i=1}^{m}{(h\_\theta(x^{(i)})-y^{(i)})x\_j^{(i)}}\\\\
=\begin{bmatrix}
h\_\theta(x^{(1)})-y^{(1)} &
h\_\theta(x^{(2)})-y^{(2)} &
\dots &
h\_\theta(x^{(i)})-y^{(i)} &
\dots &
h\_\theta(x^{(m)})-y^{(m)}
\end{bmatrix}
\cdot
\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix} \\\\
=\begin{bmatrix}
h\_\theta(x^{(1)})-y^{(1)} \\\\
h\_\theta(x^{(2)})-y^{(2)} \\\\
\vdots \\\\
h\_\theta(x^{(i)})-y^{(i)} \\\\
\vdots \\\\
h\_\theta(x^{(m)})-y^{(m)}
\end{bmatrix}^T
\cdot
\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix}
=\delta^T \cdot 
\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix}
$$

是\\(\delta^T\\)乘以\\(X\\)的第j列，而且是个实数，转置后仍是他本身。

$$\sum\_{i=1}^{m}{(h\_\theta(x^{(i)})-y^{(i)})x\_j^{(i)}}
=\left(\delta^T \cdot 
\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix}
\right)^T
=\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix}^T \cdot \delta 
$$

$$
\theta\_j:=\theta\_j-\alpha\frac{1}{m}\sum\_{i=1}^m{(h\_\theta(x^{(i)})-y^{(i)})x\_j^{(i)}}\\\\
:=\theta\_j-\frac{\alpha}{m}\begin{bmatrix}
x\_j^{(1)} \\\\
x\_j^{(2)} \\\\
\vdots \\\\
x\_j^{(i)} \\\\
\vdots \\\\
x\_j^{(m)}
\end{bmatrix}^T \cdot \delta 
$$

组合成矩阵应该是

$$
\theta:=\theta-\frac{\alpha}{m}X^T \cdot \delta
$$

写成MATLAB程序，大概是这个样子的：

{% highlight matlab %}
%h = X * theta;
%delta = h - y;
theta = theta - alpha / m * (X'* delta);
{% endhighlight %}
    


感谢[MathJax](http://www.mathjax.org)，让我写出了这么漂亮的公式。
