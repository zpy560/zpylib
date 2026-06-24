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

