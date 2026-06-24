---
id: "20260624-px4-autopilot"
title: "PX4 Autopilot"
type: "entity"
source: "raw/2026-06-24-px4-autopilot-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-px4-autopilot-flight-control-stack.md
  - wiki/2026-06-24-rpg-quadrotor-control.md
---

# PX4 Autopilot

## 基本信息

- 类型：无人系统飞控栈
- 官方仓库：https://github.com/PX4/PX4-Autopilot
- 官网：https://px4.io
- 快照分支：`main`
- 快照提交：`dc3636eed092f8f8c76a510858b3ccc34ac68448`
- 快照日期：2026-06-24

## 当前结论

PX4 是飞控系统级工程参考，适合研究飞行控制、模块通信、仿真测试和 ROS 2/MAVLink 集成。

## 核心依据

- README 明确定位为 autopilot stack。
- 支持多类无人平台。
- 使用 uORB 和 DDS-compatible pub/sub。
- 提供 MAVLink、DDS/ROS 2、SITL/HIL 和日志分析。

## 不同观点与冲突

- 作为飞控栈：优先级高。
- 作为路径规划算法库：不适用。
- 作为地面车规划控制参考：只能借鉴系统工程方法。

## 关联笔记

- `notes/2026-06-24-px4-autopilot-flight-control-stack.md`
- `wiki/2026-06-24-rpg-quadrotor-control.md`

## 待补资料

- 分析 PX4 position/attitude/rate controller 和 commander/navigator 边界。

## 更新记录

- 2026-06-24：基于 `main` 分支提交 `dc3636e` 首次建档。

