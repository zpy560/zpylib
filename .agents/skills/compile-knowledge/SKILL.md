---
name: compile-knowledge
description: Manage this project's local Markdown knowledge base. Use when Codex needs to ingest a URL, text PDF, saved article, or personal idea; compile or update topic/entity pages; answer questions from existing knowledge; repair indexes or related links; or generate writing briefs from the knowledge base.
---

# 编译本地知识

遵守项目根目录的 `AGENTS.md` 和 `techarc.md`。使用现有 Markdown 文件完成工作，不引入数据库、向量库、UI、服务或新依赖。

## 开始前

1. 读取 `AGENTS.md`。
2. 根据任务读取对应模板和 `templates/tags.yaml`。
3. 检查 `indexes/INDEX.md`，了解现有主题和内容。
4. 修改 `wiki/` 前检查 Git 状态；没有可恢复基线时先提醒用户。

## 选择工作流

- 用户提供链接、PDF、保存的文章或想法：执行“入库”。
- 用户要求整理某个主题或新资料影响已有结论：执行“编译”。
- 用户提出知识问题：执行“问答”。
- 用户要求写什么、生成选题或内容方向：执行“选题”。
- 用户要求检查知识库：执行“维护”。

## 入库

1. 识别输入类型并保存：
   - 链接：保存 URL 和正文到 `raw/`。
   - 文字型 PDF：保留原 PDF，并保存提取文本。
   - 扫描 PDF、微信、X 或抓取失败：停止自动重试，请用户手动保存。
   - 想法：使用 `templates/idea.md`。
2. 原料文件只追加，不覆盖。
3. 使用 `templates/note.md` 创建一篇单源笔记。
4. 生成稳定 `id`，文件名使用 `YYYY-MM-DD-slug.md`。
5. 从固定词表选择 1 至 5 个标签；缺少合适标签时先提出词表修改，不直接新增。
6. 搜索已有笔记和主题页，填写 `related`，并同步维护双向关联。
7. 判断是否需要创建或更新主题页、实体页。
8. 更新 `indexes/INDEX.md` 的统计和导航。
9. 报告新增文件、修改文件、冲突和手动处理项。

## 编译

1. 读取目标主题页、关联笔记和必要原料。
2. 区分原文事实、作者观点、用户判断和 AI 推断。
3. 使用 `templates/topic.md` 或 `templates/entity.md` 更新页面。
4. 保留仍有效的旧结论，明确标注新增证据、冲突和变化。
5. 更新 `related`、更新记录和总索引。
6. 不因编译修改 `raw/`。

## 问答

按 `indexes/INDEX.md` → `wiki/` → `notes/` → `raw/` 的顺序读取，信息够用即停止扩展。回答时：

- 先给结论。
- 引用对应文件。
- 明确哪些是资料事实，哪些是综合判断。
- 资料不足时直接说明缺口，不补造事实。

## 选题

1. 读取相关主题页和单源笔记。
2. 使用 `templates/brief.md` 写入 `briefs/`。
3. 每个选题包含核心观点、内容结构、可引用来源和资料缺口。
4. 更新总索引。

## 维护

检查并报告：

- 必填 frontmatter 字段。
- 不在固定词表中的标签。
- 失效的 `related` 路径和缺少的反向关联。
- 未进入索引的笔记、主题页、实体页和选题。
- 被意外修改或覆盖的原料。

只修复用户要求范围内的问题；删除、移动和 Git 回滚前先获得确认。
