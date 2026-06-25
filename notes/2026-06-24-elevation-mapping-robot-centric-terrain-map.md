---
id: "20260624-211003-elevation-mapping-note"
title: "elevation_mapping：机器人中心高程地图"
type: "note"
source: "raw/2026-06-24-elevation-mapping-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-elevation-mapping.md
---

# elevation_mapping：机器人中心高程地图

## 结论

`elevation_mapping` 适合加入规划控制知识库，但它是局部地形地图输入，不是 planner。README 明确提示已不再活跃维护，因此更适合作为地形建图方法和工程接口参考，而不是新项目默认依赖。

## 事实摘录

- 远端仓库：`ANYbotics/elevation_mapping`
- 当前核对 HEAD：`f4b082c64a3e660980da53b33c7936a8f2a2ea22`
- README 定位：mobile robot 的 ROS elevation mapping package。
- 面向带 pose estimation 和 distance sensor 的本地导航任务。
- 地图围绕机器人局部维护，并显式处理位姿估计漂移带来的不确定性。
- README 声明不再活跃维护。

## 对规划控制的意义

- 高程地图是足式机器人、越野机器人和粗糙地形导航的重要 planner 输入。
- 与 `grid_map` 配合看，可以理解高程层、方差层和可通行性层如何进入局部规划。
- 对自动驾驶道路场景，它的价值主要是地形建图思想，不替代 HD map 或 costmap。

## 使用建议

用于学习时重点看传感器融合、高程更新、不确定性传播和 grid map 输出。工程选型时应评估维护状态，必要时寻找 ANYbotics/ETH 后续替代方案。

