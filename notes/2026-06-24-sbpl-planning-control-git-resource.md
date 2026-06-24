---
id: "20260624-240005-sbpl"
title: "SBPL：搜索式规划库 Git 资源"
type: "note"
source: "raw/2026-06-24-sbpl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# SBPL：搜索式规划库 Git 资源

## 一句话结论

SBPL 是自动驾驶和移动机器人搜索规划的重要历史基线，适合研究 lattice、ARA*、AD* 等搜索式规划思想。

## 原文要点

- 仓库：https://github.com/sbpl/sbpl
- GitHub 描述 / 定位：Search-Based Planning Library.
- GitHub 页面显示 star/fork：700+ stars / 400+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：BSD。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

SBPL 是自动驾驶和移动机器人搜索规划的重要历史基线，适合研究 lattice、ARA*、AD* 等搜索式规划思想。

## 可复用内容

- 可作为 `搜索式规划库` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-sbpl-repository-snapshot.md`
