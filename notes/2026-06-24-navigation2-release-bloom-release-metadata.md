---
id: "20260624-navigation2-release-bloom-release-metadata"
title: "navigation2-release：Nav2 的 Bloom 发布元数据仓库"
type: "note"
source: "raw/2026-06-24-navigation2-release-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2-release.md
  - wiki/2026-06-13-navigation2.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - notes/2026-06-24-docs-nav2-org-navigation2-documentation-source.md
---

# navigation2-release：Nav2 的 Bloom 发布元数据仓库

## 一句话结论

`ros2-gbp/navigation2-release` 不是 Nav2 源码仓库，而是 ROS 发行版打包链路中的 Bloom release 仓库；它适合确认某个 ROS distro 中 Nav2 的发布版本、包清单、生成分支和 Bloom 工具链记录，不适合阅读算法实现。

## 原文要点

- 仓库说明是 Navigation2 metapackage 的 Bloom release repository。
- 默认分支 `master` 的 HEAD 观察为 `48c11ee63a39eafbec6d4754f4a414a7fc4ca007`。
- 顶层主要文件是 `README.md` 和 `tracks.yaml`。
- `tracks.yaml` 覆盖 bouncy、crystal、dashing、eloquent、foxy、galactic、humble、iron、jazzy、kilted。
- 当前 track 记录中，`humble` last version 为 `1.1.20`，`jazzy` 为 `1.3.12`，`kilted` 为 `1.4.2`。
- 2026-04-29 的 README 记录显示 `jazzy` 通过 `bloom-release navigation2 --rosdistro jazzy --track jazzy` 发布到 `1.3.12-1`。
- 近期 jazzy/kilted 发布包清单包含 `nav2_mppi_controller`、`nav2_smac_planner`、`nav2_route`、`nav2_collision_monitor`、`opennav_docking` 等核心包。
- 远端 refs 包含大量 `debian/*`、`release/*`、`rpm/*`、`upstream/*` 分支和标签，这是生成式发布仓库的典型形态。

## 我的判断

这个仓库的价值在“版本证据”，不是“架构学习”。如果要判断用户机器上的 Nav2 二进制包来自哪个上游版本，应先看 ROS distro 和 Debian 包版本，再回到这个 release 仓库匹配 `README.md`、`tracks.yaml` 和 `upstream/*` 标签。

对于工程调试，正确链路是：

```text
已安装 ROS distro / apt 包版本
→ navigation2-release 的 distro release 记录
→ upstream tag / upstream repository
→ Navigation2 源码与 docs.nav2.org 对应版本
```

这能避免一个常见错误：拿 Nav2 `main` 分支文档或源码解释 Humble/Jazzy 已发布二进制包的行为。Nav2 变化较快，`nav2_route`、MPPI、docking、controller 插件等模块在不同发行版中的包清单和能力边界可能不同。

## 可复用内容

| ROS distro | release 线索 |
|---|---|
| Humble | `tracks.yaml` last version `1.1.20`，README 最近记录 `1.1.20-1` |
| Jazzy | `tracks.yaml` last version `1.3.12`，README 最近记录 `1.3.12-1` |
| Kilted | `tracks.yaml` last version `1.4.2`，README 最近记录 `1.4.2-1` |

调试时优先看它的场景：

1. apt 安装的 Nav2 包和源码分支行为对不上。
2. 需要确认某个 ROS distro 是否发布了 `nav2_route`、`opennav_docking`、`nav2_mppi_controller` 等包。
3. 需要追溯某个版本的 Bloom release 时间、工具链版本和 release increment。
4. 需要确认生成的 Debian/RPM 包分支和 upstream tarball 标签。

## 疑问与冲突

- README 中部分较新记录仍显示 release repository 为 `SteveMacenski/navigation2-release.git`，而 kilted 记录显示为 `ros2-gbp/navigation2-release.git`；这应理解为历史迁移或 Bloom 元数据保留，不能直接当作当前 canonical 源码位置。
- 仅凭 release 仓库不能判断源码行为差异，必须回查对应 upstream tag 或源码分支。
- ROS distro 与 Nav2 upstream 版本之间不是简单的 `main = 已发布版本` 关系。

## 原料

- `raw/2026-06-24-navigation2-release-repository-snapshot.md`

