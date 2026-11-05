# 激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）

## 操作场景

在SGW-C/PGW-C上激活VoLTE紧急呼叫功能。

紧急呼叫不需要进行鉴权，建议紧急APN的地址分配方式采用本地分配或DHCP分配，本文档以本地地址分配为例。

VoLTE紧急呼叫和VoLTE普通呼叫使用不同的承载来传输，因此紧急呼叫的APN名称和相关数据需要分别规划，与普通呼叫的APN区分开。

## 必备事项

前提条件

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 完成加载License。
* 在MME、SGW-C、PGW-C、MSC、eNodeB等网元上完成VoLTE基本业务的数据配置。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CPVPNINST** | VPN实例名（VPNINSTANCE） | vpn1 | 本端规划 | 配置APN所属的VPN实例。 |
| **ADD CPAPN** | APN名称（APN） | sos | 全网规划 | 使能紧急呼叫功能。 |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 |  |
|  | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 |  |
|  | 支持紧急呼叫（EMERGENCYSWITCH） | ENABLE | 本端规划 |  |
| **SET APNPCCFUNC** | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 使能紧急APN的PCC功能。 |
|  | 漫游用户PCC功能（ROAMPCCSWITCH） | INHERIT | 本端规划 |  |
|  | 拜访用户PCC功能（VISITPCCSWITCH） | INHERIT | 本端规划 |  |
| **ADD CPADDRPOOL** | 地址池名称（POOLNAME） | pool-op | 全网规划 | 添加本地地址池。 |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 |  |
|  | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 |  |
| **SET APNIDLETIME** | 承载定时器(min)(BEARERTIMER) | 60 | 本端规划 | 配置紧急呼叫结束后释放缺省承载。  对于“BEARERTIMER”时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开License配置开关。

   **SET LICENSESWITCH**
3. 配置APN参数。
   1. 配置APN所属的VPN实例。
   2. 创建APN实例，使能紧急呼叫功能。

      **ADD CPAPN**

      若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
   3. 使能APN的PCC功能。

      **SET APNPCCFUNC**
4. 配置紧急呼叫结束后释放缺省承载。

   **SET APNIDLETIME**

   紧急呼叫缺省承载创建以后，除非用户关机，否则缺省承载不会被删除。这样系统资源会被一直占用，为了回收系统资源，需要配置**SET APNIDLETIME**命令来释放缺省承载，考虑到可能会有回呼的场景，“BEARERTIMER”的时间不能设置为0，建议保持缺省值60分钟。

## 任务示例

任务描述

配置VoLTE用户的紧急呼叫功能，其中紧急APN为“sos”。

脚本

1. 打开本特性的License配置开关。

   ```
   SET LICENSESWITCH:LICITEM="LKV3W9ECAL11",SWITCH=ENABLE;
   ```
2. 使能紧急呼叫功能。

   //配置APN所属的VPN实例。

   ```
   ADD CPVPNINST:VPNINSTANCE="vpn1";
   ```

   //创建APN实例，使能紧急呼叫功能。

   ```
   ADD CPAPN:APN="sos",HASVPN=ENABLE,VPNINSTANCE="vpn1",EMERGENCYSWITCH=ENABLE;
   ```

   //使能APN的PCC功能。

   ```
   SET APNPCCFUNC:APN="sos",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;
   ```
3. 配置紧急呼叫结束后释放缺省承载。

   ```
   SET APNIDLETIME: APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60;
   ```

版权所有 © 华为技术有限公司
