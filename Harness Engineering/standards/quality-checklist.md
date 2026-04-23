# 资产入库检查清单 / Quality Checklist

> **效力等级**: P0（强制）  
> **执行时机**: 任何资产新增或重大变更合并前

---

## 通用检查项

### 文档与元信息
- [ ] 文件头部或同目录 README 包含版本号、作者、适用范围
- [ ] 命名符合 `standards/naming-convention.md`
- [ ] 若存在旧版本，已同步更新 CHANGELOG

### 结构与规范
- [ ] 资产类型对应的必选字段已全部填充
- [ ] 无拼写错误、无遗留的 TODO/FIXME（已完成的应删除）
- [ ] 无敏感信息泄露（密钥、内网地址、个人数据）

### 依赖与兼容性
- [ ] 引用的外部资产版本已锁定（`assets.lock` 或配置内 version 字段）
- [ ] 循环依赖检查通过
- [ ] 未引入未在 `standards/skill-registry.yaml` 中登记的新技能（如适用）

---

## 分类型检查项

### Agent 资产 (`.role.md` + `.config.yaml`)
- [ ] 角色卡包含：Goal、Persona、Capabilities、Boundaries、Tools、Collaboration
- [ ] 配置中指定了模型参数、超时、重试策略
- [ ] 明确定义了人工介入触发条件
- [ ] 安全指令引用完整（至少包含 `instructions/safety/` 下相关文件）

### Skill 资产 (`.yaml`)
- [ ] 包含完整的 input_schema 与 output_schema（JSON Schema 格式）
- [ ] 声明了实现类型（code / llm / api / hybrid）
- [ ] 定义了 error_handling 策略与 fallback 行为
- [ ] 提供了至少 1 个 input/output 示例
- [ ] 若为 code 实现，代码已通过静态检查与单元测试

### Prompt 资产 (`.md`)
- [ ] 包含 Meta、Variables、Instruction、Examples 区块
- [ ] 所有外部输入已变量化（`{{variable}}`），无硬编码业务数据
- [ ] 输出格式有明确约束（Schema 或模板）
- [ ] 关键约束在提示词末尾有重复强调

### Scenario 资产 (`flow.yaml`)
- [ ] 包含 input_schema、nodes、edges 完整定义
- [ ] 每个节点有唯一的 id 与明确的 type
- [ ] 条件分支覆盖全部可能状态（无遗漏路径）
- [ ] 包含至少一个 checkpoint 节点作为质量门禁
- [ ] `assets.lock` 已生成且 checksum 有效

### Evaluation 资产 (`.checkpoint.yaml`)
- [ ] 定义了 3-5 个评分维度，权重之和为 1.0
- [ ] 至少有一个 mandatory 维度（通常是 safety）
- [ ] 阈值设置合理（非全 5 分或全 0 分）
- [ ] 若需要数据集，dataset 样本数 >= 10

### Instruction 资产 (`.md`)
- [ ] 使用结构化 Markdown，约束有优先级标签（【强制】/【重要】/【建议】）
- [ ] 提供示例说明正确与错误的处理方式
- [ ] 与 `evaluations/` 中的自动化检测规则可对应

---

## 评审与签字

| 角色 | 检查重点 | 签字 |
| :--- | :--- | :--- |
| 作者 | 功能正确性、完整性 | ✅ |
| 模块负责人 | 规范符合性、接口一致性 | ✅ |
| 安全专员 | 安全合规、隐私保护 | ✅ |
| 质量专员 | 评估覆盖、测试充分 | ✅ |

> 所有签字完成后，方可合并至主分支并纳入生产使用。
