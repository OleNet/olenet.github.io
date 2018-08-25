---
layout: post
title:  Global-Locally Self-Attentive Dialogue State Tracker
toc: true 
excerpt: 
date:   2018-07-23
---
# Global-Locally Self-Attentive Dialogue State Tracker 

1. 这篇文章什么领域的
    对话

2. 这篇文章解决什么问题的
    DST

3. 这篇文章的解决方法表面是什么
    上文的action、本轮的utterance、所有候选slot pair对输入到RNN中，计算slot-pair得分。

4. 这篇文章的解决方法背后的物理意义是什么
    上下文联合建模，引入attention机制

5. 这篇文章的亮点是什么
    上下文联合建模，引入attention机制，不用领域词表结合去词汇化的方式

6. 最终效果怎么样
    在dstc2和WOZ数据集上都最佳

7. 对当前的工作有什么借鉴意义
    联合上下文建模.
    request是请求限制条件，inform是添加限制条件

    | System actions in previous turn                              | User utterance                  | Predicted turn belief state                                  |
    | ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
    | N/A                                                          | 我要办理流量包                  | inform(things=COMBO_PKG)                                     |
    | request(price)      <br>request(flow_size)     <br> request(area)      <br>好的，您想办理多少价位的流量包，流量包大小和使用地域？ | 价格便宜一点的，1GB，本地使用的 | inform(price range=cheap)      inform(flow_size=1GB)      inform(area=local) |
    | request(pkg)       <br>好的，我查到了流量包有本地1GB月10元包还有本地5G30元流量包，请问您要哪一个 | 我要第一个                      | inform(do=本地1GB月10元包)                                   |

    

8. 这篇文章发论文的套路是什么
    state-of-the-art


