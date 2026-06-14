---
id: "20260614-autoware-ros2-autonomous-driving-platform"
title: "Autoware：ROS 2 原生的模块化自动驾驶平台"
type: "note"
source: "raw/2026-06-14-autoware-repository-snapshot.md"
created_at: "2026-06-14"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-14-autoware.md
  - notes/2026-06-14-apollo-autonomous-driving-platform.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
---

# Autoware：ROS 2 原生的模块化自动驾驶平台

## 一句话结论

Autoware 以 ROS 2 包、组件容器、Topic 和 launch 配置拼装完整自动驾驶系统：规则规划将路径行为、交通规则和运动速度模块分层插件化，控制链将轨迹跟随、命令门控、运行模式和独立检查器串联；开放组合能力很强，但系统正确性高度依赖版本清单和部署配置的一致性。

## 原文要点

### 主仓库是版本化装配入口

`autoware` 是元仓库，通过清单固定 Core、Universe、Launch、消息、传感器和外部依赖。完整分析必须沿清单读取实际版本源码和 launch。

Core 约含 70 个 ROS 包，Universe 约含 240 个 ROS 包。前者偏基础能力，后者承载更广泛的应用与算法模块。

### 规划是多条插件流水线

```text
Mission Planning
→ Scenario Selector
→ Lane Driving / Parking
→ Planning Validator
→ /planning/trajectory
```

Lane Driving 继续拆为 Behavior Path Planning、Behavior Velocity Planning、Path Smoothing/Optimization、Motion Velocity Planning 和 Velocity Smoothing。

路径行为插件处理起步、到达、绕障、侧移和换道；速度行为插件处理路口、交通灯、人行横道、盲区和停止规则；运动速度插件处理障碍物停车、减速、巡航和道路边界约束。

规划入口也支持 Diffusion Planner。它与规则规划共用后置轨迹验证出口，学习型规划没有绕过既有输出契约。

### 控制采用跟随器、门控和检查器分层

```text
/planning/trajectory
→ Trajectory Follower
→ Shift Decider
→ Command Gate
→ Vehicle Interface
```

轨迹跟随器默认使用横向 MPC 和纵向 PID，也支持 Pure Pursuit 横向控制。命令门控在自动、外部和紧急命令间选择，并结合 MRM、心跳和运行模式。

控制器之外还有车道偏离、控制验证、AEB、碰撞检测和模式切换等独立模块。`vehicle_cmd_gate` 与新 `control_command_gate` 处于迁移阶段，真实命令链要以目标车型 launch 参数为准。

## 我的判断

### 最大价值是 ROS 2 原生的系统级可替换性

Autoware 不只把算法做成插件，还把进程组合、Topic、车辆模型、传感器模型、参数和功能开关暴露在 launch 层。它适合研究多团队如何在统一消息和运行框架下并行开发自动驾驶模块。

代价是配置本身成为架构的一部分。评审时必须同时检查：

1. `autoware.repos` 固定的真实版本。
2. 顶层与子系统 launch 的 include 和条件开关。
3. Topic remap、参数文件与车辆/传感器模型。
4. 组件容器和实际启用的检查器。

### Core 与 Universe 是稳定性边界

从包规模、清单和 launch 依赖看，Core 更接近稳定基础层，Universe 更接近快速扩展的功能层。这有利于控制基础接口变化，但跨层组合仍需整体验证。

### 安全能力应按执行命令路径审计

Planning Validator、Control Validator、AEB、Collision Detector、Command Gate 和 MRM 只能证明系统具备候选机制，不能证明目标部署已经启用、输入完整或参数正确。

安全评审应从 Vehicle Interface 反向追踪最终命令来源，确认门控模式、紧急命令、检查器诊断和 MRM 状态是否真正接入。

### 与 Apollo、Navigation2 的位置不同

| 维度 | Autoware | Apollo | Navigation2 |
|---|---|---|---|
| 运行基础 | ROS 2 组件与 Topic | Cyber RT | ROS 2 Server/Action |
| 规划组织 | 多阶段插件流水线 | Scenario/Stage/Task | Behavior Tree |
| 主要领域 | 开放道路自动驾驶 | 开放道路自动驾驶 | 移动机器人导航 |
| 组合中心 | launch、参数、remap | DAG、配置、插件 | BT、Lifecycle、插件 |
| 末端约束 | Validator、Gate、AEB、MRM | Control、Guardian、Canbus | Smoother、Collision Monitor |

Apollo 的业务状态机边界更集中；Autoware 的能力更分布式、更贴近 ROS 2 生态；Navigation2 的任务编排和恢复机制更显式，但道路语义与车辆动力学覆盖更弱。

## 可复用内容

### 评审顺序

1. 固定主仓库提交和 manifest 中的组件版本。
2. 从顶层 launch 确认规划与控制模式。
3. 展开 include、条件开关、参数和 Topic remap。
4. 追踪 `/planning/trajectory` 到最终车辆命令。
5. 检查 Validator、Gate、AEB、Collision Detector 与 MRM 的真实接线。
6. 最后评审算法实现和参数性能。

## 疑问与冲突

- `control_command_gate` 迁移完成后的最终命令链和兼容周期需要继续跟踪。
- Diffusion Planner 的启用条件、性能和验证边界需要运行数据支撑。
- Agnocast 与标准 ROS 2 通信的延迟和部署取舍需要实测。
- 本次未编译、回放或运行仿真，实时性、参数有效性和组件兼容性不在结论范围内。

## 原料

- `raw/2026-06-14-autoware-repository-snapshot.md`
