---
id: "20260624-212215-teach-repeat-replan-note"
title: "Teach-Repeat-Replan：无人机 teach-repeat-replan 竞速系统"
type: "note"
source: "raw/2026-06-24-teach-repeat-replan-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-teach-repeat-replan.md
---

# Teach-Repeat-Replan：无人机 teach-repeat-replan 竞速系统

## 结论

Teach-Repeat-Replan 值得加入控制/规划知识库。适合 aggressive flight 中示教轨迹平滑、安全重复和局部重规划研究。

## 事实摘录

- 远端仓库：`HKUST-Aerial-Robotics/Teach-Repeat-Replan`
- 当前核对 HEAD：`98505a7f74b13c8b501176ff838a38423dbef536`
- README 定位为 complete and robust system for Autonomous Drone Race，可把 jerky teaching trajectory 转成 smooth safe repeating trajectory，并对未建图/动态障碍局部重规划。

## 对规划控制的意义

- 可作为 无人机 teach-repeat-replan 竞速系统 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
