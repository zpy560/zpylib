---
id: "20260624-230005-carla-scenario-runner"
title: "CARLA Scenario Runner：场景测试 Git 资源"
type: "note"
source: "raw/2026-06-24-carla-scenario-runner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# CARLA Scenario Runner：场景测试 Git 资源

## 一句话结论

适合把 cut-in、路口、跟车、让行等行为场景沉淀成规划控制回归测试。

## 原文要点

- 仓库：https://github.com/carla-simulator/scenario_runner
- GitHub 描述 / 定位：CARLA 交通场景定义与执行引擎。
- GitHub 页面显示 star/fork：660+ stars / 430+ forks。
- 主要语言 / 技术栈：Python。
- 许可证观察：MIT。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

适合把 cut-in、路口、跟车、让行等行为场景沉淀成规划控制回归测试。

## 可复用内容

- 可作为 `场景测试` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-carla-scenario-runner-repository-snapshot.md`
