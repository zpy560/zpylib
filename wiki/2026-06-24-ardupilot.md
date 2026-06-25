---
id: "20260624-210004-ardupilot-wiki"
title: "ArduPilot"
type: "entity"
source: "notes/2026-06-24-ardupilot-autopilot-control-stack.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-ardupilot-autopilot-control-stack.md
---

# ArduPilot

## 定位

ArduPilot 是多载具开源 autopilot 工程栈，覆盖飞行器、地面车、水面船、潜航器等平台。它的核心价值不是单个 planner，而是成熟控制系统的任务模式、车辆抽象、仿真测试和硬件适配体系。

## 适合研究的问题

- 飞控/车控软件如何组织 mode、mission、guidance、control 和 actuator output。
- 多载具共享基础设施时，车辆特定逻辑如何隔离。
- SITL、回放、板级构建和持续集成如何支撑控制栈长期维护。

## 不适合的用法

- 不应把它当成轻量路径规划算法示例库。
- 不应在不了解 GPL v3 影响的情况下直接嵌入闭源产品。
- 如果研究 ROS 2 移动机器人导航，应优先看 Nav2、ros2_control、ros2_controllers，再把 ArduPilot 作为无人系统控制栈对照。

## 入库来源

- 单源笔记：../notes/2026-06-24-ardupilot-autopilot-control-stack.md
- 仓库：https://github.com/ArduPilot/ardupilot

