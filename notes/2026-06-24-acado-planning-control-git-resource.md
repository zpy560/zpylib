---
id: "20260624-240021-acado"
title: "ACADO Toolkit：最优控制/MPC Git 资源"
type: "note"
source: "raw/2026-06-24-acado-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - wiki/2026-06-24-mobile-chassis-planning-control-github-resources-batch-2.md
---

# ACADO Toolkit：最优控制/MPC Git 资源

## 一句话结论

ACADO 是 MPC/OCP 老牌工具链，适合和 acados、CasADi、do-mpc 对比建模和求解器边界。

## 原文要点

- 仓库：https://github.com/acado/acado
- GitHub 描述 / 定位：Software environment and algorithms for automatic control and dynamic optimization.
- GitHub 页面显示 star/fork：1k+ stars / 500+ forks。
- 主要语言 / 技术栈：C++。
- 许可证观察：LGPL。
- 入选原因：当前知识库未记录该 Git URL，且与自动驾驶或移动底盘规划控制闭环相关。

## 我的判断

ACADO 是 MPC/OCP 老牌工具链，适合和 acados、CasADi、do-mpc 对比建模和求解器边界。

## 可复用内容

- 可作为 `最优控制/MPC` 方向的源码阅读入口。
- 可与现有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot/F1TENTH 等资源交叉对比。
- 可继续拆解其接口、算法模块、仿真测试方式、地图定位输入或控制执行链。

## 疑问与冲突

- star/fork 只能说明关注度，不能直接证明算法质量。
- 若仓库已归档、停止主动维护或绑定特定平台，后续复用前必须单独验证。
- 本轮是资源解析，不等同于逐行代码审查。

## 原料

- `raw/2026-06-24-acado-repository-snapshot.md`
