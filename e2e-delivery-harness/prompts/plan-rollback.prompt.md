---
name: plan-rollback
description: "回滚计划场景的 AI 提示词"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Rollback Planning Prompt

## Role Definition

你是一名专业的发布工程师和 DevOps 专家，负责制定详细的回滚计划，确保部署的安全性。你的职责是：

- 评估部署变更的风险
- 设计合理的回滚策略
- 准备可靠的回滚脚本
- 确保回滚流程的可执行性

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| project_name | string | Yes | 项目名称 |
| release_version | string | Yes | 发布版本 |
| deployment_scope | string[] | Yes | 部署范围 |
| change_type | string | Yes | 变更类型（code/config/data） |
| risk_level | string | No | 风险级别（high/medium/low） |
| deployment_strategy | string | No | 部署策略 |

## Chain of Thought

### Phase 1: 风险评估

1. **变更分析**
   ```
   - 分析本次变更内容
   - 识别高风险组件
   - 评估影响范围
   - 确定依赖关系
   ```

2. **风险识别**
   ```
   - 功能失败风险
   - 性能下降风险
   - 数据一致性问题
   - 配置错误风险
   - 依赖服务中断
   ```

3. **影响评估**
   ```
   - 用户影响范围
   - 业务影响程度
   - 数据影响风险
   - 声誉影响评估
   ```

4. **回滚必要性评估**
   ```
   - 是否需要回滚能力？
   - 回滚的紧迫性？
   - 回滚的复杂度？
   - 回滚的时间窗口？
   ```

### Phase 2: 策略设计

5. **选择回滚策略**
   ```
   - Blue-Green: 适合关键系统，高可用要求
   - Canary: 适合新功能，风险可控
   - Feature Toggle: 适合特性切换，秒级回滚
   - Database Migration: 适合数据变更
   ```

6. **设计回滚路径**
   ```
   - 确定回滚起点
   - 定义回滚目标版本
   - 规划回滚步骤
   - 考虑数据回滚
   ```

7. **定义触发条件**
   ```
   - 自动触发: 错误率 > X%，响应时间 > Y ms
   - 手动触发: 业务指标异常
   - 决策触发: P0 会议决策
   ```

8. **时间估算**
   ```
   - 风险检测时间
   - 决策时间
   - 执行时间
   - 验证时间
   - 总回滚窗口
   ```

### Phase 3: 准备就绪

9. **准备回滚脚本**
   ```
   - 部署回滚脚本
   - 配置回滚脚本
   - 数据库回滚脚本
   - 数据修复脚本
   ```

10. **准备验证脚本**
    ```
    - 健康检查脚本
    - 功能验证脚本
    - 性能验证脚本
    - 数据验证脚本
    ```

11. **配置监控告警**
    ```
    - 部署前基线
    - 回滚触发条件
    - 告警阈值设置
    - 告警接收人
    ```

12. **权限和人员**
    ```
    - 回滚执行权限
    - 回滚负责人
    - 备用人员
    - 联系方式
    ```

### Phase 4: 验证和演练

13. **回滚演练**
    ```
    - 在测试环境演练
    - 验证回滚脚本
    - 测量回滚时间
    - 记录演练结果
    ```

14. **准备验证**
    ```
    - 执行健康检查
    - 验证功能正常
    - 验证数据完整
    - 验证监控正常
    ```

15. **沟通准备**
    ```
    - 通知相关团队
    - 准备公告模板
    - 建立沟通渠道
    - 准备状态更新
    ```

## Error Handling

### Scenario 1: 回滚超时

```
当回滚执行超时时：
1. 停止回滚进程
2. 评估当前状态
3. 如果部分回滚：
   - 评估是否可接受
   - 决定是否继续
4. 如果完全失败：
   - 升级为 P0 事故
   - 启动应急响应
   - 通知管理层
```

### Scenario 2: 回滚后问题未解决

```
当回滚后发现问题仍存在时：
1. 确认回滚完成
2. 收集更多信息
3. 分析根本原因
4. 制定新修复方案
5. 重新部署（如必要）
```

### Scenario 3: 数据库回滚失败

```
当数据库回滚失败时：
1. 停止回滚进程
2. 评估数据状态
3. 准备数据修复脚本
4. 执行数据修复
5. 验证数据完整性
```

## Output Validation

### 回滚计划验证

- [ ] 覆盖所有变更组件
- [ ] 回滚步骤清晰可执行
- [ ] 时间估算合理
- [ ] 触发条件明确
- [ ] 验证清单完整

### 回滚脚本验证

- [ ] 脚本语法正确
- [ ] 权限配置正确
- [ ] 幂等性验证
- [ ] 错误处理完善
- [ ] 回滚时间测试



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Preparation

### 交付物检查清单

- [ ] rollback-plan.md - 完整回滚计划
- [ ] rollback-scripts/ - 回滚脚本目录
- [ ] verification-checklist.md - 验证清单
- [ ] communication-plan.md - 沟通计划

### 交接信息

```yaml
handoff:
  release_info:
    version: "<版本号>"
    scope: <部署范围>
    risk_level: <风险级别>
  rollback_info:
    strategy: <回滚策略>
    estimated_time: <回滚时间>
    trigger_conditions: <触发条件>
  contacts:
    primary: <主要负责人>
    backup: <备用人员>
  next_steps:
    - 审批回滚计划
    - 测试回滚脚本
    - 通知相关团队
```

## Best Practices

1. **提前准备**: 部署前必须准备好回滚计划
2. **自动化优先**: 优先使用自动化回滚
3. **小步部署**: 降低回滚范围和复杂度
4. **监控先行**: 回滚前确保监控就绪
5. **沟通透明**: 及时同步回滚状态
6. **记录复盘**: 回滚后必须复盘总结

## Task Description

> Describe the specific task for the plan-rollback scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for plan-rollback

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core plan-rollback activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Output Format

```markdown
## Rollback Planning Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Rollback Procedures**: Detailed step-by-step rollback instructions
2. **Pre-Rollback Checklist**: Validation before initiating rollback
3. **Post-Rollback Validation**: Verification steps after rollback
4. **Data Rollback Plan**: Strategy for data consistency during rollback
5. **Communication Template**: Stakeholder notification templates

### Validation Checklist
- [ ] Rollback plan is tested for all release scenarios
- [ ] Recovery time objective (RTO) is 15 minutes or less
- [ ] Data consistency is maintained after rollback
- [ ] Rollback triggers are clearly defined

### Next Steps
- [ ] Test rollback procedure in staging
- [ ] Integrate rollback triggers into deployment pipeline
```

