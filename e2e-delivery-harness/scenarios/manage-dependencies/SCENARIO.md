---
name: manage-dependencies
type: scenario
version: 1.0.0
description: 依赖管理场景，管理系统和项目依赖，确保依赖的安全性、兼容性和可维护性
trigger: 当需要分析、更新或审计项目依赖时触发
agent: developer
phase: implement-feature
tags:
  - dependencies
  - security
  - package-management
  - vulnerability
input:
  - project_name
  - project_path
  - dependency_list
  - audit_scope
output:
  - dependency-report.md
  - update-plan.md
  - vulnerability-assessment.md
---

# Dependency Management Scenario

## Overview

依赖管理是软件开发中的关键环节，涉及识别、分析、更新和维护项目所依赖的外部库、框架和工具。本场景确保依赖的安全性、兼容性和可维护性。

## Trigger Conditions

- 新项目初始化时
- 定期依赖审计（每月/每季度）
- 安全漏洞披露时
- 版本升级前
- 代码审查中发现依赖问题时

## Chain of Thought

```
1. 分析依赖清单
   ↓
2. 识别直接依赖和传递依赖
   ↓
3. 检查安全漏洞和许可证合规
   ↓
4. 评估版本兼容性和更新风险
   ↓
5. 制定更新策略和回滚计划
   ↓
6. 执行更新并验证
   ↓
7. 更新依赖锁定文件
   ↓
8. 验证构建和测试通过
```

## Decision Checkpoints

### Checkpoint 1: 依赖分析
- 依赖清单是否完整？
- 是否有未声明的传递依赖？
- 是否存在循环依赖？

### Checkpoint 2: 安全评估
- 是否有已知 CVE 漏洞？
- 漏洞严重程度如何？
- 是否有修复版本可用？

### Checkpoint 3: 兼容性评估
- 主版本更新是否破坏兼容性？
- 是否需要代码修改？
- 更新窗口期多长？

### Checkpoint 4: 更新决策
- 是否需要立即更新（高危漏洞）？
- 是否可以批量更新？
- 是否需要分阶段更新？

## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 依赖冲突 | 绘制依赖图，识别冲突源，使用版本约束解决 |
| 脆弱依赖 | 评估替代方案，制定迁移计划 |
| 许可证冲突 | 咨询法务，评估替换或购买许可 |
| 更新后构建失败 | 自动回滚，分析兼容性变更 |

## Handover Criteria

- [ ] 依赖清单完整且准确
- [ ] 安全漏洞已评估和处理
- [ ] 更新计划已制定并评审
- [ ] 依赖锁定文件已更新
- [ ] 构建和测试通过
- [ ] 文档已更新

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| dependency-report.md | 完整依赖分析报告 |
| update-plan.md | 更新计划和风险评估 |
| vulnerability-assessment.md | 安全漏洞评估报告 |
| lockfile | 更新的依赖锁定文件 |

## Related Scenarios

- [implement-feature](./implement-feature/SCENARIO.md) - 功能实现
- [audit-security](./audit-security/SCENARIO.md) - 安全审计
- [verify-test](./verify-test/SCENARIO.md) - 测试验证
