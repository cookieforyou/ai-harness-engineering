---
name: review-incident
description: review incident execution prompt for E2E delivery workflow
type: execution
version: "1.1.0"
stage: review-incident
---

# Prompt: 故障复盘场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行故障复盘流程，包括事件还原、根因分析、教训总结和改进措施制定。

## 执行变量 (Variables)

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `incident_id` | string | 是 | 故障ID | "INC-20240115-001" |
| `incident_title` | string | 是 | 故障标题 | "支付服务不可用" |
| `incident_severity` | enum | 是 | 严重等级 | SEV1/SEV2/SEV3/SEV4 |
| `incident_start_time` | datetime | 是 | 故障开始时间 | "2024-01-15 14:30:00" |
| `incident_end_time` | datetime | 是 | 故障恢复时间 | "2024-01-15 16:45:00" |
| `total_duration` | number | 是 | 总时长(分钟) | 135 |
| `affected_services` | string[] | 是 | 受影响服务 | ["支付服务", "订单服务"] |
| `impact_scope` | object | 是 | 影响范围 | 见 ImpactScope 结构 |
| `detection_info` | object | 是 | 发现信息 | 见 DetectionInfo 结构 |
| `resolution_info` | object | 是 | 解决信息 | 见 ResolutionInfo 结构 |
| `participants` | string[] | 是 | 参与人员 | ["工程师A", "工程师B"] |
| `incident_manager` | string | 是 | 故障经理 | "im_name" |
| `related_monitors` | string[] | 否 | 相关监控告警 | ["alert-123", "alert-456"] |
| `related_changes` | string[] | 否 | 相关变更 | ["CHG-20240115-001"] |
| `postmortem_attendees` | string[] | 是 | 复盘会议参与人 | ["team_lead", "sre_lead"] |

### ImpactScope 结构

```typescript
interface ImpactScope {
  user_count: number;              // 受影响用户数
  error_rate?: number;             // 错误率百分比
  business_loss?: number;          // 业务损失金额
  affected_regions?: string[];     // 受影响区域
  affected_features: string[];     // 受影响功能
}
```

### DetectionInfo 结构

```typescript
interface DetectionInfo {
  detected_by: 'USER_REPORT' | 'MONITOR' | 'ON_CALL' | 'AUTOMATION';
  detection_time: datetime;        // 发现时间
  time_to_detect: number;         // 发现耗时(分钟)
  first_indicator: string;         // 首个告警指标
}
```

### ResolutionInfo 结构

```typescript
interface ResolutionInfo {
  root_cause: string;              // 根本原因
  resolution_type: 'AUTOMATIC' | 'MANUAL' | 'ROLLBACK' | 'SCALE';
  mitigation_time?: datetime;      // 缓解时间
  resolution_time?: datetime;      // 解决时间
  resolution_steps: string[];      // 解决步骤
}
```

## 思维链 (Chain of Thought)

### Step 1: 事件时间线重建

```
时间线要素:
1. 变更事件
   - 最近的代码变更
   - 配置变更
   - 部署操作

2. 异常信号
   - 首次告警
   - 告警升级
   - 监控异常

3. 响应过程
   - 发现时间
   - 上报时间
   - 响应开始
   - 缓解开始
   - 解决完成
```

### Step 2: 根因分析 (5 Whys / Fishbone)

```
5 Whys 分析法:
Why 1: 为什么支付服务不可用?
→ 数据库连接池耗尽

Why 2: 为什么数据库连接池耗尽?
→ 存在慢查询占用连接

Why 3: 为什么存在慢查询?
→ 缺少索引优化

Why 4: 为什么缺少索引优化?
→ 上次变更未进行性能评估

Why 5: 为什么未进行性能评估?
→ 变更流程缺少性能检查环节

根因: 变更流程缺少性能检查环节
```

### Step 3: 故障分类与分析

```
分类维度:
1. 按原因分类
   - 代码缺陷
   - 配置错误
   - 基础设施
   - 第三方依赖
   - 运维操作
   - 流量异常

2. 按阶段分类
   - 预防失效
   - 检测失效
   - 响应失效
   - 恢复失效

3. 按系统性分类
   - 偶发性 (一次性)
   - 结构性 (存在隐患)
```

### Step 4: 影响评估

```
评估维度:
1. 用户影响
   - 受影响用户数量
   - 用户操作失败类型
   - 用户投诉/反馈

2. 业务影响
   - 直接经济损失
   - 订单损失
   - 客户流失风险

3. 声誉影响
   - SLO/SLA 违规
   - 公开事件影响
```

### Step 5: 改进措施制定

```
改进措施分类:
1. 即时修复 (Immediate)
   - 已执行的修复
   - 短期缓解措施

2. 短期改进 (Short-term, 1-4周)
   - 监控告警增强
   - 自动化能力
   - 文档完善

3. 长期改进 (Long-term, 1-3月)
   - 架构优化
   - 流程改进
   - 工具平台建设
```

## Error Handling

### 识别信号

| 信号类型 | 检测条件 | 优先级 |
|----------|----------|--------|
| 根因不明确 | 无法确定单一根因 | HIGH |
| 时间线不连续 | 关键时间点缺失 | HIGH |
| 证据不充分 | 缺少日志/监控数据 | HIGH |
| 改进措施模糊 | 无法验证执行效果 | MEDIUM |
| 责任归属不清 | 多人/多团队责任交叉 | MEDIUM |

### 处理方式

1. **根因不明确**
   - 使用 Fishbone 图扩展分析
   - 收集更多证据
   - 标记为"待进一步分析"

2. **时间线不连续**
   - 标注缺失时间段
   - 要求补充相关日志
   - 使用推测但需标注

3. **改进措施模糊**
   - 要求 SMART 化描述
   - 明确责任人和验收标准
   - 拆解为可执行的小项

### 升级条件

```
HIGH 升级条件:
- SEV1/SEV2 级别故障
- 影响超过 1 小时
- 涉及用户数据安全
- 发现系统性隐患

MEDIUM 升级条件:
- 复盘会议无法达成共识
- 改进措施涉及跨团队协调
```

## 输出验证 (Output Validation)

### 必须包含的字段

- [ ] `incident_id`: 故障唯一标识符
- [ ] `summary`: 事件摘要 (5句话内)
- [ ] `timeline`: 完整时间线
- [ ] `root_cause`: 根本原因分析
- [ ] `impact_assessment`: 影响评估
- [ ] `what_went_well`: 做得好的一面
- [ ] `what_went_wrong`: 做不好的一面
- [ ] `action_items`: 改进措施清单
- [ ] `lessons_learned`: 经验教训
- [ ] `follow_up`: 后续跟进事项

### 改进措施格式

```typescript
interface ActionItem {
  item_id: string;               // 措施编号
  description: string;            // 措施描述
  type: 'PREVENTIVE' | 'DETECTIVE' | 'CORRECTIVE';
  priority: 'P0' | 'P1' | 'P2';
  owner: string;                  // 负责人
  due_date?: string;              // 截止日期
  status: 'OPEN' | 'IN_PROGRESS' | 'COMPLETED';
  verification_method: string;    // 验证方法
}
```

### 质量标准

| 检查项 | 标准 |
|--------|------|
| 时间线完整性 | 覆盖 100% 关键节点 |
| 根因准确性 | 可解释所有症状 |
| 改进措施可执行性 | 每项有明确的 Owner 和验收标准 |
| 经验教训可复用性 | 可指导类似故障预防 |

## 交接准备 (Handover Context)

```markdown
## 故障复盘交接上下文

### 故障基础信息
- 故障ID: {incident_id}
- 严重等级: {incident_severity}
- 发生时间: {incident_start_time}
- 持续时长: {total_duration} 分钟

### 故障概要
- 影响服务: {affected_services}
- 影响用户: {user_count} 人
- 业务损失: {business_loss} 元

### 根因
- 直接原因: {direct_cause}
- 根本原因: {root_cause}
- 改进方向: {improvement_direction}

### 改进措施统计
- 总计: {total_items}
  - P0 (立即): {p0_count}
  - P1 (短期): {p1_count}
  - P2 (长期): {p2_count}

### 待跟进
- 未完成项: {pending_items}
- 下次复审: {follow_up_date}
```

## 执行约束

1. **无责文化**: 复盘目的是改进，不是追责
2. **事实驱动**: 所有结论基于证据，不推测
3. **系统视角**: 关注系统和流程问题，不聚焦个人
4. **可操作**: 每项改进必须有明确的执行人和验收标准
5. **知识沉淀**: 经验可复用于未来故障预防

## Task Description

> Describe the specific task for the review-incident scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for review-incident

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core review-incident activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality

## Output Format

> Standard output structure for review-incident deliverables


