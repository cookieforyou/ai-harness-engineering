# 版本管理策略 / Versioning Strategy

> **效力等级**: P0（强制）  
> **适用范围**: 全部可复用资产（agents, skills, prompts, instructions, evaluations）

---

## 版本哲学

> **独立演进，兼容承诺**: 每个资产独立版本化，发布方对兼容性做出明确承诺，消费方通过 `assets.lock` 锁定依赖。

---

## SemVer 应用规则

| 版本变化 | 含义 | 消费方行动 |
| :--- | :--- | :--- |
| **MAJOR** ↑ | 破坏性变更（接口、Schema、行为改变） | 必须人工审核后升级 |
| **MINOR** ↑ | 功能新增，向后兼容 | 可自动升级，建议回归测试 |
| **PATCH** ↑ | Bug 修复、文档优化，无行为变更 | 可自动升级 |

---

## 资产版本生命周期

```
草稿 (Draft) → 候选 (RC) → 发布 (Release) → 维护 (Maintenance) → 废弃 (Deprecated) → 移除 (Removed)
```

- **Draft**: 开发中，不保证稳定，不纳入 `assets.lock`
- **RC (Release Candidate)**: 冻结特性，仅修 Bug，可纳入测试环境 lock
- **Release**: 正式可用，纳入生产环境 lock
- **Maintenance**: 仅接受 Patch 修复，不接受新特性
- **Deprecated**: 已标记废弃，消费方需计划迁移
- **Removed**: 从库中移除（需至少 Deprecated 90 天后）

---

## 版本锁定机制

场景通过 `assets.lock` 精确锁定依赖：

```yaml
dependencies:
  - asset: "skills/diff-parser.yaml"
    version: "1.0.0"          # 精确锁定
    checksum: "sha256:abc..."
  - asset: "prompts/code-review/v1.md"
    version: "^1.0.0"         # 允许 Patch 自动升级（需 CI 验证）
```

### 版本表达式

| 表达式 | 含义 |
| :--- | :--- |
| `1.0.0` | 精确版本 |
| `^1.0.0` | 兼容 1.x.x（允许 Minor/Patch） |
| `~1.0.0` | 兼容 1.0.x（仅允许 Patch） |
| `>=1.0.0 <2.0.0` | 范围表达式 |

---

## 变更日志规范

每个资产目录下维护 `CHANGELOG.md`：

```markdown
# Changelog

## [1.1.0] - 2026-04-20
### Added
- 新增对 rename 类型 diff 的支持

### Changed
- 优化了大文件解析性能（>10MB diff）

## [1.0.1] - 2026-04-15
### Fixed
- 修复 Windows 换行符导致的解析错误

## [1.0.0] - 2026-04-01
### Added
- 初版发布，支持统一 diff 解析
```

---

## 升级检查清单

在升级资产主版本时，引用方必须确认：

- [ ] 阅读新版 CHANGELOG
- [ ] 对比输入输出 Schema 变更
- [ ] 运行场景端到端测试
- [ ] 运行 evaluations 全量评测集
- [ ] 更新 `assets.lock` 并提交评审
