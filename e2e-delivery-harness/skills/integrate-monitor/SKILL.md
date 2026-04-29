# Skill: 监控集成 (Integrate Monitor)

## 概述

本 Skill 定义了监控集成的核心知识体系。

## 核心知识

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

## 关联资产

- **Scenario**: `../../scenarios/integrate-monitor/SCENARIO.md`
- **Instruction**: `../../instructions/integrate-monitor.instructions.md`
- **Prompt**: `../../prompts/integrate-monitor.prompt.md`
- **Agent**: `../../agents/sre-engineer.agent.md`
