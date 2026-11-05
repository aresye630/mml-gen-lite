# 激活缺省承载GBR保障

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

需要为WBB用户创建一个可以提供带宽保障的any to any的GBR专有承载时，需要激活缺省承载GBR保障。

**说明** 

适用于PGW-C、SMF

## 必备事项

前提条件

- 请仔细阅读GWFD-021313 缺省承载GBR保障。
- 完成激活PCC基本功能（本地PCC）。

数据

GBR带宽需合理规划，无线侧资源不足时，any to any GBR专有承载会创建失败。用户将不能使用该any to any GBR专有承载。

| 类别               | 参数名称                                               | 取值样例     | 获取方法     | 说明                                                     |
|:-----------------|:---------------------------------------------------|:---------|:---------|:-------------------------------------------------------|
| SET DFTGBRBEARER | APN名称（APN）                                         | apn-test | 已配置数据中获取 | 使用 ADD CPAPN定义的APN名称。                                  |
| SET DFTGBRBEARER | 缺省GBR承载开关（DFTGBRBEARERSW）                          | ENABLE   | 本端规划     | 部署缺省承载GBR保障功能时，必须设置为“ENABLE”。                          |
| SET DFTGBRBEARER | 缺省GBR承载QCI值（LOCQOSQCI）                             | 4        | 本端规划     | 用于设置缺省GBR承载的QCI值。                                      |
| SET DFTGBRBEARER | 缺省GBR承载ARP值（LOCQOSARP）                             | 15       | 本端规划     | 用于设置缺省GBR承载的ARP值。                                      |
| SET DFTGBRBEARER | 缺省GBR承载Pre-emption-Capability值（LOCQOSPREEMPCAP）    | DISABLE  | 本端规划     | 用于设置缺省GBR承载的抢占能力。资源限制时，是否可以抢占更低优先级别的业务占有的资源。此处以不抢占为例。  |
| SET DFTGBRBEARER | 缺省GBR承载Pre-emption-Vulnerability值（LOCQOSPREEMPVUL） | ENABLE   | 本端规划     | 用于设置缺省GBR承载的被抢占能力。资源限制时，业务是否可以被更高优先级别的业务抢占。此处以允许被抢占为例。 |
| SET DFTGBRBEARER | 缺省GBR承载UL MBR值（千比特/秒）（LOCQOSMBRUL）                 | 64       | 本端规划     | 缺省GBR承载上行方向允许的最大比特率。                                   |
| SET DFTGBRBEARER | 缺省GBR承载DL MBR值(千比特/秒)（LOCQOSMBRDL）                 | 64       | 本端规划     | 缺省GBR承载下行方向允许的最大比特率。                                   |
| SET DFTGBRBEARER | 缺省GBR承载UL GBR值（千比特/秒）（LOCQOSGBRUL）                 | 64       | 本端规划     | 缺省GBR承载上行方向允许的保障比特率。                                   |
| SET DFTGBRBEARER | 缺省GBR承载DL GBR值（千比特/秒）（LOCQOSGBRDL）                 | 64       | 本端规划     | 缺省GBR承载下行方向允许的保障比特率。                                   |
| SET DFTGBRBEARER | 缺省GBR承载去活时去活PDU会话（SESSIONTERMINSW）                 | DISABLE  | 本端规划     | 用于设置缺省GBR承载去活时是否去活PDU会话。此处以不去活PDU会话为例。                 |
| SET DFTGBRBEARER | 用户接入类型（ACCTYPE）                                    | RATNON5G | 本端规划     | 用于指定缺省GBR承载适用的用户接入类型。此处以非5G接入类型为例。                     |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置缺省GBR承载保障的相关参数。

   **SET DFTGBRBEARER**

## 任务示例

任务描述

开启指定APN的缺省承载GBR保障开关，缺省承载相关参数值详见**必备事项>数据**。

脚本

```
SET DFTGBRBEARER: APN="apn-test", DFTGBRBEARERSW=ENABLE, LOCQOSQCI=4, LOCQOSARP=15, LOCQOSPREEMPCAP=DISABLE, LOCQOSPREEMPVUL=ENABLE, LOCQOSMBRUL=64, LOCQOSMBRDL=64, LOCQOSGBRUL=64, LOCQOSGBRDL=64, SESSIONTERMINSW=DISABLE, ACCTYPE=RAT5G;
```