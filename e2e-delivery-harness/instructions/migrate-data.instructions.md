# Instruction: 数据迁移技术规范

## 概述

本文档定义了数据迁移阶段的技术规范和执行标准。

## 迁移策略

| 策略 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| BIG_BANG | 简单 | 停机时间长 | 小数据量 |
| PARALLEL | 风险低 | 成本高 | 关键系统 |
| PHASE | 灵活 | 周期长 | 大数据量 |

## 数据校验方法

```sql
-- 记录数校验
SELECT COUNT(*) FROM source;
SELECT COUNT(*) FROM target;

-- 数据和校验
SELECT SUM(column) FROM source;
SELECT SUM(column) FROM target;

--抽样校验
SELECT * FROM source ORDER BY RAND() LIMIT 100;
SELECT * FROM target ORDER BY id LIMIT 100;
```

## 关联资产

- **Scenario**: `scenarios/migrate-data/SCENARIO.md`
- **Prompt**: `prompts/migrate-data.prompt.md`
- **Agent**: `agents/data-migration-engineer.agent.md`
- **Skill**: `skills/migrate-data/SKILL.md`
