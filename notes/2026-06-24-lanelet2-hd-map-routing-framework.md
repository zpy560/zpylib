---
id: "20260624-210007-lanelet2-note"
title: "Lanelet2：自动驾驶 HD Map 与路由基础设施"
type: "note"
source: "raw/2026-06-24-lanelet2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-lanelet2.md
---

# Lanelet2：自动驾驶 HD Map 与路由基础设施

## 结论

Lanelet2 是自动驾驶规划链里的地图与路由底座，不是行为决策器。它值得入库，因为车道级规划、交通规则约束、route graph、局部坐标投影和地图 IO 都会影响上层 planner 的设计边界。

## 事实摘录

- 远端仓库：`fzi-forschungszentrum-informatik/Lanelet2`
- 当前核对 HEAD：`ae39c8d673264afac2339c4f0252df53a7ba82dd`
- README 定位：用于 automated driving map data 的 C++ library。
- 支持 2D/3D、lane changes、area routing、不同交通参与者的 separated routing、自定义 traffic rules/routing costs、Python bindings。
- README 声明支持 ROS1、ROS2、Docker、Conan。

## 对规划控制的意义

- 对行为规划：提供路由、车道关系、交通规则和可行区域语义。
- 对路径规划：提供从 HD map 到局部参考线/可行走廊的几何和拓扑基础。
- 对工程集成：ROS1/ROS2 支持使它适合在 Autoware、Apollo 对照学习中作为地图模型参考。

## 使用建议

优先看 `lanelet2_core`、`lanelet2_routing`、`lanelet2_traffic_rules`、`lanelet2_projection`。如果只是做栅格路径规划，Lanelet2 不是最短路径；如果做道路结构内的自动驾驶规划，它是应长期保留的基础资料。

