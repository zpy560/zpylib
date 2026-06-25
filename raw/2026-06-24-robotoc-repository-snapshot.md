---
id: "20260624-211022-robotoc-raw"
title: "robotoc repository snapshot"
type: "note"
source: "https://github.com/mayataka/robotoc"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-robotoc-robot-optimal-control-solvers.md
---

# robotoc repository snapshot

- Repository: `mayataka/robotoc`
- URL: https://github.com/mayataka/robotoc
- Checked branch: `master`
- Checked HEAD: `d30d404942835f3804161cda43e0845f653cac09`
- README title: `robotoc - efficient ROBOT Optimal Control solvers`

## README facts

- robotoc provides efficient robot optimal control solvers.
- Features include direct multiple shooting based on lifted contact dynamics and inverse dynamics.
- It includes Riccati recursion for switching time optimization and pure-state equality constraints.
- It includes a primal-dual interior point method for inequality constraints.
- It uses Pinocchio for rigid body dynamics and sensitivities.
- Optional tools include gepetto-viewer, meshcat-python and PyBullet for visualization/simulation.

## Local interpretation

robotoc is relevant for legged/contact-rich optimal control and MPC. It complements OCS2, Crocoddyl, acados and TSID in the knowledge base.

