---
id: "20260624-240001-turtlebot3"
title: "TurtleBot3：AMR 教学与导航底盘 Git 资源"
type: "note"
source: "raw/2026-06-24-turtlebot3-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# TurtleBot3：AMR 教学与导航底盘 Git 资源

## 一句话结论

TurtleBot3 是移动机器人导航教学和 Nav2 验证的高频底盘入口，适合研究小型差速底盘的完整 ROS 包组织。

## 原文要点

- 仓库：https://github.com/ROBOTIS-GIT/turtlebot3
- GitHub 描述 / 定位：ROS packages for TurtleBot3，包含 bringup、description、navigation2、Cartographer、teleop 等包。
- GitHub 页面显示 star/fork：2k stars / 1.2k forks。
- 主要语言 / 技术栈：C++/Python。
- 许可证观察：Apache-2.0。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

TurtleBot3 是移动机器人导航教学和 Nav2 验证的高频底盘入口，适合研究小型差速底盘的完整 ROS 包组织。

## 可复用内容

- 可作为 `AMR 教学与导航底盘` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-turtlebot3-repository-snapshot.md`
