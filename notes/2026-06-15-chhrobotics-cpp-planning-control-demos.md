---
id: "20260615-chhrobotics-cpp-planning-control-demos"
title: "chhRobotics_CPP：自动驾驶规划与跟踪控制 C++ 演示集"
type: "note"
source: "raw/2026-06-15-chhrobotics-cpp-repository-snapshot.md"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-15-chhrobotics-cpp.md
  - notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md
  - notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md
---

# chhRobotics_CPP：自动驾驶规划与跟踪控制 C++ 演示集

## 一句话结论

chhRobotics_CPP 用 C++14、Eigen 和 matplotlib-cpp 提供 12 个路径规划与 7 个轨迹跟踪演示，覆盖 A*、DWA、RRT 系列、Dubins/Reeds-Shepp、PID、Pure Pursuit、Stanley、LQR 和 MPC，适合结合中文博客理解算法流程；但构建依赖声明不完整、OSQP MPC 未完成、源码存在明确曲率计算错误、没有测试与许可证，不能直接作为自动驾驶工程算法库。

## 原文要点

### 内容主线

项目将自动驾驶运动算法分成两组：

```text
路径规划：搜索、采样、曲线和局部速度空间
轨迹跟踪：几何、反馈、最优控制和预测控制
```

规划侧实际包含 Dijkstra、A*、APF、DWA、RRT/RRT-Connect/RRT*、Bezier、B-spline、曲线插值、Dubins 和 Reeds-Shepp。

跟踪侧包含 PID、Pure Pursuit、Stanley、Rear Wheel Feedback、LQR，以及两套 MPC 尝试。

### 教学组织方式

每个算法通常具有独立目录、类实现和 `main.cpp`。场景、障碍物、起终点和参数写在演示入口中，运行过程通过 matplotlib-cpp 可视化。README 再链接作者博客解释理论。

这种组织比单文件代码更容易定位算法边界，但算法类仍直接依赖具体容器、绘图和简化场景，没有形成统一规划器或控制器接口。

### 运动模型

跟踪算法共用运动学自行车模型：

```text
x += v cos(yaw) dt
y += v sin(yaw) dt
yaw += v / L tan(delta) dt
v += acceleration dt
```

该模型适合低速几何跟踪演示，不包含轮胎侧偏、横摆动力学、执行器动态、延迟和道路坡度。

## 我的判断

### 最适合建立规划控制算法地图

仓库把常见规划和控制算法放在相似的 C++/Eigen/绘图环境中，适合回答：

- A* 与 Dijkstra 的代码差别在哪里？
- DWA 如何形成速度窗口并评价预测轨迹？
- RRT* 如何选父节点和重布线？
- Dubins 与 Reeds-Shepp 如何表达车辆曲率约束？
- Pure Pursuit、Stanley 和 LQR 分别依赖什么误差？
- MPC 比反馈控制器多了哪些模型和优化结构？

对初学者而言，博客加动画演示的组合比直接进入 ROS 或大型自动驾驶平台更容易阅读。

### 文档能力范围大于实际仓库

README 列出蚁群、动态规划、PRM、速度规划和三类 Kalman Filter，但这些只有博客链接，没有对应 C++ 源码。评估项目能力应以 CMake 目标和源码目录为准。

### MPC 不能视为可用实现

OsqpEigen 版本的 README 和 CMake 都明确标记有 bug 或待实现，源码也没有完整构造动力学等式约束。CppAD/IPOPT 版本依赖额外外部库，但构建系统没有完整发现和版本约束。

如果目标是学习 MPC，可先读状态与代价构造；如果目标是复现实验或上车，应改用经过测试的实现并建立闭环指标。

### 存在会影响控制结果的明确错误

参考路径曲率公式使用 `3 / 2` 作为 `pow` 指数，在 C++ 中结果为整数 `1`。这不是代码风格问题，而会直接改变曲率、参考转角和相关控制器输出。由此可见，仓库内容必须经过公式对照和数值测试，不能仅以“可编译”判断正确。

### 工程成熟度较低

- 无许可证，复制与再分发权利不明确。
- 无测试、CI 和标准场景回归。
- OsqpEigen 未写入 README 依赖列表。
- CMake 无条件加载未完成的 MPC。
- Python 3.10 和 NumPy 路径被硬编码。
- 算法与 matplotlib-cpp 强耦合。
- 搜索失败、空结果和资源释放处理不足。
- 随机规划没有固定种子和统计评测。

## 可复用内容

### 推荐阅读顺序

1. `KinematicModel`：理解所有跟踪演示的模型假设。
2. Pure Pursuit 与 Stanley：比较几何误差和横向误差反馈。
3. Rear Wheel Feedback 与 LQR：进入状态误差模型。
4. Dijkstra 与 A*：比较代价搜索和启发式搜索。
5. DWA：理解速度空间局部规划。
6. RRT、RRT-Connect、RRT*：比较采样树扩展策略。
7. Dubins 与 Reeds-Shepp：理解非完整车辆曲线。
8. MPC：只作为未完成优化代码审读，不作为结果基准。

### 工程化改造顺序

1. 先修复曲率指数并添加解析曲线数值测试。
2. 将 matplotlib-cpp 从算法目标中移出。
3. 定义统一的 `PlanResult` 和 `ControlCommand` 失败语义。
4. 用值语义或智能指针管理搜索节点。
5. 给随机算法注入随机数生成器和种子。
6. 将参考线、障碍物和车辆参数改成显式输入。
7. 拆分可选 MPC 构建，并完整声明 OsqpEigen/CppAD/IPOPT。
8. 建立路径长度、碰撞、跟踪误差、控制平滑性和运行时间回归。

### 与 CppRobotics 的关系

两者都是受 PythonRobotics 生态影响的 C++ 可视化算法项目。CppRobotics 还覆盖定位算法和 Frenet/State Lattice；chhRobotics_CPP 更集中于规划曲线、采样规划和多种基础跟踪控制，并配有中文博客。后者的 CppAD/IPOPT MPC README 也明确引用 CppRobotics。

### 与 planning_algorithm 的关系

planning_algorithm 只有最小 A* 和 RRT 动画；chhRobotics_CPP 覆盖更完整的搜索、采样、曲线规划和路径跟踪算法。前者适合快速观察流程，后者适合继续比较算法族，但二者均缺少系统测试。

## 疑问与冲突

- 仓库未提供许可证，代码可否复用需要作者补充授权。
- README 所列 Ubuntu 20.04 环境与 CMake 3.21、Python 3.10 硬编码存在版本冲突。
- OSQP MPC 的预期变量布局与约束形式尚未完成。
- 2024 年最后提交是否修复运行行为，本次因缺失 OsqpEigen 未能执行验证。

## 原料

- `raw/2026-06-15-chhrobotics-cpp-repository-snapshot.md`
