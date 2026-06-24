# CommonRoad/commonroad-drivability-checker repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/CommonRoad/commonroad-drivability-checker
- Clone URL: https://github.com/CommonRoad/commonroad-drivability-checker.git
- Default branch observed: `master`
- HEAD commit: `7127f2e7f960632b3d7ff7805936a1e91b677569`
- Source inspection method: raw README from `master` plus `git ls-remote`

## README facts

- README title: CommonRoad Drivability Checker.
- README contains a deprecation notice: from version 2025.1 the curvilinear coordinate system moved to `commonroad-clcs`.
- The toolbox unifies collision avoidance, kinematic feasibility and road-compliance checks.
- It is compatible with the CommonRoad benchmark suite.
- It can be installed via `pip install commonroad-drivability-checker`.
- The software is written in Python 3.10 and C++17 and tested on macOS and Linux.
- Dependencies for source builds include Eigen3, Boost, Box2D, FCL, libccd and gpc.

## Interpretation boundary

- This is a validation/checking toolbox, not a planner.
- It is valuable for verifying planned motions in benchmark scenarios.

