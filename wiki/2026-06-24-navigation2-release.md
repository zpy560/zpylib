---
id: "20260624-navigation2-release"
title: "navigation2-release"
type: "entity"
source: "raw/2026-06-24-navigation2-release-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-navigation2-release-bloom-release-metadata.md
  - wiki/2026-06-13-navigation2.md
  - wiki/2026-06-24-docs-nav2-org.md
---

# navigation2-release

## 基本信息

- 类型：Navigation2 Bloom release 仓库
- 官方仓库：https://github.com/ros2-gbp/navigation2-release
- 上游源码：https://github.com/ros-planning/navigation2.git
- 快照分支：`master`
- 快照提交：`48c11ee63a39eafbec6d4754f4a414a7fc4ca007`
- 快照日期：2026-06-24

## 当前结论

navigation2-release 是 Nav2 的 ROS 发行版发布元数据仓库。它回答“哪个 ROS distro 发布了哪个 Nav2 版本和哪些包”，不回答“算法怎么实现”。调试二进制包行为时，它应夹在 apt 包版本和 Navigation2 源码之间，用来锁定正确的 upstream 版本。

## 核心依据

- 仓库说明明确是 Navigation2 metapackage 的 Bloom Release Repository。
- `tracks.yaml` 记录 bouncy 到 kilted 的 Bloom tracks。
- `README.md` 记录每次 bloom-release 的 distro、版本、包清单、时间和工具链版本。
- 远端 refs 中存在大量 `debian/*`、`release/*`、`rpm/*`、`upstream/*` 分支和标签。
- 近期 track 版本包括 Humble `1.1.20`、Jazzy `1.3.12`、Kilted `1.4.2`。

## 不同观点与冲突

- 作为版本溯源：优先级高。
- 作为源码学习：不适用。
- 作为 Nav2 能力判断：只能证明包是否进入发行版，不能替代源码和文档确认接口语义。
- README 中历史 release repository 字段混有 `SteveMacenski/navigation2-release.git` 和 `ros2-gbp/navigation2-release.git`，应按具体记录理解历史迁移。

## 关联笔记

- `notes/2026-06-24-navigation2-release-bloom-release-metadata.md`
- `wiki/2026-06-13-navigation2.md`
- `wiki/2026-06-24-docs-nav2-org.md`

## 待补资料

- 对照 ROS distro 官方 rosdistro 索引确认当前 apt 发布版本。
- 按 Humble/Jazzy/Kilted 分别回查 upstream tag 与 Navigation2 源码差异。
- 建立 Nav2 版本、包清单和功能模块的对照表。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `48c11ee` 首次建档。

