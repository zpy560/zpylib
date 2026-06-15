# chhRobotics_CPP 仓库快照

## 来源

- 仓库：https://github.com/CHH3213/chhRobotics_CPP
- 抓取日期：2026-06-15
- 默认分支：`master`
- 快照提交：`c8bc45c5b3c5b8bbe5cee823681ab343c3a3f39f`
- 提交时间：2024-05-25T13:18:21+08:00
- 提交标题：`Merge pull request #12 from xuc5/users/xuc5/test`
- 许可证：仓库未提供许可证文件
- 分析方式：克隆默认分支、静态源码分析和 CMake 配置检查；未安装缺失依赖，未运行演示

## 项目定位

chhRobotics_CPP 是作者 chhRobotics Python 项目的 C++ 版本，围绕自动驾驶和移动机器人路径规划、轨迹跟踪提供可视化演示。README 建议结合作者博客阅读。

实际源码分成：

```text
PathPlanning/
PathTracking/
matplotlibcpp.h
CMakeLists.txt
```

项目使用 C++14、Eigen 和 matplotlib-cpp；MPC 还涉及 OsqpEigen、CppAD 与 IPOPT。

## 实际算法

### 路径规划

CMake 定义 12 个规划演示：

- Dijkstra
- A*
- Artificial Potential Field
- Dynamic Window Approach
- RRT
- RRT-Connect
- RRT*
- Bezier
- B-spline
- Curve Interpolation
- Dubins
- Reeds-Shepp

算法通常由一个头文件、实现文件和硬编码场景的 `main.cpp` 组成，通过 matplotlib-cpp 动态显示搜索或运动过程。

README 还链接蚁群、动态规划、PRM 和速度规划文章，但仓库中没有对应 C++ 目标。

### 路径跟踪

CMake 定义 7 个控制演示：

- PID
- Pure Pursuit
- Stanley
- Rear Wheel Feedback
- LQR
- 基于 OsqpEigen 的 MPC
- 基于 CppAD/IPOPT 的速度与转向 MPC

公共工具提供运动学自行车模型、横向误差模型、参考路径生成和角度归一化。

README 的“预测”部分链接 Kalman Filter 系列文章，但仓库没有滤波或预测源码。

## 代码结构

典型运行链：

```text
main.cpp 硬编码地图、障碍物、参考线和参数
→ 算法类计算路径或控制量
→ 简化运动学模型推进状态
→ matplotlib-cpp 调用 Python 绘图
```

相比纯单文件示例，算法类与演示入口已有初步分离，但没有形成安装后的稳定库 API。根 CMake 创建的 `chhRobotics_CPP` 是仅承载 Python 链接依赖的 `INTERFACE` target，算法源码仍直接编入各演示程序。

## 关键实现观察

### 搜索与采样规划

- Dijkstra 与 A* 使用栅格地图、八邻域运动模型和 `std::map` 保存 open/closed set。
- 障碍膨胀通过遍历每个栅格与所有障碍点计算距离，规模增大时开销高。
- 搜索循环没有明确的 open set 为空失败分支。
- 节点大量使用裸 `new`，未见统一释放。
- RRT 系列使用 `rand()`，没有可配置随机种子和确定性测试。
- RRT* 实现父节点重选、rewire 与叶节点代价传播。
- DWA 在速度窗口中采样轨迹，以朝向、障碍距离和速度打分。

### 轨迹跟踪

- 公共车辆模型是离散运动学自行车模型，状态为 `x, y, yaw, v`，控制为加速度与前轮转角。
- Pure Pursuit、Stanley、后轮反馈和 LQR 都在线性或低速运动学假设下工作。
- 参考线由固定三角函数生成，不是外部地图或规划器接口。
- 最近点搜索多为每周期全路径线性扫描。

### MPC 状态

`PathTracking/MPC/README.md` 明确说明 OsqpEigen MPC “目前还有一些 bug 待解决”，CMake 注释也标记为“待实现”。源码尚未完整构造动力学等式约束，QP 变量、边界和矩阵维度的组织不能视为完成实现。

另一套 MPC 参考 PythonRobotics 与 CppRobotics，使用 CppAD/IPOPT 联合控制速度和转角。

### 明确的数值问题

`MyReferencePath.cpp` 中曲率分母写为：

```cpp
pow(dx * dx + dy * dy, 3 / 2)
```

C++ 整数除法使 `3 / 2` 等于 `1`，而不是曲率公式要求的 `1.5`。这会系统性改变参考曲率，并影响 LQR/MPC 的前馈转角与参考轨迹。

## 构建检查

执行：

```bash
cmake -S . -B /tmp/chhRobotics_CPP-build
```

结果：

- GNU C/C++ 11.4、Python 3.10 和 NumPy 被找到。
- 配置因找不到 `OsqpEigenConfig.cmake` 失败。

工程问题：

- README 依赖列表没有列出 OsqpEigen。
- CMake 无条件要求 OsqpEigen，因此即使只想构建规划算法也会失败。
- CMake 在 `PathTracking` 中硬编码 Python 3.10 头文件和 NumPy 路径。
- IPOPT 只写入链接目标，没有 `find_package` 或 CppAD 检查。
- 没有测试、CTest 或 CI。
- 最低 CMake 版本要求 3.21，与 README 声称的 Ubuntu 20.04 默认环境可能不匹配。

## 许可证

仓库根目录及子目录未发现 `LICENSE` 或其他许可证文件。公开可读不等于允许复制、修改和再分发；在许可证补充前，代码复用存在法律不确定性。

## 静态分析限制

- 未安装 OsqpEigen、CppAD 或 IPOPT。
- 未完成全量构建和运行。
- 未验证绘图窗口、算法收敛和数值结果。
- 未逐个与对应 Python 实现和博客公式对照。
- 未分析仓库外部博客正文。
