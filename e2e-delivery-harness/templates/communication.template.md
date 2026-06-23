---
name: communication
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 沟通通知 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 模板说明

本模板提供不同场景的沟通消息格式,包括:故障通知、状态更新、发布公告、干系人简报等。根据不同需求选择合适的模板。

---

## 模板 1: 故障通知

**场景**: 发生 P0/P1 故障时的即时通知

**渠道**: {Slack / 邮件 / IM / 电话}

**收件人**: {受影响团队和干系人}

```
主题: [故障] {服务名称} - {故障简述}

严重级别: P{0/1/2/3}
故障ID: INC-{number}
发现时间: {ISO8601}
当前状态: {处理中 / 已恢复}

影响:
- 影响服务: {affected_services}
- 影响范围: {impact_scope}
- 持续时间: {duration}

处理进度:
- {当前处理措施}
- {下一步操作}

联系人: {oncall_engineer} ({contact_info})
```

---

## 模板 2: 状态更新

**场景**: 故障处理过程中的定期状态更新

**渠道**: {Slack / 邮件}

**收件人**: {相关团队和干系人}

```
主题: [更新] INC-{number} - {故障简述} - 第 {n} 次更新

时间: {ISO8601}
故障ID: INC-{number}
当前状态: {处理中 / 已恢复 / 观察中}

进展:
1. {完成的处理步骤}
2. {当前处理阶段}

最新指标:
- 错误率: {current_rate}%
- 响应时间: {current_time}ms
- 影响用户: {count}

预计恢复时间: {ETA}

下一步: {next_steps}
```

---

## 模板 3: 发布公告

**场景**: 版本发布前后的通知

**渠道**: {Slack / 邮件}

**收件人**: {全体团队 / 干系人}

```
主题: [发布] {项目名} v{version} 发布通知

发布版本: v{version}
发布时间: {ISO8601}
发布类型: {常规 / 紧急 / 里程碑}
发布负责人: {release_manager}

变更内容:
- {change_1}
- {change_2}
- {change_3}

部署计划:
- 灰度开始: {time}
- 全量发布: {time}
- 观察期: {duration}

验证要点:
- {checkpoint_1}
- {checkpoint_2}

回滚条件: {rollback_conditions}

注意事项:
1. {note_1}
2. {note_2}
```

---

## 模板 4: 干系人简报

**场景**: 定期或里程碑向干系人汇报项目状态

**渠道**: {邮件 / 会议}

**收件人**: {干系人清单}

```
主题: [简报] {项目名} - {period} 项目状态

项目状态: {绿灯 / 黄灯 / 红灯}
报告周期: {start_date} ~ {end_date}

本期达成:
- {achievement_1}
- {achievement_2}

关键指标:
| 指标 | 目标 | 实际 | 状态 |
|------|------|------|------|
| {metric} | {target} | {actual} | 正常/警告/异常 |

风险和问题:
- {risk_1}: {status}
- {risk_2}: {status}

下期计划:
1. {plan_1}
2. {plan_2}

需要支持: {support_needed}
```

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
