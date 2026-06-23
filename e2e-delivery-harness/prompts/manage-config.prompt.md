---
name: manage-config
description: "manage config execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 配置管理 (Manage Configuration)

## Purpose

本提示词指导AI执行配置管理任务，按照业务需求设计并实现应用程序配置管理方案，确保配置正确、安全、可追溯。

### Key Objectives

- **准确理解配置需求**: 深入分析配置项分类、环境差异和敏感信息，确保配置方案满足业务需求
- **安全配置管理**: 实现敏感配置加密存储、最小权限访问控制和密钥轮换机制
- **配置一致性保障**: 确保各环境配置一致性，支持配置版本管理与回滚
- **变更可追溯**: 实现完整的配置变更审计日志和变更审批流程
- **规范交接准备**: 生成完整的配置清单、使用文档和运维手册

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `config_scope` | string | true | - | 配置范围: db\|redis\|mq\|app\|feature\|all | 非空字符串 |
| `environments` | array | true | - | 环境列表: dev\|staging\|prod | 非空字符串数组 |
| `secret_keys` | array | true | - | 敏感配置键列表(需加密) | 非空字符串数组 |
| `config_version` | string | false | "1.0.0" | 配置版本号 | 语义化版本格式 |
| `drift_threshold` | number | false | 5 | 配置漂移检测阈值(%) | 0-100的整数 |
| `audit_required` | boolean | true | - | 是否需要审计日志 | true/false |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的配置管理输入
config_scope: "all"
environments:
  - "dev"
  - "staging"
  - "prod"
secret_keys:
  - "db.password"
  - "redis.password"
  - "jwt.secret"
  - "api.key"
config_version: "2.1.0"
drift_threshold: 5
audit_required: true
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解配置管理需求和范围
   ├─ 输入: config_scope, environments, secret_keys
   ├─ 思考: 哪些配置项需要管理？哪些是敏感配置需要加密？
   ├─ 验证: 与业务需求对照，确认所有配置项已识别
   └─ 输出: 配置需求分析（配置清单、敏感分类、环境差异、约束条件）
   ↓
[ANALYZE] Step 2: 分析配置架构和技术方案
   ├─ 输入: 配置需求分析, environments, audit_required
   ├─ 思考: 配置分层如何设计？配置中心选型？权限模型如何规划？
   ├─ 验证: 方案满足多环境管理需求，审计能力完整
   └─ 输出: 配置架构方案（分层设计、配置中心选型、权限模型、审计方案）
   ↓
[DESIGN] Step 3: 设计配置结构和验证规则
   ├─ 输入: 配置架构方案, config_version, drift_threshold
   ├─ 思考: 配置Schema如何定义？验证规则如何设计？漂移检测如何实现？
   ├─ 验证: Schema覆盖所有配置项，验证规则完备，漂移阈值合理
   └─ 输出: 配置结构设计（Schema定义、验证规则、漂移检测、版本策略）
   ↓
[IMPLEMENT] Step 4: 实现配置管理方案
   ├─ 输入: 配置结构设计, secret_keys, environments
   ├─ 思考: 配置加载如何实现？敏感配置如何加密？变更通知如何集成？
   ├─ 验证: 配置加载正确，敏感配置已加密，审计日志可追溯
   └─ 输出: 配置代码 + 加密模块 + 访问控制 + 审计配置
   ↓
[VERIFY] Step 5: 验证配置正确性和一致性
   ├─ 输入: 配置管理实现, environments, drift_threshold
   ├─ 执行: 配置校验、环境一致性检查、漂移检测、回滚测试
   ├─ 验证: 配置校验100%通过，环境一致性≥99%，漂移检测正常
   └─ 输出: 配置验证报告（校验结果、一致性报告、漂移检测报告）
   ↓
[HANDOVER] Step 6: 准备交接给部署发布阶段
   ├─ 生成: Handover Context（配置清单、环境配置、审计报告）
   ├─ 更新: Global Context（配置状态、密钥轮换计划、已知问题）
   └─ 通知: Deploy-Release Agent（提交配置交接请求）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 配置获取失败

**识别信号**: 
- ConfigNotFound / ConnectionTimeout
- 应用程序启动时配置加载失败

**处理流程**:
```
IF 配置获取失败
THEN
  1. 使用本地缓存配置作为降级
  2. 尝试从次要来源获取配置
  3. 使用默认值（如安全可用）
  4. 告警通知运维团队
  5. 触发配置修复流程
END
```

**降级方案**: 使用本地缓存配置或安全默认值

**升级条件**: 关键配置（数据库连接等）获取失败，服务无法启动

---

### Error Scenario 2: 配置格式错误

**识别信号**: 
- ParseError / SchemaViolation
- 配置变更发现格式不正确

**处理流程**:
```
IF 配置格式错误
THEN
  1. 回退到变更前的有效配置版本
  2. 记录错误详情和配置变更内容
  3. 通知配置变更发起人
  4. 等待修正后重新提交
END
```

**降级方案**: 保持前一个有效版本，拒绝错误变更

**升级条件**: 错误配置已推送到生产环境并影响到线上服务

---

### Error Scenario 3: 配置中心不可用

**识别信号**: 
- ServiceUnavailable / ClusterDown
- 配置中心服务器异常

**处理流程**:
```
IF 配置中心不可用
THEN
  1. 降级到本地配置文件
  2. 启用只读模式（禁止配置变更）
  3. 自动触发高可用切换
  4. 告警通知SRE团队
  5. 定期探测配置中心恢复状态
END
```

**降级方案**: 使用本地缓存的配置文件，等待配置中心恢复

**升级条件**: 配置中心超过5分钟不可用，影响配置变更操作

---

### Error Scenario 4: 敏感配置泄露

**识别信号**: 
- SecurityAlert / AccessLogAnomaly
- 异常访问模式检测到

**处理流程**:
```
IF 敏感配置泄露
THEN
  1. 立即通知安全团队
  2. 轮换相关密钥和凭证
  3. 审计访问日志确定泄露范围
  4. 修复泄露源
  5. 更新安全策略防止再次发生
END
```

**降级方案**: 批量轮换所有受影响凭证，启用临时访问控制

**升级条件**: 核心系统凭证泄露，需要立即启动安全应急响应

---

### Error Scenario 5: 配置漂移异常

**识别信号**: 
- DriftDetected / ConfigMismatch
- 实际配置与期望配置不一致

**处理流程**:
```
IF 配置漂移异常
THEN
  1. 识别漂移的配置项和差异值
  2. 判断漂移是否在阈值{drift_threshold}%内
  3. 超出阈值则自动修复（回滚到期望配置）
  4. 记录漂移事件和修复操作
  5. 分析漂移根因（手动变更/自动恢复/部署异常）
END
```

**降级方案**: 自动同步期望配置覆盖漂移配置

**升级条件**: 配置漂移影响服务正常运行

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | CONFIG-VALID | =100% | (有效配置项数/总配置项数)×100% | Schema验证统计 | 30% |
| KPI-002 | ENV-PARITY | ≥99% | (一致配置项数/总配置项数)×100% | 环境对比检查 | 25% |
| KPI-003 | SECRETS-ISOLATION | =100% | (隔离机密数/总机密数)×100% | 安全审计扫描 | 25% |
| KPI-004 | DRIFT-DETECTION | ≥95% | (检测到的漂移数/实际漂移数)×100% | 定点检测验证 | 20% |

**综合评分计算**: 
```
Quality Score = (CONFIG-VALID×100) × 0.30 + (ENV-PARITY×100) × 0.25 + (SECRETS-ISOLATION×100) × 0.25 + (DRIFT-DETECTION×100) × 0.20
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Format (输出格式)

> AI必须按照以下结构生成配置管理交付物

```markdown
## Configuration Management Deliverables

### 1. Summary
- **Status**: completed / partial / blocked
- **Completion**: {percentage}
- **Quality Score**: {score}/100

### 2. Configuration Overview
- **Config Scope**: {config_scope}
- **Environments**: {environments}
- **Total Configurations**: {N}
- **Sensitive Configs**: {N} (encrypted)
- **Config Version**: {config_version}

### 3. Configuration Structure
| Environment | Config Source | Config Count | Sensitive Count |
|-------------|--------------|--------------|-----------------|
| dev | {source} | {N} | {N} |
| staging | {source} | {N} | {N} |
| prod | {source} | {N} | {N} |

### 4. Verification Results
- **Config Validation Pass Rate**: {X}% (target: 100%)
- **Environment Parity**: {X}% (target: ≥99%)
- **Secrets Isolation**: {X}% (target: 100%)
- **Drift Detection Rate**: {X}% (target: ≥95%)

### 5. Quality Score
- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - CONFIG-VALID: {value}% (target: 100%) - {pass/fail}
  - ENV-PARITY: {value}% (target: ≥99%) - {pass/fail}
  - SECRETS-ISOLATION: {value}% (target: 100%) - {pass/fail}
  - DRIFT-DETECTION: {value}% (target: ≥95%) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交前，必须完成以下验证步骤

### Validation Checklist

**V-001: Configuration Completeness (配置完整性验证)**
- [ ] 所有必需配置项已定义
- [ ] 各环境配置差异已明确标注
- [ ] 配置默认值和覆盖规则清晰

**V-002: Configuration Correctness (配置正确性验证)**
- [ ] 配置Schema验证全部通过
- [ ] 配置值在合法范围内
- [ ] 配置间引用关系正确

**V-003: Environment Consistency (环境一致性验证)**
- [ ] 环境间配置差异已明确定义
- [ ] 环境一致性 ≥ {drift_threshold}%
- [ ] 漂移检测机制已配置并可正常触发

**V-004: Secrets and Security (敏感信息安全验证)**
- [ ] 敏感配置已加密存储
- [ ] 敏感配置在日志中已脱敏
- [ ] 访问权限按最小权限原则配置

**V-005: Audit and Traceability (审计可追溯验证)**
- [ ] 配置变更有完整审计日志
- [ ] 配置变更可回滚到历史版本
- [ ] 变更审批流程已启用

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. 识别具体失败项和严重程度
  2. 尝试修复（基于可用信息）
  3. IF 无法修复 THEN 标记为 [NEEDS REVIEW] 并附详细说明
  4. 生成验证报告（每项pass/fail状态）
  5. 高亮关键问题
  6. IF 关键问题存在 THEN 不进行交接
END
```

## Handover Context (交接上下文)

> 完成配置管理任务后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "manage-config"
    to_stage: "deploy-release"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_configs: {{number}}
    sensitive_count: {{number}}
    environments: {{list}}

  artifacts:
    delivered:
      - name: "Configuration Schema"
        path: "config/schema/"
        version: "1.0.0"
      - name: "Environment Configs"
        path: "config/environments/"
        version: "1.0.0"
      - name: "Config Documentation"
        path: "docs/config-guide.md"
        version: "1.0.0"
      - name: "Audit Trail"
        path: "logs/config-audit/"
        version: "1.0.0"

  metrics:
    config_valid_rate: {{percentage}}
    env_parity_rate: {{percentage}}
    secrets_isolation_rate: {{percentage}}
    drift_detection_rate: {{percentage}}

  decisions:
    - id: "DC-001"
      description: "Configuration center selection"
      rationale: "Chose {center} for better {feature} support"
      alternatives_considered: ["{alt1}", "{alt2}"]
      impact: "Affects team workflow and tooling integration"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "{environment} config diff exceeds threshold"
        risk_level: "low"
        planned_resolution: "Sync configs in next maintenance window"

  risks:
    - id: "RISK-001"
      description: "Config drift in production may cause incidents"
      probability: "low"
      impact: "high"
      mitigation: "Automated drift detection and remediation"
      contingency_plan: "Rollback to last known good config version"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "CONFIG-VALID"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "ENV-PARITY"
        value: 99.5
        target: 99
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "SECRETS-ISOLATION"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "DRIFT-DETECTION"
        value: 98
        target: 95
        unit: "%"
        status: "pass"
    overall_score: 93
    grade: "excellent"

  recommendations:
    - "Schedule periodic config review and clean up unused configs"
    - "Set up config drift monitoring dashboard"
    - "Implement automated secrets rotation pipeline"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/manage-config/SCENARIO.md` | 配置管理场景定义 |
| Agent | `../agents/manage-config.agent.md` | 配置管理Agent角色 |
| Instruction | `../instructions/manage-config.instructions.md` | 配置管理技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Config Management Standards](../standards/config-management-standards.md) - 配置管理规范
  - [Security Guidelines](../standards/security-guidelines.md) - 安全配置指南
- **Templates**: 
  - [Config Schema Template](../templates/config-schema.template.md) - 配置Schema模板
- **Evaluations**: 
  - [Config Audit Checklist](../evaluations/config-audit-checklist.md) - 配置审计检查清单

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "manage-config"
    to_stage: "deploy-release"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "manage-config"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
