---
id: "20260624-210019-descartes-note"
title: "Descartes：ROS-Industrial 笛卡尔路径规划器"
type: "note"
source: "raw/2026-06-24-descartes-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-descartes.md
---

# Descartes：ROS-Industrial 笛卡尔路径规划器

## 结论

Descartes 值得作为机械臂笛卡尔路径规划资料入库，尤其适合工业加工、焊接、喷涂、扫描等末端轨迹受工艺约束的场景。但这次可抓取的 README 信息很少，后续深读应转向 ROS wiki 和源码包。

## 事实摘录

- 远端仓库：`ros-industrial-consortium/descartes`
- 当前核对 HEAD：`26197a993a0eaabe7c207a881fe6bd06177ab5fd`
- README 定位：ROS-Industrial Special Project: Cartesian Path Planner。
- README 指向 ROS wiki 作为进一步信息来源。

## 对规划控制的意义

- 它补齐了 MoveIt/OMPL 之外的工业笛卡尔过程规划视角。
- 工业路径规划关注的不只是起终点避障，而是整段路径上的姿态、可达性、冗余解、碰撞和工艺约束。
- 和 MoveIt 体系结合阅读，可以区分 general motion planning 与 process-constrained Cartesian planning。

## 使用建议

把它作为 ROS-Industrial 规划资料入口，不要只依赖根 README。下一步如果要深挖，应读取 ROS wiki、包结构和示例，重点看如何表达 Cartesian waypoint、采样 IK 解和图搜索。

