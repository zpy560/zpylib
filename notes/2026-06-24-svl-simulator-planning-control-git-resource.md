---
id: "20260624-230003-svl-simulator"
title: "SVL Simulator：整车仿真 Git 资源"
type: "note"
source: "raw/2026-06-24-svl-simulator-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# SVL Simulator：整车仿真 Git 资源

## 一句话结论

SVL 对研究 Autoware/Apollo 全系统仿真和历史接口有价值；新项目应优先评估更活跃的平台。

## 原文要点

- 仓库：https://github.com/lgsvl/simulator
- GitHub 描述 / 定位：面向 Autoware/Apollo 的 ROS/ROS2 多机器人自动驾驶仿真器。
- GitHub 页面显示 star/fork：2.4k+ stars / 790+ forks。
- 主要语言 / 技术栈：C#。
- 许可证观察：Custom。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

SVL 对研究 Autoware/Apollo 全系统仿真和历史接口有价值；新项目应优先评估更活跃的平台。

## 可复用内容

- 可作为 `整车仿真` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-svl-simulator-repository-snapshot.md`
