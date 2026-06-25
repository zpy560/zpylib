---
id: "20260624-230036-unitree-ros2"
title: "unitree_ros2：Unitree ROS2 Git 资源"
type: "note"
source: "raw/2026-06-24-unitree-ros2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# unitree_ros2：Unitree ROS2 Git 资源

## 一句话结论

如果研究 ROS2 下四足移动底盘接入，这比 ROS1 unitree_ros 更靠近新工程。

## 原文要点

- 仓库：https://github.com/unitreerobotics/unitree_ros2
- GitHub 描述 / 定位：Unitree 四足机器人的 ROS2 接口与示例。
- GitHub 页面显示 star/fork：730+ stars / 210+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：BSD-3-Clause。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

如果研究 ROS2 下四足移动底盘接入，这比 ROS1 unitree_ros 更靠近新工程。

## 可复用内容

- 可作为 `Unitree ROS2` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-unitree-ros2-repository-snapshot.md`
