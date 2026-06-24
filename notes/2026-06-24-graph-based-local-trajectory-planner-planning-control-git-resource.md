---
id: "20260624-240013-graph-based-local-trajectory-planner"
title: "GraphBasedLocalTrajectoryPlanner：自动赛车局部轨迹规划 Git 资源"
type: "note"
source: "raw/2026-06-24-graph-based-local-trajectory-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# GraphBasedLocalTrajectoryPlanner：自动赛车局部轨迹规划 Git 资源

## 一句话结论

README 说明该 planner 曾用于 Roborace，并达到 200kph 以上速度，是高动态局部轨迹规划参考。

## 原文要点

- 仓库：https://github.com/TUMFTM/GraphBasedLocalTrajectoryPlanner
- GitHub 描述 / 定位：Multilayer graph-based local trajectory planner for autonomous race vehicles.
- GitHub 页面显示 star/fork：265 stars / 59 forks。
- 主要语言 / 技术栈：Python。
- 许可证观察：LGPL-3.0。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

README 说明该 planner 曾用于 Roborace，并达到 200kph 以上速度，是高动态局部轨迹规划参考。

## 可复用内容

- 可作为 `自动赛车局部轨迹规划` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-graph-based-local-trajectory-planner-repository-snapshot.md`
