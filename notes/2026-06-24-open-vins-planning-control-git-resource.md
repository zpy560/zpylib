---
id: "20260624-280025-open-vins"
title: "OpenVINS：视觉惯性状态估计 Git 资源"
type: "note"
source: "raw/2026-06-24-open-vins-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-5.md
---

# OpenVINS：视觉惯性状态估计 Git 资源

## 一句话结论

OpenVINS 是 VIO 研究和移动平台定位常用框架，适合对比 VINS-Mono/Fusion。

## 原文要点

- 仓库：https://github.com/rpng/open_vins
- GitHub 描述 / 定位：Research platform for visual-inertial estimation.
- GitHub 页面显示 star/fork：1k+ stars / 500+ forks。
- 主要语言 / 技术栈：C++/ROS。
- 许可证观察：GPL-3.0。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

OpenVINS 是 VIO 研究和移动平台定位常用框架，适合对比 VINS-Mono/Fusion。

## 可复用内容

- 可作为 `视觉惯性状态估计` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、MoveIt、ROS 感知、LIO/VIO/SLAM、DDS/RMW 和移动底盘接口资源交叉对比。
- 可继续拆解其接口、算法模块、工程约束、消息类型、配置参数、测试方式或与规划控制闭环的连接点。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-open-vins-repository-snapshot.md`
