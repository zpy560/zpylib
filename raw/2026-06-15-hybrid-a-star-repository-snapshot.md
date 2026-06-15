# Hybrid A Star 仓库快照

## 来源

- 仓库：https://github.com/zm0612/Hybrid_A_Star
- 抓取日期：2026-06-15
- 默认分支：`main`
- 快照提交：`cf0cc997f285e05a1ff51f36b224d3040fc7708c`
- 提交时间：2024-06-16T23:33:20+08:00
- 提交标题：`Support custom maps`
- 许可证：BSD 3-Clause
- 分析方式：克隆默认分支后静态分析源码、ROS 接口和构建配置；未在 ROS Melodic 环境编译运行

## 项目定位

该仓库复现论文《Practical Search Techniques in Path Planning for Autonomous Driving》中的 Hybrid A* 思路，面向泊车和无道路规则约束的车辆路径搜索。项目运行于 ROS1 Melodic，通过 RViz 交互选择起点和终点，并在 OccupancyGrid 地图上显示搜索树、路径和车辆包络。

依赖：

- C++11
- ROS1 Melodic
- `nav_msgs`、`roscpp`、`tf`
- Eigen3
- glog
- map_server、RViz

## 目录结构

```text
include/hybrid_a_star/
  hybrid_a_star.h         搜索器接口
  state_node.h            三维状态节点
  rs_path.h               Reeds-Shepp 路径
  trajectory_optimizer.h  未接入主流程的轨迹优化器
  *_subscriber.h          ROS 输入
src/
  hybrid_a_star.cpp       核心搜索
  rs_path.cpp             Reeds-Shepp 公式实现
  hybrid_a_star_flow.cpp  ROS 数据与可视化流程
app/
  run_hybrid_astar.cpp
maps/                     多种演示地图
launch/                   ROS launch
rviz/                     显示配置
model/                    车辆 URDF/DAE
```

核心实现为 7 个 `.cpp` 和 11 个头文件，没有测试目录、CI 或 benchmark。

## 搜索状态与运动原语

状态空间为：

```text
x, y, yaw
```

搜索索引将连续状态离散为 x、y 和航向角三个维度，默认航向离散数为 72。

每个展开节点遍历离散转向角，并分别生成前进和倒车运动原语。简化车辆模型以后轴中心为参考：

```text
x += ds * cos(yaw)
y += ds * sin(yaw)
yaw += ds / wheel_base * tan(steer)
```

一个原语由多个小步组成，每个小步执行碰撞检查。参数包括最大转角、转角离散数、原语长度、内部步数、轴距、三类行为惩罚和 Reeds-Shepp shot 距离。

## 代价与启发式

边代价基于固定原语长度，叠加：

- 转向惩罚
- 倒车惩罚
- 转角变化惩罚

启发式默认使用当前位置到终点的 L1 距离；距离小于三倍 shot distance 时，切换为忽略障碍物的 Reeds-Shepp 距离。

当节点进入 shot distance 后，算法尝试直接生成 Reeds-Shepp 路径到目标，并逐点碰撞检测。成功则结束搜索。

## Reeds-Shepp 实现

`RSPath` 实现 18 类路径段组合，覆盖 CSC、CCC、CCCC、CCSC 和 CCSCC，并支持前进、倒车和方向切换。实现注释指出原论文第 8 节存在符号与推导错误，代码按几何关系进行了修正。

Reeds-Shepp 在项目中承担：

1. 近终点解析扩展。
2. 近终点启发式距离。

## 碰撞检测

车辆表示为矩形，默认在 `Init()` 中设置为长 4.7 m、宽 2.0 m、后轴至车尾 1.3 m。

矩形四个角经过姿态变换后映射到地图栅格，四条边使用类似 Bresenham 的线检查检测障碍。

当前实现只检查矩形轮廓边，不扫描车体内部，因此完全位于矩形内部、未触及边界的障碍栅格可能被漏检。

## ROS 运行链

```text
map_server 发布 /map
→ CostMapSubscriber 读取 OccupancyGrid
→ RViz 2D Pose Estimate 提供起点
→ RViz 2D Nav Goal 提供终点
→ HybridAStar::Search
→ 发布 searched_path、searched_tree、vehicle_path
→ TF 动画播放 ground_link
```

地图只在首次收到时初始化，后续地图消息被清空，不支持运行时动态地图更新。

## 源码中确认的问题

### 地图数组未初始化

`Init()` 使用动态数组分配障碍地图，但没有清零。随后只把障碍格设置为 `1`，自由格可能保留未定义值；碰撞结果因此可能依赖内存内容。

### 邻居启发式使用了当前节点

展开邻居时调用：

```cpp
ComputeH(current_node_ptr, goal_node_ptr)
```

随后所有邻居共用该值。标准做法应对每个 `neighbor_node_ptr` 计算启发式。

### open set 改进路径没有重新入队

当已在 open set 的状态发现更小 `g` 时，代码替换状态表指针，但没有把新节点插回 `openset_`，也没有删除旧 multimap 条目。源码自己标注该分支会内存泄漏。这会造成优先队列与状态表不一致。

### 自定义地图边界计算有误

ROS flow 传入的上界是 `width * resolution` 和 `height * resolution`，没有加地图 origin。对于负原点或非零原点地图，状态边界与 OccupancyGrid 会错位。仓库附带地图包含负原点，因此该问题与最后一次“支持自定义地图”提交直接相关。

### 其他明确问题

- `SetObstacle()` 使用 `>` 而非 `>=` 检查尺寸，边界索引可能越界。
- 矩形碰撞只检查四边，可能漏掉内部障碍。
- 起点和终点没有显式执行完整车体碰撞检查。
- 计算 G 代价后累计的是错误计时器，性能输出不可信。
- OccupancyGrid 任意非零值都被当作障碍，包括未知栅格。
- 搜索硬限制为 50000 次迭代。
- 轨迹优化器只在头文件中提供，主搜索流程没有调用。
- 搜索车辆尺寸与 RViz 显示尺寸不一致。

## 构建与验证边界

仓库要求 ROS Melodic 和 catkin。本机环境以 ROS Humble 为主，本次没有安装或切换 ROS1 依赖，因此未执行 `catkin_make`、launch 和地图案例。

仓库没有单元测试、Reeds-Shepp 数值测试、碰撞回归、标准场景成功率、路径最优性对照、基准数据文件或 CI。README 声称结果接近论文速度和效果，但仓库没有可重复 benchmark，无法独立验证。
