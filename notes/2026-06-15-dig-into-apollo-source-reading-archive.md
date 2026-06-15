---
id: "20260615-dig-into-apollo-source-reading-archive"
title: "Dig into Apollo：跨版本 Apollo 中文源码阅读档案"
type: "note"
source: "raw/2026-06-15-dig-into-apollo-repository-snapshot.md"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - knowledge-management
related:
  - wiki/2026-06-15-dig-into-apollo.md
  - notes/2026-06-14-apollo-autonomous-driving-platform.md
---

# Dig into Apollo：跨版本 Apollo 中文源码阅读档案

## 一句话结论

Dig into Apollo 是一套覆盖 Cyber RT 和 Apollo 主要业务模块的中文源码阅读档案，长篇调用链与注释适合建立 Apollo 历史架构认知；但文档横跨 Apollo 2.0 至 6.0，包含大量未验证问题和未完成章节，不能直接映射到 Apollo 11，使用时必须回到目标版本源码逐项核验。

## 原文要点

### 覆盖范围广

仓库用约 2 万行 Markdown 覆盖：

```text
系统介绍与构建
→ Cyber RT
→ Drivers / Canbus / Guardian / Monitor
→ Map / Localization
→ Perception / Prediction
→ Routing / Planning / Control
→ V2X / Simulation / Performance / Tools
```

其中 Cyber、Camera Perception、Prediction、Routing、NDT、Planning Reference Line 和 Map 的篇幅最大。

### 阅读方法以调用链为中心

文档通常从模块入口类开始：

- Cyber 从 `mainboard`、`ModuleController` 和 `Component` 展开。
- Planning 从 `PlanningComponent`、`OnLanePlanning`、Planner、Scenario 和 Task 展开。
- Prediction 从 Component 进入消息处理、容器、Evaluator 和 Predictor。
- Routing 从地图拓扑创建、请求处理和 A* 搜索展开。
- Perception 按 Component、Detector、Tracker、Fusion 和后处理展开。

这种方法比按目录顺序阅读更有效，因为它先回答“数据如何流动”，再进入算法细节。

### 作者主动保留疑问

文档没有把所有代码都包装成确定结论，而是保留：

- 为什么加锁、使用原子变量或特定容器。
- 为什么采用某种调度、变换或配置。
- 某些 TODO 分支是否完整。
- 模块设计是否可以简化。

这能暴露真正的理解难点，但这些内容仍是阅读过程记录，不是已经验证的工程结论。

### 项目正在转型

根 README 在 2026 年提出从代码解释转向：

- 设计模式。
- 工程权衡。
- 故障复盘。
- 延迟优化。

但当前快照中这些新入口仍为空，主体仍是历史代码分析档案。

## 我的判断

### 最有价值的是源码导航，而不是版本答案

对于第一次阅读 Apollo 的人，仓库能快速指出：

- 应从哪个 Component 或入口开始。
- 哪些类负责数据聚合和分发。
- 哪些配置、DAG 和 protobuf 与代码共同决定行为。
- 一个模块内部的核心数据结构和调用顺序。

它可以显著降低“面对大型仓库不知道从哪里读”的成本。

但它无法回答“当前 Apollo 11 实际如何运行”，因为文档中的环境和代码来自多个历史版本。

### 正确使用方式是三方对照

```text
Dig into Apollo 提供阅读地图
→ Apollo 官方文档确认公开设计
→ 目标 Git 提交确认真实实现
```

任何类名、配置路径、Topic、模块链和算法结论，都应在目标版本源码中重新搜索。找不到时，不应强行套用旧文档。

### 与现有 Apollo 源码档案互补

现有知识库 Apollo 档案基于本地 `v11.0.0-10` 附近源码，重点分析当前规划、控制、插件和安全执行链。

Dig into Apollo 提供：

- Cyber RT 更细的历史实现讲解。
- 感知、预测、定位、地图和路由的长篇导航。
- 旧版 Planning 与参考线机制的阅读材料。
- 构建、Docker、性能和仿真背景。

两者关系是“当前源码快照 + 历史阅读手册”，不能互相替代。

### 主要风险

1. **版本漂移**：Apollo 2.0 至 6.0 内容混合，当前 Apollo 已到 11 系列。
2. **路径漂移**：模块目录、配置、插件和消息可能已经迁移。
3. **环境过时**：Ubuntu 16.04/18.04、CUDA 9/10、Bazel 0.18 和 Caffe2 说明不适合作为当前安装指南。
4. **完成度不一**：部分章节很长，部分为空，13 个 TODO 文件仍保留。
5. **事实与推断混合**：源码事实、作者解释和未验证疑问没有统一标记。
6. **重组不等于更新**：2026 年最新提交调整了目录与定位，不能证明全部旧文档已按当前源码复核。

### 对知识管理的启发

该项目展示了大型源码知识库常见问题：

- 按模块积累容易形成跨版本混杂。
- 长文逐行注释难以持续维护。
- 没有记录目标提交时，后续读者无法判断结论适用性。
- TODO 和推断需要与事实分层，否则搜索结果会误导。

更可维护的做法是每篇分析固定提交、记录入口与关键链路，并把“源码事实、作者判断、待验证问题”分开。

## 可复用内容

### Apollo 源码阅读顺序

1. 明确要解决的问题和目标 Apollo 提交。
2. 找 Component、DAG、launch 和入口配置。
3. 画出 Topic 输入输出和主调用链。
4. 识别周期数据对象与跨周期状态。
5. 同时检查 protobuf、gflags 和插件注册。
6. 沿最终执行输出反向检查安全和兜底。
7. 用 record、仿真或单元测试验证静态判断。

### 使用本仓库的核验清单

1. 文档明确对应哪个 Apollo 版本？
2. 类和文件在目标提交中是否仍存在？
3. 配置格式和插件机制是否已经变化？
4. 文档代码片段是否完整保留上下文？
5. 结论是源码事实、作者解释还是未验证问题？
6. 官方文档和目标源码是否支持该结论？

## 疑问与冲突

- 根 README 的新工程经验方向尚未形成可访问内容，后续价值取决于实际更新。
- 每个历史章节具体对应的 Apollo commit 没有统一记录，精确溯源成本较高。
- 文档中的部分源码链接指向 Apollo `master`，链接内容会随时间变化，不等于写作时版本。
- 本次没有逐章与 Apollo 11 源码做完整差异对照。

## 原料

- `raw/2026-06-15-dig-into-apollo-repository-snapshot.md`
