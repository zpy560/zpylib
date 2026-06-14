# Build Your Own X 官方仓库快照

> 本文件记录 2026-06-14 抓取和检查到的仓库事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/codecrafters-io/build-your-own-x
- 抓取分支：`master`
- 抓取提交：`294aef8fde538d169089b1c7dc70b0ddc3b0ef6f`
- 提交时间：`2026-02-21T01:34:54-08:00`
- 提交标题：`Merge pull request #1398 from NikoPit/patch-1`
- 抓取方式：Git 浅克隆

## 项目定位

Build Your Own X 是一个“从零重建技术”的教程索引。仓库将其定位为高质量、分步骤教程的合集，目标是通过亲手实现数据库、操作系统、编程语言、网络栈等技术理解其内部原理。

它不是代码库、课程平台或统一教学体系。仓库自身主要负责分类和链接，教程正文由外部网站、GitHub 仓库、视频或 PDF 承载。

## 仓库结构

当前提交只跟踪四个文件：

- `.gitattributes`
- `ISSUE_TEMPLATE.md`
- `README.md`
- `codecrafters-banner.png`

没有独立的 `CONTRIBUTING.md`、LICENSE 文件、测试、脚本或 `.github/workflows/`。贡献说明和许可声明位于 README 底部。

## 内容规模

本次对 README 的静态统计：

- 504 行
- 约 46 KB
- 30 个 `Build your own` 分类
- 388 条以 Markdown 列表表示的教程条目
- 约 368 个 URL
- 34 条视频标记
- 1 条 PDF 标记

该统计反映当前提交的文本结构，不代表所有外部链接均有效，也不代表每条教程只包含一个 URL。

## 教程分类

README 包含以下 30 个明确分类：

1. Distributed Systems
2. 3D Renderer
3. AI Model
4. Augmented Reality
5. BitTorrent Client
6. Blockchain / Cryptocurrency
7. Bot
8. Command-Line Tool
9. Database
10. Docker
11. Emulator / Virtual Machine
12. Front-end Framework / Library
13. Game
14. Git
15. Memory Allocator
16. Network Stack
17. Neural Network
18. Operating System
19. Physics Engine
20. Processor
21. Programming Language
22. Regex Engine
23. Search Engine
24. Shell
25. Template Engine
26. Text Editor
27. Visual Recognition System
28. Voxel Engine
29. Web Browser
30. Web Server

README 另有 `Uncategorized` 区域，收录难以放入上述分类的实现教程。

## 主要语言分布

按教程条目前缀做静态计数，数量最多的语言为：

| 语言 | 条目数 |
|---|---:|
| Python | 71 |
| JavaScript | 51 |
| C | 49 |
| C++ | 33 |
| Go | 23 |
| Rust | 17 |
| Node.js | 15 |
| C# | 14 |
| Ruby | 13 |
| Nim | 9 |
| Java | 8 |

此外还覆盖 Haskell、PHP、TypeScript、Assembly、F#、Scala、OCaml、Lua、Kotlin、Clojure、Zig、Verilog、Racket、Perl 等语言。

该统计按 README 显示标签计算；同一条教程可能同时标注多种语言，因此不能用于精确衡量教程质量或生态活跃度。

## 内容组织方式

教程条目的基本格式是：

```text
[语言] + 教程标题 + 外部链接 + 可选媒介标记
```

目录按“要重建的系统”而不是按语言、难度或知识层级组织。例如：

- Database 分类包含从 KV Store、Redis 到 B+Tree 和 SQL 的实现。
- Programming Language 分类包含解释器、编译器、Lisp、Scheme、WebAssembly 等。
- Operating System 分类覆盖 bootloader、内核、驱动和完整教学操作系统。
- Network Stack 分类包含 TCP/IP、VPN 和虚拟交换机。
- AI Model 分类包含 LLM、Diffusion 和 RAG。

## 维护机制

README 的贡献说明只有两条：

- 通过 Pull Request 或 Issue 提交教程。
- 通过评论和 reaction 协助审核待提交内容。

仓库没有发现自动化链接检查、内容质量评分、难度分级或教程完成验证。

## 来源与许可

README 说明：

- 项目由 Daniel Stefanovic 发起。
- 当前由 CodeCrafters, Inc. 维护。
- 仓库索引内容采用 CC0 公共领域贡献方式。

外部教程仍受各自来源的许可约束，仓库的 CC0 声明不等于外链内容可自由复制。

## 本次检查的关键文件

- `README.md`
- `ISSUE_TEMPLATE.md`
- `.gitattributes`
- Git 提交历史和文件树
