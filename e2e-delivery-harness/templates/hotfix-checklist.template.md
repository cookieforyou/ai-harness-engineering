---
name: hotfix-checklist
type: deliverable-template
version: "1.0.0"
status: active
---

# 热修复检查清单 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 热修复基本信息

- **Hotfix ID**: HF-{number}
- **修复版本**: {version}
- **基于版本**: {base_version}
- **关联故障**: INC-{number}
- **负责人**: {owner}
- **创建日期**: {ISO8601}
- **紧急程度**: {紧急 / 高 / 中}

## 问题评估

### 问题描述

{清晰描述需要热修复的问题}

### 影响范围

- **影响用户**: {affected_users}
- **影响功能**: {affected_functions}
- **严重程度**: P0 - Critical / P1 - Major

### 修复必要性

- [ ] 影响核心业务流程
- [ ] 影响数据完整性
- [ ] 影响用户安全
- [ ] 影响 SLA 达成
- [ ] 重大用户体验问题

## 修复方案

### 修复隔离

- [ ] 仅修复目标问题,不引入额外变更
- [ ] 确认修复不依赖未发布的其它变更
- [ ] 确认修复范围最小化

### 代码变更

| 文件 | 变更描述 | 影响模块 |
|------|----------|----------|
| {file_path} | {change_description} | {module} |
| {file_path} | {change_description} | {module} |

## 测试验证

### 单元测试

- [ ] 新增测试覆盖修复场景
- [ ] 现有测试未受影响
- [ ] 测试全部通过

### 集成测试

- [ ] 核心业务流程测试通过
- [ ] 边界条件测试通过

### 回归测试

- [ ] 关键功能回归测试通过
- [ ] 相关模块回归测试通过

## 部署验证

| 检查项 | 验收标准 | 结果 |
|--------|----------|------|
| 部署成功 | 服务正常启动 | PASS/FAIL |
| 功能验证 | 修复功能正常 | PASS/FAIL |
| 健康检查 | 所有健康检查通过 | PASS/FAIL |

## 监控确认

| 监控项 | 观察周期 | 预期 | 实际 |
|--------|----------|------|------|
| 错误率 | {time_window} | {threshold} | {actual} |
| 响应时间 | {time_window} | {threshold} | {actual} |
| 业务指标 | {time_window} | {threshold} | {actual} |

## 后续安排

- [ ] 安排正式版本包含此修复
- [ ] 补充缺失的自动化测试
- [ ] 更新相关文档
- [ ] 安排 Post-mortem 复盘

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
