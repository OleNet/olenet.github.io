---
layout: post
title:  Pointwise vs. Pairwise vs. Listwise Learning to Rank
toc: true 
excerpt: 
date:   2018-07-09
---

## Pointwise 

每次丢进去算法一个文档，给出score，最后评分。

## Pairwise 

每次丢进算法两个文档，给出偏序关系，最后排序。

  <p style="text-align: center;"><img src="{{ "/images/pairwise.png" | absolute_url }}" alt="" /></p>


## Listwise

每次丢进去所有的文档，直接排序。