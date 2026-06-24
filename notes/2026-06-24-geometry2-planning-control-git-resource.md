---
id: "20260624-250002-geometry2"
title: "geometry2 / tf2：坐标变换基础设施 Git 资源"
type: "note"
source: "raw/2026-06-24-geometry2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-3.md
---

# geometry2 / tf2：坐标变换基础设施 Git 资源

## 一句话结论

tf2 是移动机器人所有定位、感知、规划、控制模块共享坐标系的基础设施。

## 原文要点

- 仓库：https://github.com/ros2/geometry2
- GitHub 描述 / 定位：ROS2 geometry2 repository, including tf2 libraries and tools.
- GitHub 页面显示 star/fork：600+ stars / 400+ forks。
- 主要语言 / 技术栈：C++/Python。
- 许可证观察：BSD。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

tf2 是移动机器人所有定位、感知、规划、控制模块共享坐标系的基础设施。

## 可复用内容

- 可作为 `坐标变换基础设施` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH、RMF 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入、优化后端或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-geometry2-repository-snapshot.md`
