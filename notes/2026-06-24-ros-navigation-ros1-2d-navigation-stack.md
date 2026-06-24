---
id: "20260624-ros-navigation-ros1-2d-navigation-stack"
title: "ROS Navigation：ROS1 二维移动机器人导航栈"
type: "note"
source: "raw/2026-06-24-ros-navigation-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-ros-navigation.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
---

# ROS Navigation：ROS1 二维移动机器人导航栈

## 一句话结论

ROS Navigation 是 ROS1 时代的二维移动机器人导航栈，输入里程计、传感器和目标点，输出安全速度命令；它是理解 Nav2 演进和 `move_base` 架构的历史基线。

## 原文要点

- README 定位为 2D navigation stack。
- 输入包括 odometry、sensor streams、goal pose。
- 输出 safe velocity commands 给 mobile base。
- 相关仓库包括 navigation_msgs、navigation_tutorials、navigation_experimental。

## 我的判断

这个仓库应和 Navigation2 分开入库。ROS Navigation 适合理解 ROS1 `move_base`、costmap、planner/controller 插件历史；Nav2 则重构为 ROS2 lifecycle、behavior tree 和 action server 体系。

## 可复用内容

- ROS1 move_base 导航链路。
- 2D costmap 与局部/全局规划器边界。
- ROS1 到 ROS2 Nav2 迁移对照。

## 疑问与冲突

- ROS1 历史栈，不代表当前 ROS2 推荐架构。
- 现代项目应优先对比 Nav2。

## 原料

- `raw/2026-06-24-ros-navigation-repository-snapshot.md`

