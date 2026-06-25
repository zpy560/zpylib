---
id: "20260624-211007-mav-voxblox-planning-note"
title: "mav_voxblox_planning：基于 ESDF 的 MAV 全局与局部规划"
type: "note"
source: "raw/2026-06-24-mav-voxblox-planning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-mav-voxblox-planning.md
---

# mav_voxblox_planning：基于 ESDF 的 MAV 全局与局部规划

## 结论

`mav_voxblox_planning` 应和 Voxblox 成对入库。Voxblox 负责 TSDF/ESDF 地图，这个仓库负责把 ESDF 接入 MAV 的全局搜索、骨架规划、局部优化、平滑和在线重规划。

## 事实摘录

- 远端仓库：`ethz-asl/mav_voxblox_planning`
- 当前核对 HEAD：`a90260baaa07cd046847d7a237ab17e2947dbce7`
- README 定位：MAV planning tools using Voxblox as map representation。
- 包含 OMPL 全局规划、skeleton sparse graph、path smoothing、local polynomial optimization、local planning 和 RViz planning plugin。
- local planner 会向 MAV controller 发送 timed、dynamically feasible trajectories，并支持 online replanning。

## 对规划控制的意义

- 展示 ESDF 地图如何真正进入 planner 和 trajectory optimizer。
- 覆盖从 global route 到 local collision-aware trajectory 的链路。
- 对四旋翼规划，比只看 RRT 或 polynomial trajectory generation 更接近完整研究系统。

## 使用建议

先读 `voxblox_rrt_planner`、`voxblox_skeleton_planner`、`voxblox_loco_planner`、`mav_local_planner`。如果目标是现代无人机规划，应再对照 Fast-Planner、EGO-Planner 和 EGO-Swarm。

