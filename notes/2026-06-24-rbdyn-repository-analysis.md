---
id: "20260624-212219-rbdyn-note"
title: "RBDyn：刚体系统动力学建模库"
type: "note"
source: "raw/2026-06-24-rbdyn-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-rbdyn.md
---

# RBDyn：刚体系统动力学建模库

## 结论

RBDyn 值得加入控制/规划知识库。适合 mc_rtc/Tasks 控制链中的 rigid body dynamics 模型基础。

## 事实摘录

- 远端仓库：`jrl-umi3218/RBDyn`
- 当前核对 HEAD：`e28c807f26346ccaabd877e70bdcb4a9386660aa`
- README 描述 RBDyn provides classes and functions to model dynamics of rigid body systems，基于 Featherstone rigid body dynamics algorithms。

## 对规划控制的意义

- 可作为 刚体系统动力学建模库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
