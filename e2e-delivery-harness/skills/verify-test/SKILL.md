---
name: verify-test
description: "设计和执行测试用例，验证功能正确性，发现并跟踪缺陷"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Testing Skill

## Use When

使用此技能的场景：

- 开发任务完成后，需要进行功能测试
- 需要设计测试用例和测试方案
- 需要执行回归测试验证修改
- 需要进行性能和安全测试

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 开发产出 | 文件 | 待测试的代码和功能说明 |
| 需求规格 | 文件 | 功能需求定义 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 接口文档 | 文件 | API 接口定义 |
| 测试规范 | 文件 | 测试标准和流程 |

## Instructions

### 步骤 1：测试计划制定

**目标**：制定测试策略和计划

**操作**：
1. 明确测试范围和重点
2. 确定测试类型（功能、性能、安全）
3. 选择测试方法
4. 规划测试资源
5. 制定测试时间表

**检查点**：
- [ ] 测试范围已明确
- [ ] 测试策略已确定
- [ ] 资源已规划

### 步骤 2：测试用例设计

**目标**：设计覆盖完整的测试用例

**操作**：
1. 设计正常路径用例
2. 设计异常路径用例
3. 设计边界条件用例
4. 设计性能测试用例（如需要）
5. 评审用例覆盖度

**检查点**：
- [ ] 用例覆盖核心功能
- [ ] 边界条件已覆盖
- [ ] 用例评审通过

### 步骤 3：测试环境准备

**目标**：搭建测试环境和准备测试数据

**操作**：
1. 搭建测试环境
2. 部署测试系统
3. 配置测试工具
4. 准备测试数据
5. 验证环境就绪

**检查点**：
- [ ] 环境可用
- [ ] 数据就绪
- [ ] 工具已配置

### 步骤 4：测试用例执行

**目标**：执行测试用例并记录结果

**操作**：
1. 按计划执行用例
2. 记录实际结果
3. 标注执行状态（通过/失败/阻塞）
4. 记录必要的截图和日志
5. 更新执行进度

**检查点**：
- [ ] 用例全部执行
- [ ] 结果记录准确
- [ ] 截图日志完整

### 步骤 5：缺陷管理

**目标**：提交、跟踪和管理缺陷

**操作**：
1. 识别和描述缺陷
2. 评估严重程度
3. 提交缺陷报告
4. 跟踪缺陷状态
5. 验证缺陷修复

**检查点**：
- [ ] 缺陷描述清晰
- [ ] 严重程度合理
- [ ] 跟踪状态准确

### 步骤 6：测试报告编写

**目标**：汇总测试结果，输出测试结论

**操作**：
1. 汇总测试执行数据
2. 统计测试覆盖率
3. 整理缺陷统计
4. 评估遗留风险
5. 给出测试结论

**检查点**：
- [ ] 数据统计准确
- [ ] 风险评估合理
- [ ] 结论明确

## Expected Output

### 产出列表

1. **测试计划**：测试策略和资源规划
2. **测试用例集**：完整的测试用例
3. **测试报告**：测试执行结果和分析
4. **缺陷报告**：发现的缺陷清单

### 输出格式

```markdown
## Test Report

### 测试概要
...

### 测试结果
...

### 缺陷统计
...

### 风险评估
...

### 测试结论
...
```

## Quality Criteria

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 测试覆盖 | 用例覆盖完整 | 覆盖率统计 |
| 执行准确 | 执行结果准确 | 结果核对 |
| 缺陷管理 | 缺陷跟踪规范 | 缺陷状态检查 |
| 报告质量 | 报告完整清晰 | 完整性检查 |




## Troubleshooting

### Issue 1: 常见问题
**Symptom**: 问题症状
**Cause**: 根本原因
**Resolution**: 解决步骤



## Related Assets

- **Agent**: [../../agents/verify-test.agent.md](../../agents/verify-test.agent.md)
- **Instruction**: [../../instructions/verify-test.instructions.md](../../instructions/verify-test.instructions.md)
- **Prompt**: [../../prompts/verify-test.prompt.md](../../prompts/verify-test.prompt.md)


## Core Knowledge

> Essential knowledge domain for verify-test execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for verify-test excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during verify-test execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
