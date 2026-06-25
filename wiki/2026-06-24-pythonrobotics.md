---
id: "20260624-pythonrobotics"
title: "PythonRobotics"
type: "entity"
source: "raw/2026-06-24-pythonrobotics-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-pathplanning-search-sampling-algorithm-demos.md
  - notes/2026-06-24-pythonrobotics-robotics-algorithm-textbook.md
  - wiki/2026-06-15-cpprobotics.md
  - wiki/2026-06-24-motionplanning.md
  - wiki/2026-06-24-pathplanning.md
---

# PythonRobotics

## 基本信息

- 类型：机器人算法教学代码库
- 官方仓库：https://github.com/AtsushiSakai/PythonRobotics
- 快照分支：`master`
- 快照提交：`b38c510e083d69a5755d98d0680bd50f3d9a91fa`
- 快照日期：2026-06-24

## 当前结论

PythonRobotics 是规划控制算法学习的首选入口之一。它覆盖面广、可读性强，适合建立算法谱系和做快速实验；不承担工程框架、实时部署和安全闭环职责。

## 核心依据

- README 定位为 Python code collection and textbook。
- 覆盖规划、跟踪控制、定位、建图、SLAM 等多个机器人算法板块。
- 多个 C++ 示例仓库直接或间接受它影响。

## 不同观点与冲突

- 作为教材：优先级高。
- 作为生产依赖：不适用。
- 作为自动驾驶算法参考：可参考思路，但必须补工程约束。

## 关联笔记

- `notes/2026-06-24-pythonrobotics-robotics-algorithm-textbook.md`
- `wiki/2026-06-24-motionplanning.md`
- `wiki/2026-06-15-cpprobotics.md`

## 待补资料

- 挑选 A*、Hybrid A*、Frenet、Stanley、MPC 逐个做公式与代码对照。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `b38c510` 首次建档。

