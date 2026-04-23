# prompts / 提示词资产库

本目录是高质量、场景化、可复用的提示词模板集合。所有提示词经过工程化设计，支持变量注入与版本管理。

---

## 设计理念

> **提示词即接口**: 每个提示词模板应像函数签名一样清晰——有明确的输入、输出与副作用。

- **场景驱动**: 不按模型或技术分，而按业务场景分（如 code-review、doc-gen、data-pipeline）
- **变量化**: 所有动态内容使用 `{{variable_name}}` 注入，禁止硬编码
- **版本化**: 同一提示词支持多版本并存，场景通过 `assets.lock` 锁定版本
- **示例丰富**: 每个提示词至少包含一个完整正例（Few-shot 优先）

---

## 文件组织

```
prompts/
├── README.md
├── _meta/
│   └── prompt-style-guide.md     # 提示词编写风格指南
├── code-review/
│   ├── v1.md
│   ├── v2.md
│   └── report-template.md
├── doc-gen/
│   ├── api-doc-v1.md
│   └── design-doc-v1.md
└── ...
```

---

## 提示词模板规范

每个 `.md` 文件必须包含以下区块：

```markdown
# {Prompt Title} / {提示词标题}

## Meta / 元信息
- version: "1.0.0"
- author: "author-name"
- scope: "适用的场景或 Agent"
- model_recommendation: "推荐使用的模型"

## Variables / 变量声明
- `{{user_input}}` — 说明
- `{{context}}` — 说明

## Instruction / 指令正文
{实际的提示词内容，使用 {{variable}} 标记变量}

## Examples / 示例（可选但推荐）
### Example 1
**Input:**
...
**Output:**
...

## Notes / 备注
- 使用时的注意事项
- 已知限制
```

---

## 版本管理

- 首次创建为 `v1.md`
- 重大语义变更（输入输出结构变化）升级主版本：`v2.md`
- 优化措辞但结构不变升级次版本：同文件内更新 `version` 标签
- 旧版本保留至少一个完整发布周期，确保依赖方平滑迁移

---

## 新增提示词流程

1. 在对应业务域目录下创建（若无则新建目录）
2. 按照上述模板规范编写
3. 自测：替换变量后是否能直接用于目标模型？
4. 补充至至少一个 `scenarios/` 或 `agents/` 中作为引用
5. 若替代旧版本，同步更新引用方的 `assets.lock`
