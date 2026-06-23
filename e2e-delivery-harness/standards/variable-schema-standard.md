---
name: variable-schema-standard
description: "Prompt 输入变量的标准化 Schema 定义规范，使用 JSON Schema 实现机器可读的变量类型、验证规则和约束声明"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
tags: ['standard', 'variables', 'json-schema', 'validation']
---

# 变量 Schema 标准化规范

## 概述

本文件定义了 E2E Delivery Harness 中所有 Prompt 文件的**输入变量标准化 Schema 规范**。每个 Prompt 必须为其输入变量提供机器可读的 JSON Schema 定义，使 AI Agent 能在执行前自动验证变量完整性。

## 变量定义格式

### 基础格式（Prompt 文件中的人类可读表格）

```markdown
## Input Variables

| Variable | Type | Required | Default | Validation | Description |
|----------|------|----------|---------|------------|-------------|
| `project_name` | string | true | - | 非空，≤100字符 | 项目名称 |
| `target_environment` | enum | true | - | "prod"/"staging"/"dev" | 目标部署环境 |
| `max_retries` | integer | false | 3 | ≥0, ≤10 | 最大重试次数 |
```

### 机器可读格式（JSON Schema 块）

每个 Prompt 文件在 Input Variables 表格后必须附加 JSON Schema 块：

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "variables/{scenario-name}",
  "title": "{Scenario Name} Input Variables",
  "type": "object",
  "required": ["project_name", "target_environment"],
  "properties": {
    "project_name": {
      "type": "string",
      "description": "项目名称",
      "minLength": 1,
      "maxLength": 100
    },
    "target_environment": {
      "type": "string",
      "description": "目标部署环境",
      "enum": ["prod", "staging", "dev"]
    },
    "max_retries": {
      "type": "integer",
      "description": "最大重试次数",
      "default": 3,
      "minimum": 0,
      "maximum": 10
    }
  },
  "additionalProperties": false
}
```

## 变量类型枚举

| 类型 | JSON Schema type | 使用场景 | 示例 |
|------|-----------------|---------|------|
| `string` | `"type": "string"` | 文本输入 | 项目名称、描述文本 |
| `integer` | `"type": "integer"` | 整数数值 | 端口号、计数、重试次数 |
| `number` | `"type": "number"` | 浮点数 | 百分比、阈值、比率 |
| `boolean` | `"type": "boolean"` | 开关标记 | 是否启用某功能 |
| `enum` | `"enum": [...]` | 枚举选择 | 环境、策略、级别 |
| `array` | `"type": "array"` | 列表数据 | 文件列表、服务清单 |
| `object` | `"type": "object"` | 结构化数据 | 配置对象、嵌套参数 |
| `markdown` | `"type": "string", "contentMediaType": "text/markdown"` | Markdown 文本 | 需求文档、设计文档 |
| `yaml` | `"type": "string", "contentMediaType": "application/yaml"` | YAML 配置 | 部署配置、流水线定义 |
| `filepath` | `"type": "string", "pattern": "..."` | 文件路径 | 相对路径、绝对路径 |
| `url` | `"type": "string", "format": "uri"` | URL 地址 | API 端点、健康检查地址 |

## 常见验证规则

```json
{
  "common_validations": {
    "non_empty_string": { "type": "string", "minLength": 1 },
    "semver": { "type": "string", "pattern": "^v?\\d+\\.\\d+\\.\\d+(-[a-zA-Z0-9.]+)?$" },
    "percentage": { "type": "integer", "minimum": 0, "maximum": 100 },
    "positive_integer": { "type": "integer", "minimum": 1 },
    "iso8601": { "type": "string", "format": "date-time" },
    "email": { "type": "string", "format": "email" },
    "git_sha": { "type": "string", "pattern": "^[a-f0-9]{7,40}$" },
    "kebab_case": { "type": "string", "pattern": "^[a-z][a-z0-9]*(-[a-z][a-z0-9]*)*$" }
  }
}
```

## TypeScript 接口（可选增强）

对于复杂嵌套对象，Prompt 可额外提供 TypeScript 接口：

```typescript
// 示例：性能测试需求定义
interface PerformanceRequirements {
  target_qps: number;           // 目标 QPS
  p99_latency_ms: number;       // P99 延迟目标 (ms)
  max_error_rate: number;       // 最大错误率 (%)
  concurrent_users: number;     // 并发用户数
  ramp_up_seconds: number;      // 加压时间 (s)
  steady_state_seconds: number; // 稳态持续时间 (s)
  test_duration_minutes: number; // 总测试时长 (min)
}
```

## 变量验证自动化

配套验证脚本 `scripts/validate-variables.py` 可自动检查：
1. Prompt 文件中 Required=true 的变量是否有值
2. 变量值是否符合 JSON Schema 定义的约束
3. 变量类型与声明是否一致

使用方式：
```bash
# 验证单个场景的变量
python3 scripts/validate-variables.py --scenario deploy-release --variables vars.yaml

# 批量验证所有场景
python3 scripts/validate-variables.py --all
```

## 相关资产

- [cot-framework.md](cot-framework.md) - CoT 执行框架
- [error-classification.md](error-classification.md) - 错误分类体系
- [output-quality-rubric.md](output-quality-rubric.md) - 输出质量评分
