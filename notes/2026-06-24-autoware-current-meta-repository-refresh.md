---
id: "20260624-autoware-current-meta-repository-refresh"
title: "Autoware：当前 meta-repository 与版本清单补充"
type: "note"
source: "raw/2026-06-24-autoware-current-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-14-autoware.md
  - notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md
---

# Autoware：当前 meta-repository 与版本清单补充

## 一句话结论

当前 Autoware 主仓库仍然是 meta-repository：真正源码由 `repositories/autoware.repos` 固定到多个 Core、Universe、Launch、消息和传感器仓库。评审 Autoware 不能只看主仓库 README，必须以 manifest 锁定的组件版本为准。

## 原文要点

- 当前 `main` HEAD 为 `4847819760656247343dfb995ea8e151fc3d9b00`。
- README 称 Autoware 是开源自动驾驶框架，并描述为面向商业部署加速的完整软件栈。
- README 把安装、快速 demo、文档、贡献指南、工作组、Q&A、CI metrics 等入口集中到官方文档与社区链接。
- `src/README.md` 明确说明 `autoware` 本身不包含完整源码，而是通过 `repositories/` 下的 manifest 管理多个仓库。
- 当前 essential source checkout 命令是 `vcs import src < repositories/autoware.repos`。
- `repositories/autoware.repos` 当前固定 `autoware_core` 到 `1.8.0`、`autoware_universe` 到 `0.51.0`、`autoware_launch` 到 `0.51.0`。
- 当前清单还包含 `agnocast 2.3.5`、`autoware_msgs 1.13.0`、`autoware_adapi_msgs 1.9.1`、`autoware_internal_msgs 1.12.1`、传感器组件和多个外部依赖。

## 我的判断

### 旧结论继续成立，但入口文件位置需要修正

2026-06-14 的核心判断仍成立：Autoware 的复杂度来自多仓库版本清单、launch、参数、remap 和功能开关共同决定最终系统行为。

本次需要修正的细节是：当前主仓库的 essential manifest 在 `repositories/autoware.repos`，不是根目录 `autoware.repos`。后续抓取和审计应从这个路径开始。

### README 的定位更偏产品化，但事实判断仍要回到源码与清单

README 使用了 production-ready 叙述，这代表项目对自身定位的表述；但对具体部署是否生产可用，仍要看目标版本、目标硬件、传感器、地图、仿真/实车验证、CI 状态和安全链路配置。

### Agnocast 已成为需要跟踪的基础设施项

清单里 `agnocast` 位于 core，并且注释说明还处于向官方 ROS 包迁移前的源码构建阶段。对 Autoware 通信性能、部署和调试链路的后续分析，需要把 Agnocast 当作一等基础设施，而不是边缘依赖。

## 可复用内容

- Autoware meta-repo 审计入口：`repositories/autoware.repos`。
- 多仓库版本化装配模式：Core、Universe、Launcher、Sensor Component 和外部依赖分区。
- 文档入口：安装、demo、设计文档、贡献流程、CI metrics 分离维护。
- 审计步骤：先读 manifest，再按 pinned version 读取实际源码，最后展开 launch 和参数。

## 疑问与冲突

- 本次没有执行 `vcs import`，没有递归读取 `autoware_core`、`autoware_universe`、`autoware_launch` 当前源码。
- 没有运行 demo、仿真或测试，因此不验证 production-ready 表述。
- Agnocast 与标准 ROS 2 通信的实际边界需要单独分析。

## 原料

- `raw/2026-06-24-autoware-current-repository-snapshot.md`
- `notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md`
