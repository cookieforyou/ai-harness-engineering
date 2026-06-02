---
name: test-quality-checklist
type: evaluation
version: "1.0.0"
status: active
---

# 测试质量清单

> 本文件为 E2E Delivery Harness 阶段/场景评估清单。

## 使用方式

1. 场景执行完成后，对照本清单逐项 PASS / PARTIAL / FAIL
2. 结合 [output-validation-checklist.md](output-validation-checklist.md) 通用项
3. 失败项写入 Handover `open_issues`

## 检查项

- [ ] V-001 完整性：必填章节与交付物齐全
- [ ] V-002 一致性：与上游 Handover 无矛盾
- [ ] V-003 准确性：假设已标注，数据可验证
- [ ] V-004 质量：Scenario KPI ≥70

## 引用

- [regression-checklist.md](regression-checklist.md)
- [common-error-patterns.md](common-error-patterns.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
