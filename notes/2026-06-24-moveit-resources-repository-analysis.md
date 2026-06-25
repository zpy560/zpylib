---
id: "20260624-212228-moveit-resources-note"
title: "moveit_resources：MoveIt 测试机器人与配置资源"
type: "note"
source: "raw/2026-06-24-moveit-resources-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-moveit-resources.md
---

# moveit_resources：MoveIt 测试机器人与配置资源

## 结论

moveit_resources 值得加入控制/规划知识库。适合 MoveIt/规划测试中的 URDF、meshes、moveit_config 基准资源。

## 事实摘录

- 远端仓库：`moveit/moveit_resources`
- 当前核对 HEAD：`647bbf84846f2846f1b254beb55e9a72ea9ada01`
- README 说明仓库包含 MoveIt 测试所需 URDFs、meshes、moveit_config packages，机器人包括 PR2、Fanuc、Panda。

## 对规划控制的意义

- 可作为 MoveIt 测试机器人与配置资源 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
