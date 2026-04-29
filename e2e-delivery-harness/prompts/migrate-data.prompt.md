# Prompt: 数据迁移场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行数据迁移流程，包括迁移评估、方案设计、迁移执行和数据验证。

## 变量定义 (Variables)

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `source_system` | string | 是 | 源系统名称 | "旧订单系统" |
| `target_system` | string | 是 | 目标系统名称 | "新订单系统" |
| `migration_scope` | object | 是 | 迁移范围 | 见 MigrationScope 结构 |
| `data_volume` | object | 是 | 数据量评估 | 见 DataVolume 结构 |
| `migration_window` | datetime | 是 | 迁移时间窗口 | "2024-01-15 02:00" |
| `allowed_downtime` | number | 是 | 允许停机时间(小时) | 4 |
| `migration_strategy` | enum | 是 | 迁移策略 | BIG_BANG/PARALLEL/PHASE |

### MigrationScope 结构

```typescript
interface MigrationScope {
  tables: string[];              // 迁移表列表
  records_estimate: number;       // 预估记录数
  total_size_gb: number;         // 总数据大小(GB)
  dependencies: string[];         // 依赖关系
  critical_data: string[];        // 关键数据
}
```

### DataVolume 结构

```typescript
interface DataVolume {
  tables: {
    name: string;
    rows: number;
    size_mb: number;
    growth_rate: number;        // 月增长率 %
  }[];
  total_rows: number;
  total_size_gb: number;
}
```

## Chain of Thought

```
1. [THINK] 理解系统 → 源和目标系统架构？
2. [THINK] 评估数据 → 数据量和复杂度？
3. [THINK] 设计方案 → 迁移策略和步骤？
4. [THINK] 准备脚本 → 数据清洗转换规则？
5. [EXECUTE] 执行迁移 → 按计划执行
6. [VALIDATE] 验证数据 → 完整性准确性
7. [OUTPUT] 输出报告 → 迁移结果
```

## 错误处理 (Error Handling)

### EH-1: 数据不一致

```
IF 校验发现数据不一致
THEN
  1. 记录不一致数据详情
  2. 分析不一致原因
  3. 修复或重新迁移
  4. 重新执行校验
END
```

### EH-2: 迁移超时

```
IF 迁移任务超时
THEN
  1. 检查任务执行状态
  2. 评估剩余工作量
  3. 决定继续或回滚
  4. 通知相关方
END
```

## Output Validation

### 验证清单

```markdown
## 自我验证报告

### V-001: 数据完整性
- [ ] 记录数一致
- [ ] 数据量一致
- [ ] 校验通过

### V-002: 数据准确性
- [ ] 字段值正确
- [ ] 业务规则正确
- [ ] 关联关系正确

### V-003: 功能验证
- [ ] 查询功能正常
- [ ] 写入功能正常
- [ ] 业务逻辑正常

### 验证结果
- 验证通过: [是/否]
```

## Handover 准备

```yaml
handover_to_production:
  deliverable: "数据迁移报告"
  status: "成功/失败/部分成功"

  summary:
    tables_migrated: N
    records_migrated: N
    duration: minutes
    success_rate: percentage

  validation:
    completeness: PASS/FAIL
    accuracy: PASS/FAIL
    integrity: PASS/FAIL
```

## Constraints

1. **零丢失**: 关键数据不能丢失
2. **可回滚**: 必须有回滚方案
3. **可追溯**: 迁移过程必须可追溯
