# 激活L2TP VPN

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

利用本地配置部署L2TP组网，在UEG上配置指定APN下是否使能L2TP功能。

适用于PGW-C、SMF

## 必备事项

前提条件

请仔细阅读GWFD-023002 L2TP VPN特性概述。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET APNL2TPCTRL** | APN名称（APN） | huawei.com | 已配置数据中获取 | 已通过命令 ****ADD CPAPN****配置。 |
|  | 支持L2TP功能（L2TPSWITCH） | ENABLE | 本端规划 | - |
| **SET PFCPPVTEXT** | FEATURE（特性名称） | ENABLE | 本端规划 | - |
| **ADD UPCMPT** | L2TP隧道信息（L2TPTNL） | INHERIT | 全网规划 | - |
|  | L2TP用户PCO信息（L2TPPCO） | INHERIT | 全网规划 | - |
| **SET L2TPKEY** | 加密开关（ENSWITCH） | DISABLE | 全网规划 | 加密开关在默认情况下设置为DISABLE，即明文携带L2TP私有信元，存在一定安全风险，建议和对端UPF同时开启加密功能。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置APN L2TP配置。

   **SET APNL2TPCTRL**
3. (可选) 打开L2TP业务加密开关，增强N4接口传输安全。

   **SET L2TPKEY**

   对端UPF需要同时打开该功能，并且配置相同密钥，否则会导致L2TP业务失败。

## 任务示例

任务描述

配置APN为huawei.com下使能L2TP功能。

脚本

//设置APN L2TP配置。

```
SET APNL2TPCTRL: APN="huawei.com", L2TPSWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
