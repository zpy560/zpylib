# Dig into Apollo 官方仓库快照

> 本文件记录 2026-06-15 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/daohu527/dig-into-apollo
- 在线文档：https://dig-into-apollo.readthedocs.io/
- 抓取分支：`main`
- 抓取提交：`fd68c72323b78cba401b907250d53ac613f266d0`
- 提交时间：`2026-02-03T10:52:52+08:00`
- 提交标题：`docs: Updated the directory and added new shareable content.`
- 抓取方式：Git 浅克隆
- 分析方式：静态文档分析

## 项目定位

Dig into Apollo 是第三方 Apollo 中文源码解读项目。根 README 表示项目正从逐行代码分析转向设计模式、工程权衡和真实问题诊断，现有主体被标记为：

```text
Legacy: Deep Dive Archive (Classic Code Analysis)
```

当前仓库仍主要由历史源码分析文档组成，新的 Engineering Philosophy、Problem Diagnosis 和 Architectural Trade-offs 入口尚未提供实际链接内容。

## 仓库规模

- 浅克隆目录：约 47 MB。
- 文件总数：196。
- Markdown 文件：71。
- Markdown 总行数：约 19761。
- 图片：约 114 张。
- 许可证：MIT。
- 文档构建：Sphinx / Read the Docs。

## 内容结构

### Apollo 基础

- Apollo 是什么、目录结构和编译。
- Docker 开发环境和构建脚本。
- 常见问题、性能调优、仿真、依赖库和论文。

### Cyber RT

- 设计目标与 ROS 替换背景。
- mainboard、DAG、Component 和 classloader。
- Node、Reader、Writer、DataVisitor 和 DataDispatcher。
- 协程、调度器、Timer、异步调用和系统监控。
- Transport、共享内存、RTPS、工具与分布式运行。

`cyber/source/readme.md` 超过 2200 行，是仓库中系统源码分析最完整的部分之一。

### 自动驾驶模块

- Drivers、Canbus、Guardian、Monitor、Transform。
- Map、Localization、NDT 和 MSF。
- Perception：Camera、LiDAR、Radar、Fusion、Inference 和检测组件。
- Prediction：容器、场景、评估器和预测器。
- Routing：拓扑图、子图、A* 路由和调试工具。
- Planning：入口、OnLanePlanning、Planner、Scenario、Stage、Task 和参考线。
- Control：输入、主流程和控制器。
- V2X、Audio、Data 和 Tools。

## 文档体量

较大的文档包括：

- Camera Perception：约 116 KB。
- Cyber 源码分析：约 97 KB。
- CNN 基础与资料：约 55 KB。
- Prediction：约 52 KB。
- Routing：约 46 KB。
- NDT Localization：约 35 KB。
- Perception Detection Component：约 35 KB。
- Planning Reference Line：约 34 KB。
- Map、Planning、Radar、V2X、Transform 和 Simulation 也有长篇分析。

## 版本线索

文档不是基于单一 Apollo 提交编写，明确出现：

- Apollo 2.0
- Apollo 2.5
- Apollo 3.5
- Apollo 5.0
- Apollo 6.0

环境线索包括：

- Ubuntu 16.04 / 18.04。
- CUDA 9.0 / 10.0 / 10.1。
- Bazel 0.18.1。
- Caffe2 和历史 LGSVL。

Planning 文档描述 Apollo 3.5 前后的触发方式和旧版 `standard_planning_config`；Control、Map、Prediction、V2X 等章节也来自不同版本阶段。

因此仓库不对应当前 Apollo 11 的一致源码快照。

## 文档风格

主要方法是：

1. 先解释模块目的和目录结构。
2. 从 Component 或主入口追踪调用链。
3. 粘贴关键源码片段并逐段添加中文注释。
4. 绘制流程图和数据关系图。
5. 记录作者阅读时的问题和 TODO。

这类内容适合建立源码导航和阅读假设，但其中推断、疑问和事实没有统一结构化标记。

## 完成度观察

仓库有 13 个 `todo.md` 文件。部分模块文档为空或极短：

- `modules/dreamview/todo.md`
- `modules/drivers/todo.md`
- `modules/drivers/hesai/readme.md`
- `modules/drivers/velodyne/readme.md`
- `modules/map/todo.md`
- Cyber DDS、Service、IO、Transport 等短文

长文中也保留大量 `TODO`、问号和未验证推断。例如：

- 对锁、原子内存模型和调度策略的疑问。
- Routing 子图和 A* 细节待补。
- Guardian、Control 和 Localization 的问题列表。
- Simulation 原理待补。

## 当前维护状态

最新提交在 2026-02-03，根 README 声明项目将转向工程经验和架构权衡。但当前快照中，新方向的三个入口为空链接，主要可用内容仍是 Legacy 档案。

由于本次是浅克隆，最新提交对大量文件进行了目录更新，不能据文件最后提交时间判断各章节的原始写作时间或是否已按新版 Apollo 逐段复核。

## 使用边界

适合：

- Apollo 模块目录和历史调用链导航。
- Cyber RT、感知、预测、路由和参考线源码阅读。
- 发现关键类、配置和术语。
- 学习“从入口沿调用链阅读大型 C++ 项目”的方法。

不适合：

- 作为 Apollo 11 当前源码的权威说明。
- 直接执行其中的旧环境安装和构建命令。
- 不核验地引用作者的问题、推断或源码片段。
- 替代 Apollo 官方文档和目标提交源码。

## 静态分析边界

- 未逐个验证外部链接和 Read the Docs 构建。
- 未将所有代码片段与对应历史 Apollo 提交逐行匹配。
- 未运行任何 Apollo 命令、仿真或工具。
- 未验证 2026 年重组前后的完整 Git 历史。
