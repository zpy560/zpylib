# ros/robot_state_publisher repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ros/robot_state_publisher
- Clone URL: https://github.com/ros/robot_state_publisher.git
- Stars observed: 300+
- Forks observed: 200+
- License observed/inferred: BSD
- Primary language/stack: C++
- Category: 机器人状态发布
- Source inspection method: GitHub repository page, README summary, repository description, visible directory names, topics, and public star/fork display checked during this knowledge-base pass.

## Repository facts

- GitHub description / role: Publishes robot state to tf from joint states and URDF.
- The repository was selected only after checking it was not already represented by existing GitHub URLs in `inbox/`, `raw/`, `notes/`, `wiki/`, and `indexes/`.
- It is relevant to planning-control either directly as a planner/controller, or indirectly as localization, transforms, simulation, collision checking, point-cloud processing, optimization, vehicle interface, communication protocol, or fleet infrastructure needed for a mobile chassis closed loop.

## Interpretation boundary

- 底盘和传感器外参需要稳定进入 tf 树，robot_state_publisher 是 ROS 机器人模型到运行时坐标树的基础节点。
- Star/fork counts are coarse popularity signals, not engineering quality proof.
- Before production reuse, inspect target branch code, license, maintenance state, and integration assumptions.
