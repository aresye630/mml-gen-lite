# 配置S11-C/S5-C接口数据

## 操作场景

**接口介绍**

* S11接口

  S11接口是MME与SGW-C间的信令面接口，主要用于MME和SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于SGW-C通知MME寻呼UE，恢复S1承载。S11接口协议栈如图1所示。

  **图1** S11接口协议栈
* S5接口

  S5接口可以作为SGW-C与PGW-C间的信令面接口，主要用于传递承载创建、更新及删除消息。对应的信令面接口协议栈如图2、图3所示。

  **图2** PGW-C与S-GW/SGW-C间基于GTPv2协议的S5信令面接口协议栈

  **图3** SGW-C与PGW-C间基于GTPv2协议的S5信令面接口协议栈

S11接口和S5接口都是基于GTP-C协议，采用GTPv2协议。

GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

园区双DC组网场景下，对于S11-C接口，SGW-C需要和本DC以及对端DC内的MME全互联对接。对于S5-C接口，由于SGW-C和PGW-C的微服务是融合的，因此仅需要在本DC内互通即可，不做跨DC的全互联。

**配置建议**

* S11-C接口与S5-C接口不共用业务IP地址。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成组网路由配置。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| **ADD LOGICIP** | 逻辑IP地址类型（IPVERSION） | IPV4 |  | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置S11-C/S5-C接口数据。 |
|  | 逻辑IPv4地址（LOGICIPV4） | 10.2.215.26  10.2.215.22  10.2.215.21 | 10.2.215.27  10.2.215.24  10.2.215.23 |  | 分别规划配置S11-C、S5-S-C、S5-P-C的接口。  S11-C接口与S5-C接口不共用业务IP地址。 |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  | UEG风筝形态内部接口组网时，使用园区统一规划的VPN。 |
|  | 描述（DESC） | s11  s5\_s  s5\_p |  |  | - |
| **ADD GTPCLEGRP** | 组号（GROUPID） | 0  1  2 |  | 本端规划 | - |
|  | 描述信息（DESC） | s11  s5\_s  s5\_p |  | 本端规划 |  |
| **ADD GTPCLEGRPMEM** | 组号（GROUPID） | 0  1  2 |  | 本端规划 | - |
|  | IP地址类型（IPTYPE） | IPv4 |  | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 |  |
|  | IPv4地址（IPV4ADDR） | 10.2.215.26  10.2.215.22  10.2.215.21 | 10.2.215.27  10.2.215.24  10.2.215.23 |  |  |
|  | VPN名称（VPN） | VPN\_CN |  |  |  |
|  | 描述信息（DESC） | s11  s5\_s  s5\_p |  | 本端规划 |  |
| **ADD GTPCINTF** | 接口类型（INTFTYPE） | E\_GTPCINTF\_ITFS11  E\_GTPCINTF\_ITFS5\_S  S5\_P\_OR\_GN |  | 全网规划 | - |
|  | 组号（GROUPID） | 0  1  2 |  | 本端规划 |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置S11-C/S5-C接口的逻辑IP地址。

   ```
   //DC1
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.26", VPNINSTNAME="VPN_CN", DESC="s11";
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.22", VPNINSTNAME="VPN_CN", DESC="s5_s";
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.21", VPNINSTNAME="VPN_CN", DESC="s5_p";
   //DC2
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.27", VPNINSTNAME="VPN_CN", DESC="s11";
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.23", VPNINSTNAME="VPN_CN", DESC="s5_s";
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.22", VPNINSTNAME="VPN_CN", DESC="s5_p";
   ```
3. 配置S11-C/S5-C接口的GTP-C本地实体组和实体组成员信息。

   ```
   //DC1
   ADD GTPCLEGRP:GROUPID=0, DESC="s11";
   ADD GTPCLEGRP:GROUPID=1, DESC="s5_s";
   ADD GTPCLEGRP:GROUPID=2, DESC="s5_p";
   ADD GTPCLEGRPMEM:GROUPID=0, IPTYPE=IPv4, IPV4ADDR="10.2.215.26", VPN="VPN_CN", DESC="s11";
   ADD GTPCLEGRPMEM:GROUPID=1, IPTYPE=IPv4, IPV4ADDR="10.2.215.22", VPN="VPN_CN", DESC="s5_s";
   ADD GTPCLEGRPMEM:GROUPID=2, IPTYPE=IPv4, IPV4ADDR="10.2.215.21", VPN="VPN_CN", DESC="s5_p";
   //DC2
   ADD GTPCLEGRP:GROUPID=0, DESC="s11";
   ADD GTPCLEGRP:GROUPID=1, DESC="s5_s";
   ADD GTPCLEGRP:GROUPID=2, DESC="s5_p";
   ADD GTPCLEGRPMEM:GROUPID=0, IPTYPE=IPv4, IPV4ADDR="10.2.215.27", VPN="VPN_CN", DESC="s11";
   ADD GTPCLEGRPMEM:GROUPID=1, IPTYPE=IPv4, IPV4ADDR="10.2.215.23", VPN="VPN_CN", DESC="s5_s";
   ADD GTPCLEGRPMEM:GROUPID=2, IPTYPE=IPv4, IPV4ADDR="10.2.215.22", VPN="VPN_CN", DESC="s5_p";
   ```
4. 配置S11-C/S5-C接口信息。

   ```
   //DC1
   ADD GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS11, GROUPID=0;
   ADD GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS5_S, GROUPID=1;
   ADD GTPCINTF:INTFTYPE=S5_P_OR_GN, GROUPID=2;
   //DC2
   ADD GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS11, GROUPID=0;
   ADD GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS5_S, GROUPID=1;
   ADD GTPCINTF:INTFTYPE=S5_P_OR_GN, GROUPID=2;
   ```

## 验证方法

1. 检查GTPC GTP路径对端是否可达。

   进入“MML命令行-UEG”窗口。

   **TST** **GTPCPATHINFO**

   * **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATHINFO: OPTYPE=OP_Tst_GtpcPath, GTPVER=GTPv2,IPTYPE=IPTypeV4, LOCALIPV4="10.2.215.26", PEERIPV4="192.168.14.20";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     -------------------------  
        GTP版本  =  GTPv1 
     IP地址类型  =  IPV4类型  
     本端IPv4地址  =  10.2.215.26  
     对端IPv4地址  =  192.168.14.20    
     (结果数目 = 1) 

      ---    END
     ```
   * **异常结果：**对端不可达。

版权所有 © 华为技术有限公司
