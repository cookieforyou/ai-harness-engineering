---
name: stakeholder-analysis
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 干系人分析 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 干系人识别

### 干系人清单

| 干系人 | 角色/职位 | 所属组织 | 项目角色 | 联系方式 |
|--------|-----------|----------|----------|----------|
| {name} | {title} | {organization} | {project_role} | {contact} |
| {name} | {title} | {organization} | {project_role} | {contact} |
| {name} | {title} | {organization} | {project_role} | {contact} |

## 干系人分析矩阵

### 影响力-兴趣矩阵

| 干系人 | 影响力 (高/中/低) | 兴趣度 (高/中/低) | 管理策略 |
|--------|-------------------|-------------------|----------|
| {name} | High / Medium / Low | High / Medium / Low | {manage_closely / keep_satisfied / keep_informed / monitor} |
| {name} | High / Medium / Low | High / Medium / Low | {manage_closely / keep_satisfied / keep_informed / monitor} |

### 影响力-兴趣矩阵说明

```
高影响力 + 高兴趣度 → 重点管理 (Manage Closely)
高影响力 + 低兴趣度 → 保持满意 (Keep Satisfied)
低影响力 + 高兴趣度 → 及时告知 (Keep Informed)
低影响力 + 低兴趣度 → 定期监控 (Monitor)
```

## 干系人详情

### {干系人名称}

| 维度 | 内容 |
|------|------|
| 角色描述 | {role_description} |
| 利益诉求 | {interests_and_expectations} |
| 主要关注点 | {key_concerns} |
| 对项目的态度 | {正面 / 中立 / 负面} |
| 影响力来源 | {influence_source} |
| 风险等级 | 高 / 中 / 低 |

**沟通策略**:
- **沟通频率**: {daily / weekly / monthly / milestone}
- **沟通方式**: {会议 / 邮件 / 报告 / 即时消息}
- **沟通内容**: {communication_content}
- **最佳触达时间**: {preferred_time}

**期望管理**:
- {期望1}: {管理策略}
- {期望2}: {管理策略}

**支持/反对因素**:
- **支持因素**: {support_factors}
- **反对因素**: {opposition_factors}

## 沟通计划

| 沟通对象 | 沟通内容 | 频率 | 渠道 | 负责人 |
|----------|----------|------|------|--------|
| {stakeholder} | {content} | {frequency} | {channel} | {owner} |
| {stakeholder} | {content} | {frequency} | {channel} | {owner} |

## 干系人风险

| 风险ID | 干系人 | 风险描述 | 影响 | 缓解措施 |
|--------|--------|----------|------|----------|
| SR-001 | {name} | {description} | {impact} | {mitigation} |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
