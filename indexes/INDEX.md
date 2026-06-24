# 知识库总索引

> 本文件是生成式导航。新增笔记、主题页或选题后同步更新。

## 统计

| 类型 | 数量 |
|---|---:|
| 单源笔记 | 39 |
| 主题页 | 0 |
| 实体页 | 33 |
| 选题 | 0 |

## 主题页

暂无。

## 实体页
- [OCS2](../wiki/2026-06-24-ocs2.md)：机器人实时最优控制工具箱；覆盖 switched systems、DDP/iLQR/SQP/IPM、Pinocchio/URDF 和 ROS 接口，适合复杂机器人 MPC。
- [do-mpc](../wiki/2026-06-24-do-mpc.md)：Python nonlinear/robust MPC 与 MHE 工具箱；适合建模、仿真和研究原型，不默认等价于嵌入式实时控制器。
- [CasADi](../wiki/2026-06-24-casadi.md)：符号建模、自动微分和优化接口工具；常与 Ipopt、acados、do-mpc 组合用于 MPC/OCP 原型。
- [Ipopt](../wiki/2026-06-24-ipopt.md)：大规模光滑非线性优化求解器；适合作为轨迹优化和非线性 MPC 原型后端，只保证局部解。
- [OSQP](../wiki/2026-06-24-osqp.md)：Operator Splitting QP 求解器；适合路径平滑、线性 MPC 和凸 QP 子问题。
- [acados](../wiki/2026-06-24-acados.md)：实时非线性最优控制求解器；面向 NMPC、MHE、OCP 和嵌入式应用。
- [MoveIt 2](../wiki/2026-06-24-moveit2.md)：ROS 2 机械臂运动规划框架；整合机器人模型、规划场景、碰撞检测、规划器和执行接口。
- [OMPL](../wiki/2026-06-24-ompl.md)：采样式运动规划算法库；覆盖 RRT、PRM、KPIECE、RRT* 等算法和多状态空间。
- [MotionPlanning](../wiki/2026-06-24-motionplanning.md)：自动驾驶规划控制 Python 示例；覆盖 Hybrid A*、Frenet、Pure Pursuit、Stanley、LQR、MPC。
- [PythonRobotics](../wiki/2026-06-24-pythonrobotics.md)：机器人规划控制算法教材式代码库；适合建立算法谱系和做快速实验。
- [navigation2-release](../wiki/2026-06-24-navigation2-release.md)：Nav2 的 Bloom 发布元数据仓库；用于确认 ROS distro、发布版本、包清单和 upstream tag，不是源码实现入口。
- [TheAlgorithms C-Plus-Plus](../wiki/2026-06-24-thealgorithms-c-plus-plus.md)：C++17 教学算法集合；目录覆盖广，README 声称跨平台 CI、self-check 和 Doxygen 文档，适合学习索引不等同生产库。
- [xtaci Algorithms](../wiki/2026-06-24-xtaci-algorithms.md)：C++ 单头文件算法与数据结构示例集；一个算法一个 header、一个 demo，适合读经典实现。
- [YoungTimes Algorithms](../wiki/2026-06-24-youngtimes-algorithms.md)：Frenet、离散点平滑、MPC 与 polynomial spiral 的小型算法示例集合；缺少根 README 和许可证，适合读片段不适合直接依赖。
- [Full Coverage Path Planner](../wiki/2026-06-24-full-coverage-path-planner.md)：ROS1/MBF 覆盖路径规划插件；用 Backtracking Spiral Algorithm 生成区域全覆盖路径，并区分机器人半径与工具半径。
- [ros2_controllers](../wiki/2026-06-24-ros2-controllers.md)：ros2_control 通用控制器插件集合；覆盖移动底盘、关节轨迹、PID、导纳、夹爪和状态 broadcaster。
- [ros2_control](../wiki/2026-06-24-ros2-control.md)：ROS 2 硬件抽象与控制器管理框架；核心价值是接口资源管理、生命周期和 `read → update → write` 实时主循环。
- [Navigation2 Tutorials](../wiki/2026-06-24-navigation2-tutorials.md)：Nav2 官方教程代码集合；适合学习插件注册、Lifecycle、costmap 扩展和感知集成，不是生产算法库。
- [planning_algorithm](../wiki/2026-06-15-planning-algorithm.md)：仅包含 A* 与 RRT 的 OpenCV 最小演示；可构建，但实现省略了关键正确性处理。
- [Hybrid A Star](../wiki/2026-06-15-hybrid-a-star.md)：ROS1 车辆三维状态栅格路径搜索实现；包含 Reeds-Shepp 解析扩展，但默认代码存在多项搜索正确性问题。
- [chhRobotics_CPP](../wiki/2026-06-15-chhrobotics-cpp.md)：自动驾驶路径规划与轨迹跟踪 C++ 可视化演示集；适合结合中文博客学习，MPC、构建和数值正确性仍有明显缺口。
- [Dev-XYS Algorithms](../wiki/2026-06-15-dev-xys-algorithms.md)：覆盖 103 个经典算法与数据结构的 C++ 单文件竞赛模板集；适合查阅，不是经过测试的算法库。
- [MPCC](../wiki/2026-06-15-mpcc.md)：将路径进度纳入优化的自主赛车预测控制参考实现；重点关注 contouring/lag error、SQP、HPIPM 与轮胎约束。
- [Dig into Apollo](../wiki/2026-06-15-dig-into-apollo.md)：跨 Apollo 2.0 至 6.0 的中文源码阅读档案；适合历史调用链导航，使用时需回查目标版本源码。
- [CppRobotics](../wiki/2026-06-15-cpprobotics.md)：经典机器人定位、规划与控制算法的 C++ 可视化示例集；适合学习，不是工程算法库。
- [RTAB-Map](../wiki/2026-06-15-rtabmap.md)：带长期记忆、外观回环、多传感器里程计和图优化后端的 SLAM 库与应用。
- [Easy-RL](../wiki/2026-06-15-easy-rl.md)：中文强化学习教材、习题、Notebook 与经典论文资源；适合系统入门，不是生产级训练框架。
- [CVPR2026-Papers-with-Code](../wiki/2026-06-15-cvpr2026-papers-with-code.md)：持续更新的 CVPR 2026 论文、代码与项目页社区索引；适合作为发现入口，不替代官方论文集。
- [ROS Motion Planning](../wiki/2026-06-14-ros-motion-planning.md)：ROS1 运动规划算法工作台；统一比较图搜索、采样、进化规划和局部控制算法。
- [Autoware](../wiki/2026-06-14-autoware.md)：ROS 2 原生自动驾驶平台；重点关注多仓库装配、规划插件流水线、控制门控与独立安全检查。
- [Build Your Own X](../wiki/2026-06-14-build-your-own-x.md)：从零实现技术的教程索引；适合围绕真实问题选择项目并用实现理解系统原理。
- [Apollo](../wiki/2026-06-14-apollo.md)：完整自动驾驶平台；重点关注 Cyber RT、Scenario/Stage/Task 规划链、控制插件和实际安全执行链。
- [Navigation2](../wiki/2026-06-13-navigation2.md)：ROS 2 移动机器人导航框架；重点关注行为树编排、插件化服务器、生命周期与末端安全链。

## 最近笔记
- 2026-06-24：[OCS2：机器人实时最优控制工具箱](../notes/2026-06-24-ocs2-real-time-optimal-control-toolbox.md)
- 2026-06-24：[do-mpc：Python 非线性与鲁棒 MPC 工具箱](../notes/2026-06-24-do-mpc-python-mpc-toolbox.md)
- 2026-06-24：[CasADi：符号建模与优化工具链](../notes/2026-06-24-casadi-symbolic-optimization-framework.md)
- 2026-06-24：[Ipopt：大规模非线性优化求解器](../notes/2026-06-24-ipopt-large-scale-nonlinear-optimizer.md)
- 2026-06-24：[OSQP：Operator Splitting 二次规划求解器](../notes/2026-06-24-osqp-operator-splitting-qp-solver.md)
- 2026-06-24：[acados：实时非线性 MPC 与 OCP 求解器](../notes/2026-06-24-acados-real-time-nmpc-solver.md)
- 2026-06-24：[MoveIt 2：ROS 2 机械臂运动规划框架](../notes/2026-06-24-moveit2-ros2-manipulation-motion-planning.md)
- 2026-06-24：[OMPL：采样式运动规划算法库](../notes/2026-06-24-ompl-sampling-based-motion-planning-library.md)
- 2026-06-24：[MotionPlanning：自动驾驶规划与跟踪控制 Python 示例](../notes/2026-06-24-motionplanning-autonomous-driving-planning-control-demos.md)
- 2026-06-24：[PythonRobotics：机器人规划控制算法教材式代码库](../notes/2026-06-24-pythonrobotics-robotics-algorithm-textbook.md)
- 2026-06-24：[navigation2-release：Nav2 的 Bloom 发布元数据仓库](../notes/2026-06-24-navigation2-release-bloom-release-metadata.md)
- 2026-06-24：[Apollo：当前远端状态确认](../notes/2026-06-24-apollo-current-status-refresh.md)
- 2026-06-24：[Dev-XYS Algorithms：当前状态确认](../notes/2026-06-24-dev-xys-algorithms-current-status-refresh.md)
- 2026-06-24：[Dig into Apollo：当前项目方向补充](../notes/2026-06-24-dig-into-apollo-current-direction-refresh.md)
- 2026-06-24：[planning_algorithm：当前状态确认](../notes/2026-06-24-planning-algorithm-current-status-refresh.md)
- 2026-06-24：[TheAlgorithms/C-Plus-Plus：C++17 教学算法集合](../notes/2026-06-24-thealgorithms-c-plus-plus-educational-algorithm-library.md)
- 2026-06-24：[Autoware：当前 meta-repository 与版本清单补充](../notes/2026-06-24-autoware-current-meta-repository-refresh.md)
- 2026-06-24：[xtaci/algorithms：C++ 单头文件算法与数据结构示例集](../notes/2026-06-24-xtaci-algorithms-cpp-header-demos.md)
- 2026-06-24：[YoungTimes Algorithms：Frenet、平滑、MPC 与 Spiral 示例集合](../notes/2026-06-24-youngtimes-algorithms-planning-demos.md)
- 2026-06-24：[ROS Motion Planning：当前仓库状态补充](../notes/2026-06-24-ros-motion-planning-current-repository-refresh.md)
- 2026-06-24：[Full Coverage Path Planner：ROS1 覆盖路径规划插件](../notes/2026-06-24-full-coverage-path-planner-ros1-coverage-planner.md)
- 2026-06-24：[ros2_controllers：ros2_control 的通用控制器插件集合](../notes/2026-06-24-ros2-controllers-common-controller-plugins.md)
- 2026-06-24：[ros2_control：ROS 2 硬件抽象与控制器管理框架](../notes/2026-06-24-ros2-control-hardware-controller-framework.md)
- 2026-06-24：[Navigation2 Tutorials：Nav2 插件与集成教程代码集合](../notes/2026-06-24-navigation2-tutorials-nav2-plugin-and-integration-examples.md)
- 2026-06-15：[planning_algorithm：A* 与 RRT 的 OpenCV 最小演示](../notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md)
- 2026-06-15：[Hybrid A Star：ROS1 车辆三维状态栅格路径搜索实现](../notes/2026-06-15-hybrid-a-star-ros1-vehicle-path-planner.md)
- 2026-06-15：[chhRobotics_CPP：自动驾驶规划与跟踪控制 C++ 演示集](../notes/2026-06-15-chhrobotics-cpp-planning-control-demos.md)
- 2026-06-15：[Dev-XYS Algorithms：单文件 C++ 竞赛算法模板集](../notes/2026-06-15-dev-xys-algorithms-competitive-programming-templates.md)
- 2026-06-15：[MPCC：将路径进度纳入优化的自主赛车预测控制](../notes/2026-06-15-mpcc-model-predictive-contouring-control.md)
- 2026-06-15：[Dig into Apollo：跨版本 Apollo 中文源码阅读档案](../notes/2026-06-15-dig-into-apollo-source-reading-archive.md)
- 2026-06-15：[CppRobotics：机器人定位、规划与控制的 C++ 可视化示例集](../notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md)
- 2026-06-15：[RTAB-Map：带长期记忆和多传感器后端的图优化 SLAM](../notes/2026-06-15-rtabmap-long-term-appearance-based-slam.md)
- 2026-06-15：[Easy-RL：从强化学习基础到深度算法的中文教程](../notes/2026-06-15-easy-rl-chinese-reinforcement-learning-tutorial.md)
- 2026-06-15：[CVPR2026-Papers-with-Code：持续更新的论文与代码追踪目录](../notes/2026-06-15-cvpr2026-papers-with-code-tracking-index.md)
- 2026-06-14：[ROS Motion Planning：统一实验环境下的规划算法工作台](../notes/2026-06-14-ros-motion-planning-algorithm-workbench.md)
- 2026-06-14：[Autoware：ROS 2 原生的模块化自动驾驶平台](../notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md)
- 2026-06-14：[Build Your Own X：通过重建系统学习技术原理](../notes/2026-06-14-build-your-own-x-learning-by-reimplementation.md)
- 2026-06-14：[Apollo：插件化自动驾驶平台与规划控制主链](../notes/2026-06-14-apollo-autonomous-driving-platform.md)
- 2026-06-13：[Navigation2：ROS 2 移动机器人导航框架](../notes/2026-06-13-navigation2-ros2-navigation-framework.md)

## 选题

暂无。
