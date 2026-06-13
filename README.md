# 本地 AI 知识编译系统

这是一个通过 Codex 使用、以 Markdown 为主数据的长期自用知识库。

## v1 能力

- 收录普通网页、文字型 PDF 和个人想法
- 生成带判断的单源笔记
- 使用固定标签和双向关联组织内容
- 把多篇笔记编译为主题页
- 基于主题页问答、查找和生成选题

## 使用入口

直接在项目目录中向 Codex提出：

```text
把这个链接入库：<URL>
```

```text
把这个 PDF 入库：<文件路径>
```

```text
记录一个想法：<内容>
```

```text
基于现有知识回答：<问题>
```

```text
基于 <主题> 生成 3 个选题
```

Codex 应按 `AGENTS.md` 和项目 Skill 执行。

## 文档

- 产品定义：`07-ai-product-thinking-20260604.md`
- 架构定义：`08-ai-architecture-thinking-20260610.md`
- 技术架构：`techarc.md`
- 总索引：`indexes/INDEX.md`

