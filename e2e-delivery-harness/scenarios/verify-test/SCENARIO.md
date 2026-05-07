---
name: verify-test
description: 测试验证场景，负责设计测试用例、执行测试并报告缺陷
type: scenario
category: quality
stage: testing
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [testing, quality, validation]
---

# Verify Test - Testing Scenario

## Purpose

设计并执行测试用例，验证功能实现是否满足需求，发现并跟踪缺陷，确保交付质量。

**核心目标**:
- 基于需求和设计创建全面的测试用例
- 执行测试并准确记录结果
- 发现和报告缺陷，跟踪修复进度
- 提供客观的质量评估

**成功标准**:
- 测试覆盖率 ≥90%
- 所有关键路径已测试
- 缺陷检出率 ≥95%
- 测试报告完整准确

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解测试范围和目标
   ├─ 输入: requirements_spec, test_scope
   ├─ 思考: 需要测试哪些功能？验收标准是什么？
   ├─ 验证: 与需求规格对照，确认覆盖所有验收标准
   └─ 输出: 测试范围定义
   ↓
Step 2: [ANALYZE] 分析测试策略和方法
   ├─ 输入: 测试范围定义, design_documents
   ├─ 思考: 采用什么测试方法？需要哪些测试类型？
   ├─ 验证: 测试策略能发现主要缺陷
   └─ 输出: 测试策略文档
   ↓
Step 3: [DESIGN] 设计测试用例和测试数据
   ├─ 输入: 测试策略文档
   ├─ 思考: 测试用例是否覆盖所有场景？边界条件呢？
   ├─ 验证: 正向、反向、边界全覆盖
   └─ 输出: 测试用例集 + 测试数据
   ↓
Step 4: [IMPLEMENT] 准备测试环境和执行测试
   ├─ 输入: 测试用例集, test_environment
   ├─ 思考: 环境是否就绪？测试数据是否充分？
   ├─ 验证: 环境配置正确，数据准备完成
   └─ 输出: 测试执行结果
   ↓
Step 5: [VERIFY] 分析测试结果和缺陷管理
   ├─ 输入: 测试执行结果
   ├─ 执行: 缺陷识别、分类、报告
   ├─ 验证: 缺陷描述清晰可复现
   └─ 输出: 缺陷报告 + 测试报告
   ↓
Step 6: [HANDOVER] 准备交接给部署或返工阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context (质量状态)
   └─ 通知: Deploy Release Agent 或 Implement Feature Agent
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 测试范围界定 | 开始测试设计前 | 全量测试/回归测试/冒烟测试 | 变更范围和风险评估 | 测试计划 |
| DC-002 | 测试方法选择 | 测试策略制定时 | 手动测试/自动化测试/混合 | 成本效益、复用频率 | 测试策略文档 |
| DC-003 | 缺陷优先级判定 | 发现缺陷时 | P0/P1/P2/P3 | 影响范围、严重程度 | 缺陷报告 |
| DC-004 | 测试充分性判断 | 测试执行中 | 继续测试/停止测试 | 覆盖率达标、边际收益递减 | 测试报告 |
| DC-005 | 争议缺陷处理 | 开发不认可缺陷时 | 维持/关闭/延期 | 是否符合需求和验收标准 | 缺陷跟踪系统 |
| DC-006 | 回归测试范围 | 缺陷修复后 | 全量回归/部分回归 | 修改影响范围、风险等级 | 回归测试计划 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续测试 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能测试 | 尝试绕过，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 测试环境问题 (P0/P1)

**识别信号**: 
- 测试环境无法访问或启动失败
- 依赖服务不可用
- 测试数据损坏或缺失

**处理流程**:
```
IF 测试环境无法正常工作
THEN
  1. 诊断具体问题（网络、配置、依赖服务等）
  2. 尝试重启或重新配置环境
  3. IF 15分钟内无法解决 THEN
       a. 联系运维团队
       b. 尝试使用备用环境
       c. 如无可用的备用环境，标记为 [阻塞-环境问题]
       d. 升级到项目负责人
     END
  4. 记录环境问题和已尝试的解决方案
END
```

**降级方案**: 使用Mock或Stub替代不可用的服务，标注测试局限性

**升级条件**: 
- P0: 完全无法进行测试，超过1小时未恢复
- P1: 部分功能无法测试，但有替代方案

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P0/P1"
  type: "test_environment_issue"
  description: "测试环境问题：{详细描述}"
  affected_tests: ["测试用例ID列表"]
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded"
```

---

### Error Scenario 2: 测试数据不足 (P1/P2)

**识别信号**: 
- 缺少必要的测试数据
- 现有数据无法覆盖特定场景
- 数据质量不符合要求

**处理流程**:
```
IF 缺少必要的测试数据
THEN
  1. 明确数据需求（字段、范围、数量）
  2. 请求数据准备或使用数据生成工具
  3. IF 无法获取真实数据 THEN
       a. 创建模拟数据（Mock Data）
       b. 使用数据脱敏的生产数据（如可用）
       c. 标注数据限制和对测试的影响
     END
  4. 评估数据不足对测试结论的影响
END
```

**降级方案**: 使用模拟数据，明确标注测试局限性

**升级条件**: 核心功能测试因数据问题无法进行

---

### Error Scenario 3: 缺陷争议 (P2)

**识别信号**: 
- 开发人员认为不是缺陷
- 产品经理认为符合预期
- 团队成员对验收标准理解不一致

**处理流程**:
```
IF 发现缺陷存在争议
THEN
  1. 引用需求规格和验收标准
  2. 组织讨论会议（测试、开发、产品三方）
  3. 澄清验收标准的真实意图
  4. IF 仍无法达成共识 THEN
       a. 升级到产品经理或技术负责人裁决
       b. 记录讨论过程和各方观点
       c. 等待最终决定
     ELSE
       a. 根据共识更新缺陷状态
       b. 如需，更新验收标准文档
     END
END
```

**降级方案**: 暂时标记为"待确认"，继续测试其他功能

**升级条件**: 超过1轮讨论仍无法达成共识

---

### Error Scenario 4: 测试时间不足 (P2)

**识别信号**: 
- 剩余时间不足以完成所有测试用例
- 临近发布截止时间
- 测试进度滞后

**处理流程**:
```
IF 测试时间不足
THEN
  1. 重新评估测试用例优先级（P0/P1/P2）
  2. 优先执行P0（关键路径）测试用例
  3. IF 时间仍然不足 THEN
       a. 与项目经理沟通调整发布计划或增加资源
       b. 基于风险评估选择性地跳过部分测试
       c. 明确标注未测试区域和风险
     END
  4. 记录时间限制对测试充分性的影响
END
```

**降级方案**: 基于风险的测试策略，优先保证核心功能质量

**升级条件**: 关键路径测试无法完成

---

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | TEST-PASS-RATE | ≥90% | (通过测试数/总测试数) × 100% | 测试执行报告 | 30% |
| KPI-002 | DEFECT-DETECTION | ≥95% | (发现的缺陷数/实际缺陷总数) × 100% | 事后回顾分析 | 25% |
| KPI-003 | REQ-TRACE | 100% | (有测试覆盖的需求数/总需求数) × 100% | 需求-测试映射表 | 25% |
| KPI-004 | TEST-COVERAGE | ≥85% | (被测试覆盖的代码行数/总代码行数) × 100% | 代码覆盖率工具 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.25) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都有对应测试用例
- [ ] 所有非功能需求都已验证
- [ ] 边界条件和异常场景已覆盖
- [ ] 测试数据充分且多样化
- [ ] 测试报告包含所有必需信息

**一致性验证 (Consistency)**:
- [ ] 测试用例与需求规格一致
- [ ] 测试结果与预期行为对比明确
- [ ] 缺陷描述标准化且可复现
- [ ] 术语使用统一

**准确性验证 (Accuracy)**:
- [ ] 测试结果准确无误
- [ ] 缺陷定位精确
- [ ] 测试数据统计正确
- [ ] 无假阳性或假阴性

**可执行性验证 (Executability)**:
- [ ] 测试用例可重复执行
- [ ] 测试环境稳定可靠
- [ ] 自动化测试脚本运行正常
- [ ] 测试数据可重置

**规范性验证 (Compliance)**:
- [ ] 遵循测试规范和流程
- [ ] 缺陷报告格式标准
- [ ] 测试文档完整归档
- [ ] 符合行业测试标准

---

## Handover Criteria (交接标准)

### 准出条件

```
✅ 测试用例设计完成并通过评审
✅ 测试环境已验证可用
✅ 计划的测试用例已全部执行
✅ 发现的缺陷已记录并分类
✅ 测试报告已编写完成
✅ 质量评估结论已给出
✅ Handover Context 已生成
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 测试用例集 | Excel/TestLink | docs/test-cases.xlsx | v1.0.0 | 完整测试用例 |
| 测试执行报告 | HTML/PDF | reports/test-execution-report.html | - | 执行结果汇总 |
| 缺陷报告 | JIRA/Excel | defects/defect-list.xlsx | - | 缺陷清单 |
| 代码覆盖率报告 | HTML | reports/coverage/index.html | - | 覆盖率详情 |
| 测试总结报告 | Markdown | docs/test-summary.md | v1.0.0 | 质量评估和建议 |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "testing"
    to_stage: "deployment" or "development"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "passed/failed/partial"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_test_cases: {{number}}
    passed: {{number}}
    failed: {{number}}
    blocked: {{number}}
    
  artifacts:
    delivered:
      - name: "Test Cases"
        path: "docs/test-cases.xlsx"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Test Execution Report"
        path: "reports/test-execution-report.html"
        version: "1.0.0"
      - name: "Defect List"
        path: "defects/defect-list.xlsx"
        version: "1.0.0"
      - name: "Test Summary Report"
        path: "docs/test-summary.md"
        version: "1.0.0"
      
  decisions:
    - id: "DC-003"
      description: "缺陷优先级判定"
      rationale: "基于影响范围和严重程度评定P0-P3"
      
  open_issues:
    blocking:
      - id: "DEFECT-001"
        description: "核心功能X存在严重缺陷"
        severity: "P0"
        status: "open"
    non_blocking:
      - id: "DEFECT-002"
        description: "UI显示小问题"
        severity: "P3"
        status: "accepted"
        
  risks:
    - id: "RISK-001"
      description: "部分边缘场景未充分测试（时间限制）"
      probability: "low"
      impact: "medium"
      mitigation: "生产环境密切监控，承诺下个迭代补充测试"
      
  recommendations:
    - "建议先修复P0和P1级别缺陷再发布"
    - "重点关注性能测试中发现的瓶颈"
    - "建议在灰度发布阶段重点监控X功能"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "TEST-PASS-RATE"
        value: 92
        target: 90
        status: "pass"
      - kpi_id: "KPI-002"
        name: "DEFECT-DETECTION"
        value: 96
        target: 95
        status: "pass"
      - kpi_id: "KPI-003"
        name: "REQ-TRACE"
        value: 100
        target: 100
        status: "pass"
      - kpi_id: "KPI-004"
        name: "TEST-COVERAGE"
        value: 87
        target: 85
        status: "pass"
    overall_score: 93
    grade: "excellent"
    recommendation: "approved_for_release"
```

---

## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| **Agent** | `../../agents/verify-test.agent.md` | 测试验证角色定义 |
| **Prompt** | `../../prompts/verify-test.prompt.md` | 测试验证执行提示词 |
| **Instruction** | `../../instructions/verify-test.instructions.md` | 测试验证技术指令 |
| **Skill** | `../../skills/verify-test/SKILL.md` | 测试验证领域技能 |

---

## Prerequisites

### Required Preconditions

1. ✅ 功能开发已完成 (implement-feature 场景输出)
2. ✅ 测试环境已部署并验证可用
3. ✅ 测试数据已准备
4. ✅ 需求规格和验收标准明确
5. ✅ 测试工具和框架已就绪

### Expected Input

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `test_scope` | string | true | - | 测试范围描述 | 非空字符串 |
| `requirements_spec` | markdown | true | - | 需求规格说明书 | 包含验收标准 |
| `test_environment` | object | true | - | 测试环境信息 | URL、账号、配置等 |
| `design_documents` | array | false | [] | 相关设计文档 | 文件路径列表 |
| `test_data` | object | false | {} | 测试数据集 | 结构化数据 |
| `previous_test_results` | array | false | [] | 历史测试结果 | 用于回归测试 |

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
