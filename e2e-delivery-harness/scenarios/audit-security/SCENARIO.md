---
name: security-audit
type: scenario
stage: testing
version: "1.1.0"
difficulty: high
prerequisites: 
---

# Security Audit Scenario

## Purpose

执行安全审计，发现安全漏洞和风险，验证安全控制的有效性，确保系统符合安全要求。

## Chain of Thought (思维链)

```
THINK: 确定审计范围
   ↓
THINK: 识别攻击面
   ↓
THINK: 执行安全测试
   ↓
THINK: 分析安全漏洞
   ↓
THINK: 评估风险等级
   ↓
THINK: 制定修复计划
```

### Step-by-Step Reasoning

**Step 1: 范围确定**
- 问：哪些部分需要审计？
- 验证：识别资产清单
- 检查：是否有遗漏

**Step 2: 攻击面识别**
- 问：有哪些可能的攻击向量？
- 验证：检查接口、入口
- 检查：信任边界

**Step 3: 测试执行**
- 问：需要执行哪些测试？
- 验证：OWASP Top 10
- 检查：业务逻辑漏洞

**Step 4: 漏洞分析**
- 问：漏洞的严重程度？
- 验证：CVSS 评分
- 检查：利用难度

**Step 5: 风险评估**
- 问：漏洞的实际风险？
- 验证：结合业务场景
- 检查：数据敏感性

## Error Handling

### EH-1: 发现高危漏洞

- **识别信号**：发现高危或严重漏洞
- **处理方式**：
  1. 立即停止测试
  2. 通知安全团队
  3. 制定紧急修复计划
- **升级条件**：必须立即处理

### EH-2: 测试环境异常

- **识别信号**：测试环境无法正常使用
- **处理方式**：
  1. 确认环境状态
  2. 准备测试数据
  3. 调整测试策略
- **升级条件**：影响审计进度

### EH-3: 误报处理

- **识别信号**：测试结果可能为误报
- **处理方式**：
  1. 人工验证结果
  2. 复现漏洞场景
  3. 确认漏洞真实性
- **升级条件**：确认误报

## Primary Assets

- **Agent**: [../../agents/verify-test.agent.md](../../agents/verify-test.agent.md)
- **Instruction**: [../../instructions/audit-security.instructions.md](../../instructions/audit-security.instructions.md)
- **Prompt**: [../../prompts/audit-security.prompt.md](../../prompts/audit-security.prompt.md)

## Expected Output

### 产出清单

1. **安全审计报告**：完整的审计结果
2. **漏洞列表**：发现的安全漏洞
3. **风险评估**：漏洞风险等级
4. **修复建议**：漏洞修复方案

### 输出格式

```markdown
## Security Audit Report

### 1. 审计概述
- 审计范围：
- 审计时间：
- 审计方法：

### 2. 发现的漏洞

| 漏洞ID | 漏洞名称 | 严重程度 | 漏洞类型 | 状态 |
|--------|----------|----------|----------|------|
| | | | | |

### 3. 风险评估
...

### 4. 修复建议
...

### 5. 安全建议
...
```

## Prerequisites

### 必需前置条件

1. 测试环境可用
2. 系统文档可用
3. 安全基线已定义

### 可选前置条件

1. 渗透测试授权
2. 安全测试工具
3. 历史漏洞数据

## Quality Gates

### 阶段准入

- [ ] 审计范围已确定
- [ ] 测试环境可用
- [ ] 测试工具就绪

### 阶段准出

- [ ] 审计覆盖所有范围
- [ ] 漏洞列表完整
- [ ] 修复建议可行

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 审计策略确认** | 完成范围定义后 | 审计重点？工具选择？ | 继续信息收集 |
| **DC-2: 严重漏洞确认** | 发现严重漏洞时 | 是否停止审计先修复？ | 继续或暂停 |
| **DC-3: 审计结论确认** | 完成漏洞评估后 | 审计结论？上线条件？ | 决定下一步 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `FINDING-COVERAGE` | ≥95% | 发现覆盖率：检查项全部执行 |
| `REMEDIATION-SLA` | ≤30d | 整改SLA：高危问题修复时间 |
| `COMPLIANCE-SCORE` | ≥95% | 合规得分：框架要求达标比例 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 审计报告 | ☐ | 完整可追溯 |
| 漏洞清单 | ☐ | 含严重等级 |
| CVSS 评分 | ☐ | 每项有评分 |
| 修复计划 | ☐ | 含优先级 |

## Workflow

```
1. 确定审计范围
2. 收集系统信息
3. 识别攻击面
4. 执行安全测试
5. 分析漏洞
6. 评估风险
7. 编写报告
```

## Related Scenarios

- **Related**: [../verify-test/](../verify-test/) - 测试验证
- **Related**: [../deploy-release/](../deploy-release/) - 部署发布

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 覆盖率 | > 90% | OWASP 检查项 |
| 高危漏洞 | 0 | 漏洞统计 |
| 中危漏洞 | < 3 | 漏洞统计 |
| 修复率 | > 95% | 漏洞修复率 |
