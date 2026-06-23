---
name: scorecard-template
description: "交付质量评分卡模板，用于各阶段门禁评审和最终发布评审的量化评分"
type: evaluation
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
tags: ['evaluation', 'scorecard', 'quality', 'template', 'delivery']
---

# E2E Delivery Quality Scorecard

## Project Information

| Field | Value |
|-------|-------|
| **Project Name** | |
| **Delivery Phase** | |
| **Evaluation Date** | |
| **Evaluator** | |
| **Overall Score** | / 100 |

## Scoring Guidelines

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 90-100 | A | Excellent - Exceeds expectations |
| 80-89 | B | Good - Meets expectations with minor improvements |
| 70-79 | C | Satisfactory - Meets basic requirements |
| 60-69 | D | Below Average - Needs significant improvement |
| 0-59 | F | Fail - Does not meet requirements |

## Phase 1: Requirement Analysis (Weight: 15%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Completeness** (需求完整性) | 25 | | |
| - Business background and goals defined | 5 | | |
| - Stakeholders identified and analyzed | 5 | | |
| - Functional requirements coverage | 10 | | |
| - Non-functional requirements defined | 5 | | |
| **Clarity** (需求清晰度) | 25 | | |
| - Requirements are unambiguous | 10 | | |
| - Business processes clearly described | 10 | | |
| - Use cases complete and traceable | 5 | | |
| **Testability** (需求可测试性) | 25 | | |
| - Acceptance criteria defined | 10 | | |
| - Requirements are verifiable | 10 | | |
| - No conflicting requirements | 5 | | |
| **Traceability** (需求可追溯性) | 25 | | |
| - Requirements to use cases mapped | 10 | | |
| - Dependencies identified | 10 | | |
| - Version control established | 5 | | |
| **Subtotal** | 100 | | **× 15% =** |

## Phase 2: System Design (Weight: 20%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Architecture Quality** (架构质量) | 30 | | |
| - Architecture meets requirements | 10 | | |
| - Technology choices justified | 10 | | |
| - System components well-defined | 10 | | |
| **Design Completeness** (设计完整性) | 25 | | |
| - Data model complete | 8 | | |
| - API design complete | 8 | | |
| - Deployment design complete | 9 | | |
| **Security Design** (安全设计) | 15 | | |
| - Security requirements addressed | 8 | | |
| - Security controls defined | 7 | | |
| **Scalability** (可扩展性) | 15 | | |
| - Future growth considered | 8 | | |
| - Extension points defined | 7 | | |
| **Risk Analysis** (风险分析) | 15 | | |
| - Risks identified | 8 | | |
| - Mitigation strategies defined | 7 | | |
| **Subtotal** | 100 | | **× 20% =** |

## Phase 3: Task Decomposition (Weight: 10%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Task Granularity** (任务粒度) | 30 | | |
| - Tasks are appropriately sized (1-3 days) | 15 | | |
| - Tasks are clear and actionable | 15 | | |
| **Dependency Management** (依赖管理) | 25 | | |
| - Dependencies identified | 10 | | |
| - Dependencies are reasonable | 15 | | |
| **Estimation Accuracy** (估算准确性) | 25 | | |
| - Estimates are based on data | 15 | | |
| - Estimation variance within acceptable range | 10 | | |
| **Planning Quality** (计划质量) | 20 | | |
| - Iterations well-structured | 10 | | |
| - Milestones are achievable | 10 | | |
| **Subtotal** | 100 | | **× 10% =** |

## Phase 4: Development (Weight: 20%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Code Quality** (代码质量) | 35 | | |
| - Follows coding standards | 10 | | |
| - Code is readable and maintainable | 10 | | |
| - No security vulnerabilities | 10 | | |
| - Error handling is comprehensive | 5 | | |
| **Testing Coverage** (测试覆盖) | 30 | | |
| - Unit test coverage meets target (>70%) | 15 | | |
| - Test cases are comprehensive | 10 | | |
| - Tests are automated | 5 | | |
| **Documentation** (文档完整性) | 20 | | |
| - Code comments are clear | 8 | | |
| - API documentation updated | 7 | | |
| - README/user docs updated | 5 | | |
| **Compliance** (合规性) | 15 | | |
| - Design compliance | 8 | | |
| - Requirements compliance | 7 | | |
| **Subtotal** | 100 | | **× 20% =** |

## Phase 5: Testing (Weight: 15%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Test Planning** (测试计划) | 20 | | |
| - Test strategy is sound | 10 | | |
| - Test environment is appropriate | 10 | | |
| **Test Coverage** (测试覆盖) | 25 | | |
| - Functional coverage complete | 10 | | |
| - Edge cases covered | 8 | | |
| - API coverage complete | 7 | | |
| **Test Execution** (测试执行) | 30 | | |
| - Execution rate > 95% | 10 | | |
| - Pass rate > 90% | 10 | | |
| - Defects properly tracked | 10 | | |
| **Defect Management** (缺陷管理) | 15 | | |
| - Defects are well-documented | 8 | | |
| - Fix rate > 95% | 7 | | |
| **Test Reporting** (测试报告) | 10 | | |
| - Report is comprehensive | 5 | | |
| - Conclusions are clear | 5 | | |
| **Subtotal** | 100 | | **× 15% =** |

## Phase 6: Deployment (Weight: 10%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Deployment Readiness** (部署就绪) | 25 | | |
| - Deployment package verified | 10 | | |
| - Environment ready | 10 | | |
| - Rollback plan prepared | 5 | | |
| **Deployment Execution** (部署执行) | 30 | | |
| - Steps executed as planned | 15 | | |
| - Issues handled promptly | 15 | | |
| **Verification** (验证) | 25 | | |
| - Post-deployment checks passed | 10 | | |
| - Functional verification passed | 10 | | |
| - Monitoring operational | 5 | | |
| **Success Rate** (成功率) | 20 | | |
| - Deployment success 100% | 10 | | |
| - Zero data loss | 10 | | |
| **Subtotal** | 100 | | **× 10% =** |

## Phase 7: Monitoring (Weight: 10%)

| Criterion | Max Score | Score | Comments |
|-----------|-----------|-------|----------|
| **Monitoring Setup** (监控配置) | 25 | | |
| - Monitoring system operational | 10 | | |
| - Alert rules configured | 10 | | |
| - Alert channels verified | 5 | | |
| **Operational Readiness** (运维就绪) | 25 | | |
| - Runbooks prepared | 10 | | |
| - Playbooks documented | 10 | | |
| - Escalation process defined | 5 | | |
| **Incident Response** (故障响应) | 30 | | |
| - Alert response time < 5 min | 15 | | |
| - MTTR < 30 min | 15 | | |
| **System Health** (系统健康) | 20 | | |
| - Availability > 99.9% | 10 | | |
| - Performance metrics stable | 10 | | |
| **Subtotal** | 100 | | **× 10% =** |

---

## Summary

### Weighted Scores

| Phase | Weight | Score | Weighted Score |
|-------|--------|-------|----------------|
| Phase 1: Requirement Analysis | 15% | | |
| Phase 2: System Design | 20% | | |
| Phase 3: Task Decomposition | 10% | | |
| Phase 4: Development | 20% | | |
| Phase 5: Testing | 15% | | |
| Phase 6: Deployment | 10% | | |
| Phase 7: Monitoring | 10% | | |
| **Total** | 100% | | |

### Grade Calculation

| Metric | Value |
|--------|-------|
| **Total Score** | / 100 |
| **Grade** | A / B / C / D / F |
| **Status** | PASS / CONDITIONAL / FAIL |

### Strengths

1.

### Areas for Improvement

1.

### Recommendations

1.

### Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Quality Lead | | | |
| Technical Lead | | | |
| Product Owner | | | |
| Release Manager | | | |

---

*This scorecard should be completed at each phase gate and during final release review.*

## 评分卡使用检查清单

在提交评分卡前，确认以下项目全部满足：

### 维度完整性

- [ ] **SC-001**: 所有 6 个评分维度（功能完整性、质量达标、流程合规、交付时效、团队协作、风险管控）均已评分
- [ ] **SC-002**: 每个维度的评分有明确的证据支撑（数据/截图/日志链接）

### 权重与计算

- [ ] **SC-003**: 各维度权重和为 100%，无权重遗漏或重复计算
- [ ] **SC-004**: 评分计算公式正确，加权总分经 Excel/脚本交叉验证无计算错误

### 审批与门禁

- [ ] **SC-005**: 阶段性评分卡已获得 ≥2 名审批人签字（含 Technical Lead）
- [ ] **SC-006**: 综合评分 ≥70 分时准出通过，<70 分时有明确的改进计划

### 趋势与改进

- [ ] **SC-007**: 对比上一阶段评分卡，识别 ≥1 项正向趋势和 ≥1 项风险信号
- [ ] **SC-008**: 针对低分维度（<60 分）制定了可落地的改进项（含负责人和截止日期）

### 归档与追溯

- [ ] **SC-009**: 评分卡已归档至项目知识库，文件名含阶段标识和日期
- [ ] **SC-010**: 历史评分趋势图已更新，用于发布评审参考

## 相关评估

- [output-validation-checklist.md](../evaluations/output-validation-checklist.md) — 输出验证清单
- [regression-checklist.md](../evaluations/regression-checklist.md) — 回归检查清单
- [code-quality-checklist.md](../evaluations/code-quality-checklist.md) — 代码质量清单
- [deployment-quality-checklist.md](../evaluations/deployment-quality-checklist.md) — 部署质量清单
