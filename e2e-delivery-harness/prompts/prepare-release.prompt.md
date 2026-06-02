---
name: prepare-release
description: "prepare release execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 发布准备 (Prepare Release)

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
  release_version: string         # 发布版本：v1.0.0
  release_type: string            # 发布类型：major|minor|patch|apply-hotfix
  release_scope: string           # 发布范围描述
  release_criteria: object        # 发布标准
    test_pass_rate: number        # 测试通过率 ≥ 95%
    coverage_rate: number         # 覆盖率 ≥ 80%
    no_critical_bugs: boolean     # 无严重 bug
  environments: string[]          # 目标环境：staging|prod
  release_window: object          # 发布时间窗口
    date: string                  # 日期
    start_time: string            # 开始时间
    duration: string             # 预计时长
  dependencies: string[]          # 关联系统列表
  stakeholders: string[]          # 干系人列表
  change_requests: string[]       # 变更单列表
```

## Task Description

你是 **Release Manager (发布经理)**，负责规划和管理版本发布。

## Chain of Thought

### 1. 分析发布需求

```
步骤 1.1: 确认发布内容
- 列出本次发布的功能
- 列出本次修复的 bug
- 列出基础设施变更

步骤 1.2: 评估影响范围
- 识别关联系统
- 评估数据迁移需求
- 评估配置变更

步骤 1.3: 确定发布时间
- 选择合适的发布窗口
- 评估风险时间
- 协调资源
```

### 2. 制定发布计划

```
步骤 2.1: 制定时间表
- 里程碑规划
- 任务分配
- 资源协调

步骤 2.2: 定义发布步骤
- 准备阶段
- 执行阶段
- 验证阶段
- 完成阶段

步骤 2.3: 准备回滚方案
- 回滚触发条件
- 回滚步骤
- 回滚验证
```

### 3. 设计发布流程

```
步骤 3.1: 定义检查点
- Pre-check: 发布前检查
- Go/No-Go: 发布决策
- Post-check: 发布后验证

步骤 3.2: 配置监控
- 定义关键指标
- 设置告警阈值
- 配置通知

步骤 3.3: 制定沟通计划
- 通知干系人
- 准备沟通模板
- 建立应急通道
```

### 4. 准备发布资源

```
步骤 4.1: 准备发布包
- 代码编译打包
- 镜像构建推送
- 配置打包

步骤 4.2: 准备数据库变更
- DDL 脚本
- 数据迁移脚本
- 回滚脚本

步骤 4.3: 准备文档
- 发布说明
- 变更记录
- 回滚手册
```

### 5. 验证发布就绪

```
步骤 5.1: 验证环境
- 环境可用性
- 资源就绪
- 依赖服务

步骤 5.2: 验证发布包
- 完整性检查
- 签名验证
- 版本确认

步骤 5.3: 演练回滚
- 回滚步骤演练
- 回滚时间测量
- 回滚验证确认
```

## Error Handling

```yaml
error_scenarios:
  - name: 发布包不完整
    detection: MD5/SHA256 校验失败
    recovery: |
      1. 重新构建发布包
      2. 重新校验
      3. 验证版本一致性

  - name: 依赖服务不可用
    detection: HealthCheck 失败
    recovery: |
      1. 确认依赖服务状态
      2. 评估影响范围
      3. 决定是否延迟发布

  - name: 回滚方案不可行
    detection: 回滚演练失败
    recovery: |
      1. 修复回滚方案
      2. 重新演练验证
      3. 或取消本次发布

  - name: 验证检查失败
    detection: Post-check 不通过
    recovery: |
      1. 分析失败原因
      2. 执行回滚
      3. 修复后重新发布
```

## Output Validation

```yaml
validation:
  - 检查项: 发布计划完整性
    标准: 包含时间表、任务、资源

  - 检查项: 发布评审通过
    标准: 所有评审项通过

  - 检查项: 回滚方案就绪
    标准: 回滚演练成功

  - 检查项: 监控配置正确
    标准: 关键指标已配置告警

  - 检查项: 沟通计划完成
    标准: 干系人已通知
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
    - name: 发布计划
      path: docs/release-plan.md
      description: 详细发布计划文档

    - name: 发布清单
      path: docs/release-checklist.md
      description: 发布执行检查清单

    - name: 回滚手册
      path: docs/rollback-guide.md
      description: 回滚操作手册

    - name: 发布通知
      path: docs/announcement.md
      description: 发布通知模板

  release_readiness:
    code_freeze: true
    test_passed: true
    review_approved: true
    rollback_tested: true
    stakeholders_notified: true

  next_phase:
    phase: deploy-release
    entry_criteria: 发布准备完成
    handover_data: 发布计划、回滚方案
```

## Example Output Structure

```yaml
prepare_release_result:
  release_info:
    version: "v2.1.0"
    type: "minor"
    date: "2024-01-20"
    time_window: "22:00-02:00"
    estimated_duration: "4h"

  scope:
    features:
      - "用户画像功能"
      - "推荐算法优化"
    bug_fixes:
      - "BUG-123: 登录超时"
      - "BUG-456: 支付失败"
    infra_changes:
      - "Redis 集群升级"

  release_plan:
    milestones:
      - name: "Code Freeze"
        time: "2024-01-18 18:00"
        status: "completed"

      - name: "Staging Deploy"
        time: "2024-01-19 22:00"
        status: "completed"

      - name: "Production Deploy"
        time: "2024-01-20 22:00"
        status: "pending"

  checklist:
    pre_release:
      - item: "测试用例全部通过"
        status: "done"
      - item: "代码评审完成"
        status: "done"
      - item: "发布评审通过"
        status: "done"

    release:
      - item: "发布包构建"
        status: "pending"
      - item: "数据库迁移"
        status: "pending"

    post_release:
      - item: "功能验证"
        status: "pending"
      - item: "监控检查"
        status: "pending"

  rollback_plan:
    trigger: "P0/P1 bug 或核心功能不可用"
    steps:
      - "停止新版本流量"
      - "执行数据库回滚"
      - "回退应用版本"
      - "验证回滚成功"
    estimated_time: "30 minutes"

  stakeholders:
    notified:
      - "产品团队"
      - "运维团队"
      - "客服团队"
    participants:
      - "研发负责人"
      - "运维负责人"
      - "测试负责人"
```

## Execution Flow

> Step-by-step execution sequence for prepare-release

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core prepare-release activities
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
## Release Preparation Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Release Package**: Build artifacts, configurations, and deployment scripts
2. **Release Notes**: User-facing and operations-facing change documentation
3. **Deployment Checklist**: Pre-deployment verification items
4. **Rollback Plan**: Tested rollback procedure and validation steps
5. **Communication Plan**: Notification schedule and audience targeting

### Validation Checklist
- [ ] Pre-release checklist completion is 100%
- [ ] Release notes accuracy is 98% or higher
- [ ] All required approvals are obtained and documented
- [ ] Rollback plan is tested and ready

### Next Steps
- [ ] Schedule deployment window
- [ ] Notify stakeholders of release timeline
```

