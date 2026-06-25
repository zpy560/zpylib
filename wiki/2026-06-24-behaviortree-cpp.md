---
id: "20260624-211040-behaviortree-cpp-wiki"
title: "BehaviorTree.CPP"
type: "entity"
source: "notes/2026-06-24-behaviortree-cpp-reactive-behavior-framework.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-behaviortree-cpp-reactive-behavior-framework.md
---

# BehaviorTree.CPP

## 定位

BehaviorTree.CPP 是 C++17 行为树框架，常用于机器人任务执行、行为规划编排和反应式控制流程组织。

## 适合研究的问题

- 行为树如何替代复杂有限状态机。
- asynchronous action、condition、decorator、blackboard 如何组织机器人任务。
- Nav2 这类导航框架如何用 BT 表达导航、恢复和重规划逻辑。

## 使用边界

它不是路径规划器，也不是控制器。它负责行为层编排，底层动作仍由 planner、controller、smoother、recovery 或具体 action server 执行。

## 入库来源

- 单源笔记：../notes/2026-06-24-behaviortree-cpp-reactive-behavior-framework.md
- 仓库：https://github.com/BehaviorTree/BehaviorTree.CPP

