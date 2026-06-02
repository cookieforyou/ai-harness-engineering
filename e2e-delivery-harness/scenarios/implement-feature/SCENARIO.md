---
name: implement-feature
description: "功能实现场景，按照任务清单完成代码开发、单元测试和文档更新"
version: "1.2.0"
type: scenario
category: development
stage: feature-implementation
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [development, coding, testing, implementation]
---
# Implement Feature - Development Scenario

## Purpose

按照任务清单完成代码开发、单元测试和文档更新，确保代码质量、可维护性和交付进度，为测试验证阶段提供高质量的代码交付物。

### Business Value

- **保证代码质量**: 通过编码规范、单元测试和代码审查确保代码符合质量标准
- **提升开发效率**: 标准化的开发流程和最佳实践减少返工和调试时间
- **降低技术债务**: 遵循SOLID原则和设计模式，保持代码的可维护性和可扩展性
- **增强可追溯性**: 清晰的代码注释、文档和Git提交历史便于问题定位和知识传承
- **提高团队协作**: 统一的编码规范和代码审查流程促进团队知识共享和质量提升

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成功能实现工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解任务需求和验收标准
   ├─ 问：任务的业务背景和核心目标是什么？验收标准是否清晰可测量？
   ├─ 验证：与任务规格说明书逐条对照，确认无歧义和遗漏
   └─ 检查：验收标准符合SMART原则（具体、可衡量、可达成、相关、有时限）
   ↓
[ANALYZE] Step 2: 分析技术方案和依赖关系
   ├─ 问：实现方案是否符合架构设计？是否有技术风险和依赖？
   ├─ 验证：参考系统设计文档，确认技术选型合理，依赖已明确
   └─ 检查：识别所有外部依赖（第三方库、API接口、数据库表等）
   ↓
[DESIGN] Step 3: 设计代码结构和接口
   ├─ 问：类/函数结构如何设计？接口契约是什么？是否符合SOLID原则？
   ├─ 验证：代码结构清晰，职责单一，接口定义明确
   └─ 检查：避免循环依赖，考虑异常处理和边界条件
   ↓
[IMPLEMENT] Step 4: 编写代码和单元测试
   ├─ 问：代码是否规范？命名是否清晰？测试是否覆盖核心逻辑？
   ├─ 验证：遵循编码规范，测试覆盖率≥80%，核心逻辑100%覆盖
   └─ 检查：无硬编码值，无重复代码，注释清晰完整
   ↓
[VERIFY] Step 5: 自检代码质量和测试覆盖
   ├─ 执行：代码规范检查（lint）、静态分析、单元测试执行
   ├─ 验证：无规范违规，圈复杂度≤15，测试全部通过
   └─ 检查：安全扫描无高危漏洞，性能无明显问题
   ↓
[HANDOVER] Step 6: 准备交接给测试验证阶段
   ├─ 生成：Handover Context（含代码统计、质量指标、开放问题）
   ├─ 更新：Global Context（代码库状态、分支信息）
   └─ 通知：Verify Test Agent（提交代码审查请求）
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 验收标准清晰度 | 需求理解阶段 | 清晰/需澄清 | 是否可测量、无歧义、符合SMART原则 | 任务理解备忘录 |
| DC-002 | 技术方案选择 | 方案设计阶段 | 方案A/方案B/方案C | 复杂度、性能、可维护性、团队熟悉度 | 技术实现方案 |
| DC-003 | 代码规范冲突 | 编码实现阶段 | 团队规范/个人习惯 | 始终遵循团队统一编码规范 | 代码审查记录 |
| DC-004 | 测试覆盖策略 | 测试编写阶段 | 全覆盖/核心覆盖 | 基于风险评估和时间约束，核心逻辑100%覆盖 | 测试计划文档 |
| DC-005 | 重构时机判断 | 发现代码异味时 | 立即重构/后续迭代 | 影响范围小且风险低则立即重构，否则记录技术债务 | 技术债务记录 |
| DC-006 | 提交粒度控制 | 代码提交时 | 大提交/小步提交 | 优先小步提交（每个commit完成一个独立功能点） | Git提交历史 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 验收标准不清晰

**识别信号**: 
- 验收标准存在模糊表述（如"用户友好"、"高性能"、"快速响应"）
- 缺少量化指标或阈值
- 多个理解方式都合理，无法确定唯一实现方案

**处理流程**:
```
IF 验收标准模糊或有歧义
THEN
  1. 列出所有可能的理解方式（至少2种）
  2. 选择最合理的理解（基于行业标准和最佳实践）
  3. 在代码注释中明确说明假设条件和选择理由
  4. 标记为 [需确认-验收标准] 并在Handover Context中突出显示
  5. IF 影响核心功能实现 THEN 升级到产品经理或Tech Lead确认
  6. 记录决策依据和潜在风险
END
```

**降级方案**: 基于行业标准做出合理假设，明确标注待确认，承诺在评审时重点讨论

**升级条件**: 影响核心功能实现、存在重大理解分歧、或假设可能导致架构变更

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "ambiguous_acceptance_criteria"
  description: "验收标准'{criteria}'存在歧义，有{N}种理解方式"
  assumptions_made:
    - assumption_1: "{假设1}"
    - assumption_2: "{假设2}"
  action_taken: "采用{assumption}作为实现标准，已在代码注释中标注"
  result: "continued_with_assumption"
  escalation_needed: true/false
```

---

### Error Scenario 2: 技术难点阻塞

**识别信号**: 
- 多次尝试（≥3次）仍无法解决的技术问题
- 缺少必要的技术知识或工具权限
- 第三方依赖存在兼容性问题或版本冲突
- 性能指标无法达到要求

**处理流程**:
```
IF 遇到无法解决的技术问题
THEN
  1. 分析问题的根本原因（使用5 Whys方法）
  2. 搜索官方文档、社区资源、Stack Overflow寻找解决方案
  3. 尝试替代方案（最多3种不同approach）
  4. 评估每种方案的优缺点和可行性
  5. IF 仍无法解决 THEN 
       a. 记录详细的问题描述、错误信息、尝试过程和失败原因
       b. 升级到技术负责人或架构师
       c. 标记任务为 [阻塞-技术难点]
       d. 提出临时解决方案或简化版本（如可行）
     END
  6. 更新技术债务记录和风险清单
END
```

**降级方案**: 实现简化版本或临时方案，明确标注技术债务和限制条件，承诺后续迭代完善

**升级条件**: 
- P0: 完全阻塞任务进展，超过2小时未解决，无临时方案
- P1: 影响核心功能，但有临时方案可继续其他工作

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-002"
  timestamp: "{{ISO8601}}"
  level: "P0/P1"
  type: "technical_blocker"
  description: "技术问题：{问题详细描述}"
  root_cause_analysis: "{5 Whys分析结果}"
  attempts:
    - attempt_1: "{方案1} - 失败原因：{原因}"
    - attempt_2: "{方案2} - 失败原因：{原因}"
    - attempt_3: "{方案3} - 失败原因：{原因}"
  workaround_available: true/false
  workaround_description: "{临时方案描述}"
  action_taken: "已升级至技术负责人，附带详细问题分析"
  result: "blocked_escalated"
  estimated_resolution_time: "{预估解决时间}"
```

---

### Error Scenario 3: 设计与实现不匹配

**识别信号**: 
- 实现过程中发现设计文档存在缺陷或不可行
- 设计方案在实际编码中发现性能瓶颈或技术限制
- 发现更好的实现方式或更优的设计模式
- 需求变更导致原设计不再适用

**处理流程**:
```
IF 发现设计与实现不匹配
THEN
  1. 分析差异的具体内容、原因和影响范围
  2. 判断是设计问题（设计不合理）还是实现问题（实现偏差）
  3. 评估修改设计的成本 vs 调整实现的成本
  4. 评估对其它模块的影响（ blast radius 分析）
  5. IF 需要修改设计 THEN
       a. 联系系统设计师讨论，提供改进建议和数据支持
       b. 提出至少2个备选方案及权衡分析
       c. 等待设计确认后再继续实现
       d. 更新设计文档并记录变更原因
     ELSE
       a. 调整实现方案以符合设计
       b. 记录偏离设计的原因和权衡考虑
       c. 在代码注释中说明特殊情况
     END
  6. 更新变更记录和技术决策日志
END
```

**降级方案**: 记录设计偏差，在代码注释中详细说明原因和权衡考虑，承诺后续与设计团队对齐

**升级条件**: 需要修改架构设计、影响多个模块、或涉及核心技术选型变更

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-003"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "design_implementation_mismatch"
  description: "设计文档与实际实现存在偏差"
  deviation_details: "{具体差异描述}"
  impact_analysis:
    affected_modules: ["模块1", "模块2"]
    severity: "high/medium/low"
  root_cause: "设计缺陷/实现偏差/需求变更"
  alternatives_considered:
    - option_1: "{方案1} - 优缺点"
    - option_2: "{方案2} - 优缺点"
  action_taken: "已联系系统设计师/已调整实现"
  decision_rationale: "{最终决策的理由}"
  result: "resolved/pending"
  design_doc_updated: true/false
```

---

### Error Scenario 4: 测试覆盖率不达标

**识别信号**: 
- 单元测试覆盖率 <80%（团队标准为80%）
- 关键业务逻辑路径未覆盖
- 边界条件和异常场景缺失测试
- Mock对象使用过多，真实逻辑测试不足

**处理流程**:
```
IF 测试覆盖率不达标
THEN
  1. 识别未覆盖的代码路径和分支（使用覆盖率报告工具）
  2. 分析未覆盖原因：
     - 难以测试（依赖外部系统、并发逻辑等）
     - 时间不足（临近交付期限）
     - 设计问题（代码耦合度高、职责不清）
  3. 补充缺失的测试用例，优先覆盖核心业务逻辑
  4. 对于难以测试的代码，考虑重构以提高可测试性
  5. IF 仍无法达到目标 THEN
       a. 记录未覆盖区域、代码行号和原因
       b. 评估未覆盖区域的风险等级（高/中/低）
       c. 制定后续完善计划和责任人
       d. 标记为 [部分覆盖-需后续完善]
       e. 在Handover Context中明确说明
     END
  6. 确保核心业务逻辑测试覆盖率100%
END
```

**降级方案**: 记录未覆盖区域和风险，承诺在下个迭代或专门的技术债务迭代中完善，获得Tech Lead批准

**升级条件**: 核心业务逻辑测试覆盖率 <60%，或高风险区域未覆盖

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-004"
  timestamp: "{{ISO8601}}"
  level: "P2"
  type: "insufficient_test_coverage"
  description: "测试覆盖率{actual}%低于目标{target}%"
  coverage_breakdown:
    total_lines: {number}
    covered_lines: {number}
    uncovered_lines: {number}
    critical_logic_coverage: {percentage}
  uncovered_areas:
    - area_1: "{代码路径} - 原因：{原因} - 风险：{风险等级}"
    - area_2: "{代码路径} - 原因：{原因} - 风险：{风险等级}"
  action_taken: "已补充{N}个测试用例，剩余未覆盖区域已记录"
  remediation_plan:
    owner: "{责任人}"
    target_date: "{日期}"
    approach: "{完善方案}"
  result: "partial_coverage_accepted"
  tech_lead_approval: true/false
```

## Quality Metrics

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | CODE-COVERAGE | ≥80% | (已覆盖行数/总行数) × 100% | 单元测试覆盖率报告（JaCoCo/Istanbul等） | 30% |
| KPI-002 | BUG-DENSITY | ≤0.5/KLOC | 缺陷数/(代码千行数) | 代码审查和测试发现的缺陷数统计 | 25% |
| KPI-003 | CYCLOMATIC | ≤15 | 平均圈复杂度 per 函数 | 静态代码分析工具（SonarQube/ESLint等） | 20% |
| KPI-004 | REVIEW-PASS | 100% | (一次通过审查的代码/总代码) × 100% | Code Review记录和审批状态 | 25% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.20) + (KPI-004 × 0.25)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

**KPI详细说明**:
- **CODE-COVERAGE**: 核心业务逻辑必须100%覆盖，整体覆盖率≥80%
- **BUG-DENSITY**: 每千行代码缺陷数≤0.5，严重缺陷数为0
- **CYCLOMATIC**: 单个函数圈复杂度≤15，超过需重构或拆分
- **REVIEW-PASS**: 代码审查一次通过率，反映代码质量和规范遵循度

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都已实现，无遗漏
- [ ] 所有验收标准都已满足并通过验证
- [ ] 单元测试覆盖核心逻辑和边界条件
- [ ] 代码注释完整清晰，关键逻辑有详细说明
- [ ] 相关文档已更新（API文档、README、CHANGELOG）
- [ ] Git提交历史清晰，每个commit有明确的message

**一致性验证 (Consistency)**:
- [ ] 代码风格与团队规范一致（缩进、命名、注释风格）
- [ ] 命名规范统一（变量、函数、类名符合约定）
- [ ] 接口设计与架构文档一致，无偏差
- [ ] 依赖关系合理，无循环依赖
- [ ] 错误处理方式统一（异常类型、错误码、日志格式）

**准确性验证 (Accuracy)**:
- [ ] 单元测试全部通过，无失败用例
- [ ] 无编译错误或警告（warning级别也需处理）
- [ ] 静态代码分析无严重问题（sonar issues=0）
- [ ] 功能行为符合预期，手动验证通过
- [ ] 性能指标符合要求（响应时间、内存占用等）

**可执行性验证 (Executability)**:
- [ ] 代码可在目标环境运行（开发、测试、生产环境验证）
- [ ] 依赖项已正确配置（package.json/pom.xml等）
- [ ] 部署脚本可用，CI/CD pipeline通过
- [ ] 配置文件完整，环境变量已定义
- [ ] 数据库迁移脚本已准备（如涉及数据模型变更）

**规范性验证 (Compliance)**:
- [ ] 遵循编码规范（团队约定的style guide）
- [ ] 安全最佳实践已应用（输入验证、SQL注入防护、XSS防护等）
- [ ] 性能考虑已纳入（避免N+1查询、合理使用缓存等）
- [ ] 可访问性标准已满足（WCAG 2.1 AA级，如适用）
- [ ] 日志记录完整，便于问题排查和审计

## Handover Criteria

### 准出条件

```
✅ 所有功能代码已完成并通过自检
✅ 单元测试覆盖率 ≥80%，核心逻辑100%覆盖
✅ 代码规范检查通过，无严重违规（lint errors=0）
✅ Code Review 已通过或已提交审查（PR创建）
✅ 接口文档已更新（如有API变更）
✅ 相关技术文档已同步（README、CHANGELOG）
✅ 静态代码分析通过（sonar issues=0或仅info级别）
✅ 安全扫描无高危漏洞
✅ Handover Context 已生成并包含所有必需字段
✅ 质量评分 ≥70分（基于KPIs计算）
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 源代码 | .java/.py/.js/.ts等 | src/{feature_path}/ | v1.0.0 | 功能实现代码，含注释 |
| 单元测试 | test files | tests/{test_path}/ | v1.0.0 | 测试用例代码 |
| 测试报告 | HTML/XML | reports/test-report.html | - | 测试执行结果和覆盖率 |
| 代码覆盖率报告 | HTML | reports/coverage/index.html | - | 详细的覆盖率分析 |
| 接口文档 | Markdown/OpenAPI YAML | docs/api-spec.md | v1.0.0 | API接口说明和示例 |
| 变更记录 | Markdown | CHANGELOG.md | - | 本次变更说明和影响 |
| Git提交历史 | Git log | repository | - | 清晰的commit message |
| Code Review记录 | PR comments | GitHub/GitLab PR | - | 审查意见和回复 |

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
    total_lines_deleted: {{number}}
    files_changed: {{number}}
    commits_count: {{number}}
    
  artifacts:
    delivered:
      - name: "Feature Implementation"
        path: "src/{feature_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
        files_count: {{number}}
      - name: "Unit Tests"
        path: "tests/{test_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
        test_cases_count: {{number}}
      - name: "Test Report"
        path: "reports/test-report.html"
        version: "1.0.0"
      - name: "Coverage Report"
        path: "reports/coverage/index.html"
        version: "1.0.0"
      - name: "API Documentation"
        path: "docs/api-spec.md"
        version: "1.0.0"
        
  decisions:
    - id: "DC-001"
      description: "技术方案选择"
      rationale: "选择方案A因为性能更优（响应时间降低30%）"
      alternatives_considered: ["方案B（简单但性能差）", "方案C（复杂但可扩展）"]
      impact: "影响模块X和Y的性能表现"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "边缘场景X的测试覆盖不足（覆盖率60%）"
        risk_level: "low"
        planned_resolution: "下个迭代补充边界测试用例"
        owner: "Developer"
        target_date: "{{date}}"
        
  risks:
    - id: "RISK-001"
      description: "新功能依赖的第三方库版本较新（v2.0.0），可能存在未知bug"
      probability: "low"
      impact: "medium"
      mitigation: "已在测试环境验证兼容性，监控生产环境日志"
      contingency_plan: "准备回滚到稳定版本v1.9.0"
      
  recommendations:
    - "重点测试边界条件和异常场景（见ISSUE-001）"
    - "关注性能敏感区域的测试（函数X和Y的圈复杂度较高）"
    - "验证与现有功能的集成，特别是模块Z的兼容性"
    - "建议在压力测试中验证第三方库的稳定性"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "CODE-COVERAGE"
        value: 85
        target: 80
        status: "pass"
        critical_logic_coverage: 100
      - kpi_id: "KPI-002"
        name: "BUG-DENSITY"
        value: 0.3
        target: 0.5
        unit: "defects/KLOC"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "CYCLOMATIC"
        value: 12
        target: 15
        max_function_complexity: 18
        status: "pass"
      - kpi_id: "KPI-004"
        name: "REVIEW-PASS"
        value: 100
        target: 100
        review_rounds: 1
        status: "pass"
    overall_score: 92
    grade: "excellent"
    
  next_steps_for_testing:
    - "执行集成测试，验证与模块A/B/C的交互"
    - "进行端到端测试，覆盖完整用户旅程"
    - "执行性能测试，验证响应时间和吞吐量指标"
    - "进行安全测试，特别是输入验证和权限控制"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/implement-feature.agent.md` | 功能实现Agent角色定义 |
| Prompt | `../../prompts/implement-feature.prompt.md` | 功能实现提示词模板 |
| Skill | `../../skills/implement-feature/SKILL.md` | 功能实现技能包 |
| Instruction | `../../instructions/implement-feature.instructions.md` | 功能实现技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Coding Standards](../../standards/coding-standards.md) - 团队编码规范
  - [Testing Guidelines](../../standards/testing-guidelines.md) - 测试编写指南
  - [Git Workflow](../../standards/git-workflow.md) - Git分支管理和提交规范
  - [Code Review Checklist](../../standards/code-review-checklist.md) - 代码审查检查清单
- **Templates**: 
  - [Pull Request Template](../../templates/pull-request.template.md) - PR模板
  - [Commit Message Convention](../../templates/commit-message-convention.md) - Commit消息规范
  - [API Documentation Template](../../templates/api-doc.template.md) - API文档模板
- **Evaluations**: 
  - [Code Quality Checklist](../../evaluations/code-quality-checklist.md) - 代码质量检查清单
  - [Test Coverage Analysis](../../evaluations/test-coverage-analysis.md) - 测试覆盖率分析
  - [Static Code Analysis Report](../../evaluations/static-code-analysis.md) - 静态代码分析报告

## Prerequisites

### 必需前置条件

1. ✅ 任务分解已完成 (decompose-task 场景输出)
2. ✅ 技术方案已确认 (design-system 场景输出)
3. ✅ 接口定义已明确 (API contract finalized)
4. ✅ 开发环境已就绪 (IDE、依赖、配置)
5. ✅ 代码仓库访问权限已获得
6. ✅ CI/CD pipeline配置完成

### 期望输入

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `task_id` | string | true | - | 任务唯一标识符 | 非空字符串，格式：TASK-XXX |
| `task_name` | string | true | - | 任务名称 | 非空字符串，长度5-100字符 |
| `acceptance_criteria` | array | true | - | 验收标准列表 | 至少1个标准，每个标准符合SMART原则 |
| `tech_stack` | array | true | - | 技术栈列表 | 有效的技术名称（Java/Python/JavaScript等） |
| `task_spec` | markdown | true | - | 详细任务规格说明 | 长度 > 100字符，包含用户故事和AC |
| `design_reference` | string | false | "" | 相关设计文档链接 | 有效的文件路径或URL |
| `codebase_context` | string | false | "" | 代码库上下文信息 | 相关模块和依赖说明 |
| `coding_standards` | string | false | "team_default" | 编码规范文档 | 有效的规范文档路径 |
| `test_requirements` | object | false | {coverage: 80} | 测试要求 | 包含覆盖率目标和测试类型 |
