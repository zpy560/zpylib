---
id: "20260624-docs-nav2-org-navigation2-documentation-source"
title: "docs.nav2.org：Navigation2 官方文档源码"
type: "note"
source: "raw/2026-06-24-docs-nav2-org-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-docs-nav2-org.md
  - wiki/2026-06-13-navigation2.md
  - notes/2026-06-24-navigation2-release-bloom-release-metadata.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
---

# docs.nav2.org：Navigation2 官方文档源码

## 一句话结论

docs.nav2.org 是 Navigation2 官方文档站的源码仓库，价值在于提供版本化文档、教程和配置说明的构建入口；它不是 Nav2 运行时代码，但应作为理解 Nav2 API、参数、迁移说明和教程的第一文档来源。

## 原文要点

- 仓库用于生成 https://docs.nav2.org/ 文档网站。
- 支持本地 Python/pip 安装依赖后构建。
- 支持 `venv` 隔离环境。
- 支持 Docker 构建和 `make html`。
- 支持 `make autobuild` 或 `sphinx-autobuild` 本地热更新预览。
- 支持 VS Code Dev Container。
- 构建产物入口是 `_build/html/index.html`。
- 图片、图表和视频可能有独立版权、商标和许可。

## 我的判断

### 它是 Nav2 知识入口，不是算法源码

Navigation2 主仓库适合看实现边界，docs.nav2.org 更适合确认概念解释、参数语义、配置示例、迁移说明和教程路径。调试 Nav2 时，先用文档确认接口契约，再回源码验证实现细节。

### 文档仓库也应版本化

Nav2 的行为树、server、plugin、参数和发行版差异变化较快。引用文档时必须记录文档仓库提交或文档站版本，否则容易把新文档套到旧运行环境上。

## 可复用内容

- Sphinx 文档站本地构建流程。
- Docker/Dev Container 文档开发环境。
- Nav2 参数、教程和迁移说明的官方入口。
- 与 Navigation2 源码条目联动，形成“文档契约 + 源码实现”双线索。

## 疑问与冲突

- 本次未逐页抓取文档内容，因此没有分析具体教程或参数页。
- 文档页面与 Navigation2 源码版本的对应关系需要按具体发行版继续确认。
- README 未直接说明许可证，媒体资源还可能有独立限制。

## 原料

- `raw/2026-06-24-docs-nav2-org-repository-snapshot.md`
