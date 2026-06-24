# leggedrobotics/ocs2 repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/leggedrobotics/ocs2
- Clone URL: https://github.com/leggedrobotics/ocs2.git
- Default branch observed: `main`
- HEAD commit: `26386754b8bf31ab78b503971d0cbf4fdbcd7cb4`
- Source inspection method: raw README from `main` plus `git ls-remote`

## README facts

- OCS2 stands for Optimal Control for Switched Systems.
- It is a C++ toolbox for nonlinear optimal control with emphasis on real-time MPC for robotics.
- README says ROS 2 port is available on branch `ros2`; `main` is ROS 1.
- Solvers include SLQ, iLQR, SQP, SLP and IPM.
- It supports switched-system OCPs, constraints via Augmented Lagrangian or relaxed barriers, analytic/automatic derivatives, Pinocchio/URDF tooling, ROS interfaces and robotic examples.
- Repository structure includes `ocs2_core`, `ocs2_oc`, `ocs2_ddp`, `ocs2_mpc`, `ocs2_sqp`, `ocs2_slp`, `ocs2_ipm`, `ocs2_pinocchio`, `ocs2_ros_interfaces`, `ocs2_robotic_examples`, `ocs2_python_interface`, `ocs2_mpcnet`, `ocs2_doc`.
- License is BSD 3-Clause.

## Interpretation boundary

- OCS2 is a robotics optimal control toolbox, not a general navigation stack.
- It is most relevant for real-time MPC on robots with rich dynamics, including legged robots, quadrotors and mobile manipulators.

