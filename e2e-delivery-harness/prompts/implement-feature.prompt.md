---
name: implement-feature
description: 功能实现提示词，用于完成具体的代码开发任务
type: development
version: "1.1.0"
stage: development
---

# Implement Feature

> **版本**: 1.1.0 | **适用阶段**: 开发实现 | **预计工时**: 1-3天/任务

## Input Variables

| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `task_id` | string | 是 | 任务ID | "T001" |
| `task_name` | string | 是 | 任务名称 | "用户登录功能" |
| `module` | string | 是 | 所属模块 | "user-service" |
| `priority` | string | 是 | 优先级 | "P0" |
| `acceptance_criteria` | string[] | 是 | 验收标准 | ["支持JWT认证"] |
| `tech_stack` | string[] | 是 | 技术栈 | ["Java", "Spring Boot"] |
| `existing_code` | string | 否 | 现有代码 | (代码路径) |

## Chain of Thought

```
1. [THINK] 理解任务 → 验收标准是否清晰？
2. [THINK] 分析实现方案 → 技术选型是否合理？
3. [THINK] 编写代码 → 是否遵循编码规范？
4. [THINK] 编写测试 → 边界条件是否覆盖？
5. [THINK] 自检代码 → 是否有安全漏洞？
6. [VALIDATE] 验证实现 → 是否满足所有验收标准？
7. [OUTPUT] 生成交付物
```

## Error Handling

### 情况 1：验收标准不清晰

```
IF 验收标准模糊或有歧义
THEN
  1. 列出所有可能的理解
  2. 选择最合理的理解
  3. 在代码注释中说明假设
  4. 标记为 [需确认]
END
```

### 情况 2：实现遇到技术难点

```
IF 遇到无法解决的技术问题
THEN
  1. 分析问题的根本原因
  2. 尝试替代方案
  3. 如仍无法解决，向上升级（联系技术负责人）
  4. 记录问题和尝试的解决方案
END
```

### 情况 3：发现设计问题

```
IF 发现设计与实现不匹配
THEN
  1. 分析差异的影响
  2. 判断是设计问题还是实现问题
  3. 与设计文档对比
  4. 如需修改设计，联系系统设计师
END
```

```

## Task Steps

### 步骤 1：任务理解

**任务**：
- 理解业务需求
- 理解技术要求
- 确认验收标准
- 识别实现难点

**产出**：任务理解备忘录

### 步骤 2：技术方案

**任务**：
- 设计代码结构
- 定义接口和类
- 考虑异常处理
- 编写伪代码（如需要）

**产出**：技术实现方案

### 步骤 3：编码实现

**任务**：
- 按照规范编写代码
- 添加必要的注释
- 确保代码规范
- 保持代码简洁

**产出**：源代码

### 步骤 4：单元测试

**任务**：
- 编写测试用例
- 覆盖正常路径
- 覆盖异常路径
- 执行测试验证

**产出**：测试代码和测试报告

### 步骤 5：代码审查

**任务**：
- 自检代码
- 准备审查材料
- 响应审查意见
- 获得审查通过

**产出**：审查通过的代码

### 步骤 6：文档更新

**任务**：
- 更新接口文档
- 更新代码注释
- 更新变更记录

**产出**：更新后的文档

## Output Format

```markdown
# 实现报告

## 1. 任务信息
- 任务ID：T001
- 任务名称：[名称]
- 执行人：[姓名]
- 完成时间：[日期]

## 2. 实现摘要

### 2.1 完成情况
| 验收标准 | 完成状态 | 说明 |
|----------|----------|------|
| 标准1 | ✅ 完成 | - |
| 标准2 | ✅ 完成 | - |
| 标准3 | ✅ 完成 | - |

### 2.2 工作量
- 计划工时：2 人天
- 实际工时：1.5 人天
- 偏差：-25%

## 3. 代码变更

### 3.1 新增文件
| 文件 | 说明 |
|------|------|
| src/xxx.ts | 新增功能实现 |

### 3.2 修改文件
| 文件 | 说明 |
|------|------|
| src/yyy.ts | 修改功能实现 |

### 3.3 删除文件
| 文件 | 说明 |
|------|------|
| - | - |

### 3.4 代码统计
- 新增代码：XXX 行
- 修改代码：XXX 行
- 删除代码：XXX 行

## 4. 测试结果

### 4.1 测试用例
| 用例ID | 描述 | 结果 |
|--------|------|------|
| TC001 | 测试描述 | 通过 |

### 4.2 测试覆盖
- 覆盖率：XX%
- 通过率：100%

## 5. 遗留问题

| 问题 | 影响 | 解决方案 | 状态 |
|------|------|----------|------|
| 问题1 | 低 | 后续优化 | 待处理 |

## 6. 后续建议

- [建议1]
- [建议2]
```

## 输出验证 (Output Validation)

> **重要**: 在提交代码前，必须完成以下验证步骤

### 验证清单

```markdown
## 自我验证报告

### V-001: 功能验证
- [ ] 所有验收标准都已实现
- [ ] 功能逻辑正确
- [ ] 异常情况已处理

### V-002: 代码质量验证
- [ ] 代码遵循编码规范
- [ ] 命名清晰有意义
- [ ] 函数长度适中
- [ ] 无硬编码值

### V-003: 安全验证
- [ ] 无 SQL 注入风险
- [ ] 无 XSS 风险
- [ ] 敏感数据已加密
- [ ] 权限控制正确

### V-004: 测试验证
- [ ] 单元测试通过
- [ ] 测试覆盖核心逻辑
- [ ] 边界条件已覆盖
- [ ] 测试可重复执行

### V-005: 文档验证
- [ ] 代码注释清晰
- [ ] API 文档已更新
- [ ] README 已更新（如需要）

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 修复问题
  2. 重新运行测试
  3. 再次验证
  4. 如无法解决，联系团队负责人
END
```

## Handover 准备

```yaml
handoff_to_testing:
  deliverable: "代码实现"
  task_id: "{{task_id}}"
  version: "1.0"

  summary:
    files_changed: N
    lines_added: N
    lines_deleted: N
    test_coverage: "XX%"

  test_results:
    unit_tests_passed: [是/否]
    coverage_meet_target: [是/否]

  open_issues:
    - issue: "问题描述"
      severity: "high/medium/low"
```

## Constraints

1. **语言**：输出使用中文
2. **规范**：遵循团队代码规范
3. **测试**：核心逻辑必须有测试覆盖
4. **文档**：代码变更必须更新相关文档
5. **可追溯**：变更必须可追溯

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 功能正确 | 实现符合需求 |
| 代码规范 | 遵循编码规范 |
| 测试通过 | 单元测试全部通过 |
| 文档同步 | 相关文档已更新 |

## Task Description

> Describe the specific task for the implement-feature scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for implement-feature

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core implement-feature activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
