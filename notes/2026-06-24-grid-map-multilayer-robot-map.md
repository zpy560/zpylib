---
id: "20260624-210031-grid-map-note"
title: "grid_map：多层二维/2.5D 机器人栅格地图"
type: "note"
source: "raw/2026-06-24-grid-map-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-grid-map.md
---

# grid_map：多层二维/2.5D 机器人栅格地图

## 结论

`grid_map` 是规划地图表达的重要基础库。它不直接做路径搜索或控制，但能把 elevation、variance、friction、foothold quality、surface normal、traversability 等多层信息组织成 planner 可消费的数据结构。

## 事实摘录

- 远端仓库：`ANYbotics/grid_map`
- 当前核对 HEAD：`515e3d815296635ac2420dd8d6a0350e0bdc4ab4`
- README 定位：C++ library with ROS interface for two-dimensional grid maps with multiple data layers。
- 数据层示例包括 elevation、variance、color、friction coefficient、foothold quality、surface normal、traversability。
- 特性包括 circular buffer、Eigen 数据存储、ROS message 转换、OpenCV 接口、RViz 可视化和 filter chain。

## 对规划控制的意义

- 对移动机器人：可作为 cost/traversability map 的中间表示。
- 对足式机器人：foothold quality、surface normal、elevation 等层直接影响落足和局部规划。
- 对自动驾驶：可借鉴多层地图表达，但道路场景还需要语义地图、车道规则和动态障碍层。

## 使用建议

把它和 elevation mapping、costmap、terrain traversability planner 一起读。不要把 `grid_map` 当 planner，它更接近 planner 的地图输入层和代价构造层。

