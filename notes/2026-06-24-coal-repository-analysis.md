---
id: "20260624-212205-coal-note"
title: "Coal：FCL/HPP-FCL 演进版碰撞库"
type: "note"
source: "raw/2026-06-24-coal-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-coal.md
---

# Coal：FCL/HPP-FCL 演进版碰撞库

## 结论

Coal 值得加入控制/规划知识库。适合机器人规划中的高性能碰撞检测、距离下界、接触点和 Python 原型。

## 事实摘录

- 远端仓库：`coal-library/coal`
- 当前核对 HEAD：`c0837af2f0024de9de29f9be3de57f9bf31fe7bb`
- README 说明 HPP-FCL 于 2024 更名为 Coal，并引入 GJK/EPA、安全裕度、Nesterov 加速、Python bindings、height fields 等特性。

## 对规划控制的意义

- 可作为 FCL/HPP-FCL 演进版碰撞库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
