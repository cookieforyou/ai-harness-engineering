---
name: defect-report
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 缺陷报告 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 缺陷基本信息

| 字段 | 值 |
|------|----|
| 缺陷ID | BUG-{number} |
| 标题 | {defect_title} |
| 严重级别 | P0 - Critical / P1 - Major / P2 - Minor / P3 - Trivial |
| 优先级 | 紧急 / 高 / 中 / 低 |
| 状态 | 新建 / 已确认 / 修复中 / 已修复 / 验证中 / 已关闭 / 重新打开 |
| 报告人 | {reporter} |
| 指派给 | {assignee} |
| 发现版本 | {found_version} |
| 修复版本 | {fix_version} |
| 发现时间 | {ISO8601} |
| 所属模块 | {module_name} |
| 关联需求 | FR-{number} |
| 关联用例 | TC-{number} |

## 环境信息

- **操作系统**: {OS} {version}
- **浏览器**: {browser} {version}
- **应用版本**: {app_version}
- **数据库版本**: {db_version}
- **网络环境**: {network_environment}

## 缺陷描述

### 复现步骤

1. {step 1}
2. {step 2}
3. {step 3}
4. {step 4}

### 预期结果

{描述期望的正确行为}

### 实际结果

{描述实际出现的错误行为}

### 截图/日志

```
{关键日志信息或截图链接}
```

## 根因分析

- **根因类别**: {代码逻辑错误 / 配置错误 / 数据错误 / 环境问题 / 设计缺陷 / 第三方依赖}
- **根因描述**: {详细的根因分析}
- **引入阶段**: {需求分析 / 系统设计 / 编码实现 / 部署配置}

## 修复方案

### 修复措施

{描述具体的修复方案}

### 影响范围

{修复可能影响的其他功能或模块}

### 验证方法

{如何验证修复正确}

## 附件

- {log_file_path}
- {screenshot_url}
- {其他附件}

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 |
|------|------|------|----------|
| v1.0 | {ISO8601} | {author} | 创建缺陷报告 |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
