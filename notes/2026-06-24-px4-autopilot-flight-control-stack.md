---
id: "20260624-px4-autopilot-flight-control-stack"
title: "PX4 Autopilot：无人系统飞控与控制栈"
type: "note"
source: "raw/2026-06-24-px4-autopilot-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-px4-autopilot.md
  - notes/2026-06-24-rpg-quadrotor-control-aggressive-flight.md
---

# PX4 Autopilot：无人系统飞控与控制栈

## 一句话结论

PX4 是无人机和无人系统飞控栈，价值在模块化飞控架构、传感器/执行器接口、控制环、仿真测试和 MAVLink/ROS 2 集成；它不是单独的路径规划算法库。

## 原文要点

- README 称 PX4 是 open-source autopilot stack for drones and unmanned vehicles。
- 支持多旋翼、固定翼、VTOL、rover 等平台。
- 运行在 NuttX、Linux、macOS。
- 架构使用 uORB 和 DDS-compatible pub/sub。
- 支持 MAVLink、DDS/ROS 2、SITL、HIL、log analysis。
- BSD 3-Clause 许可证，Dronecode Foundation 托管。

## 我的判断

PX4 是飞行控制系统级参考。和 RPG Quadrotor Control 不同，PX4 更接近生产级飞控生态；和 Fast-Planner/EGO-Planner 不同，PX4 更靠近状态估计、控制和硬件执行。

## 可复用内容

- 飞控模块化架构。
- uORB/DDS/MAVLink 通信边界。
- SITL/HIL 和日志分析工程链。
- 多平台飞行器控制栈组织。

## 疑问与冲突

- 体量大，不能只看 README 判断具体控制器实现。
- 和上层自主规划系统的边界需按 MAVLink/ROS 2 接口确认。

## 原料

- `raw/2026-06-24-px4-autopilot-repository-snapshot.md`

