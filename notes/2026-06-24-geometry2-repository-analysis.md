---
id: "20260624-212226-geometry2-note"
title: "geometry2 / tf2：ROS 2 TF2 坐标变换库集合"
type: "note"
source: "raw/2026-06-24-geometry2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-geometry2.md
---

# geometry2 / tf2：ROS 2 TF2 坐标变换库集合

## 结论

geometry2 / tf2 值得加入控制/规划知识库。适合机器人规划控制中的 frame transform、tf2 buffer 和坐标系统管理。

## 事实摘录

- 远端仓库：`ros2/geometry2`
- 当前核对 HEAD：`18314a09598acf22accd3e083ec705edd9519f76`
- 根 README 不存在；远端 refs 显示 rolling/humble 分支。按 ROS 2 生态定位，geometry2 是 tf2、tf2_ros 等坐标变换包集合。

## 对规划控制的意义

- 可作为 ROS 2 TF2 坐标变换库集合 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
