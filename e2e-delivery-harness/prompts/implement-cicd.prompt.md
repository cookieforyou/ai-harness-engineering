---
name: implement-cicd
description: "implement cicd execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: CI/CD 实施 (Implement CI/CD)

## Purpose

本提示词指导AI执行CI/CD实施任务，按照项目需求设计并实现持续集成/持续部署流水线，提升交付效率和质量。

### Key Objectives

- **准确理解CI/CD需求**: 深入分析项目结构、部署环境和发布流程，确保流水线设计匹配团队工作流
- **高质量流水线设计**: 构建高效、可靠的CI/CD流水线，包含构建、测试、部署、回滚完整闭环
- **自动化质量门禁**: 集成代码检查、安全扫描、测试执行等质量门禁，确保发布质量
- **可观测性与监控**: 实现流水线运行监控、部署状态追踪和失败告警
- **规范交接准备**: 生成完整的流水线配置文档和运维手册

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `tech_stack` | string | true | - | 技术栈 | 有效的技术名称 |
| `ci_platform` | string | true | - | CI平台: github-actions\|gitlab-ci\|jenkins | 有效的CI平台 |
| `deploy_target` | string | true | - | 部署目标: kubernetes\|vm\|container\|serverless | 有效的部署目标 |
| `test_framework` | string | true | - | 测试框架: pytest\|jest\|JUnit | 与tech_stack兼容 |
| `quality_gates` | array | false | [] | 质量门禁配置列表 | 字符串数组 |
| `environments` | array | true | - | 环境列表: dev\|staging\|prod | 非空字符串数组 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的CI/CD实施输入
project_name: "订单服务"
tech_stack: "Java 17, Spring Boot 3.0"
ci_platform: "github-actions"
deploy_target: "kubernetes"
test_framework: "JUnit 5"
quality_gates:
  - "单元测试覆盖率 ≥ 80%"
  - "代码扫描无高危漏洞"
  - "构建产物安全签名"
environments:
  - "dev"
  - "staging"
  - "prod"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解CI/CD需求和项目上下文
   ├─ 输入: project_name, tech_stack, environments, quality_gates
   ├─ 思考: 项目结构如何？有哪些构建依赖？部署环境有哪些差异？
   ├─ 验证: 需求明确，部署策略与团队协作模式匹配
   └─ 输出: CI/CD需求分析（项目结构、环境架构、发布流程、约束清单）
   ↓
[ANALYZE] Step 2: 分析流水线架构和技术选型
   ├─ 输入: CI/CD需求分析, ci_platform, deploy_target
   ├─ 思考: CI/CD平台能力是否满足？部署策略如何选择？需要哪些集成？
   ├─ 验证: 架构设计合理，平台能力覆盖所有需求
   └─ 输出: 流水线架构方案（平台配置、阶段划分、部署策略、回滚机制）
   ↓
[DESIGN] Step 3: 设计流水线各阶段
   ├─ 输入: 流水线架构方案, test_framework, quality_gates
   ├─ 思考: 构建/测试/部署各阶段如何衔接？质量门禁如何设置？
   ├─ 验证: 阶段划分合理，门禁条件明确，审批流程完整
   └─ 输出: 流水线详细设计（阶段定义、门禁规则、审批流程、通知策略）
   ↓
[IMPLEMENT] Step 4: 实现流水线配置
   ├─ 输入: 流水线详细设计, ci_platform
   ├─ 思考: YAML/DSL配置如何编写？构建环境如何配置？密钥如何管理？
   ├─ 验证: 配置语法正确，环境变量和密钥安全存储
   └─ 输出: 流水线配置代码 + 构建脚本 + 部署脚本 + 密钥配置
   ↓
[INTEGRATE] Step 5: 集成测试和安全扫描
   ├─ 输入: 流水线配置, test_framework, quality_gates
   ├─ 思考: 测试阶段如何集成？安全扫描工具如何配置？
   ├─ 验证: 所有质量门禁在流水线中正确执行，报告生成完整
   └─ 输出: 集成配置 + 测试报告配置 + 安全扫描配置 + 通知模板
   ↓
[VERIFY] Step 6: 验证流水线完整性和稳定性
   ├─ 输入: 完整流水线配置
   ├─ 执行: 端到端流水线测试、回滚测试、多环境部署验证
   ├─ 验证: 流水线通过率≥95%，回滚在5分钟内完成，部署时间≤30min
   └─ 输出: 流水线验证报告（端到端测试结果、稳定性指标、性能指标）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 构建失败

**识别信号**: 
- 退出码非零
- 编译错误/依赖下载失败

**处理流程**:
```
IF 构建失败
THEN
  1. 查看构建日志确定失败原因
  2. 修复构建配置或代码问题
  3. 重新触发构建
  4. IF 持续失败 THEN 通知开发团队
END
```

**降级方案**: 回退到上次成功构建配置

**升级条件**: 构建环境问题或基础设施故障

---

### Error Scenario 2: 测试失败

**识别信号**: 
- 测试退出码非零
- 覆盖率未达标

**处理流程**:
```
IF 测试失败
THEN
  1. 查看测试报告确定失败用例
  2. 修复失败的测试或配置
  3. 阻止代码合入主分支（门禁策略）
  4. 通知相关开发人员
END
```

**降级方案**: 允许低优先级测试跳过，但核心测试必须通过

**升级条件**: 核心测试全部失败，表明集成问题

---

### Error Scenario 3: 部署失败

**识别信号**: 
- 部署任务失败（健康检查失败/滚动更新中断）
- 部署后服务不可用

**处理流程**:
```
IF 部署失败
THEN
  1. 自动触发回滚到上一版本
  2. 查看部署日志确定失败原因
  3. 修复问题后重新部署
  4. 记录部署失败事件
END
```

**降级方案**: 保持当前版本不变，手动执行部署步骤

**升级条件**: 自动回滚也失败，需要人工介入

---

### Error Scenario 4: 流水线超时

**识别信号**: 
- 任务执行超时
- 流水线运行时间超过预期

**处理流程**:
```
IF 流水线超时
THEN
  1. 检查各阶段耗时分布
  2. 优化瓶颈阶段（测试并行化/构建缓存）
  3. 增加超时配置（如必要）
  4. 考虑拆分大型流水线
END
```

**降级方案**: 跳过非关键阶段（如性能测试）

**升级条件**: 基础构建操作超时，表明基础设施问题

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | LEAD-TIME | ≤24h | 从代码提交到生产部署的平均时间 | CI/CD系统度量 | 25% |
| KPI-002 | DEPLOY-FREQ | ≥1次/天 | 每日生产部署次数 | 部署记录统计 | 25% |
| KPI-003 | MTTR | ≤30min | 从故障识别到恢复的平均时间 | 事件记录统计 | 25% |
| KPI-004 | PIPELINE-STABILITY | ≥95% | (成功流水线数/总触发数)×100% | 流水线运行统计 | 25% |

**综合评分计算**: 
```
Quality Score = (LEAD-TIME达标?分数) × 0.25 + (DEPLOY-FREQ达标?分数) × 0.25 + (MTTR达标?分数) × 0.25 + (PIPELINE-STABILITY×100) × 0.25
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Format (输出格式)

> AI必须按照以下结构生成CI/CD实施交付物

```markdown
## CI/CD Implementation Deliverables

### 1. Summary
- **Status**: completed / partial / blocked
- **Completion**: {percentage}
- **Quality Score**: {score}/100

### 2. Pipeline Architecture
- **CI Platform**: {ci_platform}
- **Deploy Target**: {deploy_target}
- **Total Stages**: {N}
- **Total Jobs**: {N}
- **Estimated Run Time**: {X} min

### 3. Pipeline Stages
| Stage | Jobs | Trigger | Estimated Time |
|-------|------|---------|----------------|
| Build | {compile, test, scan} | push | {X} min |
| Deploy | {deploy-dev, deploy-staging} | PR merge | {X} min |
| Release | {deploy-prod} | manual | {X} min |

### 4. Quality Gates
| Gate | Check | Threshold | Action on Failure |
|------|-------|-----------|-------------------|
| G-001 | Unit Test Coverage | ≥80% | Block merge |
| G-002 | Security Scan | No critical | Block merge |

### 5. Verification Results
- **Lead Time**: {X}h (target: ≤24h)
- **Deploy Frequency**: {X}/day (target: ≥1/day)
- **MTTR**: {X}min (target: ≤30min)
- **Pipeline Stability**: {X}% (target: ≥95%)

### 6. Quality Score
- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - LEAD-TIME: {value}h (target: ≤24h) - {pass/fail}
  - DEPLOY-FREQ: {value}/day (target: ≥1/day) - {pass/fail}
  - MTTR: {value}min (target: ≤30min) - {pass/fail}
  - PIPELINE-STABILITY: {value}% (target: ≥95%) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交前，必须完成以下验证步骤

### Validation Checklist

**V-001: Pipeline Completeness (流水线完整性验证)**
- [ ] 流水线包含构建、测试、部署所有核心阶段
- [ ] 所有环境部署配置已完成
- [ ] 回滚机制已配置并可正常工作

**V-002: Quality Gates (质量门禁验证)**
- [ ] 单元测试覆盖率门禁已配置（≥80%）
- [ ] 代码安全扫描已集成
- [ ] 构建产物完整性校验已配置

**V-003: Deployment Strategy (部署策略验证)**
- [ ] 部署策略合理（滚动更新/蓝绿部署/灰度发布）
- [ ] 回滚机制经过验证
- [ ] 部署后健康检查已配置

**V-004: Security and Secrets (安全与密钥验证)**
- [ ] 密钥安全存储，无明文暴露
- [ ] 最小权限原则实施
- [ ] 流水线日志不泄露敏感信息

**V-005: Monitoring and Notifications (监控与通知验证)**
- [ ] 流水线运行监控已配置
- [ ] 失败通知及时发送给相关人员
- [ ] 部署状态可追溯

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

> 完成CI/CD实施任务后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "implement-cicd"
    to_stage: "deploy-release"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    pipeline_stages: {{number}}
    pipeline_jobs: {{number}}
    avg_duration_minutes: {{number}}

  artifacts:
    delivered:
      - name: "Pipeline Configuration"
        path: ".github/workflows/"
        version: "1.0.0"
      - name: "Deployment Scripts"
        path: "scripts/deploy/"
        version: "1.0.0"
      - name: "Environment Config"
        path: "config/environments/"
        version: "1.0.0"
      - name: "Pipeline Documentation"
        path: "docs/cicd.md"
        version: "1.0.0"

  metrics:
    lead_time_hours: {{number}}
    deploy_frequency_per_day: {{number}}
    mttr_minutes: {{number}}
    pipeline_success_rate: {{percentage}}

  decisions:
    - id: "DC-001"
      description: "CI/CD platform selection"
      rationale: "Chose {platform} for better ecosystem integration"
      alternatives_considered: ["{alt1}", "{alt2}"]
      impact: "Affects team workflow and tooling"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Performance test stage not configured"
        risk_level: "low"
        planned_resolution: "Add performance test in phase 2"

  risks:
    - id: "RISK-001"
      description: "Pipeline secrets rotation"
      probability: "low"
      impact: "high"
      mitigation: "Automated secrets rotation configured"
      contingency_plan: "Manual rotation procedure documented"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "LEAD-TIME"
        value: 12
        target: 24
        unit: "h"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "DEPLOY-FREQ"
        value: 3
        target: 1
        unit: "/day"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "MTTR"
        value: 20
        target: 30
        unit: "min"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "PIPELINE-STABILITY"
        value: 97
        target: 95
        unit: "%"
        status: "pass"
    overall_score: 92
    grade: "excellent"

  recommendations:
    - "Monitor pipeline metrics to identify optimization opportunities"
    - "Add performance and security stages in next iteration"
    - "Set up pipeline cost tracking for cloud resources"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/implement-cicd/SCENARIO.md` | CI/CD实施场景定义 |
| Agent | `../agents/implement-cicd.agent.md` | CI/CD工程师Agent角色 |
| Instruction | `../instructions/implement-cicd.instructions.md` | CI/CD实施技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [CI/CD Standards](../standards/cicd-standards.md) - CI/CD流水线标准
  - [Git Workflow](../standards/git-workflow.md) - Git分支管理和提交规范
  - [Security Guidelines](../standards/security-guidelines.md) - 安全配置指南
- **Templates**: 
  - [CI/CD Config Template](../templates/cicd-config.template.md) - 流水线配置模板
- **Evaluations**: 
  - [Pipeline Maturity Assessment](../evaluations/pipeline-maturity-assessment.md) - 流水线成熟度评估

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "implement-cicd"
    to_stage: "deploy-release"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "implement-cicd"
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
