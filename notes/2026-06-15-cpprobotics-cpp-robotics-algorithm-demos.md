---
id: "20260615-cpprobotics-cpp-robotics-algorithm-demos"
title: "CppRobotics：机器人定位、规划与控制的 C++ 可视化示例集"
type: "note"
source: "raw/2026-06-15-cpprobotics-repository-snapshot.md"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-15-cpprobotics.md
  - notes/2026-06-24-pythonrobotics-robotics-algorithm-textbook.md
  - notes/2026-06-14-ros-motion-planning-algorithm-workbench.md
  - notes/2026-06-15-mpcc-model-predictive-contouring-control.md
  - notes/2026-06-15-dev-xys-algorithms-competitive-programming-templates.md
  - notes/2026-06-15-chhrobotics-cpp-planning-control-demos.md
---

# CppRobotics：机器人定位、规划与控制的 C++ 可视化示例集

## 一句话结论

CppRobotics 是 PythonRobotics 部分经典算法的 C++11 教学移植，适合快速阅读 EKF、粒子滤波、A*、RRT、DWA、Frenet、State Lattice 和 LQR 的最小实现；它不是可复用机器人算法库，缺少统一接口、测试、CI、安装和真实系统集成，不能直接作为自动驾驶或机器人项目的生产模块。

## 原文要点

### 内容范围

当前源码包含 14 个独立演示程序，覆盖：

- 定位：EKF、粒子滤波。
- 搜索：Dijkstra、A*。
- 采样规划：RRT、RRT*。
- 局部规划：DWA。
- 车辆轨迹：Cubic Spline、Frenet、State Lattice、Model Predictive Trajectory Generator。
- 跟踪控制：LQR 转向、LQR 速度与转向、MPC 源码。

README 中 Mapping、SLAM 和 Aerial Navigation 多数条目只是目录占位，当前没有实现。

### 代码组织

```text
main() 内置场景和参数
→ 算法计算
→ OpenCV 绘制轨迹
→ 窗口播放或输出图片
```

少量公共数学结构放在 `include/`，例如样条、多项式、车辆模型和 RRT，但没有形成稳定 API 或库目标。

### 轨迹规划主线

仓库中与自动驾驶关系最直接的链路是：

```text
离散路径点
→ Cubic Spline 参考线
→ Frenet 或 State Lattice 候选轨迹
→ 速度、加速度、曲率和碰撞筛选
→ LQR 或 MPC 跟踪
```

Frenet 示例采用横向五次、纵向四次多项式，并使用 jerk、时间、横向偏移和目标速度误差构造代价。State Lattice 根据终端状态采样和查找表初值，优化自行车模型控制参数。

## 我的判断

### 价值在“短代码展示算法骨架”

CppRobotics 的优势是没有 ROS、插件、参数服务器和复杂框架干扰。读者可以在一个源文件内看到输入、状态、代价、约束、循环和可视化，适合回答：

- A* 如何维护 open/closed 集？
- RRT* 如何选择父节点和重连？
- DWA 如何形成动态窗口并打分？
- Frenet 如何采样横纵向多项式？
- LQR 如何从误差状态计算控制量？

它比大型系统更适合第一次理解算法控制流。

### 不是“库”，复制代码也不是正确复用方式

当前设计把算法与固定场景、全局常量、图像坐标和 GUI 循环混在一起。直接复制到项目会同时带入：

- 特定机器人半径、轴距和采样范围。
- 固定障碍表达和碰撞模型。
- 单线程仿真假设。
- 缺失的输入校验和失败状态。
- OpenCV GUI 与相对文件路径。

正确使用方式是提取数学与流程，重新定义项目自己的数据接口、约束、测试和性能指标，而不是把示例当组件。

### 与 ROS Motion Planning 的区别

| 维度 | CppRobotics | ROS Motion Planning |
|---|---|---|
| 定位 | 纯 C++ 单文件教学示例 | ROS1 仿真平台，不以定位为重点 |
| 规划控制 | 独立算法 demo | 统一 costmap、`move_base` 和 Gazebo |
| 接口 | 无统一运行接口 | `nav_core` 和 ROS Topic/Plugin |
| 场景 | 源码硬编码 | 地图、机器人和配置文件 |
| 评测 | 无 | 有统一实验外壳，但仍缺标准指标 |
| 用途 | 阅读最小算法实现 | 比较算法在 ROS 环境中的行为 |

两者可以形成学习顺序：先用 CppRobotics 理解算法，再用 ROS Motion Planning 检查算法在 costmap、坐标系、插件和仿真系统中的工程行为。

### 主要技术风险

1. 最后一次提交是 2023 年，依赖仍以 OpenCV 3.3 为基准。
2. README 列出的能力超过实际源码。
3. MPC 默认不构建，外部依赖说明不完整。
4. 无自动测试，数值边界和回归不可见。
5. RRT 使用裸指针，资源所有权不清晰。
6. 相对路径和输出目录依赖运行位置。
7. 多个示例可能在无可行轨迹时访问空结果，错误处理不足。
8. 未提供动态障碍预测、时空占用、车辆边界、控制延迟和安全兜底。

### 对自动驾驶的适用边界

适合：

- 规划控制算法入门。
- 将 PythonRobotics 算法映射到 C++。
- 快速验证二维静态场景中的算法结构。
- 为单元测试构造最小参考实现。

不适合：

- 直接接入车辆或机器人。
- 作为实时规划控制框架。
- 评价量产算法性能。
- 处理动态多主体、道路规则和安全约束。

## 可复用内容

### 推荐学习路径

1. Dijkstra 与 A*：理解图搜索、启发式与栅格膨胀。
2. RRT 与 RRT*：理解采样、steer、碰撞与 rewiring。
3. Cubic Spline：建立连续参考线与曲率表达。
4. Frenet：理解横纵向解耦和候选筛选。
5. State Lattice：理解运动原语、终端采样和可行性。
6. DWA：理解局部速度空间搜索。
7. LQR：理解线性误差模型、前馈与反馈。
8. MPC：最后补充外部求解器和约束优化。

### 将教学代码工程化的改造顺序

1. 把算法输入、输出和失败状态从 `main()` 分离。
2. 移除 OpenCV 可视化依赖，改为可选观察器。
3. 将参数放入明确配置结构并注明单位。
4. 使用值语义或智能指针替代裸指针。
5. 为标准场景添加确定性单元测试。
6. 添加边界条件、无解和数值异常测试。
7. 再接入 ROS、地图和车辆模型。

### 与 MPCC 的进阶关系

CppRobotics 的 MPC 源码用于展示基础预测跟踪；MPCC 进一步把路径进度作为决策变量，并加入动态轮胎模型、赛道约束、SQP 和 HPIPM。前者适合建立直觉，后者适合研究自主赛车高动态约束控制。

### 与 Dev-XYS Algorithms 的区别

两者都采用独立 C++ 示例，但 CppRobotics 面向机器人算法并提供可视化，Dev-XYS Algorithms 面向信息学竞赛和通用数据结构，以标准输入输出程序为主。它们都适合阅读算法骨架，不适合作为生产库。

### 与 chhRobotics_CPP 的关系

两者都受 PythonRobotics 影响并使用 C++ 可视化演示。CppRobotics 覆盖定位、规划与控制；chhRobotics_CPP 更集中于路径规划曲线、RRT 系列和基础跟踪控制，并提供中文博客入口。chhRobotics_CPP 的 CppAD/IPOPT MPC 也直接参考了 CppRobotics。

## 疑问与冲突

- README 中 Mapping、SLAM 和 Aerial Navigation 条目没有对应实现。
- MPC 源码是否能在现代 CppAD/IPOPT 环境编译，需要单独验证。
- 当前实现与 PythonRobotics 最新版本的算法差异和 bug 修复未核对。
- 本次未编译运行，OpenCV 4、现代 GCC 和 Eigen 版本兼容性未知。

## 原料

- `raw/2026-06-15-cpprobotics-repository-snapshot.md`
