---
name: verify-test
description: "Technical instructions for test verification execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [instruction, technical, testing]
---
# Test Verification Instructions

## Purpose

本文档定义了测试验证阶段的标准操作流程、质量检查标准和工作产出规范。测试验证是确保软件质量、发现和跟踪缺陷的关键阶段，为发布决策提供客观依据。

### Business Value

- **保证产品质量**: 通过系统化测试发现潜在缺陷，避免生产环境故障和用户投诉
- **降低修复成本**: 早期发现缺陷，修复成本远低于生产环境问题（10-100倍差异）
- **提升用户满意度**: 充分的功能和性能测试确保用户体验流畅，减少负面反馈
- **支持决策制定**: 客观的质量评估和风险分析为发布决策提供数据支持
- **建立质量基线**: 完整的测试记录和覆盖率数据便于后续回归测试和质量趋势分析

## Investigation Flow

### 流程概览

```
测试范围分析 → 测试策略制定 → 用例设计 → 环境准备 → 测试执行 → 缺陷管理 → 质量评估 → Handover
```

---

### Step 1: 测试范围分析和目标定义

**目的**: 明确测试边界、重点和验收标准

**输入**:
- 需求规格说明书 (requirements_spec)
- 测试范围描述 (test_scope)
- 相关设计文档 (design_documents)

**操作**:

1. **提取验收标准**
   - 阅读需求规格说明书，识别所有Given-When-Then格式的验收标准
   - 为每个验收标准分配唯一ID（AC-001, AC-002, ...）
   - 确认验收标准的清晰度和可测试性

2. **识别测试重点**
   - 与产品经理确认业务优先级
   - 识别核心功能模块（P0级别）
   - 识别高风险区域（复杂逻辑、新技术、频繁变更）

3. **确定非功能需求**
   - 性能要求（响应时间、吞吐量、并发用户数）
   - 安全要求（认证、授权、数据加密）
   - 可用性要求（兼容性、易用性、可访问性）

4. **评估测试约束**
   - 时间约束（测试周期、发布截止日期）
   - 资源约束（人力、环境、工具）
   - 技术约束（依赖服务、第三方集成）

**输出**: 
- 测试范围定义文档
- 验收标准清单（含ID和优先级）
- 测试重点和风险评估报告

---

### Step 2: 测试策略和方法选择

**目的**: 制定最优测试策略，平衡覆盖率和效率

**输入**:
- 测试范围定义文档
- 设计文档（架构设计、数据库设计、API设计）

**操作**:

1. **选择测试方法**
   - **黑盒测试**: 适用于功能测试、用户验收测试
   - **白盒测试**: 适用于单元测试、集成测试
   - **灰盒测试**: 适用于API测试、数据库测试

2. **确定测试类型组合**
   - 功能测试（必选）
   - 边界测试（必选）
   - 异常测试（必选）
   - 性能测试（如需要）
   - 安全测试（如需要）
   - 兼容性测试（如需要）

3. **决定手动/自动化比例**
   - 新功能：70%手动 + 30%自动化（探索性测试为主）
   - 稳定功能：30%手动 + 70%自动化（回归测试为主）
   - API测试：优先自动化（稳定性高，易于自动化）

4. **规划测试资源**
   - 人力安排（测试人员数量和技能要求）
   - 环境需求（测试服务器、数据库、第三方服务）
   - 工具需求（测试管理工具、自动化工具、性能测试工具）
   - 时间计划（测试开始/结束时间、里程碑）

**输出**: 
- 测试策略文档
- 测试资源计划
- 测试时间表

---

### Step 3: 测试用例设计

**目的**: 设计覆盖完整的高质量测试用例

**输入**:
- 测试策略文档
- 验收标准清单
- 设计文档

**操作**:

1. **运用测试设计技术**
   - **等价类划分**: 将输入域划分为有效和无效等价类
   - **边界值分析**: 测试边界值和略超边界的值
   - **决策表测试**: 处理多条件组合的逻辑
   - **状态转换测试**: 测试状态之间的转换路径
   - **用例场景法**: 基于用户操作流程设计用例

2. **为每个验收标准设计测试用例**
   - 正常路径（Happy Path）：验证预期行为
   - 异常路径（Exception Path）：验证错误处理
   - 边界条件（Boundary Condition）：验证边界值处理

3. **定义测试用例要素**
   ```markdown
   ### TC-{ID}: {用例名称}
   - **关联验收标准**: AC-{ID}
   - **优先级**: P0/P1/P2/P3
   - **前置条件**: {执行前必须满足的条件}
   - **测试数据**: {所需测试数据描述}
   - **测试步骤**:
     1. {步骤1}
     2. {步骤2}
     3. {步骤3}
   - **预期结果**: {明确可验证的预期行为}
   - **实际结果**: {执行后填写}
   - **状态**: Pass/Fail/Blocked
   ```

4. **组织用例评审**
   - 邀请开发、产品、测试三方参与
   - 审查用例覆盖度（是否覆盖所有验收标准）
   - 审查用例质量（步骤是否清晰、预期是否明确）
   - 收集反馈并优化用例

**输出**: 
- 测试用例集（Excel/TestLink/Markdown格式）
- 用例评审记录和优化建议

---

### Step 4: 测试环境准备和数据生成

**目的**: 搭建稳定的测试环境，准备充分的测试数据

**输入**:
- 测试策略文档
- 测试用例集
- 环境配置要求

**操作**:

1. **搭建测试环境**
   - 部署应用程序到测试服务器
   - 配置依赖服务（数据库、缓存、消息队列、第三方API）
   - 安装测试工具和框架（Selenium、JMeter、Postman等）
   - 配置监控和日志收集（便于问题诊断）

2. **准备测试数据**
   - 识别数据需求（字段、范围、数量、分布、特殊条件）
   - 从生产环境脱敏导入数据（需符合隐私政策，如GDPR）
   - 使用数据生成工具创建模拟数据：
     - Faker（Python/JavaScript）
     - Mockaroo（在线工具）
     - DataFactory（Java）
   - 准备特殊场景数据：
     - 边界值数据（最小值、最大值、空值）
     - 异常数据（非法格式、超长字符串、特殊字符）
     - 历史数据（用于测试时间相关功能）

3. **验证环境和数据**
   - 执行冒烟测试（Smoke Test）验证环境可用性
   - 检查数据完整性和一致性（无脏数据、无缺失数据）
   - 记录环境配置（URL、版本号、配置文件、依赖服务状态）
   - 记录数据特征（数据量、数据类型、数据来源）

**输出**: 
- 就绪的测试环境
- 测试数据集
- 环境配置文档
- 数据准备报告

---

### Step 5: 测试执行和结果记录

**目的**: 按优先级执行测试用例，准确记录测试结果

**输入**:
- 测试用例集
- 测试环境
- 测试数据

**操作**:

1. **按优先级执行测试用例**
   - P0（核心功能）优先执行
   - P1（重要功能）次之
   - P2/P3（一般/可选功能）最后

2. **记录测试结果**
   ```markdown
   ### TC-{ID} 执行结果
   - **状态**: Pass/Fail/Blocked
   - **执行时间**: {start_time} - {end_time}
   - **实际结果**: {详细描述实际观察到的行为}
   - **与预期对比**: {说明是否符合预期，如不符合则描述差异}
   - **证据**: 
     - 截图: {screenshot_path}
     - 日志: {log_path}
     - 堆栈跟踪: {stack_trace}（如适用）
   - **备注**: {其他需要说明的信息}
   ```

3. **处理异常情况**
   - **环境问题**: 
     - 尝试重启服务或重新配置
     - 联系运维团队协助
     - 标记受影响的用例为 [阻塞-环境问题]
   - **数据问题**: 
     - 补充缺失数据或使用Mock
     - 标记受影响的用例为 [阻塞-数据问题]
   - **用例问题**: 
     - 标记用例为 [待优化]
     - 记录问题描述和改进建议

4. **更新执行进度**
   - 实时更新测试执行看板
   - 统计通过率、执行率
   - 识别阻塞问题和风险

**输出**: 
- 测试执行记录
- 执行进度报告
- 阻塞问题清单

---

### Step 6: 缺陷识别、分类和报告

**目的**: 准确识别缺陷，规范报告并跟踪修复

**输入**:
- 测试执行记录
- 失败用例详情

**操作**:

1. **识别缺陷**
   - 对比预期结果和实际结果
   - 分析失败原因（代码问题、环境问题、用例问题）
   - 确认是否为真正的缺陷（排除误报）

2. **分类和评定优先级**
   | 级别 | 标识 | 描述 | 修复时限 |
   |------|------|------|----------|
   | P0 | Critical | 阻塞核心功能，系统崩溃或数据丢失 | 立即修复（<24小时） |
   | P1 | Major | 严重影响用户体验，主要功能受损 | 尽快修复（<3天） |
   | P2 | Minor | 一般功能问题，不影响核心业务流程 | 下个迭代修复 |
   | P3 | Trivial | 轻微UI/文案问题，几乎不影响使用 | 可延期修复 |

3. **编写缺陷报告**
   ```markdown
   ### DEFECT-{ID}: {缺陷标题}
   - **严重程度**: P0/P1/P2/P3
   - **关联测试用例**: TC-{ID}
   - **关联验收标准**: AC-{ID}
   - **复现步骤**:
     1. {步骤1}
     2. {步骤2}
     3. {步骤3}
   - **预期结果**: {期望的行为}
   - **实际结果**: {实际观察到的行为}
   - **影响范围**: {受影响的功能模块和用户群体}
   - **业务价值影响**: {对业务的影响分析}
   - **证据**:
     - 截图: {screenshot_path}
     - 日志: {log_path}
     - 堆栈跟踪: {stack_trace}
   - **环境信息**: {URL, 版本号, 配置}
   - **提交时间**: {timestamp}
   - **提交人**: {tester_name}
   - **状态**: Open/In Progress/Resolved/Closed
   - **指派给**: {developer_name}
   ```

4. **提交缺陷到跟踪系统**
   - JIRA、GitHub Issues、Azure DevOps等
   - 确保所有必需字段完整
   - 添加标签和组件分类

5. **跟踪缺陷状态**
   - 定期查看缺陷状态更新
   - 协调开发团队修复P0/P1缺陷
   - 验证缺陷修复，执行回归测试

**输出**: 
- 缺陷报告清单
- 缺陷跟踪记录
- 回归测试计划

---

### Step 7: 质量评估和发布建议

**目的**: 基于量化指标进行质量评估，提供客观的发布建议

**输入**:
- 测试执行记录
- 缺陷报告清单
- 代码覆盖率报告

**操作**:

1. **计算KPIs**
   - **TEST-PASS-RATE**: (通过测试数/总测试数) × 100% ≥90%
   - **DEFECT-DETECTION**: (发现的缺陷数/实际缺陷总数估算) × 100% ≥95%
     - 估算方法：基于历史数据、同行评审、生产问题回溯
   - **REQ-TRACE**: (有测试覆盖的需求数/总需求数) × 100% = 100%
   - **TEST-COVERAGE**: (被测试覆盖的代码行数/总代码行数) × 100% ≥85%
     - 使用工具：JaCoCo（Java）、Istanbul（JavaScript）、Coverage.py（Python）

2. **计算综合质量评分**
   ```
   Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.25) + (KPI-004 × 0.20)
   
   合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
   ```

3. **评估遗留风险**
   - 未测试区域的风险分析（功能模块、场景类型）
   - 已知缺陷的影响评估（P2/P3缺陷的业务影响）
   - 生产环境可能出现的问题预测（基于历史数据和经验）

4. **给出发行建议**
   - **Approved for Release**: 质量评分≥85，无P0/P1缺陷，所有KPIs达标
   - **Approved with Conditions**: 质量评分≥70，P0/P1已修复，P2/P3可接受，需在报告中说明条件
   - **Not Recommended**: 质量评分<70，或有未修复的P0/P1缺陷，或关键KPIs未达标

5. **编写测试总结报告**
   - 测试执行统计（用例数、通过率、执行率）
   - 缺陷统计（总数、按严重程度分布、修复情况）
   - 覆盖率分析（需求覆盖率、代码覆盖率）
   - 质量评分和等级
   - 遗留风险和缓解措施
   - 发布建议和条件

**输出**: 
- 质量评估报告
- 发布建议文档
- 测试总结报告

---

### Step 8: Handover Context生成和交接

**目的**: 生成完整的Handover Context，便于下一阶段顺利接手

**输入**:
- 所有交付物（测试用例、执行报告、缺陷报告、覆盖率报告、总结报告）
- 质量评估结果

**操作**:

1. **收集所有交付物**
   - 测试用例集（docs/test-cases.xlsx）
   - 测试执行报告（reports/test-execution-report.html）
   - 缺陷报告清单（defects/defect-list.xlsx）
   - 代码覆盖率报告（reports/coverage/index.html）
   - 测试总结报告（docs/test-summary.md）
   - 需求-测试追溯矩阵（docs/traceability-matrix.xlsx）

2. **填写Handover Context模板**
   ```yaml
   handover:
     header:
       from_stage: "testing"
       to_stage: "deployment" or "development"
       handover_id: "HO-{{timestamp}}-{{sequence}}"
       timestamp: "{{ISO8601}}"
       prepared_by: "{{agent.name}}"
       
     summary:
       status: "passed/failed/partial/conditional_pass"
       completion_percentage: {{0-100}}
       quality_score: {{0-100}}
       total_test_cases: {{number}}
       passed: {{number}}
       failed: {{number}}
       blocked: {{number}}
       skipped: {{number}}
       pass_rate: {{percentage}}%
       execution_rate: {{percentage}}%
       
     artifacts:
       delivered:
         - name: "Test Cases"
           path: "docs/test-cases.xlsx"
           version: "1.0.0"
           checksum: "{{SHA256}}"
         # ... 其他交付物
         
     decisions:
       - id: "DC-003"
         description: "缺陷优先级判定"
         rationale: "基于影响范围、严重程度、业务价值评定P0-P3"
         
     open_issues:
       blocking:
         - id: "DEFECT-001"
           description: "{描述}"
           severity: "P0"
           status: "open"
       non_blocking:
         - id: "DEFECT-002"
           description: "{描述}"
           severity: "P3"
           status: "accepted"
           
     risks:
       - id: "RISK-001"
         description: "{风险描述}"
         probability: "low/medium/high"
         impact: "low/medium/high"
         mitigation: "{缓解措施}"
         
     recommendations:
       - "{建议1}"
       - "{建议2}"
       
     quality_metrics:
       kpi_results:
         - kpi_id: "KPI-001"
           name: "TEST-PASS-RATE"
           value: 92
           target: 90
           unit: "%"
           status: "pass"
       overall_score: 93
       grade: "excellent"
       recommendation: "approved_for_release_with_conditions"
       
     next_steps:
       if_passed:
         - "准备部署包和发布说明"
         - "执行预发布环境验证"
       if_failed:
         - "开发团队修复P0/P1缺陷"
         - "执行回归测试验证修复"
   ```

3. **更新Global Context**
   - 质量状态（passed/failed/partial）
   - 遗留风险清单
   - 生产环境监控建议

4. **通知下一阶段的Agent**
   - 如测试通过：通知 Deploy Release Agent
   - 如测试失败：通知 Implement Feature Agent

**输出**: 
- Handover Context（YAML格式）
- Global Context更新记录
- 下一阶段Agent通知

## What To Check

### 必检项 (Mandatory Checks)

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 用例覆盖完整性 | 所有验收标准都有对应测试用例 | 需求-测试追溯矩阵检查 | 100%覆盖 |
| 测试执行率 | 计划的测试用例已全部执行 | 执行记录统计 | ≥95% |
| 缺陷报告规范性 | 缺陷描述清晰可复现，包含所有必需字段 | 缺陷报告抽样审查 | 100%规范 |
| 代码覆盖率 | 被测试覆盖的代码行数占比 | 代码覆盖率工具（JaCoCo/Istanbul） | ≥85% |
| 质量评分 | 基于KPIs计算的综合评分 | KPI计算公式验证 | ≥70分 |
| Handover Context完整性 | 所有必需字段完整 | Handover Context模板检查 | 100%完整 |

### 建议检查项 (Recommended Checks)

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 回归测试覆盖 | 变更的功能模块有回归测试 | 回归测试用例执行记录 | 100%变更已回归 |
| 非功能测试执行 | 性能和安全测试按计划执行 | 测试执行报告检查 | 已按计划完成 |
| 缺陷根因分析 | 关键缺陷有根因分析 | 缺陷分析报告审查 | P0/P1缺陷有分析 |
| 测试数据充分性 | 测试数据覆盖各种场景 | 测试数据清单审查 | 数据充分且多样化 |
| 自动化脚本质量 | 自动化脚本运行稳定，无flaky tests | 自动化测试执行历史记录 | 成功率≥95% |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 | 评分标准 |
|------|------|------|----------|
| 测试覆盖 | 用例覆盖完整，100%需求有测试 | 30% | 100%: 30分; 90-99%: 25分; 80-89%: 20分; <80%: 0分 |
| 执行准确 | 执行结果准确，无假阳性或假阴性 | 25% | 100%准确: 25分; 95-99%: 20分; 90-94%: 15分; <90%: 0分 |
| 缺陷管理 | 缺陷报告规范，跟踪及时 | 25% | 100%规范: 25分; 90-99%: 20分; 80-89%: 15分; <80%: 0分 |
| 交付物质量 | 报告完整清晰，Handover Context完整 | 20% | 100%完整: 20分; 90-99%: 15分; 80-89%: 10分; <80%: 0分 |

### 质量等级

| 等级 | 分数范围 | 说明 |
|------|----------|------|
| 卓越 (Excellent) | 95-100分 | 所有KPIs超标，测试质量极高 |
| 优秀 (Good) | 85-94分 | 所有KPIs达标，测试质量良好 |
| 合格 (Fair) | 70-84分 | 基本KPIs达标，存在改进空间 |
| 不合格 (Poor) | <70分 | 关键KPIs未达标，需要返工 |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 | 位置 |
|------|------|------|------|------|
| 测试用例集 | Excel/TestLink/Markdown | 是 | 完整测试用例，含前置条件、步骤、预期结果、优先级 | docs/test-cases.xlsx |
| 测试执行报告 | HTML/PDF | 是 | 执行结果汇总，含通过率、失败用例详情、截图证据 | reports/test-execution-report.html |
| 缺陷报告清单 | Excel/JIRA导出 | 是 | 缺陷清单，含状态、优先级、修复情况、复现步骤 | defects/defect-list.xlsx |
| 代码覆盖率报告 | HTML | 是 | 详细的代码覆盖率分析（行覆盖率、分支覆盖率、函数覆盖率） | reports/coverage/index.html |
| 测试总结报告 | Markdown | 是 | 质量评估、风险分析、发布建议 | docs/test-summary.md |
| 需求-测试追溯矩阵 | Excel/Markdown | 是 | 需求到测试用例的映射关系，确保100%覆盖 | docs/traceability-matrix.xlsx |
| Handover Context | YAML | 是 | 交接给下一阶段的完整上下文 | contexts/handover-{timestamp}.yaml |

### 输出格式要求

#### 测试用例格式
```markdown
### TC-{ID}: {用例名称}
- **关联验收标准**: AC-{ID}
- **优先级**: P0/P1/P2/P3
- **前置条件**: {执行前必须满足的条件}
- **测试数据**: {所需测试数据描述}
- **测试步骤**:
  1. {步骤1}
  2. {步骤2}
  3. {步骤3}
- **预期结果**: {明确可验证的预期行为}
- **实际结果**: {执行后填写}
- **状态**: Pass/Fail/Blocked
- **执行时间**: {timestamp}
- **执行人**: {tester_name}
```

#### 缺陷报告格式
```markdown
### DEFECT-{ID}: {缺陷标题}
- **严重程度**: P0/P1/P2/P3
- **关联测试用例**: TC-{ID}
- **关联验收标准**: AC-{ID}
- **复现步骤**:
  1. {步骤1}
  2. {步骤2}
  3. {步骤3}
- **预期结果**: {期望的行为}
- **实际结果**: {实际观察到的行为}
- **影响范围**: {受影响的功能模块和用户群体}
- **证据**:
  - 截图: {screenshot_path}
  - 日志: {log_path}
- **环境信息**: {URL, 版本号, 配置}
- **提交时间**: {timestamp}
- **提交人**: {tester_name}
- **状态**: Open/In Progress/Resolved/Closed
- **指派给**: {developer_name}
```

#### 测试总结报告格式
```markdown
# Test Summary Report

## 1. 测试概要
- 项目名称: {project_name}
- 测试阶段: {test_phase}
- 测试时间: {start_date} - {end_date}
- 测试人员: {tester_names}
- 测试环境: {environment_info}

## 2. 测试统计
- 总测试用例数: {total}
- 通过: {passed} ({pass_rate}%)
- 失败: {failed} ({fail_rate}%)
- 阻塞: {blocked} ({blocked_rate}%)
- 跳过: {skipped} ({skipped_rate}%)
- 执行率: {execution_rate}%

## 3. 缺陷统计
- 总缺陷数: {total_defects}
- P0 (Critical): {p0_count}
- P1 (Major): {p1_count}
- P2 (Minor): {p2_count}
- P3 (Trivial): {p3_count}
- 已修复: {resolved_count}
- 未修复: {open_count}

## 4. 覆盖率分析
- 需求覆盖率: {req_coverage}%
- 代码覆盖率: {code_coverage}%
  - 行覆盖率: {line_coverage}%
  - 分支覆盖率: {branch_coverage}%
  - 函数覆盖率: {function_coverage}%

## 5. 质量评估
- 质量评分: {quality_score}/100
- 质量等级: {grade}
- KPIs达成情况:
  - TEST-PASS-RATE: {kpi_001_value}% (目标: 90%) - {status}
  - DEFECT-DETECTION: {kpi_002_value}% (目标: 95%) - {status}
  - REQ-TRACE: {kpi_003_value}% (目标: 100%) - {status}
  - TEST-COVERAGE: {kpi_004_value}% (目标: 85%) - {status}

## 6. 遗留风险
- 风险1: {description} - 可能性: {probability} - 影响: {impact}
- 风险2: {description} - 可能性: {probability} - 影响: {impact}

## 7. 发布建议
- 建议: {approved_for_release/approved_with_conditions/not_recommended}
- 条件: {conditions_list}
- 理由: {rationale}

## 8. 后续工作
- 工作1: {description} - 责任人: {owner} - 目标日期: {target_date}
- 工作2: {description} - 责任人: {owner} - 目标日期: {target_date}
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../../scenarios/verify-test/SCENARIO.md` | 测试验证场景定义 |
| Agent | `../../agents/verify-test.agent.md` | 测试验证Agent角色定义 |
| Prompt | `../../prompts/verify-test.prompt.md` | 测试验证提示词模板 |
| Skill | `../../skills/verify-test/SKILL.md` | 测试验证技能包 |

## Related Resources (相关资源)

- **Standards**: 
  - [Testing Best Practices](../standards/testing-best-practices.md) - 测试最佳实践指南
  - [Defect Classification](../standards/defect-classification.md) - 缺陷分类和优先级标准
  - [Test Coverage Guidelines](../standards/test-coverage-guidelines.md) - 测试覆盖率指南
  - [Test Data Management](../standards/test-data-management.md) - 测试数据管理规范
- **Templates**: 
  - [Test Case Template](../templates/test-case.template.md) - 测试用例模板
  - [Defect Report Template](../templates/defect-report.template.md) - 缺陷报告模板
  - [Test Plan Template](../templates/test-plan.template.md) - 测试计划模板
  - [Test Report Template](../templates/test-report.template.md) - 测试报告模板
- **Evaluations**: 
  - [Test Quality Checklist](../evaluations/test-quality-checklist.md) - 测试质量检查清单
  - [Defect Analysis Report](../evaluations/defect-analysis.md) - 缺陷分析报告模板
  - [Coverage Analysis](../evaluations/coverage-analysis.md) - 覆盖率分析指南
