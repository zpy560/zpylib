---
id: "20260624-230028-husky"
title: "Husky：UGV 底盘平台 Git 资源"
type: "note"
source: "raw/2026-06-24-husky-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources.md
---

# Husky：UGV 底盘平台 Git 资源

## 一句话结论

Husky 是典型 UGV 底盘；它展示真实底盘包如何组织控制、仿真和导航配置。

## 原文要点

- 仓库：https://github.com/husky/husky
- GitHub 描述 / 定位：Clearpath Husky 的 ROS 仿真、描述、控制和导航包。
- GitHub 页面显示 star/fork：500+ stars / 430+ forks。
- 主要语言 / 技术栈：CMake/C++。
- 许可证观察：BSD-3-Clause。
- 入选原因：未在当前知识库记录过，且与自动驾驶或各种移动底盘规划控制闭环相关。

## 我的判断

Husky 是典型 UGV 底盘；它展示真实底盘包如何组织控制、仿真和导航配置。

## 可复用内容

- 可作为 `UGV 底盘平台` 方向的源码阅读入口。
- 可用于对比现有 Apollo、Autoware、Nav2、PX4、openpilot、TEB、MPC local planner 等已入库资源。
- 可继续拆解其接口、算法模块、仿真测试方式或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-husky-repository-snapshot.md`
