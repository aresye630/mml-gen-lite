# 激活统一HTR流控功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

系统（MME）的周边网元存在过载风险时，微服务USN能够基于周边网元返回成功应答数的周期变化自动调节Attach、Inter-MME TAU、、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程的处理速率。

适用于SGSN、MME。

## 必备事项

前提条件

请仔细阅读统一HTR流控功能特性概述。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****SET UNIHTR**** | 局向流控开关（OFFICESWITCH） | ON | 全网规划 | 设置统一HTR功能 |
|  | 流控速率配置策略（INITFCTHDPLCY） | DEFAULT (系统缺省值) |  |  |
|  | 初始启控速率（INITFCTHD） | 400 |  |  |
|  | 最大流控速率（MAXFCTHD） | 800 |  |  |
|  | 流控恢复阈值（SUCCPERCENT） | 85 |  |  |
| ****SET EMMPROCTRL**** | Attach拒绝原因值（统一HTR流控）（ATTACHHTRFC） | 10 | 全网规划 | 设置S1模式移动性管理流程控制参数 |
|  | Inter TAU拒绝原因值（统一HTR流控）（INTERTAUHTRFC） | 10 |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置因开启统一HTR流控而导致Attach/Inter TAU流程失败时，下发给UE的原因值。

   ****SET EMMPROCTRL****
3. **可选：**计算初始启控速率。

   启控速率的取值参照统一HTR流程功能实现原理页面。
4. 打开局向流控开关，设置初始启控速率。

   * 如果“流控速率配置策略”为“DEFAULT（系统缺省值）”，则打开局向流控开关，不需要设置初始启控速率。

     ****SET UNIHTR****
   * 如果“流控速率配置策略”为“SPECIFIC（自定义值）”，则按照3计算的值设置“初始启控速率”。

     ****SET UNIHTR****

     当“流控速率配置策略”设置为“SPECIFIC（自定义值）”时，“最大流控速率”的配置原则为：

     + “最大流控速率”取值要大于等于“初始启控速率”取值。“最大流控速率”一般设置为“初始启控速率”的两倍。
     + 当“最大流控速率”取值等于“初始启控速率”的取值时，统一HTR局向流控效果相当于固定速率流控功能。
5. 设置初始启控速率后，系统自动调整用户接入速率，过程中用户实时判断是否需要调整初始启控速率。
   1. 判断是否需要调整初始启控速率。

      当“初始启控速率”与现网的Attach、Inter TAU/RAU请求消息接入速率需求不一致时，需要调整初始启控速率。如现网需要更短的接入时长，则提高初始启控速率。

      * 是 => 5.c
      * 否 => 5.b
   2. 观察性能指标判断是否有突发需流控的情况。

      观察性能指标15分钟后，如果S6a/S6d、S11/S4、SGs、S13/Gf接口负荷过高，DRA/HSS、SGW-C/PGW-C、MSC、DRA/EIR网元长时间拥塞，接入成功率极低为5%以下，可以适当调低接入速率；如果接入成功率保持100%，可以适当调高接入速率。

      * 是 => 5.c
      * 否 => 5.d
   3. 计算并设置初始启控速率。

      计算方法参考3。****SET UNIHTR****执行后立即生效。
   4. 系统基于设置的“初始启控速率”，自动调节Attach、Inter-MME TAU、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程首条消息的接入速率。

## 任务示例

任务描述

升级过程中系统重启，可以预期产生大量的注册请求，因此系统重启前开启统一HTR流控功能，设置打开局向流控开关，计算并设置初始启控速率和流控恢复阈值，当UE接入的请求速率首次超过启控阈值，系统自动调节Attach、Inter-MME TAU、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程的首条消息的接入速率。对于因此而被流控的请求将给UE返回Attach Reject或TAU Reject消息，并携带“10#Implicitly detached”原因值。

脚本

//开局向流控开关，计算并设置初始启控速率为400（个/秒），最大流控速率为800流控恢复阈值为85。

```
SET UNIHTR: OFFICESWITCH=ON, INITFCTHDPLCY=SPECIFIC, INITFCTHD=400, MAXFCTHD=800, SUCCPERCENT=85;
```

//被流控的请求给UE返回Attach Reject携带“10#Implicitly detached”原因值。

```
SET EMMPROCTRL: PROT=ATTACH, ATTACHROAMRST=10;
```

//被流控的请求给UE返回TAU Reject携带“10#Implicitly detached”原因值。

```
SET EMMPROCTRL: PROT=INTER_TAU, INTERTAUHTRFC=10;
```

版权所有 © 华为技术有限公司
