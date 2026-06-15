# CppRobotics 官方仓库源码快照

> 本文件记录 2026-06-15 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/onlytailei/CppRobotics
- 上游项目：https://github.com/AtsushiSakai/PythonRobotics
- 抓取分支：`master`
- 抓取提交：`e30a914c91eda87da068c076d942bb6251ba95cc`
- 提交时间：`2023-07-15T21:38:33+08:00`
- 提交标题：`Merge pull request #14 from onlytailei/tailei_revise`
- 抓取方式：Git 浅克隆
- 分析方式：静态源码分析，未编译、未运行 GUI

## 项目定位

README 将 CppRobotics 定义为 PythonRobotics 的 C++ 实现。项目目标是用短小、可视化的 C++ 示例展示机器人定位、路径规划和路径跟踪算法。

它不是统一库或机器人运行框架。每个算法基本是一个独立可执行程序，场景和参数写在源码 `main()` 中，通过 OpenCV 窗口或图片显示结果。

## 仓库规模

- 浅克隆目录：约 13 MB。
- 跟踪文件：42 个。
- C++ 源文件：14 个。
- C++ 头文件：11 个。
- GIF/PNG 演示资源：13 个。
- 许可证：MIT。
- 主要依赖：CMake、C++11、Eigen3、OpenCV。
- MPC 额外依赖：CppAD 与 IPOPT。

## 实际源码覆盖

### 定位

- 扩展卡尔曼滤波定位。
- 粒子滤波定位。

### 路径与轨迹规划

- Dijkstra。
- A*。
- RRT。
- RRT*。
- Dynamic Window Approach。
- Model Predictive Trajectory Generator。
- Cubic Spline。
- State Lattice Planner。
- Frenet Optimal Trajectory。

### 路径跟踪

- LQR 转向控制。
- LQR 速度与转向控制。
- MPC 速度与转向控制源码。

README 目录还列出 Histogram Filter、Gaussian Grid Map、FastSLAM、无人机轨迹跟踪和火箭着陆，但当前仓库没有相应源码。

## 构建结构

根 `CMakeLists.txt` 为每个算法创建一个独立 `add_executable()`：

```text
src/extended_kalman_filter.cpp → ekf
src/particle_filter.cpp        → pf
src/dijkstra.cpp               → dijkstra
src/a_star.cpp                 → astar
src/rrt.cpp                    → rrt
src/rrt_star.cpp               → rrtstar
src/dynamic_window_approach.cpp → dwa
src/model_predictive_trajectory_generator.cpp → mptg
src/state_lattice_planner.cpp  → slp
src/cubic_spline_planner.cpp   → csp
src/frenet_optimal_trajectory.cpp → frenet
src/lqr_steer_control.cpp      → lqr
src/lqr_speed_steer_control.cpp → lqr_full
```

`model_predictive_control.cpp` 存在，但 CMake 中的 MPC 目标和 IPOPT 链接被注释，默认构建不会生成 MPC。

项目没有：

- 公共库目标。
- 安装规则和导出 package。
- 命令行参数或配置文件。
- ROS 节点和消息接口。
- 单元测试、集成测试和 CI 工作流。

## 数据与模型

### 搜索规划

A* 和 Dijkstra 在二维栅格上扩展八邻域，障碍物和起终点由 `main()` 硬编码。RRT/RRT* 使用圆形障碍和连续二维采样。

### 局部规划

DWA 在速度与角速度动态窗口中采样轨迹，按目标方向、速度和障碍代价选择控制量。

### 车辆轨迹

- Cubic Spline 生成参考路径、航向和曲率。
- Frenet 使用横向五次多项式和纵向四次多项式采样候选，按 jerk、时间、偏移和目标速度代价筛选，并检查速度、加速度、曲率和圆形障碍碰撞。
- State Lattice 从终端状态采样，读取 `lookuptable.csv` 作为优化初值，再使用自行车模型优化轨迹。
- Model Predictive Trajectory Generator 使用自行车模型迭代优化到目标状态。

### 控制

LQR 示例离散化误差状态，迭代求解离散代数 Riccati 方程，组合曲率前馈与状态反馈。完整 LQR 同时输出加速度和转角。

MPC 示例使用 CppAD/IPOPT 求解有限时域车辆模型，但默认不参与构建。

### 定位

EKF 示例融合运动模型和位置观测；粒子滤波示例使用地标距离观测、重要性权重和重采样。两者均是自包含仿真，不接收真实传感器数据。

## 可视化

所有示例直接依赖 OpenCV 绘图。算法、场景、仿真循环和可视化通常位于同一 `.cpp` 文件，便于阅读，但无法无界面复用。

部分程序将图片写入相对路径：

- `./csp.png`
- `./pngs/<timestamp>.png`

State Lattice 固定从 `../../lookuptable.csv` 读取初值表，运行目录变化会导致文件查找失败。

## 开发环境

仓库提供 VS Code Dev Container：

- Debian 11。
- Eigen3。
- 从源码构建 OpenCV 3.3.0。
- CMake 3.25.2。
- 带浏览器桌面的 GUI 环境。

OpenCV 3.3 已明显老旧，容器从源码编译 OpenCV 会增加构建时间和供应链依赖。项目没有锁定 Eigen、编译器或 IPOPT/CppAD 的完整版本组合。

## 代码质量观察

- 多数算法直接使用宏和硬编码常量。
- A* 与 Dijkstra 有大量重复代码。
- 算法逻辑与 OpenCV 可视化耦合。
- RRT/RRT* 使用裸指针，未形成清晰所有权管理。
- State Lattice 依赖运行目录相对路径。
- LQR Full 默认持续向不存在的 `./pngs/` 写图时可能失败。
- README 有拼写错误，且目录包含未实现条目。
- 粒子滤波源码仍有 TODO。
- 无测试和 CI，无法自动发现数值或兼容性回归。

## 静态分析边界

- 未安装 OpenCV 3.3、Eigen、CppAD 或 IPOPT。
- 未执行 CMake 和编译。
- 未打开图形窗口或验证示例输出。
- 未与 PythonRobotics 当前版本逐行对比。
- 未进行算法正确性、性能、内存和数值稳定性评测。
