# 激活VoLTE基础语音业务（适用于MME）

## 操作场景

本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程，包括开通VoLTE业务和配置VoLTE寻呼重发优化数据。

## 必备事项

前提条件

* 请仔细阅读GWFD-025401 VoLTE基础语音业务特性概述
* 本特性受License控制，请先完成加载License。

数据

| 命令 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET IMSVOPS** | MME侧全部支持PS域IMS语音（MMEHOMO） | SUPPORT | 全网规划 | 配置系统支持VoLTE语音业务。 |
| **SET S1SMPROCTRL** | 流程类型（PROT） | * “DEDICATED\_BEARER\_ACT\_PROC(专有承载建立流程)” * “BEARER\_MODIFICATION\_PROC(承载修改流程)” | 全网规划 | 当网络中SGW-C/SGW-U/PGW-C/PGW-U支持Create Bearer Request与Modify Bearer Request冲突处理时，配置本命令可以提高语音呼叫建立成功率。 |
|  | CBR冲突处理模式（CBRCONFLICTMODE） | BUFFER(缓存) | 全网规划 |  |
| **SET EMM** | 高优先级业务的T3413(s)（HPT3413） | 2 | 全网规划 | 配置VoLTE寻呼优化参数。配置后这些参数的优先级会高于**SET EMM**中的普通寻呼参数“T3413(s)”、“N3413(times)”和“重寻呼间隔递增值(s) ”。 |
|  | 高优先级业务的N3413(times)（HPN3413） | 4 | 全网规划 |  |
|  | 高优先级业务的重寻呼间隔递增值(s)（HPPAGINGDELTA） | 0 | 全网规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置到PGW-C的解析数据。（如果已配置可跳过）

   **ADD IPV4DNSH**
3. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
4. 配置系统支持VoLTE语音业务。

   **SET IMSVOPS**
5. **可选：**配置Create Bearer Request与Update Bearer Request的冲突处理模式为“缓存”。

   **SET S1SMPROCTRL**
6. 配置寻呼优化参数。

   **SET EMM**

## 任务示例

任务描述

部署VoLTE基础语音业务。

脚本

//进入“MML命令行-UEG”窗口。

//配置到PGW-C的解析数据。

```
ADD IPV4DNSH: HSINDEX=1, HOSTNAME="TOPON.PGW2.4003.SLOT5.MNC001.MCC308.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.33", PRIORITY1=127, WEIGHT1=127;
ADD DNSN: FQDN="IMS.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=PGW, INTYPE=S5, PRIORITY=1, WEIGHT=1;
```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2VOLTE01", SWITCH=ENABLE;
```

//配置系统支持VoLTE语音业务。

```
SET IMSVOPS: MMEHOMO=SUPPORT;
```

//（可选）当网络中SGW-C/SGW-U/PGW-C/PGW-U支持Create Bearer Request与Modify Bearer Request冲突处理时，配置本数据可以提升语音呼叫建立的成功率。

```
SET S1SMPROCTRL: PROT=DEDICATED_BEARER_ACT_PROC, CBRCONFLICTMODE=BUFFER;
SET S1SMPROCTRL: PROT=BEARER_MODIFICATION_PROC, UBRCONFLICTMODE=BUFFER;
```

//配置VoLTE寻呼优化参数。

```
SET EMM: HPT3413=2, HPN3413=4, HPPAGINGDELTA=0;
```

版权所有 © 华为技术有限公司
