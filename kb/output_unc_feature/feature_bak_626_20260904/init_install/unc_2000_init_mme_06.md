# 配置到MME的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到MME的路由数据后，可通过配置S10接口数据建立MME到MME的逻辑连接。

由于MME上S10接口与N26接口共用同一个接口实现，所以如果已经配置N26接口，不需要再配置S10接口。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
- 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别               | 参数名称                                 | 取值样例                                                                                                                                                                                                                          | 获取方法            | 说明                                                                                                                                                              |
|:-----------------|:-------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP    | IP版本（IPVERSION）                      | IPv4                                                                                                                                                                                                                          | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                       |
| ADD SERVICEIP    | 业务IPv4地址（SERVICEIPV4）                | 192.168.140.17                                                                                                                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                       |
| ADD SERVICEIP    | VPN实例名称（VPNINSTNAME）                 | VPN_CN                                                                                                                                                                                                                        | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                       |
| ADD GTPCLE       | 组号（GROUPID）                          | 0                                                                                                                                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置GTPC本地实体。                                                                                                                                                     |
| ADD GTPCLE       | IP地址类型（IPTYPE）                       | TPTADDR_TYPE_IPV4                                                                                                                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置GTPC本地实体。                                                                                                                                                     |
| ADD GTPCLE       | IPv4地址（LEIPV4）                       | 192.168.140.17                                                                                                                                                                                                                | 参见“水平网设LLD文档 ”。 | 配置GTPC本地实体。                                                                                                                                                     |
| ADD GTPCLE       | VPN名称（VPNNAME）                       | VPN_CN                                                                                                                                                                                                                        | 参见“水平网设LLD文档 ”。 | 配置GTPC本地实体。                                                                                                                                                     |
| SET UGTP         | 空闲计数器扫描间隔（秒）（ICI）                    | 180                                                                                                                                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                    |
| SET UGTP         | SM信令路径空闲计数器（SSI）                     | 60                                                                                                                                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                    |
| SET UGTP         | MM信令路径空闲计数器（MSI）                     | 60                                                                                                                                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                    |
| SET UGTP         | 路径版本探测扫描周期（分钟）（PATHVERCHKINT）        | 60                                                                                                                                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                    |
| ADD GTPCINTFATTR | 用户范围（SUBRANGE）                       | ALL_USER                                                                                                                                                                                                                      | 参见“水平网设LLD文档 ”。 | 配置S10接口分离。                                                                                                                                                      |
| ADD GTPCINTFATTR | 接口类型（INTFTP）                         | S10                                                                                                                                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置S10接口分离。                                                                                                                                                      |
| ADD GTPCINTFATTR | 组号（GRPID）                            | 3                                                                                                                                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置S10接口分离。                                                                                                                                                      |
| ADD IPV4DNSH     | 主机名索引（HSINDEX）                       | 4                                                                                                                                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH     | 主机名（HOSTNAME）                        | topon.eth6.mmec14.mmegi8001.mme topon.eth4.mmec12.mmegi8001.mme                                                                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH     | 地址区间号（ADDRSECTION）                   | SECTION1                                                                                                                                                                                                                      | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH     | IPv4地址1~IPv4地址8（IPV4ADDR1_IPV4ADDR8） | 10.10.1.1 10.10.1.2 10.11.1.3 10.11.1.4                                                                                                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 全称标准规范的域名（FQDN）                      | MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG TAC-LB01.TAC-HB61.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 主机名索引（HSINDEX）                       | 4 6                                                                                                                                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 网元类型（ENTITY）                         | MME                                                                                                                                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 接口类型（INTYPE）                         | S10                                                                                                                                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 优先级（PRIORITY）                        | 17 18 19 20                                                                                                                                                                                                                   | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN         | 权重（WEIGHT）                           | 111 112 113 114                                                                                                                                                                                                               | 参见“水平网设LLD文档 ”。 | 配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S10接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   - 配置S10接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。
     1. 配置MME在S10接口的GTPC IP。

        ```
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
   - 当需要将S10接口与其他接口分离部署时，配置S10接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在S10接口的GTPC IP。

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
4. **可选：**配置对端MME的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

   ```
   ADD IPV4DNSH: HSINDEX=4, HOSTNAME="topon.eth6.mmec14.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.1.1", IPV4ADDR2="10.10.1.2"; 
   ADD DNSN: FQDN="MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=18, WEIGHT=112; 
   ADD DNSN: FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10, PRIORITY=17, WEIGHT=111;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查GTPC GTP路径对端是否可达。

   **TST GTPCPATH**

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.140.17", PEERIPV4ADDR="10.10.1.1";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     -------------------------  
     本端IPv4地址  =  192.168.140.17  
     对端IPv4地址  =  10.10.1.1    
        GTP版本  =  GTPv1 
     (结果数目 = 1)  
     ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
3. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成UNC与eNodeB、UDG、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确，并且两套UNC之间互通。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪任务。

      参数选择如下：
      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   2. **可选：**

      创建GTPC协议接口跟踪（S3、S4、S10、S11、S16、Gn、Gp）。

      参数选择如下：
      - IP地址类型：填入跟踪的IP类型。
      - 本端IPv4/6地址：填本端IP地址。
      - 对端IPv4/6地址：填对端MME的IP。
      - 其它参数：选择默认值。
   3. 用户开机在本端附着，然后进行Inter MME的切换以触发Handover流程。
   4. 查看S10接口跟踪结果。
      - **预期结果：**可以在Message Direction处看到LOC和PEERSGSNMME之间有消息交互。

        如果是Inter MME切换流程，应该存在Forward Relocation交互流程。PEERSGSNMME->LOC Forward Relocation Response消息协议类型是GTPv2，cause信元为request accepted。
      - **异常结果：**观察不到LOC与PEERSGSNMME之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。

      **预期结果：**用户切换成功，可以在Message Direction处看到MME与MME之间有消息交互。

      **说明** 

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

      - **异常结果：**观察不到MME与MME之间有消息交互。或观察到MME与MME之间的消息异常。