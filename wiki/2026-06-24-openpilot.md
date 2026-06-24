---
id: "20260624-openpilot"
title: "openpilot"
type: "entity"
source: "raw/2026-06-24-openpilot-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
related:
  - notes/2026-06-24-openpilot-driver-assistance-operating-system.md
  - wiki/2026-06-14-apollo.md
  - wiki/2026-06-14-autoware.md
---

# openpilot

## 基本信息

- 类型：开源驾驶辅助系统
- 官方仓库：https://github.com/commaai/openpilot
- 文档：https://docs.comma.ai
- 快照分支：`master`
- 快照提交：`7d325d6650206d9d78e63179ba9b4a2e1d84e4fc`
- 快照日期：2026-06-24

## 当前结论

openpilot 是真实车辆 ADAS 系统参考，适合研究产品化驾驶辅助系统的规划控制和车辆接口，不等同于 Apollo/Autoware 这类 L4 平台。

## 核心依据

- README 称其为 operating system for robotics。
- 支持 300+ 车型。
- 使用需要设备、车型、线束和软件发布分支。

## 不同观点与冲突

- 作为 ADAS 产品化参考：优先级高。
- 作为通用自动驾驶算法库：不准确。
- 作为 L4 平台：不适用。

## 关联笔记

- `notes/2026-06-24-openpilot-driver-assistance-operating-system.md`
- `wiki/2026-06-14-apollo.md`
- `wiki/2026-06-14-autoware.md`

## 待补资料

- 单独分析 controlsd/plannerd/modeld 与车辆接口链路。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `7d325d6` 首次建档。

