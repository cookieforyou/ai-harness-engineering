---
name: manage-tech-debt
description: 技术债务管理场景的技术指令
type: instructions
stage: "manage-tech-debt"
version: "1.1.0"
---

# Technical Debt Management Instructions

## Overview

本指令提供技术债务管理的详细技术规范和工具使用指南。

## Debt Quantification Framework

### Code Quality Metrics

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Cyclomatic Complexity | < 10 | 10-20 | > 20 |
| Lines of Code (per function) | < 20 | 20-50 | > 50 |
| Code Duplication | < 3% | 3-10% | > 10% |
| Comment Ratio | 20-30% | 10-20% | < 10% |
| Method Length | < 10 | 10-20 | > 20 |

### Technical Debt Ratio (TDR)

```
TDR = (Cost to Fix / Cost to Rebuild) × 100%

Excellent:  < 5%
Good:       5-10%
Acceptable: 10-15%
High:       15-25%
Critical:   > 25%
```

### Interest Rate Model

| Debt Type | Interest Rate | Impact |
|-----------|---------------|--------|
| 代码债务 | 5%/月 | 开发效率下降 |
| 架构债务 | 10%/月 | 扩展成本增加 |
| 测试债务 | 8%/月 | Bug 修复时间增加 |
| 文档债务 | 3%/月 | 新人上手时间增加 |

## Analysis Tools

### Static Code Analysis

```bash
# SonarQube
sonar-scanner -Dsonar.projectKey=myproject

# ESLint (JavaScript/TypeScript)
eslint src/ --format json > eslint-report.json

# Pylint (Python)
pylint src/ --output-format=json > pylint-report.json

# Checkstyle (Java)
mvn checkstyle:checkstyle
```

### Code Complexity Analysis

```bash
# Radon (Python)
radon cc -a -b src/

# ESComplex (JavaScript)
escomplex -t

# SonarQube Code Complexity
sonar.issues.sort=COMPLEXITY
```

### Dependency Analysis

```bash
# Dependabot (GitHub)
# .github/dependabot.yml

# npm audit
npm audit --json > audit-report.json

# Snyk
snyk test --json > snyk-report.json
```

## Refactoring Patterns

### 1. Extract Method

**Before:**
```python
def process_order(order):
    # Validate order
    if not order.items:
        raise ValueError("Empty order")
    if order.total < 0:
        raise ValueError("Invalid total")
    
    # Calculate discount
    if order.customer.tier == "premium":
        discount = order.total * 0.2
    else:
        discount = order.total * 0.1
    
    # Apply discount
    order.total = order.total - discount
    
    # Save order
    db.save(order)
    
    # Send notification
    email.send(order.customer, "Order confirmed")
```

**After:**
```python
def process_order(order):
    validate_order(order)
    apply_discount(order)
    save_and_notify(order)

def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")
    if order.total < 0:
        raise ValueError("Invalid total")

def apply_discount(order):
    rate = 0.2 if order.customer.tier == "premium" else 0.1
    discount = order.total * rate
    order.total = order.total - discount
```

### 2. Replace Conditional with Polymorphism

**Before:**
```python
def calculate_shipping(order):
    if order.country == "US":
        return order.weight * 0.5
    elif order.country == "UK":
        return order.weight * 0.7
    elif order.country == "CN":
        return order.weight * 0.8
    else:
        return order.weight * 1.0
```

**After:**
```python
class ShippingStrategy:
    def calculate(self, order):
        raise NotImplementedError

class USShipping(ShippingStrategy):
    def calculate(self, order):
        return order.weight * 0.5

class UKShipping(ShippingStrategy):
    def calculate(self, order):
        return order.weight * 0.7

class ShippingFactory:
    @staticmethod
    def get_strategy(country):
        strategies = {
            "US": USShipping(),
            "UK": UKShipping(),
        }
        return strategies.get(country, DefaultShipping())
```

### 3. Introduce Null Object

**Before:**
```python
def get_customer_name(customer):
    if customer is None:
        return "Guest"
    return customer.name
```

**After:**
```python
class NullCustomer:
    name = "Guest"
    
def get_customer_name(customer):
    return (customer or NullCustomer()).name
```

## Debt Repayment Strategies

### Strategy 1: Boy Scout Rule

> "Leave the code cleaner than you found it"

```yaml
implementation:
  rule: "每次提交必须修复至少一个问题"
  scope:
    - 代码异味
    - 命名不规范
    - 缺少注释
    - 小规模重构
  validation: "所有测试必须通过"
```

### Strategy 2: dedicated Debt Sprints

```yaml
planning:
  frequency: "每季度一次"
  duration: "1-2 周"
  team_size: "2-4 人"
  focus: "高优先级债务"
  goals:
    - 债务清单减少 30%
    - 关键指标改善
    - 文档更新
```

### Strategy 3: Investment Time

```yaml
allocation:
  principle: "20% 时间用于技术改进"
  breakdown:
    - 10%: 债务偿还
    - 5%: 工具改进
    - 5%: 学习研究
  tracking: "在 Sprint 中明确任务"
```

## Prevention Mechanisms

### CI/CD Quality Gates

```yaml
quality_gates:
  - name: "Code Coverage"
    threshold: 80%
    fail_on_decrease: true
    
  - name: "Code Smells"
    max_per_file: 5
    max_per_function: 1
    
  - name: "Technical Debt Ratio"
    max: 5%
    
  - name: "Critical Issues"
    count: 0
```

### Code Review Checklist

```markdown
## Technical Debt Review Checklist

### 代码质量
- [ ] 函数长度 < 50 行
- [ ] 圈复杂度 < 10
- [ ] 无重复代码
- [ ] 命名规范清晰

### 架构
- [ ] 无循环依赖
- [ ] 符合 SOLID 原则
- [ ] 适当的抽象层级

### 测试
- [ ] 测试覆盖 > 80%
- [ ] 无脆弱测试
- [ ] 测试命名规范

### 文档
- [ ] 复杂逻辑有注释
- [ ] 公共 API 有文档
- [ ] 更新相关文档
```

## Metrics Dashboard

### Key Metrics

| Metric | Baseline | Target | Frequency |
|--------|----------|--------|-----------|
| TDR | 15% | < 5% | Monthly |
| Code Coverage | 65% | > 80% | Sprint |
| Avg. Function Length | 35 | < 20 | Weekly |
| Debt Items Open | 150 | < 50 | Monthly |
| Debt Interest Rate | 8% | < 3% | Quarterly |

### Tracking Tools

- SonarQube Dashboard
- Jira Debt Tickets
- Custom Dashboard (Grafana)
- Tech Radar


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-tech-debt.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for manage-tech-debt execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for manage-tech-debt.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for manage-tech-debt deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
