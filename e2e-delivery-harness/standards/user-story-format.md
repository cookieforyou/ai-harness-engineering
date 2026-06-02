# 用户故事与 Given-When-Then 验收标准

## 用户故事模板

```
As a <role>,
I want <capability>,
so that <business value>.
```

## 验收标准（AC-*）

每条功能需求至少一条 AC，格式：

```gherkin
Given <前置条件>
When <动作>
Then <可验证结果>
```

### 可测试性要求

- Then 子句必须可观测（HTTP 状态、DB 记录、UI 元素、指标阈值）
- 禁止单独使用「快速」「友好」「稳定」等主观词；须量化或引用 MET-*

## 示例

```markdown
### REQ-042: 订单支付
**Story**: As a 买家, I want 使用微信或支付宝完成支付, so that 我可以在线完成购买.
**AC-042-1**:
Given 购物车已结算且金额 > 0
When 用户选择微信支付并确认
Then 订单状态变为 paid 且支付流水号写入 payments 表
```

## 非功能需求（NFR-*）

```markdown
### NFR-001: 性能
- Metric: p95 API latency
- Target: ≤ 200ms @ 500 RPS
- Verification: 压测报告 TC-*
```
