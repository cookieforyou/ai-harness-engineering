---
name: audit-security
description: audit security execution prompt for E2E delivery workflow
type: execution
version: "1.1.0"
stage: audit-security
---

# Prompt: 安全审计场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行安全审计流程，包括资产识别、威胁分析、漏洞评估和安全建议生成。

## 执行变量 (Variables)

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

## 思维链 (Chain of Thought)

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

## 输出验证 (Output Validation)

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

### 质量标准

| 检查项 | 标准 |
|--------|------|
| 漏洞识别覆盖率 | ≥ 95% (OWASP Top 10) |
| CVSS 评分准确性 | ≥ 90% |
| 修复建议可行性 | 100% |
| 合规检查完整性 | 100% |

## 交接准备 (Handover Context)

```markdown
## 安全审计交接上下文

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

### 下一步行动
- 紧急修复: {urgent_remediation}
- 整改计划: {remediation_plan}
- 复审时间: {follow_up_date}
```

## 执行约束

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

## Output Format

> Standard output structure for audit-security deliverables


