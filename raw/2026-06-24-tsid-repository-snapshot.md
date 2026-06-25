---
id: "20260624-211014-tsid-raw"
title: "TSID repository snapshot"
type: "note"
source: "https://github.com/stack-of-tasks/tsid"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-tsid-task-space-inverse-dynamics.md
---

# TSID repository snapshot

- Repository: `stack-of-tasks/tsid`
- URL: https://github.com/stack-of-tasks/tsid
- Checked HEAD: `3565562ce608dc8be69c0bec294ebb25507527af`
- Checked refs: `devel` at HEAD, `master` at `591f737435f4f84be7844c9b6c59ec1a8792a738`
- README title: `TSID - Task Space Inverse Dynamics`
- License badge: BSD 2-Clause

## README facts

- TSID is a C++ library for optimization-based inverse-dynamics control.
- It is based on Pinocchio.
- Documentation includes a project wiki, exercises and teaching material.
- Examples cover Python usage with robot manipulators, humanoids and quadrupeds.
- Dependencies include Boost, Eigen3, Pinocchio, eiquadprog and example-robot-data for examples.

## Local interpretation

TSID is a control-side optimization library. It belongs in the knowledge base because planning outputs often become task-space references, and TSID shows how to convert task hierarchy and robot dynamics into feasible control commands.

