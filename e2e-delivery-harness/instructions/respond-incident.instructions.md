---
name: respond-incident
description: "事件响应场景的技术指令"
applyTo: "scenarios/respond-incident/**"
phase: incident-response
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Incident Response Instructions

## Overview

This instruction defines the technical execution standards and operational procedures for incident response across the E2E delivery lifecycle. It covers incident classification and severity assignment, triage procedures, communication cadences, escalation paths, mitigation techniques, and post-incident stabilization procedures. The instruction ensures rapid, coordinated response to production incidents with clear roles, defined service level targets for detection and resolution, and continuous improvement through blameless post-incident reviews.


## Incident Lifecycle

```
Detection → Triage → Response → Mitigation → Resolution → Follow-up
     │          │         │          │            │           │
  告警触发   严重程度    组建团队    临时修复     根本解决    复盘改进
```

## Severity Response Matrix

| Severity | Response Time | Mitigation SLA | Resolution SLA | Communication |
|----------|---------------|----------------|----------------|---------------|
| P0 | 5 min | 15 min | 1 hour | Every 15 min |
| P1 | 15 min | 1 hour | 4 hours | Every 30 min |
| P2 | 1 hour | 4 hours | 8 hours | Every 2 hours |
| P3 | 4 hours | 8 hours | 24 hours | Daily |

## On-Call Best Practices

### Rotation Structure
```yaml
oncall_rotation:
  primary:
    name: "Primary On-Call"
    escalation: 1
    response_time: 5 min
    
  secondary:
    name: "Secondary On-Call"
    escalation: 2
    response_time: 15 min
    
  manager:
    name: "On-Call Manager"
    escalation: 3
    response_time: 30 min
```

### Escalation Rules
```yaml
escalation:
  - condition: "No response in 5 min"
    action: "Escalate to secondary"
    
  - condition: "Issue not resolved in 30 min"
    action: "Escalate to manager"
    
  - condition: "P0 incident"
    action: "Immediate all-hands"
```

## Diagnostic Commands

### System Health
```bash
# CPU and Memory
top -bn1 | head -20
free -m
uptime

# Disk
df -h
iostat -x 5 3

# Network
netstat -tuln
ss -s
```

### Application Health
```bash
# Process status
ps aux | grep <process>
systemctl status <service>

# Logs
tail -f {{log_dir}}/<service>.log
journalctl -u <service> -n 100

# Port check
lsof -i :<port>
```

### Kubernetes
```bash
# Pod status
kubectl get pods -n <namespace>
kubectl describe pod <pod> -n <namespace>

# Events
kubectl get events -n <namespace> --sort-by='.lastTimestamp'

# Logs
kubectl logs <pod> -n <namespace> --tail=100
kubectl logs <pod> -n <namespace> --previous
```

## Common Fix Patterns

### Pattern 1: Pod Restart
```bash
kubectl rollout restart deployment/<name> -n <namespace>
kubectl rollout undo deployment/<name> -n <namespace>
```

### Pattern 2: Scale Up
```bash
kubectl scale deployment/<name> --replicas=10 -n <namespace>
```

### Pattern 3: Resource Adjustment
```bash
kubectl patch deployment/<name> -n <namespace> -p '{"spec":{"template":{"spec":{"containers":[{"name":"<container>","resources":{"limits":{"memory":"2Gi"}}}]}}}}'
```

### Pattern 4: Config Reload
```bash
kubectl exec <pod> -n <namespace> -- kill -HUP 1
```

## Communication Templates

### Incident Declaration
```markdown
## Incident Declaration

**事件 ID**: INC-2024-001
**严重程度**: P1
**状态**: Active
**时间**: 2024-01-01 14:30 UTC

### 影响
- 服务: API Gateway
- 影响范围: 约 30% 请求失败
- 用户影响: 部分用户无法下单

### 当前状态
- 已识别根因
- 正在执行修复

### 下次更新时间
15:00 UTC

### 事件频道
#incident-2024-001
```

### Status Update
```markdown
## Status Update (15:00 UTC)

**事件 ID**: INC-2024-001
**更新次数**: 3

### 当前状态
- [x] 根因已识别
- [x] 修复方案已确定
- [ ] 修复执行中
- [ ] 验证中

### 最新进展
正在执行 Pod 重启，预计 10 分钟内完成

### 下次更新时间
15:30 UTC
```

### Incident Resolution
```markdown
## Incident Resolution

**事件 ID**: INC-2024-001
**解决时间**: 15:45 UTC
**总持续时间**: 1 小时 15 分钟

### 摘要
API Gateway 因配置变更导致内存泄漏，已通过回滚配置解决

### 时间线
- 14:30 - 首次告警
- 14:35 - 事件升级 P1
- 14:50 - 根因识别
- 15:30 - 开始修复
- 15:45 - 服务恢复

### 影响统计
- 受影响用户: ~5,000
- 失败请求: ~50,000
- 业务损失: ~$1,000

### 后续行动
- [ ] 改进配置变更流程
- [ ] 增加内存监控告警
- [ ] 制定容量规划

### 复盘会议
时间: 2024-01-03 14:00 UTC
```

## Runbooks

### Runbook 1: High CPU
```bash
#!/bin/bash
# High CPU Investigation

# 1. Identify top CPU processes
top -bn1 -o %CPU | head -15

# 2. Check for runaway processes
ps aux --sort=-%cpu | head -10

# 3. Container-level CPU
docker stats --no-stream

# 4. Application logs
grep -i "error\|warning" {{log_dir}}/app.log | tail -50

# 5. If necessary, restart
systemctl restart <service>
```

### Runbook 2: Database Connection Exhaustion
```bash
#!/bin/bash
# Database Connection Issue

# 1. Check connection count
SELECT count(*) FROM pg_stat_activity;

# 2. Check long-running queries
SELECT * FROM pg_stat_activity WHERE state = 'active' AND query_start < now() - interval '5 minutes';

# 3. Kill long-running queries (if needed)
SELECT pg_terminate_backend(pid);

# 4. Check application connection pool
curl -s <app>/actuator/metrics/hikaricp.connections.active
```

### Runbook 3: Service Not Responding
```bash
#!/bin/bash
# Service Not Responding

# 1. Check if service is running
systemctl status <service>
curl -v {{health_endpoint}}

# 2. Check network connectivity
telnet <host> <port>
nc -zv <host> <port>

# 3. Check upstream dependencies
curl -v http://<upstream>/health

# 4. Check DNS resolution
nslookup <service>
dig <service>

# 5. If healthy, restart
systemctl restart <service>
```

## SLA Calculator

```python
def calculate_impact(sla_target, downtime_minutes, users_affected, total_users):
    """
    Calculate business impact of an incident
    
    Args:
        sla_target: SLA percentage (e.g., 99.95)
        downtime_minutes: Total downtime in minutes
        users_affected: Number of users affected
        total_users: Total users
    """
    current_uptime = 100 - (downtime_minutes / (30 * 24 * 60) * 100)
    users_impact_pct = (users_affected / total_users) * 100
    revenue_impact = estimate_revenue_impact(downtime_minutes)
    
    return {
        "current_uptime": current_uptime,
        "sla_violation": current_uptime < sla_target,
        "users_impact_pct": users_impact_pct,
        "revenue_impact": revenue_impact
    }
```


## Technical Specifications

> Detailed technical requirements and implementation guidelines for respond-incident.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for respond-incident execution.

1. **Practice 1**: Acknowledge alerts promptly and assess severity
2. **Practice 2**: Communicate status updates to stakeholders regularly
3. **Practice 3**: Document timeline and actions for post-incident review


## Multi-Language Code Examples

### PagerDuty API - Incident Management (Python)

```python
#!/usr/bin/env python3
"""
PagerDuty 事件响应集成脚本
功能: 创建事件、升级通知、确认解决、查询事件详情

Requires: pip install pagerduty
"""
import os
import json
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

PD_API_KEY = os.getenv("PAGERDUTY_API_KEY", "")
PD_SERVICE_ID = os.getenv("PAGERDUTY_SERVICE_ID", "")
PD_FROM_EMAIL = os.getenv("PAGERDUTY_FROM_EMAIL", "incident-commander@company.com")


class PagerDutyIncidentClient:
    """
    封装 PagerDuty REST API v2，提供事件生命周期管理。
    支持: 创建事件、触发升级、确认、解决、附加上下文。
    """

    BASE_URL = "https://api.pagerduty.com"

    def __init__(self, api_key: str, from_email: str):
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Token token={api_key}",
            "From": from_email,
        }

    def trigger_incident(self, title: str, severity: str,
                         service_id: str, body: str,
                         escalation_policy_id: Optional[str] = None) -> Dict:
        """
        触发一个新的事件（P0/P1/P2/P3）。

        Args:
            title: 事件标题
            severity: P0/P1/P2/P3
            service_id: PagerDuty Service ID
            body: 事件详细描述
            escalation_policy_id: 升级策略（可选，覆盖默认）
        """
        payload = {
            "incident": {
                "type": "incident",
                "title": title,
                "service": {"id": service_id, "type": "service_reference"},
                "urgency": "high" if severity in ("P0", "P1") else "low",
                "body": {
                    "type": "incident_body",
                    "details": body,
                },
            }
        }

        if escalation_policy_id:
            payload["incident"]["escalation_policy"] = {
                "id": escalation_policy_id,
                "type": "escalation_policy_reference",
            }

        resp = requests.post(
            f"{self.BASE_URL}/incidents",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        incident = resp.json()["incident"]
        logger.info("Incident %s created with severity %s", incident["id"], severity)
        return incident

    def acknowledge_incident(self, incident_id: str) -> Dict:
        """确认事件，停止升级计时器。"""
        payload = {
            "incidents": [{
                "id": incident_id,
                "type": "incident_reference",
                "status": "acknowledged",
            }]
        }
        resp = requests.put(
            f"{self.BASE_URL}/incidents",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        logger.info("Incident %s acknowledged", incident_id)
        return resp.json()

    def resolve_incident(self, incident_id: str) -> Dict:
        """解决事件。"""
        payload = {
            "incidents": [{
                "id": incident_id,
                "type": "incident_reference",
                "status": "resolved",
            }]
        }
        resp = requests.put(
            f"{self.BASE_URL}/incidents",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        logger.info("Incident %s resolved", incident_id)
        return resp.json()

    def add_note(self, incident_id: str, note: str) -> Dict:
        """
        为事件添加注释，用于记录排查过程、决策和操作记录。
        每条注释都有时间戳，用于事后复盘的时间线重建。
        """
        payload = {"note": {"content": f"[{datetime.now(timezone.utc).isoformat()}] {note}"}}
        resp = requests.post(
            f"{self.BASE_URL}/incidents/{incident_id}/notes",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        logger.info("Note added to incident %s", incident_id)
        return resp.json()

    def get_incident_timeline(self, incident_id: str) -> List[Dict]:
        """获取事件完整时间线，用于复盘和报告生成。"""
        resp = requests.get(
            f"{self.BASE_URL}/incidents/{incident_id}/notes",
            headers=self.headers,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json().get("notes", [])


# Usage
if __name__ == "__main__":
    client = PagerDutyIncidentClient(PD_API_KEY, PD_FROM_EMAIL)
    # Trigger P1 incident for database failure
    inc = client.trigger_incident(
        title="Production DB - Connection Pool Exhaustion",
        severity="P1",
        service_id=PD_SERVICE_ID,
        body="Database connection pool is exhausted. Error rate increased by 35%.\n"
             "Affected services: checkout-service, order-service\n"
             "Impact: ~15% of users cannot complete checkout.",
    )
    client.add_note(inc["id"], "Root cause identified: connection leak in payment handler")
    print(json.dumps(inc, indent=2))
```

### Slack Webhook - Incident Notification (Python)

```python
#!/usr/bin/env python3
"""
Slack Webhook 事件通知工具
战时沟通: 事件声明、状态更新、升级通知、解决公告

渠道设计:
  - #incidents:      所有事件声明和解决公告
  - #inc-{ID}:      单个事件的专用战时频道
  - @oncall:        直接 @oncall 组升级通知
"""
import json
import os
from datetime import datetime
from typing import Optional

import requests

SLACK_WEBHOOK_URL = os.getenv("SLACK_INCIDENT_WEBHOOK", "")
SLACK_INCIDENT_CHANNEL = os.getenv("SLACK_INCIDENT_CHANNEL", "#incidents")


def post_incident_declaration(
    incident_id: str,
    severity: str,
    title: str,
    service: str,
    impact: str,
    commander: str,
    channel: str = SLACK_INCIDENT_CHANNEL,
) -> bool:
    """
    发送事件声明消息到 Slack。包含严重级别、影响范围和指挥官信息。

    消息格式采用 Slack Block Kit，确保关键信息一目了然。
    """
    severity_colors = {"P0": "#FF0000", "P1": "#FF6600", "P2": "#FFCC00", "P3": "#999999"}

    blocks = [
        {"type": "header", "text": {"type": "plain_text",
                                    "text": f"[{severity}] Incident Declared: {incident_id}"}},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": f"*Title:*\n{title}"},
            {"type": "mrkdwn", "text": f"*Severity:*\n{severity}"},
            {"type": "mrkdwn", "text": f"*Service:*\n{service}"},
            {"type": "mrkdwn", "text": f"*Commander:*\n{commander}"},
            {"type": "mrkdwn", "text": f"*Impact:*\n{impact}"},
            {"type": "mrkdwn", "text": f"*Time:*\n{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}"},
        ]},
        {"type": "divider"},
        {
            "type": "context",
            "elements": [{"type": "mrkdwn",
                          "text": f":loudspeaker: Follow updates in <#inc-{incident_id.lower()}>"}],
        },
    ]

    payload = {
        "channel": channel,
        "attachments": [{"color": severity_colors.get(severity, "#FF0000"),
                         "blocks": blocks}],
    }

    resp = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    resp.raise_for_status()
    return True


def post_status_update(incident_id: str, status: str,
                       progress: str, next_update: str,
                       channel: str) -> bool:
    """
    发送周期性状态更新。战时沟通要求:
      - P0: 每 15 分钟更新一次
      - P1: 每 30 分钟更新一次
      - P2: 每 2 小时更新一次
    """
    blocks = [
        {"type": "section", "text": {
            "type": "mrkdwn",
            "text": f"*Status Update: {incident_id}*\n"
                    f"*Current Status:* {status}\n"
                    f"*Progress:* {progress}\n"
                    f"*Next Update:* {next_update}",
        }},
    ]
    payload = {"channel": channel, "blocks": blocks}
    resp = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    return resp.ok


def post_incident_resolved(incident_id: str, summary: str,
                           duration: str, timeline: str,
                           channel: str = SLACK_INCIDENT_CHANNEL) -> bool:
    """发送事件解决公告，包含摘要和关键时间线。"""
    blocks = [
        {"type": "header", "text": {"type": "plain_text",
                                    "text": f"Resolved: {incident_id}"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Summary:*\n{summary}"}},
        {"type": "section", "fields": [
            {"type": "mrkdwn", "text": f"*Duration:*\n{duration}"},
            {"type": "mrkdwn", "text": f"*Timeline:*\n{timeline}"},
        ]},
    ]
    payload = {"channel": channel, "blocks": blocks}
    resp = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    return resp.ok
```

### Statuspage API - Incident Status Updates (Python)

```python
#!/usr/bin/env python3
"""
Atlassian Statuspage API 集成
在事件响应期间同步更新公共/内部状态页面，减少用户询问。

Requires: pip install requests
"""
import os
import json
from typing import Dict, Optional

import requests

STATUSPAGE_API_KEY = os.getenv("STATUSPAGE_API_KEY", "")
STATUSPAGE_PAGE_ID = os.getenv("STATUSPAGE_PAGE_ID", "")


class StatuspageClient:
    """管理 Statuspage 事件和组件状态。"""

    BASE_URL = "https://api.statuspage.io/v1"

    def __init__(self, api_key: str, page_id: str):
        self.headers = {
            "Authorization": f"OAuth {api_key}",
            "Content-Type": "application/json",
        }
        self.page_id = page_id

    def create_incident(self, name: str, status: str,
                        impact_override: str,
                        component_ids: list,
                        body: str) -> Dict:
        """
        在 Statuspage 上创建事件公告。

        status: investigating/identified/monitoring/resolved
        impact_override: none/minor/major/critical
        """
        payload = {
            "incident": {
                "name": name,
                "status": status,
                "impact_override": impact_override,
                "body": body,
                "component_ids": component_ids,
            }
        }
        resp = requests.post(
            f"{self.BASE_URL}/pages/{self.page_id}/incidents",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def update_incident_status(self, incident_id: str,
                               status: str, body: str) -> Dict:
        """
        更新事件状态 - 在整个事件生命周期中调用。

        状态流转: investigating -> identified -> monitoring -> resolved
        """
        payload = {"incident": {"status": status, "body": body}}
        resp = requests.patch(
            f"{self.BASE_URL}/pages/{self.page_id}/incidents/{incident_id}",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def update_component_status(self, component_id: str, status: str) -> Dict:
        """
        更新单个组件的运行状态。

        status: operational/degraded_performance/partial_outage/major_outage
        """
        payload = {"component": {"status": status}}
        resp = requests.patch(
            f"{self.BASE_URL}/pages/{self.page_id}/components/{component_id}",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()


# 事件状态同步工作流示例
def incident_status_sync_workflow(statuspage: StatuspageClient,
                                  incident_id_input: str,
                                  severity: str,
                                  component: str):
    """
    事件响应过程中的 Statuspage 自动同步流程

    流程:
      告警触发 -> Statuspage: investigating -> 发现根因 -> Statuspage: identified
      -> 修复部署 -> Statuspage: monitoring -> 确认恢复 -> Statuspage: resolved
    """
    impact_map = {"P0": "critical", "P1": "major", "P2": "minor", "P3": "minor"}

    # Phase 1: 事件声明
    statuspage.update_component_status(component, "partial_outage" if severity in ("P0", "P1") else "degraded_performance")
    statuspage.create_incident(
        name=f"[{severity}] Production Incident - {component}",
        status="investigating",
        impact_override=impact_map.get(severity, "minor"),
        component_ids=[component],
        body="We are investigating a potential issue with the service. "
             "Further updates will be provided shortly.",
    )
```

### Grafana Annotation API - 事件标记 (Python)

```python
#!/usr/bin/env python3
"""
Grafana Annotation API 集成: 在事件响应期间自动在 Dashboard 上
标记关键时间点，便于事后复盘时直观看到事件时间线与指标变化的关联。
"""
import os
from datetime import datetime, timezone
from typing import Dict, Optional

import requests

GRAFANA_URL = os.getenv("GRAFANA_URL", "http://grafana:3000")
GRAFANA_API_KEY = os.getenv("GRAFANA_SERVICE_ACCOUNT_TOKEN", "")


class GrafanaAnnotationClient:
    """
    Grafana Annotation 管理客户端。

    Annotation 用于在 Dashboard 图表上标记关键时间点:
      - 事件开始 (红色)
      - 根因定位 (黄色)
      - 修复部署 (蓝色)
      - 事件解决 (绿色)
    """

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def create_annotation(self, dashboard_uid: str, panel_id: int,
                          text: str, tags: Optional[list] = None,
                          time_usec: Optional[int] = None) -> Dict:
        """
        在指定的 Dashboard 和 Panel 上添加 Annotation 标记。

        Args:
            dashboard_uid: Grafana Dashboard UID
            panel_id: Panel ID (-1 表示所有 panel)
            text: Annotation 文本描述
            tags: 标签列表 (如 ["incident", "P1"])
            time_usec: 时间戳 (微秒)，默认当前时间

        标签规范:
          - severity:P0/P1/P2/P3
          - phase:declaration/detection/mitigation/resolution
          - service:<service_name>
        """
        payload = {
            "dashboardUID": dashboard_uid,
            "panelId": panel_id,
            "text": text,
            "tags": tags or [],
            "time": time_usec or int(datetime.now(timezone.utc).timestamp() * 1000),
            "timeEnd": 0,
        }

        resp = requests.post(
            f"{self.base_url}/api/annotations",
            headers=self.headers,
            json=payload,
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()

    def create_incident_timeline_annotations(
        self, dashboard_uid: str, incident_id: str,
        severity: str, service: str
    ) -> Dict:
        """
        在事件响应过程中自动创建完整时间线标记序列。
        只需调用一次，按事件生命周期逐步填充注释。
        """
        results = {}
        # 事件声明标记
        results["declaration"] = self.create_annotation(
            dashboard_uid, 0,
            f"[{severity}] {incident_id} - Incident Declared: {service}",
            tags=["incident", f"severity:{severity}", "phase:declaration", f"service:{service}"],
        )
        return results
```

## Error Handling

### Error Scenario 1: 告警升级路径失效 (P0)

**触发条件**: P0/P1 事件触发后，Primary On-Call 在 5 分钟内未响应，Secondary 在 15 分钟内也未响应，自动升级机制未能触达可响应人员

**处理流程**:
```
IF Primary 超时未响应 (5min) AND Secondary 超时未响应 (15min)
THEN
  1. 立即启动 Manual Override:
     a. 通过 PagerDuty 的 override 功能强制指派给已知在线人员
     b. 同时拨打值班经理电话
     c. 在 #incidents Slack 频道 @channel 全员广播
  2. 检查 PagerDuty 配置：
     a. 验证升级策略的层级配置是否正确
     b. 验证通知渠道（电话、短信、推送）是否正常
     c. 检查值班人员日历是否覆盖了节假日
  3. 临时解决方案:
     a. 从团队中指定备用 On-Call
     b. 建立临时通信渠道（企业微信/钉钉群）
  4. 事后修复:
     a. 更新 PagerDuty 升级策略
     b. 增加多层升级路径（至少 3 层）
     c. 添加 SMS 和语音电话双通道
END
```

**降级方案**: 手动呼叫值班团队 leader，逐层电话通知直到有人响应

**升级条件**: 30 分钟内无人响应事件，升级至 VP Engineering 并启动全团队紧急召集

### Error Scenario 2: 战时沟通混乱 (P1)

**触发条件**: 事件响应过程中出现多个并行沟通渠道（Slack、微信、电话同时涌入信息），关键状态更新丢失，指挥官无法掌握全局

**处理流程**:
```
IF 沟通混乱导致信息丢失
THEN
  1. 指挥官立即执行 Communication Lockdown:
     a. 所有沟通统一到 #inc-{ID} 专用频道
     b. 禁止在多个渠道并行讨论
     c. 非响应人员设为只读模式（仅指挥官和管理层可以发公告）
  2. 建立沟通节奏:
     a. 指挥官每 15-30 分钟发布一次正式状态更新
     b. 使用标准模板（当前状态、进展、下次更新时间）
     c. 所有决策以指挥官发布的文字记录为准
  3. 设立沟通副官角色：
     a. 一人负责对外沟通（管理层/客户/Statuspage）
     b. 一人负责对内协调（技术团队/日志查询）
  4. 启用 War Room:
     a. 视频会议 / Zoom 作为实时讨论渠道
     b. Slack 频道仅用于公告和决策记录
END
```

**降级方案**: 切换到纯文字沟通（禁用语音/视频），防止信息过载

**升级条件**: 事件持续超过 1 小时仍混乱，升级至 Incident Management 团队介入指挥架构重组

### Error Scenario 3: 错误定级导致响应不足 (P1)

**触发条件**: 事件初始被评定为 P2/P3，但实际影响达到 P0/P1 级别，导致响应资源不足延误修复

**处理流程**:
```
IF 发现定级错误/影响超出预期
THEN
  1. 当前负责人立即执行 Severity Re-classification:
     a. 重新评估影响范围（实际受影响用户 %）
     b. 重新评估业务影响（收入损失、安全风险）
     c. 检查是否有遗漏的关键服务受影响
  2. 执行 Severity Upgrade:
     a. 在 PagerDuty 更新事件 severity
     b. 触发更高级别的升级策略
     c. 增加响应人手（从 2 人扩展到全团队）
  3. 加速响应流程:
     a. 缩短状态更新间隔（P1→15min, P0→5min）
     b. 立即通知更高级别的技术负责人
     c. 启用更多调试和监控资源
  4. 事后改进:
     a. 复盘定级失误原因
     b. 改进告警规则自动定级逻辑
     c. 建立快速升级机制
END
```

**降级方案**: 不确定 severity 时，默认按高一级处理，事后可降级

**升级条件**: 事件定级错误导致 MTTR 超过 SLA 200%，需做定级流程改进

### Error Scenario 4: 恢复操作验证不充分，二次故障 (P0)

**触发条件**: 修复部署后认为事件已解决，但 30 分钟内出现相同或关联故障

**处理流程**:
```
IF 二次故障发生在首次解决后 30 分钟内
THEN
  1. 立即评估二次故障的严重程度和影响范围
  2. IF 二次故障 >= 原故障 THEN:
     a. 立即回滚修复（全量回滚到事件前版本）
     b. 启动更深入的根因分析
     c. 考虑联系厂商或第三方专家支持
  3. IF 二次故障 < 原故障 THEN:
     a. 评估是否接受权衡（降级运行 vs 再次修复）
     b. 如果选择修复，需增加更多测试验证
     c. 延长观察期至 2 小时
  4. 增加观察频次:
     a. 每 5 分钟检查一次关键指标
     b. 自动告警阈值临时收紧 50%
     c. 保持 War Room 人员就位
END
```

**降级方案**: 保持降级运行模式，禁用新功能或非核心服务保障核心功能

**升级条件**: 3 次修复尝试均导致二次故障，需架构评审并考虑大版本回滚

## Quality Standards

> Acceptance criteria and quality gates for respond-incident deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Mean time to recovery (MTTR) is 1 hour or less | Automated check |
| Standard 2 | Escalation accuracy is 90% or higher | Automated check |
| Standard 3 | First communication is sent within 15 minutes | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
