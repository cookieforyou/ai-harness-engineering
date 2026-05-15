---
name: implement-feature
description: "Technical instructions for feature implementation execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [instruction, technical, development]
---
# Feature Implementation Instructions

## Purpose

本文档定义了功能实现阶段的标准操作流程、质量检查标准和工作产出规范。功能实现是按照任务规格完成高质量代码开发、单元测试和文档更新的过程，为测试验证阶段提供可靠的代码交付物。

### Business Value

- **保证代码质量**: 通过编码规范、单元测试和代码审查确保代码符合质量标准
- **提升开发效率**: 标准化的开发流程和最佳实践减少返工和调试时间
- **降低技术债务**: 遵循SOLID原则和设计模式，保持代码的可维护性和可扩展性
- **增强可追溯性**: 清晰的代码注释、文档和Git提交历史便于问题定位和知识传承
- **提高团队协作**: 统一的编码规范和代码审查流程促进团队知识共享和质量提升

## Investigation Flow

### 流程概览

```
任务理解 → 技术方案 → 代码设计 → 编码实现 → 质量自检 → 交接准备
```

### 步骤 1：任务理解与需求分析

**目的**：深入理解任务需求和验收标准，确认无歧义

**输入**：
- 任务规格说明书（task_spec）
- 验收标准列表（acceptance_criteria）
- 相关设计文档（design_reference）

**操作**：

1. **需求阅读与分析**
   - 仔细阅读任务规格，理解业务背景和核心目标
   - 识别用户故事中的角色、功能、价值三要素
   - 提取关键业务规则和技术要求

2. **验收标准检查**
   - 逐条检查验收标准，确认符合SMART原则
   - 标记模糊或有歧义的验收标准
   - 列出所有可能的理解方式（如有歧义）
   - 主动与产品经理或Tech Lead沟通澄清

3. **依赖识别**
   - 识别外部依赖（第三方库、API接口、数据库表）
   - 识别内部依赖（其他模块、共享服务）
   - 确认依赖可用性和版本兼容性

4. **风险评估**
   - 识别潜在的技术风险和难点
   - 评估风险的影响程度和发生概率
   - 制定初步的应对策略

5. **任务理解备忘录编写**
   - 记录需求摘要和关键点
   - 列出疑问清单和待确认事项
   - 明确任务范围和边界

**输出**：任务理解备忘录（包含需求摘要、关键点、疑问清单、依赖清单、风险评估）

**质量标准**：
- 所有验收标准清晰明确，无模糊表述
- 外部依赖已识别并确认可用
- 技术风险已评估并有应对方案
- 任务范围和边界已明确

---

### 步骤 2：技术方案设计与依赖分析

**目的**：制定具体的技术实现方案，分析依赖和风险

**输入**：
- 任务理解备忘录
- 系统设计文档
- 编码规范
- 技术栈信息

**操作**：

1. **架构对齐**
   - 参考系统设计文档，确认实现方案符合整体架构
   - 识别需要遵循的架构约束和设计决策
   - 确认模块边界和接口契约

2. **技术选型**
   - 选择合适的编程语言、框架、库
   - 考虑团队熟悉度、社区支持、长期维护成本
   - 评估技术选型的风险和收益

3. **类/接口设计**
   - 设计类结构、职责划分、继承关系
   - 定义接口契约（方法签名、参数、返回值、异常）
   - 绘制类图，标注关键属性和方法

4. **流程设计**
   - 设计关键业务流程和算法
   - 绘制时序图或流程图，展示对象交互
   - 识别并发场景和同步需求

5. **数据模型设计**
   - 设计DTO、Entity、VO等数据对象
   - 定义字段类型、约束、验证规则
   - 考虑数据持久化策略（数据库、缓存）

6. **依赖管理**
   - 列出所有外部依赖（库、服务、API）
   - 确认版本兼容性和许可证
   - 解决版本冲突（如有）

7. **风险评估与缓解**
   - 评估技术风险（性能、安全、兼容性）
   - 制定缓解措施和应急预案
   - 识别需要技术调研的领域（technical spike）

8. **方案评审（如需要）**
   - 复杂任务进行方案评审
   - 获得Tech Lead或架构师批准
   - 记录评审结论和修改建议

**输出**：技术实现方案（包含类图、时序图、依赖清单、风险评估、备选方案）

**质量标准**：
- 实现方案符合架构设计，无偏差
- 技术选型合理，有明确的理由
- 类图和接口设计清晰，符合SOLID原则
- 所有依赖已识别，版本冲突已解决
- 技术风险已评估并有缓解措施

---

### 步骤 3：代码结构设计与接口定义

**目的**：设计清晰的代码结构和接口，确保可维护性

**输入**：
- 技术实现方案
- 编码规范
- 项目目录结构约定

**操作**：

1. **目录结构设计**
   - 按照项目约定组织代码目录
   - 区分主代码、测试代码、资源文件
   - 模块化组织，便于导航和维护

2. **类职责划分**
   - 每个类只负责一个职责（Single Responsibility）
   - 避免God Class（方法数>10或行数>500）
   - 使用组合优于继承

3. **接口定义**
   - 定义清晰的接口契约
   - 方法命名清晰，表达意图
   - 参数数量≤5个，超过则使用对象封装
   - 定义返回值类型和可能的异常

4. **数据模型设计**
   - 设计DTO（Data Transfer Object）用于层间传输
   - 设计Entity用于数据持久化
   - 设计VO（View Object）用于前端展示
   - 明确字段类型、约束、验证规则

5. **异常处理策略**
   - 定义统一的异常类型层次结构
   - 定义错误码规范（业务错误码、系统错误码）
   - 设计异常处理流程（捕获、记录、转换、抛出）

6. **日志策略**
   - 确定日志级别使用规范（DEBUG/INFO/WARN/ERROR）
   - 定义日志格式（时间、级别、线程、类名、消息）
   - 标识关键业务流程的日志点

7. **配置管理**
   - 外部化配置，避免硬编码
   - 支持不同环境（dev/test/prod）的配置
   - 敏感信息使用密钥管理服务

**输出**：代码结构设计文档（包含目录结构、类图、接口定义、数据模型、异常策略）

**质量标准**：
- 目录结构清晰，符合项目约定
- 每个类职责单一，无God Class
- 接口定义清晰，参数和返回值明确
- 数据模型完整，字段类型和约束正确
- 异常处理策略统一，错误码规范
- 日志策略合理，便于问题排查
- 配置外部化，无硬编码值

---

### 步骤 4：编码实现与单元测试编写

**目的**：按照规范编写高质量的代码和充分的单元测试

**输入**：
- 代码结构设计
- 编码规范
- 验收标准
- 测试框架

**操作**：

1. **编码规范遵循**
   - 严格遵循团队编码规范（命名、缩进、注释、导入顺序）
   - 使用IDE的代码格式化功能
   - 运行lint工具检查代码风格

2. **命名规范**
   - 变量名：名词或名词短语，表达含义（userName, orderList）
   - 函数名：动词或动词短语，表达行为（getUser, calculateTotal）
   - 类名：名词，表达概念（UserService, OrderProcessor）
   - 常量名：全大写，下划线分隔（MAX_RETRY_COUNT）
   - 避免缩写和单字母变量（除非是循环计数器i/j/k）

3. **函数设计**
   - 函数长度<50行（推荐），最多不超过100行
   - 每个函数只做一件事（Single Responsibility）
   - 参数数量≤5个，超过则使用对象封装
   - 返回值明确，避免返回null（使用Optional或空集合）

4. **注释添加**
   - 为复杂逻辑添加注释，说明"为什么"而不是"做什么"
   - public API添加Javadoc/docstring，说明用途、参数、返回值、异常
   - TODO注释标记未完成的工作，包含责任人和建议完成时间
   - 避免冗余注释（代码已经很清晰的地方不需要注释）

5. **DRY原则应用**
   - 识别重复代码（相似代码出现≥2次）
   - 提取公共逻辑为独立函数或类
   - 使用模板方法或策略模式消除条件重复

6. **异常处理**
   - 捕获具体异常，避免catch (Exception e)
   - 提供有意义的错误信息，包含上下文
   - 记录日志后再抛出或处理
   - 不要在catch块中吞掉异常（empty catch block）

7. **单元测试编写**（TDD推荐）
   - **Red**: 先写失败的测试用例
   - **Green**: 编写最少的代码使测试通过
   - **Refactor**: 重构代码，保持测试通过
   - 覆盖正常路径、异常路径、边界条件
   - 使用Given-When-Then格式组织测试
   - Mock外部依赖，隔离测试单元
   - 测试用例命名清晰，描述测试场景

8. **增量开发与测试**
   - 小步实现，每完成一个小功能就编写测试
   - 频繁运行测试，确保新代码不破坏现有功能
   - 使用CI/CD pipeline自动执行测试

**输出**：源代码文件 + 单元测试代码

**质量标准**：
- 代码遵循编码规范，lint检查通过
- 命名清晰有意义，无缩写和单字母变量
- 函数长度适中，职责单一
- 注释完整，关键逻辑有详细说明
- 无重复代码，DRY原则已应用
- 异常处理完整，错误信息清晰
- 单元测试覆盖核心逻辑和边界条件
- 测试覆盖率≥80%，核心逻辑100%覆盖
- 所有测试用例通过，无失败用例

---

### 步骤 5：质量自检与优化

**目的**：执行全面的质量检查，确保代码符合标准

**输入**：
- 源代码
- 单元测试代码
- 质量检查工具

**操作**：

1. **代码规范检查**
   - 运行lint工具（ESLint、Checkstyle、Pylint等）
   - 修复所有errors
   - 尽量减少warnings（目标：<10个）

2. **静态代码分析**
   - 运行SonarQube或类似工具
   - 修复所有critical和major issues
   - 记录minor和info issues，后续迭代处理

3. **圈复杂度检查**
   - 检查单个函数的圈复杂度
   - 确保圈复杂度≤15（目标：≤10）
   - 超过阈值的函数进行重构或拆分

4. **重复代码检测**
   - 使用工具检测重复代码（PMD CPD、SonarQube）
   - 提取公共逻辑为独立函数或类
   - 目标：重复率 < 3%

5. **安全扫描**
   - 运行安全扫描工具（Snyk、OWASP Dependency-Check）
   - 修复所有high severity vulnerabilities
   - 评估medium和low severity vulnerabilities

6. **性能检查**
   - 识别性能瓶颈（N+1查询、inefficient algorithms）
   - 检查内存使用情况（内存泄漏、大对象持有）
   - 优化数据库查询（索引、JOIN、分页）
   - 合理使用缓存

7. **代码审查准备**
   - 自查代码，对照代码审查清单
   - 准备PR描述，包含变更说明、测试说明、审查要点
   - 标注重点关注区域（复杂逻辑、新技术应用）

**输出**：自检报告 + 测试报告 + 覆盖率报告 + 静态分析报告

**质量标准**：
- Lint检查通过，无errors，warnings < 10
- Sonar issues = 0（critical/major），或仅有info级别
- 圈复杂度≤15（单个函数），平均值≤10
- 无重复代码，或重复率 < 3%
- 安全扫描无高危漏洞
- 无明显性能瓶颈

---

### 步骤 6：文档更新与交接准备

**目的**：同步更新相关文档，准备完整的交接材料

**输入**：
- 源代码
- 测试结果
- 质量检查报告

**操作**：

1. **API文档更新**
   - 如API有变更，更新OpenAPI/Swagger文档
   - 包含请求/响应示例
   - 说明参数约束和验证规则
   - 标注breaking changes

2. **代码注释完善**
   - 确保public API有Javadoc/docstring
   - 关键逻辑有详细注释，说明"为什么"
   - 复杂算法有伪代码或流程图说明

3. **README更新**
   - 如新增模块或功能，更新README
   - 说明使用方法、配置项、注意事项
   - 添加示例代码或使用场景

4. **CHANGELOG编写**
   - 添加本次变更记录
   - 分类记录：Added（新功能）、Changed（变更）、Fixed（bug修复）、Deprecated（废弃）、Removed（删除）、Security（安全修复）
   - 遵循Semantic Versioning规范

5. **技术决策记录**
   - 记录关键技术决策和权衡考虑
   - 说明选择某个方案的理由
   - 记录备选方案和未选择的理由
   - 便于后续追溯和理解

6. **Handover Context生成**
   - 填写交接模板，包含：
     - summary（状态、完成度、质量评分、代码统计）
     - artifacts（交付物清单，含checksum）
     - decisions（关键决策和理由）
     - open_issues（开放问题和风险）
     - recommendations（测试建议）
     - quality_metrics（KPI结果）
   - 确保所有必需字段完整
   - 计算质量评分，确保≥70分

7. **Pull Request创建**
   - 创建PR，选择正确的目标分支
   - 填写PR描述，包含：
     - 变更说明（What changed）
     - 变更原因（Why）
     - 测试说明（How tested）
     - 审查要点（What to review）
   - 指定reviewers（至少2人）
   - 标注labels（feat/fix/refactor等）
   - 关联issue号（Closes #XXX）

**输出**：更新后的文档 + Handover Context + Pull Request

**质量标准**：
- API文档已更新（如API有变更）
- 代码注释完整，关键逻辑有详细说明
- README已更新（如需要）
- CHANGELOG已添加本次变更记录
- 技术决策已记录
- Handover Context字段完整，质量评分≥70分
- Pull Request已创建，描述清晰

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 代码规范 | 遵循团队编码规范 | Lint工具检查 | errors=0, warnings<10 |
| 功能实现 | 所有验收标准已实现 | AC逐条核对 | 100% AC通过 |
| 测试覆盖 | 核心逻辑100%覆盖，整体≥80% | 覆盖率报告 | coverage ≥80%, critical=100% |
| 静态分析 | 无critical/major issues | SonarQube检查 | critical/major issues=0 |
| 安全扫描 | 无高危漏洞 | 安全扫描工具 | high vulnerabilities=0 |
| 代码审查 | PR已创建，reviewers指定 | Git平台检查 | PR状态=open, reviewers≥2 |
| 文档同步 | API文档、CHANGELOG已更新 | 文档检查 | 所有必需文档已更新 |
| 质量评分 | 综合评分≥70分 | KPI计算 | score ≥70 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 性能考虑 | 无明显性能瓶颈 | Profiler检查 | 响应时间符合要求 |
| 错误处理 | 异常情况有妥善处理 | 代码审查 | 关键异常已处理并记录日志 |
| 日志完整性 | 关键业务流程有日志 | 日志检查 | 关键节点有INFO/ERROR日志 |
| 可配置性 | 无硬编码值 | 代码扫描 | 所有配置项外部化 |
| 国际化 | 用户可见文本支持i18n | 代码检查 | 无硬编码字符串（如适用） |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 | 计算方法 |
|------|------|------|----------|
| 功能正确性 | 所有验收标准已实现并通过验证 | 35% | (通过的AC数/总AC数) × 100% |
| 代码质量 | 遵循编码规范，无严重issues | 25% | 100 - (lint_errors×10 + sonar_critical×20 + sonar_major×10) |
| 测试覆盖 | 核心逻辑100%覆盖，整体≥80% | 20% | min(100, (实际覆盖率/80) × 100) |
| 文档完整 | API文档、注释、CHANGELOG已更新 | 20% | (已更新文档数/必需文档数) × 100% |

### 评分标准

| 等级 | 分值 | 描述 | 行动 |
|------|------|------|------|
| 卓越 | 95-100 | 代码质量优秀，测试充分，文档完整，可直接合并 | 无需修改，直接合并 |
| 优秀 | 85-94 | 代码质量良好，有小幅改进空间，不影响功能 | 记录改进建议，可合并 |
| 良好 | 70-84 | 满足核心要求，有优化空间，需在后续迭代完善 | 标注待完善项，可合并 |
| 合格 | 60-69 | 基本可用，需补充不完整项，可能影响质量 | 补充缺失项后再合并 |
| 不合格 | <60 | 不满足基本要求，存在重大缺陷 | 重新实现或大幅修改 |

### 质量评分计算

```
Quality Score = (Functionality × 0.35) + (Code Quality × 0.25) + (Test Coverage × 0.20) + (Documentation × 0.20)

示例计算:
Functionality = 100% (5/5 AC通过)
Code Quality = 100 - (0×10 + 0×20 + 0×10) = 100
Test Coverage = min(100, (85/80) × 100) = 100
Documentation = 100% (4/4文档已更新)

Quality Score = (100 × 0.35) + (100 × 0.25) + (100 × 0.20) + (100 × 0.20)
              = 35 + 25 + 20 + 20
              = 100分 (卓越)
```

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 | 文件路径示例 |
|------|------|------|------|--------------|
| 源代码 | .java/.py/.js/.ts等 | 是 | 实现的功能代码，含注释 | src/{feature_path}/ |
| 单元测试 | test files | 是 | 测试用例代码 | tests/{test_path}/ |
| 测试报告 | HTML/XML | 是 | 测试执行结果和覆盖率 | reports/test-report.html |
| 覆盖率报告 | HTML | 是 | 详细的覆盖率分析 | reports/coverage/index.html |
| API文档 | Markdown/OpenAPI YAML | 如API变更 | API接口说明和示例 | docs/api-spec.md |
| CHANGELOG | Markdown | 是 | 本次变更记录 | CHANGELOG.md |
| Handover Context | YAML | 是 | 交接给测试阶段的上下文 | contexts/handover-DEV-{timestamp}.yaml |
| Pull Request | Git PR | 是 | 代码审查请求 | GitHub/GitLab PR |

### 产出模板

功能实现交付物应包含以下内容：

```markdown
# Feature Implementation Deliverables

## 1. Task Information
- **Task ID**: {task_id}
- **Task Name**: {task_name}
- **Developer**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed/Partial/Blocked

## 2. Implementation Summary

### 2.1 Acceptance Criteria Status
| AC ID | Acceptance Criteria | Status | Notes |
|-------|---------------------|--------|-------|
| AC-001 | {criteria description} | ✅ Pass / ⚠️ Partial / ❌ Fail | {explanation} |

### 2.2 Work Effort
- **Planned Effort**: {X} person-days
- **Actual Effort**: {Y} person-days
- **Variance**: {Z}%

## 3. Code Changes

### 3.1 New Files
| File Path | Description | Lines |
|-----------|-------------|-------|
| src/{path}/{file}.java | {description} | {N} |

### 3.2 Modified Files
| File Path | Changes Description | Lines Added/Deleted |
|-----------|---------------------|---------------------|
| src/{path}/{file}.java | {description} | +{N}/-{M} |

### 3.3 Code Statistics
- **Total Lines Added**: {N}
- **Total Lines Modified**: {M}
- **Total Lines Deleted**: {K}
- **Files Changed**: {count}
- **Commits Count**: {count}

## 4. Test Results

### 4.1 Unit Test Summary
- **Total Test Cases**: {N}
- **Passed**: {N}
- **Failed**: {0}
- **Skipped**: {0}

### 4.2 Coverage Report
- **Overall Coverage**: {X}% (target: 80%)
- **Critical Logic Coverage**: {Y}% (target: 100%)
- **Line Coverage**: {X}%
- **Branch Coverage**: {Y}%

## 5. Code Quality Metrics

### 5.1 Static Analysis Results
- **Lint Errors**: {0} (target: 0)
- **Lint Warnings**: {N} (target: <10)
- **Sonar Issues**: {N} (target: 0 critical/major)
- **Cyclomatic Complexity**: Avg {X}, Max {Y} (target: ≤15)

### 5.2 Security Scan
- **High Vulnerabilities**: {0} (target: 0)
- **Medium Vulnerabilities**: {N}
- **Low Vulnerabilities**: {M}

## 6. Design Decisions

### 6.1 Key Decisions
| Decision ID | Description | Rationale | Alternatives Considered |
|-------------|-------------|-----------|-------------------------|
| DC-001 | {decision} | {rationale} | [Option A, Option B] |

## 7. Documentation Updates

### 7.1 Updated Documents
- [ ] API Documentation (docs/api-spec.md) - Version {version}
- [ ] README.md - Section {section} updated
- [ ] CHANGELOG.md - Entry added for this feature
- [ ] Code Comments - Added to {N} files

## 8. Open Issues & Risks

### 8.1 Open Issues
| Issue ID | Description | Severity | Planned Resolution | Owner | Target Date |
|----------|-------------|----------|--------------------|-------|-------------|
| ISSUE-001 | {description} | Low/Medium/High | {plan} | {owner} | {date} |

### 8.2 Risks
| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|--------------|
| RISK-001 | {description} | Low/Medium/High | Low/Medium/High | {mitigation} |

## 9. Recommendations for Testing

1. **Focus Areas**: 
   - {area 1}: {reason}
   - {area 2}: {reason}

2. **Test Scenarios**:
   - Scenario 1: {description}
   - Scenario 2: {description}

## 10. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - CODE-COVERAGE: {value}% (target: 80%) - {pass/fail}
  - BUG-DENSITY: {value}/KLOC (target: ≤0.5) - {pass/fail}
  - CYCLOMATIC: {value} (target: ≤15) - {pass/fail}
  - REVIEW-PASS: {value}% (target: 100%) - {pass/fail}
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/implement-feature/SCENARIO.md` | 功能实现场景定义 |
| Agent | `../agents/implement-feature.agent.md` | 功能实现Agent角色 |
| Prompt | `../prompts/implement-feature.prompt.md` | 功能实现提示词模板 |
| Skill | `../skills/implement-feature/SKILL.md` | 功能实现技能包 |

## Related Resources (相关资源)

- **Standards**: 
  - [Coding Standards](../standards/coding-standards.md) - 团队编码规范
  - [Testing Guidelines](../standards/testing-guidelines.md) - 测试编写指南
  - [Git Workflow](../standards/git-workflow.md) - Git分支管理和提交规范
  - [Code Review Checklist](../standards/code-review-checklist.md) - 代码审查检查清单
- **Templates**: 
  - [Pull Request Template](../templates/pull-request.template.md) - PR模板
  - [Commit Message Convention](../templates/commit-message-convention.md) - Commit消息规范
  - [API Documentation Template](../templates/api-doc.template.md) - API文档模板
- **Evaluations**: 
  - [Code Quality Checklist](../evaluations/code-quality-checklist.md) - 代码质量检查清单
  - [Test Coverage Analysis](../evaluations/test-coverage-analysis.md) - 测试覆盖率分析
  - [Static Code Analysis Report](../evaluations/static-code-analysis.md) - 静态代码分析报告
