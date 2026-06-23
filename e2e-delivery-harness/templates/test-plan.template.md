---
name: test-plan
type: deliverable-template
version: "1.0.0"
status: active
---

# 测试计划 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 测试范围

### 在测范围

- {功能模块1}: {测试范围描述}
- {功能模块2}: {测试范围描述}
- {功能模块3}: {测试范围描述}

### 非测范围

- {不在测试范围的内容}: {理由}

## 测试策略

### 测试层级

| 测试层级 | 测试类型 | 工具/框架 | 执行策略 | 责任人 |
|----------|----------|-----------|----------|--------|
| Level 0 - 单元测试 | 白盒测试 | {jest/JUnit/pytest} | 代码提交时触发 | {developer} |
| Level 1 - 集成测试 | 接口测试 | {Postman/TestNG} | 每日构建 | {developer} |
| Level 2 - 系统测试 | 功能测试 | {Selenium/Cypress} | 迭代完成时 | {tester} |
| Level 3 - 验收测试 | E2E 测试 | {Playwright/Cucumber} | 发布前 | {tester} |

### 测试数据管理

- **测试数据来源**: {生产脱敏/手工构造/自动生成}
- **数据准备方式**: {SQL脚本/API 生成/测试夹具}
- **数据清理策略**: {测试后的数据清理方案}

### 测试环境

| 环境名称 | 用途 | 配置 | 数据 | 访问方式 |
|----------|------|------|------|----------|
| DEV | 开发自测 | {config} | {data} | {access} |
| SIT | 系统集成测试 | {config} | {data} | {access} |
| UAT | 用户验收测试 | {config} | {data} | {access} |
| STAGING | 预发布验证 | {config} | {data} | {access} |

## 测试进度安排

| 阶段 | 开始日期 | 结束日期 | 交付物 | 里程碑 |
|------|----------|----------|--------|--------|
| 测试设计 | {date} | {date} | 测试用例 | {milestone} |
| 测试执行 | {date} | {date} | 测试报告 | {milestone} |
| 回归测试 | {date} | {date} | 回归报告 | {milestone} |

## 资源分配

| 角色 | 人员 | 职责 | 投入比例 |
|------|------|------|----------|
| 测试负责人 | {name} | 测试策略与管理 | 100% |
| 测试工程师 | {name} | 测试执行 | 100% |
| 开发工程师 | {name} | 缺陷修复支持 | 50% |

## 风险分析

| 风险ID | 风险描述 | 概率 | 影响 | 缓解措施 |
|--------|----------|------|------|----------|
| T-RSK-01 | {description} | H/M/L | H/M/L | {mitigation} |

## 准入/准出标准

### 准入标准 (Entry Criteria)

- [ ] 需求文档已评审确认
- [ ] 开发完成并提测
- [ ] 单元测试通过
- [ ] 测试环境就绪
- [ ] 测试数据准备完成

### 准出标准 (Exit Criteria)

- [ ] 所有测试用例执行完毕
- [ ] 无 P0/P1 级缺陷未修复
- [ ] 测试覆盖率达到 {coverage}%
- [ ] 性能指标满足要求
- [ ] 测试报告已评审

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
