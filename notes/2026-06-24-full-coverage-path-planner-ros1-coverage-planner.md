---
id: "20260624-full-coverage-path-planner-ros1-coverage-planner"
title: "Full Coverage Path Planner：ROS1 覆盖路径规划插件"
type: "note"
source: "raw/2026-06-24-full-coverage-path-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - autonomous-driving
  - programming
  - tools
related:
  - wiki/2026-06-24-full-coverage-path-planner.md
  - wiki/2026-06-14-ros-motion-planning.md
---

# Full Coverage Path Planner：ROS1 覆盖路径规划插件

## 一句话结论

Full Coverage Path Planner 是一个聚焦“区域全覆盖”的 ROS1 全局规划插件，核心是 Backtracking Spiral Algorithm，适合清扫、割草、巡检这类覆盖任务的算法参考；它不是通用点到点导航框架，也不是当前仍被维护方内部使用的生产主线。

## 原文要点

- 仓库提供 FCPP 的实现，使用 Backtracking Spiral Algorithm。
- 包以 `move_base` / Move Base Flex 全局规划插件形式接入。
- 插件名为 `full_coverage_path_planner/SpiralSTC`。
- `robot_radius` 用于静态地图碰撞检查，`tool_radius` 用于覆盖离散化和覆盖进度计算。
- 示例系统包含 `coverage_progress` 节点，发布 `/coverage_grid` 与 `/coverage_progress`。
- README 标注测试环境为 ROS Melodic 和 Ubuntu 18.04。
- README 明确说明 Nobleo 已不再内部使用该包，但仍欢迎贡献。

## 我的判断

### 价值在覆盖任务，而不是替代全局导航

该仓库解决的问题和 A*、RRT、DWA 这类点到点规划不同：目标不是找一条到终点的短路径，而是让工具覆盖可达区域。对自动驾驶主线规划来说，它的直接复用价值有限；对园区清扫、仓储地面维护、农机覆盖作业更相关。

### ROS1 插件边界清晰，但技术栈偏旧

插件接口、launch 示例和测试说明都围绕 ROS1、catkin、`move_base`/MBF。若要迁移到 ROS2/Nav2，重点不是搬代码，而是重做 lifecycle、pluginlib 接口、costmap 接口和行为树触发方式。

### `tool_radius` 是阅读重点

覆盖规划里“机器人不碰障碍”和“工具扫过区域”是两个半径问题。该仓库把两者拆开，是比普通 footprint 膨胀更贴近覆盖任务的建模方式。

## 可复用内容

- 覆盖路径规划任务建模：区分 robot footprint 与 coverage tool footprint。
- 覆盖进度监控：用 occupancy grid 记录工具圆盘覆盖过的 cell。
- ROS1 全局规划插件样例：从 costmap 生成全覆盖路径，再交给路径跟踪控制器。
- 测试思路：用随机地图检查可达 cell 是否被覆盖。

## 疑问与冲突

- README 标注维护方不再内部使用，工程活跃性需要谨慎看待。
- 本次未编译运行，无法确认 ROS Melodic 依赖在当前系统上的可复现性。
- 该仓库的覆盖算法和通用规划算法工作台关注点不同，不应简单横向比较路径长度。

## 原料

- `raw/2026-06-24-full-coverage-path-planner-repository-snapshot.md`
