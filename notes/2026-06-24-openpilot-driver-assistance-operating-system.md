---
id: "20260624-openpilot-driver-assistance-operating-system"
title: "openpilot：面向量产车辆的驾驶辅助机器人系统"
type: "note"
source: "raw/2026-06-24-openpilot-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
related:
  - wiki/2026-06-24-openpilot.md
  - notes/2026-06-14-apollo-autonomous-driving-platform.md
  - notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md
---

# openpilot：面向量产车辆的驾驶辅助机器人系统

## 一句话结论

openpilot 是面向真实车辆的驾驶辅助系统，不是单个规划控制库；它适合研究量产车接口、驾驶辅助控制闭环、发布分支和用户设备部署边界。

## 原文要点

- README 称 openpilot is an operating system for robotics。
- 当前支持 300+ 车型的驾驶辅助升级。
- 使用需要 supported device、software、supported car、car harness。
- README 区分 release、staging、nightly、nightly-dev 等分支。
- 推荐使用预构建分支而不是直接跑 master。

## 我的判断

和 Apollo/Autoware 不同，openpilot 更贴近“消费级 ADAS 产品化系统”。学习它时不应只看控制算法，还要看车辆接口、分支发布、设备约束和安全边界。

## 可复用内容

- 量产车 ADAS 系统边界。
- 设备、车型、线束和软件发布的耦合关系。
- 自动驾驶开源项目的 release/staging/nightly 分支策略。

## 疑问与冲突

- 不是 L4 自动驾驶平台。
- 真实车辆使用涉及安全、法规和硬件适配，不能只按源码理解。

## 原料

- `raw/2026-06-24-openpilot-repository-snapshot.md`

