---
layout: post
title:  Attention is all you need
toc: true 
excerpt: 
date:   2018-08-25
---

1. 文章背景简介

   Google的大作，发表在NIPS上，一作是Ashish Vaswani。

2. 这篇文章什么领域的
   MT: Machine Translation

3. 这篇文章解决什么问题的

   不用CNN、RNN，只用Attention机制来做Machine Learning。

4. 这篇文章的解决方法表面是什么

   - **Encoder/decoder**
   - **Attention-module** in **Encoder/decoder**

   <p class="fit" style="text-align: center;"><img style="height: 400px;" src="{{ "/images/2018-08-25-attention-is-all-you-need.png" | absolute_url }}" alt="" /></p>
   

   - Scaled-dot-product attention/multi-head attention in **Attention-module**

   <p class="fit" style="text-align: center;"><img style="height: 500px;" src="{{ "/images/2018-08-25-attention-is-all-you-need2.png" | absolute_url }}" alt="" /></p>


5. 这篇文章的解决方法背后的物理意义是什么

   让模型通过attention机制学习到表示与映射。

6. 这篇文章的亮点是什么

   无rnn、cnn的全attention架构

7. 这篇文章的缺点是什么

   N/A

8. 最终效果怎么样

    评测的指标是BLEU

   - WMT 2014 English-to-German评测中，比最好的模型高2.0个BLEU（包括ensemble模型）
   - WMT 2014 English-to-French评测中，要比所有的但模型结果要好，但是节省了1/4的浮点运算次数。

9. 对当前的工作有什么借鉴意义

   attention is awesome.

   attention的结果也可以获得很好的效果展示

   <p class="fit" style="text-align: center;"><img style="height: 100px;" src="{{ "/images/2018-08-25-attention-is-all-you-need3.png" | absolute_url }}" alt="" /></p>

10. 这篇文章发论文的套路是什么

  颠覆了当时MT-DL都要走CNN、RNN的套路，提出了完全基于Attention的方法，不仅效果好，计算也比较快。

  

