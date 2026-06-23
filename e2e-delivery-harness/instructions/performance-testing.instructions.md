---
name: performance-testing
description: "Detailed technical instructions for performance-testing scenario execution"
applyTo: "scenarios/performance-testing/**"
phase: testing
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instruction: 性能测试技术规范

## Overview

本文档定义了性能测试阶段的技术规范和执行标准，用于指导 AI Agent 执行专业级的性能测试工作。

## Performance Test Types

| 测试类型 | 目的 | 持续时间 | 并发用户 |
|----------|------|----------|----------|
| 基准测试 | 获取单用户性能基线 | 5-10 分钟 | 1 |
| 负载测试 | 验证正常负载下的性能 | 30-60 分钟 | 目标 50% |
| 压力测试 | 找出系统极限 | 20-30 分钟 | 逐步增加至崩溃 |
| 稳定性测试 | 验证长时间运行稳定性 | 8-24 小时 | 目标 70% |
| 峰值测试 | 验证峰值负载能力 | 1-2 小时 | 目标 100%+ |

## Performance Metrics Standards

### 响应时间标准

| 指标 | 优秀 | 良好 | 可接受 | 差 |
|------|------|------|--------|-----|
| P50 | < 100ms | < 200ms | < 500ms | > 500ms |
| P95 | < 200ms | < 500ms | < 1s | > 1s |
| P99 | < 500ms | < 1s | < 2s | > 2s |

### 吞吐量标准

| 系统规模 | TPS 目标 | QPS 目标 |
|----------|----------|----------|
| 小型 | > 100 | > 500 |
| 中型 | > 500 | > 2000 |
| 大型 | > 2000 | > 10000 |
| 超大型 | > 10000 | > 50000 |

### 资源利用率标准

| 资源 | 正常 | 警告 | 危险 |
|------|------|------|------|
| CPU | < 70% | 70-85% | > 85% |
| Memory | < 80% | 80-90% | > 90% |
| Disk IO | < 70% | 70-85% | > 85% |
| Network | < 50% | 50-70% | > 70% |

## Test Script Standards

### JMeter 脚本规范

```jmeter
# 测试计划结构
Test Plan
├── Thread Group (线程组)
│   ├── Number of Threads: {并发数}
│   ├── Ramp-up Period: {预热时间}
│   └── Duration: {持续时间}
├── HTTP Request Defaults
│   ├── Server: {服务器地址}
│   └── Port: {端口}
├── HTTP Cookie Manager
├── HTTP Request (Sampler)
│   ├── Method: POST/GET
│   ├── Path: {API路径}
│   └── Body: {请求体}
├── Response Assertion
├── Duration Assertion
└── View Results Tree / Summary Report
```

### Locust 脚本规范

```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def view_products(self):
        self.client.get("/api/products")
    
    @task(1)
    def create_order(self):
        self.client.post("/api/orders", json={
            "product_id": 1,
            "quantity": 1
        })
```

## Monitoring Metrics Standards

### 必监控指标

```yaml
application_metrics:
  - 响应时间 (RT)
  - 吞吐量 (TPS/QPS)
  - 错误率 (ER)
  - 并发连接数

system_metrics:
  - CPU 使用率
  - Memory 使用率
  - Disk IO
  - Network IO

database_metrics:
  - 连接池使用率
  - 查询响应时间
  - 慢查询数量
  - 事务日志

cache_metrics:
  - 命中率
  - 内存使用率
  - 驱逐数量
```

### 监控采样间隔

| 场景 | 采样间隔 | 数据保留 |
|------|----------|----------|
| 负载测试 | 5-10 秒 | 7 天 |
| 稳定性测试 | 30 秒 | 30 天 |
| 问题诊断 | 1 秒 | 24 小时 |

## Test Data Standards

### 数据准备原则

1. **真实性**: 数据分布应接近生产环境
2. **充分性**: 数据量应满足测试需要
3. **隔离性**: 测试数据与生产数据隔离
4. **可恢复性**: 测试后数据可恢复

### 数据量估算

```
数据量 = 峰值日操作量 × 测试天数 × 安全系数

安全系数:
- 短期测试 (1天): 1.2
- 中期测试 (7天): 1.1
- 长期测试 (30天): 1.05
```

## Report Templates

### Performance Test Report结构

```markdown
## 1. 测试概述

### 1.1 测试背景
### 1.2 测试范围
### 1.3 测试目标

## 2. 测试环境

### 2.1 硬件配置
### 2.2 软件版本
### 2.3 网络拓扑

## 3. 测试设计

### 3.1 测试模型
### 3.2 测试场景
### 3.3 测试数据

## 4. 测试执行

### 4.1 测试记录
### 4.2 测试结果

## 5. 性能分析

### 5.1 指标分析
### 5.2 瓶颈分析

## 6. 结论与建议

### 6.1 测试结论
### 6.2 优化建议
```

## Bottleneck Analysis Methods

### 响应时间分解

```
总响应时间 = 网络延迟 + 服务器处理 + 数据库查询 + 第三方调用

分解步骤:
1. 分析各阶段占比
2. 识别主要耗时点
3. 确定优化优先级
```

### 瓶颈定位流程

```
1. 检查应用层 (APM)
   ├── 慢接口定位
   ├── 异常堆栈分析
   └── 代码级瓶颈

2. 检查中间件
   ├── 数据库连接池
   ├── 缓存命中率
   └── 消息队列积压

3. 检查基础设施
   ├── CPU 使用率
   ├── 内存使用率
   ├── IO 等待
   └── 网络带宽
```

## Optimization Priority

| 优先级 | 优化类型 | 预期收益 | 实施难度 |
|--------|----------|----------|----------|
| P0 | 数据库优化 | 高 | 中 |
| P1 | 缓存优化 | 高 | 低 |
| P2 | 代码优化 | 中 | 高 |
| P3 | 架构优化 | 高 | 高 |
| P4 | 资源扩容 | 中 | 低 |

## Associated Assets

| 资产类型 | 文件路径 |
|----------|----------|
| Scenario | `scenarios/performance-testing/SCENARIO.md` |
| Prompt | `prompts/performance-testing.prompt.md` |
| Agent | `agents/performance-testing.agent.md` |
| Skill | `skills/performance-testing/SKILL.md` |

## Multi-Language Code Examples

### JMeter: JMX 测试计划配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- jmeter-benchmark.jmx — JMeter 性能测试计划 -->
<jmeterTestPlan version="1.2" properties="5.0">
  <hashTree>
    <!-- 测试计划元数据 -->
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="API Performance Test">
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments">
        <collectionProp name="Arguments.arguments">
          <elementProp name="BASE_URL" elementType="Argument">
            <stringProp name="Argument.name">BASE_URL</stringProp>
            <stringProp name="Argument.value">${__P(base_url,http://localhost:8080)}</stringProp>
          </elementProp>
          <elementProp name="USERS" elementType="Argument">
            <stringProp name="Argument.name">USERS</stringProp>
            <stringProp name="Argument.value">${__P(users,100)}</stringProp>
          </elementProp>
          <elementProp name="DURATION" elementType="Argument">
            <stringProp name="Argument.name">DURATION</stringProp>
            <stringProp name="Argument.value">${__P(duration,300)}</stringProp>
          </elementProp>
        </collectionProp>
      </elementProp>
    </TestPlan>
    <hashTree>

      <!-- 全局默认配置 -->
      <ConfigTestElement guiclass="HttpDefaultsGui" testclass="ConfigTestElement"
                         testname="HTTP Request Defaults">
        <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
        <stringProp name="HTTPSampler.protocol">https</stringProp>
        <stringProp name="HTTPSampler.connect_timeout">5000</stringProp>
        <stringProp name="HTTPSampler.response_timeout">30000</stringProp>
      </ConfigTestElement>
      <hashTree/>

      <!-- 用户自定义变量 -->
      <Arguments guiclass="ArgumentsPanel" testclass="Arguments"
                 testname="User Defined Variables">
        <collectionProp name="Arguments.arguments">
          <stringProp name="THINK_TIME">1000</stringProp>
          <stringProp name="AUTH_TOKEN">Bearer ${__UUID}</stringProp>
        </collectionProp>
      </Arguments>
      <hashTree/>

      <!-- 并发用户组 -->
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup"
                   testname="Load Test - ${USERS} Users">
        <intProp name="ThreadGroup.num_threads">${USERS}</intProp>
        <intProp name="ThreadGroup.ramp_time">60</intProp>
        <boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>
        <stringProp name="ThreadGroup.duration">${DURATION}</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController">
          <boolProp name="continue_forever">true</boolProp>
        </elementProp>
      </ThreadGroup>
      <hashTree>

        <!-- 定时器：模拟用户思考时间 -->
        <UniformRandomTimer guiclass="UniformRandomTimerGui"
                           testclass="UniformRandomTimer"
                           testname="Think Time">
          <stringProp name="ConstantTimer.delay">500</stringProp>
          <stringProp name="RandomTimer.range">1500</stringProp>
        </UniformRandomTimer>
        <hashTree/>

        <!-- 测试场景 1: 获取商品列表 (权重 60%) -->
        <OnceOnlyController guiclass="OnceOnlyControllerGui"
                           testclass="OnceOnlyController"
                           testname="Login - Once Only"/>
        <hashTree>
          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy"
                           testname="POST /api/auth/login">
            <stringProp name="HTTPSampler.method">POST</stringProp>
            <stringProp name="HTTPSampler.path">/api/auth/login</stringProp>
            <stringProp name="HTTPSampler.postBodyRaw">true</stringProp>
            <stringProp name="HTTPSampler.body">
              {"username":"test_user","password":"test_pass"}
            </stringProp>
          </HTTPSamplerProxy>
          <hashTree>
            <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion"
                             testname="Assert Login Success">
              <stringProp name="Assertion.test_field">response_code</stringProp>
              <stringProp name="Assertion.test_type">2</stringProp>
              <stringProp name="Assertion.assume_success">true</stringProp>
            </ResponseAssertion>
            <hashTree/>
            <!-- 提取 token 供后续请求使用 -->
            <JSONPostProcessor guiclass="JSONPostProcessorGui"
                              testclass="JSONPostProcessor"
                              testname="Extract Token">
              <stringProp name="JSONPostProcessor.referenceNames">authToken</stringProp>
              <stringProp name="JSONPostProcessor.jsonPathExpressions">$.data.token</stringProp>
            </JSONPostProcessor>
            <hashTree/>
          </hashTree>
        </hashTree>

        <!-- 加权测试场景 1: 获取商品列表 -->
        <WeightedSwitchController guiclass="WeightedSwitchControllerGui"
                                 testclass="WeightedSwitchController"
                                 testname="Weighted Scenarios">
          <stringProp name="weights">60, 30, 10</stringProp>
        </WeightedSwitchController>
        <hashTree>

          <!-- 场景 1: 查询商品 (60%) -->
          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy"
                           testname="GET /api/products">
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <stringProp name="HTTPSampler.path">/api/products?page=1&size=20</stringProp>
          </HTTPSamplerProxy>
          <hashTree>
            <DurationAssertion guiclass="DurationAssertionGui"
                              testclass="DurationAssertion"
                              testname="Response < 500ms">
              <longProp name="DurationAssertion.duration">500</longProp>
            </DurationAssertion>
            <hashTree/>
          </hashTree>

          <!-- 场景 2: 创建订单 (30%) -->
          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy"
                           testname="POST /api/orders">
            <stringProp name="HTTPSampler.method">POST</stringProp>
            <stringProp name="HTTPSampler.path">/api/orders</stringProp>
            <stringProp name="HTTPSampler.postBodyRaw">true</stringProp>
            <stringProp name="HTTPSampler.body">
              {"product_id": ${__Random(1,1000)},"quantity":1}
            </stringProp>
          </HTTPSamplerProxy>
          <hashTree>
            <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion"
                             testname="Status 201">
              <stringProp name="Assertion.test_field">response_code</stringProp>
              <stringProp name="Assertion.test_type">2</stringProp>
            </ResponseAssertion>
            <hashTree/>
          </hashTree>

          <!-- 场景 3: 搜索 (10%) -->
          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy"
                           testname="GET /api/search">
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <stringProp name="HTTPSampler.path">/api/search?q=${__RandomString(5,abcdefghijk)}</stringProp>
          </HTTPSamplerProxy>
          <hashTree/>
        </hashTree>

        <!-- 监听器：结果收集 -->
        <ResultCollector guiclass="SummaryReportGui" testclass="ResultCollector"
                        testname="Summary Report"/>
        <hashTree/>
        <ResultCollector guiclass="GraphsListenerGui" testclass="ResultCollector"
                        testname="Response Time Graph"/>
        <hashTree/>

      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```

```bash
# JMeter CLI 执行命令
jmeter -n -t jmeter-benchmark.jmx \
  -Jbase_url=https://api.company.com \
  -Jusers=200 \
  -Jduration=600 \
  -l results.jtl \
  -e -o ./report/

# 分布式压测
jmeter -n -t test-plan.jmx \
  -R slave1:1099,slave2:1099 \
  -Gbase_url=https://api.company.com \
  -l distributed-results.jtl
```

### Locust: Python 压测脚本

```python
#!/usr/bin/env python3
"""
locustfile.py — Locust 性能测试脚本
基于生产流量模型模拟多场景用户行为
"""
import random
import json
from locust import HttpUser, task, between, events
from locust.runners import MasterRunner, WorkerRunner
from locust.env import Environment
from gevent import sleep


class ApiUser(HttpUser):
    """
    模拟 API 用户行为
    wait_time 模拟真实用户的操作间隔（1-5 秒）
    """
    wait_time = between(1, 5)
    token = None
    user_id = None

    def on_start(self):
        """每个用户启动时执行一次（登录）"""
        self.login()

    def login(self):
        """用户登录获取 token"""
        resp = self.client.post("/api/auth/login", json={
            "username": f"perf_test_{random.randint(1, 10000)}",
            "password": "test_password",
        })
        if resp.status_code == 200:
            data = resp.json()
            self.token = data.get("token")
            self.user_id = data.get("user_id")
            # 设置后续请求的认证头
            self.client.headers.update({
                "Authorization": f"Bearer {self.token}"
            })

    @task(5)  # 权重 5 — 最高频率
    def browse_products(self):
        """浏览商品列表 — 最高频操作"""
        page = random.randint(1, 10)
        category = random.choice(["electronics", "clothing", "books", "home"])

        with self.client.get(
            f"/api/products?page={page}&size=20&category={category}",
            name="/api/products [browse]",
            catch_response=True,
        ) as resp:
            if resp.status_code == 200:
                try:
                    data = resp.json()
                    # 记录响应时间到自定义指标
                    if resp.elapsed.total_seconds() > 0.5:
                        resp.failure(f"Response too slow: {resp.elapsed.total_seconds():.3f}s")
                except json.JSONDecodeError:
                    resp.failure("Invalid JSON response")
            else:
                resp.failure(f"Status code: {resp.status_code}")

    @task(3)  # 权重 3
    def search_products(self):
        """搜索商品"""
        query = random.choice(["laptop", "phone", "book", "shoe", "watch"])
        with self.client.get(
            f"/api/search?q={query}&page=1",
            name="/api/search",
            catch_response=True,
        ) as resp:
            if resp.status_code != 200:
                resp.failure(f"Search failed: {resp.status_code}")

    @task(2)  # 权重 2
    def view_product_detail(self):
        """查看商品详情"""
        product_id = random.randint(1, 1000)
        with self.client.get(
            f"/api/products/{product_id}",
            name="/api/products/[id]",
            catch_response=True,
        ) as resp:
            if resp.status_code == 200:
                data = resp.json()
                # 验证响应结构完整性
                if "name" not in data or "price" not in data:
                    resp.failure("Missing required fields")

    @task(1)  # 权重 1 — 最低频率
    def create_order(self):
        """下单 — 低频高价值操作"""
        if not self.token:
            return

        order_data = {
            "items": [
                {
                    "product_id": random.randint(1, 1000),
                    "quantity": random.randint(1, 3),
                }
            ],
            "shipping_address": {
                "street": "123 Test St",
                "city": "Shanghai",
                "zip": "200000",
            },
            "payment_method": random.choice(["credit_card", "alipay", "wechat"]),
        }

        with self.client.post(
            "/api/orders",
            json=order_data,
            name="/api/orders [create]",
            catch_response=True,
        ) as resp:
            if resp.status_code == 201:
                # 验证响应包含订单 ID
                try:
                    data = resp.json()
                    if "order_id" not in data:
                        resp.failure("Missing order_id in response")
                except json.JSONDecodeError:
                    resp.failure("Invalid JSON response")
            else:
                resp.failure(f"Order creation failed: {resp.status_code}")


# ===== 自定义事件监听器 =====

@events.test_start.add_listener
def on_test_start(environment: Environment, **kwargs):
    """测试开始前执行（数据准备）"""
    print(f"[Setup] Performance test starting...")
    print(f"[Setup] Target: {environment.host}")
    print(f"[Setup] Users: {environment.runner.target_user_count}")
    print(f"[Setup] Spawn rate: {environment.runner.spawn_rate}/s")


@events.test_stop.add_listener
def on_test_stop(environment: Environment, **kwargs):
    """测试结束后执行（清理）"""
    print(f"[Teardown] Performance test completed.")
    print(f"[Teardown] Total requests: {environment.stats.total.num_requests}")
    print(f"[Teardown] Failures: {environment.stats.total.num_failures}")


@events.request.add_listener
def on_request(request_type, name, response_time, response_length,
               exception, context, **kwargs):
    """记录慢请求到单独日志"""
    SLOW_THRESHOLD_MS = 1000
    if response_time >= SLOW_THRESHOLD_MS:
        with open("slow-requests.log", "a") as f:
            f.write(f"{request_type} {name} {response_time}ms\n")
```

```bash
# Locust 压测启动命令
locust -f locustfile.py \
  --host=https://api.company.com \
  --users=500 \
  --spawn-rate=10 \
  --run-time=30m \
  --headless \
  --csv=results \
  --html=report.html \
  --logfile=locust.log

# 分布式模式（多台机器）
locust -f locustfile.py --worker --master-host=192.168.1.100
locust -f locustfile.py --master --expect-workers=4
```

### k6: JavaScript 压测脚本

```javascript
// k6-script.js — k6 性能测试脚本
import http from 'k6/http';
import { check, sleep, group } from 'k6';
import { Rate, Trend, Counter } from 'k6/metrics';

// ===== 自定义指标 =====
const errorRate = new Rate('errors');
const apiTrend = new Trend('api_duration');
const orderCounter = new Counter('orders_created');

// ===== 测试配置 =====
export const options = {
  // 多阶段负载：逐步增加并发
  stages: [
    { duration: '5m', target: 100 },   // 热身阶段
    { duration: '10m', target: 500 },  // 爬升阶段
    { duration: '15m', target: 500 },  // 稳态阶段
    { duration: '5m', target: 800 },   // 峰值阶段
    { duration: '5m', target: 0 },     // 冷却阶段
  ],
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<2000'],
    http_req_failed: ['rate<0.01'],
    errors: ['rate<0.05'],
  },
  // 模拟真实浏览器
  userAgent: 'k6-performance-test/1.0',
  // 全局标签
  tags: {
    environment: 'staging',
    test_suite: 'api-benchmark',
  },
};

// ===== 模拟数据 =====
const USER_AGENTS = [
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15',
  'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) Mobile/15E148',
];

const CATEGORIES = ['electronics', 'clothing', 'books', 'home', 'sports'];

// ===== 默认函数 =====
export default function () {
  // 随机选择 User-Agent
  http.setUserAgent(USER_AGENTS[Math.floor(Math.random() * USER_AGENTS.length)]);

  // 分组执行业务场景
  group('Browse Products', () => {
    browseProducts();
  });

  group('Search & Detail', () => {
    searchProducts();
    viewProductDetail();
  });

  group('Create Order', () => {
    if (Math.random() < 0.2) {  // 20% 概率执行下单
      createOrder();
    }
  });

  sleep(1 + Math.random() * 3);  // 模拟思考时间
}

// ===== 业务函数 =====

function browseProducts() {
  const page = Math.floor(Math.random() * 10) + 1;
  const category = CATEGORIES[Math.floor(Math.random() * CATEGORIES.length)];

  const res = http.get(
    `/api/products?page=${page}&size=20&category=${category}`,
    {
      tags: { business_flow: 'browse' },
    }
  );

  apiTrend.add(res.timings.duration);
  errorRate.add(res.status !== 200);
  check(res, {
    'products status is 200': (r) => r.status === 200,
    'products response < 500ms': (r) => r.timings.duration < 500,
    'products has body': (r) => r.body.length > 0,
  });
}

function searchProducts() {
  const query = ['laptop', 'phone', 'book', 'shoe', 'watch'][Math.floor(Math.random() * 5)];
  const res = http.get(`/api/search?q=${query}`, {
    tags: { business_flow: 'search' },
  });

  check(res, {
    'search status is 200': (r) => r.status === 200,
  });
}

function viewProductDetail() {
  const productId = Math.floor(Math.random() * 1000) + 1;
  const res = http.get(`/api/products/${productId}`, {
    tags: { business_flow: 'detail' },
  });

  check(res, {
    'detail status is 200': (r) => r.status === 200,
    'detail has product name': (r) => r.json().name !== undefined,
  });
}

function createOrder() {
  const payload = JSON.stringify({
    items: [{ product_id: Math.floor(Math.random() * 1000) + 1, quantity: 1 }],
    shipping_address: { street: '123 Test St', city: 'Shanghai', zip: '200000' },
    payment_method: 'credit_card',
  });

  const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { business_flow: 'checkout' },
  };

  const res = http.post('/api/orders', payload, params);
  orderCounter.add(1);

  check(res, {
    'order status is 201': (r) => r.status === 201,
    'order has order_id': (r) => r.json().order_id !== undefined,
  });
}

// ===== 生命周期钩子 =====
export function setup() {
  // 测试前数据准备
  console.log('Setting up test data...');
  const setupRes = http.post(`${__ENV.BASE_URL}/api/test/setup`, JSON.stringify({
    users: 1000,
    products: 5000,
  }), { headers: { 'Content-Type': 'application/json' } });
  return { setupId: setupRes.json().id };
}

export function teardown(data) {
  // 测试后清理
  console.log(`Cleaning up test data: ${data.setupId}`);
  http.del(`${__ENV.BASE_URL}/api/test/cleanup/${data.setupId}`);
}
```

```bash
# k6 执行命令
k6 run k6-script.js \
  --vus 500 \
  --duration 30m \
  --out json=results.json \
  --out csv=results.csv \
  --out influxdb=http://localhost:8086/k6 \
  -e BASE_URL=https://api.company.com

# k6 云输出（Grafana Cloud）
k6 run --out cloud k6-script.js
```

### Gatling: Scala 高性能测试

```scala
// ApiSimulation.scala — Gatling 性能测试模拟
package com.company.perftest

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._
import io.gatling.core.structure.ScenarioBuilder

import scala.concurrent.duration._
import scala.util.Random

/**
 * Gatling API 性能测试模拟
 *
 * 运行命令：
 *   mvn gatling:test -Dgatling.simulationClass=com.company.perftest.ApiSimulation
 */
class ApiSimulation extends Simulation {

  // ===== HTTP 协议配置 =====
  val httpProtocol = http
    .baseUrl("https://api.company.com")
    .acceptHeader("application/json")
    .contentTypeHeader("application/json")
    .userAgentHeader("Gatling-Performance-Test/1.0")
    .shareConnections                      // 共享连接池
    .warmUp("https://api.company.com/health")  // 预热
    .maxConnectionsPerHostLikeChrome       // 模拟 Chrome 连接行为

  // ===== 自定义 headers =====
  val authHeader = Map("Authorization" -> "Bearer ${token}")

  // ===== 辅助函数 =====
  val productIdFeeder = Iterator.continually(Map(
    "productId" -> (Random.nextInt(1000) + 1),
    "category" -> Seq("electronics", "clothing", "books")(Random.nextInt(3)),
    "searchQuery" -> Seq("laptop", "phone", "book", "shoe")(Random.nextInt(4)),
  ))

  // ===== 场景定义 =====

  /** 用户登录（前置操作） */
  val loginScenario = scenario("Login")
    .exec(
      http("POST /api/auth/login")
        .post("/api/auth/login")
        .body(StringBody("""{"username": "perf_user", "password": "test123"}"""))
        .check(
          status.is(200),
          jsonPath("$.data.token").saveAs("token"),
          jsonPath("$.data.user_id").saveAs("userId"),
        )
    )
    .exec(session => {
      println(s"User ${session("userId").as[String]} logged in")
      session
    })

  /** 浏览商品 */
  val browseProducts = exec(
    http("GET /api/products [browse]")
      .get("/api/products")
      .queryParam("page", "1")
      .queryParam("size", "20")
      .queryParam("category", "${category}")
      .headers(authHeader)
      .check(
        status.is(200),
        jsonPath("$.items[*]").count.gt(0),
        responseTimeInMillis.lte(500),
      )
  )

  /** 搜索商品 */
  val searchProducts = exec(
    http("GET /api/search")
      .get("/api/search")
      .queryParam("q", "${searchQuery}")
      .headers(authHeader)
      .check(status.is(200))
  )

  /** 查看商品详情 */
  val viewProductDetail = exec(
    http("GET /api/products/${productId}")
      .get("/api/products/${productId}")
      .headers(authHeader)
      .check(
        status.is(200),
        jsonPath("$.name").exists,
      )
  )

  /** 创建订单 */
  val createOrder = exec(
    http("POST /api/orders")
      .post("/api/orders")
      .headers(authHeader)
      .body(StringBody(
        """{"items":[{"product_id":${productId},"quantity":1}],"payment_method":"credit_card"}"""
      ))
      .check(
        status.is(201),
        jsonPath("$.order_id").exists,
      )
  )

  // ===== 用户行为场景 =====
  val userBehavior = scenario("UserBehavior")
    .feed(productIdFeeder)
    .exec(loginScenario)
    .during(30.minutes) {  // 持续 30 分钟
      randomSwitch(
        50.0 -> browseProducts,     // 50% 概率浏览
        20.0 -> searchProducts,     // 20% 概率搜索
        15.0 -> viewProductDetail,  // 15% 概率查看详情
        10.0 -> createOrder,        // 10% 概率下单
        5.0  -> pause(5, 10)       // 5% 概率休息
      )
    }

  // ===== 负载模型 =====
  setUp(
    userBehavior.inject(
      nothingFor(5.seconds),           // 初始等待
      rampUsers(50).during(30.seconds),  // 快速爬升到 50
      constantUsersPerSec(50).during(10.minutes),  // 恒定 50/s
      rampUsersPerSec(50).to(200).during(5.minutes),  // 爬升到 200/s
      constantUsersPerSec(200).during(15.minutes),  // 峰值
      rampUsersPerSec(200).to(0).during(5.minutes),  // 冷却
    ).protocols(httpProtocol)
  ).assertions(
    global.responseTime.percentile(95).lte(500),   // P95 < 500ms
    global.responseTime.percentile(99).lte(2000),  // P99 < 2s
    global.successfulRequests.percent.gte(99.5),   // 成功率 > 99.5%
  )

  // ===== 测试后处理器 =====
  after {
    println("=== Performance Test Complete ===")
    println("Check results in target/gatling/ directory")
  }
}
```

```bash
# Gatling 运行命令
mvn gatling:test \
  -Dgatling.simulationClass=com.company.perftest.ApiSimulation

# 指定参数
mvn gatling:test \
  -Dgatling.simulationClass=com.company.perftest.ApiSimulation \
  -DbaseUrl=https://api.company.com \
  -Dusers=500 \
  -Dduration=30
```

## Error Handling

### Error Scenario 1: 测试环境与生产环境差异 (P1)

**触发条件**: 性能测试结果无法反映生产环境真实表现，测试环境与生产环境存在显著差异

**处理流程**:
```
IF 测试结果无法复现生产性能特征（差异 > 30%）
THEN
  1. 对比测试环境与生产环境的配置差异：
     - 硬件配置（CPU 型号/核数、内存大小、磁盘类型）
     - 软件版本（JDK、中间件、数据库、OS）
     - 网络拓扑（延迟、带宽、有无 CDN/WAF）
     - 数据规模（生产数据量 vs 测试数据量）
  2. 检查测试数据特征：
     - 数据分布是否符合生产特征（热点数据倾斜度）
     - 数据量是否足够（建议 ≥ 生产数据的 30%）
     - 索引/分区配置是否与生产一致
  3. 调整测试环境或方法：
     - 使用生产环境的副本（如数据库脱敏副本）
     - 在非高峰时段使用生产环境子集进行测试
     - 调整测试模型匹配生产流量特征
  4. 建立环境一致性检查清单：
     - 配置对比工具自动化检查
     - 定期同步测试环境与生产环境
  5. 记录差异并提供修正因子/系数
END
```

**降级方案**: 使用生产流量的 shadow 模式（流量复制）替代独立测试环境

**升级条件**: 环境差异导致测试结论完全不可信，需要重建测试环境

### Error Scenario 2: 压测导致生产环境影响 (P0)

**触发条件**: 性能测试执行过程中影响到生产环境的正常运行（资源争抢、数据库负载飙高）

**处理流程**:
```
IF 压测过程中生产监控告警触发（错误率上升、延迟增加）
THEN
  1. 立即暂停压测：
     - 停止所有压测流量（Locust/k6/JMeter 平稳停止）
     - 通知所有相关团队
  2. 评估生产影响范围：
     - 检查错误率、延迟、吞吐量等生产指标
     - 确认受影响的功能和用户范围
     - 评估是否需要回滚或降级
  3. 隔离压测环境：
     - 确认压测与生产共享的任何基础设施（数据库、缓存、消息队列）
     - 检查压测目标是否正确（域名/IP 是否误指向生产）
     - 检查网络隔离策略（VPC、安全组、防火墙）
  4. 恢复生产环境：
     - 清理残留的测试数据
     - 恢复被压测消耗的资源（连接池重置、缓存清理）
     - 验证服务恢复
  5. 事后复盘：
     - 分析压测影响生产的根本原因
     - 更新测试环境隔离策略
     - 增加压测前的环境检查清单
END
```

**降级方案**: 将压测流切换到完全隔离的测试环境，生产环境保持最小资源运行

**升级条件**: 压测影响持续超过 10 分钟，或对用户造成可见影响

### Error Scenario 3: 结果数据偏差 (P2)

**触发条件**: 性能测试结果存在明显的数据偏差，无法得出有效结论

**处理流程**:
```
IF 测试结果偏差较大（同场景多次运行标准差 > 20%）
THEN
  1. 检查测试基础设施稳定性：
     - 压测机资源使用（CPU/内存/网络是否瓶颈）
     - 是否有其他测试或任务在同时运行
     - 网络抖动（ping 目标服务器检查延迟稳定性）
  2. 预热检查：
     - JVM: 确认 JIT 编译已完成（可通过 -XX:+PrintCompilation 验证）
     - 连接池：确认已填充到稳定状态
     - 缓存：确认缓存已预热（缓存命中率稳定）
  3. 结果异常值处理：
     - 识别并记录异常值（+/- 3σ）
     - 分析异常值原因（GC STW、网络抖动、资源争用）
     - 计算去除异常值后的统计指标
  4. 增加测试迭代次数和热身时间：
     - 建议预热时间 ≥ 5 分钟
     - 建议测试持续时间 ≥ 15 分钟
     - 至少运行 3 次取平均值
  5. 使用更稳健的统计方法：
     - 使用中位数而非平均值
     - 报告 P50/P95/P99 分位数
     - 计算置信区间（95% CI）
END
```

**降级方案**: 增加测试次数和时长，延长预热期，使用聚合报告而非单次结果

**升级条件**: 连续 5 次测试结果偏差均超过 20%，需要检查基础设施是否存在硬件问题


## Quality Standards

> Acceptance criteria and quality gates for performance-testing deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | SLO achievement rate is 99.5% or higher | Automated check |
| Standard 2 | All known bottlenecks are identified and documented | Automated check |
| Standard 3 | Test validity correlation is 95% or higher | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
