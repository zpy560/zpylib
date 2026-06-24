---
id: "20260624-230014-rsband-local-planner"
title: "rsband_local_planner：Ackermann 局部规划 Git 资源"
type: "note"
source: "raw/2026-06-24-rsband-local-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# rsband_local_planner：Ackermann 局部规划 Git 资源

## 一句话结论

这是比通用 DWA 更贴近 Ackermann 底盘的 ROS1 局部规划参考。

## 原文要点

- 仓库：https://github.com/gkouros/rsband_local_planner
- GitHub 描述 / 定位：面向 Ackermann 或四轮转向 car-like robots 的 ROS move_base local planner 插件。
- GitHub 页面显示 star/fork：170+ stars / 50+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：BSD。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

这是比通用 DWA 更贴近 Ackermann 底盘的 ROS1 局部规划参考。

## 可复用内容

- 可作为 `Ackermann 局部规划` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-rsband-local-planner-repository-snapshot.md`
