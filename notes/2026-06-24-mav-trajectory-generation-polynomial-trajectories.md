---
id: "20260624-mav-trajectory-generation-polynomial-trajectories"
title: "mav_trajectory_generation：MAV 多项式轨迹生成与优化"
type: "note"
source: "raw/2026-06-24-mav-trajectory-generation-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-mav-trajectory-generation.md
  - notes/2026-06-24-fast-planner-quadrotor-fast-flight-planning.md
---

# mav_trajectory_generation：MAV 多项式轨迹生成与优化

## 一句话结论

mav_trajectory_generation 是 ETH ASL 的 MAV 多项式轨迹生成和优化工具，适合把航点/约束转成平滑可执行轨迹；它不是感知、避障或任务规划框架。

## 原文要点

- README 明确包含 polynomial trajectory generation and optimization tools。
- 特别适合 rotary-wing MAVs。
- 主要参考 aggressive quadrotor flight 的 polynomial trajectory planning。
- ROS catkin 安装流程面向 Indigo/Kinetic/Melodic。

## 我的判断

它补的是无人机规划链中的轨迹生成层：上游需要给出目标点、约束或路径，工具负责生成多项式轨迹。适合和 Fast-Planner、EGO-Planner 对照。

## 可复用内容

- 多项式轨迹生成。
- MAV 轨迹优化和约束表达。
- ROS1 轨迹生成工具包组织。

## 疑问与冲突

- ROS 版本偏旧。
- 不处理完整动态避障闭环。

## 原料

- `raw/2026-06-24-mav-trajectory-generation-repository-snapshot.md`

