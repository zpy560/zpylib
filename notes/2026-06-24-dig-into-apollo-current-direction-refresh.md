---
id: "20260624-dig-into-apollo-current-direction-refresh"
title: "Dig into Apollo：当前项目方向补充"
type: "note"
source: "raw/2026-06-24-dig-into-apollo-current-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - knowledge-management
related:
  - wiki/2026-06-15-dig-into-apollo.md
  - notes/2026-06-15-dig-into-apollo-source-reading-archive.md
  - wiki/2026-06-14-apollo.md
---

# Dig into Apollo：当前项目方向补充

## 一句话结论

Dig into Apollo 当前 HEAD 与旧条目一致，但根 `readme.md` 明确把项目定位从“代码解析”转向“工程智慧”：设计模式、工程权衡、故障复盘和延迟优化。知识库应保留旧代码阅读价值，同时把新定位标成尚待内容落地的方向变化。

## 原文要点

- 根入口是 `readme.md`，不是 `README.md`。
- README 写明项目正在从 code analysis 转向 engineering wisdom。
- 新方向包括 Engineering Philosophy、Problem Diagnosis、Architectural Trade-offs。
- 旧内容被归入 Legacy Deep Dive Archive。
- Legacy 目录仍覆盖 Cyber、Docker、Apollo modules、performance、simulation、library、papers、questions。
- 作者说明正在构建 WheelOS，并希望分享系统如何设计、为什么失败等经验。

## 我的判断

### 方向变化有价值，但不能当作已有内容

README 的新定位更接近高级工程经验库，正好弥补“逐行源码解释容易过时”的问题。但目前知识库结论仍应以旧档案为主，因为已有可检索内容主体仍是 Apollo 历史源码导航。

### 对知识管理的启发更强

这个项目的转向说明大型源码知识库最终会遇到维护瓶颈：纯代码解析会被版本漂移和 AI 解释替代，真正长期有价值的是设计取舍、失败案例、性能优化路径和工程约束。

## 可复用内容

- 把大型源码笔记拆成两层：legacy code map 与 engineering lessons。
- 对每篇源码分析固定 commit，避免跨版本混用。
- 对工程经验记录原因、约束、失败模式和验证证据。

## 疑问与冲突

- 远端 HEAD 与旧条目相同，因此这不是代码增量。
- 新方向对应的 PEP、故障复盘和架构权衡链接目前在 README 中还没有具体内容。
- 本次未逐章复查旧文档。

## 原料

- `raw/2026-06-24-dig-into-apollo-current-repository-snapshot.md`
- `notes/2026-06-15-dig-into-apollo-source-reading-archive.md`
