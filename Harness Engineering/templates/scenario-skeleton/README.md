# 场景骨架模板 / Scenario Skeleton

> 复制到 `scenarios/{your-scenario-name}/` 开始新建场景

---

## 使用步骤

1. 重命名本目录为场景名（kebab-case）
2. 填写 `README.md` 的业务背景、输入输出、成功标准
3. 设计 `flow.yaml` 的节点与边
4. 识别依赖资产，生成 `assets.lock`
5. 在 `evaluations/` 中注册质量门禁
6. 自测运行通过后提交评审

---

## 文件清单

| 文件 | 状态 | 说明 |
| :--- | :--- | :--- |
| `README.md` | **必须填写** | 场景业务说明 |
| `flow.yaml` | **必须填写** | 编排定义 |
| `checkpoint.yaml` | 可选 | 若与全局评估不同，在此定义专属检查点 |
| `assets.lock` | **必须生成** | 依赖资产版本锁定 |
