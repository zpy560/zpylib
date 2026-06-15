---
id: "20260615-planning-algorithm-a-star-rrt-demos"
title: "planning_algorithm：A* 与 RRT 的 OpenCV 最小演示"
type: "note"
source: "raw/2026-06-15-planning-algorithm-repository-snapshot.md"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
related:
  - wiki/2026-06-15-planning-algorithm.md
  - notes/2026-06-15-chhrobotics-cpp-planning-control-demos.md
---

# planning_algorithm：A* 与 RRT 的 OpenCV 最小演示

## 一句话结论

planning_algorithm 是一个只有 A* 和 RRT 两个 OpenCV 动画程序的入门仓库，能够在现代 GCC/OpenCV 环境成功构建，适合观察栅格扩展和随机树生长；但 A* 缺少 open-set 松弛更新，RRT 不检查扩展边碰撞且没有迭代上限，加上无测试和许可证，不能作为正确算法基线或自动驾驶规划组件。

## 原文要点

### 实际内容少于 README 分类

README 总结了图搜索、State Lattice、采样规划、插值曲线和数值优化等自动驾驶规划方法，但源码只实现：

```text
50 x 50 八连通栅格 A*
15 x 15 圆障碍场景 RRT
```

两者的地图、起终点、障碍和参数都写死在 `main()` 中。

### A* 演示

A* 使用欧氏距离启发式和八邻域移动，通过优先队列选择最小 `f = g + h` 节点。OpenCV 逐格显示搜索过程，再根据父节点绘制最终路径。

### RRT 演示

RRT 在二维区域内随机采样，以线性扫描查找最近树节点，沿采样方向扩展固定步长。新节点靠近目标后停止，并用父指针绘制路径。

## 我的判断

### 教学价值主要来自可视化，而不是实现严谨性

仓库代码很短，适合第一次观察：

- 启发式如何改变搜索展开顺序。
- 八连通栅格如何生成邻居。
- RRT 如何采样、最近邻和 steer。
- 父节点如何重建路径。

但实现省略了多个决定算法正确性的步骤，读者必须结合伪代码和成熟实现对照。

### A* 没有实现文档中的松弛更新

源码在节点首次加入 open set 时立即将其标记为已访问，后续路径无法降低该节点的 `g` 值。文档明确写了“若通过当前节点得到更小代价则更新 backpointer”，代码却没有该分支。

这说明“看起来像 A*”不等于完整实现。工程版本至少要维护：

- 未发现、open、closed 三种状态。
- 对 open 节点的代价松弛。
- 优先队列过期条目处理或 decrease-key。
- 无路可达的失败返回。
- 对角穿角策略。

### RRT 的碰撞模型只验证点

新节点不在障碍内并不意味着扩展边无碰撞。当步长较大或障碍较薄时，父节点与新节点之间的线段可能穿过障碍。目标连接也需要相同检查。

正确的最小 RRT 应至少增加：

- 线段到圆障碍的距离检测。
- 机器人半径膨胀。
- 最大迭代数和失败状态。
- 固定随机种子选项。
- 最后一步目标连接碰撞检测。

### 与自动驾驶的关系有限

README 使用自动驾驶规划分类，但当前模型没有车辆航向、曲率、速度、道路边界或动态障碍。它们是二维点机器人算法演示，不是车辆可执行轨迹规划。

## 可复用内容

### 推荐使用方式

1. 运行原始动画建立算法直觉。
2. 为 A* 增加 open-set 松弛和失败返回。
3. 构造能让首次发现路径不是最优的测试地图。
4. 为 RRT 增加边碰撞和迭代上限。
5. 固定随机种子并统计成功率、节点数和路径长度。
6. 最后再迁移到统一地图和算法接口。

### 与 chhRobotics_CPP 的学习关系

planning_algorithm 只展示最小 A* 与 RRT；chhRobotics_CPP 进一步提供 Dijkstra、A*、DWA、RRT/RRT-Connect/RRT*、曲线规划和多种跟踪控制。推荐先用本仓库看动画，再到后者比较更完整的算法族，但两者都需要独立验证正确性。

## 疑问与冲突

- README 的算法分类表是否代表未来规划，仓库没有 roadmap 说明。
- A* 文档与代码在 open-set 更新行为上不一致。
- RRT 的目标节点没有真正连接到搜索树。
- 仓库没有许可证，复用前需要取得授权。

## 原料

- `raw/2026-06-15-planning-algorithm-repository-snapshot.md`
