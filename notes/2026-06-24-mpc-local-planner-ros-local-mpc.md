---
id: "20260624-mpc-local-planner-ros-local-mpc"
title: "mpc_local_planner：ROS 局部 MPC 规划器"
type: "note"
source: "raw/2026-06-24-mpc-local-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-mpc-local-planner.md
  - notes/2026-06-24-teb-local-planner-timed-elastic-band.md
---

# mpc_local_planner：ROS 局部 MPC 规划器

## 一句话结论

mpc_local_planner 是 ROS 局部规划中的 MPC 路线参考，适合研究预测模型、约束和局部控制融合；它不解决全局路径、行为决策和完整安全闭环。

## 原文要点

- README 标题为 `mpc_local_planner ROS Package`。
- 仓库来自 rst-tu-dortmund。
- 当前 `master` HEAD 为 `5b4e465`。

## 我的判断

和 TEB 相比，mpc_local_planner 更适合研究“局部规划即有限时域最优控制”的思路。它应该与 Nav2 MPPI、TEB、acados/OSQP 等工具链一起比较。

## 可复用内容

- ROS local planner 中的 MPC 插件化形态。
- 局部模型预测控制问题组织。
- 与 TEB 的算法边界对照。

## 疑问与冲突

- ROS1 历史生态，直接迁移需评估。
- 局部 MPC 的实时性和失败处理必须实测。

## 原料

- `raw/2026-06-24-mpc-local-planner-repository-snapshot.md`

