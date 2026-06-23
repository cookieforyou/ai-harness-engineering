---
name: manage-secrets
description: "Domain skill for manage-secrets execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 密钥管理 (Secrets Management)

## Overview

本 Skill 定义了密钥管理的核心知识体系。

## Core Knowledge

### 密钥生命周期

```python
class SecretLifecycle:
    """密钥生命周期管理"""

    stages = [
        "generation",   # 生成
        "distribution", # 分发
        "usage",        # 使用
        "rotation",     # 轮换
        "retirement"    # 废弃
    ]

    def __init__(self):
        self.current_version = None

    def generate(self, secret_type):
        """生成密钥"""
        if secret_type == "symmetric":
            return self._generate_symmetric_key()
        elif secret_type == "asymmetric":
            return self._generate_asymmetric_key()
        elif secret_type == "certificate":
            return self._generate_certificate()

    def rotate(self, secret_name):
        """轮换密钥"""
        # 1. 生成新版本
        new_version = self.generate(self.get_type(secret_name))

        # 2. 更新密钥
        self.update(secret_name, new_version)

        # 3. 通知相关服务
        self.notify_rotation(secret_name)

        # 4. 旧版本保留一段时间
        self.schedule_deletion(secret_name, old_version)

    def retire(self, secret_name):
        """废弃密钥"""
        # 1. 停止分发
        self.disable(secret_name)

        # 2. 通知相关方
        self.notify_retirement(secret_name)

        # 3. 删除密钥
        self.delete(secret_name)
```

### 加密技术

```python
class Encryption:
    """加密工具类"""

    @staticmethod
    def encrypt_symmetric(plaintext, key):
        """对称加密"""
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend

        iv = os.urandom(16)
        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv, ciphertext, encryptor.tag

    @staticmethod
    def encrypt_asymmetric(plaintext, public_key):
        """非对称加密"""
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding

        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    @staticmethod
    def sign(data, private_key):
        """数字签名"""
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding

        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
```

### Vault 集成

```python
class VaultClient:
    """Vault 客户端"""

    def __init__(self, vault_addr, token=None, role_id=None, secret_id=None):
        self.client = self._init_client(vault_addr)
        if token:
            self.client.token = token
        elif role_id and secret_id:
            self._auth_approle(role_id, secret_id)

    def get_secret(self, path):
        """获取密钥"""
        return self.client.secrets.kv.v2.read_secret_version(path)

    def set_secret(self, path, data):
        """设置密钥"""
        self.client.secrets.kv.v2.create_or_update_secret(
            path=path,
            secret=data
        )

    def delete_secret(self, path):
        """删除密钥"""
        self.client.secrets.kv.v2.delete_metadata(path)

    def get_dynamic_secret(self, path):
        """获取动态密钥"""
        return self.client.secrets.database.generate_credentials(path)

    def rotate_static_secret(self, path):
        """轮换静态密钥"""
        return self.client.secrets.database.rotate_static_credentials(path)

    def renew_secret(self, lease_id):
        """续期密钥租约"""
        return self.client.leases.renew_secret(lease_id)

    def revoke_secret(self, lease_id):
        """吊销密钥"""
        self.client.leases.revoke_secret(lease_id)
```

### 密钥轮换实现

```python
class SecretRotation:
    """密钥轮换管理器"""

    def __init__(self, vault_client):
        self.client = vault_client
        self.rotation_policies = {}

    def register_policy(self, secret_path, policy):
        """注册轮换策略"""
        self.rotation_policies[secret_path] = policy

    def execute_rotation(self, secret_path):
        """执行轮换"""
        policy = self.rotation_policies.get(secret_path)
        if not policy:
            return

        if policy.type == "static":
            self._rotate_static(secret_path, policy)
        elif policy.type == "dynamic":
            self._rotate_dynamic(secret_path, policy)

    def _rotate_static(self, secret_path, policy):
        """轮换静态密钥"""
        # 1. 生成新密钥
        new_value = self._generate_new_secret(policy)

        # 2. 更新 Vault
        self.client.set_secret(secret_path, {"password": new_value})

        # 3. 通知应用
        self._notify_applications(secret_path)

        # 4. 记录审计
        self._audit_rotation(secret_path)

    def _rotate_dynamic(self, secret_path, policy):
        """轮换动态密钥"""
        # 动态密钥由 Vault 自动轮换
        self.client.rotate_static_secret(secret_path)

    def schedule_rotation(self):
        """定时轮换"""
        for secret_path, policy in self.rotation_policies.items():
            if self._should_rotate(secret_path, policy):
                self.execute_rotation(secret_path)
```

### KMS Integration Examples

#### Java: AWS KMS SDK with Spring Vault

```java
// Java implementation - AWS KMS encryption and Spring Vault integration
// Dependencies: aws-java-sdk-kms, spring-vault-core (Maven/Gradle)
package com.example.secrets;

import com.amazonaws.services.kms.AWSKMS;
import com.amazonaws.services.kms.AWSKMSClientBuilder;
import com.amazonaws.services.kms.model.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.vault.core.VaultKeyValueOperationsSupport;
import org.springframework.vault.core.VaultTemplate;
import org.springframework.vault.support.VaultResponse;

import javax.annotation.PostConstruct;
import java.nio.ByteBuffer;
import java.util.Base64;

@Component
public class KmsService {
    private AWSKMS kmsClient;

    @Value("${aws.kms.key-id}")
    private String kmsKeyId;

    @Value("${aws.region:us-east-1}")
    private String region;

    @PostConstruct
    public void init() {
        this.kmsClient = AWSKMSClientBuilder.standard()
            .withRegion(region)
            .build();
    }

    // Encrypt a plaintext string using AWS KMS
    public String encrypt(String plaintext) {
        EncryptRequest request = new EncryptRequest()
            .withKeyId(kmsKeyId)
            .withPlaintext(ByteBuffer.wrap(plaintext.getBytes()));

        EncryptResult result = kmsClient.encrypt(request);
        return Base64.getEncoder().encodeToString(result.getCiphertextForBlob().array());
    }

    // Decrypt a ciphertext string using AWS KMS
    public String decrypt(String ciphertext) {
        byte[] decoded = Base64.getDecoder().decode(ciphertext);

        DecryptRequest request = new DecryptRequest()
            .withCiphertextBlob(ByteBuffer.wrap(decoded));

        DecryptResult result = kmsClient.decrypt(request);
        return new String(result.getPlaintext().array());
    }

    // Generate a new data key for envelope encryption
    public GenerateDataKeyResult generateDataKey(String keySpec) {
        GenerateDataKeyRequest request = new GenerateDataKeyRequest()
            .withKeyId(kmsKeyId)
            .withKeySpec(keySpec); // "AES_256" or "AES_128"

        return kmsClient.generateDataKey(request);
    }
}

// Spring Vault integration for dynamic secrets
@Component
class VaultSecretManager {
    private final VaultTemplate vaultTemplate;

    public VaultSecretManager(VaultTemplate vaultTemplate) {
        this.vaultTemplate = vaultTemplate;
    }

    public String getSecret(String path, String key) {
        VaultResponse response = vaultTemplate.opsForKeyValue("secret",
            VaultKeyValueOperationsSupport.KeyValueBackend.KV_2).get(path);

        if (response != null && response.getData() != null) {
            return (String) response.getData().get(key);
        }
        throw new RuntimeException("Secret not found: " + path);
    }

    public void setSecret(String path, String key, String value) {
        java.util.Map<String, Object> data = new java.util.HashMap<>();
        data.put(key, value);
        vaultTemplate.opsForKeyValue("secret",
            VaultKeyValueOperationsSupport.KeyValueBackend.KV_2).put(path, data);
    }
}
```

#### Go: AWS KMS (aws-sdk-go-v2) + HashiCorp Vault

```go
// Go implementation - AWS KMS envelope encryption and Vault integration
// Dependencies: github.com/aws/aws-sdk-go-v2/service/kms, github.com/hashicorp/vault/api
package secrets

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"

    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/kms"
    "github.com/hashicorp/vault/api"
)

// KMSClient wraps AWS KMS for encryption operations
type KMSClient struct {
    client *kms.Client
    keyID  string
}

func NewKMSClient(ctx context.Context, keyID string) (*KMSClient, error) {
    cfg, err := config.LoadDefaultConfig(ctx)
    if err != nil {
        return nil, fmt.Errorf("load AWS config: %w", err)
    }
    return &KMSClient{
        client: kms.NewFromConfig(cfg),
        keyID:  keyID,
    }, nil
}

// Encrypt encrypts plaintext using AWS KMS
func (k *KMSClient) Encrypt(ctx context.Context, plaintext []byte) (string, error) {
    result, err := k.client.Encrypt(ctx, &kms.EncryptInput{
        KeyId:     aws.String(k.keyID),
        Plaintext: plaintext,
    })
    if err != nil {
        return "", fmt.Errorf("kms encrypt: %w", err)
    }
    return base64.StdEncoding.EncodeToString(result.CiphertextBlob), nil
}

// Decrypt decrypts ciphertext using AWS KMS
func (k *KMSClient) Decrypt(ctx context.Context, ciphertext string) ([]byte, error) {
    decoded, err := base64.StdEncoding.DecodeString(ciphertext)
    if err != nil {
        return nil, fmt.Errorf("decode base64: %w", err)
    }

    result, err := k.client.Decrypt(ctx, &kms.DecryptInput{
        CiphertextBlob: decoded,
    })
    if err != nil {
        return nil, fmt.Errorf("kms decrypt: %w", err)
    }
    return result.Plaintext, nil
}

// GenerateDataKey creates a new data key for envelope encryption
func (k *KMSClient) GenerateDataKey(ctx context.Context) (plaintext []byte, ciphertext []byte, err error) {
    result, err := k.client.GenerateDataKey(ctx, &kms.GenerateDataKeyInput{
        KeyId:   aws.String(k.keyID),
        KeySpec: "AES_256",
    })
    if err != nil {
        return nil, nil, fmt.Errorf("generate data key: %w", err)
    }
    return result.Plaintext, result.CiphertextBlob, nil
}

// VaultClient wraps HashiCorp Vault for secret storage
type VaultClient struct {
    client *api.Client
}

func NewVaultClient(address, token string) (*VaultClient, error) {
    config := &api.Config{
        Address: address,
    }
    client, err := api.NewClient(config)
    if err != nil {
        return nil, fmt.Errorf("create vault client: %w", err)
    }
    client.SetToken(token)
    return &VaultClient{client: client}, nil
}

// LoginWithAppRole authenticates using AppRole auth method
func (v *VaultClient) LoginWithAppRole(ctx context.Context, roleID, secretID string) error {
    data := map[string]interface{}{
        "role_id":   roleID,
        "secret_id": secretID,
    }
    secret, err := v.client.Logical().WriteWithContext(ctx, "auth/approle/login", data)
    if err != nil {
        return fmt.Errorf("vault approle login: %w", err)
    }
    v.client.SetToken(secret.Auth.ClientToken)
    log.Println("vault authentication successful")
    return nil
}

// GetSecret retrieves a secret from Vault KV store
func (v *VaultClient) GetSecret(ctx context.Context, path string) (map[string]interface{}, error) {
    secret, err := v.client.KVv2("secret").Get(ctx, path)
    if err != nil {
        return nil, fmt.Errorf("vault get secret: %w", err)
    }
    return secret.Data, nil
}

// SetSecret stores a secret in Vault KV store
func (v *VaultClient) SetSecret(ctx context.Context, path string, data map[string]interface{}) error {
    _, err := v.client.KVv2("secret").Put(ctx, path, data)
    if err != nil {
        return fmt.Errorf("vault set secret: %w", err)
    }
    return nil
}
```

#### Node.js: AWS SDK v3 KMS + node-vault

```javascript
// Node.js implementation - AWS KMS client (v3 SDK) and Vault integration
// Dependencies: @aws-sdk/client-kms, node-vault (npm install @aws-sdk/client-kms node-vault)
const { KMSClient, EncryptCommand, DecryptCommand, GenerateDataKeyCommand } = require('@aws-sdk/client-kms');

class KmsService {
    constructor(options = {}) {
        this.client = new KMSClient({
            region: options.region || process.env.AWS_REGION || 'us-east-1',
            ...(options.credentials && {
                credentials: options.credentials,
            }),
        });
        this.keyId = options.keyId || process.env.AWS_KMS_KEY_ID;
    }

    // Encrypt a plaintext string
    async encrypt(plaintext) {
        const command = new EncryptCommand({
            KeyId: this.keyId,
            Plaintext: Buffer.from(plaintext, 'utf-8'),
        });
        const response = await this.client.send(command);
        return response.CiphertextBlob.toString('base64');
    }

    // Decrypt a base64-encoded ciphertext
    async decrypt(ciphertext) {
        const command = new DecryptCommand({
            CiphertextBlob: Buffer.from(ciphertext, 'base64'),
        });
        const response = await this.client.send(command);
        return Buffer.from(response.Plaintext).toString('utf-8');
    }

    // Generate a data key for envelope encryption
    async generateDataKey(keySpec = 'AES_256') {
        const command = new GenerateDataKeyCommand({
            KeyId: this.keyId,
            KeySpec: keySpec,
        });
        const response = await this.client.send(command);
        return {
            plaintext: Buffer.from(response.Plaintext).toString('base64'),
            ciphertext: Buffer.from(response.CiphertextBlob).toString('base64'),
        };
    }

    // Envelope encrypt: generate data key, encrypt data locally, return wrapped key
    async envelopeEncrypt(plaintext) {
        const { createCipheriv } = require('crypto');
        const dataKey = await this.generateDataKey('AES_256');
        const plaintextKey = Buffer.from(dataKey.plaintext, 'base64');

        const iv = require('crypto').randomBytes(12);
        const cipher = createCipheriv('aes-256-gcm', plaintextKey, iv);

        const encrypted = Buffer.concat([
            cipher.update(plaintext, 'utf-8'),
            cipher.final(),
        ]);
        const authTag = cipher.getAuthTag();

        return {
            encryptedData: encrypted.toString('base64'),
            iv: iv.toString('base64'),
            authTag: authTag.toString('base64'),
            wrappedKey: dataKey.ciphertext,
        };
    }

    // Envelope decrypt: unwrap data key with KMS, then decrypt locally
    async envelopeDecrypt(envelope) {
        const { createDecipheriv } = require('crypto');
        const { plaintext: plaintextKey } = await this.decrypt(envelope.wrappedKey);

        const iv = Buffer.from(envelope.iv, 'base64');
        const authTag = Buffer.from(envelope.authTag, 'base64');
        const encryptedData = Buffer.from(envelope.encryptedData, 'base64');

        const decipher = createDecipheriv('aes-256-gcm', Buffer.from(plaintextKey), iv);
        decipher.setAuthTag(authTag);

        return decipher.update(encryptedData, null, 'utf-8') + decipher.final('utf-8');
    }
}

// Vault integration using node-vault
const vault = require('node-vault')({
    apiVersion: 'v1',
    endpoint: process.env.VAULT_ADDR || 'http://127.0.0.1:8200',
    token: process.env.VAULT_TOKEN,
});

class VaultSecretManager {
    constructor(vaultClient) {
        this.vault = vaultClient;
    }

    // Authenticate using AppRole
    async loginWithAppRole(roleId, secretId) {
        const result = await this.vault.approleLogin({
            role_id: roleId,
            secret_id: secretId,
        });
        this.vault.token = result.auth.client_token;
        console.log('Vault authentication successful');
    }

    // Read a secret from KV v2 store
    async getSecret(path) {
        const result = await this.vault.read(`secret/data/${path}`);
        return result.data.data;
    }

    // Write a secret to KV v2 store
    async setSecret(path, data) {
        await this.vault.write(`secret/data/${path}`, { data });
    }

    // Delete a secret
    async deleteSecret(path) {
        await this.vault.delete(`secret/data/${path}`);
    }

    // Generate dynamic database credentials
    async generateDatabaseCredentials(roleName) {
        const result = await this.vault.read(`database/creds/${roleName}`);
        return {
            username: result.data.username,
            password: result.data.password,
            leaseId: result.lease_id,
            leaseDuration: result.lease_duration,
        };
    }
}

// Usage
async function main() {
    const kms = new KmsService({ keyId: 'arn:aws:kms:us-east-1:123456789012:key/abc-123' });
    const encrypted = await kms.encrypt('sensitive-data');
    const decrypted = await kms.decrypt(encrypted);
    console.log('Decrypted:', decrypted);

    const vault = new VaultSecretManager();
    await vault.setSecret('myapp/db', {
        host: 'prod-db.example.com',
        password: 's3cr3t',
    });
    const secret = await vault.getSecret('myapp/db');
    console.log('DB password:', secret.password);
}

main().catch(console.error);
```

## Best Practices

### 密钥管理原则

1. **最小权限**
   - 只授予必需的权限
   - 定期审查权限

2. **密钥分离**
   - 不同环境使用不同密钥
   - 不同服务使用不同密钥

3. **定期轮换**
   - 自动轮换高敏感密钥
   - 手动轮换其他密钥

4. **完整审计**
   - 记录所有访问
   - 监控异常行为

### 密钥存储原则

1. **不存储明文**
   - 使用加密存储
   - 内存中解密

2. **安全传输**
   - 使用 TLS
   - 验证证书

3. **访问控制**
   - 基于角色
   - 基于属性

## Toolchain

### 密钥管理工具

| 工具 | 用途 |
|------|------|
| HashiCorp Vault | 通用密钥管理 |
| AWS Secrets Manager | AWS 密钥管理 |
| Azure Key Vault | Azure 密钥管理 |
| CyberArk | 企业密钥管理 |
| 1Password | 团队密钥共享 |

### 安全工具

| 工具 | 用途 |
|------|------|
| Vault Agent | 密钥注入 |
| Sops | 密钥加密管理 |
| envconsul | 环境变量注入 |

## Associated Assets

- **Scenario**: `../../scenarios/manage-secrets/SCENARIO.md`
- **Instruction**: `../../instructions/manage-secrets.instructions.md`
- **Prompt**: `../../prompts/manage-secrets.prompt.md`
- **Agent**: `../../agents/manage-secrets.agent.md`


## Core Knowledge

> Essential knowledge domain for manage-secrets execution.

### Domain Fundamentals
- **Secret Zero Problem**: 管理密钥系统本身的初始密钥如何安全传递的经典问题，需通过多因子认证或带外方式解决。
- **动态密钥 vs 静态密钥**: 动态密钥有生命周期自动过期(如 Vault 生成的 DB 凭证)，静态密钥长期有效需手动轮转。
- **密钥轮转策略**: 定义密钥更换频率和方式，包括手动轮转、定时自动轮转和事件驱动轮转三种模式。

### Key Principles
1. **密钥不入代码仓库**: 密钥绝对不可硬编码在源码、配置文件或 CI 脚本中，必须通过密钥管理服务注入。
2. **最小暴露面**: 每个服务仅能访问其需要的密钥，严格执行最小权限原则，减少泄露风险面。
3. **定期自动轮转**: 所有密钥必须设定轮转周期，通过自动化工具实现到期前自动轮转，避免人工遗忘。


## Best Practices

> Proven practices for manage-secrets excellence.

1. **Vault/HSM 集中管理**: 使用 HashiCorp Vault、AWS KMS 或 Azure Key Vault 等集中式密钥管理服务，统一管理密钥生命周期、访问审计和轮转策略。
2. **临时凭证优先于长期密钥**: 尽可能使用动态凭证（如 Vault 生成的数据库凭证、AWS STS 临时令牌），减少长期密钥泄露风险。
3. **密钥访问审计日志**: 所有密钥访问操作必须记录审计日志，包括谁、何时、从哪访问了什么密钥，用于安全审计和异常检测。


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during manage-secrets execution.

### Pitfall 1: 默认密码不修改 (Default Credentials)
**Risk**: 部署后未修改默认密码，攻击者可轻易通过公开的默认凭据入侵系统。
**Prevention**: 部署流水线中强制密码修改检查，首次登录必须更换默认密码。
**Impact**: 系统在数小时内可能被自动化脚本攻破，数据泄露风险极高。

### Pitfall 2: 密钥硬编码在 CI 脚本中 (Secrets in CI Scripts)
**Risk**: 将密钥直接写在 GitHub Actions、Jenkinsfile 或环境变量中，日志泄露或仓库泄露后密钥即刻暴露。
**Prevention**: 使用 CI 平台的内置密钥管理功能（如 GitHub Secrets、Jenkins Credentials），运行时注入而非硬编码。
**Impact**: 密钥在 CI 日志中明文暴露，攻击者利用密钥横向移动，扩大安全事件范围。

### Pitfall 3: 轮转时忽视依赖方 (Rotation Without Notifying Dependents)
**Risk**: 轮转密钥后未通知或更新依赖该密钥的服务和应用，导致集成中断。
**Prevention**: 轮转前梳理密钥依赖关系图，轮转后验证所有依赖方都已更新为新密钥。
**Impact**: 服务间认证失败，业务流程中断，需紧急手动恢复，影响面广。
