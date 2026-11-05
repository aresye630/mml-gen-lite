# 配置到AMF的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。

由于MME上N26接口与S10接口共用同一个接口实现，所以如果已经配置S10接口，不需要再配置N26接口的业务IP、GTP数据以及解析数据。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数 |
|  | 业务IPv4地址（SERVICEIPV4） | 192.168.140.17 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  |
| ****ADD GTPCLE**** | 组号（GROUPID） | 3 |  | 配置GTP-C本地实体。 |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |
|  | IPv4地址（LEIPV4） | 192.168.140.17 |  |  |
|  | VPN名称（VPNNAME） | VPN\_CN |  |  |
| ****SET UGTP**** | 空闲计数器扫描间隔（秒）（ICI） | 180 |  | 配置GTP路径管理参数 |
|  | SM信令路径空闲计数器（SSI） | 60 |  |  |
|  | MM信令路径空闲计数器（MSI） | 60 |  |  |
|  | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60 |  |  |
| ****ADD GTPCINTFATTR**** | 用户范围（SUBRANGE） | ALL\_USER |  | 配置N26接口分离。 |
|  | 接口类型（INTFTP） | S10 |  |  |
|  | 组号（GRPID） | 3 |  |  |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 4  5  6 |  | * 配置AMF的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。  * HOSTNAME及FQDN格式定义详见配置Hostfile数据。 * 如果对端AMF开启了MME-S10和AMF-N26接口地址合一功能，则注意此处的AMF IP地址与MME S10地址相同，需要修改MME上查询AMF的IPV4DNSH的地址为MME的GTPCLE地址。 * 当配置对端AMF解析时，可以通过S10或N26选择AMF，S10和N26方式二选一。 |
|  | 主机名（HOSTNAME） | topon.eth6.mmec14.mmegi8001.mme  topon.eth4.mmec12.mmegi8001.mme |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPv4地址1（IPV4ADDR1） | 10.10.1.1  10.11.1.3 |  |  |
|  | IPv4地址2（IPV4ADDR2） | 10.10.1.2  10.11.1.4 |  |  |
| ****ADD DNSN****（本端MME） | FQDN（FQDN） | MMEC14.MMEG18001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG  TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG |  |  |
|  | 主机名索引（HSINDEX） | 4 |  |  |
|  | 网元类型（ENTITY） | MME |  |  |
|  | 接口类型（INTYPE） | S10 |  |  |
|  | 优先级（PRIORITY） | 18  17 |  |  |
|  | 权重（WEIGHT） | 112  111 |  |  |
| **ADD DNSN**（对端AMF） | FQDN（FQDN） | * 基于S10：   + MMEC12.MMEG18001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG   + TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG  * 基于N26：   + PT12.SET260.REGION31.AMFI.5GC.MNC001.MCC123.3GPPNETWORK.ORG   + TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG |  |  |
|  | 主机名索引（HSINDEX） | 6 |  |  |
|  | 网元类型（ENTITY） | 基于S10：MME  基于N26：AMF、MME |  |  |
|  | 接口类型（INTYPE） | 基于S10：S10  基于N26：N26、S10 |  |  |
|  | 优先级（PRIORITY） | 20  19 |  |  |
|  | 权重（WEIGHT） | 114  113 |  |  |
| ****ADD N26IWKPLCY**** | 用户范围（SUBRANGE） | ALL\_USER | 全网规划 | 配置LTE和5G网络互操作策略。 |
|  | 是否支持接入5GC(IS5GCALLOW) | YES | 全网规划 |  |
|  | 是否允许接入5GS的NR(ISNRALLOW) | YES | 全网规划 |  |
|  | 融合SMF+PGW-C选择策略（SMFSELPLCY） | N1CAP\_CNR | 全网规划 |  |
| ****SET DNS**** | N26DNSTYPE | S10或N26 | 全网规划 | 配置LTE和5G网络互操作DNS查询方式，S10与N26方式二选一。   * 如果运营商希望DNS查询AMF时采用N26标准方式，则配置为N26。 * 如果运营商希望DNS查询AMF时采用S10标准方式，则配置为S10。 |
|  | 非5G用户是否选择到融合的SMF+PGW-C（NON5GSEL） | YES | 全网规划 | 限制非5G用户接入融合网关SMF+PGW-C。 |
| **SET S1CMPT** | 是否携带NR Restriction in 5GS信元（NRRIN5GS） | YES | 全网规划 | 配置S1接口兼容性参数。 |
|  | 是否携带Core Network Type Restrictions信元（CNR） | YES | 全网规划 |  |
|  | 是否携带GUAMI映射的GUMMEI（GUAMIGUMMEI） | YES | 全网规划 | 可选，仅当在LTE和5G网络间重选的过程中需要优选AMF与MME融合部署的AMF时执行。 |
| ****ADD MMECHARACT**** | RANGE（对端设备范围） | ALL\_MME | 全网规划 | 增加对端MME属性信息，配置S10接口兼容性参数。 |
|  | 是否携带UE NR安全能力（UENRSECCAP） | YES | 全网规划 |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置N26接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   * 配置N26接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。
     1. 配置MME在N26接口的GTPC IP。

        ```
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
   * 当需要将N26接口与其他接口分离部署时，配置N26接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在N26接口的GTPC IP。

        ```
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
     3. 配置GTPC接口属性。

        ```
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S10, GRPID=3;
        ```
4. **可选：**配置本端MME的域名解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

   ```
   ADD IPV4DNSH: HSINDEX=4, HOSTNAME="topon.eth6.mmec14.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.1.1", IPV4ADDR2="10.10.1.2"; 
   ADD DNSN: FQDN="MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=18, WEIGHT=112; 
   ADD DNSN: FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=17, WEIGHT=111;
   ```
5. 配置LTE和5G互操作DNS查询方式。

   //配置基于S10选择AMF（S10与N26方式二选一）：

   ```
   SET DNS:N26DNSTYPE=S10;
   ```

   //配置基于N26选择AMF（S10与N26方式二选一）：

   ```
   SET DNS:N26DNSTYPE=N26;
   ```
6. （可选）配置对端AMF的域名解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择AMF使用的DNS记录及在Inter Handover流程中根据TAI值选择AMF使用的DNS记录。

   //当未对接DNS服务器，需要配置本地解析时，执行本操作。

   ```
   ADD IPV4DNSH: HSINDEX=6, HOSTNAME="topon.eth4.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.11.1.3", IPV4ADDR2="10.11.1.4";
   ```

   //当未对接DNS服务器，需要配置本地解析，S10和N26地址合一时，执行本操作。

   ```
   ADD IPV4DNSH: HSINDEX=6, HOSTNAME="topon.eth4.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.140.17";
   ```

   //配置基于S10选择AMF（S10与N26方式二选一）：

   ```
   ADD DNSN: FQDN="MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=20, WEIGHT=114;  
   ADD DNSN: FQDN="TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=19, WEIGHT=113;
   ```

   //配置基于N26选择AMF（S10与N26方式二选一）：

   ```
   ADD DNSN: FQDN="PT12.SET260.REGION31.AMFI.5GC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=AMF, INTYPE=N26, PRIORITY=20, WEIGHT=114;
   ADD DNSN: FQDN="TAC-LB01.TAC-MB21.TAC-HB61.5GSTAC.5GC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=6, ENTITY=MME, INTYPE=S10, PRIORITY=19, WEIGHT=113;
   ```
7. 配置支持UE在LTE与5G SA网络间互操作。

   1. 打开LTE与5G SA网络互操作特性的License配置开关。

      ```
      SET LICENSESWITCH: LICITEM="LKV2NRBL5", SWITCH=ENABLE;
      SET LICENSESWITCH: LICITEM="LKV2PHBL5", SWITCH=ENABLE;
      ```
   2. 设置本特性必选软件参数。

      ```
      SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=5, VALUE=VALUE_1, POSITION=8;
      ```
   3. 配置LTE和5G网络互操作策略。
      1. 增加互操作本地策略。

         ```
         ADD N26IWKPLCY: SUBRANGE=ALL_USER, IS5GCALLOW=YES, ISNRALLOW=YES, SMFSELPLCY=N1CAP_CNR;
         ```
      2. **可选：**如果需要限制非5G用户接入融合网关SMF+PGW-C，执行本步骤。

         ```
         SET DNS: NON5GSEL=NO;
         ```
   4. **可选：**配置S1接口兼容性参数。

      ```
      SET S1CMPT: NRRIN5GS=YES, CNR=YES;
      ```
   5. **可选：**增加对端MME属性信息，配置S10接口兼容性参数。

      ```
      ADD MMECHARACT: RANGE=ALL_MME, UENRSECCAP=YES;
      ```
   6. **可选：**（可选）配置在LTE和5G网络间重选的过程中优选AMF与MME融合部署的UAM。

      ```
      SET S1CMPT: GUAMIGUMMEI=YES;
      ```

## 验证方法

1. 检查GTPC GTP路径对端是否可达。

   进入“MML命令行-UNC”窗口。

   **TST GTPCPATH**

   * **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATH: GTPVER=GTPv2, IPTYPE=IPV4, LOCIPV4ADDR="192.168.140.17", PEERIPV4ADDR="10.11.1.3";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     -------------------------  
     本端IPv4地址  =  192.168.140.17  
     对端IPv4地址  =  10.11.1.3    
        GTP版本  =  GTPv2 
     (结果数目 = 1) 

      ---    END
     ```
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
2. 进行业务测试。

   * 进行业务测试前，需要首先完成UNC与eNodeB、UDG、HSS的链路配置。
   * 进行业务测试时，需要保证DNS的配置正确，并且UNC与UNC之间互通。
   * 进行业务测试的手机必须是在对接的HSS及UDM开户的手机。

   1. **创建用户跟踪任务**。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. **可选：**

      **创建GTPC协议接口跟踪（S3、S4、S10、S11、S16、Gn、Gp）**。

      参数选择如下：
      * IP地址类型：填入跟踪的IP类型。
      * 本端IPv4/6地址：填本端IP地址。
      * 对端IPv4/6地址：填对端AMF的IP。
      * 其它参数：选择默认值。
   3. 用户开机在本端附着，然后进行LTE到5G网络的切换以触发Handover流程。
   4. 查看用户跟踪结果。

      * **预期结果：**用户切换成功，可以在Forward Relocation Request消息中的Target ID信元携带gNodB ID。

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

      * **异常结果：**观察不到Forward Relocation Request消息中的Target ID信元携带gNodB ID，或观察到MME与AMF之间的消息异常。

版权所有 © 华为技术有限公司
