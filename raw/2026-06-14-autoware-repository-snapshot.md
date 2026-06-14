# Autoware 仓库快照

## 来源与版本

- 官方仓库: https://github.com/autowarefoundation/autoware.git
- 分析日期: 2026-06-14
- 分析方式: 本地静态分析，未编译、未启动车辆栈

| 仓库 | 版本或提交 | 提交日期 |
|---|---|---|
| `autoware` | `59468eedea0e2f40c5ad7265082dacfc81631392` | 2026-06-12 |
| `autoware_core` | `1.8.0` / `16045061a9c10da468b60e190b8fab02110fa501` | 2026-05-02 |
| `autoware_universe` | `0.51.0` / `d4d260983d357e1b2b34291d91933f9f4b53bf94` | 2026-05-03 |
| `autoware_launch` | `0.51.0` / `3ba12ba6a47abca105e755e6d21cf66a0cdf743f` | 2026-05-02 |

主仓库是元仓库，不包含完整功能源码。`repositories/autoware.repos` 通过 `vcs`/`vcs2l` 固定 Core、Universe、Launch、消息、工具、传感器驱动和外部依赖等 31 个仓库。

## 工程结构

- `ansible/`: 开发环境配置入口；旧 `setup-dev-env.sh` 已标记弃用。
- `docker/`: base、core、universe、CUDA、开发和运行镜像分层。
- `repositories/`: 工作区仓库清单。
- `.github/`: CI、版本清单更新和多平台构建流程。
- `autoware_launch`: Vehicle、System、Map、Sensing、Localization、Perception、Planning、Control、API 和 RViz 的总装入口。
- `autoware_core`: 约 70 个 ROS 包，提供基础能力。
- `autoware_universe`: 约 240 个 ROS 包，承载应用、算法和实验能力。

CI 构建矩阵覆盖 ROS 2 Humble/Jazzy 与 amd64/arm64。系统大量使用 ROS 2 composable node、Topic remap、YAML 参数和 launch XML 组装，也可通过 Agnocast wrapper 使用替代通信路径。

## 规划链

```text
Mission Planning
→ Scenario Planning / Diffusion Planner
→ Planning Validator
→ /planning/trajectory
```

规则规划的 Scenario Selector 在 Lane Driving 与 Parking 之间切换。Lane Driving 由 Behavior Planning 与 Motion Planning 组成：

- Behavior Path Planner 通过插件组合起步、到达、绕障、侧移、换道和双向交通等模块。
- Behavior Velocity Planner 组合路口、交通灯、人行横道、盲区、停止线、限速和减速带等规则模块。
- Motion Planning 可组合 Elastic Band、Path Optimizer 或 Path Sampler，再执行障碍物停车/减速/巡航、越界和道路边界等速度模块。
- 最终经过 Velocity Smoother 与 Planning Validator 发布轨迹。

Parking 使用 Costmap Generator 与 Freespace Planner。Diffusion Planner 是学习型替代链，后接轨迹修改或优化插件，最终仍进入 Planning Validator。

## 控制链

`autoware_trajectory_follower_node` 接收规划轨迹、里程计、转角和加速度，分别运行横向与纵向控制器并同步状态：

- 横向: MPC，可切换 Pure Pursuit。
- 纵向: PID。
- 输出: `autoware_control_msgs/Control`。

```text
/planning/trajectory
→ Trajectory Follower
→ Shift Decider
→ Vehicle Cmd Gate / Control Command Gate
→ /control/command/*
→ Vehicle Interface
```

Vehicle Cmd Gate 在自动、外部和紧急命令之间门控，并接收 MRM 状态、运行模式、心跳和车辆状态。`control_command_gate` 是迁移中的新路径，当前 launch 默认仍关闭。

## 控制检查与安全

控制 launch 默认启用或可配置 Lane Departure Checker、Control Validator、AEB、Collision Detector、Control Evaluator、Operation Mode Transition Manager、Obstacle Collision Checker 和 Predicted Path Checker。

系统层还包含故障诊断、MRM 状态和紧急控制命令。是否形成完整安全链取决于具体 launch 参数、车辆配置、传感器输入和组件启用状态。

## 限制

主仓库采用 Apache-2.0，并明确不保证特定用途适用性或安全性。本快照未执行编译、仿真、回放或实车验证；包数量、默认参数和链路结论来自上述固定提交的静态文件。
