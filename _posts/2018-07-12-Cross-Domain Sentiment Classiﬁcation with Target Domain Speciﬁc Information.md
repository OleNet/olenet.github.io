---
layout: post
title:  Cross-Domain Sentiment Classiﬁcation with Target Domain Speciﬁc Information
toc: true 
excerpt: 
date:   2018-07-12
---
1. 这篇文章什么领域的

   sentiment classification, 文本分类

2. 这篇文章解决什么问题的

   用迁移学习解决文本分类问题，

3. 这篇文章的解决方法表面是什么
   和DSN一模一样的网路，但是使用了一部分的target的label信息，即增加了一个target loss

4. 这篇文章的解决方法背后的物理意义是什么
   相较于前人的文章，只用了shared info， 这篇文章突破了限制，引入了少量的target label info

5. 这篇文章的亮点是什么
   突破了前人做domain classification target data 无标签的限制，引入了target信息。再整合式的加入了别人的一个创新方法CMD，代替了MMD作为衡量Diff/Similarity的方法

6. 最终效果怎么样
   做了大量的实验，带/不带CMD的 x 带/不带DA的。

7. 对当前的工作有什么借鉴意义
   可以尝试放入少量的labeled target data进来，毕竟不用白不用。

8. 这篇文章发论文的套路是什么
   打破传统限制，引入target info，提出了一种训练范式(有点像主动学习)，利用了无标签数据。整合式创新，加入了别人提出的CMD算法。
