---
id: "20260624-navigation2-tutorials"
title: "Navigation2 Tutorials"
type: "entity"
source: "https://github.com/ros-navigation/navigation2_tutorials.git"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-navigation2-tutorials-nav2-plugin-and-integration-examples.md
  - wiki/2026-06-13-navigation2.md
---

# Navigation2 Tutorials

## 基本信息

- 类型：Navigation2 官方教程代码仓库
- 官方仓库：https://github.com/ros-navigation/navigation2_tutorials.git
- 官方文档：https://docs.nav2.org/
- 默认分支：`rolling`
- 其他分支：`humble`、`jazzy`、`kilted`
- 快照提交：`86f674fef07f2e9e78bdaebbedd88292840b3011`
- 最后提交时间：2026-05-15
- 最后提交标题：`Add tutorial for usage of ground consistency layer (#142)`
- 主要语言：C++、Python、YAML、XML
- 主要机制：pluginlib、Nav2 Lifecycle、Costmap Layer、Costmap Filter、BasicNavigator、Gazebo、robot_localization
- 分析方式：静态源码、配置和 launch 分析；未编译运行

## 当前判断

Navigation2 Tutorials 是学习 Nav2 插件和系统集成的入口仓库，不是算法库。它适合照着写自定义 planner、controller、costmap layer、behavior 和传感器增强 costmap，但示例算法只用于说明接口，不能直接当生产实现。

## 主要内容

### 插件开发

- `nav2_straightline_planner`：GlobalPlanner 插件最小样例。
- `nav2_pure_pursuit_controller`：Controller 插件和 Pure Pursuit 控制样例。
- `nav2_gradient_costmap_plugin`：Costmap Layer 插件样例。
- `nav2_sms_behavior`：Behavior 插件、自定义 Action 与外部 HTTP 服务样例。

### 导航集成

- `nav2_costmap_filters_demo`：keepout 与 speed filter mask。
- `nav2_gps_waypoint_follower_demo`：GPS waypoint、Mapviz、dual EKF 和无静态地图导航。
- `nav2_semantic_segmentation_demo`：ONNX 语义分割输出接入语义 costmap layer。
- `nav2_lidar_ground_segmentation_demo`：3D lidar 地面分割接入 ground consistency costmap layer。

### 仿真与机器人描述

- `sam_bot_description`：差速机器人描述、Gazebo bridge、EKF、RViz 和示例 world。

## 工程边界

- 教程代码与 ROS 发行版和 Nav2 API 强绑定。
- `rolling` 分支不应直接用于 Humble/Jazzy/Kilted 项目。
- Straight-line planner 不处理障碍和取消。
- Pure Pursuit controller 没有实现速度限制和完整安全约束。
- Gradient layer 示例会覆盖 master costmap。
- SMS behavior 需要 Twilio 凭据和外网，不能默认放入恢复链。
- 感知增强示例依赖外部模型、外部包和仿真资源。
- 仓库缺少顶层 CI 和算法行为回归测试。

## 最值得学习

- Nav2 插件从 C++ 类到 XML、CMake、`package.xml` 和 YAML 参数的完整注册链。
- Lifecycle 回调在插件中的职责分配。
- Costmap layer/filter 如何把业务约束变成规划代价。
- GPS/IMU/odom 融合后如何让 Nav2 在无静态地图场景执行 waypoint。
- 语义分割和激光地面分割如何进入二维 costmap。

## 关联笔记

- `notes/2026-06-24-navigation2-tutorials-nav2-plugin-and-integration-examples.md`
- `wiki/2026-06-13-navigation2.md`

## 更新记录

- 2026-06-24：基于 `rolling` 分支提交 `86f674f` 完成教程包结构、插件接口、感知集成和工程边界建档。
