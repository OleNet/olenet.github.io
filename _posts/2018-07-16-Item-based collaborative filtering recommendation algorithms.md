---
layout: post
title:  Item-based collaborative filtering recommendation algorithms
toc: true 
excerpt: 
date:   2018-07-16
---

1. 这篇文章什么领域的
   推荐系统
2. 这篇文章解决什么问题的
   推荐系统中，协同滤波的两种解法：Userbased & itembased
3. 这篇文章的解决方法表面是什么
   - Userbased
     用了用户与用户之间的信息(相似)来预测某个item的score，可以理解为用户聚类。
   - Itembased
     用户的历史信息建模，预测某个item的score
     item聚类，用相似的item的评分，对某个item打分
4. 这篇文章的解决方法背后的物理意义是什么
   找到相似信息，要么是相似用户，要么是相似的物品。
5. 这篇文章的亮点是什么
   一篇比较老的综述性文章。
6. 最终效果怎么样
    item-item的效果要稳一些，最后的实验MAE的效果，较user-user的效果好0.5个点。
7. 对当前的工作有什么借鉴意义
    如果是对于Kaggle上的WSDM的推荐比赛来说，可以找一个推荐系统源码，利用CF的范式将数据代入，得到一个baseline。
8. 这篇文章发论文的套路是什么
    综述了当时的CF的两种范式。
