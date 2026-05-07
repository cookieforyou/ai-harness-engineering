---
name: integrate-monitor
description: "Domain skill for integrate-monitor execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 监控集成 (Integrate Monitor)

## Overview

本 Skill 定义了监控集成的核心知识体系。

## Core Knowledge

### 可观测性三大支柱

```python
class ObservabilitySkill:
    """可观测性技能"""

    def __init__(self):
        self.three_pillars = {
            "metrics": {
                "description": "指标 - 聚合的数值数据",
                "tools": ["Prometheus", "Datadog"],
                "types": ["Counter", "Gauge", "Histogram"]
            },
            "logs": {
                "description": "日志 - 事件的时间序列",
                "tools": ["ELK", "Loki", "Splunk"],
                "formats": ["JSON", "Plain Text"]
            },
            "traces": {
                "description": "链路 - 请求的完整路径",
                "tools": ["Jaeger", "Zipkin", "Tempo"],
                "concepts": ["Span", "Trace", "Context Propagation"]
            }
        }

    def implement_metrics(self, service):
        """
        实现指标监控
        """
        # 1. 选择采集方式
        # 2. 定义指标
        # 3. 配置导出

    def implement_tracing(self, service):
        """
        实现链路追踪
        """
        # 1. 集成 SDK
        # 2. 配置采样
        # 3. 配置导出
```

## Associated Assets

- **Scenario**: `../../scenarios/integrate-monitor/SCENARIO.md`
- **Instruction**: `../../instructions/integrate-monitor.instructions.md`
- **Prompt**: `../../prompts/integrate-monitor.prompt.md`
- **Agent**: `../../agents/integrate-monitor.agent.md`


## Core Knowledge

> Essential knowledge domain for integrate-monitor execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for integrate-monitor excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during integrate-monitor execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
