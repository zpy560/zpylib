---
id: "20260624-drake-robotics-planning-control-toolbox"
title: "Drake：机器人建模仿真规划控制工具箱"
type: "note"
source: "raw/2026-06-24-drake-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-drake.md
---

# Drake：机器人建模仿真规划控制工具箱

## 一句话结论

Drake 不是单一控制器或规划器，而是把机器人建模、仿真、优化、规划和控制放在同一套系统里的大型工具箱；适合研究复杂机器人系统，不适合当作轻量算法示例入口。

## 原文要点

- 仓库为 RobotLocomotion 维护的 Drake。
- README 将详细信息导向官方网站和文档。
- 当前快照 HEAD 为 `1714364cbecd8c863c301fe0f60412c40f00c89a`。

## 我的判断

Drake 的价值在系统级一体化：动力学模型、优化问题、仿真和控制闭环可以共用同一套基础设施。对自动驾驶规划控制可借鉴系统组织方式，但直接引入成本较高。

## 可复用内容

- 多体系统建模与仿真思路。
- 优化驱动的规划控制架构。
- 复杂系统实验平台设计。

## 疑问与冲突

- 仓库体量大，学习曲线和构建成本高。
- 不是 ROS/Nav2/Autoware 这类部署框架。

## 原料

- `raw/2026-06-24-drake-repository-snapshot.md`

