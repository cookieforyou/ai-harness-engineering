---
name: security-audit
description: 安全审计技能，提供安全测试和漏洞评估的方法论
type: skill
version: "1.1.0"
stage: testing
---

# Security Audit Skill

## Skill Overview

安全审计是发现系统安全漏洞和风险的重要手段。本技能提供安全测试的方法论、检查清单和评估标准。

## Prerequisites

1. 理解 OWASP Top 10
2. 理解常见漏洞类型
3. 掌握安全测试工具

## Knowledge Base

### OWASP Top 10 (2021)

| 排名 | 漏洞类型 | 描述 |
|------|----------|------|
| A01 | Broken Access Control | 访问控制失效 |
| A02 | Cryptographic Failures | 加密失败 |
| A03 | Injection | 注入攻击 |
| A04 | Insecure Design | 不安全设计 |
| A05 | Security Misconfiguration | 安全配置错误 |
| A06 | Vulnerable Components | 漏洞组件 |
| A07 | Auth Failures | 认证失败 |
| A08 | Data Integrity Failures | 数据完整性失败 |
| A09 | Logging Failures | 日志记录失败 |
| A10 | SSRF | 服务器端请求伪造 |

### 漏洞严重程度 (CVSS)

| 等级 | 分值范围 | 描述 |
|------|----------|------|
| Critical | 9.0-10.0 | 紧急修复 |
| High | 7.0-8.9 | 优先修复 |
| Medium | 4.0-6.9 | 计划修复 |
| Low | 0.1-3.9 | 可选修复 |

### 常见漏洞检查

1. **注入漏洞**
   - SQL 注入
   - NoSQL 注入
   - LDAP 注入
   - OS 命令注入

2. **认证漏洞**
   - 弱密码
   - 会话管理问题
   - 多因素认证缺失

3. **敏感数据**
   - 敏感数据暴露
   - 加密不当
   - 密钥硬编码

4. **API 安全**
   - API 认证
   - API 限流
   - API 版本问题

## Procedures

### 安全审计流程

1. 收集系统信息
2. 识别攻击面
3. 执行安全测试
4. 分析漏洞
5. 评估风险
6. 编写报告

### 渗透测试流程

1. 侦察和信息收集
2. 漏洞扫描
3. 漏洞利用
4. 后渗透
5. 报告

## Tools & Resources

- OWASP ZAP
- Burp Suite
- SQLMap
- Nmap
- Nessus

## Validation

### 审计完整性检查

- [ ] OWASP Top 10 已覆盖
- [ ] 所有入口点已测试
- [ ] 漏洞已验证

### 报告质量检查

- [ ] 漏洞描述准确
- [ ] CVSS 评分合理
- [ ] 修复建议可行

## Examples

### Example：SQL 注入漏洞

**发现位置**：/api/users?id=1

**测试方法**：
```
/api/users?id=1' OR '1'='1
```

**结果**：返回所有用户数据

**漏洞类型**：SQL 注入
**CVSS 评分**：9.8 (Critical)

**修复建议**：
- 使用参数化查询
- 输入验证
- 最小权限原则


## Core Knowledge

> Essential knowledge domain for audit-security execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for audit-security excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during audit-security execution.

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
