# 结构化输出格式指令 / Structured Output Format Instruction

> **效力等级**: L1（全局约束）
> **适用范围**: 本资产库全部 Agent 与 Skill 的主输出

---

## 1. JSON 输出强制规范

- 所有机器消费的主输出必须为纯 JSON 文本，禁止包裹 Markdown 代码块（```json）
- JSON 必须合法可解析，键名使用 snake_case
- 字符串值使用双引号，禁止使用单引号
- 数值类型禁止加引号（如 `"count": 10` 正确，`"count": "10"` 错误）

## 2. 双格式输出策略

当输出同时需要机器解析与人工阅读时，采用双格式输出：

```
{
  "structured": { ... },
  "human_readable": "Markdown 格式的摘要或报告"
}
```

- `structured`: 严格遵循 Schema，供下游节点解析
- `human_readable`: 供人工快速浏览，不保证结构化

## 3. 错误响应格式

所有错误响应必须统一格式：

```json
{
  "status": "error",
  "error_code": "UPPER_SNAKE_CASE",
  "message": "人类可读的错误描述",
  "suggestions": ["建议修复步骤 1", "建议修复步骤 2"],
  "retryable": true
}
```

## 4. Schema 兼容性

- 新增字段必须为可选（不破坏旧解析器）
- 删除或重命名字段属于破坏性变更，需升级 MAJOR 版本
- 枚举值新增属于向后兼容，但需评估下游影响

## 5. 验证要求

- 输出前必须通过 `skills/schema-validator.yaml` 自校验
- 校验失败时返回统一错误格式，不输出部分结果
