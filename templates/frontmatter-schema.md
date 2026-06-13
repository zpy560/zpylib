# Frontmatter 约定

所有 `notes/`、`wiki/` 和 `briefs/` Markdown 文件必须包含：

```yaml
---
id: "YYYYMMDD-HHMMSS-slug"
title: "标题"
type: "note"
source: ""
created_at: "YYYY-MM-DD"
tags: []
related: []
---
```

## 字段规则

| 字段 | 规则 |
|---|---|
| `id` | 创建时生成，之后不得修改 |
| `title` | 简洁表达文件的核心内容 |
| `type` | 只允许 `note`、`topic`、`entity`、`brief` |
| `source` | URL、原始文件相对路径；想法可以为空 |
| `created_at` | 使用 `YYYY-MM-DD` |
| `tags` | 只能使用 `templates/tags.yaml` 中的值 |
| `related` | 使用项目内相对路径 |

