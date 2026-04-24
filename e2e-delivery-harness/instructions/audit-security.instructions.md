---
name: security-audit
description: 安全审计执行指南，用于执行安全测试
type: instruction
version: "1.1.0"
stage: testing
---

# Security Audit Instruction

## Objective

执行安全审计，发现安全漏洞和风险，确保系统符合安全要求。

## Prerequisites

1. 测试环境可用
2. 安全测试工具
3. 系统文档
4. 渗透测试授权

## Process Steps

### Step 1: 收集信息

1. 收集系统架构
2. 收集 API 文档
3. 收集认证机制
4. 识别资产清单

### Step 2: 识别攻击面

1. 识别入口点
2. 识别信任边界
3. 识别数据流
4. 识别关键资产

### Step 3: 执行安全测试

按照 OWASP Top 10 执行：

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Auth Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF

### Step 4: 分析漏洞

1. 验证漏洞存在
2. 评估严重程度
3. 分析利用难度
4. 提出修复建议

### Step 5: 编写报告

1. 整理漏洞列表
2. 评估风险
3. 提出建议
4. 归档报告

## Quality Gates

### 准入检查

- [ ] 测试环境可用
- [ ] 测试工具就绪
- [ ] 审计范围已定

### 准出检查

- [ ] OWASP Top 10 已覆盖
- [ ] 漏洞列表完整
- [ ] 报告已归档

## Handoff Criteria

交接给开发前：

- [ ] 安全审计报告已完成
- [ ] 漏洞已确认
- [ ] 修复建议已提供
