---
layout: post
title:  Hybrid Recommender Systems Survey and Experiments
toc: true 
excerpt: 
date:   2018-07-31
---

1. 这篇文章什么领域的
    推荐系统(2002)

2. 这篇文章解决什么问题的
    综述

3. 这篇文章的解决方法表面是什么
    文章利用从数据的角度对推荐系统进行了一个分类。具体根据数据来源分类，主要有外部知识、用户x物品、用户。
    简单描述一下这几种方法:

    - Collaborative: 经典的协同滤波方法，利用相似用户的信息进行推荐商品.
    - Content-based: 根据用户点评的商品，对用户建立画像(理解为一个向量即可)，然后再$I$中寻找相似的物品
    - Demographic: 人口统计学，预先收集用户的信息作为背景知识，预测用户的喜好。好处是不需要用户对商品的历史信息，不过随着大家越来越重视隐私，这种方法基本不太可行了。
    - Utility-based：建立一种映射关系，能够预测$u$对$i$的评分。
    - Knowledge-based：我的理解，所谓的知识即用户提供的额外信息。在文中的例子中，用户提供了价格、饭店氛围等多种偏好来引导系统预测推荐的酒店。

    | Technique        | Background                                                   | Input                                                        | Process                                                      |
    | ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | Collaborative    | Ratings from $U$ of items in $I$.                            | Ratings from u of items in $I$.                              | Identify users in $U$ similar to $u$, and extrapolate from their ratings of $i$. |
    | Content-based    | Features of items in $I$                                     | $u$’s ratings of items in $I$                                | Generate a classifier that fits $u$’s rating behavior and use it on $i$. |
    | Demographic      | Demographic information about $U$ and their ratings of items in $I$. | Demographic information about $u$.                           | Identify users that are demographically similar to $u$, and extrapolate from their ratings of $i$. |
    | Utility-based    | Features of items in $I$.                                    | A utility function over items in $I$ that describes $u$’s preferences. | Apply the function to the items and determine $i$’s rank.    |
    | Knowledge- based | Features of items in $I$. Knowledge of how these items meet a user’s needs. | A description of $u$’s needs or interests.                   | Infer a match between $i$ and $u$’s need.                    |

    

4. 这篇文章的解决方法背后的物理意义是什么

    N/A

5. 这篇文章的亮点是什么

    N/A

6. 这篇文章的缺点是什么

    N/A

7. 最终效果怎么样

    N/A

8. 对当前的工作有什么借鉴意义

    这篇文章属于比较老的经典论文了， 2002年发表，引用数3k+。这篇文章不仅对当时的推荐方法做了一个分类，还总结了不同推荐系统的结合套路是什么样的。

    - Weighted: 线性加权，多个系统的权重可以随着用户的行为进行调整、学习

    - Mixed: 混合式，其实就类似于ensemble，最简单的办法是A/B两个系统的评分对应项相乘/加为最终推荐得分。

    - Switching: A/B两个推荐系统，由于冷启动等问题，其中一个系统失效、没有办法预测、或者预测的不好，则切换到另一个系统进行预测

    - Feature Combination: 特征层的整合，例如Content-based和Collaborative特征的结合

    - Cascade:层次化模型，两个模型分别负责粗排和精排。

    - Feature Aug: 原文中，作者这样描述“特征增强”:

      > One technique is employed to produce a rating or classification of an item and that information is then incorporated into the processing of the next recommendation technique. 

    就我的理解而言，这种方法也包含两个模型，只不过第一个模型的输出会做为第二个模型的特征。
    - Meta-level: 仍然是两个模型，但是相较于FeatureAug方法中，第二个模型的输入是第一个模型的输出，meta-level的第二个方法是第一个模型全部(并不清楚作者这个观点是什么样的细节)。

      

      总的来看，这篇文章是非常老的了。不过也可以帮我们了解上一个时代的人，是怎么看这些问题的。如果再看新文章，可以思考一下人们是如何在这些年转换思路的，以及转换思路的思路是什么。

9. 这篇文章发论文的套路是什么

    N/A

