---
id: "20260624-230001-carla-simulator"
title: "CARLA：整车仿真 Git 资源"
type: "note"
source: "raw/2026-06-24-carla-simulator-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# CARLA：整车仿真 Git 资源

## 一句话结论

CARLA 是整车规划控制算法闭环验证的事实标准之一；它不是规划器本体，但决定算法如何在交通参与者、地图和传感器闭环中被测试。

## 原文要点

- 仓库：https://github.com/carla-simulator/carla
- GitHub 描述 / 定位：自动驾驶研究仿真器，适合规划、控制、传感器和交通场景闭环验证。
- GitHub 页面显示 star/fork：14k+ stars / 4.6k+ forks。
- 主要语言 / 技术栈：C++/Python。
- 许可证观察：MIT。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

CARLA 是整车规划控制算法闭环验证的事实标准之一；它不是规划器本体，但决定算法如何在交通参与者、地图和传感器闭环中被测试。

## 可复用内容

- 可作为 `整车仿真` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-carla-simulator-repository-snapshot.md`
