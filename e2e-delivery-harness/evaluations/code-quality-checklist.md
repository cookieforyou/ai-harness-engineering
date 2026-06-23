---
name: code-quality-checklist
type: evaluation
version: "1.0.0"
status: active
updated: 2026-06-23
---

# 代码质量检查清单 (Code Quality Checklist)

## Purpose

本清单用于开发阶段代码评审与合入前自检，覆盖命名与结构、错误处理、安全、性能、可测试性和文档六个维度。每个检查项均提供明确的 PASS/PARTIAL/FAIL 判定标准。

## Scoring

- **PASS**: 完全满足要求
- **PARTIAL**: 部分满足，存在可接受的微小偏差
- **FAIL**: 不满足要求，必须修复后方可合入
- **NA**: 不适用

## 使用时机

- 开发完成提交 Code Review 前自检
- Code Review 评审过程中逐项核查
- 合入主分支前的最终质量门禁

---

## 1. 命名与结构 (Naming & Structure)

- [ ] **CNS-001**: 类/模块命名遵循所在语言/框架的命名规范（PascalCase/camelCase/snake_case），1 次 Code Review 未提出命名异议 → PASS；存在 1-2 处不规范 → PARTIAL；≥3 处 → FAIL
- [ ] **CNS-002**: 函数/方法单一职责：单个函数不超过 40 行（排除纯数据声明），超长需拆分且有正当理由
- [ ] **CNS-003**: 文件组织结构符合项目约定（按 feature/按 layer），无散落游离文件
- [ ] **CNS-004**: 常量与配置项集中管理，无硬编码魔法值（数字/字符串）；允许 0/1/null/空字符串等公认常量例外
- [ ] **CNS-005**: 循环复杂度 ≤ 15（Cyclomatic Complexity），超过需重构或标注豁免理由
- [ ] **CNS-006**: 嵌套深度 ≤ 4 层（if/for/while 不累计超过 4 层），超限需提取为独立函数
- [ ] **CNS-007**: 导入/引用语句按规范排序（标准库 → 第三方 → 内部模块），无未使用的 import

## 2. 错误处理 (Error Handling)

- [ ] **CEH-001**: 所有外部调用（API/DB/FS/网络）均有 try-catch/error 边界处理，无裸奔调用
- [ ] **CEH-002**: 错误信息有业务上下文（非仅 "Error occurred"），便于问题定位
- [ ] **CEH-003**: 异常分类清晰：业务异常与系统异常分离，使用自定义异常类型或错误码体系
- [ ] **CEH-004**: 资源释放有保障（文件句柄、DB 连接、网络 socket），使用 try-with-resources/using/context manager 或 finally 块
- [ ] **CEH-005**: 日志分级正确（ERROR 对应异常、WARN 对应异常但不影响流程、INFO 对应关键节点），无敏感信息泄露
- [ ] **CEH-006**: 外部依赖超时已设置（网络请求 ≤ 30s，DB 查询 ≤ 5s），超时后有 fallback 或熔断逻辑

## 3. 安全 (Security)

- [ ] **CSEC-001**: 用户输入经过校验/清洗/参数化，无直接拼接至 SQL/Shell/HTML 的场景
- [ ] **CSEC-002**: 敏感数据（密码/Token/PII）不在日志、错误消息、URL 中以明文形式出现
- [ ] **CSEC-003**: 认证与授权检查应用在 API 入口层，非仅前端隐藏按钮
- [ ] **CSEC-004**: 依赖库无已知高危 CVE（SAST/SCA 扫描通过，或已记录偏差审批）
- [ ] **CSEC-005**: 密钥/证书不硬编码在代码仓库中，使用环境变量/密钥管理服务
- [ ] **CSEC-006**: API 限流/防重放机制已考虑（敏感接口如登录/支付），非 CRUD 场景可 NA

## 4. 性能 (Performance)

- [ ] **CPF-001**: 循环内无高开销操作（DB 查询、RPC 调用、文件 IO），已提取至循环外或批量处理
- [ ] **CPF-002**: 数据集合操作考虑时间复杂度，避免 O(n²) 及以上场景（嵌套循环遍历大集合）
- [ ] **CPF-003**: 缓存策略合理：热点数据有缓存、缓存失效时间已配置、无缓存穿透风险
- [ ] **CPF-004**: 大对象/大数据集分页或流式处理，禁止全量加载至内存
- [ ] **CPF-005**: 异步/并发调用已正确使用锁或原子操作，无竞态条件
- [ ] **CPF-006**: 数据库查询有索引覆盖（通过 EXPLAIN/执行计划验证），无全表扫描（数据量 < 1 万行例外）

## 5. 可测试性 (Testability)

- [ ] **CTE-001**: 核心业务逻辑已编写单元测试，覆盖率为 ≥ 80%（分支覆盖）
- [ ] **CTE-002**: 外部依赖可 Mock/Stub，代码未直接硬编码具体实现类（依赖注入或工厂模式）
- [ ] **CTE-003**: 测试用例独立、可重复执行，无测试间数据耦合
- [ ] **CTE-004**: 边界条件已覆盖（空值、极值、特殊字符、超长输入）
- [ ] **CTE-005**: 测试命名体现被测行为：`[MethodName]_[Scenario]_[ExpectedResult]` 或等效约定

## 6. 注释与文档 (Documentation)

- [ ] **CDOC-001**: 公开 API/接口有 JSDoc/JavaDoc 风格注释，包含参数说明、返回值、异常说明
- [ ] **CDOC-002**: 复杂业务逻辑有行内注释解释"为什么"而非"是什么"
- [ ] **CDOC-003**: TODO/FIXME 已关联 Issue 编号，无遗留未解决的 TODO（允许短期追踪的 TODO）
- [ ] **CDOC-004**: 变更日志（CHANGELOG/版本发布说明）已更新

---

## Summary

| 维度 | PASS | PARTIAL | FAIL | 通过率 |
|------|------|---------|------|--------|
| 命名与结构 | __ | __ | __ | __% |
| 错误处理 | __ | __ | __ | __% |
| 安全 | __ | __ | __ | __% |
| 性能 | __ | __ | __ | __% |
| 可测试性 | __ | __ | __ | __% |
| 注释与文档 | __ | __ | __ | __% |
| **总计** | **__** | **__** | **__** | **__%** |

### 判定标准

| 通过率 | 结果 |
|--------|------|
| ≥ 90% | PASS - 可合入 |
| 70-89% | PARTIAL - 需修复 FAIL 项后合入 |
| < 70% | FAIL - 禁止合入，需整体返工 |

### 遗留问题

| # | 维度 | 检查项 | 问题描述 | 修复责任人 | 截止日期 |
|---|------|--------|----------|-----------|----------|
| 1 | | | | | |
| 2 | | | | | |

---

## References

- [regression-checklist.md](regression-checklist.md)
- [common-error-patterns.md](common-error-patterns.md)
- [static-code-analysis.md](static-code-analysis.md)
- [test-quality-checklist.md](test-quality-checklist.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
