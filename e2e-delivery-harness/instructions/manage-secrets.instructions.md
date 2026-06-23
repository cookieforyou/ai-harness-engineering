---
name: manage-secrets
description: "Detailed technical instructions for manage-secrets scenario execution"
applyTo: "scenarios/manage-secrets/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 密钥管理 (Manage Secrets)

## Secret Management Service Selection

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

## Secret Type Standards

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

## Access Control Standards

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

## Secret Rotation Standards

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

## Secret Storage Standards

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

## Secret Usage Standards

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

## Audit Standards

### 审计日志配置

```yaml
audit_config:
  enabled: true

  backends:
    - type: "file"
      path: "{{vault_audit_log_path}}"

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

## Compliance Requirements

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


## Overview

> High-level description of the manage-secrets execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the manage-secrets scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-secrets.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Multi-Language Code Examples

> Production-ready secret management code examples across multiple languages.

### Java (Spring Vault + AWS KMS)

Secret retrieval and rotation with Vault-backed property source and AWS KMS key wrapping.

```java
// VaultConfig.java -- Spring Vault configuration
import org.springframework.context.annotation.Configuration;
import org.springframework.vault.authentication.AppRoleAuthentication;
import org.springframework.vault.authentication.AppRoleAuthenticationOptions;
import org.springframework.vault.client.VaultEndpoint;
import org.springframework.vault.config.AbstractVaultConfiguration;
import org.springframework.vault.support.VaultToken;
import org.springframework.beans.factory.annotation.Value;

import java.net.URI;

@Configuration
public class VaultConfig extends AbstractVaultConfiguration {

    @Value("${vault.uri:https://vault.example.com:8200}")
    private String vaultUri;

    @Value("${vault.approle.role-id}")
    private String roleId;

    @Value("${vault.approle.secret-id}")
    private String secretId;

    @Override
    public VaultEndpoint vaultEndpoint() {
        return VaultEndpoint.from(URI.create(vaultUri));
    }

    @Override
    public ClientAuthentication clientAuthentication() {
        AppRoleAuthenticationOptions options = AppRoleAuthenticationOptions.builder()
            .roleId(AppRoleAuthenticationOptions.RoleId.provided(roleId))
            .secretId(AppRoleAuthenticationOptions.SecretId.provided(secretId))
            .build();
        return new AppRoleAuthentication(options, restOperations());
    }
}

// SecretService.java -- read and rotate secrets
import org.springframework.stereotype.Service;
import org.springframework.vault.core.VaultKeyValueOperationsSupport;
import org.springframework.vault.core.VaultTemplate;
import org.springframework.vault.support.VaultResponse;
import java.util.Map;

@Service
public class SecretService {

    private final VaultTemplate vaultTemplate;

    public SecretService(VaultTemplate vaultTemplate) {
        this.vaultTemplate = vaultTemplate;
    }

    /** Read secret from Vault KV v2 engine. */
    public Map<String, Object> readSecret(String path) {
        var kvOps = vaultTemplate.opsForKeyValue("secret",
            VaultKeyValueOperationsSupport.KeyValueBackend.KV_2);
        VaultResponse response = kvOps.get(path);
        if (response == null || response.getData() == null) {
            throw new RuntimeException("Secret not found: " + path);
        }
        return response.getData();
    }

    /** Rotate a secret by writing a new version. */
    public void rotateSecret(String path, Map<String, Object> newData) {
        var kvOps = vaultTemplate.opsForKeyValue("secret",
            VaultKeyValueOperationsSupport.KeyValueBackend.KV_2);
        kvOps.put(path, newData);
    }

    /** Wrap a secret with AWS KMS for transit encryption. */
    public byte[] wrapWithKms(byte[] plaintext, String kmsKeyId) {
        // AWS KMS encrypt call
        // AWSKMS kms = AWSKMSClientBuilder.defaultClient();
        // EncryptRequest req = new EncryptRequest()
        //     .withKeyId(kmsKeyId)
        //     .withPlaintext(ByteBuffer.wrap(plaintext));
        // EncryptResult result = kms.encrypt(req);
        // return result.getCiphertextBlob().array();
        throw new UnsupportedOperationException("KMS integration placeholder");
    }
}
```

### Go (Vault API)

Secret read, write, and dynamic secret lease management using the official Vault API client.

```go
package vault

import (
    "context"
    "fmt"
    "log"
    "os"
    "time"

    vault "github.com/hashicorp/vault/api"
)

// Client wraps the Vault API client with authentication.
type Client struct {
    client *vault.Client
}

// NewClient authenticates to Vault via AppRole and returns a ready client.
func NewClient(address, roleID, secretID string) (*Client, error) {
    config := vault.DefaultConfig()
    config.Address = address

    client, err := vault.NewClient(config)
    if err != nil {
        return nil, fmt.Errorf("failed to create vault client: %w", err)
    }

    // AppRole login
    data := map[string]interface{}{
        "role_id":   roleID,
        "secret_id": secretID,
    }
    resp, err := client.Logical().Write("auth/approle/login", data)
    if err != nil {
        return nil, fmt.Errorf("vault approle login failed: %w", err)
    }
    client.SetToken(resp.Auth.ClientToken)

    return &Client{client: client}, nil
}

// ReadSecret reads a secret from the KV v2 engine.
func (c *Client) ReadSecret(ctx context.Context, path string) (map[string]interface{}, error) {
    secret, err := c.client.Logical().ReadWithContext(ctx, path)
    if err != nil {
        return nil, fmt.Errorf("failed to read secret %s: %w", path, err)
    }
    if secret == nil || secret.Data == nil {
        return nil, fmt.Errorf("secret %s not found or no data", path)
    }
    // KV v2 returns data under "data" key
    data, ok := secret.Data["data"].(map[string]interface{})
    if !ok {
        return nil, fmt.Errorf("unexpected secret format at %s", path)
    }
    return data, nil
}

// WriteSecret writes a secret to the KV v2 engine.
func (c *Client) WriteSecret(ctx context.Context, path string, data map[string]interface{}) error {
    wrapped := map[string]interface{}{
        "data": data,
    }
    _, err := c.client.Logical().WriteWithContext(ctx, path, wrapped)
    if err != nil {
        return fmt.Errorf("failed to write secret %s: %w", path, err)
    }
    return nil
}

// DynamicDatabaseCredential acquires a dynamic database credential with a TTL.
func (c *Client) DynamicDatabaseCredential(ctx context.Context, role string) (*DynamicCred, error) {
    path := fmt.Sprintf("database/creds/%s", role)
    secret, err := c.client.Logical().ReadWithContext(ctx, path)
    if err != nil {
        return nil, fmt.Errorf("failed to get dynamic creds for %s: %w", role, err)
    }
    if secret == nil || secret.Data == nil {
        return nil, fmt.Errorf("no dynamic creds returned for %s", role)
    }

    leaseDuration := time.Duration(secret.LeaseDuration) * time.Second
    renewalDeadline := time.Now().Add(leaseDuration / 2)

    return &DynamicCred{
        Username:       secret.Data["username"].(string),
        Password:       secret.Data["password"].(string),
        LeaseID:        secret.LeaseID,
        Renewable:      secret.Renewable,
        LeaseDuration:  leaseDuration,
        RenewalDeadline: renewalDeadline,
    }, nil
}

// DynamicCred holds a dynamic credential and its lease metadata.
type DynamicCred struct {
    Username        string
    Password        string
    LeaseID         string
    Renewable       bool
    LeaseDuration   time.Duration
    RenewalDeadline time.Time
}

// RenewLease renews a dynamic secret lease before it expires.
func (c *Client) RenewLease(ctx context.Context, cred *DynamicCred) error {
    if !cred.Renewable {
        return fmt.Errorf("lease %s is not renewable", cred.LeaseID)
    }
    _, err := c.client.Sys().RenewWithContext(ctx, cred.LeaseID, int(cred.LeaseDuration.Seconds()))
    if err != nil {
        return fmt.Errorf("failed to renew lease %s: %w", cred.LeaseID, err)
    }
    // Reset renewal deadline
    cred.RenewalDeadline = time.Now().Add(cred.LeaseDuration / 2)
    log.Printf("Lease %s renewed, next renewal at %s", cred.LeaseID, cred.RenewalDeadline)
    return nil
}
```

### JavaScript (node-vault)

Vault client for CRUD operations on secrets with token renewal.

```javascript
// vault-client.js -- Vault secret management client
const vault = require('node-vault')({
  apiVersion: 'v1',
  endpoint: process.env.VAULT_ADDR || 'https://vault.example.com:8200',
  token: process.env.VAULT_TOKEN,
});

/**
 * Authenticate to Vault using AppRole.
 * @param {string} roleId  - AppRole RoleID
 * @param {string} secretId - AppRole SecretID
 * @returns {Promise<string>} Client token
 */
async function loginAppRole(roleId, secretId) {
  const result = await vault.approleLogin({
    role_id: roleId,
    secret_id: secretId,
  });
  vault.token = result.auth.client_token;
  return vault.token;
}

/**
 * Read a secret from KV v2 engine.
 * @param {string} path - Secret path (e.g., "prod/database/primary-password")
 * @returns {Promise<Object>} Secret data
 */
async function readSecret(path) {
  const fullPath = `secret/data/${path}`;
  const result = await vault.read(fullPath);
  if (!result || !result.data) {
    throw new Error(`Secret not found at ${fullPath}`);
  }
  // KV v2 wraps data under result.data.data
  return result.data.data;
}

/**
 * Write/update a secret in KV v2 engine.
 * @param {string} path   - Secret path
 * @param {Object} data   - Key-value pairs to store
 */
async function writeSecret(path, data) {
  const fullPath = `secret/data/${path}`;
  await vault.write(fullPath, { data });
  console.log(`Secret written to ${fullPath}`);
}

/**
 * Delete a secret and its metadata.
 * @param {string} path - Secret path
 */
async function deleteSecret(path) {
  const fullPath = `secret/data/${path}`;
  await vault.delete(fullPath);
  // Also delete metadata
  await vault.delete(`secret/metadata/${path}`);
  console.log(`Secret deleted from ${fullPath}`);
}

/**
 * List secrets under a given path.
 * @param {string} path - Base path to list
 * @returns {Promise<string[]>} List of secret keys
 */
async function listSecrets(path) {
  const fullPath = `secret/metadata/${path}`;
  const result = await vault.list(fullPath);
  return result.data.keys;
}

/**
 * Periodically renew the Vault token before expiration.
 * @param {number} intervalMs - Renewal interval in ms
 */
function startTokenRenewal(intervalMs = 1800000) {
  setInterval(async () => {
    try {
      await vault.tokenRenewSelf();
      console.log('Vault token renewed successfully');
    } catch (err) {
      console.error('Vault token renewal failed:', err.message);
    }
  }, intervalMs);
}

module.exports = {
  loginAppRole,
  readSecret,
  writeSecret,
  deleteSecret,
  listSecrets,
  startTokenRenewal,
};

// Example usage:
// const vault = require('./vault-client');
// await vault.loginAppRole(process.env.VAULT_ROLE_ID, process.env.VAULT_SECRET_ID);
// const dbPassword = await vault.readSecret('prod/database/primary-password');
// console.log('Database password retrieved');
```


## Best Practices

> Industry-standard best practices for manage-secrets execution.

1. **Practice 1**: Store secrets in dedicated vault or KMS solutions
2. **Practice 2**: Implement least-privilege access controls
3. **Practice 3**: Rotate secrets on schedule or after suspected compromise


## Error Handling

> Common error scenarios and resolution strategies for manage-secrets.

### Error Scenario 1: 密钥过期未轮转 (P1)

**触发条件**: Vault 中静态密钥超过轮转周期 (如 30 天/90 天) 未被更新。

**处理流程**:
```
IF key_rotation_overdue
  AND days_since_last_rotation > rotation_period
THEN
  1. 查询 Vault 元数据获取密钥创建时间和上次轮转时间
  2. 评估密钥依赖关系：哪些服务/实例正在使用该密钥
  3. 生成新密钥并写入 Vault，保留旧版本 (max_versions=5)
  4. 通知依赖服务使用新版密钥的路径
  5. 验证新密钥连通性 (数据库连接测试 / API 调用测试)
  6. 更新审计日志并设置下次轮转提醒
END
```

**降级方案**: 如自动轮转失败，手动通过 Vault UI/CLI 执行轮转，并延长旧密钥有效期 24 小时作为缓冲。

**升级条件**: 密钥已过期超过 7 天且依赖服务超过 5 个，升级为 P0 并强制轮转。

### Error Scenario 2: Vault不可用降级 (P1)

**触发条件**: 应用无法连接到 Vault 服务端或连接超时导致密钥获取失败。

**处理流程**:
```
IF vault_unreachable
  AND timeout > 5s OR connection_error
THEN
  1. 切换密钥获取策略：尝试备用 Vault 集群或本地缓存
  2. 检查本地密钥缓存有效期 (默认 60s)，有效期内继续服务
  3. 健康检查 Vault 集群状态 (sys/health API)
  4. 如主集群故障，自动切到灾备 Vault 集群
  5. 通知 SRE 和密钥管理团队启动 Vault 恢复流程
  6. 记录 Vault 不可用时段和受影响的密钥请求数
END
```

**降级方案**: 启用本地加密缓存，使用最近一次获取的有效密钥继续服务（缓存 TTL 可配置，默认 300 秒）。

**升级条件**: Vault 不可用超过 5 分钟或涉及关键支付/证书类密钥请求失败，升级为 P0。

### Error Scenario 3: 密钥泄露应急 (P0)

**触发条件**: 确认密钥被未授权实体获取，包括日志泄露、代码仓库泄露、外部安全通报。

**处理流程**:
```
IF secret_compromised
  AND confirmed_by_security_team
THEN
  1. 立即在 Vault 中禁用泄露密钥 (disable / revoke)
  2. 在宽限期内生成新密钥并部署到所有依赖服务
  3. 扫描所有可能泄露渠道：日志系统、Git 历史、CI/CD 产物
  4. 启用 Vault 审计回溯，查明密钥被访问的时间线和范围
  5. 更新访问策略，移除受影响的角色/Token 权限
  6. 发布安全事件报告，分析根本原因并改进防护措施
END
```

**降级方案**: 如无法立即部署新密钥，在 Vault 中启用密钥包装 (Key Wrapping)，使用封装密钥替换原始密钥。

**升级条件**: 泄露密钥具备外部系统访问权限或涉及合规数据 (PCI/GDPR)，立即启动公司安全事件响应流程。


## Quality Standards

> Acceptance criteria and quality gates for manage-secrets deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Secret rotation compliance is 100% | Automated check |
| Standard 2 | All secret access is logged and auditable | Automated check |
| Standard 3 | Secret leak detection time is under 1 hour | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
