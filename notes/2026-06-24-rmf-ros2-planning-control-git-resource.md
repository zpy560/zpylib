---
id: "20260624-240034-rmf-ros2"
title: "rmf_ros2：多机器人 fleet ROS2 集成 Git 资源"
type: "note"
source: "raw/2026-06-24-rmf-ros2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# rmf_ros2：多机器人 fleet ROS2 集成 Git 资源

## 一句话结论

RMF 面向多机器人楼宇/仓储交通调度，适合研究 AMR 任务、交通和 fleet adapter 的系统边界。

## 原文要点

- 仓库：https://github.com/open-rmf/rmf_ros2
- GitHub 描述 / 定位：Internal ROS infrastructure for RMF.
- GitHub 页面显示 star/fork：113 stars / 97 forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：Apache-2.0。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

RMF 面向多机器人楼宇/仓储交通调度，适合研究 AMR 任务、交通和 fleet adapter 的系统边界。

## 可复用内容

- 可作为 `多机器人 fleet ROS2 集成` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-rmf-ros2-repository-snapshot.md`
