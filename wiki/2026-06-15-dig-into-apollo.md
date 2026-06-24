---
id: "20260615-dig-into-apollo"
title: "Dig into Apollo"
type: "entity"
source: "https://github.com/daohu527/dig-into-apollo"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - knowledge-management
related:
  - notes/2026-06-15-dig-into-apollo-source-reading-archive.md
  - notes/2026-06-24-dig-into-apollo-current-direction-refresh.md
  - wiki/2026-06-14-apollo.md
---

# Dig into Apollo

## 基本信息

- 类型：Apollo 中文源码解读与工程经验项目
- 作者：daohu527
- 官方仓库：https://github.com/daohu527/dig-into-apollo
- 在线文档：https://dig-into-apollo.readthedocs.io/
- 许可证：MIT
- 快照分支：`main`
- 快照提交：`fd68c72323b78cba401b907250d53ac613f266d0`
- 快照日期：2026-06-15

## 当前判断

Dig into Apollo 是 Apollo 历史源码阅读的高价值中文导航，尤其适合 Cyber、感知、预测、路由、参考线、地图和定位模块。

它不是当前 Apollo 的版本化官方文档。内容横跨 Apollo 2.0 至 6.0，必须与目标提交源码对照使用。

## 内容规模

- 71 个 Markdown 文件。
- 约 19761 行文档。
- 约 114 张图片。
- 13 个 TODO 文件。
- Sphinx / Read the Docs 文档入口。

## 重点内容

- Cyber RT：Component、Node、通信、协程、调度、Timer 和 classloader。
- Perception：Camera、LiDAR、Radar、Fusion 和检测组件。
- Prediction：容器、场景、Evaluator 和 Predictor。
- Planning：入口、Planner、Scenario、Task 和参考线。
- Routing：拓扑图、子图、A* 和调试。
- Localization：RTK、MSF 和 NDT。
- Map、Control、Canbus、V2X、Simulation 和 Performance。

## 推荐使用方式

```text
用本仓库定位入口和调用链
→ 用 Apollo 官方文档确认设计
→ 用目标 Git 提交验证代码与配置
→ 用运行数据验证静态结论
```

## 主要边界

- 大量内容基于 Apollo 3.5 前后。
- 部分模块明确来自 Apollo 2.0、2.5、5.0 或 6.0。
- Ubuntu、CUDA、Bazel 和 Caffe2 环境说明已经过时。
- 部分章节为空或未完成。
- 作者疑问与源码事实混合存在。
- 2026 年目录重组不代表全部章节完成新版复核。

## 与 Apollo 档案的关系

知识库中的 Apollo 实体基于本地 Apollo 11 附近源码，负责当前实现判断；Dig into Apollo 负责提供历史模块导航和中文阅读材料。

## 关联笔记

- `notes/2026-06-15-dig-into-apollo-source-reading-archive.md`
- `notes/2026-06-24-dig-into-apollo-current-direction-refresh.md`
- `wiki/2026-06-14-apollo.md`

## 更新记录

- 2026-06-15：基于官方 `main` 提交 `fd68c72` 完成文档范围、版本适用性和维护风险建档。
- 2026-06-24：确认远端 HEAD 仍为 `fd68c72`；补充根 `readme.md` 中从代码分析转向工程经验的当前定位。
