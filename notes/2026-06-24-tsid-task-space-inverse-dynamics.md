---
id: "20260624-211015-tsid-note"
title: "TSID：任务空间逆动力学控制"
type: "note"
source: "raw/2026-06-24-tsid-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-tsid.md
---

# TSID：任务空间逆动力学控制

## 结论

TSID 是机器人控制链中值得重点保留的库。它不做路径规划，而是解决“规划给出的任务目标如何在动力学约束下转成控制命令”的问题，适合和 Pinocchio、Crocoddyl、OCS2、mc_rtc 对照阅读。

## 事实摘录

- 远端仓库：`stack-of-tasks/tsid`
- 当前核对 HEAD：`3565562ce608dc8be69c0bec294ebb25507527af`
- README 定位：optimization-based inverse-dynamics control C++ library。
- 基于 Pinocchio。
- 示例覆盖 manipulators、humanoids、quadrupeds。
- 依赖包括 Eigen3、Pinocchio、eiquadprog。

## 对规划控制的意义

- 对全身控制：TSID 提供任务层级和动力学约束下的控制求解思路。
- 对移动操作/足式机器人：规划层输出不能直接执行，需要 inverse dynamics 或 whole-body control 承接。
- 对学习路线：先看任务定义、约束、QP 组装，再看具体机器人示例。

## 使用建议

不要把 TSID 和轨迹优化库混为一谈。它更接近控制执行层，可与 Crocoddyl/OCS2 的轨迹优化输出衔接。

