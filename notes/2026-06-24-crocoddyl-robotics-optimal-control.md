---
id: "20260624-crocoddyl-robotics-optimal-control"
title: "Crocoddyl：机器人最优控制求解库"
type: "note"
source: "raw/2026-06-24-crocoddyl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-crocoddyl.md
  - notes/2026-06-24-pinocchio-robot-dynamics-library.md
  - notes/2026-06-24-control-toolbox-optimal-control-library.md
---

# Crocoddyl：机器人最优控制求解库

## 一句话结论

Crocoddyl 是机器人最优控制求解库，适合研究 DDP/iLQR 类轨迹优化和动态系统控制；它不是路径搜索库，也不是完整 ROS 规划控制栈。

## 原文要点

- 仓库属于 loco-3d 生态。
- README 提供项目使用和文档入口。
- 远端 HEAD 观察为 `da3d180`。

## 我的判断

Crocoddyl 应和 Pinocchio 一起看：一个偏最优控制问题求解，一个偏机器人动力学建模。它对腿式机器人、机械臂等动态系统轨迹优化有直接参考价值。

## 可复用内容

- DDP/iLQR 类最优控制架构。
- 动力学模型与 cost/residual/action model 的组织思路。
- 与机器人动力学库协同的控制问题建模方式。

## 疑问与冲突

- 对初学者不如 PythonRobotics/do-mpc 直观。
- 工程部署需要额外处理实时性、状态估计和执行接口。

## 原料

- `raw/2026-06-24-crocoddyl-repository-snapshot.md`

