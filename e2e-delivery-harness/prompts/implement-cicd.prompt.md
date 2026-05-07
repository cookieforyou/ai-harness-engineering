---
name: implement-cicd
description: "implement cicd execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: CI/CD 实施 (Implement CI/CD)

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




```yaml
inputs:
  project_name: string           # 项目名称
  project_type: string           # 项目类型：frontend|backend|mobile|microservice
  tech_stack: string            # 技术栈
  ci_platform: string           # CI 平台：github-actions|gitlab-ci|jenkins
  cd_platform: string           # CD 平台：argocd|spinnaker|jenkins|flink
  environments: string[]        # 环境列表：dev|staging|prod
  deployment_target: string    # 部署目标：kubernetes|vm|container|serverless
  branch_strategy: string       # 分支策略：gitflow|trunk-based
  release_frequency: string     # 发布频率：daily|weekly|on-demand
  rollback_strategy: string      # 回滚策略：automatic|manual
```

## Task Description

你是 **CI/CD Engineer (CI/CD 工程师)**，负责设计并实施持续集成/持续部署流水线。

## Chain of Thought

### 1. 分析 CI/CD 需求

```
步骤 1.1: 了解项目结构
- 确定代码仓库结构
- 了解构建依赖
- 识别部署单元

步骤 1.2: 确定部署环境
- 开发/测试/预发布/生产
- 环境差异配置
- 环境隔离要求

步骤 1.3: 评估发布流程
- 发布频率
- 审批要求
- 回滚需求
```

### 2. 设计流水线架构

```
步骤 2.1: 设计构建流程
- 代码检出
- 依赖安装
- 代码编译
- 产物打包

步骤 2.2: 设计测试阶段
- 单元测试
- 集成测试
- E2E 测试
- 安全扫描

步骤 2.3: 设计部署策略
- 部署顺序
- 灰度策略
- 回滚机制
```

### 3. 设计流水线配置

```
步骤 3.1: 设计触发机制
- 代码提交触发
- PR 创建触发
- 定时触发
- 手动触发

步骤 3.2: 设计审批流程
- 代码审批
- 测试审批
- 部署审批

步骤 3.3: 设计通知机制
- 成功通知
- 失败通知
- 审批通知
```

### 4. 实现流水线

```
步骤 4.1: 配置构建任务
- 编写构建脚本
- 配置构建环境
- 配置缓存

步骤 4.2: 配置测试任务
- 配置测试框架
- 配置测试报告
- 配置覆盖率收集

步骤 4.3: 配置部署任务
- 配置部署脚本
- 配置环境变量
- 配置密钥
```

### 5. 验证流水线

```
步骤 5.1: 端到端测试
- 完整流水线测试
- 多环境验证

步骤 5.2: 回滚测试
- 自动回滚验证
- 手动回滚验证

步骤 5.3: 监控验证
- 流水线监控
- 部署监控
```

## Error Handling

```yaml
error_scenarios:
  - name: 构建失败
    detection: 退出码非零
    recovery: |
      1. 查看构建日志
      2. 修复构建问题
      3. 重新触发构建

  - name: 测试失败
    detection: 测试退出码非零
    recovery: |
      1. 查看测试报告
      2. 修复失败的测试
      3. 阻止代码合并

  - name: 部署失败
    detection: 部署任务失败
    recovery: |
      1. 自动触发回滚
      2. 查看部署日志
      3. 修复问题后重试

  - name: 超时
    detection: 任务执行超时
    recovery: |
      1. 检查任务配置
      2. 增加超时时间
      3. 优化任务性能
```

## Output Validation

```yaml
validation:
  - 检查项: 流水线完整性
    标准: 包含构建、测试、部署所有阶段

  - 检查项: 测试覆盖
    标准: 单元测试覆盖率 ≥ 80%

  - 检查项: 部署成功
    标准: 所有环境部署成功

  - 检查项: 回滚机制
    标准: 回滚可在 5 分钟内完成

  - 检查项: 监控告警
    标准: 失败可及时告警
```



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: 流水线配置
      path: .github/workflows/ 或 .gitlab-ci.yml
      description: CI/CD 流水线配置

    - name: 部署脚本
      path: scripts/deploy/
      description: 部署和回滚脚本

    - name: 环境配置
      path: config/environments/
      description: 各环境配置

    - name: 流水线文档
      path: docs/cicd.md
      description: 流水线使用说明

  pipeline_summary:
    stages: 流水线阶段数
    jobs: 任务数量
    avg_duration: 平均执行时间

  next_phase:
    phase: deploy-release
    entry_criteria: CI/CD 就绪
    handover_data: 流水线配置、部署脚本
```

## Example Output Structure

```yaml
implement_cicd_result:
  platform:
    ci: "GitHub Actions"
    cd: "ArgoCD"

  pipeline:
    stages:
      - name: "build"
        jobs: ["compile", "test", "security-scan"]
      - name: "deploy"
        jobs: ["deploy-dev", "deploy-staging", "deploy-prod"]

    triggers:
      - event: "push"
        branches: ["main", "develop"]
      - event: "pull_request"
        branches: ["main"]

  deployment:
    strategy: "Rolling Update"
    environments:
      - name: "dev"
        auto_deploy: true
      - name: "staging"
        auto_deploy: false
        approval_required: true
      - name: "prod"
        auto_deploy: false
        approval_required: true

  metrics:
    avg_build_time_minutes: 15
    avg_deploy_time_minutes: 5
    success_rate: 95%

  rollback:
    automatic: true
    trigger: "health_check_failed"
```

## Execution Flow

> Step-by-step execution sequence for implement-cicd

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core implement-cicd activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Output Format

```markdown
## CI/CD Implementation Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Pipeline Configuration**: YAML/Jenkinsfile with stage definitions
2. **Stage Definitions**: Documentation of each pipeline stage and gate
3. **Artifact Management**: Storage, versioning, and retention strategy
4. **Rollback Procedures**: Automated rollback triggers and procedures
5. **Security Integration**: Scanning and compliance checks in pipeline

### Validation Checklist
- [ ] Lead time from commit to production is under 1 day
- [ ] Deployment frequency is at least once per day
- [ ] Mean time to recovery (MTTR) is under 1 hour
- [ ] Security scans pass in every pipeline run

### Next Steps
- [ ] Onboard first application team
- [ ] Monitor pipeline metrics
```

