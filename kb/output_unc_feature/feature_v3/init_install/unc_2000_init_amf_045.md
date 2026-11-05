# N26接口配置

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

**接口介绍**

N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。

N26接口协议栈如图1所示。

**图1** N26接口协议栈

* MME的S10和AMF的N26接口地址独立场景下，需要分别完成MME的S10接口和AMF的N26接口的数据配置。
* MME的S10和AMF的N26接口地址合一场景下，如果已经完成MME的S10接口配置，则无需重复配置AMF的N26接口数据。

GTP-C版本为GTPv2。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD LOGICIP** | 逻辑IP地址类型（IPVERSION） | IPv4 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置N26接口数据  说明：  如果开启MME的S10和AMF的N26接口地址合一功能，已经完成MME的S10的接口数据配置，则无需重复配置AMF的N26接口数据。 |
|  | 逻辑IPv4地址（LOGICIPV4） | 10.2.215.24 |  |  |
|  | VPN实例名称（VPNINSTNAME） | \_public\_ |  |  |
|  | 描述（DESC） | n26 |  |  |
| **ADD GTPCLEGRP** | 组号（GROUPID） | 3 | 本端规划 |  |
|  | 描述信息（DESC） | n26 | 本端规划 |  |
| **ADD GTPCLEGRPMEM** | 组号（GROUPID） | 3 | 本端规划 |  |
|  | IP地址类型（IPTYPE） | IPv4 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 |  |
|  | IPv4地址（IPV4ADDR） | 10.2.215.24 |  |  |
|  | VPN名称（VPN） | \_public\_ |  |  |
|  | 描述信息（DESC） | n26 | 本端规划 |  |
| **ADD GTPCINTF** | 接口类型（INTFTYPE） | E\_GTPCINTF\_ITFN26 | 全网规划 |  |
|  | 组号（GROUPID） | 3 | 本端规划 |  |
| **SET AMFN26PLCY** | AMF N26接口部署方式（N26ITFMODE） | MME的S10和AMF的N26接口地址合一场景：COMBINE  MME的S10和AMF的N26接口独立场景：无需配置此命令，默认使用参数SEPARATE | 全网规划 | 仅开启MME的S10和AMF的N26接口地址合一功能场景下，配置该命令。  MME的S10和AMF的N26接口地址独立功能场景下，使用默认配置。 |
| **ADD N26MMECHAR** | RANGE（对端设备范围） | SPECIAL\_MME | 全网规划 | 增加对端MME的属性信息。 |
|  | IP地址类型（IPTYPE） | IPV4 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 |  |
|  | MME IPv4信令面地址（IPV4） | 172.16.0.6 |  |  |
|  | IPv4掩码（MASKV4） | 255.255.255.255 |  |  |
|  | MME能力（MMECAP） | NONIPPDN | 与对端协商 |  |
| **ADD NGMMSUBDATA** | 用户范围（SUBRANGE） | IMSI\_PREFIX | 本端规划 | 增加用户接入和移动性限制。 |
|  | IMSI前缀（IMSIPRE） | 12303 | 本端规划 |  |
|  | RAT限制（RATRESTRICT） | EUTRA-1 | 全网规划 |  |
|  | 网络限制（CORERESTRICT） | EPC-1 | 全网规划 |  |

## 操作步骤

* **MME的S10和AMF的N26接口地址独立场景**
  1. 进入“MML命令行-UNC”窗口。
  2. 配置N26接口的IP地址。

     ```
     ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.215.24", VPNINSTNAME="_public_", DESC="FOR N26";
     ```
  3. 配置AMF的N26接口的GTP-C本地实体组和实体组成员信息。

     ```
     ADD GTPCLEGRP: GROUPID=3, DESC="n26";
     ADD GTPCLEGRPMEM: GROUPID=3, IPTYPE=IPv4, IPV4ADDR="10.2.215.24", VPN="_public_", DESC="n26";
     ```
  4. 配置N26接口信息。

     ```
     ADD GTPCINTF: INTFTYPE=E_GTPCINTF_ITFN26, GROUPID=3;
     ```
  5. 配置支持UE在LTE与5G SA网络间互操作。

     1. 设置对端MME支持non-IP类型PDN。

        ```
        ADD N26MMECHAR: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="172.16.0.6", MASKV4="255.255.255.255", MMECAP="NONIPPDN";
        ```
     2. 设置UE接入限制。

        ```
        ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", RATRESTRICT=EUTRA-1, CORERESTRICT=EPC-1;
        ```
* **MME的S10和AMF的N26接口地址合一场景（已完成MME的S10接口配置）**
  1. 配置使用MME的S10和AMF的N26接口地址合一功能。

     ```
     SET AMFN26PLCY: N26ITFMODE=COMBINE;
     ```
  2. 配置支持UE在LTE与5G SA网络间互操作。

     1. 设置对端MME支持non-IP类型PDN。

        ```
        ADD N26MMECHAR: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="172.16.0.6", MASKV4="255.255.255.255", MMECAP="NONIPPDN";
        ```
     2. 设置UE接入限制。

        ```
        ADD NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", RATRESTRICT=EUTRA-1, CORERESTRICT=EPC-1;
        ```

版权所有 © 华为技术有限公司
