---
id: "20260624-docs-nav2-org"
title: "docs.nav2.org"
type: "entity"
source: "raw/2026-06-24-docs-nav2-org-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-docs-nav2-org-navigation2-documentation-source.md
  - wiki/2026-06-13-navigation2.md
  - wiki/2026-06-24-navigation2-release.md
---

# docs.nav2.org

## 基本信息

- 类型：Navigation2 官方文档站源码
- 官方仓库：https://github.com/ros-navigation/docs.nav2.org
- 文档站：https://docs.nav2.org/
- 快照分支：`master`
- 快照提交：`92e92dfa37778eccde54a2d4d57036f34aadc576`
- 快照日期：2026-06-24

## 当前结论

docs.nav2.org 是理解 Nav2 参数、教程、迁移和概念的官方文档入口。它应与 Navigation2 源码仓库配合使用：文档确认契约和推荐用法，源码确认真实实现和版本细节。

## 核心依据

- README 明确该仓库用于生成 Navigation2 文档网站。
- 支持本地 `make html` 构建。
- 支持 Docker、VS Code Dev Container 和 `sphinx-autobuild`。
- 文档站地址为 https://docs.nav2.org/。

## 不同观点与冲突

- 作为 Nav2 学习入口：优先级高。
- 作为算法实现来源：不适用。
- 作为工程证据：必须记录对应提交或发行版，避免文档与运行代码版本错配。

## 关联笔记

- `notes/2026-06-24-docs-nav2-org-navigation2-documentation-source.md`
- `wiki/2026-06-13-navigation2.md`
- `wiki/2026-06-24-navigation2-release.md`

## 待补资料

- 按具体 Nav2 发行版读取 migration guide。
- 抽取参数页、行为树页、plugin API 页到专题笔记。
- 对比文档说明与 Navigation2 当前源码实现差异。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `92e92df` 首次建档。
