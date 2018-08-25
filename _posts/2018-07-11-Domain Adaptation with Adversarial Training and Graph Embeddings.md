---
layout: post
title:  Domain Adaptation with Adversarial Training and Graph Embeddings
toc: true 
excerpt: 
date:   2018-07-11
---

1. 这篇文章什么领域的

   Tweeter 事件分类

2. 这篇文章解决什么问题的

   不同地域的tweeter的分类迁移(Queensland <--> Nepal)

3. 这篇文章的解决方法表面是什么

   Graph embedding as unsupervised learning, combined with DSN to do transfer learning.

4. 这篇文章的解决方法背后的物理意义是什么

   在迁移的过程中，能够学到实践的结点关系。

5. 这篇文章的亮点是什么

   结合了Graph embedding，将社交网络中twitter的图信息在网络中进行了建模，提高了效果。

6. 最终效果怎么样

   相对于baseline提升了5-7%f1


