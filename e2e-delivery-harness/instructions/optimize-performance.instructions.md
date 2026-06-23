---
name: optimize-performance
description: "Detailed technical instructions for optimize-performance scenario execution"
applyTo: "scenarios/optimize-performance/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Instructions: 性能优化 (Optimize Performance)

## Performance Optimization Layers

### 优化层次结构

```
┌─────────────────────────────────────┐
│           架构层优化                  │
│  (异步、缓存、读写分离、分库分表)      │
├─────────────────────────────────────┤
│           服务层优化                  │
│  (连接池、线程池、并发优化)           │
├─────────────────────────────────────┤
│           数据库优化                  │
│  (索引、SQL、架构)                   │
├─────────────────────────────────────┤
│           代码层优化                  │
│  (算法、数据结构、资源管理)            │
└─────────────────────────────────────┘
```

## Code Optimization Standards

### 算法优化

| 场景 | 优化前 | 优化后 |
|------|--------|--------|
| 列表查找 | O(n) 遍历 | O(1) Map |
| 嵌套循环 | O(n²) | O(n) 单循环 |
| 重复计算 | 每次计算 | 缓存结果 |

### 并发优化

```python
# 连接池优化
pool_config = {
    "min_size": 10,
    "max_size": 100,
    "idle_timeout": 300,
    "max_lifetime": 3600
}

# 线程池优化
executor_config = {
    "core_pool_size": 10,
    "max_pool_size": 100,
    "queue_capacity": 1000,
    "keep_alive_time": 60
}
```

## Database Optimization Standards

### 索引优化

```sql
-- 覆盖索引优化
-- 创建覆盖索引
CREATE INDEX idx_user_cover ON users(id, name, email);

-- 查询使用覆盖索引
SELECT id, name, email FROM users WHERE id = ?;
```

### SQL 优化

```sql
-- 避免 SELECT *
SELECT id, name FROM users WHERE id = 1;

-- 使用 LIMIT 限制
SELECT * FROM logs WHERE created_at > ? LIMIT 100;

-- 使用 EXPLAIN 分析
EXPLAIN SELECT * FROM orders WHERE user_id = 1;
```

## Cache Optimization Standards

### 多级缓存

```yaml
cache_levels:
  l1:
    type: "本地缓存 (Caffeine/Guava)"
    capacity: "1000 items"
    ttl: "5 minutes"

  l2:
    type: "Redis 分布式缓存"
    capacity: "无限制"
    ttl: "30 minutes"

  strategy: "Cache-Aside"
```

### 缓存策略

| 策略 | 适用场景 | 实现难度 |
|------|----------|----------|
| Cache-Aside | 读多写少 | 低 |
| Write-Through | 数据一致性 | 中 |
| Write-Behind | 高写入性能 | 高 |

## Performance Monitoring Metrics

```yaml
metrics:
  latency:
    p50: "< 50ms"
    p95: "< 200ms"
    p99: "< 500ms"

  throughput:
    qps: "> 1000"

  error_rate:
    percentage: "< 0.1%"
```

## Multi-Language Code Examples

### Java: JMH 基准测试

```java
// BenchmarkService.java — JMH 微基准测试示例
package com.company.performance;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.Blackhole;
import org.openjdk.jmh.results.format.ResultFormatType;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import org.openjdk.jmh.runner.options.TimeValue;

import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

/**
 * JMH 微基准测试 — 比较不同集合操作性能
 * 
 * 运行方式：
 *   mvn clean verify
 *   java -jar target/benchmarks.jar
 */
@BenchmarkMode(Mode.Throughput)           // 吞吐量模式（ops/ms）
@OutputTimeUnit(TimeUnit.MILLISECONDS)    // 输出单位：微秒
@State(Scope.Thread)                      // 每个线程独立状态
@Fork(value = 2, warmups = 1)            // 2次正式fork，1次预热fork
@Warmup(iterations = 3, time = 2)         // 3次预热，每次2秒
@Measurement(iterations = 5, time = 5)    // 5次测量，每次5秒
public class BenchmarkService {

    private static final int DATA_SIZE = 10_000;
    private List<Integer> dataList;
    private Set<Integer> dataSet;
    private Map<Integer, String> dataMap;
    private int[] dataArray;

    @Setup(Level.Trial)
    public void setup() {
        Random random = new Random(42);
        dataList = new ArrayList<>(DATA_SIZE);
        dataSet = new HashSet<>(DATA_SIZE);
        dataMap = new HashMap<>(DATA_SIZE);
        dataArray = new int[DATA_SIZE];

        for (int i = 0; i < DATA_SIZE; i++) {
            int value = random.nextInt(DATA_SIZE * 10);
            dataList.add(value);
            dataSet.add(value);
            dataMap.put(value, "value-" + value);
            dataArray[i] = value;
        }
    }

    /** 基准：ArrayList contains 操作（O(n)） */
    @Benchmark
    @OperationsPerInvocation(DATA_SIZE)
    public boolean listContains(Blackhole bh) {
        boolean result = false;
        for (int i = 0; i < DATA_SIZE; i++) {
            result ^= dataList.contains(i);
        }
        return result;
    }

    /** 优化：HashSet contains 操作（O(1)） */
    @Benchmark
    @OperationsPerInvocation(DATA_SIZE)
    public boolean setContains(Blackhole bh) {
        boolean result = false;
        for (int i = 0; i < DATA_SIZE; i++) {
            result ^= dataSet.contains(i);
        }
        return result;
    }

    /** 基准：Stream filter + findFirst */
    @Benchmark
    public Optional<Integer> streamFilter() {
        return dataList.stream()
                .filter(x -> x > DATA_SIZE * 5)
                .findFirst();
    }

    /** 优化：传统 for 循环（更优） */
    @Benchmark
    public int forLoop() {
        for (int i = 0; i < DATA_SIZE; i++) {
            if (dataArray[i] > DATA_SIZE * 5) {
                return dataArray[i];
            }
        }
        return -1;
    }

    /** 基准：字符串拼接 */
    @Benchmark
    public String stringConcat() {
        String result = "";
        for (int i = 0; i < 100; i++) {
            result += "item-" + i + ",";  // 每次创建新 String 对象
        }
        return result;
    }

    /** 优化：StringBuilder */
    @Benchmark
    public String stringBuilder() {
        StringBuilder sb = new StringBuilder(1000);
        for (int i = 0; i < 100; i++) {
            sb.append("item-").append(i).append(",");
        }
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        Options opt = new OptionsBuilder()
                .include(BenchmarkService.class.getSimpleName())
                .result("benchmark-results.json")
                .resultFormat(ResultFormatType.JSON)
                .shouldFailOnError(true)
                .jvmArgs("-Xms2g", "-Xmx2g")
                .addProfiler("gc")        // 同时采集 GC 统计
                .addProfiler("stack")     // 采集热点栈信息
                .build();
        new Runner(opt).run();
    }
}
```

```xml
<!-- pom.xml — JMH 插件配置 -->
<project>
  <build>
    <plugins>
      <plugin>
        <groupId>org.openjdk.jmh</groupId>
        <artifactId>jmh-generator-annprocess</artifactId>
        <version>1.37</version>
      </plugin>
    </plugins>
  </build>
  <dependencies>
    <dependency>
      <groupId>org.openjdk.jmh</groupId>
      <artifactId>jmh-core</artifactId>
      <version>1.37</version>
    </dependency>
    <dependency>
      <groupId>org.openjdk.jmh</groupId>
      <artifactId>jmh-generator-annprocess</artifactId>
      <version>1.37</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

### Go: Benchmark + pprof 性能分析

```go
// internal/bench/bench.go — Go 基准测试与 pprof 集成
package bench

import (
	"fmt"
	"math/rand"
	"sort"
	"strings"
	"testing"
	"time"
)

// 基准数据
var testData = func() []int {
	data := make([]int, 10000)
	rng := rand.New(rand.NewSource(42))
	for i := range data {
		data[i] = rng.Intn(100000)
	}
	return data
}()

// 基准：冒泡排序
func BenchmarkBubbleSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		arr := make([]int, len(testData))
		copy(arr, testData)
		n := len(arr)
		for i := 0; i < n; i++ {
			for j := 0; j < n-i-1; j++ {
				if arr[j] > arr[j+1] {
					arr[j], arr[j+1] = arr[j+1], arr[j]
				}
			}
		}
	}
}

// 优化：标准库排序（O(n log n)）
func BenchmarkStdSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		arr := make([]int, len(testData))
		copy(arr, testData)
		sort.Ints(arr)
	}
}

// 基准：字符串拼接
func BenchmarkStringConcat(b *testing.B) {
	items := []string{"hello", "world", "foo", "bar", "baz"}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		var result string
		for _, s := range items {
			result += s + ","
		}
		_ = result
	}
}

// 优化：strings.Builder
func BenchmarkStringBuilder(b *testing.B) {
	items := []string{"hello", "world", "foo", "bar", "baz"}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		var sb strings.Builder
		sb.Grow(len(items) * 10)
		for _, s := range items {
			sb.WriteString(s)
			sb.WriteString(",")
		}
		_ = sb.String()
	}
}

// 基准：map 查找
func BenchmarkMapLookup(b *testing.B) {
	m := make(map[int]string, len(testData))
	for _, v := range testData {
		m[v] = fmt.Sprintf("value-%d", v)
	}
	target := testData[len(testData)/2]
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = m[target]
	}
}

// 基准：slice 线性查找（慢）
func BenchmarkSliceLookup(b *testing.B) {
	target := testData[len(testData)/2]
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, v := range testData {
			if v == target {
				break
			}
		}
	}
}
```

```bash
# Go 性能分析命令
#!/bin/bash
set -euo pipefail

echo "=== Running Benchmarks ==="
go test -bench=. -benchtime=5x -count=3 ./internal/bench/ \
  | tee benchmark-results.txt

echo "=== CPU Profiling ==="
go test -bench=. -cpuprofile=cpu.prof -memprofile=mem.prof ./internal/bench/

echo "=== Analyzing Profile ==="
go tool pprof -top -cum cpu.prof | head -30
go tool pprof -top -cum mem.prof | head -30

# 生成火焰图（需要安装 FlameGraph）
# go tool pprof -raw cpu.prof | stackcollapse-go.pl | flamegraph.pl > cpu-flame.svg

echo "=== Tracing ==="
go test -bench=. -trace=trace.out ./internal/bench/
go tool trace trace.out

echo "=== Profile Comparison ==="
# 对比优化前后的性能差异
go test -bench=. -count=10 ./old/ > old.txt
go test -bench=. -count=10 ./new/ > new.txt
benchstat old.txt new.txt
```

### Python: cProfile + line_profiler 性能分析

```python
#!/usr/bin/env python3
"""
performance_profiler.py — 多维度 Python 性能分析脚本
使用 cProfile、line_profiler、memory_profiler 分析瓶颈
"""
import cProfile
import pstats
import io
import time
import functools
from typing import Callable, Any

try:
    from line_profiler import LineProfiler
    HAS_LINE_PROFILER = True
except ImportError:
    HAS_LINE_PROFILER = False

try:
    from memory_profiler import profile as mem_profile
    HAS_MEM_PROFILER = True
except ImportError:
    HAS_MEM_PROFILER = False


def profile_cpu(output_file: str = "profile.cprof",
                sort_by: str = "cumulative",
                lines: int = 30) -> Callable:
    """cProfile 装饰器 — 函数级 CPU 分析"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            profiler = cProfile.Profile()
            try:
                result = profiler.runcall(func, *args, **kwargs)
            finally:
                profiler.dump_stats(output_file)
                # 打印分析结果
                s = io.StringIO()
                ps = pstats.Stats(profiler, stream=s).sort_stats(sort_by)
                ps.print_stats(lines)
                print(s.getvalue())
            return result
        return wrapper
    return decorator


def profile_line(func: Callable) -> Callable:
    """line_profiler 装饰器 — 逐行分析（需安装 line_profiler）"""
    if not HAS_LINE_PROFILER:
        print("WARNING: line_profiler not installed. Install with: pip install line_profiler")
        return func

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        lp = LineProfiler()
        lp_wrapper = lp(func)
        result = lp_wrapper(*args, **kwargs)
        lp.print_stats()
        return result
    return wrapper


# ===== 被分析的业务函数 =====

def process_large_dataset(data_size: int = 100000) -> list:
    """模拟大数据处理函数"""
    data = list(range(data_size))
    result = []

    # 瓶颈 1：列表操作
    for i in data:
        if i % 2 == 0:
            result.append(i ** 2)

    # 瓶颈 2：字符串操作
    strings = [f"item-{x}" for x in result[:1000]]
    merged = ""
    for s in strings:
        merged += s + ","  # 低效拼接

    # 瓶颈 3：排序
    result.sort(reverse=True)

    return result[:1000]


@profile_line
def find_duplicates(items: list) -> set:
    """查找重复项（line_profiler 逐行分析）"""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates


@profile_cpu(output_file="data_processing.prof")
def data_processing_pipeline() -> dict:
    """数据处理流水线（cProfile 分析）"""
    print("Generating dataset...")
    data = list(range(200000))
    import random
    random.shuffle(data)

    print("Processing...")
    result = process_large_dataset(len(data))

    print("Finding duplicates...")
    dupes = find_duplicates(data[:50000])

    return {
        "sample_count": len(result),
        "duplicates_found": len(dupes),
    }


if __name__ == "__main__":
    # 1. 使用 cProfile（粗粒度）
    print("=" * 60)
    print("Method 1: cProfile")
    print("=" * 60)
    data_processing_pipeline()

    # 2. 使用 line_profiler（逐行）
    if HAS_LINE_PROFILER:
        print("\n" + "=" * 60)
        print("Method 2: line_profiler")
        print("=" * 60)
        test_data = list(range(10000)) * 2
        find_duplicates(test_data)

    # 3. 使用 time.perf_counter 手动计时
    print("\n" + "=" * 60)
    print("Method 3: Manual Timing")
    print("=" * 60)
    start = time.perf_counter()
    process_large_dataset(50000)
    elapsed = time.perf_counter() - start
    print(f"process_large_dataset(50000): {elapsed:.4f}s")
```

```bash
# Python 性能分析工具链
pip install line_profiler memory_profiler py-spy

# cProfile 分析
python -m cProfile -o output.prof my_script.py
python -m pstats output.prof  # 进入交互分析模式

# line_profiler 逐行分析
kernprof -l -v my_script.py

# memory_profiler 内存分析
python -m memory_profiler my_script.py

# py-spy 采样分析（无需修改代码）
py-spy record -o profile.svg --duration 30 --pid $(pgrep -f my_script)
```

### JavaScript: Clinic.js + 0x 性能分析

```javascript
/**
 * performance-bench.js — Node.js 性能基准测试脚本
 * 使用 Clinic.js 和 0x 进行性能分析
 */
const http = require('http');
const { performance, PerformanceObserver } = require('perf_hooks');

// ===== 基准测试框架 =====
class BenchmarkRunner {
  constructor({ name, iterations = 1000, warmup = 100 }) {
    this.name = name;
    this.iterations = iterations;
    this.warmup = warmup;
    this.results = [];
  }

  /**
   * 执行基准测试
   * @param {Function} fn - 被测函数
   */
  async run(fn, ...args) {
    // 预热
    for (let i = 0; i < this.warmup; i++) {
      fn(...args);
    }

    // 正式测量
    const durations = [];
    for (let i = 0; i < this.iterations; i++) {
      const start = performance.now();
      fn(...args);
      durations.push(performance.now() - start);
    }

    // 统计分析
    durations.sort((a, b) => a - b);
    const total = durations.reduce((a, b) => a + b, 0);
    const avg = total / durations.length;
    const median = durations[Math.floor(durations.length / 2)];
    const p95 = durations[Math.floor(durations.length * 0.95)];
    const p99 = durations[Math.floor(durations.length * 0.99)];
    const min = durations[0];
    const max = durations[durations.length - 1];

    return {
      name: this.name,
      iterations: this.iterations,
      avg: avg.toFixed(3),
      median: median.toFixed(3),
      p95: p95.toFixed(3),
      p99: p99.toFixed(3),
      min: min.toFixed(3),
      max: max.toFixed(3),
    };
  }
}

// ===== 测试用例 =====

// 测试 1: 数组操作
function slowArrayLookup(arr, target) {
  return arr.filter(x => x === target).length > 0;  // 慢：创建新数组
}

function fastArrayLookup(arr, target) {
  return arr.includes(target);  // 快：短路操作
}

// 测试 2: 字符串拼接
function slowStringConcat(items) {
  let result = '';
  for (const item of items) {
    result += item + ',';  // 慢：每次创建新字符串
  }
  return result;
}

function fastStringConcat(items) {
  return items.join(',');  // 快：一次分配
}

// 测试 3: 对象 vs Map
function slowObjectOps(data) {
  // Object 动态添加属性较慢
  const obj = {};
  for (const [k, v] of data) {
    obj[k] = v;
  }
  return obj;
}

function fastMapOps(data) {
  // Map 对于频繁增删更优
  const map = new Map();
  for (const [k, v] of data) {
    map.set(k, v);
  }
  return map;
}

// ===== 主程序 =====
async function main() {
  console.log('\n=== Performance Benchmarks ===\n');

  // 准备数据
  const testArray = Array.from({ length: 10000 }, (_, i) => i);
  const testStrings = Array.from({ length: 10000 }, (_, i) => `item-${i}`);
  const testEntries = Array.from({ length: 5000 }, (_, i) => [`key-${i}`, `value-${i}`]);

  // 运行基准测试
  const runner1 = new BenchmarkRunner({ name: 'Array Lookup' });
  const result1 = await runner1.run(() => slowArrayLookup(testArray, 9999));
  console.table([result1]);

  const runner2 = new BenchmarkRunner({ name: 'Array Lookup (Optimized)' });
  const result2 = await runner2.run(() => fastArrayLookup(testArray, 9999));
  console.table([result2]);

  const runner3 = new BenchmarkRunner({ name: 'Map vs Object' });
  const result3 = await runner3.run(() => fastMapOps(testEntries));
  console.table([result3]);

  // 综合报告
  console.log('\n=== Optimization Recommendations ===');
  console.log(`- Array.includes() is faster than Array.filter().length > 0`);
  console.log(`- Array.join() is faster than string concatenation in loops`);
  console.log(`- Map is preferred for frequent key-value operations`);
}

main().catch(console.error);
```

```bash
# Node.js 性能分析工具链
npm install -g clinic 0x autocannon

# Clinic.js Doctor — 综合诊断
clinic doctor -- node app.js
# 生成 interactive HTML 报告

# Clinic.js Flame — 火焰图
clinic flame -- node app.js

# Clinic.js Bubbleprof — 异步追踪
clinic bubbleprof -- node app.js

# 0x — 轻量级火焰图
npx 0x app.js

# autocannon — HTTP 基准测试
npx autocannon -c 100 -d 30 http://localhost:3000/api/health

# Node 内置分析
node --prof app.js           # 生成 v8.log
node --prof-process v8.log   # 解析为可读报告
node --inspect-brk app.js    # Chrome DevTools 分析
```

## Error Handling

### Error Scenario 1: 优化引入功能回归 (P0)

**触发条件**: 性能优化提交（如缓存引入、并发改造、SQL 优化）导致已有功能出现行为异常

**处理流程**:
```
IF 性能优化 MR 合并后，监控或测试发现功能回归
THEN
  1. 立即评估回归严重程度：
     - 影响核心业务流程 → 立即回滚优化变更
     - 影响边缘功能 → 标记问题并修复
  2. 对比优化前后行为差异：
     - 检查缓存策略是否改变了数据一致性语义
     - 检查并发改造是否引入了竞态条件
     - 检查 SQL 优化是否返回了不同结果集
  3. 回滚有问题的优化变更：
     - git revert <optimization-commit>
     - 重新部署原版本
  4. 制定修复方案：
     - 添加集成测试覆盖被破坏的场景
     - 在测试环境中复现问题并调试
     - 重新实施优化，确保兼容性
  5. 优化实施前强制补充以下验证：
     - 功能等价性测试（原结果 vs 优化后结果）
     - 并发安全性测试（race detection）
     - 回滚演练（确保可安全回退）
END
```

**降级方案**: 保留旧版本运行，将优化拆分更小粒度分批上线

**升级条件**: 回归影响核心交易/支付/登录链路，或影响超过 5% 用户

### Error Scenario 2: 缓存策略失效 (P1)

**触发条件**: 引入缓存后出现缓存雪崩、缓存穿透、缓存击穿，导致数据库压力激增

**处理流程**:
```
IF 缓存命中率骤降（降低超过 30%）或数据库连接池打满
THEN
  1. 分析缓存失效模式：
     - 缓存雪崩：大量 key 同时过期 → 过期时间增加随机偏移（+/- TTL*20%）
     - 缓存穿透：查询不存在的数据 → 布隆过滤器 + 空值缓存
     - 缓存击穿：热点 key 过期 → 互斥锁重建 + 永不过期策略
  2. 实施应急修复：
     - 热点 key 设置永不过期 + 异步更新
     - 数据库连接池临时扩容（max 提高 50%）
     - 开启限流保护数据库
  3. 调整缓存配置：
     - TTL 增加随机偏移量（如 300s + random(60)）
     - 设置合理的 maxmemory 和淘汰策略（allkeys-lru）
     - 启用本地缓存（Caffeine）作为 L1 缓存
  4. 监控恢复后的缓存命中率和数据库负载
  5. 长期治理：添加缓存策略自动化测试
END
```

**降级方案**: 暂时绕过缓存层，直接读取数据库（需配合限流 + 降级开关）

**升级条件**: 缓存失效导致数据库连接耗尽，引发大面积服务不可用

### Error Scenario 3: 数据库连接池耗尽 (P1)

**触发条件**: 优化后数据库连接池耗尽，应用无法获取数据库连接

**处理流程**:
```
IF 应用日志出现 "Cannot acquire connection from pool" 或 "Connection is not available"
THEN
  1. 检查连接池状态：
     - HikariCP: /actuator/health 查看 active/idle/pending 连接数
     - DBCP2: 查看 JMX 指标
     - 数据库端: SHOW PROCESSLIST 查看当前连接数
  2. 分析连接泄漏源：
     - 启用连接泄漏检测：HikariCP leakDetectionThreshold=60000
     - 检查是否有未关闭的 ResultSet / Statement / Connection
     - 确认事务是否及时提交或回滚
  3. 应急恢复：
     - 临时调大连接池上限（max: 50 -> 100）
     - 缩短连接超时时间（connectionTimeout: 30000 -> 10000）
     - 重启问题服务实例释放泄漏连接
  4. 代码层面修复：
     - 确保所有数据库操作使用 try-with-resources
     - 使用连接池监控工具定期巡检
     - 添加 SQL 超时配置（statementTimeout: 30s）
  5. 设置连接池告警阈值（使用率 > 80% 告警）
END
```

**降级方案**: 临时降级非核心功能（如报表、审计日志），释放数据库连接给核心交易链路

**升级条件**: 连接池耗尽导致核心功能不可用，影响超过 30% 请求


## Quality Standards

> Acceptance criteria and quality gates for optimize-performance deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Target metric improves by 20% or more | Automated check |
| Standard 2 | No regression in non-target metrics | Automated check |
| Standard 3 | Optimization cost does not exceed resource budget | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
