---
id: "20260624-230038-mujoco"
title: "MuJoCo：动力学仿真 Git 资源"
type: "note"
source: "raw/2026-06-24-mujoco-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# MuJoCo：动力学仿真 Git 资源

## 一句话结论

MuJoCo 是腿式、机械臂和移动底盘控制算法验证的基础设施，尤其适合接触动力学和学习控制。

## 原文要点

- 仓库：https://github.com/google-deepmind/mujoco
- GitHub 描述 / 定位：Multi-Joint dynamics with Contact 通用物理仿真器。
- GitHub 页面显示 star/fork：14k+ stars / 1.6k+ forks。
- 主要语言 / 技术栈：C/C++/Python。
- 许可证观察：Apache-2.0。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

MuJoCo 是腿式、机械臂和移动底盘控制算法验证的基础设施，尤其适合接触动力学和学习控制。

## 可复用内容

- 可作为 `动力学仿真` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-mujoco-repository-snapshot.md`
