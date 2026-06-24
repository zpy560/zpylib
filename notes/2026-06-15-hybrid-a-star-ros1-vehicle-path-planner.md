---
id: "20260615-hybrid-a-star-ros1-vehicle-path-planner"
title: "Hybrid A Star：ROS1 车辆三维状态栅格路径搜索实现"
type: "note"
source: "raw/2026-06-15-hybrid-a-star-repository-snapshot.md"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
related:
  - wiki/2026-06-15-hybrid-a-star.md
  - notes/2026-06-24-motionplanning-autonomous-driving-planning-control-demos.md
  - notes/2026-06-14-ros-motion-planning-algorithm-workbench.md
---

# Hybrid A Star：ROS1 车辆三维状态栅格路径搜索实现

## 一句话结论

该仓库完整展示了 Hybrid A* 的关键骨架：在 `(x, y, yaw)` 状态栅格上使用前后向车辆运动原语搜索，以转向、倒车和转角变化构造代价，并用 Reeds-Shepp 距离与解析扩展加速近终点连接；但地图初始化、启发式计算、open-set 更新、自定义地图边界和车体碰撞均存在明确实现问题，适合源码学习与修复实验，不应直接用于泊车或自动驾驶规划。

## 原文要点

### 为什么不是普通 A*

普通栅格 A* 的节点通常只有 `(x, y)`，邻居是上下左右或八方向栅格。Hybrid A* 的节点加入航向角，邻居由运动学自行车模型、离散转角和前后方向生成。这保证搜索路径在离散步长意义上满足车辆非完整约束，特别适合窄空间掉头和泊车。

### 搜索组成

```text
连续车辆状态
→ 离散到 x/y/yaw 状态栅格
→ 生成转向角 × 前后方向运动原语
→ 原语内部逐步车体碰撞检测
→ 累计转向、倒车和转角变化代价
→ L1 / Reeds-Shepp 启发式
→ 近目标 Reeds-Shepp analytic shot
→ 父节点回溯并拼接中间状态
```

默认航向分成 72 个区间。每个运动原语保留内部连续采样状态，因此最终路径比状态栅格中心序列更细。

### Reeds-Shepp 的双重作用

Reeds-Shepp 曲线允许车辆前进和倒车，是泊车场景常用的无障碍最短曲线模型。本仓库将它用于估计近终点剩余代价和在 shot distance 内直接连接目标。解析连接只有在整条离散曲线通过车体碰撞检查时才接受。

### ROS1 交互外壳

项目通过 `map_server`、OccupancyGrid、RViz 起终点工具和 Marker/Path 发布器提供完整演示链。用户可以切换迷宫、泊车场、空地图和障碍地图观察搜索树。

## 我的判断

### 最值得学习的是 Hybrid A* 的最小工程闭环

该项目比只给算法函数的示例多了 OccupancyGrid 坐标转换、车辆矩形包络、连续运动原语碰撞检查、前进/倒车与换向代价、解析扩展和搜索树可视化。这些正是从二维 A* 过渡到车辆路径规划时最容易遗漏的部分。

### 但它不是论文的完整工程复现

Dolgov 等人的实践方案通常还结合二维动态规划启发式、非完整约束启发式、更系统的障碍代价和后端平滑优化。本仓库远距离只使用 L1，近距离使用 Reeds-Shepp；轨迹优化器没有接入主流程。因此更准确的定位是“Hybrid A* 核心前端复现”。

### 当前代码存在搜索正确性风险

以下问题由源码直接确认：

1. 障碍地图数组未初始化，自由空间值不确定。
2. 所有邻居使用当前节点的启发式，而非各自启发式。
3. open set 中状态降代价时没有重新插入优先队列。
4. 自定义地图上界遗漏 origin 偏移。
5. 障碍索引边界允许 `x == width` 或 `y == height`。
6. 车体碰撞只检查矩形四边，可能漏掉内部障碍。

其中前四项足以改变搜索可达性、展开顺序或地图坐标，不只是性能问题。

### 路径可行不等于可执行

搜索只约束几何运动学和静态占用，不包含曲率变化率、方向盘速度、速度、加速度、jerk、动态障碍、定位不确定性、控制跟踪误差或档位切换时间。输出还需要方向分段、平滑、速度规划和闭环控制验证。

## 可复用内容

### 推荐阅读顺序

1. `state_node.h`：状态、方向和父节点。
2. `DynamicModel()`：车辆运动原语。
3. `GetNeighborNodes()`：转角和前后向展开。
4. `ComputeG()`：驾驶行为惩罚。
5. `ComputeH()`：两类启发式。
6. `RSPath`：解析距离和连接。
7. `CheckCollision()`：车辆包络映射。
8. `Search()`：open/closed 状态更新。
9. `hybrid_a_star_flow.cpp`：ROS 地图和可视化。

### 修复优先级

1. 对地图数组显式清零。
2. 为每个邻居计算启发式。
3. 正确实现 decrease-key，或插入新条目并跳过过期条目。
4. 修复地图上界为 `origin + size * resolution`。
5. 将障碍索引判断改为 `>=`。
6. 使用填充多边形、footprint 或距离场检查车体内部。
7. 为起终点增加边界和完整 footprint 校验。
8. 为 Reeds-Shepp、坐标转换和状态更新添加单元测试。

### 工程化验证场景

- 空地图不同姿态连接。
- 单障碍绕行。
- 窄通道与死胡同倒车。
- 平行泊车与垂直泊车。
- 非零及负地图原点。
- 障碍完全位于车辆内部。
- 起点或终点与障碍相交。
- 同一状态被更低代价路径重新发现。
- 解析连接碰撞和搜索超时。

## 疑问与冲突

- README 声称速度和效果接近论文，但没有可重复 benchmark。
- 最后提交标题为支持自定义地图，但非零 origin 的边界计算仍不正确。
- `trajectory_optimizer.h` 是否曾在其他分支接入，当前默认分支看不到调用。
- ROS Melodic 之外的 ROS1 版本兼容性没有 CI 证明。

## 原料

- `raw/2026-06-15-hybrid-a-star-repository-snapshot.md`
