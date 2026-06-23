---
name: manage-config
description: "Domain skill for manage-config execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
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
- **12-Factor App 配置原则**: 应用配置与代码严格分离，配置通过环境变量注入而非硬编码在代码仓库中。同一份代码可以在不同环境(开发/测试/生产)通过不同的配置值运行，实现构建一次、多处部署的目标。
- **配置分层 (应用/环境/集群)**: 配置按照作用域分为应用层(代码内默认值)、环境层(dev/staging/prod差异)和集群层(多集群差异化)三个层次。上层配置覆盖下层默认值，层次化设计减少重复并提升灵活性。
- **Feature Toggle 模式**: 通过运行时配置开关控制功能是否对外可见或可用，无需重新部署即可控制功能发布节奏。Feature Toggle支持暗发布、A/B测试、灰度验证和即时熔断，是现代持续交付不可或缺的能力。

### Key Principles
1. **配置与代码分离**: 配置信息不应嵌入源代码或编译产物中，而应通过外部机制(环境变量、配置中心、Secrets服务)在运行时注入。分离部署确保同一构建物安全跨越不同环境，避免因配置差异导致的构建泛滥和敏感信息泄露。
2. **环境间配置独立**: 每个环境(开发、测试、预发、生产)拥有完全独立的配置实例，环境间不存在配置共享或继承链上的意外覆盖。独立性确保变更在一个环境的配置不会对其他环境造成影响，降低发布风险。
3. **变更可审计**: 所有配置变更必须有完整的操作记录，包括变更人、变更时间、变更内容和前后对比。可审计性支持问题定位、合规追溯和意外变更回滚，是配置管理治理的基础要求。


## Best Practices

> Proven practices for manage-config excellence.

1. **配置中心统一管理**: 使用专业配置中心(如Apollo、Nacos、Consul)集中管理所有环境的配置，提供Web界面变更、灰度发布、版本回溯和推送监控能力。配置中心取代散落的配置文件和手工编辑，实现配置变更的集中化、标准化和自动化。

2. **敏感配置加密存储**: 对数据库密码、API密钥、证书私钥等敏感配置项在存储和传输过程中强制加密。使用云KMS服务或HashiCorp Vault管理加密密钥，并在应用运行时解密使用，确保敏感信息静态度和传输态均受保护。

3. **配置变更回滚机制**: 每次配置变更自动生成版本快照，支持一键回滚到任意历史版本。回滚机制不仅还原配置值，同时触发关联服务的配置重载，确保回滚后系统状态与预期一致。定期清理过期版本以控制存储成本。

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during manage-config execution.

### Pitfall 1: 配置硬编码在代码中
**Risk**: 将环境相关的配置值直接写入源代码文件(如YAML、JSON、properties文件)，导致配置值随代码一起提交到版本控制系统。换环境时需要修改代码，增加了配置变更风险和部署复杂度。
**Prevention**: 严格遵守12-Factor App配置原则——代码中只使用配置变量的占位符或引用，通过环境变量或配置中心在运行时注入实际值。将不同环境的配置模板置于独立的配置仓库中管理。
**Impact**: 敏感信息通过版本控制历史泄露；环境间切换需要重新构建，打破了"构建一次、多处部署"的目标；配置变更需要走代码提交流程，降低了灵活性。

### Pitfall 2: 生产配置泄露到日志
**Risk**: 应用在启动日志、异常堆栈或调试输出中打印配置信息，特别是数据库连接串、API密钥等敏感内容。日志文件通常被聚合到集中式日志平台，访问权限管控可能弱于配置系统自身。
**Prevention**: 实现日志过滤器自动替换敏感字段(如密码、密钥、证书)为掩码(****)；在配置加载和写入日志时使用独立的脱敏层；定期扫描日志存储检查是否存在敏感信息泄露。
**Impact**: 敏感信息被开发和运维以外的角色(如审计人员、第三方支持)获得，导致安全合规违规；恶意攻击者通过日志分析获取配置信息，扩大攻击面。

### Pitfall 3: 多环境配置漂移
**Risk**: 随着时间推移，开发、测试、预发和生产环境之间的配置逐渐产生差异——开发环境添加了新配置项但生产环境未同步，或生产环境调整了阈值但开发环境未更新。配置差异导致"在我机器上能跑"的问题蔓延到跨环境。
**Prevention**: 使用配置中心统一管理并定期进行跨环境配置差异对比(如Apollo的Namespace对比功能)；建立配置同步策略——新配置项先应用于开发环境和测试环境验证，再推广到预发和生产环境；CI/CD管道中包含配置一致性检查步骤。
**Impact**: 环境差异导致的功能表现不一致增加调试时间；测试环境无法复现生产问题；未经充分验证的配置直接修改生产环境引发稳定性风险。
