# 查询定时器详细信息（DSP MSSTIMERINFOTAIL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询定时器详细信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                          |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------|
| RUNAME | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于表示该参数用于指定RU名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：使用DSP RU查看RU名称。 |

#### 使用实例

查询定时器详细信息：

```
DSP MSSTIMERINFOTAIL:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功。

结果如下
--------
定时器ID   定时器控制块魔术字    定时器状态    定时器模式    定时器类型     定时器触发类型    定时器时长（ms）    定时器超时最大/平均值（ms）    序列号        定时器回调函数名称

0          4660                  TICKING       PERIOD        NORMAL         WORKFRAME         15000               --/--                          18            PAE_DP_DrvSndFailChkHandle
1          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufp_MemLeakCheckProc
2          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          61            ufp_MemDamageCheckProc
3          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufp_MemOverLoadCheckProc
4          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufpMbufQueCollect
5          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufLeakCheck
6          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufDamageCheckPorc
7          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufOverLoadCheck
8          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          26            ufpQueDeadCheck
9          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpQueDamageCheck
10         4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpQueOverloadCheck
11         4660                  TICKING       PERIOD        NORMAL         WORKFRAME         5000                --/--                          53            PAE_DP_FabricReassTimerHandle
12         4660                  TICKING       PERIOD        NORMAL         WORKFRAME         100                 --/--                          27            PAE_DP_OamTimerHandle
13         4660                  TICKING       PERIOD        NORMAL         CALLBACK          10                  --/--                          26            ufp_SchCpuSamping
(结果个数 = 14)
---    END
```

#### 输出结果说明

| 输出项名称           | 输出项解释                                                      |
|:----------------|:-----------------------------------------------------------|
| 定时器ID           | 用于表示定时器ID。                                                 |
| 定时器控制块魔术字       | 用于表示定时器控制块魔术字。                                             |
| 定时器状态           | 用于表示定时器状态，IDLE：空闲；CREATE：创建；TICKING：待触发；OUT：触发；DELETE：待删除。 |
| 定时器模式           | 用于表示定时器模式，ONE_SHOT：单次定时器；PERIOD：循环定时器。                     |
| 定时器类型           | 用于表示定时器类型，NORMAL：普通定时器；PRECISION：高精度定时器。                   |
| 定时器触发类型         | 用于表示定时器触发类型，CALLBACK：回调方式；WORKFRAME：work框架方式。              |
| 定时器时长（ms）       | 用于表示定时器时长，单位为毫秒。                                           |
| 定时器超时最大/平均值（ms） | 用于表示定时器超时的最大值和平均值，单位为毫秒。                                   |
| 序列号             | 用于表示定时器序列号。                                                |
| 定时器回调函数名称       | 用于表示定时器回调函数名称。                                             |