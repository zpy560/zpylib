---
id: "20260624-navigation2-ignition-gazebo-turtlebot3-tf-bridge-example"
title: "navigation2_ignition_gazebo_turtlebot3：TurtleBot3 Ignition Gazebo Nav2 示例"
type: "note"
source: "raw/2026-06-24-navigation2-ignition-gazebo-turtlebot3-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2-ignition-gazebo-turtlebot3.md
  - wiki/2026-06-13-navigation2.md
---

# navigation2_ignition_gazebo_turtlebot3：TurtleBot3 Ignition Gazebo Nav2 示例

## 一句话结论

Onicc/navigation2_ignition_gazebo_turtlebot3 是一个聚焦 TurtleBot3、Ignition Gazebo、ros_ign_bridge、TF 和 nav2_bringup 接线的示例，适合理解 Gazebo 仿真数据如何桥接到 ROS 2/Nav2。

## 原文要点

- 用 Nav2 导航 Ignition Gazebo 中的 TurtleBot3。
- 一条 launch 命令同时启动 simulation、Nav2 和 RViz2。
- `/odom`、`odom` frame 和 `/odom/tf` 在 `model.sdf` 中定义。
- `/odom/tf` 发布 `base_footprint` 在 `odom` frame 中的变换，并 remap 到 `/tf`。
- Ignition Gazebo 发布 `joint_states`，通过 `ros_ign_bridge` 转为 ROS 2 topic。
- `robot_state_publisher` 消费 joint states 并发布多数 TF。
- `nav2_bringup` 启动基础服务和配置。
- 测试环境为 Ignition Gazebo Fortress 和 ROS 2 Humble。

## 我的判断

### 价值在 TF/bridge 细节

很多 Nav2 + Gazebo 问题不在规划器，而在 `/tf`、`/odom`、`joint_states` 和 bridge remap。这个示例直接说明了 odom/tf 和 robot_state_publisher 的关系，适合作为排查仿真接线的参考。

### 示例规模较小

它不像 art-e-fact 示例那样强调自动化测试和 CI，更像一个 TurtleBot3 bringup 参考。使用时重点看 launch、SDF、bridge 和 Nav2 参数，不应把它当作完整仿真测试框架。

## 可复用内容

- TurtleBot3 + Ignition Gazebo + Nav2 bringup。
- `/odom/tf` remap 到 `/tf` 的接线说明。
- ros_ign_bridge 与 robot_state_publisher 数据流。
- 用 `tf2_tools view_frames` 检查 TF 关系。

## 疑问与冲突

- 本次未运行仿真。
- 当前 Gazebo/ROS 发行版命名已演进，Fortress/Humble 之外需重新验证依赖。

## 原料

- `raw/2026-06-24-navigation2-ignition-gazebo-turtlebot3-repository-snapshot.md`
