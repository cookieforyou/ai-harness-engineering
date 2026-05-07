---
name: implement-feature
description: 开发实现场景，按照任务清单完成代码开发、单元测试和文档更新
type: scenario
category: development
stage: development
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [development, coding, testing]
---

# Implement Feature - Development Scenario

## Purpose

按照任务清单完成代码开发、单元测试和文档更新，确保代码质量和交付进度。

**核心目标**:
- 根据任务规格完成功能代码实现
- 编写充分的单元测试保证代码质量
- 遵循编码规范和最佳实践
- 及时更新相关技术文档

**成功标准**:
- 所有验收标准均已满足
- 单元测试覆盖率 ≥80%
- 代码审查通过率 100%
- 无严重或阻塞性缺陷

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务需求和验收标准
   ├─ 输入: task_spec, acceptance_criteria
   ├─ 思考: 需求是否清晰？验收标准是否可测量？
   ├─ 验证: 与需求规格对照，确认无歧义
   └─ 输出: 任务理解备忘录
   ↓
Step 2: [ANALYZE] 分析技术方案和依赖关系
   ├─ 输入: 任务理解备忘录, design_reference
   ├─ 思考: 实现方案是否合理？是否有技术风险？
   ├─ 验证: 符合架构设计，依赖已明确
   └─ 输出: 技术实现方案
   ↓
Step 3: [DESIGN] 设计代码结构和接口
   ├─ 输入: 技术实现方案
   ├─ 思考: 类/函数结构如何设计？接口契约是什么？
   ├─ 验证: 符合SOLID原则，接口清晰
   └─ 输出: 代码结构设计
   ↓
Step 4: [IMPLEMENT] 编写代码和单元测试
   ├─ 输入: 代码结构设计
   ├─ 思考: 代码是否规范？测试是否充分？
   ├─ 验证: 遵循编码规范，测试覆盖核心逻辑
   └─ 输出: 源代码 + 单元测试
   ↓
Step 5: [VERIFY] 自检代码质量和测试覆盖
   ├─ 输入: 源代码, 单元测试
   ├─ 执行: 代码规范检查, 单元测试执行
   ├─ 验证: 无规范违规，测试全部通过
   └─ 输出: 自检报告 + 测试报告
   ↓
Step 6: [HANDOVER] 准备交接给测试验证阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context (代码库状态)
   └─ 通知: Verify Test Agent
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 验收标准清晰度 | 需求理解阶段 | 清晰/需澄清 | 是否可测量、无歧义 | 任务理解备忘录 |
| DC-002 | 技术方案选择 | 方案设计阶段 | 方案A/方案B/方案C | 复杂度、性能、可维护性 | 技术实现方案 |
| DC-003 | 代码规范冲突 | 编码实现阶段 | 团队规范/个人习惯 | 始终遵循团队统一规范 | 代码审查记录 |
| DC-004 | 测试覆盖策略 | 测试编写阶段 | 全覆盖/核心覆盖 | 基于风险评估和时间约束 | 测试计划文档 |
| DC-005 | 重构时机判断 | 发现代码异味时 | 立即重构/后续迭代 | 影响范围、紧急程度 | 技术债务记录 |
| DC-006 | 提交粒度控制 | 代码提交时 | 大提交/小步提交 | 优先小步提交便于追溯 | Git提交历史 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续开发 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 验收标准不清晰 (P1)

**识别信号**: 
- 验收标准存在模糊表述（如"用户友好"、"高性能"）
- 缺少量化指标
- 多个理解方式都合理

**处理流程**:
```
IF 验收标准模糊或有歧义
THEN
  1. 列出所有可能的理解方式
  2. 选择最合理的理解（基于行业标准和最佳实践）
  3. 在代码注释中明确说明假设条件
  4. 标记为 [需确认-验收标准]
  5. IF 影响核心功能实现 THEN 升级到产品经理
END
```

**降级方案**: 基于行业标准做出合理假设，明确标注待确认

**升级条件**: 影响核心功能实现或存在重大理解分歧

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "ambiguous_acceptance_criteria"
  description: "验收标准'{criteria}'存在歧义"
  action_taken: "采用{assumption}作为实现标准，已标注待确认"
  result: "continued_with_assumption"
```

---

### Error Scenario 2: 技术难点阻塞 (P0/P1)

**识别信号**: 
- 多次尝试仍无法解决的技术问题
- 缺少必要的技术知识或工具
- 第三方依赖存在兼容性问题

**处理流程**:
```
IF 遇到无法解决的技术问题
THEN
  1. 分析问题的根本原因（使用5 Whys方法）
  2. 搜索文档、社区资源寻找解决方案
  3. 尝试替代方案（最多3种）
  4. IF 仍无法解决 THEN 
       a. 记录详细的问题描述和尝试过程
       b. 升级到技术负责人
       c. 标记任务为 [阻塞-技术难点]
     END
END
```

**降级方案**: 实现简化版本或临时方案，标注技术债务

**升级条件**: 
- P0: 完全阻塞任务进展，超过2小时未解决
- P1: 影响核心功能，但有临时方案

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-002"
  timestamp: "{{ISO8601}}"
  level: "P0/P1"
  type: "technical_blocker"
  description: "技术问题：{问题描述}"
  attempts:
    - attempt_1: "{方案1} - 失败原因"
    - attempt_2: "{方案2} - 失败原因"
  action_taken: "已升级至技术负责人"
  result: "blocked_escalated"
```

---

### Error Scenario 3: 设计与实现不匹配 (P1)

**识别信号**: 
- 实现过程中发现设计文档存在缺陷
- 设计方案在实际编码中不可行
- 发现更好的实现方式

**处理流程**:
```
IF 发现设计与实现不匹配
THEN
  1. 分析差异的具体内容和影响范围
  2. 判断是设计问题还是实现问题
  3. 评估修改设计的成本 vs 调整实现的成本
  4. IF 需要修改设计 THEN
       a. 联系系统设计师讨论
       b. 提出改进建议
       c. 等待设计确认后继续
     ELSE
       a. 调整实现方案
       b. 记录偏离设计的原因
     END
END
```

**降级方案**: 记录设计偏差，在代码注释中说明原因

**升级条件**: 需要修改架构设计或影响多个模块

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-003"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "design_implementation_mismatch"
  description: "设计文档与实际实现存在偏差"
  impact: "影响范围描述"
  action_taken: "已联系系统设计师/已调整实现"
  result: "resolved/pending"
```

---

### Error Scenario 4: 测试覆盖率不达标 (P2)

**识别信号**: 
- 单元测试覆盖率 <80%
- 关键逻辑路径未覆盖
- 边界条件和异常场景缺失

**处理流程**:
```
IF 测试覆盖率不达标
THEN
  1. 识别未覆盖的代码路径
  2. 分析未覆盖原因（难以测试/时间不足/设计问题）
  3. 补充缺失的测试用例
  4. IF 仍无法达到目标 THEN
       a. 记录未覆盖区域和原因
       b. 评估风险等级
       c. 标记为 [部分覆盖-需后续完善]
     END
END
```

**降级方案**: 记录未覆盖区域和风险，承诺后续迭代完善

**升级条件**: 核心业务逻辑测试覆盖率 <60%

---

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | CODE-COVERAGE | ≥80% | (已覆盖行数/总行数) × 100% | 单元测试覆盖率报告 | 30% |
| KPI-002 | BUG-DENSITY | ≤0.5/KLOC | 缺陷数/(代码千行数) | 代码审查和测试发现 | 25% |
| KPI-003 | CYCLOMATIC | ≤15 | 平均圈复杂度 per 函数 | 静态代码分析工具 | 20% |
| KPI-004 | REVIEW-PASS | 100% | (一次通过审查的代码/总代码) × 100% | Code Review记录 | 25% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.20) + (KPI-004 × 0.25)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都已实现
- [ ] 所有验收标准都已满足
- [ ] 单元测试覆盖核心逻辑
- [ ] 代码注释完整清晰
- [ ] 相关文档已更新

**一致性验证 (Consistency)**:
- [ ] 代码风格与团队规范一致
- [ ] 命名规范统一
- [ ] 接口设计与架构文档一致
- [ ] 依赖关系合理无循环

**准确性验证 (Accuracy)**:
- [ ] 单元测试全部通过
- [ ] 无编译错误或警告
- [ ] 静态代码分析无严重问题
- [ ] 功能行为符合预期

**可执行性验证 (Executability)**:
- [ ] 代码可在目标环境运行
- [ ] 依赖项已正确配置
- [ ] 部署脚本可用
- [ ] 配置文件完整

**规范性验证 (Compliance)**:
- [ ] 遵循编码规范
- [ ] 安全最佳实践已应用
- [ ] 性能考虑已纳入
- [ ] 可访问性标准已满足

---

## Handover Criteria (交接标准)

### 准出条件

```
✅ 所有功能代码已完成并通过自检
✅ 单元测试覆盖率 ≥80%，核心逻辑100%覆盖
✅ 代码规范检查通过，无严重违规
✅ Code Review 已通过或已提交审查
✅ 接口文档已更新（如有API变更）
✅ 相关技术文档已同步
✅ Handover Context 已生成
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 源代码 | .java/.py/.js等 | src/ | v1.0.0 | 功能实现代码 |
| 单元测试 | test files | tests/ | v1.0.0 | 测试用例代码 |
| 测试报告 | HTML/XML | reports/test-report.html | - | 测试执行结果 |
| 代码覆盖率报告 | HTML | reports/coverage/index.html | - | 覆盖率详情 |
| 接口文档 | Markdown/YAML | docs/api-spec.md | v1.0.0 | API接口说明 |
| 变更记录 | Markdown | CHANGELOG.md | - | 本次变更说明 |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "development"
    to_stage: "testing"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_lines_added: {{number}}
    total_lines_modified: {{number}}
    files_changed: {{number}}
    
  artifacts:
    delivered:
      - name: "Feature Implementation"
        path: "src/{feature_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Unit Tests"
        path: "tests/{test_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Test Report"
        path: "reports/test-report.html"
        version: "1.0.0"
        
  decisions:
    - id: "DC-001"
      description: "技术方案选择"
      rationale: "选择方案A因为性能更优"
      alternatives_considered: ["方案B", "方案C"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "边缘场景X的测试覆盖不足"
        planned_resolution: "下个迭代补充"
        
  risks:
    - id: "RISK-001"
      description: "新功能依赖的第三方库版本较新"
      probability: "low"
      impact: "medium"
      mitigation: "已在测试环境验证兼容性"
      
  recommendations:
    - "重点测试边界条件和异常场景"
    - "关注性能敏感区域的测试"
    - "验证与现有功能的集成"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "CODE-COVERAGE"
        value: 85
        target: 80
        status: "pass"
      - kpi_id: "KPI-002"
        name: "BUG-DENSITY"
        value: 0.3
        target: 0.5
        status: "pass"
      - kpi_id: "KPI-003"
        name: "CYCLOMATIC"
        value: 12
        target: 15
        status: "pass"
      - kpi_id: "KPI-004"
        name: "REVIEW-PASS"
        value: 100
        target: 100
        status: "pass"
    overall_score: 92
    grade: "excellent"
```

---

## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| **Agent** | `../../agents/implement-feature.agent.md` | 开发实现角色定义 |
| **Prompt** | `../../prompts/implement-feature.prompt.md` | 功能实现执行提示词 |
| **Instruction** | `../../instructions/implement-feature.instructions.md` | 开发实现技术指令 |
| **Skill** | `../../skills/implement-feature/SKILL.md` | 功能实现领域技能 |

---

## Prerequisites

### Required Preconditions

1. ✅ 任务分解已完成 (decompose-task 场景输出)
2. ✅ 技术方案已确认 (design-system 场景输出)
3. ✅ 接口定义已明确
4. ✅ 开发环境已就绪
5. ✅ 代码仓库访问权限已获得

### Expected Input

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `task_id` | string | true | - | 任务唯一标识符 | 非空字符串 |
| `task_name` | string | true | - | 任务名称 | 非空字符串 |
| `acceptance_criteria` | array | true | - | 验收标准列表 | 至少1个标准 |
| `tech_stack` | array | true | - | 技术栈列表 | 有效的技术名称 |
| `task_spec` | markdown | true | - | 详细任务规格说明 | 长度 > 50字符 |
| `design_reference` | string | false | "" | 相关设计文档链接 | 有效的文件路径 |
| `codebase_context` | string | false | "" | 代码库上下文信息 | - |
| `coding_standards` | string | false | "team_default" | 编码规范文档 | - |

---

## Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识
- **Version**: 1.2.0

---

**Scenario Version**: 1.2.0  
**Last Updated**: 2026-05-07  
**Author**: AI Harness Engineering Team
