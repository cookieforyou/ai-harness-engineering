---
name: audit-security
description: "audit security execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 安全审计场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行安全审计流程，包括资产识别、威胁分析、漏洞评估和安全建议生成。

## Execution Variables

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `audit_scope` | string | 是 | 审计范围 | "用户认证模块" |
| `audit_type` | enum | 是 | 审计类型 | FULL/SECURITY_ENHANCEMENT/COMPLIANCE/INCIDENT |
| `audit_target` | object | 是 | 审计目标详情 | 见 AuditTarget 结构 |
| `compliance_standards` | string[] | 否 | 合规标准列表 | ["ISO27001", "GDPR", "PCI-DSS"] |
| `critical_assets` | string[] | 是 | 关键资产列表 | ["用户数据库", "支付接口"] |
| `previous_audits` | string[] | 否 | 历史审计报告 | ["2023-Q1-Report.md"] |
| `known_vulnerabilities` | string[] | 否 | 已知漏洞列表 | ["CVE-2024-XXXX"] |
| `threat_intelligence` | object | 否 | 威胁情报 | 相关威胁信息 |
| `audit_team` | string[] | 是 | 审计团队成员 | ["安全工程师A", "安全工程师B"] |
| `audit_deadline` | datetime | 否 | 审计截止日期 | "2024-02-01" |

### AuditTarget 结构

```typescript
interface AuditTarget {
  system_name: string;           // 系统名称
  system_type: string;           // 系统类型 (Web/API/Mobile/Cloud/On-prem)
  architecture: string;          // 架构描述
  tech_stack: string[];          // 技术栈
  exposure: 'INTERNAL' | 'EXTERNAL' | 'BOTH';
  data_classification: string;    // 数据分类等级
  user_count?: number;           // 用户数量
  endpoints: string[];           // API端点列表
}
```

## Chain of Thought

### Step 1: 资产识别与分析

```
识别资产类型:
1. 硬件资产
   - 服务器、网络设备
   - 终端设备
   - 云资源

2. 软件资产
   - 自研应用
   - 第三方组件
   - 开源库

3. 数据资产
   - 用户数据
   - 业务数据
   - 敏感配置

4. 接口资产
   - API接口
   - 第三方集成
   - 数据流
```

### Step 2: 威胁建模 (STRIDE/ATT&CK)

```
STRIDE 威胁分类:
- Spoofing (伪装): 身份冒充风险
- Tampering (篡改): 数据/代码篡改风险
- Repudiation (抵赖): 操作不可追溯风险
- Information Disclosure (信息泄露): 敏感信息暴露风险
- Denial of Service (拒绝服务): 服务可用性风险
- Elevation of Privilege (权限提升): 越权访问风险

ATT&CK 矩阵映射:
- 识别相关攻击技术
- 评估防御覆盖度
```

### Step 3: 漏洞评估 (CVSS)

```
CVSS 评分维度:
1. 基本度量 (Base)
   - 攻击向量 (AV)
   - 攻击复杂度 (AC)
   - 所需权限 (PR)
   - 用户交互 (UI)
   - 影响范围 (S)
   - 机密性影响 (C)
   - 完整性影响 (I)
   - 可用性影响 (A)

2. 时序度量 (Temporal)
   - 利用代码成熟度
   - 修复级别
   - 报告可信度

3. 环境度量 (Environmental)
   - 资产价值
   - 业务影响
```

### Step 4: 风险计算

```
风险等级 = 漏洞严重性 × 资产重要性 × 利用可能性

风险矩阵:
| 可能性 \ 影响 | LOW | MEDIUM | HIGH |
|---------------|-----|--------|------|
| LOW           | 低  | 低     | 中   |
| MEDIUM        | 低  | 中     | 高   |
| HIGH          | 中  | 高     | 极高 |
```

### Step 5: 合规检查

```
检查维度:
1. 访问控制 (ISO27001 A.9)
2. 加密要求 (数据传输/存储)
3. 审计日志 (操作记录)
4. 数据保护 (隐私合规)
5. 第三方安全 (供应商管理)
```

## Error Handling

### 识别信号

| 信号类型 | 检测条件 | 优先级 |
|----------|----------|--------|
| 严重漏洞发现 | CVSS ≥ 9.0 | CRITICAL |
| 合规项不达标 | 关键控制项缺失 | CRITICAL |
| 证据不足 | 无法验证安全控制 | HIGH |
| 范围蔓延 | 超出初始审计范围 | MEDIUM |
| 情报冲突 | 与已知威胁情报不一致 | HIGH |

### 处理方式

1. **严重漏洞发现**
   - 立即标记为 CRITICAL
   - 生成紧急修复建议
   - 建议隔离或缓解措施
   - 通知安全事件响应团队

2. **合规项不达标**
   - 详细列出不合规项
   - 提供合规差距分析
   - 制定整改计划

3. **证据不足**
   - 要求补充证据
   - 提供证据收集指南
   - 标注为待验证项

### 升级条件

```
CRITICAL 升级条件:
- 发现 RCE (远程代码执行) 漏洞
- 发现大规模数据泄露风险
- 发现关键合规项严重缺失
- 发现活跃攻击痕迹

HIGH 升级条件:
- 高危漏洞数量 > 5
- 核心资产无安全防护
- 审计范围存在重大遗漏
```

## Output Validation

### 必须包含的字段

- [ ] `audit_id`: 审计唯一标识符
- [ ] `scope_definition`: 审计范围定义
- [ ] `asset_inventory`: 资产清单
- [ ] `threat_model`: 威胁模型
- [ ] `vulnerability_list`: 漏洞列表 (含 CVSS 评分)
- [ ] `risk_assessment`: 风险评估结果
- [ ] `compliance_matrix`: 合规检查矩阵
- [ ] `remediation_plan`: 修复计划
- [ ] `executive_summary`: 执行摘要

### 漏洞格式

```typescript
interface Vulnerability {
  vuln_id: string;                    // 漏洞编号 (VULN-YYYY-NNN)
  title: string;                       // 漏洞标题
  description: string;                 // 详细描述
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'INFO';
  cvss_score: number;                  // CVSS 评分 (0-10)
  cvss_vector: string;                 // CVSS 向量
  affected_components: string[];       // 受影响组件
  evidence: string[];                 // 证据
  impact: string;                      // 影响分析
  poc: string;                         // 验证方法
  remediation: string;                 // 修复建议
  priority: number;                    // 修复优先级 (1-5)
  deadline?: string;                   // 建议修复期限
}
```

### Quality Standards

| 检查项 | 标准 |
|--------|------|
| 漏洞识别覆盖率 | ≥ 95% (OWASP Top 10) |
| CVSS 评分准确性 | ≥ 90% |
| 修复建议可行性 | 100% |
| 合规检查完整性 | 100% |



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

```markdown
## Security Audit Handover Context

### 审计基础信息
- 审计ID: {audit_id}
- 审计范围: {audit_scope}
- 审计类型: {audit_type}
- 完成时间: {completion_time}

### 漏洞统计
- 总计: {total_vulnerabilities}
  - CRITICAL: {critical_count} (需立即修复)
  - HIGH: {high_count} (优先修复)
  - MEDIUM: {medium_count}
  - LOW: {low_count}

### 风险评估
- 极高风险: {critical_risk_count}
- 高风险: {high_risk_count}
- 中风险: {medium_risk_count}
- 低风险: {low_risk_count}

### 合规状态
- 通过项: {passed_controls}
- 不通过项: {failed_controls}
- 待验证项: {pending_controls}

### Next Steps行动
- 紧急修复: {urgent_remediation}
- 整改计划: {remediation_plan}
- 复审时间: {follow_up_date}
```

## Execution Constraints

1. **客观独立**: 不受业务压力影响，基于事实评估
2. **证据驱动**: 所有结论必须有充分证据支持
3. **保密性**: 审计结果严格保密
4. **全面性**: 不遗漏任何潜在风险点
5. **实用性**: 修复建议必须可执行、可验证

## Task Description

> Describe the specific task for the audit-security scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for audit-security

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core audit-security activities
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
## Security Audit Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]
- Risk Level: [critical | high | medium | low]

### Key Outputs
1. **Audit Report**: Comprehensive security audit findings with evidence
2. **Finding Register**: List of issues with severity, evidence, and remediation recommendations
3. **Compliance Matrix**: Mapping against target frameworks (ISO27001, SOC2, etc.)
4. **Remediation Plan**: Prioritized action items with timelines and owners
5. **Risk Register**: Security risk assessment summary

### Validation Checklist
- [ ] All critical and high findings have remediation plans
- [ ] Compliance coverage meets target framework requirements
- [ ] Audit trail is complete and tamper-evident
- [ ] Risk ratings are justified with evidence

### Next Steps
- [ ] Present findings to security committee
- [ ] Track remediation progress
```

