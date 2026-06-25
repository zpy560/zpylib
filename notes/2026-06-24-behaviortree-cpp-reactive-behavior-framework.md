---
id: "20260624-211039-behaviortree-cpp-note"
title: "BehaviorTree.CPP：机器人行为树与任务编排框架"
type: "note"
source: "raw/2026-06-24-behaviortree-cpp-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-behaviortree-cpp.md
---

# BehaviorTree.CPP：机器人行为树与任务编排框架

## 结论

BehaviorTree.CPP 不属于轨迹规划或控制算法，但它属于规划控制系统的行为编排层。对于 Nav2、机器人任务执行、恢复行为和异步 action 组织，它是必须保留的基础资料。

## 事实摘录

- 远端仓库：`BehaviorTree/BehaviorTree.CPP`
- 当前核对 HEAD：`8068d683814870a222c3c491b6a81cebf737116c`
- README 定位：C++17 behavior tree framework。
- 主要 use case 是 robotics。
- 特性包括 asynchronous actions、reactive behaviors、XML runtime tree loading、plugin nodes、type-safe dataflow、logging/profiling。
- README 指向 `behaviortree.dev` 和 Groot2。

## 对规划控制的意义

- 对导航系统：行为树负责把导航、重规划、恢复、等待、清图等动作组织为可解释执行流。
- 对控制系统：它不替代控制器，但能调度控制模式和任务状态。
- 对工程：XML tree 和 plugin node 让行为逻辑可配置、可扩展、可视化。

## 使用建议

结合 Nav2 的 BT Navigator 和 XML 行为树一起读。重点看 async action、condition、decorator、blackboard/dataflow 和 runtime plugin loading。

