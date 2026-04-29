# Scenario: 自动化测试 (Automate Test)

## 概述

本场景用于搭建自动化测试框架、编写自动化测试用例、集成 CI/CD 流水线。

## Chain of Thought

```
[THINK] 理解测试需求
├─ 确定测试范围和目标
├─ 分析被测系统架构
└─ 评估测试工具选型

[ANALYZE] 设计测试框架
├─ 选择测试框架（pytest/jest/JUnit）
├─ 设计测试分层结构
└─ 制定测试数据策略

[DESIGN] 编写测试用例
├─ 设计测试用例结构
├─ 编写测试数据构造器
└─ 实现测试断言库

[IMPLEMENT] 实现测试脚本
├─ 编写 Page Object 模型
├─ 实现测试用例脚本
└─ 添加测试报告生成

[INTEGRATE] 集成 CI/CD
├─ 配置测试执行流水线
├─ 设置测试报告收集
└─ 配置失败自动通知
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 测试框架选型确认 | 是否选择当前框架？ |
| DC-002 | 测试用例评审 | 用例是否覆盖核心路径？ |
| DC-003 | CI 集成方案 | 测试触发时机？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 测试环境不可用 | 等待环境就绪或通知 DevOps |
| 依赖安装失败 | 检查 pip/npm 配置 |
| 测试数据缺失 | 构造测试数据或联系数据团队 |

## Handover Criteria

- [x] 测试框架搭建完成
- [x] 核心用例覆盖率 ≥ 80%
- [x] CI 流水线集成成功
- [x] 测试报告可正常生成
- [x] 维护文档已编写

## 关联资产

- **Prompt**: `prompts/automate-test.prompt.md`
- **Instruction**: `instructions/automate-test.instructions.md`
- **Agent**: `agents/test-automation-engineer.agent.md`
- **Skill**: `skills/automate-test/SKILL.md`
