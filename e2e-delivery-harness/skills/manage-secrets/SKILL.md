# Skill: 密钥管理 (Secrets Management)

## 概述

本 Skill 定义了密钥管理的核心知识体系。

## 核心知识

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

## 最佳实践

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

## 工具链

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

## 关联资产

- **Scenario**: `../../scenarios/manage-secrets/SCENARIO.md`
- **Instruction**: `../../instructions/manage-secrets.instructions.md`
- **Prompt**: `../../prompts/manage-secrets.prompt.md`
- **Agent**: `../../agents/security-engineer.agent.md`
