---
layout: post
title:  logistic ridge lasso
toc: true 
excerpt: 
date:   2018-07-23
---
# Logistic,ridge, lasso



## Logistic

Cost function:
$$ J(\theta_0, \theta_1) = \frac{1}{2m}\sum{(h_\theta(x^{(i)})-y^{(i)})^2}$$



##Ridge

logitstic +l2 regularization == ridge

Cost function:

$$ min(\left |\left | Y-X(\theta)  \right |  \right |_{2}^2 + \lambda \left \| \theta \right \|_{2}^2) $$



##Lasso

logitstic +l2 regularization == lasso

Cost function:

$$  min(\left |\left | Y-X(\theta)  \right |  \right |_{2}^2 + \lambda \left \| \theta\right \|_{1})  $$