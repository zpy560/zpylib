---
id: "20260624-240037-cartographer"
title: "Cartographer：2D/3D SLAM Git 资源"
type: "note"
source: "raw/2026-06-24-cartographer-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# Cartographer：2D/3D SLAM Git 资源

## 一句话结论

Cartographer 是移动机器人 SLAM 重要基线；README 明确说明已不再主动维护，适合历史架构参考。

## 原文要点

- 仓库：https://github.com/cartographer-project/cartographer
- GitHub 描述 / 定位：Real-time SLAM in 2D and 3D across platforms and sensor configurations.
- GitHub 页面显示 star/fork：7.9k stars / 2.3k forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：Apache-2.0。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

Cartographer 是移动机器人 SLAM 重要基线；README 明确说明已不再主动维护，适合历史架构参考。

## 可复用内容

- 可作为 `2D/3D SLAM` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-cartographer-repository-snapshot.md`
