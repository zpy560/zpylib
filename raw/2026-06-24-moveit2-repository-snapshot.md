# moveit/moveit2 repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/moveit/moveit2
- Clone URL: https://github.com/moveit/moveit2.git
- Default branch observed: `main`
- HEAD commit: `4a766fd1ba7798822c8e5997ba8c18ecdff2f113`
- Source inspection method: raw README from `main` plus `git ls-remote`

## README facts

- MoveIt 2 is described as the MoveIt Motion Planning Framework for ROS 2.
- It is an open source robotics manipulation platform for commercial applications, prototyping and benchmarking.
- README points to tutorials and documentation at `moveit.picknik.ai`.
- Branch policy: `main` is development for all active distros and rolling; `humble`, `jazzy`, `kilted` are stable release branches for specific distros.
- Buildfarm table includes packages such as `moveit_core`, `moveit_planners`, `moveit_kinematics`, `moveit_ros_move_group`, `moveit_servo`, `moveit_task_constructor`.

## Interpretation boundary

- MoveIt 2 is a manipulation planning framework, not a mobile robot navigation stack.
- It typically consumes OMPL and other planners and integrates kinematics, planning scene, collision checking, execution and ROS 2 interfaces.

