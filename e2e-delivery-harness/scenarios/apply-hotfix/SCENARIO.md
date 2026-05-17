---
name: apply-hotfix
description: "紧急修复场景，负责生产环境P0/P1级别缺陷的快速定位、修复和上线"
version: "1.2.0"
type: scenario
category: emergency-response
stage: incident-resolution
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [hotfix, emergency, incident, rapid-response]
---
# Hotfix Scenario (紧急修复场景)

## Purpose

在生产环境发生P0/P1级别严重故障时，快速响应、定位根因、执行最小化修复并验证上线，最大限度减少业务影响和用户损失。

### Business Value

- **保障业务连续性**: 通过快速应急响应，将核心服务中断时间降至最低（P0≤2h，P1≤8h）
- **降低用户影响**: 快速恢复受影响功能，减少用户投诉和业务损失
- **控制风险扩散**: 最小化修复范围，避免引入新问题，确保修复可回滚
- **提升团队应急能力**: 建立标准化应急响应流程，提高团队处理突发事件的效率
- **持续改进机制**: 通过事后复盘，识别系统性问题，预防同类故障再次发生

## Chain of Thought (思维链)

### Think-Aloud Protocol (强制遵循)

```
[ASSESS] Step 1: 评估问题严重性和影响范围
   ├─ 问：问题的严重程度是什么？影响了多少用户？哪些核心功能受损？
   ├─ 验证：确认问题级别（P0/P1/P2），评估业务影响
   └─ 检查：启动相应级别的应急响应流程
   ↓
[LOCATE] Step 2: 快速定位问题根因
   ├─ 问：问题出在哪里？最近的变更有哪些？日志显示什么异常？
   ├─ 验证：分析日志、监控数据、最近代码变更
   └─ 检查：使用5 Whys方法深入分析，30分钟内定位根因
   ↓
[DESIGN] Step 3: 设计最小化修复方案
   ├─ 问：如何用最少的代码改动修复问题？有无临时止血方案？修复是否可回滚？
   ├─ 验证：方案只修改必要部分，不影响其他功能
   └─ 检查：准备回滚方案，评估修复风险
   ↓
[IMPLEMENT] Step 4: 执行修复和测试
   ├─ 问：修复代码是否正确？测试是否覆盖关键场景？有无引入新问题？
   ├─ 验证：代码审查通过，单元测试和回归测试通过
   └─ 检查：在预发环境验证修复效果
   ↓
[DEPLOY] Step 5: 部署上线和监控
   ├─ 问：部署是否顺利？修复是否生效？系统是否稳定？
   ├─ 验证：灰度发布或全量发布，监控系统指标
   └─ 检查：观察30分钟以上，确认无异常后宣布修复完成
   ↓
[REPORT] Step 6: 产出修复报告和后续计划
   ├─ 生成：紧急修复报告（含问题描述、根因、修复方案、验证结果）
   ├─ 更新：Global Context（故障状态、修复记录、遗留问题）
   └─ 交接：安排正式修复计划（如需长期解决方案）
```

## Decision Checkpoints (决策检查点)

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 问题级别判定 | 收到问题报告时 | P0(立即)/P1(15min)/P2(1h) | 影响范围、业务价值、用户数量 | 故障报告 |
| DC-002 | 根因定位策略 | 30分钟未定位时 | 继续排查/临时止血/升级专家 | 问题复杂度、时间压力、可用资源 | 排查记录 |
| DC-003 | 修复方案选择 | 设计修复方案时 | 直接修复/临时止血/回滚版本 | 修复难度、风险评估、时间要求 | 修复方案文档 |
| DC-004 | 测试范围确定 | 修复完成后 | 最小测试/标准测试/完整回归 | 修复影响范围、风险等级、时间允许 | 测试计划 |
| DC-005 | 发布策略选择 | 准备上线时 | 灰度发布/全量发布/紧急回滚 | 修复稳定性、影响范围、业务时段 | 发布计划 |
| DC-006 | 是否需要正式修复 | 修复上线后 | 需要/不需要 | 临时方案还是永久方案、技术债务 | 后续计划 |

## Error Scenarios (错误场景)

### Error Scenario 1: 根因不明 (P1)

**识别信号**: 
- 30分钟内无法定位问题根因
- 日志信息不足或模糊
- 问题无法稳定复现
- 多个疑似原因但无法确认

**处理流程**:
```
IF 30分钟内无法定位根因
THEN
  1. 扩大日志收集范围（增加调试日志、启用详细追踪）
  2. 排查最近24小时内的所有变更（代码、配置、基础设施）
  3. 尝试临时止血方案（功能开关、限流降级、回滚版本）
  4. 升级到专家团队（架构师、资深开发、DBA）
  5. 组织战时会议，集体排查
  6. 记录所有排查步骤和假设
END
```

**降级方案**: 实施临时止血措施（回滚、降级、限流），优先恢复服务

**升级条件**: 60分钟仍无法定位，或影响超过50%用户

### Error Scenario 2: 修复失败 (P1)

**识别信号**: 
- 修复后问题仍然存在
- 修复引入了新的问题
- 测试通过但生产环境仍失败
- 多次修复尝试均无效

**处理流程**:
```
IF 修复失败
THEN
  1. 立即回滚修复（恢复到修复前状态）
  2. 重新分析问题根因（是否有误判）
  3. 收集更多证据（生产日志、用户反馈、监控数据）
  4. 制定新的修复方案（考虑不同 approach）
  5. 在小范围环境验证新方案
  6. 必要时寻求外部支持（社区、供应商、专家）
END
```

**降级方案**: 保持回滚状态，使用临时方案维持服务

**升级条件**: 3次修复尝试均失败，或问题持续恶化

### Error Scenario 3: 修复引发回归 (P0)

**识别信号**: 
- 修复后其他功能出现异常
- 回归测试发现新问题
- 用户报告新的故障
- 监控指标异常波动

**处理流程**:
```
IF 检测到回归问题
THEN
  1. 立即评估回归问题的严重程度
  2. IF 回归问题≥原问题 THEN 立即回滚全部修复
  3. IF 回归问题<原问题 THEN 评估是否接受权衡
  4. 分析回归原因（依赖关系、边界条件、副作用）
  5. 制定修复回归的方案
  6. 扩大测试范围，确保无其他回归
END
```

**降级方案**: 回滚到修复前状态，重新评估修复方案

**升级条件**: 回归问题影响核心功能或超过原问题影响

### Error Scenario 4: 部署失败 (P0)

**识别信号**: 
- 部署过程中出现错误
- 部署后服务无法启动
- 健康检查失败
- 关键指标异常

**处理流程**:
```
IF 部署失败
THEN
  1. 立即停止部署流程
  2. 自动或手动回滚到上一版本
  3. 验证回滚后系统恢复正常
  4. 分析部署失败原因（配置错误、依赖缺失、兼容性问题）
  5. 修复部署问题（修正配置、补充依赖）
  6. 在预发环境重新验证部署流程
  7. 重新执行部署
END
```

**降级方案**: 保持旧版本运行，寻找其他修复途径

**升级条件**: 多次部署失败，或无法回滚

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | HOTFIX-TIME-P0 | ≤2h | P0问题从发现到修复上线的时间 | 故障时间线统计 | 30% |
| KPI-002 | HOTFIX-TIME-P1 | ≤8h | P1问题从发现到修复上线的时间 | 故障时间线统计 | 25% |
| KPI-003 | REGRESSION-RATE | ≤5% | (修复引入新问题数/总修复数) × 100% | 回归测试统计 | 25% |
| KPI-004 | VERIFY-COVERAGE | 100% | 关键场景回归测试覆盖率 | 测试覆盖率报告 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001得分 × 0.30) + (KPI-002得分 × 0.25) + (KPI-003得分 × 0.25) + (KPI-004得分 × 0.20)

KPI得分计算:
- HOTFIX-TIME-P0: ≤2h=100分, 2-4h=80分, 4-6h=60分, >6h=0分
- HOTFIX-TIME-P1: ≤8h=100分, 8-12h=80分, 12-24h=60分, >24h=0分
- REGRESSION-RATE: ≤5%=100分, 5-10%=80分, 10-15%=60分, >15%=0分
- VERIFY-COVERAGE: 100%=100分, 90-99%=80分, 80-89%=60分, <80%=0分

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 修复代码 | ☐ | 已测试通过，代码审查完成 |
| 验证报告 | ☐ | 修复有效，回归测试通过 |
| 回滚方案 | ☐ | 已准备并可执行 |
| 变更记录 | ☐ | 已记录到变更管理系统 |
| 监控配置 | ☐ | 已配置修复后的专项监控 |
| 后续计划 | ☐ | 正式修复计划已制定（如需要） |

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/apply-hotfix.agent.md` | 紧急修复Agent角色定义 |
| Prompt | `../../prompts/apply-hotfix.prompt.md` | 紧急修复提示词模板 |
| Skill | `../../skills/apply-hotfix/SKILL.md` | 紧急修复技能包 |
| Instruction | `../../instructions/apply-hotfix.instructions.md` | 紧急修复技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Incident Management](../standards/incident-management.md) - 事件管理标准
  - [Emergency Response](../standards/emergency-response.md) - 应急响应标准
  - [Change Management](../standards/change-management.md) - 变更管理标准
  - [Rollback Procedures](../standards/rollback-procedures.md) - 回滚流程标准
- **Templates**: 
  - [Incident Report Template](../templates/incident-report.template.md) - 故障报告模板
  - [Hotfix Checklist](../templates/hotfix-checklist.template.md) - 热修复检查清单
  - [Post-Mortem Template](../templates/post-mortem.template.md) - 事故复盘模板
  - [Communication Template](../templates/communication.template.md) - 沟通通知模板
- **Evaluations**: 
  - [Hotfix Quality Checklist](../evaluations/hotfix-quality-checklist.md) - 热修复质量检查清单
  - [Regression Test Suite](../evaluations/regression-test-suite.md) - 回归测试套件
  - [Response Time Analysis](../evaluations/response-time-analysis.md) - 响应时间分析
