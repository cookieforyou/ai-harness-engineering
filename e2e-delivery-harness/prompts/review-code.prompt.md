---
name: review-code
description: "review code execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: 代码审查场景执行 Prompt

## Purpose

本提示词指导AI执行代码审查任务，作为 **Code Reviewer (代码审查工程师)**，按照代码规范和质量标准对PR变更进行全面审查，识别代码缺陷、安全隐患和优化机会，确保代码质量和团队规范一致性。

### Key Objectives

- **全面变更分析**: 深入理解PR变更范围、影响域和功能关联
- **多维度审查**: 覆盖功能正确性、代码质量、性能、安全、测试五个维度
- **精准问题识别**: 按严重级别分类问题，提供具体可执行的修复建议
- **质量量化评估**: 基于KPI体系量化代码质量，输出结构化审查报告

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `pr_diff` | string | true | PR代码差异内容或Diff链接 | 非空，包含完整的代码变更上下文 |
| `coding_standards` | string | true | 团队编码规范文档路径或内容 | 有效的规范文档，包含命名、格式、架构约定 |
| `security_scan_config` | string | false | 安全扫描配置文件路径 | 有效的配置文件路径或JSON/YAML内容 |
| `review_checklist` | array | false | 审查检查清单（按维度分组） | 至少包含关键检查项，覆盖5个维度 |
| `changed_files` | array | true | 变更文件列表（含路径和变更类型） | 非空，每个元素包含file_path和change_type |
| `author_info` | object | false | 代码作者信息 | 包含name、role、experience_level字段 |
| `test_coverage_report` | string | false | 测试覆盖率报告路径 | 有效的报告文件路径或覆盖率数据 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解PR上下文和变更范围
   ├─ 输入: pr_diff, changed_files, author_info
   ├─ 思考: PR的核心变更是什么？影响哪些模块？是否需要特殊审查关注点？
   ├─ 验证: 确认理解了所有变更文件和其功能关联关系
   └─ 输出: PR上下文摘要（变更范围、影响域、审查关注点清单）
   ↓
[ANALYZE] Step 2: 分析变更影响和技术风险
   ├─ 输入: PR上下文摘要, coding_standards
   ├─ 思考: 变更是否引入破坏性影响？是否有安全/性能/兼容性风险？
   ├─ 验证: 分析覆盖了所有变更文件的潜在影响，无遗漏模块
   └─ 输出: 影响分析报告（风险评估矩阵、兼容性影响表、重点审查区域）
   ↓
[REVIEW] Step 3: 逐文件多维审查代码变更
   ├─ 输入: pr_diff, review_checklist, security_scan_config
   ├─ 执行:
   │   ├─ 功能正确性审查: 业务逻辑是否完整，边界条件是否处理，错误处理是否得当
   │   ├─ 代码质量审查: 命名清晰度、函数长度、设计模式、编码规范符合性
   │   ├─ 性能审查: N+1查询、资源泄漏、算法效率、缓存使用
   │   ├─ 安全审查: 输入验证、注入风险、认证授权、敏感数据处理
   │   └─ 测试审查: 覆盖率达标、边界测试覆盖、异常场景测试
   ├─ 验证: 每个维度至少一个检查点，安全审查不遗漏任何敏感路径
   └─ 输出: 逐文件审查意见（每个问题含文件位置、行号、严重级别、类别、修复建议）
   ↓
[FEEDBACK] Step 4: 生成结构化审查反馈
   ├─ 输入: 逐文件审查意见
   ├─ 思考: 如何组织反馈使之清晰可执行？问题分级是否准确一致？
   ├─ 验证: 每个问题包含确切文件位置和具体可执行的修复建议
   └─ 输出: 结构化审查反馈（按严重级别分组的审查意见汇总 + 改进建议）
   ↓
[VERIFY] Step 5: 验证审查完整性和质量标准
   ├─ 输入: 审查反馈, test_coverage_report, security_scan_config
   ├─ 执行: 覆盖率核对、安全扫描结果验证、规范符合性检查、变更文件覆盖确认
   ├─ 验证: 缺陷检测率≥85%，安全漏洞遗漏率≤5%，审查覆盖率≥95%
   └─ 输出: 审查质量自检报告（覆盖统计、遗漏风险评估、质量验证结果）
   ↓
[APPROVE] Step 6: 综合评估并给出审查结论
   ├─ 输入: 审查反馈, 审查质量自检报告
   ├─ 决策: APPROVED（批准）/ CHANGES_REQUESTED（需修改后批准）/ REJECTED（拒绝）
   ├─ 验证: 审查结论符合质量标准、团队规范，且所有BLOCKER问题已标注
   └─ 输出: 最终审查结论 + 质量评分 + 后续行动项清单
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 代码逻辑不清晰

**识别信号**: 
- 代码存在多种理解方式（≥3种合理理解）
- 关键逻辑缺少注释或文档说明
- 函数过长（>50行）或职责不单一
- 违反SOLID原则导致意图模糊

**处理流程**:
```
IF 代码逻辑难以理解
THEN
  1. 列出所有可能的理解方式（至少2种）
  2. 选择最合理的理解（基于常见约定和上下文线索）
  3. 标记为 [需澄清-逻辑模糊] 并记录具体文件位置和行号
  4. 要求作者补充注释或重构为更清晰的逻辑
  5. IF 影响核心功能判断 THEN 升级为MAJOR级别
  6. 在审查评论中提供具体的重构建议和代码示例
END
```

**降级方案**: 假设合理理解，在审查评论中明确标注"需要作者确认",待作者回复后确认

**升级条件**: BLOCKER级 - 核心业务逻辑错误可能导致生产故障或数据不一致

---

### Error Scenario 2: 安全漏洞检测

**识别信号**: 
- 检测到潜在注入漏洞（SQL/XSS/命令注入）
- 敏感数据（密码、Token、PII）未加密或未脱敏
- 身份认证或授权机制缺失或不正确
- 使用了已知存在CVE漏洞的依赖版本
- 直接拼接用户输入到系统命令或查询

**处理流程**:
```
IF 发现潜在安全漏洞
THEN
  1. 确认漏洞类型、攻击面和可利用性
  2. 评估漏洞严重程度（参考CVSS评分标准）
  3. IF CVSS ≥ 7.0 OR 可直接被外部未认证用户利用 THEN
       a. 立即标记为 BLOCKER 级别
       b. 详细描述漏洞原理和潜在利用方式
       c. 提供具体的修复方案（含修复代码示例）
       d. 要求作者必须在合并前修复
     ELSE
       a. 标记为 MAJOR 级别
       b. 提供安全加固建议
       c. 建议在当前 Sprint 内修复
     END
  4. 记录到安全审查报告中备查
END
```

**降级方案**: 针对低风险（CVSS < 4.0）漏洞，建议创建技术债务条目在后续迭代修复

**升级条件**: 任何可直接被外部利用的安全漏洞，无论严重程度，均需上报安全团队

---

### Error Scenario 3: 测试覆盖不足

**识别信号**: 
- 新增代码测试覆盖率 < 70%
- 关键业务路径（核心if-else分支）缺乏测试
- 边界条件和异常场景未覆盖
- Mock对象使用过多，缺少真实集成测试
- 覆盖率报告显示明显缺失的代码块

**处理流程**:
```
IF 测试覆盖不足
THEN
  1. 分析覆盖率报告，精确识别未覆盖区域的代码行和分支
  2. 区分核心业务逻辑和非核心逻辑
  3. 列出需要补充的测试场景清单（含输入和期望输出）
  4. IF 核心业务逻辑覆盖率 < 80% THEN
       a. 标记为 BLOCKER 级别
       b. 要求作者补充核心路径的测试用例
       c. 提供测试用例模板参考
     ELSE
       a. 标记为 MAJOR 级别
       b. 列出需要补充的测试场景
       c. 建议在合并前或紧接着的提交中补充
     END
  5. 标注必须覆盖的关键路径和边界条件
END
```

**降级方案**: 非核心逻辑（工具函数、配置代码）可接受较低覆盖率，但需记录技术债务

**升级条件**: 核心业务逻辑测试覆盖率 < 60%，或新增代码无任何测试

## Quality Score (质量评分)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 权重 | 计算公式 | 验证方法 |
|--------|----------|--------|------|----------|----------|
| KPI-001 | DEFECT-DETECTION | ≥85% | 30% | (审查发现的缺陷数 / 后续确认的总缺陷数) × 100% | 对比审查后Bug追踪中的缺陷统计 |
| KPI-002 | REVIEW-TURNAROUND | ≤4h | 30% | PR提交时间到审查完成时间的间隔(小时) | 时间戳记录，含首次评论到最终结论 |
| KPI-003 | SECURITY-FINDINGS | 遗漏率≤5% | 20% | (遗漏的安全漏洞数 / 总安全漏洞数) × 100% | 安全扫描结果与审查发现对比 |
| KPI-004 | REVIEW-COVERAGE | ≥95% | 20% | (已审查文件数 / 总变更文件数) × 100% | 文件级别覆盖率逐文件核对 |

**综合评分计算**:
```
Quality Score = (DEFECT-DETECTION_SCORE × 0.30) + (TURNAROUND_SCORE × 0.30) + (SECURITY_SCORE × 0.20) + (COVERAGE_SCORE × 0.20)

DEFECT-DETECTION_SCORE  = min(100, actual_rate / 85% × 100)
TURNAROUND_SCORE        = IF actual_time ≤ 4h THEN 100 ELSE max(0, 100 - (actual_time - 4) × 10)
SECURITY_SCORE          = IF leak_rate ≤ 5% THEN 100 ELSE max(0, 100 - (leak_rate - 5) × 10)
COVERAGE_SCORE          = min(100, actual_coverage / 95% × 100)

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Validation (输出验证)

> **AI 在提交审查结论前，必须完成以下验证步骤**

### Review Validation Checklist

**V-001: Completeness Validation (完整性验证)**
- [ ] All changed files in `changed_files` have been reviewed
- [ ] No file is skipped or partially reviewed
- [ ] Review covers all 5 dimensions (correctness, quality, performance, security, testing)
- [ ] All review comments reference specific code locations (file:line)
- [ ] Review coverage ≥ 95% of total changed files

**V-002: Accuracy Validation (准确性验证)**
- [ ] Issue severity classification is correct and consistent across all findings
- [ ] All reported issues are reproducible from the diff context
- [ ] Fix suggestions are actionable and contain specific code recommendations
- [ ] No false positives in security findings (verified against security scan config)
- [ ] Severity distribution is reasonable (BLOCKER < MAJOR < MINOR)

**V-003: Actionability Validation (可执行性验证)**
- [ ] Each issue has a clear fix recommendation or specific suggestion
- [ ] Code examples provided for complex or non-obvious fixes
- [ ] Reference links to coding standards or best practices included
- [ ] Priority levels clearly indicate required actions (must fix vs. optional)
- [ ] For BLOCKER issues: exact fix code or detailed steps provided

**V-004: Quality Standards Validation (质量标准验证)**
- [ ] Defect detection rate meets ≥ 85% target
- [ ] Review turnaround time meets ≤ 4 hours target
- [ ] Zero P0/P1 security vulnerabilities are missed (leak rate ≤ 5%)
- [ ] Review conclusion is consistent with findings severity
- [ ] Overall quality score calculated and documented

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and severity level
  2. IF completeness (V-001) or accuracy (V-002) check fails THEN re-review affected files
  3. IF critical security issue missed (V-004) THEN escalate to security team immediately
  4. Generate validation report with pass/fail status for each check
  5. IF BLOCKER-level validation failures exist THEN do not finalize review
  6. Document all validation results in the review report
END
```

## Execution Flow (执行流程)

> **领域特定的代码审查执行流程，替代通用Phase模式**

### Phase 1: 审查准备 (Review Preparation)

**目标**: 理解PR上下文，确定审查策略和关注重点

1. **变更范围评估**
   - 统计变更文件数量和类型（新增/修改/删除）
   - 识别核心变更文件和辅助变更文件
   - 评估变更影响边界和风险等级
   - 确定变更所属模块/功能域

2. **审查策略制定**
   - 根据变更类型（功能新增/重构/修复）确定审查重点领域
   - 制定审查优先级排序（高影响区域优先审查）
   - 准备参考资源（编码规范、安全基线、检查清单）

3. **上下文理解**
   - 阅读PR描述和关联Issue
   - 了解业务需求背景
   - 确认自动化检查（Lint/CI）结果

**输出**: PR上下文摘要 + 审查策略计划 + 重点关注区域清单

### Phase 2: 深度审查执行 (Deep Review Execution)

**目标**: 对每项变更进行逐文件多维度审查，识别所有质量问题

1. **逐文件多维度审查**
   - 按优先级顺序对变更文件进行审查
   - 对每个文件执行5维度审查矩阵
   - 记录每个发现的问题（文件路径、行号、问题描述、分级、修复建议）

2. **问题分类和严重级别标定**
   - BLOCKER: 阻塞性问题，必须修复（功能逻辑错误、安全漏洞、严重性能问题）
   - MAJOR: 主要问题，建议修复（代码可读性、测试覆盖不足、潜在风险）
   - MINOR: 次要问题，可选修复（编码风格不一致、微小优化建议）
   - COMMENT: 评论建议（架构讨论、经验分享、长期改进建议）

3. **交叉引用和一致性验证**
   - 验证文件间变更的接口契约匹配
   - 检查前后端/模块间变更的一致性
   - 确认异常处理链完整
   - 验证配置变更与环境要求一致

**输出**: 逐文件审查意见清单 + 问题分类汇总

### Phase 3: 审查总结与输出 (Review Summary & Output)

**目标**: 综合评估代码质量，生成结构化审查报告

1. **质量评分计算**
   - 基于KPI体系计算各项指标得分
   - 综合加权计算总体质量评分
   - 确定审查结论: APPROVED / CHANGES_REQUESTED / REJECTED

2. **结构化报告生成**
   - 按Output Format模板组织审查结果
   - 包含问题分类统计、质量评分、行动项
   - 提供改进建议和最佳实践参考

3. **自检与交接准备**
   - 执行Output Validation检查清单
   - 确认审查完整无遗漏
   - 准备审查交接上下文

**输出**: 最终审查报告 + 质量评分 + 审查结论 + 后续行动项

## Output Format (输出格式)

> AI必须按照以下结构化模板生成代码审查交付物

```markdown
# Code Review Report

## 1. Review Summary

### 1.1 PR Information
- **PR Number**: {pr_number}
- **Branch**: {branch_name} → {base_branch}
- **Author**: {author}
- **Reviewer**: {reviewer}
- **Review Date**: {current_date}
- **Status**: APPROVED / CHANGES_REQUESTED / REJECTED

### 1.2 Change Statistics
| Metric | Value |
|--------|-------|
| Files Changed | {N} |
| Lines Added | {N} |
| Lines Deleted | {N} |
| Languages | {languages} |

### 1.3 Review Coverage
| Module | Total Files | Reviewed | Coverage |
|--------|-------------|----------|----------|
| {module} | {N} | {N} | {X}% |
| **Total** | **{N}** | **{N}** | **{X}%** |

## 2. Review Findings

### 2.1 Issue Summary
| Severity | Count | Action Required |
|----------|-------|-----------------|
| BLOCKER | {N} | Must fix before merge |
| MAJOR | {N} | Recommended to fix |
| MINOR | {N} | Optional |
| COMMENT | {N} | Discuss |
| **Total** | **{N}** | |

### 2.2 BLOCKER Issues
| # | File | Line | Category | Description | Suggestion |
|---|------|------|----------|-------------|------------|
| 1 | {file_path} | {L} | {category} | {description} | {suggestion} |

### 2.3 MAJOR Issues
| # | File | Line | Category | Description | Suggestion |
|---|------|------|----------|-------------|------------|

### 2.4 MINOR Issues
| # | File | Line | Category | Description | Suggestion |
|---|------|------|----------|-------------|------------|

### 2.5 Comments
| # | File | Line | Description |
|---|------|------|-------------|

## 3. Five-Dimension Assessment

| Dimension | Score (1-5) | Key Findings |
|-----------|-------------|--------------|
| 功能正确性 Functional Correctness | {X}/5 | {key_findings} |
| 代码质量 Code Quality | {X}/5 | {key_findings} |
| 性能评估 Performance | {X}/5 | {key_findings} |
| 安全审查 Security | {X}/5 | {key_findings} |
| 测试覆盖 Testing | {X}/5 | {key_findings} |
| **Overall** | **{X}/5** | |

## 4. Quality Score

### 4.1 KPI Results
| KPI ID | Metric | Target | Actual | Score | Weight | Weighted |
|--------|--------|--------|--------|-------|--------|----------|
| KPI-001 | DEFECT-DETECTION | ≥85% | {X}% | {S} | 30% | {W} |
| KPI-002 | REVIEW-TURNAROUND | ≤4h | {X}h | {S} | 30% | {W} |
| KPI-003 | SECURITY-FINDINGS | 遗漏率≤5% | {X}% | {S} | 20% | {W} |
| KPI-004 | REVIEW-COVERAGE | ≥95% | {X}% | {S} | 20% | {W} |

### 4.2 Overall Score
- **Total Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)

## 5. Action Items

### 5.1 Required Actions (Must Fix Before Merge)
- [ ] {action item with file reference}
- [ ] {action item with file reference}

### 5.2 Recommended Actions (Fix in Current Sprint)
- [ ] {action item}

### 5.3 Improvement Suggestions (For Future Sprints)
- [ ] {suggestion}

## 6. Best Practices & Recommendations

1. **{recommendation_title}**: {detailed_recommendation}
2. **{recommendation_title}**: {detailed_recommendation}
3. **{recommendation_title}**: {detailed_recommendation}
```

## Handover Context (交接上下文)

> 完成代码审查后，生成以下交接信息

```yaml
handover:
  review_id: "CR-{pr_number}-{timestamp}"
  reviewer: "{agent_name}"
  review_date: "{ISO8601}"
  pr_info:
    pr_number: {pr_number}
    branch: "{branch_name}"
    base_branch: "{base_branch}"
    author: "{author}"
  summary:
    status: "approved/changes_requested/rejected"
    quality_score: {0-100}
    grade: "excellent/good/satisfactory/needs_improvement"
    issue_breakdown:
      total: {N}
      blocker: {N}
      major: {N}
      minor: {N}
      comment: {N}
  artifacts:
    - name: "Review Report"
      path: "reviews/review-{pr_number}.md"
    - name: "Issue List"
      path: "reviews/issues-{pr_number}.csv"
  kpi_results:
    defect_detection:
      value: {X}
      target: 85
      unit: "%"
      status: "pass/fail"
    review_turnaround:
      value: {X}
      target: 4
      unit: "hours"
      status: "pass/fail"
    security_findings_leak:
      value: {X}
      target: 5
      unit: "%"
      status: "pass/fail"
    review_coverage:
      value: {X}
      target: 95
      unit: "%"
      status: "pass/fail"
  next_steps:
    - "Author addresses BLOCKER and MAJOR issues"
    - "Re-review after fixes (if CHANGES_REQUESTED)"
    - "Merge after all BLOCKER issues resolved"
```

## Execution Constraints

1. **客观公正**: 基于代码规范和最佳实践评价，不针对个人
2. **建设性**: 提供具体可行的改进建议，而非简单批评
3. **高效**: 优先关注高风险问题，审查时间≤4小时
4. **安全优先**: 重点审查安全敏感代码，零遗漏容忍

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/review-code/SCENARIO.md` | 代码审查场景定义 |
| Agent | `../agents/review-code.agent.md` | 代码审查Agent角色 |
| Skill | `../skills/review-code/SKILL.md` | 代码审查技能包 |
| Instruction | `../instructions/review-code.instructions.md` | 代码审查技术指令 |

## Related Resources (相关资源)

- **Standards**:
  - [Coding Standards](../standards/coding-standards.md) - 团队编码规范
  - [Code Review Checklist](../standards/code-review-checklist.md) - 审查检查清单
  - [Security Baseline](../standards/security-baseline.md) - 安全基线规范
- **Templates**:
  - [Review Comment Template](../templates/review-comment.template.md) - 审查评论模板
- **Evaluations**:
  - [Code Quality Checklist](../evaluations/code-quality-checklist.md) - 代码质量评估

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md) 生成交接上下文。
