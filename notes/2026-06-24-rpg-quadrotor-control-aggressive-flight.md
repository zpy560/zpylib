---
id: "20260624-rpg-quadrotor-control-aggressive-flight"
title: "RPG Quadrotor Control：四旋翼高速轨迹跟踪控制框架"
type: "note"
source: "raw/2026-06-24-rpg-quadrotor-control-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-rpg-quadrotor-control.md
  - notes/2026-06-24-mav-trajectory-generation-polynomial-trajectories.md
---

# RPG Quadrotor Control：四旋翼高速轨迹跟踪控制框架

## 一句话结论

RPG Quadrotor Control 是四旋翼高速轨迹跟踪和控制框架，适合研究 differential flatness、thrust mixing、body-rate control 和 RotorS 仿真接口；它是研究代码，不应直接当生产飞控。

## 原文要点

- README 明确这是 ROS packages，并说明是 research code。
- 包含完整 quadrotor flying framework。
- 提供 RotorS Gazebo 接口、简单轨迹生成、手柄控制、电池电压标定和 FPV racing flight controller 通信。
- 理论来自 RA-L 2017/2018 论文和仓库内 theory document。

## 我的判断

这补的是无人机控制层：Fast-Planner/EGO-Planner 更偏规划，mav_trajectory_generation 更偏轨迹生成，而 RPG Quadrotor Control 更靠近跟踪控制和执行。

## 可复用内容

- 四旋翼高速轨迹跟踪控制。
- RotorS 仿真和真实飞控接口。
- 研究代码如何组织理论文档和工程包。

## 疑问与冲突

- README 明确声明 research code，生产使用风险高。
- 依赖 ROS/RotorS 生态，版本兼容需确认。

## 原料

- `raw/2026-06-24-rpg-quadrotor-control-repository-snapshot.md`

