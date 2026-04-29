# Instructions: 密钥管理 (Manage Secrets)

## 密钥管理服务选型

### 主流服务对比

| 服务 | 特点 | 适用场景 |
|------|------|----------|
| HashiCorp Vault | 开源、功能全面 | 多云/混合云 |
| AWS Secrets Manager | AWS 原生集成 | AWS 环境 |
| Azure Key Vault | Azure 原生集成 | Azure 环境 |
| 阿里云 KMS | 阿里云原生集成 | 阿里云环境 |
| GCP Cloud KMS | GCP 原生集成 | GCP 环境 |

### HashiCorp Vault 架构

```yaml
vault_architecture:
  storage_backend:
    - "Consul"
    - "etcd"
    - "DynamoDB"
    - "PostgreSQL"

  high_availability:
    mode: "active-active"
    nodes: 3
    consensus: "Raft"

  audit:
    backends:
      - "file"
      - "syslog"
      - "cloudwatch"
```

## 密钥类型规范

### 密钥分类

```yaml
secret_types:
  high_sensitive:
    examples:
      - "生产数据库密码"
      - "支付 API 密钥"
      - "私钥/证书"
      - "OAuth Client Secret"
    rotation_period: "30 天"
    encryption: "required"

  medium_sensitive:
    examples:
      - "测试环境密钥"
      - "内部 API 密钥"
      - "监控凭证"
    rotation_period: "90 天"
    encryption: "required"

  low_sensitive:
    examples:
      - "公开配置"
      - "非敏感参数"
    rotation_period: "180 天"
    encryption: "optional"
```

## 访问控制规范

### 基于角色的访问控制

```yaml
# Vault Policy 示例
path "secret/data/prod/*" {
  capabilities = ["read"]
}

path "secret/data/prod/database" {
  capabilities = ["read"]
  policy = "high_sensitivity"
}

path "secret/metadata/*" {
  capabilities = ["list"]
}
```

### 身份认证方法

| 方法 | 适用场景 | 安全等级 |
|------|----------|----------|
| AppRole | 服务间认证 | 高 |
| Kubernetes Auth | K8s Pod | 高 |
| AWS IAM Auth | AWS 资源 | 高 |
| LDAP Auth | 人类用户 | 中 |
| Token Auth | 临时访问 | 低 |

## 密钥轮换规范

### 轮换策略

```yaml
rotation_strategy:
  automatic:
    enabled: true
    methods:
      - "Vault Agent"
      - "动态密钥"
      - "Webhook"

  manual:
    enabled: true
    triggers:
      - "安全事件"
      - "人员变更"
      - "定期审计"

  emergency:
    enabled: true
    procedure: "立即轮换 + 通知"
```

### 动态密钥 vs 静态密钥

```yaml
comparison:
  dynamic_secrets:
   优点:
      - "无持久化存储"
      - "自动过期"
      - "最小权限"
    适用:
      - "数据库凭证"
      - "云服务凭证"

  static_secrets:
    优点:
      - "可控性强"
      - "兼容性好"
    适用:
      - "API 密钥"
      - "证书私钥"
```

## 密钥存储规范

### 密钥存储结构

```yaml
secret_path_structure:
  secret/
    ├── data/
    │   ├── prod/
    │   │   ├── database/
    │   │   │   ├── primary-password
    │   │   │   └── replica-password
    │   │   ├── api-keys/
    │   │   │   ├── stripe
    │   │   │   └── twilio
    │   │   └── certificates/
    │   ├── staging/
    │   └── dev/
    └── metadata/
```

### 密钥命名规范

```yaml
naming_convention:
  pattern: "{environment}-{service}-{purpose}"
  examples:
    - "prod-db-primary-password"
    - "staging-api-stripe-key"
    - "dev-cache-redis-password"

  forbidden:
    - "明文密码"
    - "默认密码"
    - "环境名称混淆"
```

## 密钥使用规范

### 安全最佳实践

```yaml
best_practices:
  do:
    - "使用密钥管理服务"
    - "启用审计日志"
    - "配置自动轮换"
    - "遵循最小权限"
    - "密钥不写入代码"
    - "定期安全审计"

  dont:
    - "密钥提交到代码仓库"
    - "密钥硬编码"
    - "密钥写在配置文件"
    - "密钥通过日志输出"
    - "共享密钥"
```

### 密钥访问模式

```yaml
access_patterns:
  # Kubernetes Pod 中使用
  kubernetes:
    method: "Vault Agent Sidecar"
    example: |
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "app-role"

  # CI/CD 中使用
  cicd:
    method: "Vault CLI / API"
    example: |
      vault kv get -field=password secret/prod/db

  # 应用中使用
  application:
    method: "SDK"
    example: |
      client = VaultClient()
      password = client.get_secret("secret/prod/db/password")
```

## 审计规范

### 审计日志配置

```yaml
audit_config:
  enabled: true

  backends:
    - type: "file"
      path: "/var/log/vault/audit.log"

    - type: "syslog"
      facility: "AUTH"

    - type: "cloudwatch"
      log_group: "/aws/vault/audit"

  logged_events:
    - "read"
    - "write"
    - "delete"
    - "list"
    - "policy_changes"

  retention:
    days: 365
    storage: "encrypted"
```

### 告警规则

```yaml
alert_rules:
  - name: "unauthorized_access"
    condition: "response.status == 403"
    severity: "critical"
    action: "notify_security"

  - name: "bulk_access"
    condition: "count > 100 in 1 minute"
    severity: "warning"
    action: "notify_team"

  - name: "key_expiration"
    condition: "days_to_expiry < 7"
    severity: "warning"
    action: "notify_owner"

  - name: "key_modification"
    condition: "operation == write AND sensitivity == high"
    severity: "info"
    action: "log_only"
```

## 合规要求

### 常见合规标准

| 标准 | 要求 | 密钥管理相关 |
|------|------|--------------|
| SOC 2 | 访问控制、加密 | 审计日志、密钥轮换 |
| PCI DSS | 密钥管理 | 密钥分离、加密标准 |
| GDPR | 数据保护 | 加密密钥保护 |
| HIPAA | 医疗数据 | 密钥访问控制 |

### 加密标准

```yaml
encryption_standards:
  algorithm:
    symmetric: "AES-256-GCM"
    asymmetric: "RSA-2048 / RSA-4096"
    hashing: "SHA-256"

  key_length:
    aes: 256
    rsa: 2048
    ec: "P-256"

  compliance:
    fips_140_2: true
    pci_dss: true
```
