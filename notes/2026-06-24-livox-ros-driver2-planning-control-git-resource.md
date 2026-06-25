---
id: "20260624-270019-livox-ros-driver2"
title: "livox_ros_driver2：Livox 激光雷达驱动 Git 资源"
type: "note"
source: "raw/2026-06-24-livox-ros-driver2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-4.md
---

# livox_ros_driver2：Livox 激光雷达驱动 Git 资源

## 一句话结论

Livox 非重复扫描模式对建图和避障有特殊影响，驱动是规划输入链的基础。

## 原文要点

- 仓库：https://github.com/Livox-SDK/livox_ros_driver2
- GitHub 描述 / 定位：ROS2/ROS1 driver for Livox lidar.
- GitHub 页面显示 star/fork：700+ stars / 500+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：MIT。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

Livox 非重复扫描模式对建图和避障有特殊影响，驱动是规划输入链的基础。

## 可复用内容

- 可作为 `Livox 激光雷达驱动` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH、RMF、MAVLink 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、传感器输入、地图定位链路、可视化调试或车辆控制工具链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-livox-ros-driver2-repository-snapshot.md`
