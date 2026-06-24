---
id: "20260624-youngtimes-algorithms"
title: "YoungTimes Algorithms"
type: "entity"
source: "raw/2026-06-24-youngtimes-algorithms-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - autonomous-driving
  - programming
related:
  - notes/2026-06-24-youngtimes-algorithms-planning-demos.md
  - wiki/2026-06-15-cpprobotics.md
---

# YoungTimes Algorithms

## 基本信息

- 类型：车辆规划控制算法示例集合
- 官方仓库：https://github.com/YoungTimes/algorithms
- 主要语言：Python
- 快照分支：`main`
- 快照提交：`35bb6aac1e5fec962efce8e280d1281c9bf18f8e`
- 快照日期：2026-06-24
- 许可证：GitHub 未检测到

## 当前结论

YoungTimes/algorithms 可作为 Frenet、离散点平滑、MPC 和 spiral path generation 的零散源码参考，但缺少根 README、许可证和统一工程说明，不适合作为直接依赖库。

## 核心依据

- 仓库文件树包含 `Frenet_planning`、`Frenet&Cartesian`、`discretized_points_smoothing`、`mpc` 和 `spiral`。
- `Frenet_planning` 覆盖 following、stopping、velocity keeping 轨迹场景。
- 平滑模块包含 FEM position deviation 的 OSQP 接口。
- 仓库内包含第三方 OSQP 二进制库和已构建可执行文件。
- 根 README 在 `main` 分支不可用。

## 不同观点与冲突

- 作为学习片段：有价值，覆盖多个规划控制基础模块。
- 作为工程库：风险高，缺少文档、许可证、测试和包边界。
- 作为知识库条目：应标注推断边界，不能把目录名推断当成作者原文。

## 关联笔记

- `notes/2026-06-24-youngtimes-algorithms-planning-demos.md`
- `wiki/2026-06-15-cpprobotics.md`

## 待补资料

- 阅读 `Frenet_planning` 三个场景源码，确认代价函数和约束。
- 阅读 `discretized_points_smoothing` 的 QP 形式。
- 检查 `mpc_linear.py` 的车辆模型、预测步长和约束处理。

## 更新记录

- 2026-06-24：基于 `main` 分支提交 `35bb6aa` 首次建档。
