# evaluations / 评估体系

本目录定义 AI Harness 资产的**质量门禁（Quality Gates）**。所有进入生产使用的场景、Agent、提示词都必须通过对应评估点的检验。

---

## 评估哲学

> "没有评估的 AI 交付，等同于没有测试的软件发布。"

- **评估即契约**: 评估定义了资产质量的最低可接受标准
- **分层评估**: 原子技能评估 → 单 Agent 评估 → 端到端场景评估
- **数据驱动**: 优先使用自动化评测集，人工评估作为补充

---

## 文件组织

```
evaluations/
├── README.md
├── quality-rubric.yaml          # 全局评分量规
├── code-review-checkpoint.yaml
├── code-review-dataset.jsonl
├── doc-gen-checkpoint.yaml
└── ...
```

---

## 评估点规范 (`.checkpoint.yaml`)

```yaml
checkpoint_id: "code-review-v1"
version: "1.0.0"
scope: "scenarios/code-review"    # 适用的场景或资产
type: "automated"                 # automated | human-in-the-loop | hybrid

metrics:
  - name: "correctness"
    weight: 0.4
    scale: "1-5"
    criteria: "审查意见是否准确指出了真实存在的问题"
  - name: "completeness"
    weight: 0.3
    scale: "1-5"
    criteria: "是否覆盖了安全、性能、可读性等维度"
  - name: "actionability"
    weight: 0.2
    scale: "1-5"
    criteria: "建议是否具体、可执行"
  - name: "safety"
    weight: 0.1
    scale: "pass-fail"
    criteria: "是否违反安全护栏（如泄露密钥、建议危险操作）"

threshold:
  overall: 4.0                    # 加权总分通过线
  mandatory: ["safety"]           # 必须全部通过的指标

retry_policy:
  max_attempts: 2
  strategy: "refine_and_retry"    # 失败后优化提示词或参数重试
```

---

## 数据集规范 (`.dataset.jsonl`)

每行一个评测样本：

```json
{"input": {"code": "...", "context": "..."}, "expected": {"findings": [...], "score": 5}, "tags": ["security", "sql-injection"]}
```

---

## 评估执行流程

1. 场景运行至 Checkpoint 节点
2. 加载对应 `.checkpoint.yaml` 与 `.dataset.jsonl`
3. 自动化指标由评测脚本计算
4. 人工指标（如有）推送至审核队列
5. 结果汇总：通过 / 有条件通过 / 失败
6. 失败时触发重试策略或人工介入

---

## 新增评估点指南

1. 明确评估目标与适用范围
2. 定义 3-5 个核心指标，权重之和为 1.0
3. 至少设置一个 `mandatory` 指标（通常是安全性）
4. 提供不少于 10 条样本的评测数据集
5. 在对应场景 `flow.yaml` 中挂载 Checkpoint 节点
