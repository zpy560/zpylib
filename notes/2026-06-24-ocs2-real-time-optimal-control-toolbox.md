---
id: "20260624-ocs2-real-time-optimal-control-toolbox"
title: "OCS2：机器人实时最优控制工具箱"
type: "note"
source: "raw/2026-06-24-ocs2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-ocs2.md
  - notes/2026-06-24-acados-real-time-nmpc-solver.md
  - notes/2026-06-24-casadi-symbolic-optimization-framework.md
---

# OCS2：机器人实时最优控制工具箱

## 一句话结论

OCS2 是面向机器人实时 MPC 的 C++ 最优控制工具箱，覆盖 switched systems、DDP/iLQR/SQP/IPM、多种约束处理、自动微分和 ROS 接口；适合研究动态机器人控制，不是通用导航框架。

## 原文要点

- README 定位为 Optimal Control for Switched Systems。
- 强调 nonlinear optimal control 和 real-time MPC for robotics。
- 求解器包括 SLQ、iLQR、SQP、SLP、IPM。
- 支持 mode schedule、jump map、Augmented Lagrangian、relaxed barrier、CppAD、Pinocchio、URDF、ROS 接口。
- ROS 2 port 在 `ros2` 分支，`main` 是 ROS 1。

## 我的判断

OCS2 和 acados 都属于实时最优控制方向，但 OCS2 更强调机器人系统建模、switched systems 和 ROS/Pinocchio 工具链。它适合腿式、飞行器、移动操作臂等复杂动力学控制参考。

## 可复用内容

- 实时 MPC 系统组织方式。
- DDP/iLQR/SQP/IPM 多求解器框架。
- Pinocchio/URDF 到最优控制问题的建模链路。

## 疑问与冲突

- ROS 1/ROS 2 分支分离，使用时必须确认目标分支。
- 复杂机器人模型下调参、数值稳定和实时性仍需实验验证。

## 原料

- `raw/2026-06-24-ocs2-repository-snapshot.md`

