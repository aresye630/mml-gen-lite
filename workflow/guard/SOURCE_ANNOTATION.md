# 来源标注语法（@src）

产物里的每条命令、每个关键参数都可以标注来源。**标注是可选的，但机器可解析。**

## 核心原则

```
有注释 = 有依据
无注释 = 无依据（含【待填写】占位符、凭空编的值）
```

单向可判定，不需要单独的「无依据」标记。

---

## 语法

统一格式：`@src=<类型>:<定位>[,<补充>]`

### 类型 1：`exp` — 取自现网 EXP

```mml
ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com";   // @src=exp:L1122
```

- `L<数字>` = EXP 文件的行号
- 守门可自动核验：去 EXP 第 1122 行看这个值是否真的存在

**派生自现网统计的**（值是新的，但规律来自现网）：

```mml
ADD HOST:HOSTNAME="hngd_00_h_013";   // @src=exp:derive naming=hngd_00_h_NNN,现网66条连续
```

- `derive` + 说明 = 值是新造的，但命名/格式规律来自现网实测
- 守门只能核验「前缀/格式是否存在」，不能核验具体值

### 类型 2：`doc` — 取自特性文档

```mml
ADD URR:URRNAME="hngd_00_cbb_online", USAGERPTMODE=ONLINE;   // @src=doc:F352:表2
```

- `<文档编号>:<章节>` 
- 值必须能在该文档对应章节找到

### 类型 3：`intent` — 意图明确给出

```mml
ADD FILTER:FILTERNAME="hngd_tcp80", L34PROTOCOL=TCP, SVRSTARTPORT=80;   // @src=intent:端口80,443
```

- 用 `,` 分隔具体的意图要素
- 守门可核验：意图原文里有没有这些词

### 类型 4：`plan` — 来自用户提供的数据规划表

```mml
ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=30000;   // @src=plan:域名规划#3
```

- 有规划表时，这是最强依据
- 守门无法自动核验（规划表不在系统里），但可以检查格式

### 类型 5：`infer` — 从业务逻辑推导

```mml
ADD URR:URRNAME="hngd_00_cbb_offline", URRID=2018010063;   // @src=infer F352:离线URRID=在线+10000
```

- **必须附推导规则**，不能只写 `infer`
- 守门检查：有没有 `=` 或 `:` 后面跟说明

---

## 命令级 vs 参数级

### 命令级（推荐，覆盖整条命令）

注释放在行尾：

```mml
ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=30000;   // @src=plan:域名规划#3
```

### 参数级（同一命令里参数依据不同时）

关键参数后面单独标注：

```mml
ADD HOST:HOSTNAME="hngd_00_h_001",        // @src=exp:derive naming
         DOMAINVALUE="【待填写】",         // （无注释 = 无依据）
         PRIORITY=10600;                  // @src=exp:derive priority
```

---

## 判定规则（守门用）

| 情况 | 判定 |
|---|---|
| 整行无 `@src` | ungrounded（无依据）|
| `@src=exp:L###` 且该行 EXP 确实有该值 | grounded（已核验）|
| `@src=exp:L###` 但 EXP 里找不到 | **error**（虚假依据）|
| `@src=exp:derive` 但无说明 | warning（推导无说明）|
| `@src=doc:F###:章节` | grounded-doc（文档依据，抽查）|
| `@src=plan:...` | grounded-plan（规划表，最强）|
| `@src=intent:...` | grounded-intent（意图可核验）|
| `@src=infer ...` | derived（推导，需有规则说明）|

### 严重性分级

```python
fatal（必须修）：
  · 主键参数 ungrounded 且非【待填写】→ 编造值
  · @src=exp:L### 核验失败 → 虚假依据
  · 整族 >5 条且全部 ungrounded → 空壳族

warning（可接受但记录）：
  · ungrounded 比例 > 70%
  · @src=infer 无推导说明
  · @src=exp:derive 无规律说明

pass：
  · 全部 grounded 或 ungrounded 的都是【待填写】占位符
```

---

## 完整示例

```mml
// ===== Phase 1: 主机 =====
// 依据：F352 表1 要求按域名建 HOST；命名规律取自 EXP L1122 起 66 条实测
ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=30000;   // @src=plan:域名规划#1
ADD HOST:HOSTNAME="hngd_00_h_002", DOMAINVALUE="【待填写】", PRIORITY=30001;          // @src=exp:derive naming=hngd_00_h_NNN

// ===== Phase 2: 过滤器 =====
// 依据：EXP L1230 的 HOSTNAME 模式过滤器写法
ADD FILTER:FILTERNAME="hngd_00_f_h_001", L34PROTTYPE=STRING, L34PROTOCOL=ANY,
           SVRIPMODE=HOSTNAME, HOSTNAME="hngd_00_h_001";   // @src=exp:L1230
ADD FILTER:FILTERNAME="hngd_00_f_tcp_80", L34PROTOCOL=TCP, SVRSTARTPORT=80, SVRENDPORT=80;   // @src=intent:TCP80

// ===== Phase 4: URR =====
// 依据：F352 表2 场景二（单独费率需 ADD URR）；URRID 规则见 F352
ADD URR:URRNAME="hngd_00_cbb_online", URRID="【待填写】", USAGERPTMODE=ONLINE;   // @src=doc:F352:表2
ADD URR:URRNAME="hngd_00_cbb_offline", URRID="【待填写】", USAGERPTMODE=OFFLINE; // @src=doc:F352:表2
```

---

## 为什么这么设计

### 1. 不增加负担

现有产物本来就在写自然语言注释（「依据：F329」「命名取自现网统计」），只是不规范。
加 `@src=` 前缀就能机器解析，不需要 agent 多做工作。

### 2. 「无注释 = 无依据」是单向规则

不需要维护「哪些是无依据」的清单，省一半工作量。

### 3. 可以自动核验最强的那一类

`@src=exp:L###` 是唯一能 100% 自动核验的类型——去 EXP 行号看值在不在。
这覆盖了大部分场景（命名规律、参数格式都来自现网）。

### 4. 编造会被抓

```mml
ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com";   // @src=exp:L1122
```
如果 EXP 第 1122 行没有 `video.hncatv.com` → 守门报 **虚假依据**，直接 fatal。

**agent 要么标真依据，要么不标（被判无依据），没法编。**
