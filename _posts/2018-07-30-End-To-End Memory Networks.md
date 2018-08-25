---
layout: post
title:  End-To-End Memory Networks
toc: true 
excerpt: 
date:   2018-07-30
---
# End-To-End Memory Networks 


1. 这篇文章什么领域的
    QA问答

2. 这篇文章解决什么问题的
    a. QA问题，
    b.   前序文章 J. Weston, S. Chopra, and A. Bordes. Memory networks. In International Conference on Learning Representations (ICLR), 2015.  的延续。
    解决分阶段训练(?)的问题

3. 这篇文章的解决方法表面是什么

    在图中右侧引入了attention机制，即$O$模块的输出不是$o=argmax(In_k)$而是$p_i=softmax(In_k), o=\sum_{i}p_ic_i$

    ![image-20180730121832322](/Users/liujiaxiang/Document/olenet.github.io/_posts/static/pics/e2ememnn-result.png)

4. 这篇文章的解决方法背后的物理意义是什么

    和前序文章Memory Networks是很相似的，只不过利用了attention机制，能够结合更多的上文信息。

5. 这篇文章的亮点是什么

    可以E2E训练, 不需要强监督， there is no supervision of supporting facts 。

6. 这篇文章的缺点是什么

    在1k QA集合上，和MMNN的效果还有差距。lookup阶段对于大规模的memory还有待优化。

7. 最终效果怎么样

    在synthetic QA 集合上测试，10k训练集，测试集有20个不同类型的问题。Mean error是6.6， failed task是4。

    在Penn TreeBank和Task8上测试语言模型，通过给定当前words选取下一个和里的word。调整hop数发现hop数增大之后，混淆度是有下降的(baseline 115->111)，证明了模型的有效性。

8. 对当前的工作有什么借鉴意义

    

9. 这篇文章发论文的套路是什么

    改进模型。
