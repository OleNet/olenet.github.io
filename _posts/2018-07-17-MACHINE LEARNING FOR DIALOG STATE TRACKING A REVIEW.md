---
layout: post
title:  MACHINE LEARNING FOR DIALOG STATE TRACKING A REVIEW
toc: true 
excerpt: 
date:   2018-07-17
---
1. 这篇文章什么领域的

   对话领域

2. 这篇文章解决什么问题的
   一篇05年的综述。根据前面几届DSTC，梳理了一下DST的概念和几类作法：Rule-based/Generative Based/Discriminative method based.

3. 这篇文章的解决方法表面是什么
   N/A

4. 这篇文章的解决方法背后的物理意义是什么
   N/A

5. 这篇文章的亮点是什么
   N/A

6. 最终效果怎么样
   N/A

7. 对当前的工作有什么借鉴意义
   有几个概念可以借鉴:
   - DST: The term dialog state loosely denotes a full representation of what the user wants at any point from the dialog system.
   - The tracker may have access to the whole history of the dialog up to the current turn, including previous system acts, Automatic Speech Recognition (ASR) hypotheses, Spoken Language Understanding (SLU) hypotheses, and external informa- tion such as databases and models of previous interactions. The ASR hypotheses are typically given as an N -best list of sentences, a word confusion network [5], or a lattice; the SLU typically outputs an M - best list of interpretations
   - Slot type: informable /requested slots. **Informable slots** are attributes of the entities in the database that the user may use to con- strain their search. **Requestable slots** are attributes that users may ask the value of, but may not necessarily be allowed to specify a value for as a constraint. (*<u>A typical example of a requestable slot that is not informable is the phone number, which the user may ask for but would not give as a constraint</u>*).换句话说，前者是带属性的槽位，后者则不带属性。例如属于前者的食物（甜的、咸的、辣的），价格（低、中、高）。
   - Tracker的常用三种做法：1) 基于规则的做法 2)基于生成模型 3)基于判别模型。 其中3)又包括提取特征之后训练分类器的做法，还包括seqeunce标注。当然这些方法也可以做ensemble、结合迁移学习提升效果。

8. 这篇文章发论文的套路是什么
   N/A
