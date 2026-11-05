# 激活S6a/S6d接口固定速率流控功能

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

S6a/S6d/DRA存在过载风险时，微服务USN基于配置的流控速率阈值，控制Attach、Inter TAU/RAU、Intra TAU(GERAN/UTRAN->LTE)、Intra RAU(LTE->GERAN/UTRAN)流程首次到HSS/DRA的取鉴权集请求或位置更新请求的速率，对于超过阈值的请求，给UE返回Attach Reject或TAU/RAU Reject消息，并携带相应失败原因值。

**说明** 

适用于SGSN、MME。

## 必备事项

前提条件

请仔细阅读S6a/S6d接口固定速率流控功能特性概述。

数据

| 类别             | 参数名称                              | 取值样例   | 获取方法   | 说明                |
|:---------------|:----------------------------------|:-------|:-------|:------------------|
| SET FIXEDFC    | 固定速率流控开关（FCSWITCH）                | ON     | 全网规划   | 设置固定速率流控信息        |
| SET FIXEDFC    | 固定流控速率（FCTHD）                     | 400    | 全网规划   | 设置固定速率流控信息        |
| SET EMMPROCTRL | ULR拒绝原因值（S6a接口流控）（ULRS6AFLOWCTRL） | 10     | 全网规划   | 设置S1模式移动性管理流程控制参数 |
| SET EMMPROCTRL | AIR拒绝原因值（S6a接口流控）（AIRS6AFLOWCTRL） | 10     | 全网规划   | 设置S1模式移动性管理流程控制参数 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置因S6a接口流控而导致ULR/AIR流程失败时，下发给UE的原因值。

   ****SET EMMPROCTRL****
3. 打开固定速率流控开关，计算并设置固定流控速率。

   ****SET FIXEDFC****

   **说明** 

   固定流控速率的取值参照S6a/S6d接口固定速率流控功能实现原理页面。

## 任务示例

任务描述

升级过程中系统重启，可以预期大量到HSS的取数据操作同时发生，因此系统重启前开启S6a/S6d接口固定速率流控功能，设置打开固定速率流控开关，计算并设置固定流控速率，AIR、ULR消息按照设定的固定流控速率接入。

脚本

//设置因S6a接口流控而导致ULR/AIR流程失败时，下发给UE的原因值。

```
SET EMMPROCTRL: PROT=UPDATE_LOCATION, ULRS6AFLOWCTRL=10;
SET EMMPROCTRL: PROT=AIR,AIRS6AFLOWCTRL=10;
```

//打开固定速率流控开关，计算并设置固定流控速率为400（个/秒）。

```
SET FIXEDFC: FCSWITCH=ON, FCTHD=400;
```