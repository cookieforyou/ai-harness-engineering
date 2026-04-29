# Prompt: 容量规划场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行容量规划工作。

## 变量定义 (Variables)

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `system_name` | string | 是 | 系统名称 | "订单系统" |
| `current_capacity` | object | 是 | 当前容量 | 见 Capacity 结构 |
| `growth_rate` | number | 是 | 业务增长率(%) | 20 |
| `planning_period` | number | 是 | 规划周期(月) | 12 |
| `budget_limit` | number | 否 | 预算限制(万) | 100 |

### Capacity 结构

```typescript
interface Capacity {
  current_users: number;         // 当前用户数
  current_tps: number;          // 当前 TPS
  current_storage_gb: number;   // 当前存储(GB)
  current_bandwidth_mbps: number; // 当前带宽(Mbps)
  utilization: {
    cpu: number;                // CPU 利用率 %
    memory: number;             // 内存利用率 %
    storage: number;            // 存储利用率 %
  };
}
```

## Chain of Thought

```
1. [THINK] 分析当前 → 当前容量和利用率？
2. [THINK] 预测需求 → 未来业务增长？
3. [THINK] 评估差距 → 容量缺口多大？
4. [THINK] 制定方案 → 如何扩容？
5. [VALIDATE] 验证方案 → 方案可行？
6. [OUTPUT] 输出报告 → 规划报告
```

## 错误处理 (Error Handling)

### EH-1: 数据不足

```
IF 历史数据不足
THEN
  1. 收集更多数据
  2. 使用行业基准
  3. 增加安全系数
END
```

## Output Validation

### 验证清单

```markdown
## 自我验证报告

### V-001: 数据完整性
- [ ] 历史数据分析完整
- [ ] 预测模型合理

### V-002: 方案可行性
- [ ] 预算可行
- [ ] 技术可行

### 验证结果
- 验证通过: [是/否]
```

## Handover 准备

```yaml
handover_to_management:
  deliverable: "容量规划报告"
  status: "完成"

  summary:
    current_utilization: object
    predicted_demand: object
    capacity_gap: object
    expansion_plan: object
    budget_estimate: number
```

## Constraints

1. **数据驱动**: 基于数据分析
2. **成本效益**: 合理控制成本
3. **可执行**: 方案切实可行
