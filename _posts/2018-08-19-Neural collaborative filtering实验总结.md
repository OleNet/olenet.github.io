---
layout: post
title:  Neural collaborative filtering实验总结
toc: true 
excerpt: 
date:   2018-08-19
---

参考了作者公开的[源码1](https://github.com/hexiangnan/neural_collaborative_filtering)和另一个网友的[源码2](https://github.com/LaceyChen17/neural-collaborative-filtering)。

作者公开的源码使用keras+tensorflow实现。但是年久失修，keras的版本和tf的版本远落后与最新版本，无法运行成功。索性找了pytorch版的代码。

跑了别人的代码，也实现了自己代码，发现有很多东西可以总结一下：

- load数据的阶段争取用pytorch提供的DataLoader，速度可以提升非常大。

- 用tensorboardX结果可视化。如果是远程开发机的话，不能可视化可以考虑是不是端口受限。tensorboardX默认端口是6006，可以将端口由6006改为8000试试。```tensorboard --logdir=./ --port=8000```

- 代码结构按照，一般问题不大，用着都比较舒服。哪怕是跑集群任务，也可以把code和data分离开来，上传代码也比较方便。

  ```
  |-- code
  |   |-- data.py
  |   |-- evaluate.py
  |   |-- main.py
  |   |-- model.py
  |-- data
  |   |-- train.csv
  ```

- 在动手之前，不仅要把网络结构的实现想好，其他的工程细节也尽量在5分钟之内想一下，具体包括

  - 数据的结构体（数据组织方式）
  - 评测代码的接口
  - 评测模块的测试

- 做实验写代码之前，一定要想清楚再动手。否则就是在猜，反而影响工程实现的效率。