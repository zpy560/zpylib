# ZJU-FAST-Lab/ego-planner repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ZJU-FAST-Lab/ego-planner
- Clone URL: https://github.com/ZJU-FAST-Lab/ego-planner.git
- Default branch observed: `master`
- HEAD commit: `bfda51284c8c1b476043255a8145ef925a3778a5`
- Source inspection method: raw README from `master` plus `git ls-remote`

## README facts

- README says EGO-Swarm is an evolution from EGO-Planner and is more recommended.
- ROS2 support is referred to the `ros2_version` branch of ego-planner-swarm.
- Quick start says compilation tests passed on Ubuntu 16.04, 18.04 and 20.04 with ROS installed.
- EGO-Planner is described as an ESDF-free gradient-based local planner for quadrotors.
- README says total planning time is around 1 ms and ESDF computation is not needed.
- The framework is based on Fast-Planner.

## Interpretation boundary

- EGO-Planner is a quadrotor local planner, not a generic autonomous driving planner.
- README itself points users toward EGO-Swarm for a newer, more robust and safer planner.

## Verification on 2026-07-13

- Remote `master` and `HEAD` still resolve to `bfda51284c8c1b476043255a8145ef925a3778a5`.
- The latest commit date is 2025-03-08; the commit only updates `README.md`.
- The repository is a ROS 1 catkin workspace. The README lists Ubuntu 16.04, 18.04 and 20.04 as tested systems and uses `catkin_make`.
- Planner packages are split into `plan_env`, `path_searching`, `bspline_opt`, `plan_manage` and `traj_utils`; the repository also bundles a UAV simulator.
- Source inspection confirms a local occupancy grid accepting depth images or point clouds, an A* initializer, uniform B-spline trajectory representation and optimization, and an FSM that triggers replanning, collision checks and emergency stops.
- The optimizer uses the lightweight header-only `LBFGS-Lite`; the simulator requires Armadillo. The optional `local_sensing` CUDA path only affects simulated depth rendering.
- The repository-level license is GPLv3. Several bundled ROS package manifests still contain `TODO` license fields or use their own BSD/LGPL/GPL declarations, so redistribution requires file-level license review.
- The modified RealSense driver is tied to librealsense2 2.30.0 and D435/D435i-era hardware assumptions; it should not be treated as a current generic camera integration path.
