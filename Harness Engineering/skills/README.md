# skills / 技能模块

本目录封装**可复用的原子能力**。技能是 Agent 或场景调用的最小功能单元，类似于传统编程中的"函数"或"服务"。

---

## 设计理念

> **技能即 API**: 每个技能有明确的输入输出 Schema、错误处理策略与实现方式。

- **原子性**: 单一职责，一个技能只做一件事
- **可组合**: 复杂能力通过组合多个技能实现，而非编写大而全的技能
- **多实现**: 同一技能接口可支持 LLM 实现、代码实现、外部 API 调用
- **自描述**: 技能定义本身包含足够信息，供编排引擎自动匹配与调用

---

## 文件组织

```
skills/
├── README.md
├── diff-parser.yaml
├── security-audit.yaml
├── report-merger.yaml
├── notification.yaml
├── trace-archiver.yaml
├── doc-generator.yaml
└── ...
```

---

## 技能定义规范 (`.yaml`)

```yaml
skill_id: "diff-parser"
version: "1.0.0"
description: "将统一 diff 字符串解析为结构化文件变更列表"

interface:
  input_schema:
    type: "object"
    required: ["raw_diff"]
    properties:
      raw_diff:
        type: "string"
        description: "统一 diff 格式的原始文本"
  output_schema:
    type: "array"
    items:
      type: "object"
      properties:
        file_path: { type: "string" }
        change_type: { type: "string", enum: ["added", "modified", "deleted"] }
        hunks:
          type: "array"
          items:
            type: "object"
            properties:
              old_start: { type: "integer" }
              new_start: { type: "integer" }
              lines:
                type: "array"
                items:
                  type: "object"
                  properties:
                    type: { type: "string", enum: ["context", "add", "remove"] }
                    content: { type: "string" }

implementation:
  type: "code"            # code | llm | api | hybrid
  runtime: "python"
  entry: "diff_parser.parse"
  dependencies:
    - "unidiff>=0.7.0"

error_handling:
  strategy: "fail_fast"
  fallback: null
  on_error:
    output:
      status: "error"
      error_code: "DIFF_PARSE_ERROR"
      message: "无法解析 diff 格式"

examples:
  - input:
      raw_diff: "diff --git a/src/main.py..."
    output:
      - file_path: "src/main.py"
        change_type: "modified"
        hunks: [...]

observability:
  metrics:
    - "execution_time_ms"
    - "files_parsed"
  logs:
    level: "DEBUG"
```

---

## 实现类型说明

| type | 说明 | 适用场景 |
| :--- | :--- | :--- |
| `code` | 纯代码实现，确定性执行 | 数据解析、格式转换、简单计算 |
| `llm` | 由 LLM 根据提示词完成 | 自然语言理解、创意生成、复杂推理 |
| `api` | 调用外部服务 | 搜索、知识库查询、专有系统对接 |
| `hybrid` | 代码 + LLM 混合 | 先结构化提取再 LLM 推理 |

---

## 技能复用与依赖

- 技能之间应尽量**无状态、无耦合**
- 若技能 A 依赖技能 B，应在 `implementation.dependencies` 中声明引用关系
- 禁止循环依赖

---

## 新增技能流程

1. 定义清晰的输入输出 Schema（参考 `templates/skill-skeleton.yaml`）
2. 选择实现类型（code / llm / api / hybrid）
3. 编写实现（代码或提示词）
4. 提供至少 2 个 input/output 示例
5. 定义错误处理与降级策略
6. 在 `evaluations/` 中补充该技能的单元级评估（若有逻辑）
7. 注册至 `standards/skill-registry.yaml`（全局索引）
