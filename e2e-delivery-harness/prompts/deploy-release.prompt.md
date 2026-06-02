---
name: deploy-release
description: "部署发布提示词，用于规划和执行应用部署"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, deployment, release]
---
# Deploy Release Prompt

## Purpose

本提示词指导AI执行部署发布任务，将测试通过的软件安全、可靠地部署到目标环境，执行发布流程，确保部署成功并建立完善的监控和回滚机制。

### Key Objectives

- **安全可靠部署**: 通过标准化流程和自动化脚本，确保部署过程可控、可追溯
- **最小化停机时间**: 采用蓝绿/滚动/灰度等先进部署策略，实现零停机或最短停机
- **完善回滚机制**: 准备详细的回滚方案，确保在异常情况下能快速恢复到稳定状态
- **全面验证确认**: 执行功能、性能、集成、数据等多维度验证，确保部署质量
- **持续监控告警**: 配置完善的监控和告警规则，及时发现和处理问题

## Input Variables

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `release_version` | string | true | 发布版本号 | 语义化版本格式（如v1.2.3） |
| `release_scope` | markdown | true | 发布范围说明 | 包含变更清单、新功能、Bug修复 |
| `target_environment` | string | true | 目标环境 | prod/staging/dev，必须明确指定 |
| `rollback_plan` | markdown | true | 回滚方案 | 包含详细步骤、预计时间、验证方法 |
| `deployment_config` | yaml | true | 部署配置 | 有效的YAML配置，包含所有必需参数 |
| `health_check_url` | string | false | "" | 健康检查URL | 有效的URL，返回200表示健康 |
| `smoke_tests` | array | false | [] | 冒烟测试用例 | 测试脚本路径列表 |
| `deployment_strategy` | string | false | "rolling" | 部署策略 | blue-green/rolling/canary/direct |
| `maintenance_window` | object | false | {} | 维护窗口 | 开始时间、结束时间、通知对象 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 确认发布范围和计划
   ├─ 输入: release_version, target_environment, release_scope
   ├─ 思考: 发布范围是什么？是否有回滚计划？是否获得发布授权？
   ├─ 验证: 检查测试报告、审批记录、回滚方案
   └─ 输出: 发布确认清单（含版本号、变更清单、目标环境、时间窗口）
   ↓
[ANALYZE] Step 2: 分析部署环境和依赖
   ├─ 输入: 发布确认清单, deployment_config
   ├─ 思考: 目标环境是否就绪？依赖服务是否正常？资源配置充足吗？
   ├─ 验证: 环境检查、资源评估、依赖服务健康状态
   └─ 输出: 环境准备报告（含服务器、网络、数据库、缓存等检查结果）
   ↓
[DESIGN] Step 3: 设计部署流程和监控方案
   ├─ 输入: 环境准备报告, deployment_strategy
   ├─ 思考: 采用什么部署策略（蓝绿/滚动/灰度）？如何监控？告警阈值是多少？
   ├─ 验证: 部署流程清晰，监控指标明确，告警规则合理
   └─ 输出: 部署执行计划（含部署步骤、验证点、回滚触发条件、监控面板）
   ↓
[IMPLEMENT] Step 4: 执行部署操作
   ├─ 输入: 部署执行计划, release_package
   ├─ 思考: 按步骤执行，实时监控状态，有异常吗？
   ├─ 验证: 每个步骤执行成功，无异常告警，健康检查通过
   └─ 输出: 部署执行日志（含每步执行结果、时间戳、状态）
   ↓
[VERIFY] Step 5: 验证部署结果
   ├─ 输入: 部署执行日志, health_check_url, smoke_tests
   ├─ 执行: 功能验证、性能验证、集成验证、数据验证
   ├─ 验证: 所有验证通过，监控指标正常，用户体验良好
   └─ 输出: 部署验证报告（含验证结果、性能指标、问题清单）
   ↓
[HANDOVER] Step 6: 准备交接给运维监控阶段
   ├─ 生成: Handover Context（含部署统计、监控配置、遗留问题、建议）
   ├─ 更新: Global Context（发布状态、监控重点、应急联系人）
   └─ 通知: Monitor Operate Agent（开始持续监控）
```

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 部署失败 (P0)

**识别信号**: 
- 部署脚本执行失败
- 服务启动失败
- 健康检查不通过
- 关键依赖缺失或配置错误

**处理流程**:
```
IF 部署过程出现错误导致部署失败
THEN
  1. 立即停止部署流程
  2. 分析错误原因（查看日志、监控、事件记录）
  3. IF 错误可快速修复（<5分钟） THEN
       a. 尝试修复并重试部署
       b. 最多重试2次
     ELSE
       a. 立即执行回滚操作
       b. 恢复到上一个稳定版本
       c. 验证回滚后系统正常
     END
  4. 记录详细的失败原因和处理过程
  5. 升级到技术负责人和运维团队
  6. 标记发布为 [失败-已回滚]
END
```

**降级方案**: 回滚到上一稳定版本，保证服务可用性

**升级条件**: 部署失败且无法快速恢复，或回滚操作也失败

---

### Error Scenario 2: 部署后验证不通过 (P1)

**识别信号**: 
- 功能测试失败
- 性能指标异常（响应时间>阈值、错误率>阈值）
- 健康检查端点返回非200状态
- 用户反馈问题或投诉

**处理流程**:
```
IF 部署后功能验证失败
THEN
  1. 快速定位问题原因和影响范围
  2. 评估问题的严重程度（P0/P1/P2）
  3. IF 问题为P0级别（核心功能异常） THEN
       a. 立即执行回滚
       b. 通知相关干系人（产品、运营、客服）
     ELSE IF 问题为P1级别 THEN
       a. 评估修复时间
       b. IF 可在15分钟内修复 THEN 尝试热修复
       c. ELSE 执行回滚
     ELSE
       a. 记录问题并持续监控
       b. 计划在下一个补丁版本修复
     END
  4. 更新部署状态和问题跟踪
END
```

**降级方案**: 根据问题严重程度决定回滚或热修复

**升级条件**: 核心功能异常或SLA面临违约风险

---

### Error Scenario 3: 性能下降 (P1/P2)

**识别信号**: 
- 响应时间显著增加（>基线30%）
- 吞吐量下降
- 资源利用率异常（CPU>80%、内存>90%）
- 数据库慢查询增多

**处理流程**:
```
IF 部署后性能指标异常
THEN
  1. 对比部署前后的性能基线
  2. 识别性能瓶颈（应用层、数据库、网络、缓存等）
  3. 评估性能下降对业务的影响
  4. IF 性能下降严重影响业务（>30%） THEN
       a. 考虑回滚或紧急优化
       b. 扩容资源作为临时方案
     ELSE
       a. 持续监控性能趋势
       b. 计划在后续版本优化
     END
  5. 记录性能数据和优化建议
END
```

**降级方案**: 临时扩容资源，承诺后续优化

**升级条件**: 性能下降超过30%或SLA面临违约风险

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 部署前检查
- [ ] 部署包校验通过（MD5/SHA256签名验证）
- [ ] 目标环境就绪（服务器、网络、依赖服务）
- [ ] 回滚方案可用（已测试验证）
- [ ] 部署团队就位（开发、运维、DBA）
- [ ] 监控告警已配置

### V-002: 部署过程检查
- [ ] 每步部署执行记录完整（时间戳、状态、日志）
- [ ] 健康检查全部通过（所有端点返回200）
- [ ] 异常情况已记录并处理
- [ ] 回滚触发条件正确设置

### V-003: 部署后检查
- [ ] 所有副本运行正常（实例数符合预期）
- [ ] 健康检查100%通过
- [ ] 核心功能验证通过（冒烟测试通过）
- [ ] 性能指标正常（响应时间、吞吐量、错误率在基线范围内）
- [ ] 监控告警正常工作

### V-004: 验证完成标准
- [ ] 服务状态: Healthy
- [ ] 错误率: < 0.1%
- [ ] 响应时间: < SLA要求
- [ ] 无新增告警
- [ ] 用户反馈正常

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
- 补救措施: [如有]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 评估是否可以自动恢复
  3. 超过阈值时执行回滚
  4. 记录失败原因和恢复过程
  5. 通知相关干系人
END
```

## Output Format

```markdown
## Deployment & Release Deliverables

### Summary
- Status: [success/partial/failed_rolled_back]
- Completion: [percentage]%
- Deployment Strategy: [blue-green/rolling/canary/direct]
- Deployment Duration: [duration]
- Downtime: [duration_or_zero]

### Key Outputs
1. **Deployment Log**: Execution log with status for each step
   - Total Steps: {number}
   - Successful Steps: {number}
   - Failed Steps: {number}
   - Rollback Triggered: [true/false]

2. **Health Check Results**: Validation of all health endpoints
   - Endpoints Checked: {number}
   - Passed: {number}
   - Failed: {number}
   - Details: [{endpoint_url: status_code, response_time}]

3. **Verification Report**: Post-deployment validation results
   - Functional Tests: {passed}/{total}
   - Performance Tests: {passed}/{total}
   - Integration Tests: {passed}/{total}
   - Data Validation: {passed}/{total}

4. **Monitoring Dashboard**: Links to real-time metrics and alerts
   - Dashboard URL: {url}
   - Key Metrics: [response_time, error_rate, cpu_usage, memory_usage]
   - Alert Rules Configured: {number}

5. **Rollback Status**: Confirmation of rollback readiness
   - Rollback Plan Tested: [true/false]
   - Estimated Rollback Time: {minutes}
   - Last Stable Version: {version}

### Validation Checklist
- [ ] Deployment success rate target is met (≥99%)
- [ ] Rollback capability is verified and ready (≤15min)
- [ ] Zero-downtime achieved for user-facing services (100%)
- [ ] All health checks pass post-deployment (100%)
- [ ] Performance metrics within baseline (±10%)

### Next Steps
- [ ] Monitor deployment metrics for stability period (24 hours)
- [ ] Conduct post-deployment review
- [ ] Update deployment documentation
- [ ] Archive deployment records
```

## Handover Context Template

```yaml
handover:
  header:
    from_stage: "deployment"
    to_stage: "monitoring-operations"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "success/partial/failed_rolled_back"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    deployment_duration: "{{duration}}"
    downtime: "{{duration_or_zero}}"
    deployment_strategy: "blue-green/rolling/canary/direct"
    
  artifacts:
    delivered:
      - name: "Release Package"
        path: "registry/releases/{version}"
        version: "{release_version}"
        checksum: "{{SHA256}}"
      - name: "Deployment Scripts"
        path: "deploy/scripts/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Deployment Log"
        path: "logs/deployment-log.md"
        version: "1.0.0"
      - name: "Rollback Plan"
        path: "docs/rollback-plan.md"
        version: "1.0.0"
      - name: "Release Report"
        path: "docs/release-report.md"
        version: "1.0.0"
      - name: "Monitoring Configuration"
        path: "monitoring/alerts.yaml"
        version: "1.0.0"
      - name: "Verification Report"
        path: "reports/verification-report.md"
        version: "1.0.0"
      
  decisions:
    - id: "DC-002"
      description: "部署策略选择"
      rationale: "选择蓝绿部署以最小化停机时间"
      alternatives_considered: ["滚动部署", "灰度发布"]
      criteria_used: "业务连续性要求高，基础设施支持蓝绿部署"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "非核心功能X存在小问题，计划下版本修复"
        severity: "P3"
        planned_fix: "v1.1.0"
        
  risks:
    - id: "RISK-001"
      description: "新版本依赖的中间件版本较新，需密切监控"
      probability: "low"
      impact: "medium"
      affected_areas: ["缓存服务", "消息队列"]
      mitigation: "已在测试环境充分验证，生产环境加强监控"
      contingency_plan: "如出现问题，立即回滚到上一版本"
      
  recommendations:
    - "前24小时密切监控错误率和响应时间"
    - "关注数据库性能，必要时优化慢查询"
    - "准备好热修复方案应对紧急情况"
    - "建议在下次迭代中优化启动时间（当前>30秒）"
    - "建议增加自动化冒烟测试，减少人工验证工作量"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "DEPLOY-SUCCESS-RATE"
        value: 100
        target: 99
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "ROLLBACK-TIME"
        value: 8
        target: 15
        unit: "minutes"
        status: "pass"
        note: "回滚演练时间，实际未触发回滚"
      - kpi_id: "KPI-003"
        name: "ZERO-DOWNTIME"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "POST-DEPLOY-VERIFICATION"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
    overall_score: 100
    grade: "excellent"
    recommendation: "approved_for_production"
      
  next_steps:
    immediate:
      - "Monitor Operate Agent开始持续监控（至少24小时）"
      - "重点关注错误率、响应时间、资源使用率"
      - "设置告警通知渠道（Slack、邮件、短信）"
    short_term:
      - "24小时后编写部署回顾报告"
      - "收集团队反馈，优化部署流程"
      - "更新部署文档和最佳实践"
    long_term:
      - "分析部署数据，识别改进机会"
      - "探索更先进的部署策略（如GitOps、渐进式交付）"
      - "提升自动化水平，减少人工干预"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../../scenarios/deploy-release/SCENARIO.md` | 部署发布场景定义 |
| Agent | `../../agents/deploy-release.agent.md` | 部署发布Agent角色定义 |
| Skill | `../../skills/deploy-release/SKILL.md` | 部署发布技能包 |
| Instruction | `../../instructions/deploy-release.instructions.md` | 部署发布技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Deployment Best Practices](../standards/deployment-best-practices.md) - 部署最佳实践指南
  - [Rollback Strategy](../standards/rollback-strategy.md) - 回滚策略标准
  - [Health Check Guidelines](../standards/health-check-guidelines.md) - 健康检查指南
- **Templates**: 
  - [Deployment Plan Template](../templates/deployment-plan.template.md) - 部署计划模板
  - [Rollback Plan Template](../templates/rollback-plan.template.md) - 回滚方案模板
  - [Release Report Template](../templates/release-report.template.md) - 发布报告模板
- **Evaluations**: 
  - [Deployment Quality Checklist](../evaluations/deployment-quality-checklist.md) - 部署质量检查清单
  - [Rollback Drill Report](../evaluations/rollback-drill-report.md) - 回滚演练报告

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "deployment"
    to_stage: "operations"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "deploy-release"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
