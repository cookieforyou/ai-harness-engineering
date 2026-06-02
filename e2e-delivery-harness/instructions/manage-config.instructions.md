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


## Best Practices

> Industry-standard best practices for manage-config execution.

1. **Practice 1**: Externalize configuration from application code
2. **Practice 2**: Use environment-specific config with validation schemas
3. **Practice 3**: Track configuration changes with version control


## Error Handling

> Common error scenarios and resolution strategies for manage-config.

### Error Category 1
**Symptom**: Configuration is inconsistent across environments
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Sensitive values are hardcoded in source code
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


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
