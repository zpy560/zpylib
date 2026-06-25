---
id: "20260624-212208-orocos-kdl-note"
title: "Orocos KDL：实时可用运动学与动力学库"
type: "note"
source: "raw/2026-06-24-orocos-kdl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-orocos-kdl.md
---

# Orocos KDL：实时可用运动学与动力学库

## 结论

Orocos KDL 值得加入控制/规划知识库。适合机器人正逆运动学、运动链建模和 ROS 机器人基础设施。

## 事实摘录

- 远端仓库：`orocos/orocos_kinematics_dynamics`
- 当前核对 HEAD：`5c787496c9c57460c0eb076f300afd8ac7412f68`
- README 定位为 RealTime usable kinematics and dynamics code，包含 rigid body kinematics、kinematic structures、inverse/forward kinematic solvers。

## 对规划控制的意义

- 可作为 实时可用运动学与动力学库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
