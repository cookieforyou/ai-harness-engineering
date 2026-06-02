# 干系人分析指南

## 四类关键角色（必须覆盖）

| 类型 | 英文 | 说明 | 示例 |
|------|------|------|------|
| 决策者 | Decision Maker | 预算、范围、优先级拍板 | 产品总监、发起人 |
| 使用者 | User | 直接操作系统的人 | 终端用户、运营 |
| 影响者 | Influencer | 无决策权但影响方案 | 架构师、合规 |
| 监管者 | Regulator | 合规、审计、法务 | 安全、法务 |

## 影响力矩阵

| 干系人 | 影响力 (H/M/L) | 利益相关度 | 策略 |
|--------|----------------|------------|------|
| {name} | H | H | 密切合作 |
| {name} | H | L | 满足期望 |
| {name} | L | H | 随时告知 |

## 沟通计划

```yaml
stakeholder_communication:
  - name: "{name}"
    role: "{role}"
    type: Decision Maker|User|Influencer|Regulator
    frequency: weekly|per-milestone|ad-hoc
    channel: workshop|email|review
    key_concerns: []
```

## 冲突处理

1. 记录冲突双方诉求与背后 OBJ-*
2. 提供至少 2 个折中方案（DC-003）
3. 2 轮协商无果 → 升级决策者

## 产出物

- `docs/stakeholder-analysis.md`：矩阵 + 沟通计划
- 纳入 Handover `confirmed_stakeholder_needs`
