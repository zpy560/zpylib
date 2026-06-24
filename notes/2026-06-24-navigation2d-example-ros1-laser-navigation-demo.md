---
id: "20260624-navigation2d-example-ros1-laser-navigation-demo"
title: "navigation2d_example：ROS1 UTM-30LX 与 move_base 示例"
type: "note"
source: "raw/2026-06-24-navigation2d-example-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2d-example.md
  - wiki/2026-06-13-navigation2.md
---

# navigation2d_example：ROS1 UTM-30LX 与 move_base 示例

## 一句话结论

DaikiMaekawa/navigation2d_example 是一个 ROS1 时代的 UTM-30LX + move_base 示例，和 ROS 2 Navigation2 没有直接关系；价值在历史参考和激光雷达二维导航配置，不应混入 Nav2 现代架构判断。

## 原文要点

- 示例使用 UTM-30LX 和 `navigation2d` ROS node。
- 依赖安装示例为 `ros-<distro>-move-base`。
- 启动命令为 `roslaunch navigation2d_example move_base.launch`。
- README 链接了作者文章和 RViz 视频。
- 许可证为 MIT。

## 我的判断

### 名称容易误导

`navigation2d` 不是 ROS 2 `Navigation2`。这个仓库应归类为 ROS1/move_base 历史示例，而不是 Nav2 插件或 ROS 2 教程。

### 可作为迁移前对照

如果要比较 ROS1 move_base 与 ROS2 Nav2，可用它观察老式 launch、传感器和二维导航配置，再对照 Nav2 的 lifecycle、BT、server/plugin 设计。

## 可复用内容

- UTM-30LX 激光雷达二维导航历史示例。
- ROS1 `move_base` 最小启动参考。
- 与 Nav2 迁移对比材料。

## 疑问与冲突

- 本次未浅克隆或运行。
- README 内容较少，具体配置还需要读 launch 和参数文件。

## 原料

- `raw/2026-06-24-navigation2d-example-repository-snapshot.md`
