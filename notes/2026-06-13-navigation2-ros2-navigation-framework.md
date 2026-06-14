---
id: "20260613-navigation2-ros2-navigation-framework"
title: "Navigation2：ROS 2 移动机器人导航框架"
type: "note"
source: "https://github.com/ros-navigation/navigation2"
created_at: "2026-06-13"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-13-navigation2.md
  - notes/2026-06-14-apollo-autonomous-driving-platform.md
---

# Navigation2：ROS 2 移动机器人导航框架

## 一句话结论

Nav2 不是一个单独的路径规划库，而是一套面向移动机器人的完整导航操作系统：行为树负责策略编排，ROS 2 Action 和生命周期节点负责系统协作，Planner/Controller 等服务器负责能力承载，pluginlib 负责算法替换，代价地图和末端安全链负责环境约束与执行兜底。

## 原文要点

### 系统主链

```text
导航目标
→ BT Navigator
→ Planner Server 生成全局路径
→ 可选 Smoother Server 平滑路径
→ Controller Server 生成速度指令
→ Velocity Smoother 限制速度和加速度变化
→ Collision Monitor 做末端碰撞约束
→ 底盘 cmd_vel
```

定位与环境表达在主链旁提供状态和约束：

```text
AMCL / SLAM / 里程计 / TF
→ 机器人状态

静态地图 / 传感器
→ 全局与局部 Costmap
→ Planner / Controller / Behavior
```

### 三层架构

1. **任务策略层**：BT Navigator 把规划、控制、条件检查、恢复和重规划组成可替换行为树。
2. **能力服务器层**：Planner、Controller、Smoother、Behavior、Route、Waypoint、Docking、Following 等服务器通过 ROS 2 Action/Service 提供能力。
3. **算法插件层**：规划器、控制器、平滑器、恢复行为、goal/progress checker 等通过稳定接口动态加载。

### 默认恢复策略

默认 NavigateToPose 行为树不是“规划一次然后跟踪到底”，而是持续检查路径并周期性重规划。失败时按作用域恢复：

- 规划失败：清理全局代价地图。
- 控制失败：清理局部代价地图。
- 系统恢复：清图、旋转、等待、后退轮询。
- 新目标到达：打断当前恢复，优先响应新任务。

### 工程化设计

- 核心节点使用 ROS 2 Lifecycle，启动、暂停、恢复和关闭由 Lifecycle Manager 统一管理。
- 服务器与算法分离，同一服务器可通过配置切换不同插件。
- 支持独立进程或组件化部署，组件模式可配合进程内通信降低开销。
- 全局和局部 Costmap 均支持图层插件，环境表达可以按传感器和业务约束扩展。
- Route Server 引入拓扑路线图，与自由空间全局规划形成两种不同抽象。
- 命令输出后仍有 Velocity Smoother 和 Collision Monitor，安全约束不完全依赖控制器内部实现。

## 我的判断

### 最值得借鉴的不是算法，而是边界设计

Nav2 最强的地方不是拥有某个最优规划器，而是把“任务决策、规划、控制、地图、安全和生命周期”拆成稳定边界。算法可以替换，系统主流程不需要跟着重写。

对于自动驾驶规划控制架构，以下模式有直接参考价值：

1. **策略与算法分离**：行为树决定何时规划、何时恢复，Planner/Controller 只解决本职计算。
2. **Server + Plugin**：稳定服务接口承载变化频繁的算法插件，适合多车型、多场景算法切换。
3. **分级恢复**：局部错误先局部恢复，系统错误再升级恢复，避免所有失败都重启全系统。
4. **末端安全链**：控制器输出不是最终执行命令，后置速度约束和碰撞监控保留独立否决权。
5. **生命周期显式化**：配置、激活、暂停和清理成为协议，而不是散落在节点内部的隐式状态。
6. **拓扑与几何双层规划**：Route Graph 管长程任务约束，自由空间 Planner 解决局部几何可达性。

### 不应直接照搬到乘用车自动驾驶

Nav2 的主要目标是室内外移动机器人和工业车辆导航，不是开放道路高速自动驾驶。它的默认假设包括二维代价地图、相对低速、目标点导航和 ROS 分布式节点协作。

它没有直接覆盖乘用车自动驾驶中的：

- 车道级语义和交通规则决策
- 多主体轨迹预测与交互博弈
- 复杂场景行为规划
- 高速车辆动力学和轨迹时空约束
- 面向量产的功能安全、冗余和确定性时延证明

因此正确用法是借鉴系统组织方式，不能把 Nav2 当作 Apollo、Autoware 或量产规划控制栈的等价替代。

### 主要工程代价

- 插件、参数、Action、Topic、TF、Lifecycle 和 Behavior Tree 同时存在，配置面很大。
- 分布式 ROS 系统的问题定位通常跨节点、跨通信和跨坐标系。
- 行为树适合显式任务与恢复编排，但树过大后同样会形成隐式耦合。
- 默认示例参数只能作为起点，机器人模型、传感器和场景变化后必须系统调参。

## 可复用内容

### 可复用的导航系统骨架

```text
任务入口
→ 策略编排器
→ 标准化能力服务器
→ 可替换算法插件
→ 输出整形
→ 独立安全监控
→ 执行器
```

### 评审规划控制架构的六个问题

1. 任务策略是否与规划控制算法解耦？
2. 算法能否在不修改主流程的情况下替换？
3. 失败是否按局部、模块、系统分级恢复？
4. 控制输出之后是否还有独立安全约束？
5. 模块生命周期和健康状态是否显式可管理？
6. 拓扑任务规划和几何运动规划是否使用了合适的不同表达？

## 疑问与冲突

- Nav2 的 Behavior Tree 在大规模工业项目中如何控制复杂度，需要继续研究其树拆分、可观测性和测试方法。
- Route Server、Following Server 和新 MPPI 能力正在快速演进，后续应按具体 ROS 发行版而不是直接按 `main` 使用。
- 值得单独对比 Nav2、Autoware Universe 与 Apollo 在“任务编排—规划—控制—安全后处理”上的边界差异。

Apollo 的本地源码对比已补充至 `notes/2026-06-14-apollo-autonomous-driving-platform.md`。

## 原料

- `raw/2026-06-13-navigation2-repository-snapshot.md`
