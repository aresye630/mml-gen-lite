# 配置N26接口数据

## 操作场景

**接口介绍**

N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。

N26接口协议栈如图1所示。

**图1** N26接口协议栈

GTP-C版本为GTPv2。

MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。

* 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。
* 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

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
| **ADD LOGICIP** | 逻辑IP地址类型（IPVERSION） | IPV4 |  | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置N26接口数据。 |
|  | 逻辑IPv4地址（LOGICIPV4） | 10.2.215.23 | 10.2.215.24 |  | - |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  | UEG风筝形态内部接口组网时，使用园区统一规划的VPN。 |
|  | 描述（DESC） | n26 |  |  | - |
| **ADD GTPCLEGRP** | 组号（GROUPID） | 3 |  | 本端规划 | - |
|  | 描述信息（DESC） | n26 |  | 本端规划 |  |
| **ADD GTPCLEGRPMEM** | 组号（GROUPID） | 3 |  | 本端规划 |  |
|  | IP地址类型（IPTYPE） | IPv4 | IPv4 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 |  |
|  | IPv4地址（IPV4ADDR） | 10.2.215.23 | 10.2.215.24 |  |  |
|  | VPN名称（VPN） | VPN\_CN |  |  |  |
|  | 描述信息（DESC） | n26 |  | 本端规划 |  |
| **ADD GTPCINTF** | 接口类型（INTFTYPE） | E\_GTPCINTF\_ITFN26 |  | 全网规划 |  |
|  | 组号（GROUPID） | 3 |  | 本端规划 |  |
| **SET AMFN26PLCY** | AMF N26接口部署方式（N26ITFMODE） | SEPARATE |  | 本端规划 | - |
|  | 是否支持UAM内部互操作（INTRAIWK） | YES |  | 本端规划 |  |
|  | UAM内切换识别模式（INTRAHOQRYMODE） | DNS\_QUERY |  | 本端规划 |  |
| **SET NGDNS** | DNS解析方式（ANALYSETYPE） | HOSTFILE\_SERVER |  | 全网规划 | 配置AMF选择MME参数。  如果没有DNS Server，DNS查询时优先使用本地配置数据，包含：   * 在4G到5G的移动注册更新流程中AMF根据GUMMEI找MME的时候的DNSN记录。 * 在Inter Handover流程中AMF根据eNodeB的TAC值选择MME使用的DNSN记录。 |
|  | N26接口本网IP地址选择策略（IPPLCY） | IPV4 |  | 全网规划 |  |
|  | 优选融合MME开关（MMESWITCH） | MME\_ON |  | 全网规划 |  |
| **ADD NGIPV4DNSH** | 主机名索引（HSINDEX） | 7 | 8 | 全网规划 | - |
|  | 主机名（HOSTNAME） | topon.mme-s10.mmec01.  mmegi8001.mme.epc.mnc003.  mcc123.3gppnetwork.org | topon.mme-s10.mmec02.  mmegi8001.mme.epc.mnc003.  mcc123.3gppnetwork.org | 全网规划 |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  | 全网规划 |  |
|  | IPv4地址1（IPV4ADDR1） | 10.10.10.1 | 10.10.10.3 | 全网规划 |  |
| **ADD NGDNSN** | FQDN（FQDN） | tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org | tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org | 全网规划 | - |
|  | 主机名索引（HSINDEX） | 7 | 8 | 已配置数据中获取 | 该参数需已通过ADD NGIPV4DNSH命令完成配置。 |
|  | 网元类型（ENTITY） | MME |  | 全网规划 | - |
|  | 接口类型（INTYPE） | N26 |  | 全网规划 | - |
| **ADD N26MMECHAR** | RANGE（对端设备范围） | SPECIAL\_MME |  | 全网规划 | 增加对端MME的属性信息。 |
|  | IP地址类型（IPTYPE） | IPV4 |  | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 |  |
|  | MME IPv4信令面地址（IPV4） | 172.16.0.5 | 172.16.0.6 |  |  |
|  | IPv4掩码（MASKV4） | 255.255.255.255 |  |  |  |
|  | MME能力（MMECAP） | NONIPPDN |  | 与对端协商 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. **可选：**配置GTP数据配置N26接口的IP地址。

   ```
   //DC1
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.154.23", VPNINSTNAME="VPN_CN", DESC="FOR N26";
   //DC2
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.2.154.24", VPNINSTNAME="VPN_CN", DESC="FOR N26";
   ```
3. **可选：**配置GTP数据。
   1. 配置AMF的N26接口的GTP-C本地实体组和实体组成员信息。

      ```
      //DC1
      ADD GTPCLEGRP: GROUPID=3, DESC="n26";
      ADD GTPCLEGRPMEM: GROUPID=3, IPTYPE=IPv4, IPV4ADDR="10.2.154.23", VPN="VPN_CN", DESC="n26";
      //DC2
      ADD GTPCLEGRP: GROUPID=3, DESC="n26";
      ADD GTPCLEGRPMEM: GROUPID=3, IPTYPE=IPv4, IPV4ADDR="10.2.154.24", VPN="VPN_CN", DESC="n26";
      ```
   2. 配置N26 GTPC接口信息，通过组号的关联，用于组网规划不同接口。

      ```
      //DC1
      ADD GTPCINTF: INTFTYPE=E_GTPCINTF_ITFN26, GROUPID=3;
      //DC2
      ADD GTPCINTF: INTFTYPE=E_GTPCINTF_ITFN26, GROUPID=3;
      ```
4. 配置MME选择参数。

   ```
   //DC1
   //（可选）本地Hostfile配置MME解析数据 
   SET NGDNS: ANALYSETYPE=HOSTFILE_SERVER, IPPLCY=IPV4, MMESWITCH=MME_ON; 
   //配置AMF的DNS Client数据,用于寻址MME。 
   ADD NGIPV4DNSH: HSINDEX=7, HOSTNAME="topon.mme-s10.mmec01.mmegi8001.mme.epc.mnc003.mcc123.3gppnetwork.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.1";  
   ADD NGDNSN: FQDN="tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org", HSINDEX=7, ENTITY=MME, INTYPE=N26;  
   //DC2
   //（可选）本地Hostfile配置MME解析数据 
   SET NGDNS: ANALYSETYPE=HOSTFILE_SERVER, IPPLCY=IPV4, MMESWITCH=MME_ON; 
   //配置AMF的DNS Client数据,用于寻址MME。 
   ADD NGIPV4DNSH: HSINDEX=8, HOSTNAME="topon.mme-s10.mmec02.mmegi8001.mme.epc.mnc003.mcc123.3gppnetwork.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.3";  
   ADD NGDNSN: FQDN="tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org", HSINDEX=8, ENTITY=MME, INTYPE=N26;
   ```
5. 配置支持UE在LTE与5G SA网络间互操作。

   ```
   //DC1
   ADD N26MMECHAR: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="172.16.0.5", MASKV4="255.255.255.255", MMECAP="NONIPPDN";
   //DC2
   ADD N26MMECHAR: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="172.16.0.6", MASKV4="255.255.255.255", MMECAP="NONIPPDN";
   ```

## 验证方法

1. 检查GTPC GTP路径对端是否可达。

   进入“MML命令行-UEG”窗口。

   **TST UAMGTPCPATH**

   * **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST UAMGTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="10.2.154.24", PEERIPV4ADDR="192.168.140.17";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     -------------------------  
          GTP版本  =  GTPv1 
     本端IPv4地址  =  10.2.154.24 
     本端IPv6地址  =  :: 
     对端IPv4地址  =  192.168.140.17   
     对端IPv6地址  =  :: 
         网元类型  =  AMF
     (结果数目 = 1) 

      ---    END
     ```
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
2. 进行业务测试。

   * 进行业务测试前，需要首先完成AMF与gNodeB、UDM的链路配置。
   * 进行业务测试时，需要保证MME与AMF之间互通。
   * 进行业务测试的手机必须是在对接的UDM开户的手机。

   1. **创建用户跟踪任务**。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. **可选：**

      **创建GTPC协议接口跟踪（N26）**。

      参数选择如下：
      * IP地址类型：填入跟踪的IP类型。
      * 本端IPv4/6地址：填本端IP地址。
      * 对端IPv4/6地址：填对端MME的IP。
      * 其它参数：选择默认值。
   3. 用户开机在4G网络附着，然后进行LTE到5G网络的切换以触发Handover流程。
   4. 查看用户跟踪结果。

      * **预期结果：**用户切换成功，可以在Forward Relocation Request消息中的Target ID信元携带gNodeB ID。

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**观察不到Forward Relocation Request消息中的Target ID信元携带gNodeB ID，或观察到AMF与MME之间的消息异常。

版权所有 © 华为技术有限公司
