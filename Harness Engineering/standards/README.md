# standards / 规范标准

本目录是 AI Harness 资产库的**制度层**，定义资产的命名、版本、质量、安全、协作等全部规范。所有资产的生命周期管理都必须以本目录文件为准绳。

---

## 规范体系

```
standards/
├── README.md
├── naming-convention.md          # 命名规范
├── versioning.md                 # 版本管理策略
├── quality-checklist.md          # 资产入库检查清单
├── skill-registry.yaml           # 全局技能索引
├── e2e-workflow-lifecycle.md     # E2E 全生命周期规范
├── scenario-integration.md       # 场景衔接规范（数据契约）
└── delivery-playbook.md          # E2E 交付全流程操作手册
```

---

## 规范效力等级

| 等级 | 说明 | 变更审批 |
| :--- | :--- | :--- |
| **P0 - 强制** | 所有资产必须遵守，违反者无法入库 | 技术委员会 |
| **P1 - 重要** | 强烈建议遵守，特殊情况可申请豁免 | 模块负责人 |
| **P2 - 建议** | 最佳实践参考，不做硬性检查 | 无 |

---

## 核心规范速查

### 命名规范 (P0)
- 文件/目录: `kebab-case`
- 变量/字段: `snake_case`
- 常量: `UPPER_SNAKE_CASE`
- ID 标识: `{module}-{name}-{version}`

### 版本规范 (P0)
- 遵循 [SemVer 2.0](https://semver.org/lang/zh-CN/)
- 资产版本独立管理，不随库整体版本强制对齐
- 破坏性变更必须升级主版本，保留旧版本至少一个周期

### 文档规范 (P1)
- 所有资产必须有 README 或自描述文件
- 中文文档优先，核心文档中英双语
- 变更日志（CHANGELOG）按资产维护

---

## 规范变更流程

1. 提交规范变更提案（修改 standards/ 下文件）
2. 评估影响范围：哪些现有资产需要改造？
3. 设定迁移窗口期与兼容性策略
4. 更新 `quality-checklist.md` 中的检查项
5. 通过评审后发布，同步通知所有资产维护者

---

## 新增规范文件

- 确定规范类型与适用范围
- 标注效力等级（P0/P1/P2）
- 提供正反示例（Do / Don't）
- 在 `README.md` 中登记索引
