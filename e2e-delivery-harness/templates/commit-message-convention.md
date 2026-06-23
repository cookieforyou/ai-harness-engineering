---
name: commit-message-convention
type: deliverable-template
version: "1.0.0"
status: active
---

# Commit 消息规范 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 概述

本项目遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范,通过结构化的提交信息实现自动版本管理和变更日志生成。

## 提交信息格式

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### 格式说明

| 组成部分 | 必填 | 说明 |
|----------|------|------|
| type | 是 | 提交类型,参见下方类型说明 |
| scope | 否 | 影响范围,如模块名称 |
| description | 是 | 变更的简要描述,使用祈使句,首字母小写 |
| body | 否 | 详细描述,解释变更的动机和背景 |
| footer | 否 | 附加信息,如 Breaking Changes、关联 Issue |

## 类型说明

| 类型 | 含义 | 发布类型 | 示例 |
|------|------|----------|------|
| feat | 新功能 | MINOR | feat: 添加用户注册功能 |
| fix | 缺陷修复 | PATCH | fix: 修复登录页面崩溃问题 |
| docs | 文档变更 | - | docs: 更新 API 使用说明 |
| style | 代码格式调整 | - | style: 格式化代码缩进 |
| refactor | 代码重构 | - | refactor: 重构用户服务 |
| perf | 性能优化 | PATCH | perf: 优化查询性能 |
| test | 测试相关 | - | test: 添加单元测试 |
| build | 构建系统变更 | - | build: 升级 Maven 版本 |
| ci | CI 配置变更 | - | ci: 更新 GitHub Actions |
| chore | 杂项 | - | chore: 更新依赖版本 |
| revert | 回退提交 | - | revert: 回退用户模块变更 |

## 规范示例

### 功能提交

```
feat(auth): 添加 OAuth2 登录支持

实现基于 OAuth2 协议的第三方登录功能,支持 Google 和 GitHub 登录。
重构原有登录流程以支持多种认证方式。

Closes #123
```

### 缺陷修复

```
fix(api): 修复用户查询接口空指针异常

当用户名为空时,UserService.findById 返回 null,
导致后续调用链出现 NullPointerException。

Fixes #456
```

### 破坏性变更

```
feat(core): 重构消息队列接口

BREAKING CHANGE: 消息处理接口签名变更,
handle 方法新增 MessageContext 参数。

需同步更新所有 MessageHandler 实现类。

Closes #789
```

### 文档更新

```
docs(readme): 更新快速开始指南

补充环境配置步骤和常见问题说明
```

## 分支命名规范

| 分支类型 | 格式 | 示例 |
|----------|------|------|
| 功能分支 | feat/description | feat/user-login |
| 修复分支 | fix/issue-description | fix/null-pointer-login |
| 发布分支 | release/version | release/v1.2.0 |
| 热修复分支 | hotfix/issue-description | hotfix/security-patch |

## 变更日志生成

提交信息将自动生成 CHANGELOG.md:

- **feat**: 新增功能 (Added)
- **fix**: 缺陷修复 (Fixed)
- **BREAKING CHANGE**: 重大变更 (Changed)
- **deprecated**: 废弃功能 (Deprecated)

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
