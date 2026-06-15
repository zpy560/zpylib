# MPCC 仓库快照

## 来源

- 仓库：https://github.com/alexliniger/MPCC
- 抓取日期：2026-06-15
- 默认分支：`master`
- 快照提交：`bd331621ba47ae3326711922a863bdb1cdf2d2ea`
- 提交时间：2021-11-11T15:10:14+01:00
- 提交标题：`fix optimizer name issue in matlab`
- 许可证：Apache License 2.0
- 分析方式：克隆默认分支后进行静态源码分析；未安装依赖、未编译、未运行仿真

## 仓库定位

MPCC 是 Alexander Liniger 发布的 Model Predictive Contouring Control 自主赛车仿真实现，包含 C++ 和 MATLAB 两套代码。它源自 ETH Zurich Automatic Control Laboratory 的 1:43 比例赛车研究，目标不是按照固定时间参数追踪参考轨迹，而是在赛道边界内同时优化横向误差、纵向进度和车辆控制。

仓库根目录 README 说明的基本问题为：

1. 使用路径进度状态近似车辆在参考线上的位置。
2. 惩罚 contouring error 与 lag error。
3. 奖励沿参考路径前进。
4. 惩罚输入变化。
5. 加入赛道、状态、输入和输入变化率约束。
6. 使用非线性动态自行车模型、Magic Formula 轮胎和动力系统模型。

非线性问题通过逐次线性化近似为时变二次规划：线性化并离散化动力学，一阶近似 contouring/lag error，并以沿赛道边界的线性半空间近似赛道约束。QP 主要由 HPIPM 求解。

## 目录与规模

```text
C++/
  Constraints/   边界、赛道、轮胎和软约束
  Cost/          contouring、lag、进度和正则代价
  Interfaces/    HPIPM 与求解器接口
  MPC/           SQP 循环、初值更新与求解恢复
  Model/         车辆模型与数值积分
  Params/        JSON 参数和赛道
  Plotting/      仿真绘图
  Spline/        三次样条与弧长参数化
  Tests/         样条、模型、代价和约束检查函数
Matlab/
  MPCC 仿真、多个求解器接口和避障走廊生成
Images/
```

克隆快照包含 121 个文件；核心代码约为 20 个 C++、20 个头文件和 28 个 MATLAB 文件。仓库没有 GitHub Actions 或其他 CI 配置。

## C++ 实现

### 状态、输入与时域

`C++/config.h` 固定：

- 状态维数 `NX = 10`
- 输入维数 `NU = 3`
- 预测步数 `N = 60`
- 多面体约束数 `NPC = 3`
- 软约束数 `NS = 3`

状态为：

```text
X, Y, phi, vx, vy, r, s, D, delta, vs
```

其中 `s` 是路径进度，`D` 是驱动命令状态，`delta` 是转角状态，`vs` 是虚拟进度速度。优化输入为三者的变化率：

```text
dD, dDelta, dVs
```

默认配置使用 `Ts = 0.02 s`、60 步预测时域、每周期两次 SQP 迭代和 0.8 的解混合系数。

### 求解流程

`MPC::runMPC()` 的主要流程：

```text
当前车辆状态
→ 投影到弧长样条并处理闭环坐标
→ 移位或重新生成初始轨迹
→ 每次 SQP 迭代构造各阶段 QP
→ HPIPM 求解
→ 反归一化并与旧解混合
→ 多次失败后重置初值
→ 返回第一拍输入和预测轨迹
```

阶段构造包含归一化后的代价、线性化动力学、约束、状态/输入/松弛变量边界和路径进度 trust region。源码中明确留有“使用 line search 和 merit function”的 TODO，当前采用固定混合更新。

### C++ 特有能力

C++ 版本不是论文原始实现的逐行复刻，而是吸收 AMZ Driverless 工作后的新版本：

- 将输入变化率直接作为连续时间模型输入。
- 增加前轮侧偏角约束。
- 增加后轮轮胎摩擦椭圆约束。
- 增加车辆质心侧偏角代价。
- 仅支持 HPIPM。
- 不支持避障。

README 明确说明 `master` 参数不适合全尺寸车辆；另有 `full-size` 分支采用不同 SQP 形式。远端同时存在独立 `main` 分支，因此引用代码时必须记录具体分支与提交。

## MATLAB 实现

MATLAB 版本更接近 1:43 赛车论文中的 MPCC，支持：

- ORCA 与 FullSize 车辆模型。
- ORCA 与 RCP 赛道。
- HPIPM、YALMIP、CVX 和 `quadprog` 接口。
- 基于一维动态规划网格搜索的避障路径选择。
- 将避障结果转换为走廊并修改赛道约束。

避障只存在于 MATLAB 版本，且部分障碍位置需要手工修改，不是通用动态场景接口。

## 构建与依赖

C++ 使用 CMake 3.7、C++14，并由 `install.sh` 直接克隆：

- BLASFEO
- HPIPM
- matplotlib-cpp
- Eigen
- nlohmann/json

安装脚本不固定依赖版本。README 仍声称 matplotlib-cpp 需要 Python 2.7，而 CMake 通过 `find_package(Python COMPONENTS Development)` 查找 Python 开发环境。该组合在现代系统上的兼容性需要重新验证。

CMake 只生成一个 `MPCC` 可执行文件。测试源文件被编入该可执行文件，但 `main.cpp` 中的测试调用全部注释，没有独立测试目标、CTest 或 CI。

## 论文与研究关系

README 链接的研究脉络包括：

- Optimization-based autonomous racing of 1:43 scale RC cars
- Model predictive contouring control for time-optimal path tracking
- Randomized MPC for autonomous racing
- Stochastic MPC for autonomous racing
- Cautious NMPC with Gaussian Process dynamics
- Learning-based MPC for autonomous racing
- AMZ Driverless: The Full Autonomous Racing System

仓库适合作为这些论文中“路径进度变量、contouring/lag error、赛道约束与逐次 QP”概念的可执行参考，但不同语言、分支和论文版本并不完全等价。

## 静态分析限制

- 未安装外部依赖。
- 未验证现代 GCC、CMake、Python、BLASFEO 和 HPIPM 的兼容性。
- 未测量求解时间、闭环误差、最大横向加速度或失败率。
- 未检查 `full-size` 分支。
- 未将当前实现与论文公式逐项数值复现。
