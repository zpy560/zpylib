---
id: "20260624-230037-unitree-mujoco"
title: "unitree_mujoco：Unitree 仿真 Git 资源"
type: "note"
source: "raw/2026-06-24-unitree-mujoco-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# unitree_mujoco：Unitree 仿真 Git 资源

## 一句话结论

它是 Unitree 实机控制前的仿真验证入口，适合研究 SDK2 控制程序如何在 MuJoCo 中复用。

## 原文要点

- 仓库：https://github.com/unitreerobotics/unitree_mujoco
- GitHub 描述 / 定位：Unitree SDK2 与 MuJoCo 的仿真桥。
- GitHub 页面显示 star/fork：1k+ stars / 350+ forks。
- 主要语言 / 技术栈：C++/Python。
- 许可证观察：BSD-3-Clause。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

它是 Unitree 实机控制前的仿真验证入口，适合研究 SDK2 控制程序如何在 MuJoCo 中复用。

## 可复用内容

- 可作为 `Unitree 仿真` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-unitree-mujoco-repository-snapshot.md`
