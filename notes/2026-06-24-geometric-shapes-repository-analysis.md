---
id: "20260624-212227-geometric-shapes-note"
title: "geometric_shapes：几何形状和 body 操作库"
type: "note"
source: "raw/2026-06-24-geometric-shapes-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-geometric-shapes.md
---

# geometric_shapes：几何形状和 body 操作库

## 结论

geometric_shapes 值得加入控制/规划知识库。适合 MoveIt/碰撞检测中的 primitive、mesh、point containment 和 ray intersection。

## 事实摘录

- 远端仓库：`ros-planning/geometric_shapes`
- 当前核对 HEAD：`071a9ef2391722e6f99a44ba32e741cd39f831a2`
- README 定位为 generic definitions of geometric shapes and bodies，以及 shape messages 操作工具；支持 sphere、box、cone、cylinder、mesh。

## 对规划控制的意义

- 可作为 几何形状和 body 操作库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
