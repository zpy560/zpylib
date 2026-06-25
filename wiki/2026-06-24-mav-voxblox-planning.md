---
id: "20260624-211008-mav-voxblox-planning-wiki"
title: "mav_voxblox_planning"
type: "entity"
source: "notes/2026-06-24-mav-voxblox-planning-esdf-mav-planners.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-mav-voxblox-planning-esdf-mav-planners.md
---

# mav_voxblox_planning

## 定位

`mav_voxblox_planning` 是基于 Voxblox ESDF 地图的 MAV 规划工具集合，覆盖全局规划、骨架图规划、轨迹平滑、局部优化和在线重规划。

## 适合研究的问题

- ESDF 如何服务碰撞代价和局部轨迹优化。
- 全局采样规划与局部 polynomial/loco 规划如何衔接。
- MAV planner 如何向控制器输出 timed dynamically feasible trajectories。

## 使用边界

README 标注开发中，接口可能变化。它适合研究和对照，不应未经验证直接作为产品级飞行规划模块。

## 入库来源

- 单源笔记：../notes/2026-06-24-mav-voxblox-planning-esdf-mav-planners.md
- 仓库：https://github.com/ethz-asl/mav_voxblox_planning

