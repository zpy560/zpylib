---
id: "20260624-210011-karlkurzer-path-planner-note"
title: "karlkurzer/path_planner：实时 Hybrid A* 车辆路径规划"
type: "note"
source: "raw/2026-06-24-karlkurzer-path-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-karlkurzer-path-planner.md
---

# karlkurzer/path_planner：实时 Hybrid A* 车辆路径规划

## 结论

`karlkurzer/path_planner` 是适合长期保留的 Hybrid A* 实现参考。它比教学伪代码更接近车辆工程问题，又比 Apollo/Autoware 这类大系统更容易单独阅读。

## 事实摘录

- 远端仓库：`karlkurzer/path_planner`
- 当前核对 HEAD：`ddf1a3afcafc323ef44d5e49d5cbb7b3c3f53665`
- README 定位：KTH Research Concept Vehicle 的 Hybrid A* Path Planner。
- 使用二值障碍地图作为输入，配合 ROS 与 RViz。
- 特征包括 72 headings per cell、5 degree discretization、constrained heuristic、unconstrained heuristic、Dubins shot 和约 10 Hz C++ 实现。

## 对规划控制的意义

- 适合研究非完整车辆在停车场、施工区域等无结构场景中的状态格搜索。
- 可用于理解 Hybrid A* 中连续状态、离散航向、解析扩展和启发函数之间的关系。
- 与本库已入库的 `Hybrid A Star` 可以互相对照：一个偏 ROS1 工程实现，一个偏算法正确性检查。

## 使用建议

先读节点入口、地图输入、Node3D/Node2D、heuristic 和 collision checking。不要直接把 2016 年研究代码当成现代量产 planner；如果要工程化，应补充动态障碍、轨迹后处理、速度规划和系统级安全边界。

