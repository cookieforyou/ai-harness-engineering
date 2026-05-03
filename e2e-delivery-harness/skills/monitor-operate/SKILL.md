---
name: monitoring
description: 配置监控系统，执行日常巡检，处理告警和故障，保障系统稳定运行
category: operations
version: "1.0.0"
---

# Monitoring Skill

## Use When

使用此技能的场景：

- 应用上线后，需要进行运行监控
- 发生告警，需要进行故障排查
- 需要制定运维手册和应急预案
- 需要进行容量规划和性能优化

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 部署完成报告 | 文件 | 来自部署阶段的产出 |
| 系统架构 | 文件 | 系统的架构设计文档 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 监控需求 | 文本 | 特定的监控需求和要求 |
| 历史问题 | 文件 | 历史故障和问题记录 |

## Instructions

### 步骤 1：监控方案设计

**目标**：设计完整的监控指标体系

**操作**：
1. 定义基础监控指标（CPU、内存、磁盘、网络）
2. 定义应用监控指标（QPS、响应时间、错误率）
3. 定义业务监控指标（核心业务指标）
4. 设置告警阈值和级别
5. 配置告警通知渠道

**检查点**：
- [ ] 指标体系完整
- [ ] 阈值设置合理
- [ ] 通知配置正确

### 步骤 2：监控配置实施

**目标**：配置监控系统

**操作**：
1. 部署监控代理
2. 配置数据采集
3. 创建告警规则
4. 创建监控仪表盘
5. 验证监控生效

**检查点**：
- [ ] 代理已部署
- [ ] 数据已采集
- [ ] 告警已配置

### 步骤 3：日常巡检执行

**目标**：定期检查系统运行状态

**操作**：
1. 检查系统健康状态
2. 检查资源使用情况
3. 检查业务运行指标
4. 检查告警情况
5. 汇总巡检结果

**检查点**：
- [ ] 巡检已执行
- [ ] 结果已记录
- [ ] 问题已处理

### 步骤 4：告警响应处理

**目标**：及时响应和处理告警

**操作**：
1. 确认告警信息
2. 评估告警级别
3. 启动相应流程
4. 定位告警原因
5. 执行处理措施
6. 验证处理效果

**检查点**：
- [ ] 告警已确认
- [ ] 处理已执行
- [ ] 告警已消除

### 步骤 5：故障排查修复

**目标**：定位和解决系统故障

**操作**：
1. 确认故障现象
2. 评估故障影响
3. 收集故障信息
4. 分析故障原因
5. 制定修复方案
6. 执行修复措施
7. 验证修复效果
8. 编写故障报告

**检查点**：
- [ ] 故障已确认
- [ ] 原因已定位
- [ ] 修复已验证
- [ ] 报告已编写

### 步骤 6：容量管理评估

**目标**：评估和规划系统容量

**操作**：
1. 分析当前容量
2. 评估资源使用率
3. 分析业务增长趋势
4. 预测容量需求
5. 制定扩容计划

**检查点**：
- [ ] 容量已评估
- [ ] 需求已预测
- [ ] 计划已制定

### 步骤 7：运维优化

**目标**：持续改进运维效率

**操作**：
1. 分析运维数据
2. 识别优化机会
3. 实施优化措施
4. 更新运维文档
5. 分享运维经验

**检查点**：
- [ ] 优化已识别
- [ ] 措施已实施
- [ ] 文档已更新

## Expected Output

### 产出列表

1. **监控方案**：监控指标和告警规则
2. **运维手册**：日常运维操作指南
3. **应急预案**：故障处理流程和预案
4. **巡检报告**：周期巡检结果
5. **容量报告**：容量评估和规划

### 输出格式

```markdown
## 运维报告

### 监控概览
...

### 监控配置
...

### 巡检记录
...

### 告警记录
...

### 故障记录
...

### 容量评估
...

### 优化建议
...
```

## Quality Criteria

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 稳定性 | 系统稳定运行 | 可用率统计 |
| 响应性 | 问题及时响应 | 响应时间统计 |
| 可观测性 | 监控完善有效 | 覆盖率检查 |
| 持续改进 | 运维持续优化 | 优化记录检查 |

## Related Assets

- **Agent**: [../../agents/monitor-operate.agent.md](../../agents/monitor-operate.agent.md)
- **Instruction**: [../../instructions/monitoring-operations.instructions.md](../../instructions/monitoring-operations.instructions.md)
- **Prompt**: [../../prompts/monitor-operate.prompt.md](../../prompts/monitor-operate.prompt.md)


## Core Knowledge

> Essential knowledge domain for monitor-operate execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for monitor-operate excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during monitor-operate execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
