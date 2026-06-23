---
name: manage-config
description: "Detailed technical instructions for manage-config scenario execution"
applyTo: "scenarios/manage-config/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 配置管理 (Manage Configuration)

## Configuration Center Selection

### 主流配置中心对比

| 特性 | Apollo | Nacos | Consul | Spring Cloud Config |
|------|--------|-------|--------|-------------------|
| 多语言支持 | 通用 | 通用 | 通用 | Java 专用 |
| 配置推送 | 长轮询 | 长轮询/HTTP | HTTP | 需配合 Bus |
| 管理界面 | 完善 | 完善 | 基础 | 无（需自建） |
| 高可用 | 支持 | 支持 | 支持 | 需配合 Eureka |
| 权限管理 | 完善 | 基础 | 基础 | 无 |

### 配置中心部署架构

```
                    ┌──────────────┐
                    │   Client     │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Config API  │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
   │ Config1 │        │ Config2 │        │ Config3 │
   │ (Leader)│◄──────►│ (Follow)│◄──────►│ (Follow)│
   └─────────┘        └─────────┘        └─────────┘
        │                                     │
        └─────────────────┬───────────────────┘
                          │
                   ┌──────▼──────┐
                   │  Database   │
                   └─────────────┘
```

## Configuration Layering Standards

### 分层结构

```yaml
# 配置分层
layers:
  - name: "Global"
    priority: 1
    description: "全局默认配置"
    editable: false

  - name: "Cluster"
    priority: 2
    description: "集群级别配置"
    editable: true

  - name: "Namespace"
    priority: 3
    description: "命名空间配置"
    editable: true

  - name: "Application"
    priority: 4
    description: "应用级别配置"
    editable: true

  - name: "Local"
    priority: 5
    description: "本地覆盖配置"
    editable: false
```

### 命名空间设计

```yaml
namespaces:
  - name: "application"
    type: "private"
    description: "应用核心配置"

  - name: "database"
    type: "private"
    description: "数据库配置"

  - name: "redis"
    type: "private"
    description: "缓存配置"

  - name: "mq"
    type: "private"
    description: "消息队列配置"

  - name: "feature"
    type: "private"
    description: "特性开关配置"
```

## Configuration Format Standards

### YAML 配置示例

```yaml
# application.yml
server:
  port: 8080
  servlet:
    context-path: /api

spring:
  application:
    name: user-service

database:
  host: ${DB_HOST}
  port: ${DB_PORT:3306}
  name: ${DB_NAME}
  username: ${DB_USERNAME}
  password: ${DB_PASSWORD:encrypted}  # 加密存储

redis:
  host: ${REDIS_HOST}
  port: ${REDIS_PORT:6379}
  password: ${REDIS_PASSWORD:encrypted}

feature:
  new_ui: ${FEATURE_NEW_UI:false}
  beta_api: ${FEATURE_BETA_API:false}
```

### 环境特定配置

```yaml
# application-dev.yml
database:
  host: {{db_host}}
  url: jdbc:mysql://{{db_host}}:{{db_port}}/users

# application-prod.yml
database:
  host: ${DB_HOST}
  url: jdbc:mysql://{{db_host}}:{{db_port}}/users

# application-staging.yml
database:
  host: staging.rds.com
  url: jdbc:mysql://{{db_host}}:{{db_port}}/{{db_name}}
```

## Sensitive Configuration Management

### 敏感配置分类

| 类型 | 示例 | 处理方式 |
|------|------|----------|
| 密码 | db.password, redis.password | 加密存储 |
| Token | api.token, access.key | 加密+访问控制 |
| 证书 | ssl.cert, private.key | 文件引用 |
| IP 白名单 | admin.ips | IP 限制 |

### 加密方案

```yaml
# 使用配置中心加密
sensitive_config:
  - key: "db.password"
    value: "cipher:xxxxx"  # 加密后的密文
    algorithm: "AES"

  - key: "redis.password"
    value: "cipher:xxxxx"
    algorithm: "AES"

# 使用密钥管理服务
kms_config:
  - key: "api.token"
    provider: "aliyun-kms"
    secret_id: "{{kms_secret_id}}"
```

### 访问控制矩阵

```yaml
access_control:
  prod_environment:
    read:
      - role: developer  # 仅查看
      - role: ops       # 可查看
    write:
      - role: lead      # 可修改
      - role: ops       # 可修改

  change_approval:
    enabled: true
    approvers:
      - role: lead
      - role: security-officer
```

## Feature Toggle Standards

### 开关命名

```yaml
# 命名规范: {module}_{feature}_{state}
feature_switches:
  - name: "user_new_ui"
    description: "新用户界面"
    type: "boolean"

  - name: "payment_limit_percent"
    description: "支付限额百分比"
    type: "percentage"

  - name: "payment_rollout_users"
    description: "灰度用户列表"
    type: "user_list"

  - name: "recommendation_algorithm"
    description: "推荐算法版本"
    type: "string"
```

### 开关管理策略

```yaml
switch_lifecycle:
  states:
    - name: "pending"
      description: "待上线"
    - name: "enabled"
      description: "已启用"
    - name: "disabled"
      description: "已禁用"
    - name: "archived"
      description: "已归档"

  transitions:
    - from: "pending"
      to: "enabled"
      requires: "测试通过"

    - from: "enabled"
      to: "disabled"
      requires: "业务确认"
```

## Configuration Change Process

### 变更流程

```
┌─────────────┐
│  创建变更   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  审批变更   │ ← DC: 是否需要审批？
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  执行变更   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  验证变更   │ ← 验证配置生效
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  记录审计   │
└─────────────┘
```

### 回滚策略

```yaml
rollback:
  enabled: true

  strategies:
    - name: "automatic"
      trigger: "健康检查失败"
      action: "回滚到上一版本"

    - name: "manual"
      trigger: "人工触发"
      action: "选择版本回滚"
```

## Monitoring and Alerting Standards

### 监控指标

| 指标 | 告警阈值 | 说明 |
|------|----------|------|
| 配置获取延迟 | > 100ms | 网络问题 |
| 配置同步延迟 | > 30s | 同步异常 |
| 节点配置不一致 | > 0 | 集群问题 |
| 未授权访问 | > 0 | 安全问题 |

### Alert Configuration

```yaml
alerts:
  - name: "config_sync_delay"
    condition: "sync_delay > 30s"
    severity: "warning"
    action: "notify_ops"

  - name: "unauthorized_access"
    condition: "count > 0"
    severity: "critical"
    action: "notify_security"

  - name: "config_missing"
    condition: "required_config not found"
    severity: "critical"
    action: "notify_lead"
```


## Overview

> High-level description of the manage-config execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the manage-config scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-config.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Multi-Language Code Examples

> Production-ready configuration code examples across multiple languages.

### Spring Cloud Config (Java)

Remote config server bootstrap with refresh scope and health checks.

```java
// bootstrap.yml -- loaded before application.yml
// spring:
//   cloud:
//     config:
//       uri: ${CONFIG_SERVER_URI:http://localhost:8888}
//       name: user-service
//       profile: ${SPRING_PROFILES_ACTIVE:dev}
//       label: main
//       fail-fast: true
//       retry:
//         initial-interval: 1000
//         multiplier: 1.5
//         max-attempts: 5

// AppConfig.java -- refresh-scoped configuration bean
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.context.annotation.Configuration;
import org.springframework.beans.factory.annotation.Value;
import jakarta.annotation.PostConstruct;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RefreshScope
@Configuration
public class AppConfig {

    private static final Logger log = LoggerFactory.getLogger(AppConfig.class);

    @Value("${database.host:localhost}")
    private String dbHost;

    @Value("${database.port:3306}")
    private int dbPort;

    @Value("${feature.new_ui:false}")
    private boolean newUiEnabled;

    @PostConstruct
    public void validate() {
        if (dbHost == null || dbHost.isBlank()) {
            throw new IllegalStateException("database.host is required");
        }
        log.info("Configuration loaded: db={}:{}, feature.new_ui={}",
                 dbHost, dbPort, newUiEnabled);
    }
}

// ConfigController.java -- expose refresh endpoint
import org.springframework.cloud.endpoint.RefreshEndpoint;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ConfigController {

    private final RefreshEndpoint refreshEndpoint;

    public ConfigController(RefreshEndpoint refreshEndpoint) {
        this.refreshEndpoint = refreshEndpoint;
    }

    @PostMapping("/actuator/refresh")
    public String refresh() {
        var changedKeys = refreshEndpoint.refresh();
        return "Refreshed keys: " + String.join(", ", changedKeys);
    }
}
```

### Go (Viper)

Configuration loading from file, environment variables, and remote config store with struct binding.

```go
package config

import (
    "fmt"
    "log"
    "strings"

    "github.com/spf13/viper"
)

// AppConfig holds all application configuration.
type AppConfig struct {
    Server   ServerConfig   `mapstructure:"server"`
    Database DatabaseConfig `mapstructure:"database"`
    Redis    RedisConfig    `mapstructure:"redis"`
    Feature  FeatureConfig  `mapstructure:"feature"`
}

type ServerConfig struct {
    Port        int    `mapstructure:"port"`
    ContextPath string `mapstructure:"context-path"`
}

type DatabaseConfig struct {
    Host     string `mapstructure:"host"`
    Port     int    `mapstructure:"port"`
    Name     string `mapstructure:"name"`
    Username string `mapstructure:"username"`
    Password string `mapstructure:"password"`
}

type RedisConfig struct {
    Host     string `mapstructure:"host"`
    Port     int    `mapstructure:"port"`
    Password string `mapstructure:"password"`
}

type FeatureConfig struct {
    NewUI   bool   `mapstructure:"new_ui"`
    BetaAPI string `mapstructure:"beta_api"`
}

// LoadConfig reads configuration from file, env, and remote source.
func LoadConfig(configPath, env string) (*AppConfig, error) {
    v := viper.New()

    // 1. Set defaults
    v.SetDefault("server.port", 8080)
    v.SetDefault("database.port", 3306)
    v.SetDefault("redis.port", 6379)
    v.SetDefault("feature.new_ui", false)

    // 2. Config file
    v.SetConfigName("application")
    v.SetConfigType("yaml")
    v.AddConfigPath(configPath)
    v.AddConfigPath("/etc/app/config/")

    // 3. Environment variables (APP_DATABASE_HOST -> database.host)
    v.SetEnvPrefix("APP")
    v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
    v.AutomaticEnv()

    // 4. Read config file (non-fatal; env overrides)
    if err := v.ReadInConfig(); err != nil {
        if _, ok := err.(viper.ConfigFileNotFoundError); ok {
            log.Println("No config file found, using env & defaults")
        } else {
            return nil, fmt.Errorf("failed to read config: %w", err)
        }
    }

    // 5. Remote config (Consul / etcd) -- optional
    remotePath := fmt.Sprintf("apps/user-service/%s", env)
    if err := v.AddRemoteProvider("consul", "localhost:8500", remotePath); err != nil {
        log.Printf("Remote config provider unavailable: %v", err)
    }

    // 6. Bind to struct
    var cfg AppConfig
    if err := v.Unmarshal(&cfg); err != nil {
        return nil, fmt.Errorf("unable to decode config: %w", err)
    }

    // 7. Validate required fields
    if cfg.Database.Host == "" {
        return nil, fmt.Errorf("DATABASE_HOST is required")
    }
    if cfg.Redis.Host == "" {
        return nil, fmt.Errorf("REDIS_HOST is required")
    }

    return &cfg, nil
}

// WatchConfig reloads the application when config changes on disk.
func WatchConfig(cfg *AppConfig, configPath string) {
    v := viper.New()
    v.AddConfigPath(configPath)
    v.SetConfigName("application")
    v.SetConfigType("yaml")

    v.WatchConfig()
    v.OnConfigChange(func(e viper.ConfigChangeEvent) {
        log.Printf("Config file changed: %s -- reloading", e.Key())
        if err := v.Unmarshal(cfg); err != nil {
            log.Printf("Failed to reload config: %v", err)
            return
        }
        log.Println("Configuration hot-reloaded successfully")
    })
}
```

### JavaScript (dotenv + convict)

Environment-based configuration with schema validation and strict mode.

```javascript
// config/index.js -- schema-driven configuration loader
const convict = require('convict');
const dotenv = require('dotenv');
const fs = require('fs');
const path = require('path');

const env = process.env.NODE_ENV || 'development';
const envFile = path.resolve(__dirname, `../.env.${env}`);

if (fs.existsSync(envFile)) {
  dotenv.config({ path: envFile });
} else {
  dotenv.config();
}

const schema = {
  env: {
    doc: 'Application environment',
    format: ['development', 'staging', 'production', 'test'],
    default: 'development',
    env: 'NODE_ENV',
  },
  server: {
    port: {
      doc: 'HTTP server port',
      format: 'port',
      default: 8080,
      env: 'SERVER_PORT',
    },
    contextPath: {
      doc: 'API base path',
      format: String,
      default: '/api',
      env: 'CONTEXT_PATH',
    },
  },
  database: {
    host: {
      doc: 'Database hostname',
      format: String,
      default: null,
      env: 'DB_HOST',
    },
    port: {
      doc: 'Database port',
      format: 'port',
      default: 3306,
      env: 'DB_PORT',
    },
    name: {
      doc: 'Database name',
      format: String,
      default: null,
      env: 'DB_NAME',
    },
    username: {
      doc: 'Database username',
      format: String,
      default: null,
      env: 'DB_USERNAME',
    },
    password: {
      doc: 'Database password',
      format: String,
      default: null,
      env: 'DB_PASSWORD',
      sensitive: true,
    },
  },
  redis: {
    host: {
      doc: 'Redis hostname',
      format: String,
      default: null,
      env: 'REDIS_HOST',
    },
    port: {
      doc: 'Redis port',
      format: 'port',
      default: 6379,
      env: 'REDIS_PORT',
    },
    password: {
      doc: 'Redis password',
      format: String,
      default: '',
      env: 'REDIS_PASSWORD',
      sensitive: true,
    },
  },
  feature: {
    newUI: {
      doc: 'Enable new UI',
      format: Boolean,
      default: false,
      env: 'FEATURE_NEW_UI',
    },
    betaAPI: {
      doc: 'Enable beta API',
      format: Boolean,
      default: false,
      env: 'FEATURE_BETA_API',
    },
  },
};

const config = convict(schema);

config.validate({ allowed: 'strict' });
console.log(`Configuration loaded for environment: ${config.get('env')}`);

const frozenConfig = Object.freeze({
  env: config.get('env'),
  server: Object.freeze(config.get('server')),
  database: Object.freeze(config.get('database')),
  redis: Object.freeze(config.get('redis')),
  feature: Object.freeze(config.get('feature')),
});

module.exports = frozenConfig;

// Usage:
// const config = require('./config');
// console.log(`Server starting on port ${config.server.port}`);
```


## Best Practices

> Industry-standard best practices for manage-config execution.

1. **Practice 1**: Externalize configuration from application code
2. **Practice 2**: Use environment-specific config with validation schemas
3. **Practice 3**: Track configuration changes with version control


## Error Handling

> Common error scenarios and resolution strategies for manage-config.

### Error Scenario 1: 配置漂移检测 (P1)

**触发条件**: 集群中部分节点的实际配置与配置中心记录的期望配置不一致，差异超过阈值。

**处理流程**:
```
IF config_drift_detected
  AND drift_count > threshold(5 nodes)
THEN
  1. 立即触发配置一致性审计，对比配置中心版本与各节点实际版本
  2. 使用配置同步工具 (如 Apollo OpenAPI / Consul CLI) 获取差异报告
  3. 分析漂移根因：网络分区、手动修改、灰度发布遗漏
  4. 执行配置同步：推送配置中心最新版本到漂移节点
  5. 验证漂移节点配置 hash 与配置中心一致
  6. 记录审计日志并通知配置管理员
END
```

**降级方案**: 如自动同步失败，启用配置快照回滚，将节点恢复到上一个已验证的版本。

**升级条件**: 漂移节点超过集群 30% 或涉及数据库/支付等关键配置，升级为 P0 事件。

### Error Scenario 2: 敏感配置泄露 (P0)

**触发条件**: 检测到明文密码/密钥被输出到日志、错误堆栈或暴露在配置管理界面。

**处理流程**:
```
IF secret_leak_detected
  AND leak_type IN (log_output, api_exposure, code_commit)
THEN
  1. 立即隔离泄露源：暂停相关服务实例的日志输出或下线暴露的 API
  2. 立即轮换所有涉及泄露的敏感配置值（密码/密钥/AK/SK）
  3. 扫描全量日志、Git 历史、APM 链路中的泄露痕迹
  4. 更新敏感配置策略：启用自动脱敏（log mask）和访问审计
  5. 评估泄露影响范围：确定泄露持续时间和可访问人员
  6. 报告安全负责人并生成安全事件报告
END
```

**降级方案**: 若无法立即轮换配置，启用紧急访问控制策略，限制对泄露配置的读取权限，同时使用临时密钥替代。

**升级条件**: 确认配置已被外部未授权方获取，立即升级为安全事件响应流程。

### Error Scenario 3: 配置热加载失败 (P1)

**触发条件**: 配置中心推送变更后，应用未能成功刷新配置，仍使用旧值运行。

**处理流程**:
```
IF hot_reload_failed
  AND retry_count > 3
THEN
  1. 检查配置中心到应用的网络连通性 (ping, telnet)
  2. 查看应用日志中的 RefreshScope 错误堆栈
  3. 验证配置变更格式：YAML/JSON 语法、数据类型兼容性
  4. 检查应用健康状态 (Spring Actuator / Health Endpoint)
  5. 手动触发配置刷新端点 (/actuator/refresh) 并对比结果
  6. 如仍失败，重启应用实例并验证配置加载
END
```

**降级方案**: 保持应用运行旧配置，通过配置回滚恢复到上一个已知正确的版本。

**升级条件**: 热加载失败导致功能异常或业务指标下降，升级为 P0 事件并启动服务重启流程。


## Quality Standards

> Acceptance criteria and quality gates for manage-config deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All configurations pass schema validation | Automated check |
| Standard 2 | Environment parity is 95% or higher | Automated check |
| Standard 3 | No hardcoded secrets in codebase | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
