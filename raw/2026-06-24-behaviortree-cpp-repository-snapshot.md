---
id: "20260624-211038-behaviortree-cpp-raw"
title: "BehaviorTree.CPP repository snapshot"
type: "note"
source: "https://github.com/BehaviorTree/BehaviorTree.CPP"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-behaviortree-cpp-reactive-behavior-framework.md
---

# BehaviorTree.CPP repository snapshot

- Repository: `BehaviorTree/BehaviorTree.CPP`
- URL: https://github.com/BehaviorTree/BehaviorTree.CPP
- Checked branch: `master`
- Checked HEAD: `8068d683814870a222c3c491b6a81cebf737116c`
- README title: `BehaviorTree.CPP 4.9`
- License badge: MIT

## README facts

- BehaviorTree.CPP is a C++17 framework to create behavior trees.
- It is designed to be flexible, easy to use, reactive and fast.
- The main use case is robotics, but it can also be used for game AI or replacing finite state machines.
- Features include asynchronous non-blocking actions, reactive behaviors with concurrent actions, XML-based tree definitions loaded at runtime, plugins, type-safe dataflow and logging/profiling.
- Documentation is hosted at `behaviortree.dev`; Doxygen is hosted on GitHub Pages.
- README references Groot2 as a GUI editor.

## Local interpretation

BehaviorTree.CPP is not a path planner or controller, but it is central to behavior-level planning orchestration. Nav2 uses behavior trees conceptually for navigation task execution and recovery logic.

