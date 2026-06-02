---
name: manage-dependencies
description: "依赖管理场景的技术指令，详细说明依赖管理的工具和方法"
applyTo: "scenarios/manage-dependencies/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Dependency Management Instructions

## Overview

本指令提供依赖管理的详细技术规范，包括工具选择、命令示例和最佳实践。

## Supported Package Managers

### Node.js / npm

```bash
# 查看依赖树
npm ls --depth=0        # 直接依赖
npm ls --all           # 完整依赖树
npm ls <package>       # 特定依赖

# 查看过时依赖
npm outdated

# 更新依赖
npm update             # 更新到 semver 允许范围
npm update <package>   # 更新特定依赖
npx npm-check-updates -u  # 交互式更新

# 安全审计
npm audit             # 漏洞扫描
npm audit fix         # 自动修复
npm audit --audit-level=high  # 仅显示高级别

# 许可证检查
npx license-checker --csv --out dependencies.csv
```

### Python / pip

```bash
# 导出依赖
pip freeze > requirements.txt
pipreqs . --force       # 基于代码分析

# 检查过时
pip list --outdated

# 安全检查
pip-audit
safety check

# 版本约束
pip install "requests>=2.28.0,<3.0.0"
```

### Go / go.mod

```bash
# 查看依赖
go list -m all          # 所有依赖
go list -m tree         # 依赖树

# 更新依赖
go get -u              # 更新所有
go get <package>@latest # 更新特定

# 清理依赖
go mod tidy
go mod verify

# 安全检查
gosec ./...
```

## Dependency Analysis

### 依赖健康度指标

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| 依赖年龄 | < 6 months | 6-12 months | > 12 months |
| 更新频率 | Weekly/Monthly | Quarterly | Yearly+ |
| 社区规模 | > 1000 stars | 100-1000 | < 100 |
| 维护状态 | Active | Limited | Abandoned |

### 漏洞评估标准

- **Critical (9-10)**: 立即修复，RCE 或数据泄露风险
- **High (7-8.9)**: 1周内修复，权限提升或注入风险
- **Medium (4-6.9)**: 1月内修复，信息泄露风险
- **Low (0-3.9)**: 计划修复，较低风险

### 许可证兼容性矩阵

| License Type | Commercial Use | Modification | Distribution |
|--------------|---------------|-------------|--------------|
| MIT | Yes | Yes | Yes |
| Apache 2.0 | Yes | Yes | Yes |
| BSD 3-Clause | Yes | Yes | Yes |
| GPL 3.0 | Yes | Yes | Yes (copyleft) |
| AGPL 3.0 | Yes | Yes | Yes (strong copyleft) |
| Proprietary | Varies | No | No |

## Update Strategy

### 渐进式更新流程

```
1. 隔离环境测试
   └── 在 CI 隔离环境测试

2. 小批次更新
   └── 每次最多 5 个依赖

3. 回归测试
   └── 运行完整测试套件

4. 代码审查
   └── Review 变更内容

5. 合并部署
   └── 合并到主分支
```

### 批量更新策略

```yaml
# update-config.yaml
update_strategy:
  batch_size: 5
  interval_days: 7
  max_version_jump:
    major: 0  # 不允许主版本跳跃
    minor: 2  # 最多跳跃2个小版本
    patch: 5   # 最多跳跃5个补丁版本
  require_approval: true
  auto_rollback: true
```

## Lock File Management

### package-lock.json

```json
{
  "dependencies": {
    "lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "integrity": "sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZ3eBuzfnkkMOs1+pCjfyw==",
      "dev": false
    }
  }
}
```

### requirements.txt

```
# 固定版本
requests==2.28.0

# 范围版本（谨慎使用）
django>=3.2,<4.0

# 特定来源
git+https://github.com/user/repo.git@v1.2.3
-e git+https://github.com/user/repo.git#egg=mypackage
```

## Vulnerability Remediation

### 修复优先级

1. **立即处理**：Critical/High 漏洞且有可用修复
2. **计划处理**：High/Medium 漏洞需要代码修改
3. **监控观察**：无直接风险的漏洞
4. **接受风险**：无法修复且可接受的漏洞

### 缓解措施

```yaml
# security-config.yaml
mitigations:
  - type: WAF_RULE
    description: 阻止特定攻击向量
    expires: "2024-06-01"

  - type: NETWORK_ISOLATION
    description: 隔离受影响组件
    scope: internal_only

  - type: ADDITIONAL_MONITORING
    description: 加强日志和告警
    alert_threshold: 1/hour
```

## Rollback Procedures

### 自动回滚触发条件

- 构建失败
- 测试失败率 > 5%
- 安全扫描发现新漏洞
- 性能回归 > 20%

### 回滚命令

```bash
# npm
git checkout package-lock.json
npm ci

# pip
pip install -r requirements.lock

# go
git checkout go.sum
go mod download
```

## Best Practices

### Do's

1. 使用锁文件确保一致性
2. 定期更新依赖（至少每季度）
3. 关注安全通报
4. 最小化依赖数量
5. 优先选择活跃维护的库
6. 审核新增依赖
7. 记录重大依赖变更

### Don'ts

1. 不要忽略安全警告
2. 不要直接修改锁文件
3. 不要使用未知来源的包
4. 不要跳过测试直接部署
5. 不要忽略许可证要求
6. 不要使用已弃用的包
7. 不要忽略版本不兼容警告


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-dependencies.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Error Handling

> Common error scenarios and resolution strategies for manage-dependencies.

### Error Category 1
**Symptom**: Vulnerable dependencies are not identified promptly
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: License violations are discovered late in cycle
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for manage-dependencies deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All known CVEs are identified and tracked | Automated check |
| Standard 2 | License compliance is 100% with no prohibited licenses | Automated check |
| Standard 3 | Critical patches are applied within 30 days | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
