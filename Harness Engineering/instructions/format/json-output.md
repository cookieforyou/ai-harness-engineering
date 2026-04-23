# JSON 输出格式指令 / JSON Output Format Instruction

> 【建议】当场景或 Agent 需要结构化输出时，引用本指令。

---

## 通用要求

1. **纯 JSON 输出**: 除非特别说明，否则响应体必须为合法 JSON，不含 Markdown 代码块标记
2. **无多余字段**: 不要输出未在 Schema 中定义的字段
3. **编码**: UTF-8，字符串中的特殊字符需正确转义
4. **日期格式**: ISO 8601（`2026-04-23T10:00:00Z`）

---

## Schema 声明规范

每个要求 JSON 输出的任务，应在 instructions 或 prompts 中附带 JSON Schema：

```json
{
  "type": "object",
  "required": ["status", "data"],
  "properties": {
    "status": { "type": "string", "enum": ["success", "partial", "failure"] },
    "data": { "type": "object" },
    "error": { "type": "string" }
  }
}
```

---

## 错误输出格式

当任务无法完成时，使用统一错误结构：

```json
{
  "status": "failure",
  "error": "简洁的错误描述",
  "error_code": "ERROR_TYPE_DETAIL",
  "escalation": {
    "required": true,
    "reason": "需要人工介入的原因"
  }
}
```

---

## 验证

所有 JSON 输出在交付前需通过 Schema 校验。校验失败视为该任务执行失败，触发重试或人工介入。
