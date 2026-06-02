# Requirement Quality Checklist (需求质量检查清单)

> 需求分析阶段准出检查。完整回归项见 [regression-checklist.md](regression-checklist.md) 阶段 R-*。

## 完整性 (R-001 ~ R-005)

- [ ] **R-001**: 业务目标（OBJ-*）符合 [smart-criteria.md](../standards/smart-criteria.md)
- [ ] **R-002**: 四类干系人已识别（见 [stakeholder-analysis-guide.md](../standards/stakeholder-analysis-guide.md)）
- [ ] **R-003**: 功能需求 REQ-* 使用 [user-story-format.md](../standards/user-story-format.md)
- [ ] **R-004**: 非功能需求 NFR-* 可量化
- [ ] **R-005**: 追溯矩阵 REQ → OBJ 覆盖率 ≥95%

## 质量 (R-006 ~ R-010)

- [ ] **R-006**: 验收标准 AC-* 100% 可测试
- [ ] **R-007**: 优先级 P0–P3 已标注
- [ ] **R-008**: 冲突已记录 DC-* 并解决或升级
- [ ] **R-009**: 假设与约束已显式列出
- [ ] **R-010**: Handover YAML 已生成

## 评分

| 通过项占比 | 建议 |
|------------|------|
| ≥90% | 准出 |
| 70–89% | 修复后准出 |
| <70% | 禁止进入 design-system |
