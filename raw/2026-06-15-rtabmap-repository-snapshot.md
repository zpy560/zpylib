# RTAB-Map 官方仓库源码快照

> 本文件记录 2026-06-15 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/introlab/rtabmap
- 项目主页：https://introlab.github.io/rtabmap/
- Wiki：https://github.com/introlab/rtabmap/wiki
- 抓取分支：`master`
- 抓取提交：`9f464db7c9d87867cb0dad98871a1614db0b62cf`
- 提交时间：`2026-06-13T16:20:37-07:00`
- 提交标题：`OpenVINS config file support (#1719)`
- 抓取方式：Git 浅克隆
- 分析方式：静态源码分析，未编译、未运行数据集

## 仓库定位

README 将项目定义为“RTAB-Map library and standalone application”。`package.xml` 将其描述为具有实时约束的 RGB-D SLAM 方法。

当前源码实际覆盖：

- 视觉、RGB-D、双目、激光和视觉惯性输入。
- 内置及外部里程计后端。
- 基于外观的全局回环、时间邻近回环和空间邻近回环。
- 图优化、局部/全局定位和多会话地图。
- 2D 栅格、点云、OctoMap、网格和纹理地图。
- SQLite 数据库、数据库查看与离线重处理。
- Qt 桌面应用、Android、iOS、命令行工具和 C++ 示例。

ROS 节点、消息、launch 和 TF 集成主要位于独立的 `rtabmap_ros` 仓库；本仓库是其底层库和 ROS 可构建的软件包。

## 快照规模

- 浅克隆目录：约 64 MB。
- 文件总数：1409。
- C/C++ 头文件：约 612。
- C/C++ 源文件：约 262。
- 主要目录：`corelib/`、`utilite/`、`guilib/`、`app/`、`tools/`、`examples/`、`data/`。
- 许可证：BSD 3-Clause。

## 目录职责

| 目录 | 职责 |
|---|---|
| `corelib/` | SLAM、里程计、特征、注册、图优化、地图、数据库和传感器抽象 |
| `utilite/` | 线程、事件、日志、计时、文件和通用工具 |
| `guilib/` | Qt 图形界面、地图显示、参数和数据库操作 |
| `app/` | 桌面主应用、Android 和 iOS 客户端 |
| `tools/` | 数据录制、数据库查看、重处理、导出、恢复、评测和数据集工具 |
| `examples/` | BOW、RGB-D、LiDAR、Wi-Fi 和无事件总线示例 |
| `data/` | 默认配置、样例和预设 |
| `cmake_modules/` | 大量可选依赖的发现脚本 |

## 核心处理链

`corelib/src/Rtabmap.cpp` 中 `Rtabmap::process()` 是 SLAM 主循环：

```text
SensorData + odometry + covariance
→ 检查里程计与模式
→ Memory::update() 创建 Signature
→ 邻接约束细化
→ 时间邻近回环
→ 外观似然与贝叶斯后验
→ 从数据库重激活候选节点
→ 空间邻近视觉/扫描回环
→ 全局回环变换估计
→ 添加 Link 约束
→ 图优化
→ 优化误差检查与错误回环撤销/修复
→ 更新 map→odom、统计和数据库
→ 按实时/内存阈值清理工作记忆
```

映射模式要求有效里程计；定位模式可加载既有优化图，通过新观测更新 `map→odom` 修正。

## 记忆模型

`Memory` 管理三层记忆：

- STM：Short-Term Memory，保留最新节点。
- WM：Working Memory，参与当前回环候选和图操作。
- LTM：Long-Term Memory，保存在数据库中，按候选需要重新加载。

节点由 `Signature` 表示，包含传感器数据、位姿、视觉词、局部特征、全局描述子、地图 ID、权重和图约束。

当实时阈值或内存阈值触发时，低权重或较旧节点从 WM 转入 LTM；回环候选需要时再由 SQLite 载入。该机制是 RTAB-Map 名称中“Real-Time Appearance-Based Mapping”的核心。

## 回环检测

### 全局外观回环

1. 从当前图像提取局部特征和视觉词。
2. 用倒排词典计算当前节点与 WM 节点的外观似然。
3. BayesFilter 结合虚拟位置与图邻居传播计算后验。
4. 对最高候选执行阈值、比率、GPS 和可选对极几何检查。
5. 使用视觉、ICP 或级联注册估计六自由度变换。
6. 添加 `kGlobalClosure` 图约束。

### 局部回环

- 时间邻近：检查 STM 中非直接相邻节点。
- 空间邻近：在优化图的局部半径内搜索，使用视觉匹配或扫描匹配。
- 地标：可将标签/标记作为图中的特殊负 ID 节点。

### 错误约束处理

图优化后计算线性和角度误差与约束标准差之比。超过 `RGBD/OptimizeMaxError` 时撤销本轮回环；连续命中相同旧错误约束时，可以在指定半径内移除旧链接并重新优化。

## 可插拔算法

### 里程计

- 内置 Frame-to-Map、Frame-to-Frame 和单目里程计。
- FOVIS、libviso2、DVO、ORB-SLAM2/3、OKVIS。
- LOAM、FLOAM、LIO-SAM。
- MSCKF-VIO、VINS-Fusion、OpenVINS。
- Open3D Odometry、NVIDIA cuVSLAM。

多数外部后端由 CMake 选项控制，未安装依赖时不可用。

### 注册

- 纯视觉注册。
- ICP 注册。
- 视觉后接 ICP 的级联注册。

### 特征

支持 SURF、SIFT、ORB、FAST/BRIEF、FREAK、GFTT、BRISK、KAZE、ORB Octree、SuperPoint 和 Python 自定义检测器。不可用的实现会回退到编译环境支持的特征。

### 图优化

- g2o
- GTSAM
- TORO
- Ceres
- CVSBA，主要用于 Bundle Adjustment

请求的后端不可用时，工厂会按可用性自动回退。

## 地图输出

- `OccupancyGrid`：2D/3D 局部栅格融合。
- `CloudMap`：全局点云。
- `OctoMap`：概率体素地图。
- `GridMap`：可选 Grid Map。
- 深度图点云、表面重建、网格、纹理和优化网格。

地图数据既可实时生成，也可从数据库离线重建和导出。

## 数据库

默认后端是 SQLite。数据库保存：

- 节点、图约束与地图会话。
- RGB/深度图像、激光扫描和标定。
- 局部特征、视觉词和全局描述子。
- 里程计、GPS、IMU/环境传感器和用户数据。
- 统计、参数、优化位姿、2D 地图和优化网格。

`DBDriver` 使用异步垃圾队列写入，但源码注释明确指出 SQLite 连接的跨线程互斥设计仍需要重构。仓库保留多个旧 schema，用于数据库向后兼容。

## 线程与事件模型

独立应用的典型流水线：

```text
SensorCaptureThread
→ SensorEvent
→ OdometryThread
→ OdometryEvent
→ RtabmapThread
→ RtabmapEvent
→ GUI / MapBuilder
```

线程间通过自有 `UEventsManager` 事件总线和带上限的数据缓冲区通信。也提供 `NoEventsExample`，展示不使用事件总线的直接同步调用方式。

## 工具与离线工作流

仓库提供 25 个工具目录，包括：

- Camera、CameraRGBD、LidarViewer、DataRecorder。
- DatabaseViewer、Info、Recovery、Reprocess。
- Export、GlobalBundleAdjustment、ReduceGraph。
- DetectMoreLoopClosures、CleanupLocalGrids。
- KittiDataset、EurocDataset、RgbdDataset、CidSimsDataset。
- Report、StereoEval、VocabularyComparison、Matcher。

数据库是在线运行与离线调试之间的主要交付物，可以重放、补回环、重优化、导出地图和生成报告。

## 构建与平台

- 构建系统：CMake 3.14+。
- 必需核心依赖：OpenCV、PCL、SQLite、zlib 等。
- 大量传感器、优化器、里程计和地图依赖可选。
- 支持 Linux、Windows、macOS、Android 和 iOS。
- GitHub Actions 编译 Linux、Windows、macOS、ROS 和 Docker。
- README 列出 ROS 1 Noetic，以及 ROS 2 Humble、Jazzy、Kilted、Rolling 二进制。

## 版本与测试观察

当前提交存在版本元数据不一致：

- README 徽章：`0.23.1`
- `package.xml`：`0.23.5`
- 根 `CMakeLists.txt`：`0.23.7`

GitHub Actions 主要验证配置和编译。工作流中的 `ctest` 步骤被注释，源码中未发现 `enable_testing()`、`add_test()` 或主流单元测试框架注册。

## 静态分析边界

- 未安装仓库的大量系统依赖。
- 未执行 CMake、编译或 CI。
- 未运行 TUM RGB-D、KITTI、EuRoC 等数据集。
- 未验证各传感器驱动、移动端和 ROS 包。
- 性能、精度、内存、实时性和参数有效性需要目标硬件与数据集实验。
