# 配置S11-C接口数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增SGW-C或MME时，在配置完成MME到SGW-C的路由数据后，可通过配置S11接口数据建立MME到SGW-C的逻辑连接。

S11-C接口是MME与S-GW/SGW-C间的信令面接口，主要用于MME和S-GW/SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于S-GW/SGW-C通知MME寻呼UE，恢复S1承载。

S11-C接口协议栈如图1所示。

**图1** S11-C接口协议栈

GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。GTP-C版本为GTPv2。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

双DC组网场景下，MME不仅需要和本DC内的SGW-C对接，也需要和另外一个DC的SGW-C对接。这样当用户业务接入时，MME会以负荷分担的方式选择其中一个DC的SGW-C进行业务，当其中一个DC故障时，另一个DC的SGW-C会承担园区内所有用户的业务。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- 已完成组网路由配置。
- 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
- 如需在UE在4G网络附着选择合一SGW-C/PGW-C，则需要开通“S-GW/P-GW 拓扑选择”特性，即加载对应的License项“82205919 LKV2SELGW03 S-GW/P-GW 拓扑选择”。
- 已经获取网设LLD文档。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                          | DC1取值样例                                                                                                           | DC2取值样例                                                                                                           | 获取方法            | 说明                                                                                                                                                                           |
|:--------------|:------------------------------|:------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）               | IPv4                                                                                                              | IPv4                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                    |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）         | 192.168.140.17                                                                                                    | 192.168.140.18                                                                                                    | 参见“水平网设LLD文档 ”。 | -                                                                                                                                                                            |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）          | VPN_CN                                                                                                            | VPN_CN                                                                                                            | 参见“水平网设LLD文档 ”。 | UEG风筝形态内部接口组网时，使用园区统一规划的VPN。                                                                                                                                                 |
| ADD GTPCLE    | 组号（GROUPID）                   | 0                                                                                                                 | 0                                                                                                                 | 参见“水平网设LLD文档 ”。 | 配置本端的S11-C接口的GTP-C IP。 GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。                                                                                                                       |
| ADD GTPCLE    | IP地址类型（IPTYPE）                | TPTADDR_TYPE_IPV4                                                                                                 | TPTADDR_TYPE_IPV4                                                                                                 | 参见“水平网设LLD文档 ”。 | 配置本端的S11-C接口的GTP-C IP。 GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。                                                                                                                       |
| ADD GTPCLE    | IPv4地址（leIpv4）                | 192.168.140.17                                                                                                    | 192.168.140.18                                                                                                    | 参见“水平网设LLD文档 ”。 | 配置本端的S11-C接口的GTP-C IP。 GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。                                                                                                                       |
| ADD GTPCLE    | VPN名称（vpnName）                | VPN_CN                                                                                                            | VPN_CN                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置本端的S11-C接口的GTP-C IP。 GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。                                                                                                                       |
| SET UGTP      | 空闲计数器扫描间隔（秒）（ICI）             | 180                                                                                                               | 180                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                 |
| SET UGTP      | SM信令路径空闲计数器（SSI）              | 60                                                                                                                | 60                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                 |
| SET UGTP      | MM信令路径空闲计数器（MSI）              | 60                                                                                                                | 60                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                 |
| SET UGTP      | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60                                                                                                                | 60                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                 |
| ADD IPV4DNSH  | 主机名索引（HSINDEX）                | 1 2                                                                                                               | 1 2                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH  | 主机名（HOSTNAME）                 | topon.eth1.gw32.nodes topon.eth2.gw32.nodes                                                                       | topon.eth1.gw32.nodes topon.eth2.gw32.nodes                                                                       | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH  | IPV4地址1（IPV4ADDR1）            | 10.2.215.26 10.2.215.27                                                                                           | 10.2.215.26 10.2.215.27                                                                                           | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH  | 主机地址段号（ADDRSECTION）           | SECTION1(1)                                                                                                       | SECTION1(1)                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 全称标准规范的域名（FQDN）               | TAC-LB01.TAC-HB11.TAC.EPC.MNC001. MCC123.3GPPNETWORK.ORG TAC-LB02.TAC-HB11.TAC.EPC.MNC001. MCC123.3GPPNETWORK.ORG | TAC-LB01.TAC-HB11.TAC.EPC.MNC001. MCC123.3GPPNETWORK.ORG TAC-LB02.TAC-HB11.TAC.EPC.MNC001. MCC123.3GPPNETWORK.ORG | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 主机名索引（HSINDEX）                | 1 2                                                                                                               | 1 2                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 网元类型（ENTITY）                  | SGW PGW                                                                                                           | SGW PGW                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 接口类型（INTYPE）                  | S11 S5                                                                                                            | S11 S5                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 优先级（PRIORITY）                 | 10                                                                                                                | 10                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN      | 权重（WEIGHT）                    | 104                                                                                                               | 104                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| SET SMFUNC    | 拓扑选择开关（TOPSELCFG）             | YES                                                                                                               | YES                                                                                                               | 全网规划            | 配置就近选择合一SGW-C/PGW-C策略。                                                                                                                                                       |
| ADD GWSELPLCY | 选择策略（SELPLCY）                 | PGWFIRST                                                                                                          | PGWFIRST                                                                                                          | 全网规划            | 配置就近选择合一SGW-C/PGW-C策略。                                                                                                                                                       |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置S11-C接口业务IP。

   ```
   //DC1
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN";
   //DC2
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.18", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   - 配置S11-C接口与其他GTPC接口共部署时，GTP-C本端实体对应的组号配置为0。
     1. 配置MME在S11-C接口的GTP-C IP。

        ```
        //DC1
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        //DC2
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.18",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        //DC1
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        //DC2
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
   - 当需要将S11-C接口与其他GTPC接口分离部署时，配置S11接口分离。此时将GTP-C本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在S11-C接口的GTP-C IP。

        ```
        //DC1
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        //DC2
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.18",VPNNAME="VPN_CN";
        ```
     2. 配置GTP-C路径管理参数。

        ```
        //DC1
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        //DC2
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
     3. 配置GTP-C接口属性。

        ```
        //DC1
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S11, GRPID=3;
        //DC2
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S11, GRPID=3;
        ```
4. **可选：**配置SGW-C解析数据。

   ```
   //DC1
   ADD IPV4DNSH:HSINDEX=1,HOSTNAME="topon.eth1.gw32.nodes",ADDRSECTION=SECTION1,IPV4ADDR1="10.2.215.26"; 
   ADD IPV4DNSH:HSINDEX=2,HOSTNAME="topon.eth2.gw32.nodes",ADDRSECTION=SECTION1,IPV4ADDR1="10.2.215.27"; 
   ADD DNSN:FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG",HSINDEX=1,ENTITY=SGW,INTYPE=S11,PRIORITY=10,WEIGHT=104; 
   ADD DNSN:FQDN="TAC-LB02.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG",HSINDEX=2,ENTITY=PGW,INTYPE=S5,PRIORITY=10,WEIGHT=104;
   //DC2
   ADD IPV4DNSH:HSINDEX=1,HOSTNAME="topon.eth1.gw32.nodes",ADDRSECTION=SECTION1,IPV4ADDR1="10.2.215.26"; 
   ADD IPV4DNSH:HSINDEX=2,HOSTNAME="topon.eth2.gw32.nodes",ADDRSECTION=SECTION1,IPV4ADDR1="10.2.215.27"; 
   ADD DNSN:FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG",HSINDEX=1,ENTITY=SGW,INTYPE=S11,PRIORITY=10,WEIGHT=104;
   ```

   ```
   ADD DNSN:FQDN="TAC-LB02.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG",HSINDEX=2,ENTITY=PGW,INTYPE=S5,PRIORITY=10,WEIGHT=104;
   ```
5. 配置就近选择合一SGW-C/PGW-C策略。

   ```
   //DC1
   SET SMFUNC: TOPSELCFG=YES;
   ADD GWSELPLCY: SUBRANGE=ALL_USER, APNNI="huawei1.com", SLCTM=STANDARD_SELECTION_MODE, SELPLCY=PGWFIRST;
   //DC2
   SET SMFUNC: TOPSELCFG=YES;
   ADD GWSELPLCY: SUBRANGE=ALL_USER, APNNI="huawei1.com", SLCTM=STANDARD_SELECTION_MODE, SELPLCY=PGWFIRST;
   ```

## 验证方法

1. 进入“MML命令行-UEG”窗口。
2. 检查GTPC GTP路径对端是否可达。

   ****TST UAMGTPCPATH****

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST UAMGTPCPATH: GTPVER=GTPv2, IPTYPE=IPV4, LOCALIPV4="192.168.140.17", PEERIPV4="192.168.9.20";%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本端IPv4地址  =  192.168.140.17 
     对端IPv4地址  =  192.168.9.20      
         GTP版本  =  GTPv2 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
3. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成MME与eNodeB、UEG、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪任务。

      参数选择如下：
      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   2. **可选：**创建GTPC协议接口跟踪（S11-C）。

      参数选择如下：
      - Ru名称：资源单元的名称。
      - 本端IPv4/6地址：填本端IP地址。
      - 对端IPv4/6地址：填对端SGW-C的IP。
      - 其它参数：选择默认值。
   3. 用户开机附着。
   4. **可选：**查看S11-C接口跟踪结果。
      - **预期结果：**可以在Message Direction处看到MME和SGW-C之间有消息交互。

        如果是附着流程，应该存在Create Session和Modify Bearer交互流程。SGW-C->MME Create Session Response消息cause信元为request accepted；SGW-C->MME Modify Bearer Response消息cause信元为request accepted。

        如果执行了****RMV USR****命令后，应该存在Delete Session交互流程。SGW-C->MME Delete Session Response消息cause信元为request accepted。
      - **异常结果：**观察不到MME与SGW-C之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。
      - **预期结果：**用户切换成功，可以在Message Direction处看到MME与SGW-C之间有消息交互。

        **说明** 

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      - **异常结果：**观察不到MME与SGW-C之间有消息交互。或观察到MME与SGW-C之间的消息异常。