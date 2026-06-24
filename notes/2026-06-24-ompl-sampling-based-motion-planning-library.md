---
id: "20260624-ompl-sampling-based-motion-planning-library"
title: "OMPL：采样式运动规划算法库"
type: "note"
source: "raw/2026-06-24-ompl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-ompl.md
  - notes/2026-06-24-moveit2-ros2-manipulation-motion-planning.md
---

# OMPL：采样式运动规划算法库

## 一句话结论

OMPL 是采样式运动规划的核心库，适合研究和复用 RRT、PRM、KPIECE、RRT* 等多状态空间规划器；它不是完整机器人栈，需要 MoveIt 等框架提供机器人模型、碰撞环境和执行集成。

## 原文要点

- README 定位为 open source sampling-based motion planning library。
- 提供 40 多种采样式规划算法、20 多种状态空间。
- 支持 Python/C++ 扩展规划器，C++ 扩展状态空间。
- VAMP 提供 SIMD 加速规划能力。

## 我的判断

OMPL 是规划算法库层面的必收条目。读它要关注 planner/state space/validity checker 的抽象边界，而不是期待它直接处理 ROS 系统、机械臂配置或自动驾驶任务逻辑。

## 可复用内容

- 采样式规划器选型和接口设计。
- 多状态空间建模方式。
- 作为 MoveIt 规划插件的底层算法来源。

## 疑问与冲突

- 对车辆道路规划，OMPL 只能提供通用运动规划能力；交通规则、语义地图和动态障碍预测需外部系统补齐。

## 原料

- `raw/2026-06-24-ompl-repository-snapshot.md`

