---
id: "20260615-planning-algorithm"
title: "planning_algorithm"
type: "entity"
source: "https://github.com/kushuaiming/planning_algorithm"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
related:
  - notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md
  - wiki/2026-06-15-chhrobotics-cpp.md
---

# planning_algorithm

## 基本信息

- 类型：A* 与 RRT C++/OpenCV 教学演示
- 作者：kushuaiming
- 官方仓库：https://github.com/kushuaiming/planning_algorithm
- 主要语言：C++
- 依赖：CMake、OpenCV
- 许可证：未提供
- 默认分支：`master`
- 快照提交：`e5ce3ffcc04c1c579a9785a42c7d98b27de0a500`
- 最后提交时间：2023-03-18
- 分析方式：静态源码分析；已在 GCC 11.4、OpenCV 4.8 下构建，未启动 GUI

## 当前判断

该仓库适合用最少代码观察 A* 栅格扩展和 RRT 随机树生长，不适合作为算法正确性参考。README 的自动驾驶规划分类远大于实际实现，源码只有两个硬编码二维点机器人演示。

## 实际算法

### A*

- 50 x 50 栅格
- 八连通邻居
- 欧氏距离启发式
- 矩形障碍
- 优先队列
- OpenCV 动画

缺少 open-set 代价松弛、失败处理和对角穿角约束。

### RRT

- 二维均匀随机采样
- 目标偏置
- 线性最近邻
- 固定步长扩展
- 圆形障碍
- OpenCV 动画

只检查新节点碰撞，不检查扩展边；没有最大迭代数、可复现种子和有效目标连接。

## 构建结果

```text
GCC 11.4 + OpenCV 4.8
→ a_star 构建成功
→ rrt 构建成功
```

## 工程边界

- 场景和参数硬编码。
- 算法与 GUI 耦合。
- 没有车辆模型。
- 没有动态障碍。
- 没有统一接口、测试或 CI。
- 裸指针节点没有释放。
- 无许可证。

## 关联笔记

- `notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md`
- `wiki/2026-06-15-chhrobotics-cpp.md`

## 更新记录

- 2026-06-15：基于 `master` 提交 `e5ce3ff` 完成算法范围、源码偏差、构建和工程边界建档。
