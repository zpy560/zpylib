---
id: "20260625-robust-pose-graph-entity"
title: "robust-pose-graph"
type: "entity"
source: "notes/2026-06-25-robust-pose-graph-repository-note.md"
created_at: "2026-06-25"
tags:
  - autonomous-driving
  - planning-control
related:
  - "../notes/2026-06-25-robust-pose-graph-repository-note.md"
---

# robust-pose-graph

## 定位

鲁棒位姿图优化，偏 SLAM 后端，但影响定位和规划地图质量。

## 来源事实

- 仓库：https://github.com/RobotLocomotion/robust-pose-graph
- 原料：../raw/2026-06-25-robust-pose-graph-repository-snapshot.md
- 笔记：../notes/2026-06-25-robust-pose-graph-repository-note.md
- 抓取状态：README 抓取失败或默认分支未命中；保留 GitHub 仓库 URL 作为原始来源。

## 适合研究的问题

- 它在规划、控制、建图、仿真或机器人软件栈中承担什么边界。
- 它和现有知识库中的 Nav2、MoveIt、OCS2、Pinocchio、Crocoddyl、F1TENTH、CommonRoad 等项目如何互补。
- 是否具备可复现实验、清晰接口、活跃维护和可迁移价值。

## 后续检查

- 许可证、最近提交、release/tag、CI 状态。
- 核心包目录、依赖版本和最小可运行 demo。
- 与已有同类库的差异：算法新意、工程成熟度、系统依赖和可复用模块。
