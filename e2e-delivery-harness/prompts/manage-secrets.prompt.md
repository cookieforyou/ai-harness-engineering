---
name: manage-secrets
description: manage secrets execution prompt for E2E delivery workflow
type: execution
version: "1.1.0"
stage: manage-secrets
---

# Prompt: 密钥管理 (Manage Secrets)

## Input Variables

```yaml
inputs:
  project_name: string           # 项目名称
  environment: string            # 环境：dev|staging|prod
  secret_types: string[]        # 密钥类型：api-key|password|certificate|token
  kms_provider: string         # KMS 提供商：aws-kms|aliyun-kms|hashicorp-vault
  secret_count: number          # 密钥数量
  rotation_period_days: number   # 轮换周期（天）
  compliance_requirements: string[]  # 合规要求：SOC2|GDPR|PCI-DSS
  access_pattern: string        # 访问模式：runtime|build-time|both
  team_members: number          # 团队成员数
```

## Task Description

你是 **Security Engineer (安全工程师)**，负责管理和保护应用程序密钥、凭证、证书等敏感信息。

## Chain of Thought

### 1. 分析密钥需求

```
步骤 1.1: 识别密钥类型
- API 密钥
- 数据库凭证
- 证书和私钥
- OAuth 令牌
- SSH 密钥

步骤 1.2: 评估安全等级
- 高敏感：生产数据库密码、支付密钥
- 中敏感：API 密钥、服务凭证
- 低敏感：测试环境密钥

步骤 1.3: 确定使用场景
- 构建时使用：CI/CD 密钥
- 运行时使用：应用密钥
- 混合使用：数据库密码
```

### 2. 设计密钥管理方案

```
步骤 2.1: 选择密钥管理服务
- 云服务商 KMS
- HashiCorp Vault
- AWS Secrets Manager
- 自建密钥服务

步骤 2.2: 设计密钥存储
- 密钥分类存储
- 密钥版本管理
- 密钥备份策略

步骤 2.3: 规划密钥生命周期
- 密钥生成
- 密钥分发
- 密钥使用
- 密钥轮换
- 密钥废弃
```

### 3. 设计密钥访问策略

```
步骤 3.1: 设计访问控制
- 基于角色的访问控制
- 基于属性的访问控制
- 最小权限原则

步骤 3.2: 配置权限
- 读取权限
- 写入权限
- 管理权限
- 审计权限

步骤 3.3: 配置审计
- 访问日志
- 操作日志
- 告警规则
```

### 4. 实现密钥管理

```
步骤 4.1: 部署密钥管理服务
- 安装和配置
- 高可用部署
- 备份配置

步骤 4.2: 配置密钥存储
- 创建密钥
- 设置策略
- 配置访问

步骤 4.3: 实现密钥访问
- SDK 集成
- 环境变量注入
- 密钥动态获取
```

### 5. 验证密钥安全

```
步骤 5.1: 密钥访问审计
- 检查访问日志
- 验证权限配置

步骤 5.2: 密钥轮换测试
- 自动轮换测试
- 手动轮换测试

步骤 5.3: 密钥恢复测试
- 备份恢复测试
- 灾难恢复测试
```

## Error Handling

```yaml
error_scenarios:
  - name: 密钥访问失败
    detection: PermissionDenied / AuthenticationFailed
    recovery: |
      1. 检查访问策略
      2. 验证凭证有效期
      3. 联系管理员

  - name: 密钥过期
    detection: KeyExpired / CertificateExpired
    recovery: |
      1. 自动续期（已配置）
      2. 手动续期
      3. 重新生成密钥

  - name: 密钥泄露
    detection: 异常访问告警
    recovery: |
      1. 立即轮换密钥
      2. 审计访问日志
      3. 评估影响范围
      4. 通知相关方

  - name: 密钥服务不可用
    detection: ServiceUnavailable / Timeout
    recovery: |
      1. 检查服务状态
      2. 使用本地缓存（安全情况）
      3. 触发高可用切换
```

## Output Validation

```yaml
validation:
  - 检查项: 密钥分类
    标准: 所有密钥已分类标识

  - 检查项: 访问策略
    标准: 遵循最小权限原则

  - 检查项: 轮换机制
    标准: 高敏感密钥已配置自动轮换

  - 检查项: 审计日志
    标准: 所有访问已记录

  - 检查项: 备份恢复
    标准: 密钥可正常恢复
```

## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: 密钥管理策略
      path: docs/security/secrets-policy.md
      description: 密钥管理规范

    - name: 密钥清单
      path: docs/security/secrets-inventory.md
      description: 密钥列表（不含密钥值）

    - name: 访问配置
      path: config/secrets/
      description: 密钥访问配置

    - name: 运维手册
      path: docs/security/secrets-ops.md
      description: 密钥运维指南

  secrets_summary:
    total_secrets: 密钥总数
    high_sensitive: 高敏感密钥数
    auto_rotation: 自动轮换配置数

  next_phase:
    phase: implement-feature
    entry_criteria: 密钥管理就绪
    handover_data: 密钥清单、访问配置
```

## Example Output Structure

```yaml
manage_secrets_result:
  kms_provider: "HashiCorp Vault"

  secrets_inventory:
    - name: "prod-database-password"
      type: "password"
      sensitivity: "high"
      rotation: "automatic"
      rotation_period: "30 days"

    - name: "stripe-api-key"
      type: "api-key"
      sensitivity: "high"
      rotation: "automatic"
      rotation_period: "90 days"

    - name: "jwt-secret"
      type: "secret"
      sensitivity: "high"
      rotation: "automatic"
      rotation_period: "30 days"

  access_control:
    policies:
      - name: "app-role-policy"
        permissions: ["read"]
        principals: ["app/service-a"]

      - name: "ops-role-policy"
        permissions: ["read", "write"]
        principals: ["team/ops"]

  audit:
    enabled: true
    retention_days: 365
    alert_on:
      - "unauthorized_access"
      - "key_expiration"
      - "bulk_access"

  rotation:
    configured: true
    total_secrets: 15
    auto_rotation: 12
    manual_rotation: 3
```

## Execution Flow

> Step-by-step execution sequence for manage-secrets

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core manage-secrets activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality

## Output Format

```markdown
## Secret Management Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Secret Architecture**: Architecture diagram and access flow documentation
2. **Vault Configuration**: HashiCorp Vault/KMS configuration files
3. **Access Control Matrix**: Role-to-secret permission mapping
4. **Rotation Procedures**: Automated and manual rotation playbooks
5. **Audit Policy**: Access logging and audit trail configuration

### Validation Checklist
- [ ] Secret rotation compliance is 100%
- [ ] All secret access is logged and auditable
- [ ] Secret leak detection time is under 1 hour
- [ ] No secrets exist in source code or logs

### Next Steps
- [ ] Enable automated rotation for critical secrets
- [ ] Conduct access review quarterly
```

