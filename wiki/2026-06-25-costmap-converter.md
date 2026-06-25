---
id: "20260625-costmap-converter-entity"
title: "costmap_converter"
type: "entity"
source: "notes/2026-06-25-costmap-converter-repository-note.md"
created_at: "2026-06-25"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-25-costmap-converter-repository-note.md
---
# costmap_converter

## 定位

costmap 到几何障碍物转换工具，常与 TEB/MPC 局部规划器配套。

## 来源事实

- 仓库：https://github.com/rst-tu-dortmund/costmap_converter
- 原料：../raw/2026-06-25-costmap-converter-repository-snapshot.md
- 笔记：../notes/2026-06-25-costmap-converter-repository-note.md
- 抓取状态：README 抓取失败或默认分支未命中；保留 GitHub 仓库 URL 作为原始来源。

## 适合研究的问题

- 它在规划、控制、建图、仿真或机器人软件栈中承担什么边界。
- 它和现有知识库中的 Nav2、MoveIt、OCS2、Pinocchio、Crocoddyl、F1TENTH、CommonRoad 等项目如何互补。
- 是否具备可复现实验、清晰接口、活跃维护和可迁移价值。

## 后续检查

- 许可证、最近提交、release/tag、CI 状态。
- 核心包目录、依赖版本和最小可运行 demo。
- 与已有同类库的差异：算法新意、工程成熟度、系统依赖和可复用模块。
