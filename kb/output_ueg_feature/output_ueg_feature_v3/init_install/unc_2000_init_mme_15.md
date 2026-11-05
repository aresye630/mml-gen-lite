# 配置N26接口数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。

N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。

**图1** N26接口协议栈

MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。

* 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。
* 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

双DC组网场景下，MME不仅需要和本DC内的AMF对接，也需要和另外一个DC的AMF对接。

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
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  | 参见“水平网设LLD文档 ”。 | 配置业务IP参数 |
|  | 业务IPv4地址（SERVICEIPV4） | 192.168.140.17 | 192.168.140.18 |  | - |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  | UEG风筝形态内部接口组网时，使用园区统一规划的VPN。 |
| ****ADD GTPCLE**** | 组号（GROUPID） | 3 |  |  | 配置GTP-C本地实体。 |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |  |
|  | IPv4地址（LEIPV4） | 192.168.140.17 | 192.168.140.18 |  |  |
|  | VPN名称（VPNNAME） | VPN\_CN |  |  |  |
| ****SET UGTP**** | 空闲计数器扫描间隔（秒）（ICI） | 180 |  |  | 配置GTP路径管理参数。 |
|  | SM信令路径空闲计数器（SSI） | 60 |  |  |  |
|  | MM信令路径空闲计数器（MSI） | 60 |  |  |  |
|  | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60 |  |  |  |
| ****ADD GTPCINTFATTR**** | 用户范围（SUBRANGE） | ALL\_USER |  |  | 配置N26接口分离。 |
|  | 接口类型（INTFTP） | S10 |  |  |  |
|  | 组号（GRPID） | 3 |  |  |  |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 4  5  6 |  |  | * 配置AMF的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。 |
|  | 主机名（HOSTNAME） | topon.eth6.mmec14.mmegi8001.mme  topon.eth4.mmec12.mmegi8001.mme |  |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |  |
|  | IPv4地址1（IPV4ADDR1） | 10.10.1.1  10.11.1.3 |  |  |  |
|  | IPv4地址2（IPV4ADDR2） | 10.10.1.2  10.11.1.4 |  |  |  |
| ****ADD DNSN**** | FQDN（FQDN） | MMEC12.MMEG18001.MME.EPC.  MNC001.MCC123.3GPPNETWORK.ORG  TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.  MNC001.MCC123.3GPPNETWORK.ORG | MMEC14.MMEG18001.MME.EPC.  MNC001.MCC123.3GPPNETWORK.ORG  TAC-LB01.TAC-HB11.TAC.EPC.  MNC001.MCC123.3GPPNETWORK.ORG |  | - |
|  | 主机名索引（HSINDEX） | 4  5 |  |  |  |
|  | 网元类型（ENTITY） | MME |  |  |  |
|  | 接口类型（INTYPE） | S10 |  |  | MME上N26接口与S10接口共用一个S10接口实现。 |
|  | 优先级（PRIORITY） | 18  17 |  |  | - |
|  | 权重（WEIGHT） | 112  111 |  |  |  |
| ****ADD N26IWKPLCY**** | 用户范围（SUBRANGE） | ALL\_USER |  | 全网规划 | 配置LTE和5G网络互操作策略。 |
|  | 是否支持接入5GC(IS5GCALLOW) | YES |  | 全网规划 |  |
|  | 是否允许接入5GS的NR(ISNRALLOW) | YES |  | 全网规划 |  |
|  | 融合SMF+PGW-C选择策略（SMFSELPLCY） | N1CAP\_CNR |  | 全网规划 |  |
| ****SET DNS**** | 非5G用户是否选择到融合的SMF+PGW-C（NON5GSEL） | YES |  | 全网规划 | 限制非5G用户接入融合网关SMF+PGW-C。 |
| **SET S1CMPT** | 是否携带NR Restriction in 5GS信元（NRRIN5GS） | YES |  | 全网规划 | 配置S1接口兼容性参数。 |
|  | 是否携带Core Network Type Restrictions信元（CNR） | YES |  | 全网规划 |  |
| ****ADD MMECHARACT**** | RANGE（对端设备范围） | ALL\_MME |  | 全网规划 | 增加对端MME属性信息，配置S10接口兼容性参数。 |
|  | 是否携带UE NR安全能力（UENRSECCAP） | YES |  | 全网规划 |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置N26接口业务IP。

   ```
   //DC1
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN";
   //DC2
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.18", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   * 配置N26接口与其他GTPC接口共部署时，GTPC本端实体对应的组号配置为0。
     1. 配置MME在N26接口的GTPC IP。

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
   * 当需要将N26接口与其他GTPC接口分离部署时，配置N26接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在N26接口的GTPC IP。

        ```
        //DC1
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        //DC2
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.18",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        //DC1
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60; 
        //DC2
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
     3. 配置GTPC接口属性。

        ```
        //DC1
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S10, GRPID=3;
        //DC2
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S10, GRPID=3;
        ```
4. **可选：**配置本端MME的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

   ```
   //DC1
   ADD IPV4DNSH: HSINDEX=4, HOSTNAME="topon.eth4.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.1.1", IPV4ADDR2="10.10.1.2"; 
   ADD DNSN: FQDN="MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=18, WEIGHT=112; 
   ADD DNSN: FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=17, WEIGHT=111;
   //DC2
   ADD IPV4DNSH: HSINDEX=4, HOSTNAME="topon.eth4.mmec14.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.1.1", IPV4ADDR2="10.10.1.2"; 
   ADD DNSN: FQDN="MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=18, WEIGHT=112; 
   ADD DNSN: FQDN="TAC-LB02.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=17, WEIGHT=111;
   ```
5. **可选：**配置对端AMF的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择AMF使用的DNS记录及在Inter Handover流程中根据TAI值选择AMF使用的DNS记录。

   ```
   //DC1
   ADD IPV4DNSH: HSINDEX=6, HOSTNAME="topon.eth6.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.11.1.3", IPV4ADDR2="10.11.1.4"; 
   ADD DNSN: FQDN="MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=20, WEIGHT=114;  
   ADD DNSN: FQDN="TAC-LB02.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=19, WEIGHT=113; 
   //DC2
   ADD IPV4DNSH: HSINDEX=6, HOSTNAME="topon.eth6.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.11.1.3", IPV4ADDR2="10.11.1.4"; 
   ADD DNSN: FQDN="MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=20, WEIGHT=114;  
   ADD DNSN: FQDN="TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=19, WEIGHT=113;
   ```
6. 配置支持UE在LTE与5G SA网络间互操作。

   1. 打开LTE与5G SA网络互操作特性的License配置开关。

      ```
      //DC1
      SET LICENSESWITCH: LICITEM="LKV2NRBL5", SWITCH=ENABLE;
      SET LICENSESWITCH: LICITEM="LKV2PHBL5", SWITCH=ENABLE;
      //DC2
      SET LICENSESWITCH: LICITEM="LKV2NRBL5", SWITCH=ENABLE;
      SET LICENSESWITCH: LICITEM="LKV2PHBL5", SWITCH=ENABLE;
      ```
   2. 设置本特性必选软件参数。

      ```
      //DC1
      SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=5, VALUE=VALUE_1, POSITION=8;
      //DC2
      SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=5, VALUE=VALUE_1, POSITION=8;
      ```
   3. 配置LTE和5G网络互操作策略。
      1. 增加互操作本地策略。

         ```
         //DC1
         ADD N26IWKPLCY: SUBRANGE=ALL_USER, IS5GCALLOW=YES, ISNRALLOW=YES, SMFSELPLCY=N1CAP_CNR;
         //DC2
         ADD N26IWKPLCY: SUBRANGE=ALL_USER, IS5GCALLOW=YES, ISNRALLOW=YES, SMFSELPLCY=N1CAP_CNR;
         ```
      2. **可选：**如果需要限制非5G用户接入融合网关SMF+PGW-C，执行本步骤。

         ```
         //DC1
         SET DNS: NON5GSEL=NO;
         //DC2
         SET DNS: NON5GSEL=NO;
         ```
   4. **可选：**配置S1接口兼容性参数。

      ```
      //DC1
      SET S1CMPT: NRRIN5GS=YES, CNR=YES;
      //DC2
      SET S1CMPT: NRRIN5GS=YES, CNR=YES;
      ```
   5. **可选：**增加对端MME属性信息，配置S10接口兼容性参数。

      ```
      //DC1
      ADD MMECHARACT: RANGE=ALL_MME, UENRSECCAP=YES;
      //DC2
      ADD MMECHARACT: RANGE=ALL_MME, UENRSECCAP=YES;
      ```
   6. **可选：**在LTE和5G网络间重选的过程中需要优选AMF与MME融合部署的AMF时，设置如下软参取值为“1”。

      ```
      //DC1
      SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=331, VALUE=VALUE_1, POSITION=3;
      //DC2
      SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=331, VALUE=VALUE_1, POSITION=3;
      ```

## 验证方法

1. 检查GTPC GTP路径对端是否可达。

   进入“MML命令行-UEG”窗口。

   **TST UAMGTPCPATH**

   * **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST UAMGTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCALIPV4="192.168.140.17", PEERIPV4="10.2.154.24";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     -------------------------  
          GTP版本  =  GTPv1
     本端IPv4地址  =  192.168.140.17  
     本端IPv6地址  =  :: 
     对端IPv4地址  =  10.2.154.24 
     对端IPv6地址  =  ::    
        网元类型   =  MME
     (结果数目 = 1) 

      ---    END
     ```
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
2. 进行业务测试。

   * 进行业务测试前，需要首先完成MME与eNodeB、HSS的链路配置。
   * 进行业务测试时，需要保证MME与AMF之间互通。
   * 进行业务测试的手机必须是在对接的HSS开户的手机。

   1. **创建用户跟踪任务**。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. **可选：**

      **创建GTPC协议接口跟踪（N26）**。

      参数选择如下：
      * IP地址类型：填入跟踪的IP类型。
      * 本端IPv4/6地址：填本端IP地址。
      * 对端IPv4/6地址：填对端AMF的IP。
      * 其它参数：选择默认值。
   3. 用户开机在本端附着，然后进行LTE到5G网络的切换以触发Handover流程。
   4. 查看用户跟踪结果。

      * **预期结果：**用户切换成功，可以在Forward Relocation Request消息中的Target ID信元携带gNodeB ID。

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**观察不到Forward Relocation Request消息中的Target ID信元携带gNodeB ID，或观察到MME与AMF之间的消息异常。

版权所有 © 华为技术有限公司
