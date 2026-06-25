---
id: "20260624-211004-elevation-mapping-wiki"
title: "elevation_mapping"
type: "entity"
source: "notes/2026-06-24-elevation-mapping-robot-centric-terrain-map.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-elevation-mapping-robot-centric-terrain-map.md
---

# elevation_mapping

## 定位

`elevation_mapping` 是机器人中心局部高程地图 ROS 包，用于把距离传感器和位姿估计融合为可供导航使用的地形地图。

## 适合研究的问题

- 局部地形地图如何随机器人移动维护。
- 位姿漂移和不确定性如何进入高程地图。
- 高程地图如何服务 rough-terrain navigation。

## 使用边界

README 声明项目已不再活跃维护。它适合方法学习和历史工程参考，不适合不经评估直接作为新项目核心依赖。

## 入库来源

- 单源笔记：../notes/2026-06-24-elevation-mapping-robot-centric-terrain-map.md
- 仓库：https://github.com/ANYbotics/elevation_mapping

