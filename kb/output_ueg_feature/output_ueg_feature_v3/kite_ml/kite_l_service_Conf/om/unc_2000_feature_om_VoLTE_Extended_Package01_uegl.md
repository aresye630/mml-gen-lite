# 激活基于VoLTE的优先语音服务（适用于SGW-C/PGW-C）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

在UEG上激活基于VoLTE的优先语音服务，支持异常情况下的通话场景。

适用于SGW-C、PGW-C。

## 必备事项

前提条件

* 已经加载支持该特性的License。
* 请仔细阅读GWFD-025402 基于VoLTE的优先语音服务特性概述。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET DDNATTR** | 携带ARP（ARP） | Enable | 全网规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带ARP信元。 |
|  | ARP值（ARPVALUE） | TriDDNBearer | 本端规划 |  |
|  | 携带EBI（EBI） | Enable | 本端规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带EBI信元。 |
|  | EBI值（EBIVALUE） | TriDDNBearer | 本端规划 |  |
| **ADD CPAPN** | APN名称（APN） | ims | 已配置数据中获取 | - |
|  | Ppd功能开关（PPDSWITCH） | ENABLE | 本端规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置ARP参数。

   **SET DDNATTR**
3. 打开PPD功能开关。

   **ADD CPAPN**

## 任务示例

任务描述

激活基于VoLTE的优先语音服务。

脚本

//进入“MML命令行-UEG”窗口。

//配置ARP参数。

```
SET DDNATTR: EBI=Enable, EBIVALUE=TriDDNBearer, ARP=Enable, ARPVALUE=TriDDNBearer;
```

//打开PPD功能开关。

```
ADD CPAPN:APN="ims",PPDSWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
