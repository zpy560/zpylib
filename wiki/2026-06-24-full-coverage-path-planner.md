---
id: "20260624-full-coverage-path-planner"
title: "Full Coverage Path Planner"
type: "entity"
source: "raw/2026-06-24-full-coverage-path-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - autonomous-driving
  - programming
  - tools
related:
  - notes/2026-06-24-full-coverage-path-planner-ros1-coverage-planner.md
  - wiki/2026-06-14-ros-motion-planning.md
---

# Full Coverage Path Planner

## 基本信息

- 类型：ROS1 覆盖路径规划全局规划插件
- 官方仓库：https://github.com/nobleo/full_coverage_path_planner
- 目标环境：ROS Melodic、Ubuntu 18.04
- 主要语言：C++
- 快照分支：`master`
- 快照提交：`113e627b2864e0a69de89185a3bc18f04e98bf1f`
- 快照日期：2026-06-24
- 许可证：Apache-2.0

## 当前结论

Full Coverage Path Planner 适合研究和复用覆盖路径规划的 ROS1 插件实现，尤其是 Backtracking Spiral Algorithm、工具半径建模和覆盖进度监控。它不适合作为通用导航系统，也不应忽略 README 中“维护方不再内部使用”的状态信号。

## 核心依据

- 插件名为 `full_coverage_path_planner/SpiralSTC`。
- 与 `move_base` / Move Base Flex 集成。
- `robot_radius` 和 `tool_radius` 分离，分别处理碰撞与覆盖离散化。
- `coverage_progress` 节点通过 occupancy grid 跟踪覆盖率。
- 测试覆盖基础函数、Spiral STC 场景和 ROS 系统仿真。

## 不同观点与冲突

- 对点到点导航任务，它不如 A*、NavFn、Smac Planner 或 RRT 系列直接相关。
- 对全区域作业任务，它比普通最短路规划更贴近问题本质。
- ROS1/MBF 技术栈偏旧，迁移 ROS2/Nav2 需要重做接口层。

## 关联笔记

- `notes/2026-06-24-full-coverage-path-planner-ros1-coverage-planner.md`
- `wiki/2026-06-14-ros-motion-planning.md`

## 待补资料

- 逐文件阅读 BSA 实现和地图离散化逻辑。
- 检查分支 `ros2` 与 `galactic` 的可用状态。
- 与 Nav2 coverage planner 类项目做对照。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `113e627` 首次建档。
