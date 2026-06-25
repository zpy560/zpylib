---
id: "20260624-210020-descartes-wiki"
title: "Descartes"
type: "entity"
source: "notes/2026-06-24-descartes-cartesian-path-planner.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-descartes-cartesian-path-planner.md
---

# Descartes

## 定位

Descartes 是 ROS-Industrial 的 Cartesian Path Planner，面向机械臂末端沿笛卡尔路径运动的工业规划问题。

## 适合研究的问题

- 末端路径点如何转为一组可行关节解。
- 工艺轨迹约束如何和碰撞、可达性、冗余自由度结合。
- Cartesian process planning 与通用 motion planning 的边界。

## 使用边界

根 README 信息很少，不足以支撑完整判断。后续使用时应进入 ROS wiki 和源码示例验证接口、维护状态和适配 ROS 版本。

## 入库来源

- 单源笔记：../notes/2026-06-24-descartes-cartesian-path-planner.md
- 仓库：https://github.com/ros-industrial-consortium/descartes

