---
layout: post
title:  Fully Statistical Neural Belief Tracking
toc: true 
excerpt: 
date:   2018-07-23
---

1. 这篇文章什么领域的
    对话系统

2. 这篇文章解决什么问题的
    Dialogue State的更新方式。

3. 这篇文章的解决方法表面是什么
    结合了上一轮系统的输出(NLG的自然语言表达)，当前轮次用户的表达，系统槽位的候选信息，利用NN的方式，分别得到了上一轮系统输出的语义表达、用户的语义表达、候选槽位的语义表达。
    接着利用了门机制，选择是否采用上一轮的系统输出信息，进行上下文信息建模。其次对句子的语义(本体/槽位)进行的表达。最终完成决策，即更新槽位概率矩阵。
    当然，这还没完，作者又利用了NN，将上一轮的$ DS_{t-1} $和本轮的决策${y_t}​$ 合并，得到了最终的$ DS_t ​$。

4. 这篇文章的解决方法背后的物理意义是什么

    上文系统信息(其实是一个action)、本轮信息联合建模，输出所有槽位的状态。再结合上轮信息输出本轮的对话状态。

5. 这篇文章的亮点是什么

    现有的NBT模型使用手工制作的信念状态更新机制，无论何时将模型部署到新的对话域，都需要进行昂贵的手动重新调整步骤。

    改进了作者之前的一个工作：改进了本轮信息和上轮状态结合时使用的是规则方式，本文用NN对两个信息的结合做了建模，从而从该DST框架中去除最后的基于规则的模块，并且为DST模型提供了一个强大的框架。

6. 最终效果怎么样

    作者使用的是作者自己整理的一份数据集叫做WOZ，1,200 dialogues split into training (600 dialogues), validation (200), and test data (400).  指标用的是joint goal accuracy, 计算方式是

    $$Acc = \frac{\#(turns where user’s search goal constraints were correctly identified)}{\#(total turns)} $$

    最终效果比规则略好。

7. 对当前的工作有什么借鉴意义

    两轮的信息通过$\lambda$来进行融合是可以借鉴的，当然前提是要把当前的问题套进dialogue state这个框架，即每轮其实是有一个槽位概率矩阵在系统中维护着。

    另一个点是作者在开篇的时候，提及当前人们是把SLU和DST分开做[^1]:  但是有前人的工作表明合并做效果更好。

8. 这篇文章发论文的套路是什么

    将基于规则的DS更新变为基于NN的DS更新。



[^1] The Dialog State Tracking Challenge series: A review.