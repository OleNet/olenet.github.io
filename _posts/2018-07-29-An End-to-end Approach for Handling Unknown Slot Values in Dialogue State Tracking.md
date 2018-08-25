---
layout: post
title:  An End-to-end Approach for Handling Unknown Slot Values in Dialogue State Tracking
toc: true 
excerpt: 
date:   2018-07-29
---

1. 这篇文章什么领域的
    对话任务
2. 这篇文章解决什么问题的
    解决DST转移过程中，识别不在ontology中的槽位值的问题。
3. 这篇文章的解决方法表面是什么
    利用pointer network，识别在历史中语句中的词作为DST中的槽位值。
4. 这篇文章的解决方法背后的物理意义是什么
    DST的槽位由槽位类型和历史信息共同决定
5. 这篇文章的亮点是什么
    提出了一个框架(1)，能够识别不在系统词表中定义的槽位值(2)，引入了一个dropout技术提高了槽位召回的问题(3)。
     ![image-20180729221717023](./_posts/static/pics/e2e_handling_unknown_slot_values_dst.png)
6. 最终效果怎么样
    本文章为18年的成果，没有17年的MEMNN效果好(74.0% v.s. 72.1%)。但是这篇文章没有用SLU的输出，而且可以解决词表中没有定义槽位值的问题。
7. 对当前的工作有什么借鉴意义
    当前工作中，流量包等业务槽位值是没有办法穷举的，所以这种机制可以解决识别新槽位值的问题，也能解决智能系统落后于业务更新的问题。
8. 这篇文章发论文的套路是什么
    新的整合方法解决过去没人解决的问题。


