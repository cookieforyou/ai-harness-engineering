---
name: manage-config
description: "Domain skill for manage-config execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 配置管理 (Configuration Management)

## Overview

本 Skill 定义了配置管理的核心知识体系。

## Core Knowledge

### 配置类型

#### 按用途分类

```yaml
config_types:
  application:
    - server.port
    - logging.level
    - api.timeout

  database:
    - connection.url
    - connection.pool_size
    - connection.timeout

  cache:
    - redis.host
    - redis.ttl
    - cache.strategy

  feature_flags:
    - feature.enabled
    - feature.percentage
    - feature.rollout
```

#### 按生命周期分类

```
┌─────────────────────────────────────────────┐
│              Build-time Config              │
│  编译时确定，构建产物包含                    │
├─────────────────────────────────────────────┤
│              Deploy-time Config             │
│  部署时注入，环境变量/配置文件               │
├─────────────────────────────────────────────┤
│              Runtime Config                │
│  运行时可变，热更新                          │
└─────────────────────────────────────────────┘
```

### 配置加载顺序

```python
# Spring Boot 配置加载顺序
load_order = [
    "1. Spring Boot default config",
    "2. @PropertySource annotations",
    "3. Config application.yml (package resources)",
    "4. Config application-{profile}.yml",
    "5. OS environment variables",
    "6. Command line arguments",
    "7. @TestPropertySource (test only)"
]

# 后加载覆盖先加载
# 高优先级覆盖低优先级
```

### 配置一致性

#### 多实例配置同步

```python
class ConfigSync:
    """配置同步策略"""

    strategies = {
        "push": "配置中心主动推送",
        "pull": "客户端定期拉取",
        "hybrid": "推拉结合"
    }

    @staticmethod
    def validate_consistency(configs):
        """验证配置一致性"""
        unique = set(configs)
        if len(unique) > 1:
            return False, f"Found {len(unique)} different configs"
        return True, "All instances have same config"
```

### 敏感配置处理

#### 加密流程

```
                    ┌─────────────┐
                    │   明文配置   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  加密算法    │  AES-256-GCM
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  密文存储    │
                    └─────────────┘
                           │
                    ┌──────▼──────┐
                    │  运行时解密  │  KMS/HSM
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   明文使用   │
                    └─────────────┘
```

#### 密钥管理

```python
kms_providers = {
    "aws": "AWS KMS",
    "aliyun": "Aliyun KMS",
    "huawei": "Huawei KMS",
    "azure": "Azure Key Vault",
    "gcp": "GCP Cloud KMS"
}

# 密钥轮换策略
key_rotation = {
    "frequency": "90_days",
    "before_expiry": "30_days_warning",
    "grace_period": "7_days"
}
```

### 配置监控

#### 配置健康指标

```yaml
health_metrics:
  - name: "config_load_time"
    unit: "ms"
    target: "< 50"

  - name: "config_error_rate"
    unit: "percent"
    target: "< 0.01"

  - name: "config_sync_delay"
    unit: "seconds"
    target: "< 5"

  - name: "hot_config_updates"
    unit: "count"
    target: "> 0"
```

## Best Practices

### 配置命名规范

```yaml
# 推荐命名
good_names:
  - "database.connection.timeout"
  - "redis.cache.ttl.seconds"
  - "api.retry.max_attempts"

# 不推荐命名
bad_names:
  - "dbConnTO"           # 缩写不清晰
  - "redisTtl"           # 缺少命名空间
  - "apiRetry"           # 缺少层级
```

### 配置验证

```python
class ConfigValidator:
    """配置验证器"""

    def validate_all(self, config):
        results = []

        # Schema 验证
        schema_result = self.validate_schema(config)
        results.append(schema_result)

        # 类型验证
        type_result = self.validate_types(config)
        results.append(type_result)

        # 值域验证
        range_result = self.validate_ranges(config)
        results.append(range_result)

        # 依赖验证
        dep_result = self.validate_dependencies(config)
        results.append(dep_result)

        return all(results)

    def validate_schema(self, config):
        """验证配置结构"""
        required_fields = ["app.name", "app.version"]
        for field in required_fields:
            if field not in config:
                return False, f"Missing required field: {field}"
        return True, "Schema valid"

    def validate_ranges(self, config):
        """验证值域"""
        rules = {
            "server.port": (1, 65535),
            "cache.ttl": (0, 86400),
            "pool.size": (1, 100)
        }
        for key, (min_val, max_val) in rules.items():
            if key in config:
                val = config[key]
                if not (min_val <= val <= max_val):
                    return False, f"{key} value {val} out of range"
        return True, "Ranges valid"
```

## Toolchain

### 配置管理工具

| 工具 | 厂商 | 特点 |
|------|------|------|
| Apollo | 携程 | 功能完善、界面友好 |
| Nacos | 阿里 | 简单易用、集成性好 |
| Consul | HashiCorp | 服务发现+配置 |
| Spring Cloud Config | Spring | Spring 生态 |
| etcd | CNCF | Kubernetes 原生 |

### 配置同步工具

| 工具 | 用途 |
|------|------|
| etcd-sync | etcd 配置同步 |
| Consul-template | 配置模板化 |
| Spring Cloud Bus | Spring 配置刷新 |

## Associated Assets

- **Scenario**: `../../scenarios/manage-config/SCENARIO.md`
- **Instruction**: `../../instructions/manage-config.instructions.md`
- **Prompt**: `../../prompts/manage-config.prompt.md`
- **Agent**: `../../agents/manage-config.agent.md`


## Core Knowledge

> Essential knowledge domain for manage-config execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for manage-config excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during manage-config execution.

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
