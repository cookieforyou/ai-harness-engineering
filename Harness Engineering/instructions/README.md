# instructions / 指令集

本目录存放系统级指令（System Instructions）与行为约束，用于控制 Agent 的全局行为模式、安全边界和输出规范。

---

## 设计理念

> **指令即缰绳**: 好的指令不是更长的 Prompt，而是更精确的结构化约束。

- **分层约束**: 全局指令 → 场景指令 → 任务指令，越往下越具体
- **负面约束优先**: 明确告诉 Agent "不能做什么" 比 "尽量做好" 更有效
- **可验证性**: 指令应能被 evaluations 中的规则直接检验

---

## 文件组织

```
instructions/
├── README.md
├── system/
│   ├── code-review-system.md
│   └── doc-gen-system.md
├── safety/
│   ├── data-privacy.md
│   ├── no-secrets-leak.md
│   └── refuse-policy.md
├── format/
│   ├── json-output.md
│   └── report-template.md
└── ...
```

---

## 指令编写规范

1. **使用结构化 Markdown**: 标题层级清晰，便于 Agent 解析重点
2. **优先级标记**: 对关键约束使用 `【强制】`、`【重要】`、`【建议】` 标签
3. **示例驱动**: 对格式类指令必须提供输入/输出示例
4. **单一职责**: 一个文件聚焦一个约束维度，避免大杂烩

---

## 引用方式

在 Agent 配置或场景编排中引用：

```yaml
instructions:
  system: "instructions/system/code-review-system.md"
  safety:
    - "instructions/safety/data-privacy.md"
    - "instructions/safety/no-secrets-leak.md"
  format: "instructions/format/json-output.md"
```

---

## 新增指令流程

1. 确定约束类型（system / safety / format / ...）
2. 编写指令文件，附示例与违规后果说明
3. 在 `evaluations/` 中补充可自动化检验该指令的检测规则
4. 更新 `standards/` 中相关规范文档（如新增一类约束需更新分类标准）
