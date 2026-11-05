# 激活NAS信令加密与完整性保护（适用于4G）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活NAS信令加密和完整性保护特性的操作过程。

NAS（Non-Access-Stratum）协议是UE-MME之间的协议，支持核心网和UE之间业务和信令消息的传输。

NAS信令加密和完整性保护可以对NAS信令进行加密及完整性保护，提高系统的安全性。

适用于MME

## 必备事项

前提条件

* 请仔细阅读GWFD-021505 NAS信令加密与完整性保护特性概述（适用于4G）。
* EPS网络中各网元系统及操作维护台运行正常。
* 用户在HSS中已签约EPS业务。
* UE支持Null Ciphering Algorithm、SNOW 3G、AES或ZUC加密算法。
* UE支持Null Integrity Algorithm、SNOW 3G、AES或ZUC完整性算法。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **MOD S1USRSECPARA** | 用户范围（USRRANGE） | DEFAULT（缺省） | 全网规划 | 修改用户的安全配置 |
|  | 安全策略（SECPLC） | AUTHANDPROTECTED(鉴权并保护) | 全网规划 |  |
|  | 加密算法（SUPTCIPHAGTH） | EEA0-1&EEA1-1&EEA2-1&EEA3-1 | 全网规划 |  |
|  | 完整性算法（SUPTINTAGTH） | EIA0-1&EIA1-1&EIA2-1&EIA3-1 | 全网规划 |  |
| **ADD S1ALGPRIORITY** | 算法类型(ALGTYPE) | CIPH(LTE加密算法)  INTE(LTE完整性算法) | 全网规划 | 配置算法优先级 |
|  | 加密算法(ALGCIPH) | EEA2(采用AES加密算法) | 全网规划 |  |
|  | 完整性算法(ALGINTE) | EIA2(采用AES完整性算法) | 全网规划 |  |
|  | 算法优先级(ALGPRI) | 0 | 全网规划 |  |
| SET LICENSESWITCH | License项（LICITEM） | LKV2AES02 | 本端规划 | 以使用AES算法为例，打开对应的License配置开关。 |
|  | 开关（SWITCH） | ENABLE |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开加密算法和完整性算法开关。

   **MOD S1USRSECPARA**

   * “用户范围”固定选择“DEFAULT”（缺省）
   * “安全策略”固定选择“AUTHANDPROTECTED”(鉴权并保护)
3. 配置加密算法和完整性算法的算法优先级。

   **ADD S1ALGPRIORITY**
4. 打开License配置开关。

   SET LICENSESWITCH

## 任务示例

任务描述

打开如下加密算法和完整性算法开关：AES、ZUC、空加密/空完整性算法。

设置上述加密算法和完整性算法开关的算法优先级顺序从高到低依次为：AES、ZUC、空加密/空完整性算法。

脚本

//打开加密算法和完整性算法开关。

```
MOD S1USRSECPARA: USRRANGE=DEFAULT, SECPLC=AUTHANDPROTECTED, SUPTINTAGTH=EIA0-1&EIA2-1&EIA3-1, SUPTCIPHAGTH=EEA0-1&EEA2-1&EEA3-1;
```

//设置加密算法和完整性算法的算法优先级。

```
ADD S1ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=EEA0, ALGPRI=2;
ADD S1ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=EEA2, ALGPRI=0;
ADD S1ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=EEA3, ALGPRI=1;
ADD S1ALGPRIORITY: ALGTYPE=INTE, ALGINTE=EIA0, ALGPRI=2;
ADD S1ALGPRIORITY: ALGTYPE=INTE, ALGINTE=EIA2, ALGPRI=0;
ADD S1ALGPRIORITY: ALGTYPE=INTE, ALGINTE=EIA3, ALGPRI=1;
```

//打开license配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2AES02", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
