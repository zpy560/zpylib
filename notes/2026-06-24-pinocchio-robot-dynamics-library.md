---
id: "20260624-pinocchio-robot-dynamics-library"
title: "Pinocchio：机器人运动学与动力学库"
type: "note"
source: "raw/2026-06-24-pinocchio-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-pinocchio.md
  - notes/2026-06-24-crocoddyl-robotics-optimal-control.md
---

# Pinocchio：机器人运动学与动力学库

## 一句话结论

Pinocchio 是机器人运动学和动力学计算库，是最优控制、轨迹优化和全身控制的底层基础设施；它不是规划器或控制器。

## 原文要点

- 仓库属于 stack-of-tasks 生态。
- README 提供文档、安装和项目说明。
- 当前远端 HEAD 为 `893ed4d`。

## 我的判断

Pinocchio 的价值在“模型计算层”：没有高效准确的 kinematics/dynamics，Crocoddyl、OCS2、whole-body control 等上层算法很难可靠工作。

## 可复用内容

- 机器人运动学/动力学建模。
- 最优控制中的模型和导数计算。
- 机械臂、腿式机器人、移动操作臂控制基础。

## 疑问与冲突

- 对车辆路径规划的直接价值有限。
- 使用价值取决于机器人模型和上层控制框架。

## 原料

- `raw/2026-06-24-pinocchio-repository-snapshot.md`

