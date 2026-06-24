---
id: "20260624-navigation2-ignition-gazebo-example-nav2-gz-testing"
title: "Navigation2 Ignition Gazebo Example：Nav2 + Gazebo Fortress 测试示例"
type: "note"
source: "raw/2026-06-24-navigation2-ignition-gazebo-example-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2-ignition-gazebo-example.md
  - wiki/2026-06-13-navigation2.md
---

# Navigation2 Ignition Gazebo Example：Nav2 + Gazebo Fortress 测试示例

## 一句话结论

art-e-fact/navigation2_ignition_gazebo_example 是一个更工程化的 Nav2 + Ignition Gazebo 最小项目：除了 bringup，还包含 waypoint/reach-goal 示例、launch_testing、Artefacts CI 和 Rerun 可视化入口，适合学习 Nav2 仿真回归测试。

## 原文要点

- 面向 ROS 2 Humble、Gazebo Fortress 和 Navigation2。
- 基于官方 Gazebo Classic Nav2 示例迁移到 Ignition Gazebo。
- 使用 `deps.repos` 导入源码依赖。
- 主 launch 为 `sam_bot_nav2_gz complete_navigation.launch.py`。
- 提供 `follow_waypoints.py` 和 `reach_goal.py`。
- 提供 bringup、reach-goal 和 follow-waypoints 的 launch tests。
- 支持 Artefacts CI 和 Docker 测试。
- 提供实验性的 Rerun.io 可视化。

## 我的判断

### 比普通 demo 更适合做回归测试模板

该仓库不只是“能跑起来”的仿真 demo，还把 launch_testing 和 CI 纳入 README。对 Nav2 集成项目，最可复用的是仿真场景自动化验证思路，而不是某个机器人模型本身。

### 技术栈有版本边界

它明确面向 Humble + Gazebo Fortress。迁移到 Jazzy/Harmonic 或 Gazebo 新命名体系时，需要重新检查 bridge、launch、world、Nav2 参数和依赖版本。

## 可复用内容

- Nav2 + Gazebo Fortress + RViz 一体 bringup。
- waypoint 和 reach-goal 自动化测试样例。
- Artefacts CI / Docker 运行仿真测试的组织方式。
- Rerun 可视化 Nav2 仿真数据的实验入口。

## 疑问与冲突

- 本次未运行仿真或测试。
- Ignition/Gazebo 命名和版本体系变化快，后续需要按目标 ROS 发行版复核。

## 原料

- `raw/2026-06-24-navigation2-ignition-gazebo-example-repository-snapshot.md`
