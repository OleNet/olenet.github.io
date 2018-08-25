---
layout: post
title:  Solving the Partial Label Learning Problem An Instance-based Approach
toc: true 
excerpt: 
date:   2018-08-23
---
# Solving the Partial Label Learning Problem- An Instance-based Approach

1. 文章背景简介

   二作是[于菲](https://www.zhihu.com/people/yu-fei-82)，东南大学。文章发表在IJCAI2015.

2. 这篇文章什么领域的
   偏标记领域的文章

3. 这篇文章解决什么问题的

   所谓的偏标记指的是训练样本$x_i$的label由一个集合$S_i$组成，其中只有一个$y_i\in S_i$是真正的label。

4. 这篇文章的解决方法表面是什么

   - Step1. $KNN$聚类，对每一个样本$x_i$聚类得到$k$个近邻样本。
   - Step2. 计算$k$个样本，每一个样本对$x_i$的权重$H$。
   - Step3. 初始化每一个样本$x_i$的标签集合$S_i$内$y\in S_i$的概率$p_i=\frac{1}{S_i}\in[1, c]$ ，$c$是类别个数
     这样假如有$m$个样本，那么就可以得到关于$p$的矩阵$P\in[m,c]$
   - Step4. 令$F_o=P$, 那么利用样本权重迭代$F$，$\tilde{F}_{(t)} =\alpha·H^\mathsf{T}F_{(t−1)} +(1−\alpha)·P $
   - Step5. 迭代完成后，选取更新幅度最大的label作为样本的标签。$\hat{y_i}=\operatorname*{argmax}\limits_{y_c\in \mathcal{Y}} \frac{n_c}{\hat{n}_c}\cdot\hat{f}_{i,c}$

5. 这篇文章的解决方法背后的物理意义是什么

   - 同类别的样本之间是有联系的，这种联系可以用$KNN$去建模，同时再算出来近邻样本的权重。

   - 利用这些近邻样本的标签和权重来迭代更新每个样本的$S_i$的分布。其实后面这一步，也就是step3, 也叫做propagation。说的简单一点，就是以周围样本影响力为权，计算指定目标数值的带权平均。
   - 训练完成后，分布变化最剧烈的标签就是目标标签。

6. 这篇文章的亮点是什么

   - 前人对于偏标记的做法是把$S_i$中的每一个标签都当做是label进行训练，在预测阶段，把输出的值取平均作为预测输出。这种方式显而易见粗暴。
   - 这篇文章开辟了另外一种方式来解决，利用到了样本之间的信息(可以理解为图)来做迭代。显然这种方式就没那么粗暴了。

7. 这篇文章的缺点是什么

   似乎可以再多解释一下，为什么这种方式会work。

8. 最终效果怎么样

   N/A

9. 对当前的工作有什么借鉴意义

   可以用KNN对样本进行聚类，然后获得多个样本之间的影响关系，进而做label propagation。这点挺有意思的。可以mark一下。

10. 这篇文章发论文的套路是什么

   在一个比较偏的领域，解决了前人的问题，并给出大量的实验证明。
