---
name: audit-security
description: "安全审计技能，提供安全测试和漏洞评估的方法论"
category: governance
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['skill', 'knowledge']
---
# Security Audit Skill

## Skill Overview

安全审计是发现系统安全漏洞和风险的重要手段。本技能提供安全测试的方法论、检查清单和评估标准。

## Prerequisites

1. 理解 OWASP Top 10
2. 理解常见漏洞类型
3. 掌握安全测试工具

## Knowledge Base

### OWASP Top 10 (2021) — 详细说明

| 排名 | 漏洞类型 | 描述 | 常见场景 | 测试方法 | 修复建议 |
|------|----------|------|----------|----------|----------|
| A01 | **Broken Access Control** (访问控制失效) | 未正确实施权限限制，用户可访问未授权功能或数据 | IDOR越权、目录遍历、权限提升、CORS配置错误 | 手动测试不同角色的端点访问、修改请求参数中的ID | 实施RBAC/ABAC，服务器端权限校验，拒绝默认 |
| A02 | **Cryptographic Failures** (加密失败) | 敏感数据未加密或使用弱加密算法 | 明文密码存储、HTTPS未强制、弱TLS配置、硬编码密钥 | 检查数据传输加密、扫描配置文件中的密钥 | 使用强加密算法(AES-256)，密钥托管于Vault/KMS |
| A03 | **Injection** (注入攻击) | 不可信数据作为命令或查询的一部分执行 | SQL/NoSQL注入、OS命令注入、LDAP注入、模板注入 | 输入点fuzz测试、参数化查询检查、时间盲注测试 | 参数化查询/预编译语句、输入验证与净化、最小权限 |
| A04 | **Insecure Design** (不安全设计) | 架构层面存在安全缺陷，非实现Bug | 缺乏速率限制、未设计安全控制、信任默认配置 | 架构评审、威胁建模(STRIDE)、设计文档审查 | 安全设计评审(SDL)、威胁建模前置、安全模式应用 |
| A05 | **Security Misconfiguration** (安全配置错误) | 系统配置不当导致安全漏洞 | 默认凭据未修改、错误信息泄露、目录列表启用、多余端口开放 | 配置审计、端口扫描、HTTP头检查、云配置检查 | 最小化配置、自动化配置基线检查、定期审计 |
| A06 | **Vulnerable and Outdated Components** (漏洞组件) | 使用了已知漏洞的第三方库或框架 | Log4Shell、过时的依赖库、未打补丁的中间件 | SCA扫描 (Snyk/Trivy/Dependency-Check)、版本检查 | 及时更新依赖、SCA集成到CI/CD、SBOM管理 |
| A07 | **Identification and Authentication Failures** (认证失败) | 身份验证和会话管理缺陷 | 弱密码策略、会话固定、暴力破解无防护、凭据填充 | 密码策略检查、会话Token分析、MFA验证 | 强密码策略、MFA强制、账户锁定机制、OAuth 2.1/OIDC |
| A08 | **Software and Data Integrity Failures** (数据完整性失败) | 软件更新和数据完整性验证缺失 | 不安全的反序列化、CI/CD管道无签名校验、不安全的自动更新 | 反序列化测试、供应链安全检查、签名验证检查 | 代码签名、完整性校验(CSP/SRI)、安全序列化库 |
| A09 | **Security Logging and Monitoring Failures** (日志监控失败) | 安全日志记录不充分，无法检测和追溯安全事件 | 日志缺失关键事件、日志存储不安全、监控告警未配置 | 审计日志覆盖检查、日志完整性验证、告警规则审查 | 关键事件全量日志、日志集中管理(SIEM)、实时告警 |
| A10 | **Server-Side Request Forgery** (SSRF) | 服务器端请求伪造，攻击者可让服务器发起未授权请求 | URL读取外部资源、代理转发、云元数据API访问 | 输入URL变换测试、内部网络探测、云元数据访问测试 | URL白名单、禁用不必要的协议、网络分段隔离 |

### 漏洞严重程度 (CVSS)

| 等级 | 分值范围 | 描述 |
|------|----------|------|
| Critical | 9.0-10.0 | 紧急修复 |
| High | 7.0-8.9 | 优先修复 |
| Medium | 4.0-6.9 | 计划修复 |
| Low | 0.1-3.9 | 可选修复 |

### STRIDE 威胁建模框架

STRIDE 是由微软提出的威胁分类模型，用于系统化识别安全威胁：

| 威胁类型 | 英文 | 定义 | 安全属性 | 典型攻击 | 防御措施 |
|----------|------|------|----------|----------|----------|
| **伪装** | Spoofing | 冒充他人身份访问系统 | 身份认证 | 会话劫持、密码暴力破解、JWT伪造 | 强认证、MFA、证书认证 |
| **篡改** | Tampering | 未授权修改数据或代码 | 完整性 | SQL注入修改数据、请求参数篡改、中间人攻击 | 数字签名、完整性校验、输入验证 |
| **抵赖** | Repudiation | 用户否认执行过的操作 | 不可否认性 | 日志缺失、操作无记录、审计追踪不完整 | 完整审计日志、数字签名、WORM存储 |
| **信息泄露** | Information Disclosure | 敏感信息暴露给未授权方 | 机密性 | 数据泄露、错误信息暴露、侧信道攻击 | 加密、最小数据暴露、访问控制 |
| **拒绝服务** | Denial of Service | 系统资源耗尽无法服务 | 可用性 | DDoS攻击、慢速攻击、资源耗尽、无限循环 | 限流、资源隔离、CDN/云防护 |
| **权限提升** | Elevation of Privilege | 未授权获取更高权限 | 授权 | 水平越权、垂直越权、角色滥用 | 最小权限、RBAC/ABAC、基于策略的访问控制 |

### 常见漏洞模式与代码示例

#### 1. SQL注入 (SQL Injection)

**漏洞代码**:
```python
# 不安全的字符串拼接
user_id = request.GET['id']
query = f"SELECT * FROM users WHERE id = '{user_id}'"
cursor.execute(query)
```

**攻击Payload**: `' OR '1'='1` → 查询所有用户

**安全代码**:
```python
# 使用参数化查询
user_id = request.GET['id']
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))
```

#### 2. 跨站脚本 (XSS)

**漏洞代码**:
```javascript
// 直接将用户输入插入DOM
const userName = new URLSearchParams(location.search).get('name');
document.getElementById('greeting').innerHTML = `Hello ${userName}`;
```

**攻击Payload**: `<script>fetch('/api/steal', {body: document.cookie})</script>`

**安全代码**:
```javascript
// 使用textContent而非innerHTML
const userName = new URLSearchParams(location.search).get('name');
document.getElementById('greeting').textContent = `Hello ${userName}`;

// 或使用DOMPurify净化HTML
import DOMPurify from 'dompurify';
document.getElementById('greeting').innerHTML = DOMPurify.sanitize(`Hello ${userName}`);
```

#### 3. 不安全的反序列化

**漏洞代码**:
```python
import pickle

# 不安全的反序列化用户数据
user_data = pickle.loads(request.data)  # 可执行任意代码
```

**安全代码**:
```python
import json

# 使用安全的序列化格式
user_data = json.loads(request.data)
```

#### 4. 访问控制失效 (IDOR)

**漏洞代码**:
```javascript
// 仅依赖请求参数控制访问
app.get('/api/order/:id', (req, res) => {
  // 未检查当前用户是否有权访问该订单
  const order = db.findOrder(req.params.id);
  res.json(order);
});
```

**安全代码**:
```javascript
app.get('/api/order/:id', (req, res) => {
  const userId = req.session.userId;  // 从会话获取当前用户
  // 验证订单归属当前用户
  const order = db.findOrderByIdAndUserId(req.params.id, userId);
  if (!order) return res.status(403).json({ error: 'Forbidden' });
  res.json(order);
});
```

#### 5. SSRF (服务器端请求伪造)

**漏洞代码**:
```python
# 直接使用用户输入构造请求
url = request.GET['url']
response = requests.get(url, timeout=5)  # 可访问内部服务
```

**攻击Payload**: `http://169.254.169.254/latest/meta-data/` (云元数据)

**安全代码**:
```python
from urllib.parse import urlparse

def is_safe_url(url):
    parsed = urlparse(url)
    allowed_hosts = ['api.trusted.com', 'cdn.trusted.com']
    return parsed.hostname in allowed_hosts

url = request.GET['url']
if not is_safe_url(url):
    return ResponseError('URL not allowed')
# 且限制协议、禁用内部IP


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

## Security Testing Tools Reference (安全测试工具参考)

### SAST (静态应用安全测试)
| 工具 | 类型 | 适用场景 | 特点 |
|------|------|----------|------|
| **Semgrep** | 开源 | 自定义规则SAST | 支持多语言，规则编写灵活，CI/CD集成友好 |
| **SonarQube** | 开源/商业 | 代码质量+安全 | 支持30+语言，安全热点检测，质量门禁 |
| **Checkmarx** | 商业 | 企业级SAST | 高精度，支持IaC和API安全，CxFlow集成 |
| **Fortify (MicroFocus)** | 商业 | 企业级SAST | 合规审计强，支持大规模代码库，NIST认证 |
| **CodeQL (GitHub)** | 商业(BB) | 深度安全分析 | 查询语言灵活，CVE发现能力强，DevSecOps集成 |

### DAST (动态应用安全测试)
| 工具 | 类型 | 适用场景 | 特点 |
|------|------|----------|------|
| **OWASP ZAP** | 开源 | Web应用安全扫描 | 插件生态丰富，API扫描，主动/被动扫描模式 |
| **Burp Suite Pro** | 商业 | 手动渗透测试 | Repeater/Intruder/Scanner，扩展生态(BApp) |
| **Acunetix** | 商业 | DAST全栈扫描 | 深度扫描，SaaS/本地部署，WAF集成 |
| **Nessus** | 商业 | 基础设施漏洞扫描 | 兼容性广，CVE数据库全面，合规模板 |

### SCA (软件组成分析)
| 工具 | 类型 | 适用场景 | 特点 |
|------|------|----------|------|
| **Snyk** | 商业(BB) | 容器/依赖/代码 | 容器镜像扫描，依赖树分析，PR自动修复 |
| **Trivy** | 开源 | 容器/依赖/IaC | 轻量快速，多格式支持，CVE精准 |
| **OWASP Dependency-Check** | 开源 | Java/.NET/NPM | OWASP官方，CPE匹配，OWASP Top 10覆盖 |
| **Renovate** | 开源 | 依赖自动更新 | 自动创建PR更新依赖，可自定义策略 |

### 基础设施与云安全
| 工具 | 类型 | 适用场景 | 特点 |
|------|------|----------|------|
| **Prowler** | 开源 | AWS安全审计 | 300+检查项，CIS基准，合规报告 |
| **ScoutSuite** | 开源 | 多云安全审计 | AWS/Azure/GCP，多账户支持 |
| **OpenSCAP** | 开源 | 系统基线检查 | CIS/STIG基准，合规报告生成 |
| **Lynis** | 开源 | Linux安全审计 | 通用系统审计，建议修复措施 |
| **kube-bench** | 开源 | K8s安全审计 | CIS K8s基准，自动检查集群配置 |

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

> 安全审计领域的核心知识体系

### Domain Fundamentals

1. **网络安全基础 (Network Security)**
   - TCP/IP协议栈安全：TCP SYN Flood、DNS劫持、ARP欺骗
   - 网络分段策略：DMZ、VLAN、微隔离
   - TLS/SSL协议：握手过程、证书链验证、密码套件、降级攻击

2. **Web应用安全基础 (Web Application Security)**
   - HTTP协议安全：请求伪造、头注入、会话管理
   - 同源策略(SOP)与跨域资源(CORS)：浏览器安全模型
   - 认证与授权机制：Session/Cookie/JWT/OAuth 2.0/OIDC/SAML

3. **密码学基础 (Cryptography)**
   - 对称加密：AES-256-GCM、ChaCha20-Poly1305
   - 非对称加密：RSA、ECDSA、Ed25519
   - 哈希函数：SHA-256、SHA-3、bcrypt/Argon2（密码存储）
   - 密钥管理：密钥生命周期、HSM、密钥派生

4. **操作系统与基础设施安全 (OS & Infrastructure)**
   - Linux安全：SELinux/AppArmor、Capabilities、Namespace
   - 容器安全：镜像扫描、运行时安全、Seccomp/AppArmor Profile
   - 云安全：IAM策略、安全组、VPC设计、KMS密钥管理

5. **威胁情报 (Threat Intelligence)**
   - 常见威胁行为体：APT组织、勒索软件团伙、脚本小子
   - TTPs (Tactics, Techniques, Procedures)：MITRE ATT&CK框架
   - IoC (Indicators of Compromise)：入侵指标识别与分类

### Key Principles

1. **纵深防御 (Defense in Depth)**: 不依赖单一安全控制，在多个层面部署防御措施（网络层→主机层→应用层→数据层）
2. **最小权限 (Least Privilege)**: 用户和系统只应拥有完成任务所需的最小权限集合
3. **安全默认 (Secure by Default)**: 系统默认配置应该是安全的，关闭不必要的服务和端口
4. **永不信任，始终验证 (Zero Trust)**: 不信任任何内部或外部流量，每次访问都需要验证和授权
5. **公开设计 (Open Design)**: 安全不应依赖于保密，而应依赖于强密钥和算法（Kerckhoffs原则）

### 漏洞分类标准

| 分类体系 | 用途 | 常用场景 |
|----------|------|----------|
| **CVE** | 通用漏洞披露 | 标识已知漏洞的唯一编号 |
| **CWE** | 通用缺陷枚举 | 漏洞类型的标准化分类 |
| **CVSS 3.1** | 通用漏洞评分系统 | 漏洞严重程度量化评分 |
| **OWASP Top 10** | Web应用安全风险 | 重点关注TOP风险类别 |
| **MITRE ATT&CK** | 攻击技术知识库 | 威胁建模和防御策略设计 |


## Best Practices

> 安全审计最佳实践

1. **范围明确化 (Scope Clarity)**: 审计开始前必须书面确认审计边界、目标系统、测试方法、时间窗口，避免范围蔓延和法律风险。签署授权书（RoE, Rules of Engagement）。

2. **证据完整性 (Evidence Integrity)**: 所有测试结果、截图、日志、请求/响应数据必须妥善保存，形成完整的证据链（Chain of Custody）。使用hash校验确保证据未被篡改。

3. **分类分级测试 (Tiered Testing)**: 先执行自动化扫描发现问题，再对手工验证高风险项目，最后进行深度渗透测试。避免在未扫描前直接进行手工测试浪费资源。

4. **误差控制 (Error Control)**: 建立误报/漏报验证机制。自动化扫描结果必须经过人工验证后方可确认为有效发现。使用多种工具交叉验证。

5. **修复验证闭环 (Fix Verification Loop)**: 所有修复建议必须附带验证方法，修复完成后需要进行回归测试确认已修复，防止"修复失败"或"修复不完整"。

6. **报告结构化 (Structured Reporting)**: 报告按严重程度排序，执行摘要面向管理层，详细发现面向技术团队，修复建议应明确优先级和责任人。

7. **保密与安全 (Confidentiality)**: 审计数据和报告属于高度敏感信息，加密传输和存储，仅限于知悉需要的人员访问。

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> 安全审计中的常见陷阱

### Pitfall 1: 范围蔓延 (Scope Creep)
**Risk**: 审计过程中不断加入新的测试目标，导致审计范围失控、时间超支、资源不足
**Prevention**: 
- 审计前签署明确的审计授权书，定义不可变更的边界
- 发现超出范围的高风险资产时，先申请范围变更再测试
- 未经授权严禁测试第三方系统或生产环境
**Impact**: 导致审计延期、法律风险、客户信任损害

### Pitfall 2: 自动化扫描替代人工验证
**Risk**: 完全依赖自动化扫描工具，不进行人工验证和深入分析
**Prevention**: 
- 自动化扫描作为初步发现手段，关键漏洞必须人工复现
- 业务逻辑漏洞、配置缺陷、设计缺陷依赖人工发现
- PoC必须是可复现的，不仅仅是工具输出
**Impact**: 漏报率显著上升（自动化扫描只能发现约60%的漏洞），误报不排除导致报告质量差

### Pitfall 3: CVSS评分不准确
**Risk**: 未正确计算CVSS环境度量，导致漏洞优先级排序错误
**Prevention**: 
- 使用最新的CVSS 3.1计算器验证评分
- 结合业务场景调整环境度量（资产价值、影响范围）
- 对Critical/High评分进行二次审核
**Impact**: 高危漏洞被低估导致修复延迟，低危漏洞被高估浪费修复资源

### Pitfall 4: 忽略业务逻辑漏洞
**Risk**: 只关注技术漏洞（SQL注入、XSS等），忽略业务逻辑层面的安全问题
**Prevention**: 
- 在审计前充分了解业务逻辑和流程
- 手工测试关键业务流程的旁路可能（绕过支付、批量注册、优惠滥用）
- 竞态条件、参数篡改、批量分配等逻辑漏洞测试
**Impact**: 逻辑漏洞可能导致严重经济损失（如绕过支付、套利）

### Pitfall 5: 测试导致生产环境问题
**Risk**: 渗透测试操作不当导致生产环境服务中断或数据损坏
**Prevention**: 
- 测试前明确区分生产环境和测试环境
- 限制写入/删除操作，使用只读模式测试
- 高危payload在测试环境确认后再使用
- 准备应急回滚方案
**Impact**: 生产环境故障导致业务中断，客户数据丢失或损坏
