---
name: audit-security
description: "audit security execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
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

## Chain of Thought (安全审计思维链)

> **AI 必须按照以下思维链逐步执行安全审计**，每完成一步后进行自我验证

### Step 1: 范围确定 (Scoping)

```
[THINK] 明确审计边界和目标
├─ 问：本次审计的范围是什么？包含哪些系统、模块、API？
├─ 收集：系统架构文档、资产清单、接口列表、数据流图
├─ 识别：关键资产（高价值数据、核心服务）、信任边界
├─ 验证：审计范围划分清晰，无重叠和遗漏
└─ 输出：审计计划书（范围、目标、方法、排期、人员）
```

### Step 2: 信息收集与侦察 (Reconnaissance)

```
[RECON] 收集目标系统信息，发现攻击面
├─ 被动侦察：
│  ├─ 查询域名信息和WHOIS记录
│  ├─ 收集子域名和DNS记录
│  ├─ 分析HTTP头和服务指纹
│  └─ 爬取公开信息（GitHub、文档、论坛）
│
├─ 主动侦察：
│  ├─ 端口扫描和服务探测 (Nmap)
│  ├─ 目录和文件枚举
│  ├─ 技术栈指纹识别 (Wappalyzer, WhatWeb)
│  └─ API端点发现和参数分析
│
├─ 攻击面分析：
│  ├─ 映射所有入口点和出口点
│  ├─ 识别第三方集成和依赖
│  ├─ 分析认证和授权机制
│  └─ 标记高风险区域
│
└─ 输出：信息收集报告（资产清单、攻击面地图、技术栈分析）
```

### Step 3: 威胁建模 (Threat Modeling)

```
[THREAT] 运用STRIDE方法论系统和全面地识别威胁
├─ 绘制数据流图 (DFD)：
│  ├─ 识别外部实体、数据存储、处理过程
│  └─ 标注数据流和信任边界
│
├─ STRIDE威胁分类分析：
│  ├─ Spoofing (伪装): 身份伪造、会话劫持、重放攻击
│  │  └─ 验证：认证机制是否完善？是否存在默认凭据？
│  ├─ Tampering (篡改): 数据篡改、参数污染、请求伪造
│  │  └─ 验证：数据完整性校验？签名校验？防篡改机制？
│  ├─ Repudiation (抵赖): 日志不完整、操作无追溯
│  │  └─ 验证：审计日志是否完整？是否防篡改？
│  ├─ Information Disclosure (泄露): 敏感数据泄漏
│  │  └─ 验证：传输加密？存储加密？最小数据暴露？
│  ├─ Denial of Service (拒绝服务): 资源耗尽
│  │  └─ 验证：限流措施？资源隔离？熔断机制？
│  └─ Elevation of Privilege (越权): 水平/垂直越权
│      └─ 验证：权限校验？RBAC/ABAC？最小权限？
│
├─ 风险优先级排序：
│  ├─ 按利用难度 × 资产价值 × 影响范围排序
│  └─ 标注需要优先测试的威胁
│
└─ 输出：威胁模型（DFD图、STRIDE威胁列表、优先级矩阵）
```

### Step 4: 漏洞扫描 (Vulnerability Scanning)

```
[SCAN] 执行多层次的漏洞扫描和自动化测试
├─ SAST (静态应用安全测试):
│  ├─ 执行源代码安全审计 (Semgrep/Checkmarx/Fortify)
│  ├─ 扫描安全编码规范违规（注入、XSS、硬编码密钥）
│  └─ 检查依赖库漏洞 (SCA - Snyk/Trivy/Dependency-Check)
│
├─ DAST (动态应用安全测试):
│  ├─ 执行OWASP ZAP/Burp Suite自动化扫描
│  ├─ 测试OWASP Top 10漏洞类别
│  │  ├─ A01: 访问控制失效 - IDOR测试、权限提升测试
│  │  ├─ A02: 加密失败 - TLS配置检查、敏感数据传输测试
│  │  ├─ A03: 注入 - SQL/NoSQL/OS命令/LDAP注入测试
│  │  ├─ A04: 不安全设计 - 设计缺陷分析
│  │  ├─ A05: 安全配置错误 - 默认配置、暴露管理端口
│  │  ├─ A06: 漏洞和过时组件 - 组件版本检查
│  │  ├─ A07: 认证和身份验证失败 - 暴力破解、会话管理
│  │  ├─ A08: 数据完整性失败 - 反序列化、签名校验
│  │  ├─ A09: 安全日志记录和监控失败 - 日志覆盖检查
│  │  └─ A10: SSRF - 服务器端请求伪造测试
│  └─ 测试业务逻辑漏洞（逻辑缺陷、流程绕过、竞争条件）
│
├─ 基础设施安全扫描:
│  ├─ 云安全配置审计 (ScoutSuite/Prowler)
│  ├─ 容器和K8s安全扫描 (Trivy/kube-bench)
│  ├─ 网络分段和防火墙规则检查
│  └─ 操作系统基线检查 (OpenSCAP/Lynis)
│
└─ 输出：自动化扫描结果（原始发现列表、漏洞分类统计）
```

### Step 5: 渗透测试与漏洞验证 (Exploitation Testing)

```
[EXPLOIT] 手动验证和深入测试已发现的潜在漏洞
├─ 漏洞验证：
│  ├─ 复现自动化扫描发现的可疑结果
│  ├─ 手工PoC（Proof of Concept）开发和执行
│  ├─ 验证漏洞的可利用性和影响范围
│  └─ 排除误报，确认真实漏洞
│
├─ 深入渗透测试：
│  ├─ SQL注入：时间盲注、联合查询、报错注入、带外注入
│  ├─ XSS：存储型、反射型、DOM型、基于Mutation观察者
│  ├─ CSRF：Token验证检查、SameSite Cookie配置
│  ├─ SSRF：内部服务探测、云元数据访问
│  ├─ 文件上传：类型绕过、路径穿越、WebShell上传
│  └─ 业务逻辑：越权操作、批量分配、参数篡改
│
├─ 后渗透验证：
│  ├─ 权限提升测试（低权限→高权限）
│  ├─ 横向移动测试（服务→服务）
│  ├─ 数据提取测试（敏感数据访问）
│  └─ 持久化机制测试（后门可能性）
│
└─ 输出：验证后的漏洞列表（含PoC、复现步骤、影响证明）
```

### Step 6: CVSS评分与风险评估

```
[SCORE] 使用CVSS 3.1标准对每个漏洞进行精确评分
├─ 基本度量 (Base Metrics):
│  ├─ AV (攻击向量): Network/Adjacent/Local/Physical
│  ├─ AC (攻击复杂度): Low/High
│  ├─ PR (所需权限): None/Low/High
│  ├─ UI (用户交互): None/Required
│  ├─ S (影响范围): Unchanged/Changed
│  ├─ C (机密性影响): None/Low/High
│  ├─ I (完整性影响): None/Low/High
│  └─ A (可用性影响): None/Low/High
│  └─ Base Score: [CVSS向量如 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H → 9.8]
│
├─ 环境度量 (Environmental Metrics):
│  ├─ 资产价值评估（关键/重要/一般）
│  ├─ 业务影响分析（数据泄露量、财务损失、监管处罚）
│  └─ 缓解措施可用性
│
├─ 风险等级判定:
│  ├─ Critical (9.0-10.0): 立即修复（24h内）
│  ├─ High (7.0-8.9): 优先修复（7天内）
│  ├─ Medium (4.0-6.9): 计划修复（30天内）
│  ├─ Low (0.1-3.9): 可选修复（下一迭代）
│  └─ Info (0): 信息性发现
│
└─ 输出：漏洞风险评估表（CVSS评分、向量、严重等级、业务影响）
```

### Step 7: 报告编写与输出 (Reporting)

```
[REPORT] 生成完整的安全审计报告
├─ 执行摘要：
│  ├─ 审计概述和时间范围
│  ├─ 总体风险评分和安全态势
│  ├─ 关键发现汇总（按严重等级统计）
│  └─ 核心建议和行动项
│
├─ 详细发现：
│  ├─ 每个漏洞的完整信息（ID、描述、CVSS、复现步骤、截图）
│  ├─ 按严重程度降序排列
│  ├─ 每个发现的修复建议和预计工时
│  └─ 参考标准（CWE、CVE、OWASP分类）
│
├─ 合规矩阵：
│  ├─ 对照合规框架的控制项映射
│  ├─ 达标/未达标状态
│  └─ 差距分析和整改建议
│
├─ 修复计划：
│  ├─ Critical/High漏洞的紧急修复行动项
│  ├─ Medium/Low漏洞的按计划修复安排
│  └─ 责任人和时间表
│
└─ 输出：安全审计报告.pdf/.md（完整文档，含所有章节）
```

## Domain-Specific Error Handling (领域错误处理)

> **AI 在安全审计过程中遇到以下领域特定情况时必须按指定流程处理**

### Error Scenario 1: 发现活跃利用痕迹 (P0)

**识别信号**:
- 日志中发现针对目标系统的实际攻击行为
- 检测到后门、WebShell、C2通信
- 发现异常提权或横向移动痕迹
- 敏感数据正在被未授权访问

**处理流程**:
```
IF 发现活跃利用痕迹
THEN
  1. 立即停止所有测试活动（不干扰攻击者）
  2. 记录发现的攻击痕迹和IoC（取证快照）
  3. 立即通知安全事件响应团队（IRT）
  4. 不得尝试与攻击者交互或阻断攻击
  5. 配合IRT进行应急响应
  6. 调整审计策略，转为事件响应支持模式
END
```

**降级方案**: 暂停所有主动测试，仅保留被动监控

**升级条件**: 任何活跃利用迹象必须立即升级

### Error Scenario 2: 高危漏洞导致测试风险 (P1)

**识别信号**:
- 测试中发现RCE漏洞，可能导致系统崩溃
- SQL注入命中生产数据库（非预期）
- 拒绝服务测试导致服务不稳定
- 文件上传测试成功写入可执行文件

**处理流程**:
```
IF 发现高危漏洞且测试存在风险
THEN
  1. 立即停止当前测试向量
  2. 评估已造成的实际影响
  3. 如已造成影响：立即通知系统管理员和业务方
  4. 记录详细的漏洞信息和测试步骤
  5. 制定安全的生产环境验证方案
  6. 在测试环境或隔离环境完成验证
  7. 根据结果调整后续测试策略
END
```

**降级方案**: 切换到低风险测试方法（被动分析、代码审查替代主动利用）

**升级条件**: 测试导致生产环境服务降级或数据受损

### Error Scenario 3: 范围蔓延 (P1)

**识别信号**:
- 审计过程中发现超出初始范围的高价值目标
- 测试路径引导到未授权的系统和数据
- 第三方系统或供应商系统被涉及
- 发现未在资产清单中的系统

**处理流程**:
```
IF 发现范围蔓延
THEN
  1. 立即停止超出范围的活动
  2. 记录发现的新资产和访问路径
  3. 评估新资产的风险等级
  4. IF 风险等级为Critical/High THEN 升级给审计负责人
  5. 等待范围变更确认后再继续
  6. 如范围变更获批，更新审计计划书
END
```

**降级方案**: 记录新发现但不测试，在报告中补充说明

**升级条件**: 新发现的系统涉及敏感数据或核心业务

### Error Scenario 4: 误报处理 (P2)

**识别信号**:
- 自动化扫描结果与系统实际行为不一致
- 复现测试无法稳定触发漏洞
- 漏洞表现不符合该类型漏洞的典型特征
- 安全控制（WAF/IPS）正确拦截了测试payload

**处理流程**:
```
IF 疑似误报
THEN
  1. 手动复现漏洞，至少尝试3次不同payload
  2. 分析系统实际响应和扫描工具判断逻辑
  3. 检查是否存在WAF/IPS等安全控制的干扰
  4. IF 确认误报 THEN 从发现清单中移除并标记
  5. IF 不确定 THEN 标注为"待人工确认"
  6. 记录误报排除的理由和证据
END
```

**降级方案**: 标注为待人工确认，不立即排除

**升级条件**: 误报影响审计结果判断，需要安全专家介入

### Error Scenario 5: 测试环境不可用 (P2)

**识别信号**:
- 目标系统无法访问或响应超时
- 测试账号/权限被撤销
- 测试数据被移除或修改
- 系统处于维护窗口或已下线

**处理流程**:
```
IF 测试环境不可用
THEN
  1. 确认环境状态（是否是预期维护）
  2. IF 临时不可用 THEN 调整测试顺序，先做其他模块
  3. IF 长期不可用 THEN 与系统负责人沟通获取ETA
  4. 切换到可用的备用环境
  5. 调整审计计划和排期
END
```

**降级方案**: 优先完成其他可用模块的审计，记录缺失的测试项

**升级条件**: 核心测试环境连续24小时不可用，影响审计进度

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



## Output Template: Security Audit Report (安全审计报告)

> 安全审计完成后，必须按以下模板生成完整的安全审计报告

```markdown
# Security Audit Report: {system_name}

## 1. 执行摘要 (Executive Summary)

### 审计概览
- **审计ID**: AUDIT-{YYYY}-{NNNN}
- **系统名称**: {system_name}
- **审计类型**: {FULL / SECURITY_ENHANCEMENT / COMPLIANCE / INCIDENT}
- **审计周期**: {start_date} → {end_date}
- **审计团队**: {team_members}
- **总体安全评分**: {score}/100

### 发现统计
| 严重等级 | 数量 | 占比 |
|----------|------|------|
| CRITICAL | {N} | {x%} |
| HIGH     | {N} | {x%} |
| MEDIUM   | {N} | {x%} |
| LOW      | {N} | {x%} |
| INFO     | {N} | {x%} |
| **总计** | {total} | 100% |

### 核心发现摘要
1. **{漏洞名称}** - CVSS {score} - {简短描述}
2. **{漏洞名称}** - CVSS {score} - {简短描述}
3. **{漏洞名称}** - CVSS {score} - {简短描述}

### 关键建议
1. 立即修复 {N} 个 Critical 级别漏洞
2. 在7天内修复 {N} 个 High 级别漏洞
3. {其他核心建议}

---

## 2. 审计范围 (Audit Scope)

### 审计目标
- **系统**: {system_name} (版本 {version})
- **技术栈**: {tech_stack}
- **部署环境**: {production/staging/development}
- **数据分类**: {data_classification}

### 在范围 (In Scope)
| 资产类型 | 资产名称 | 描述 |
|----------|----------|------|
| Web应用  | {name}   | {description} |
| API      | {name}   | {description} |
| 数据库   | {name}   | {description} |
| 基础设施 | {name}   | {description} |

### 不在范围 (Out of Scope)
- {资产名称} - {原因}
- {资产名称} - {原因}

---

## 3. 测试方法论 (Testing Methodology)

### 审计方法
- **方法**: {Black-box / White-box / Grey-box}
- **工具链**: 
  - SAST: {Semgrep / Checkmarx / SonarQube}
  - DAST: {OWASP ZAP / Burp Suite / Acunetix}
  - SCA: {Snyk / Trivy / Dependency-Check}
  - 基础设施: {Nmap / OpenSCAP / Prowler}
- **标准参考**: OWASP Top 10 (2021), CWE, CVSS 3.1

### 测试活动
| 活动 | 描述 | 覆盖范围 |
|------|------|----------|
| 威胁建模 | STRIDE方法论 | 所有核心功能 |
| SAST扫描 | 源代码安全审计 | {x} 个代码库 |
| DAST扫描 | 动态应用安全测试 | {x} 个端点 |
| SCA扫描 | 第三方组件分析 | {x} 个依赖 |
| 渗透测试 | 手动漏洞验证 | {x} 个关键场景 |
| 合规检查 | {框架} 控制项检查 | {x} 个控制项 |

---

## 4. 详细发现 (Detailed Findings)

### 4.1 CRITICAL 级别发现

#### {VULN-001}: {漏洞标题}
| 属性 | 值 |
|------|-----|
| **漏洞ID** | VULN-{YYYY}-{001} |
| **CWE** | CWE-{ID} |
| **CVSS 3.1** | {score} |
| **CVSS向量** | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H |
| **严重等级** | CRITICAL |
| **受影响组件** | {component} v{version} |
| **发现日期** | {date} |

**漏洞描述**:
{详细描述漏洞的行为和影响}

**复现步骤**:
1. {步骤1}
2. {步骤2}
3. {步骤3}

**PoC (Proof of Concept)**:
```bash
{poc_command_or_code}
```

**影响分析**:
{分析漏洞可能造成的实际影响，包括数据泄露、系统控制、业务中断等}

**修复建议**:
{具体的修复方案和最佳实践建议}

**参考链接**:
- {参考链接1}
- {参考链接2}

---

### 4.2 HIGH 级别发现

#### {VULN-002}: {漏洞标题}
{同上格式}

---

## 5. 风险评估 (Risk Assessment)

### 风险矩阵
| 风险ID | 漏洞ID | 漏洞名称 | 可能性 | 影响 | 风险等级 | 优先级 |
|--------|--------|----------|--------|------|----------|--------|
| RISK-001 | VULN-001 | {name} | High | Critical | Extreme | P0 |
| RISK-002 | VULN-002 | {name} | Medium | High | High | P1 |
| RISK-003 | VULN-003 | {name} | Low | Medium | Medium | P2 |

### 业务影响分析
- **受影响用户**: {用户数量或比例}
- **潜在数据泄露**: {数据类型和规模}
- **法规风险**: {违反的合规要求}
- **财务影响**: {预估损失}

---

## 6. 合规检查矩阵 (Compliance Matrix)

| 控制项ID | 控制要求 | 达标状态 | 证据 | 备注 |
|----------|----------|----------|------|------|
| {ISO-A.9.1.1} | {控制要求描述} | ✅/❌/⚠️ | {证据位置} | {备注} |
| {ISO-A.9.1.2} | {控制要求描述} | ✅/❌/⚠️ | {证据位置} | {备注} |

**达标率**: {pass_rate}% ({passed}/{total})

---

## 7. 修复计划 (Remediation Plan)

### 紧急修复 (24小时内)
| 优先级 | 漏洞ID | 漏洞名称 | 负责人 | 预计工时 |
|--------|--------|----------|--------|----------|
| P0 | VULN-001 | {name} | {owner} | {hours}h |

### 短期修复 (7天内)
| 优先级 | 漏洞ID | 漏洞名称 | 负责人 | 预计工时 |
|--------|--------|----------|--------|----------|
| P1 | VULN-002 | {name} | {owner} | {hours}h |

### 中期修复 (30天内)
| 优先级 | 漏洞ID | 漏洞名称 | 负责人 | 预计工时 |
|--------|--------|----------|--------|----------|
| P2 | VULN-003 | {name} | {owner} | {hours}h |

---

## 8. 附录 (Appendix)

### A. 使用工具清单
| 工具 | 版本 | 用途 |
|------|------|------|
| {tool} | {version} | {purpose} |

### B. 测试账号和凭据（审计后已销毁）
- {说明}

### C. 原始扫描数据
- {文件路径}

### D. 参考资料
- {参考文档列表}
```

