---
name: implement-feature
description: "按照任务清单完成代码开发、单元测试和文档更新，确保代码质量"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: [skill, knowledge, development]
---
# Feature Implementation Skill

## Skill Overview

本技能包提供功能实现的专业知识、最佳实践和常见陷阱，指导AI高质量地完成从任务规格到代码实现的转换，确保代码质量、可维护性和测试覆盖。

### Core Competencies

- **代码实现**: 根据任务规格编写清晰、高效、符合规范的源代码
- **测试驱动开发**: 编写全面的单元测试，核心逻辑100%覆盖，整体≥80%
- **质量保障**: 通过静态分析、代码审查和安全扫描确保代码质量
- **SOLID原则应用**: 遵循单一职责、开闭原则、里氏替换、接口隔离、依赖倒置
- **设计模式运用**: 合理使用常见设计模式（工厂、策略、观察者等）提高代码可维护性
- **性能优化**: 识别和优化性能瓶颈，避免N+1查询、内存泄漏等问题
- **安全编码**: 应用安全最佳实践，防止SQL注入、XSS、CSRF等常见漏洞

## Use When

使用此技能的场景：

- 任务分解完成后，需要进行编码实现
- 需要实现特定功能模块或用户故事
- 需要修复代码缺陷或bug
- 需要进行代码重构以提高可维护性
- 需要优化性能或解决技术问题

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 | 验证要求 |
|--------|------|------|----------|
| 任务规格 | markdown | 包含用户故事、验收标准、技术要求 | 长度 > 100字符，AC符合SMART原则 |
| 技术栈 | 列表 | 使用的编程语言、框架、库 | 有效的技术名称列表 |

### 可选输入

| 输入项 | 类型 | 描述 | 用途 |
|--------|------|------|------|
| 设计文档 | 文件 | 系统设计、架构设计、接口定义 | 参考实现方案和技术选型 |
| 编码规范 | 文件 | 团队编码规范和风格指南 | 确保代码一致性 |
| 代码库上下文 | 文本 | 相关模块、依赖、现有代码说明 | 了解现有实现和集成点 |
| 测试要求 | 对象 | 覆盖率目标、测试类型 | 指导测试编写 |

## Instructions

### 步骤 1：任务理解与需求分析

**目标**：深入理解任务需求和验收标准，确认无歧义

**操作方法**:
1. **需求阅读**: 仔细阅读任务规格，理解业务背景和核心目标
2. **验收标准检查**: 逐条检查验收标准，确认符合SMART原则（具体、可衡量、可达成、相关、有时限）
3. **疑问识别**: 标记模糊或有歧义的验收标准，列出所有可能的理解方式
4. **依赖分析**: 识别任务的外部依赖（第三方库、API接口、数据库表、其他模块）
5. **风险评估**: 识别潜在的技术风险和难点，评估影响程度
6. **澄清确认**: 如有疑问，主动与产品经理或Tech Lead沟通澄清

**检查点**:
- [ ] 所有验收标准清晰明确，无模糊表述
- [ ] 外部依赖已识别并确认可用
- [ ] 技术风险已评估并有应对方案
- [ ] 任务范围和边界已明确

**示例**:
```
模糊AC: "系统应该快速响应用户请求"
澄清后: "API接口在正常负载（100并发用户）下，响应时间应<500ms；在峰值负载（500并发用户）下，响应时间应<1秒"
```

---

### 步骤 2：技术方案设计与依赖分析

**目标**：制定具体的技术实现方案，分析依赖和风险

**操作方法**:
1. **架构对齐**: 参考系统设计文档，确认实现方案符合整体架构
2. **技术选型**: 选择合适的技术栈、框架、库，考虑团队熟悉度和社区支持
3. **类/接口设计**: 设计类结构、接口契约、数据模型，绘制类图
4. **流程设计**: 设计关键业务流程和算法，绘制时序图或流程图
5. **依赖管理**: 列出所有外部依赖，确认版本兼容性和许可证
6. **风险评估**: 评估技术风险（性能、安全、兼容性），制定缓解措施
7. **方案评审**: 复杂任务进行方案评审，获得Tech Lead批准

**检查点**:
- [ ] 实现方案符合架构设计，无偏差
- [ ] 技术选型合理，有明确的理由
- [ ] 类图和接口设计清晰，符合SOLID原则
- [ ] 所有依赖已识别，版本冲突已解决
- [ ] 技术风险已评估并有缓解措施

**工具**: 
- 类图工具：PlantUML、Mermaid
- 时序图工具：PlantUML、Mermaid
- 依赖检查：npm audit、mvn dependency:tree

---

### 步骤 3：代码结构设计与接口定义

**目标**：设计清晰的代码结构和接口，确保可维护性

**操作方法**:
1. **目录结构设计**: 按照项目约定组织代码目录（src/main/java/com/example/{module}/）
2. **类职责划分**: 每个类只负责一个职责，避免God Class
3. **接口定义**: 定义清晰的接口契约，包括方法签名、参数、返回值、异常
4. **数据模型设计**: 设计DTO、Entity、VO等数据对象，明确字段类型和约束
5. **异常处理策略**: 定义统一的异常类型和错误码，设计异常处理流程
6. **日志策略**: 确定日志级别（DEBUG/INFO/WARN/ERROR）和日志格式
7. **配置管理**: 外部化配置，避免硬编码，支持不同环境

**检查点**:
- [ ] 目录结构清晰，符合项目约定
- [ ] 每个类职责单一，无God Class
- [ ] 接口定义清晰，参数和返回值明确
- [ ] 数据模型完整，字段类型和约束正确
- [ ] 异常处理策略统一，错误码规范
- [ ] 日志策略合理，便于问题排查
- [ ] 配置外部化，无硬编码值

**SOLID原则应用**:
- **Single Responsibility**: 每个类只有一个改变的理由
- **Open/Closed**: 对扩展开放，对修改关闭
- **Liskov Substitution**: 子类可以替换父类而不影响程序正确性
- **Interface Segregation**: 接口应该小而专一，避免Fat Interface
- **Dependency Inversion**: 依赖抽象而非具体实现

---

### 步骤 4：编码实现与单元测试编写

**目标**：按照规范编写高质量的代码和充分的单元测试

**操作方法**:
1. **编码规范遵循**: 严格遵循团队编码规范（命名、缩进、注释、导入顺序等）
2. **命名规范**: 使用有意义的变量名、函数名、类名，避免缩写和单字母变量
3. **函数设计**: 函数长度<50行，参数≤5个，只做一件事
4. **注释添加**: 为复杂逻辑添加注释，说明"为什么"而不是"做什么"
5. **DRY原则**: 避免重复代码，提取公共逻辑为独立函数或类
6. **异常处理**: 捕获具体异常，提供有意义的错误信息，记录日志
7. **单元测试编写**（TDD推荐）:
   - 先写测试用例，再写实现代码
   - 覆盖正常路径、异常路径、边界条件
   - 使用Given-When-Then格式组织测试
   - Mock外部依赖，隔离测试单元
   - 测试用例命名清晰，描述测试场景

**检查点**:
- [ ] 代码遵循编码规范，lint检查通过
- [ ] 命名清晰有意义，无缩写和单字母变量
- [ ] 函数长度适中，职责单一
- [ ] 注释完整，关键逻辑有详细说明
- [ ] 无重复代码，DRY原则已应用
- [ ] 异常处理完整，错误信息清晰
- [ ] 单元测试覆盖核心逻辑和边界条件
- [ ] 测试覆盖率≥80%，核心逻辑100%覆盖
- [ ] 所有测试用例通过，无失败用例

**测试覆盖策略**:
- **正常路径**: 主要业务流程，预期输入和输出
- **异常路径**: 错误输入、异常情况、失败场景
- **边界条件**: 空值、null、空集合、最大值、最小值
- **特殊场景**: 并发、超时、网络故障、数据库连接失败

**示例**: Given-When-Then测试
```java
@Test
void shouldReturnTokenWhenLoginSuccess() {
    // Given
    String email = "user@example.com";
    String password = "correctPassword";
    when(userRepository.findByEmail(email)).thenReturn(Optional.of(user));
    when(passwordEncoder.matches(password, user.getPassword())).thenReturn(true);
    
    // When
    LoginResponse response = authService.login(email, password);
    
    // Then
    assertThat(response.getToken()).isNotNull();
    assertThat(response.getExpiresIn()).isEqualTo(86400);
    verify(loginLogger).logSuccess(email);
}
```

---

### 步骤 5：代码质量自检与优化

**目标**：执行全面的质量检查，确保代码符合标准

**操作方法**:
1. **代码规范检查**: 运行lint工具（ESLint、Checkstyle、Pylint等），修复所有错误
2. **静态代码分析**: 运行SonarQube或类似工具，修复critical和major issues
3. **圈复杂度检查**: 确保单个函数圈复杂度≤15，超过则重构或拆分
4. **重复代码检测**: 使用工具检测重复代码，提取公共逻辑
5. **安全扫描**: 运行安全扫描工具（Snyk、OWASP Dependency-Check），修复高危漏洞
6. **性能检查**: 识别性能瓶颈（N+1查询、 inefficient algorithms、内存泄漏）
7. **代码审查准备**: 自查代码，准备PR描述和审查要点

**检查点**:
- [ ] Lint检查通过，无errors，warnings < 10
- [ ] Sonar issues = 0（critical/major），或仅有info级别
- [ ] 圈复杂度≤15（单个函数），平均值≤10
- [ ] 无重复代码，或重复率 < 3%
- [ ] 安全扫描无高危漏洞
- [ ] 无明显性能瓶颈
- [ ] PR描述清晰，包含变更说明、测试说明、审查要点

**质量指标**:
- **CODE-COVERAGE**: ≥80%（整体），100%（核心逻辑）
- **BUG-DENSITY**: ≤0.5 defects/KLOC
- **CYCLOMATIC**: ≤15（单个函数），≤10（平均）
- **REVIEW-PASS**: 100%（一次通过率）

---

### 步骤 6：文档更新与交接准备

**目标**：同步更新相关文档，准备完整的交接材料

**操作方法**:
1. **API文档更新**: 如API有变更，更新OpenAPI/Swagger文档，包含请求/响应示例
2. **代码注释完善**: 确保关键逻辑有详细注释，public API有Javadoc/docstring
3. **README更新**: 如新增模块或功能，更新README说明使用方法和注意事项
4. **CHANGELOG编写**: 添加本次变更记录，包括新功能、bug修复、breaking changes
5. **技术决策记录**: 记录关键技术决策和权衡考虑，便于后续追溯
6. **Handover Context生成**: 填写交接模板，包含代码统计、质量指标、开放问题、风险
7. **Pull Request创建**: 创建PR，填写描述，指定reviewers，标注重点关注区域

**检查点**:
- [ ] API文档已更新（如API有变更）
- [ ] 代码注释完整，关键逻辑有详细说明
- [ ] README已更新（如需要）
- [ ] CHANGELOG已添加本次变更记录
- [ ] 技术决策已记录
- [ ] Handover Context字段完整，质量评分≥70分
- [ ] Pull Request已创建，描述清晰

**Handover Context必需字段**:
- summary（状态、完成度、质量评分、代码统计）
- artifacts（交付物清单，含checksum）
- decisions（关键决策和理由）
- open_issues（开放问题和风险）
- recommendations（测试建议）
- quality_metrics（KPI结果）

## Expected Output

### 产出列表

1. **源代码**：符合规范的实现代码，位于src/{feature_path}/
2. **单元测试**：覆盖核心逻辑的测试代码，位于tests/{test_path}/
3. **测试报告**：测试执行结果和覆盖率报告，位于reports/
4. **API文档**：更新的API接口说明（如API有变更），位于docs/api-spec.md
5. **实现说明**：关键技术决策、难点和解决方案的记录
6. **Handover Context**：交接给测试验证阶段的完整上下文信息

### 输出格式

功能实现交付物应包含以下内容：

```markdown
# Feature Implementation Deliverables

## 1. Task Information
- Task ID, Task Name, Developer, Completion Date, Status

## 2. Implementation Summary
- Acceptance Criteria Status (table)
- Work Effort (planned vs actual)

## 3. Code Changes
- New Files, Modified Files, Deleted Files
- Code Statistics (lines added/modified/deleted, files changed, commits count)

## 4. Test Results
- Unit Test Summary (total, passed, failed, skipped)
- Coverage Report (overall, critical logic, line, branch, function)
- Uncovered Areas (if any)

## 5. Code Quality Metrics
- Static Analysis Results (lint errors, sonar issues, cyclomatic complexity)
- Security Scan (vulnerabilities by severity)

## 6. Design Decisions
- Key Decisions (table with rationale and alternatives)
- Deviations from Design (if any)

## 7. Documentation Updates
- Updated Documents checklist
- API Changes (if applicable)

## 8. Open Issues & Risks
- Open Issues (table with severity and resolution plan)
- Risks (table with probability, impact, mitigation)

## 9. Recommendations for Testing
- Focus Areas
- Test Scenarios
- Integration Points

## 10. Quality Score
- Overall Score and Grade
- KPI Breakdown
```

## Quality Criteria

### Quality Standards

| 维度 | 标准 | 检查方法 | 合格线 |
|------|------|----------|--------|
| 功能正确性 | 所有验收标准已实现并通过验证 | AC核对，手动测试 | 100% AC通过 |
| 代码质量 | 遵循编码规范，无严重issues | Lint检查，SonarQube | lint errors=0, sonar critical/major=0 |
| 测试覆盖 | 核心逻辑100%覆盖，整体≥80% | 覆盖率报告 | coverage ≥80%, critical=100% |
| 文档完整 | API文档、注释、CHANGELOG已更新 | 文档检查 | 所有必需文档已更新 |
| 安全合规 | 无高危漏洞，安全最佳实践已应用 | 安全扫描 | high vulnerabilities=0 |

### Quality Score Calculation

```
Quality Score = (CODE-COVERAGE × 0.30) + (BUG-DENSITY × 0.25) + (CYCLOMATIC × 0.20) + (REVIEW-PASS × 0.25)

其中:
- CODE-COVERAGE: 实际覆盖率/目标覆盖率 × 100（最高100分）
- BUG-DENSITY: (1 - 实际密度/目标密度) × 100（最高100分）
- CYCLOMATIC: (1 - max(0, 实际复杂度-目标复杂度)/目标复杂度) × 100（最高100分）
- REVIEW-PASS: 一次通过率 × 100

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Core Knowledge

### Domain Fundamentals

**编码最佳实践**:
- **SOLID原则**: 单一职责、开闭原则、里氏替换、接口隔离、依赖倒置
- **DRY原则**: Don't Repeat Yourself，避免重复代码
- **KISS原则**: Keep It Simple, Stupid，保持简单
- **YAGNI原则**: You Aren't Gonna Need It，不要过度设计
- **Clean Code**: 清晰命名、小函数、少参数、有意义注释

**测试方法论**:
- **TDD（Test-Driven Development）**: 红-绿-重构循环
- **AAA模式**: Arrange-Act-Assert，组织测试代码
- **测试金字塔**: 单元测试（多）→ 集成测试（中）→ E2E测试（少）
- **Mock vs Stub**: Mock验证行为，Stub提供数据

**设计模式**:
- **创建型**: Factory, Singleton, Builder, Prototype
- **结构型**: Adapter, Decorator, Facade, Proxy
- **行为型**: Strategy, Observer, Command, Template Method

**性能优化**:
- **数据库**: 索引优化、查询优化、避免N+1、连接池
- **缓存**: Redis、Memcached、CDN、浏览器缓存
- **异步**: 消息队列、线程池、非阻塞IO
- **算法**: 选择合适的数据结构和算法，降低时间/空间复杂度

**安全编码**:
- **输入验证**: 白名单验证、类型检查、长度限制
- **SQL注入防护**: 参数化查询、ORM、存储过程
- **XSS防护**: 输出编码、Content Security Policy
- **CSRF防护**: CSRF Token、SameSite Cookie
- **认证授权**: JWT、OAuth 2.0、RBAC、最小权限原则

### Key Principles

1. **质量优先**: 宁可慢一点也要写好代码，避免后期返工和技术债务累积
2. **测试驱动**: 先写测试再写实现，或至少保证测试与代码同步完成
3. **渐进式提交**: 小步提交，每个commit完成一个独立功能点，便于追溯和回滚
4. **文档同步**: 代码变更时立即更新相关文档，避免文档滞后成为技术债务
5. **透明沟通**: 遇到问题及时升级，不隐瞒技术难点和风险
6. **持续改进**: 每次实现后反思总结，积累经验和最佳实践

## Best Practices

### 1. 遵循TDD（测试驱动开发）

**实践描述**: 先写失败的测试用例，再写实现代码使测试通过，最后重构优化代码。

**理由**: TDD确保测试覆盖，促进更好的设计，减少debug时间，提高代码质量。研究表明，TDD可以减少15-20%的bug数量。

**操作方法**:
1. **Red**: 编写一个失败的测试用例（因为功能尚未实现）
2. **Green**: 编写最少的代码使测试通过（不必完美）
3. **Refactor**: 重构代码，提高质量，保持测试通过
4. 重复上述步骤，逐步完成功能

**示例**:
```
// Step 1: Red - 写测试
@Test
void shouldCalculateCorrectTotal() {
    ShoppingCart cart = new ShoppingCart();
    cart.addItem(new Item("Book", 10.0));
    cart.addItem(new Item("Pen", 2.0));
    assertEquals(12.0, cart.getTotal());  // Fails - method not implemented
}

// Step 2: Green - 写实现
class ShoppingCart {
    private List<Item> items = new ArrayList<>();
    
    public void addItem(Item item) {
        items.add(item);
    }
    
    public double getTotal() {
        return items.stream().mapToDouble(Item::getPrice).sum();  // Passes
    }
}

// Step 3: Refactor - 优化
// 添加折扣逻辑、税费计算等，保持测试通过
```

---

### 2. 编写有意义的测试用例

**实践描述**: 测试用例命名清晰，覆盖正常路径、异常路径和边界条件，使用Given-When-Then格式组织。

**理由**: 清晰的测试用例便于理解和维护，全面的覆盖确保代码质量，Given-When-Then格式提高可读性。

**操作方法**:
- **命名规范**: should{ExpectedBehavior}When{Condition} 或 test{Scenario}_{ExpectedResult}
- **覆盖策略**: 正常路径（80%）、异常路径（15%）、边界条件（5%）
- **Given-When-Then**: 清晰分隔准备、执行、验证三个阶段
- **单一断言**: 每个测试只验证一个行为，便于定位失败原因
- **独立性**: 测试之间互不影响，可并行执行

**示例**:
```java
@Test
void shouldLockAccountAfterFiveFailedAttempts() {
    // Given
    String email = "user@example.com";
    String wrongPassword = "wrongPassword";
    
    // When
    for (int i = 0; i < 5; i++) {
        try {
            authService.login(email, wrongPassword);
        } catch (AuthenticationException e) {
            // Expected
        }
    }
    
    // Then
    assertThrows(AccountLockedException.class, () -> {
        authService.login(email, "correctPassword");
    });
    verify(accountLocker).lock(email, Duration.ofMinutes(30));
}
```

---

### 3. 小步提交，清晰Commit Message

**实践描述**: 将大任务拆分为多个小commit，每个commit完成一个独立功能点，使用规范的commit message。

**理由**: 小步提交便于代码审查、问题定位和回滚，清晰的commit message提高代码历史的可读性。

**操作方法**:
- **提交粒度**: 每个commit完成一个独立功能点（如：添加实体类、实现Service方法、编写测试）
- **Commit Message格式**: Conventional Commits
  ```
  <type>(<scope>): <subject>
  
  <body>
  
  <footer>
  ```
- **Type**: feat（新功能）、fix（bug修复）、refactor（重构）、test（测试）、docs（文档）、chore（构建/工具）
- **Subject**: 简短描述（≤50字符），使用祈使句
- **Body**: 详细说明变更内容和原因（可选）
- **Footer**: 关联issue号、breaking changes（可选）

**示例**:
```
feat(auth): implement JWT token generation

- Add JwtTokenService class
- Implement token generation with expiration
- Add unit tests for token service

Closes #123
```

---

### 4. 代码审查前的自检

**实践描述**: 提交代码审查前，先进行全面的自检，确保代码质量和规范遵循。

**理由**: 自检减少审查轮次，提高审查效率，展现专业态度，避免低级错误浪费reviewer时间。

**自检清单**:
- [ ] 代码编译通过，无错误或警告
- [ ] Lint检查通过，无errors
- [ ] 所有单元测试通过，覆盖率达标
- [ ] 静态代码分析通过，无critical/major issues
- [ ] 安全扫描无高危漏洞
- [ ] 代码注释完整，关键逻辑有说明
- [ ] PR描述清晰，包含变更说明、测试说明、审查要点
- [ ] 相关文件已更新（API文档、README、CHANGELOG）

---

### 5. 合理使用设计模式

**实践描述**: 根据实际问题选择合适的设计模式，避免过度设计或模式滥用。

**理由**: 设计模式提供经过验证的解决方案，提高代码可维护性和可扩展性，但过度使用会增加复杂度。

**常用模式及适用场景**:
- **Strategy**: 多种算法可互换（如：多种支付方式、多种排序算法）
- **Factory**: 创建复杂对象或需要根据条件创建不同类型对象
- **Observer**: 一对多依赖关系，一个对象变化需要通知多个对象（如：事件系统）
- **Decorator**: 动态添加功能，避免子类爆炸（如：Java IO流）
- **Template Method**: 算法骨架固定，部分步骤由子类实现

**注意事项**:
- 不要为了使用模式而使用模式
- 优先考虑简单直接的解决方案
- 模式应该使代码更清晰，而不是更复杂
- 团队应该对常用模式有共识

---

### 6. 性能意识编程

**实践描述**: 在编码过程中始终关注性能影响，避免常见的性能陷阱。

**理由**: 性能问题后期优化成本高，预防胜于治疗。良好的性能意识可以避免大部分性能问题。

**常见性能陷阱及避免方法**:
- **N+1查询**: 使用JOIN或批量查询，避免循环中执行数据库查询
- **内存泄漏**: 及时释放资源（close streams, connections），避免持有不必要的大对象引用
- **字符串拼接**: 大量字符串拼接使用StringBuilder而非+运算符
- **集合操作**: 选择合适的数据结构（ArrayList vs LinkedList, HashMap vs TreeMap）
- **同步锁**: 减少锁粒度，使用并发容器（ConcurrentHashMap），避免死锁
- **懒加载**: 大数据集使用分页或懒加载，避免一次性加载全部数据

**性能检查工具**:
- Profiler: JProfiler, VisualVM, Py-Spy
- APM: New Relic, Datadog, SkyWalking
- Database: EXPLAIN ANALYZE, slow query log

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

### Pitfall 1: 忽视测试覆盖

**风险**: 测试覆盖率低导致bug难以发现，后期修复成本高，回归测试困难。

**预防方法**:
- 采用TDD方法，先写测试再写实现
- 设置覆盖率门槛（≥80%），CI/CD pipeline自动检查
- 核心业务逻辑必须100%覆盖
- 定期审查测试质量，避免"为了覆盖而覆盖"

**影响**: 可能导致生产环境bug频发、回归测试困难、重构风险高、团队信心不足

**案例**:
```
某电商系统在促销活动期间，由于订单计算逻辑缺乏边界条件测试，
导致满减优惠计算错误，造成公司损失超过50万元。事后发现，如果
有充分的测试覆盖（特别是边界条件），这个问题完全可以避免。
```

---

### Pitfall 2: 硬编码值和魔法数字

**风险**: 硬编码值难以维护，修改时需要搜索多处，容易遗漏，增加bug风险。

**预防方法**:
- 使用常量或枚举代替魔法数字和字符串
- 外部化配置（配置文件、环境变量），避免代码中硬编码
- 使用有意义的常量名，说明值的含义
- 集中管理配置，避免散落在多处

**影响**: 可能导致维护困难、配置错误、部署问题、多环境不一致

**示例**:
```java
// ❌ Bad: 硬编码
if (status == 1) { ... }
Thread.sleep(5000);
String url = "https://api.example.com/v1/users";

// ✅ Good: 常量
if (status == OrderStatus.PAID.getCode()) { ... }
Thread.sleep(REQUEST_TIMEOUT_MS);
String url = config.getApiBaseUrl() + "/users";
```

---

### Pitfall 3: 过大的函数和类

**风险**: 过大的函数和类难以理解和维护，违反单一职责原则，测试困难。

**预防方法**:
- 函数长度控制在50行以内，最多不超过100行
- 类的方法数控制在10个以内
- 参数数量≤5个，超过则使用对象封装
- 定期重构，提取公共逻辑为独立函数或类
- 使用静态分析工具检测God Class和Long Method

**影响**: 可能导致理解困难、修改风险高、测试困难、代码复用率低

**指标**:
- 函数圈复杂度 ≤15
- 函数行数 ≤50（推荐），≤100（最大）
- 类方法数 ≤10
- 类字段数 ≤10

---

### Pitfall 4: 忽略异常处理和日志记录

**风险**: 异常处理不当导致程序崩溃或静默失败，日志缺失使问题难以排查。

**预防方法**:
- 捕获具体异常，避免catch (Exception e)
- 提供有意义的错误信息，包含上下文
- 记录日志时使用合适的级别（DEBUG/INFO/WARN/ERROR）
- 不要在catch块中吞掉异常（empty catch block）
- 使用统一的异常处理机制（全局异常处理器）
- 记录关键业务流程的日志，便于审计和问题追踪

**影响**: 可能导致程序崩溃、静默失败、问题难以排查、用户体验差

**示例**:
```java
// ❌ Bad: 吞掉异常
try {
    processOrder(order);
} catch (Exception e) {
    // Do nothing
}

// ✅ Good: 正确处理
try {
    processOrder(order);
} catch (OrderProcessingException e) {
    log.error("Failed to process order {}: {}", order.getId(), e.getMessage(), e);
    throw new ServiceException("Order processing failed", e);
}
```

## Related Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../../scenarios/implement-feature/SCENARIO.md` | 功能实现场景定义 |
| Agent | `../../agents/implement-feature.agent.md` | 功能实现Agent角色 |
| Prompt | `../../prompts/implement-feature.prompt.md` | 功能实现提示词模板 |
| Instruction | `../../instructions/implement-feature.instructions.md` | 功能实现技术指令 |

## Related Resources

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
