---
id: "20260624-teb-local-planner-timed-elastic-band"
title: "teb_local_planner：Timed Elastic Band 局部规划器"
type: "note"
source: "raw/2026-06-24-teb-local-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-teb-local-planner.md
  - notes/2026-06-24-mpc-local-planner-ros-local-mpc.md
---

# teb_local_planner：Timed Elastic Band 局部规划器

## 一句话结论

teb_local_planner 是 ROS 生态中经典的 Timed Elastic Band 局部轨迹规划器，适合研究局部轨迹优化、障碍约束和时间维度约束；它不是全局规划器，也不是完整导航系统。

## 原文要点

- README 标题为 `teb_local_planner ROS Package`。
- 仓库来自 rst-tu-dortmund。
- 当前远端 HEAD 为 `8f42953`。

## 我的判断

TEB 的价值在把几何路径和时间维度一起优化，是局部规划与速度规划之间的重要参考。它适合和 mpc_local_planner、Nav2 controller 体系对照。

## 可复用内容

- Timed Elastic Band 局部轨迹优化思想。
- 障碍物、时间和运动约束联合处理。
- ROS local planner 插件形态参考。

## 疑问与冲突

- ROS1 生态历史项目，迁移到 ROS2/Nav2 需重新评估。
- 局部优化不等于全局最优和系统安全。

## 原料

- `raw/2026-06-24-teb-local-planner-repository-snapshot.md`

