---
name: {scenario-name}
description: "{scenario-description}"
type: scenario
version: "1.2.0"
category: "{category}"
stage: "{stage-id}"
status: active
tags: [{tag1}, {tag2}]
---

# {Scenario Title}

## Purpose

{场景目标与业务价值}

## Chain of Thought

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: ...
[VALIDATE] ...
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 |
|----|--------|----------|----------|----------|
| DC-001 | ... | ... | ... | ... |

## Error Handling (错误处理)

### Error Scenario 1: {名称}

**识别信号**: ...

**处理流程**: ...

**降级方案**: ...

**升级条件**: ...

## Quality Metrics

| KPI ID | 指标 | 目标值 |
|--------|------|--------|
| KPI-001 | ... | ≥70 合格 |

## Handover Criteria

- [ ] 准出条件 1

```yaml
handover:
  header:
    from_stage: "{from}"
    to_stage: "{to}"
```

## Related Assets

| Asset Type | Path |
|------------|------|
| Agent | `../../agents/{scenario-name}.agent.md` |
| Prompt | `../../prompts/{scenario-name}.prompt.md` |
| Instruction | `../../instructions/{scenario-name}.instructions.md` |
| Skill | `../../skills/{scenario-name}/SKILL.md` |

## Prerequisites

- [ ] 前置条件 1
