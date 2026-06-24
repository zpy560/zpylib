---
id: "20260624-250003-robot-state-publisher"
title: "robot_state_publisher：机器人状态发布 Git 资源"
type: "note"
source: "raw/2026-06-24-robot-state-publisher-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-3.md
---

# robot_state_publisher：机器人状态发布 Git 资源

## 一句话结论

底盘和传感器外参需要稳定进入 tf 树，robot_state_publisher 是 ROS 机器人模型到运行时坐标树的基础节点。

## 原文要点

- 仓库：https://github.com/ros/robot_state_publisher
- GitHub 描述 / 定位：Publishes robot state to tf from joint states and URDF.
- GitHub 页面显示 star/fork：300+ stars / 200+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：BSD。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

底盘和传感器外参需要稳定进入 tf 树，robot_state_publisher 是 ROS 机器人模型到运行时坐标树的基础节点。

## 可复用内容

- 可作为 `机器人状态发布` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH、RMF 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入、优化后端或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-robot-state-publisher-repository-snapshot.md`
