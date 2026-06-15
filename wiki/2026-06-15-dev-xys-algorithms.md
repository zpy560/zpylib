---
id: "20260615-dev-xys-algorithms"
title: "Dev-XYS Algorithms"
type: "entity"
source: "https://github.com/Dev-XYS/Algorithms"
created_at: "2026-06-15"
tags:
  - programming
  - tools
related:
  - notes/2026-06-15-dev-xys-algorithms-competitive-programming-templates.md
  - wiki/2026-06-15-cpprobotics.md
---

# Dev-XYS Algorithms

## 基本信息

- 类型：C++ 信息学竞赛算法与数据结构模板集
- 作者：Dev-XYS
- 官方仓库：https://github.com/Dev-XYS/Algorithms
- 主要语言：C++
- 许可证：The Unlicense
- 默认分支：`master`
- 协作分支：`candidate`
- 快照提交：`c10d4c212fa1fbf8b9fb3c781d61f41e75e96aaa`
- 最后提交时间：2019-11-01
- 源文件数量：103
- 分析方式：静态源码分析及 C++14 语法编译，未执行正确性测试

## 当前判断

该仓库适合按算法名称查找简短的竞赛实现，不适合作为工程依赖或权威标准答案。所有算法都与 `main()`、标准输入输出和固定容量全局数组绑定，缺少接口文档、复杂度、样例和自动测试。

## 算法范围

- 基础结构：栈、队列、链表、堆、并查集。
- 树结构：树状数组、线段树、Splay、Treap、LCT、树链剖分。
- 图论：最短路、最小生成树、连通性、最大流、匹配、2-SAT。
- 字符串：KMP、Trie、AC 自动机、后缀数组/自动机、回文树。
- 数学：数论筛法、模逆、FFT/NTT、高斯消元、组合计数。
- 几何：凸包、线段关系、多边形重心。
- 排序与选择：常见排序、逆序对和 LIS。
- 持久化结构：数组、线段树、Treap 和 Trie。

## 代码形态

```text
单个 .cpp
→ 固定容量宏与全局数组
→ 算法函数
→ main() 读取和输出
```

没有公共库、构建系统、依赖、测试或 CI。

## 编译检查

C++14 语法检查结果：

- 101/103 通过。
- KMP 因 `gets()` 无法编译。
- 无旋 Treap 因缺少 `<cstring>` 无法编译。

语法通过不等于算法正确，仓库作者也明确不提供正确性担保。

## 最值得利用

- 经典算法名称索引。
- 竞赛式数组实现的最小骨架。
- 同类算法横向比较。
- 高级数据结构的操作流程参考。
- 作为重构与测试练习的原始素材。

## 工程边界

- 2019 年后未更新。
- 输入输出契约依赖阅读源码。
- 固定容量与整数类型可能不适合目标数据。
- 少量说明性注释。
- 指针结构资源管理不完整。
- 特定竞赛题代码与通用模板混合。
- 无性能和正确性回归。

## 关联笔记

- `notes/2026-06-15-dev-xys-algorithms-competitive-programming-templates.md`
- `wiki/2026-06-15-cpprobotics.md`

## 更新记录

- 2026-06-15：基于 `master` 提交 `c10d4c2` 完成算法范围、代码形态、许可证和全量语法编译建档。
