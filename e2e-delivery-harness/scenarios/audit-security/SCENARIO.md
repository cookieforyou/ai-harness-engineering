---
name: audit-security
description: "Audit Security scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['workflow', 'process']
---
# Security Audit Scenario

## Purpose

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

执行安全审计，发现安全漏洞和风险，验证安全控制的有效性，确保系统符合安全要求。

### Step-by-Step Reasoning

**Step 1: 范围确定**
- 问：哪些部分需要审计？
- 验证：识别资产清单
- 检查：是否有遗漏

**Step 2: 攻击面识别**
- 问：有哪些可能的攻击向量？
- 验证：检查接口、入口
- 检查：信任边界

**Step 3: 测试执行**
- 问：需要执行哪些测试？
- 验证：OWASP Top 10
- 检查：业务逻辑漏洞

**Step 4: 漏洞分析**
- 问：漏洞的严重程度？
- 验证：CVSS 评分
- 检查：利用难度

**Step 5: 风险评估**
- 问：漏洞的实际风险？
- 验证：结合业务场景
- 检查：数据敏感性

## Error Handling

### EH-1: 发现高危漏洞

- **识别信号**：发现高危或严重漏洞
- **处理方式**：
  1. 立即停止测试
  2. 通知安全团队
  3. 制定紧急修复计划
- **升级条件**：必须立即处理

### EH-2: 测试环境异常

- **识别信号**：测试环境无法正常使用
- **处理方式**：
  1. 确认环境状态
  2. 准备测试数据
  3. 调整测试策略
- **升级条件**：影响审计进度

### EH-3: 误报处理

- **识别信号**：测试结果可能为误报
- **处理方式**：
  1. 人工验证结果
  2. 复现漏洞场景
  3. 确认漏洞真实性
- **升级条件**：确认误报

### 产出清单

1. **安全审计报告**：完整的审计结果
2. **漏洞列表**：发现的安全漏洞
3. **风险评估**：漏洞风险等级
4. **修复建议**：漏洞修复方案

### 输出格式

```markdown
### 1. 审计概述
- 审计范围：
- 审计时间：
- 审计方法：

### 2. 发现的漏洞

| 漏洞ID | 漏洞名称 | 严重程度 | 漏洞类型 | 状态 |
|--------|----------|----------|----------|------|
| | | | | |

### 3. 风险评估
...

### 4. 修复建议
...

### 5. 安全建议
...
```

## Prerequisites

### 必需前置条件

1. 测试环境可用
2. 系统文档可用
3. 安全基线已定义

### 可选前置条件

1. 渗透测试授权
2. 安全测试工具
3. 历史漏洞数据

### 阶段准入

- [ ] 审计范围已确定
- [ ] 测试环境可用
- [ ] 测试工具就绪

### 阶段准出

- [ ] 审计覆盖所有范围
- [ ] 漏洞列表完整
- [ ] 修复建议可行

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 审计范围 | 启动审计前 | 全量 / 增量 / 专项 | 风险与合规要求 | 审计计划 |
| DC-002 | 发现分级 | 发现漏洞后 | Critical 立即修复 / 计划修复 | CVSS + 业务影响 | 审计报告 |
| DC-003 | 准出决策 | 整改完成后 | 通过 / 有条件通过 / 不通过 | 整改率与残留风险 | 准出签字 |

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

## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `FINDING-COVERAGE` | ≥95% | 发现覆盖率：检查项全部执行 |
| `REMEDIATION-SLA` | ≤30d | 整改SLA：高危问题修复时间 |
| `COMPLIANCE-SCORE` | ≥95% | 合规得分：框架要求达标比例 |
| `FALSE-POSITIVE` | ≤10% | 误报率：误报数占总发现数比例 |
| `AUDIT-COMPLETENESS` | 100% | 审计完整性：所有审计范围覆盖完毕 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 审计报告 | ☐ | 完整可追溯 |
| 漏洞清单 | ☐ | 含严重等级 |
| CVSS 评分 | ☐ | 每项有评分 |
| 修复计划 | ☐ | 含优先级 |

## Workflow

```
1. 确定审计范围
2. 收集系统信息
3. 识别攻击面
4. 执行安全测试
5. 分析漏洞
6. 评估风险
7. 编写报告
```

## Related Scenarios

- **Related**: [../verify-test/](../verify-test/) - 测试验证
- **Related**: [../deploy-release/](../deploy-release/) - 部署发布

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "audit-security"
    to_stage: "deploy-release"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
