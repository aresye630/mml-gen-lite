# 配置到S-GW的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增S-GW或MME时，在配置完成MME到S-GW的路由数据后，可通过配置S11接口数据建立MME到S-GW的逻辑连接。

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

| 类别            | 参数名称                          | 取值样例                                                    | 获取方法            | 说明                                                                                                                                                                                                          |
|:--------------|:------------------------------|:--------------------------------------------------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）               | IPv4                                                    | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                   |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）         | 192.168.140.17                                          | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                   |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）          | VPN_CN                                                  | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                                                   |
| ADD GTPCLE    | 组号（GROUPID）                   | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置本端的S11接口的GTP-C IP。                                                                                                                                                                                        |
| ADD GTPCLE    | IP地址类型（IPTYPE）                | TPTADDR_TYPE_IPV4                                       | 参见“水平网设LLD文档 ”。 | 配置本端的S11接口的GTP-C IP。                                                                                                                                                                                        |
| ADD GTPCLE    | IPv4地址（LEIPV4）                | 192.168.140.17                                          | 参见“水平网设LLD文档 ”。 | 配置本端的S11接口的GTP-C IP。                                                                                                                                                                                        |
| ADD GTPCLE    | VPN名称（VPNNAME）                | VPN_CN                                                  | 参见“水平网设LLD文档 ”。 | 配置本端的S11接口的GTP-C IP。                                                                                                                                                                                        |
| SET UGTP      | 空闲计数器扫描间隔（秒）（ICI）             | 180                                                     | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                                                |
| SET UGTP      | SM信令路径空闲计数器（SSI）              | 60                                                      | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                                                |
| SET UGTP      | MM信令路径空闲计数器（MSI）              | 60                                                      | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                                                |
| SET UGTP      | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60                                                      | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                                                                |
| ADD IPV4DNSH  | 主机名索引（HSINDEX）                | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | 主机名（HOSTNAME）                 | topon.eth1.gw32.nodes                                   | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | IPV4地址1（IPV4ADDR1）            | 10.80.47.1                                              | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | 主机地址段号（ADDRSECTION）           | SECTION1(1)                                             | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 全称标准规范的域名（FQDN）               | TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 主机名索引（HSINDEX）                | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 网元类型（ENTITY）                  | SGW                                                     | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 接口类型（INTYPE）                  | S11                                                     | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 优先级（PRIORITY）                 | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |
| ADD DNSN      | 权重（WEIGHT）                    | 104                                                     | 参见“水平网设LLD文档 ”。 | 配置S-GW的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择S-GW。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME及FQDN格式定义详见配置Hostfile数据。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S11接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   - 配置S11接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。
     1. 配置MME在S11接口的GTP-C IP。

        ```
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
   - 当需要将S11接口与其他接口分离部署时，配置S11接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在S11接口的GTP-C IP。

        ```
        ADD GTPCLE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_CN";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60;
        ```
     3. 配置GTPC接口属性。

        ```
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=S11, GRPID=3;
        ```
4. **可选：**配置S-GW解析数据。

   ```
   ADD IPV4DNSH:HSINDEX=1,HOSTNAME="topon.eth1.gw32.nodes",ADDRSECTION=SECTION1,IPV4ADDR1="10.80.47.1"; 
   ADD DNSN:FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG",HSINDEX=1,ENTITY=SGW,INTYPE=S11,PRIORITY=10,WEIGHT=104;
   ```
5. **可选：**在NBIoT场景下，配置S11-U接口，用于MME与SGW-U传输用户面数据。

   1. 配置S11-U接口业务IP。

      ```
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.20", VPNINSTNAME="VRF_IOT_CN";
      ```
   2. 配置GTP数据。
      - 配置S11-U接口与其他接口共部署时，GTPU本端实体对应的组号配置为0。

        配置MME在S11-U接口的GTP-U IP。

        ```
        ADD GTPULE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.20",VPNNAME="VRF_IOT_CN";
        ```
      - 当需要将S11-U接口与其他接口分离部署时，配置S11-U接口分离。此时将GTPU本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
        1. 配置MME在S11-U接口的GTP-U IP。

           ```
           ADD GTPULE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.20",VPNNAME="VRF_IOT_CN";
           ```
        2. 配置GTPU接口属性。

           ```
           ADD GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=S11, GRPID=3;
           ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查GTPC GTP路径对端是否可达。

   ****TST GTPCPATH****

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATH: GTPVER=GTPv2, IPTYPE=IPV4, LOCIPV4ADDR="192.168.140.17", PEERIPV4ADDR="10.80.47.1";%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本端IPv4地址  =  192.168.140.17 
     对端IPv4地址  =  10.80.47.1      
         GTP版本  =  GTPv2 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
3. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成UNC与eNodeB、UDG、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪任务。

      参数选择如下：
      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   2. **可选：**创建GTPC协议接口跟踪（S3、S4、S10、S11、S16、Gn、Gp）。

      参数选择如下：
      - Ru名称：资源单元的名称。
      - 本端IPv4/6地址：填本端IP地址。
      - 对端IPv4/6地址：填对端S-GW的IP。
      - 其它参数：选择默认值。
   3. 用户开机附着。
   4. **可选：**查看S11接口跟踪结果。
      - **预期结果：**可以在Message Direction处看到MME和S-GW之间有消息交互。

        如果是附着流程，应该存在Create Session和Modify Bearer交互流程。S-GW->MME Create Session Response消息cause信元为request accepted；S-GW->MME Modify Bearer Response消息cause信元为request accepted。

        如果执行了****RMV USR****命令后，应该存在Delete Session交互流程。S-GW->MME Delete Session Response消息cause信元为request accepted。
      - **异常结果：**观察不到MME与S-GW之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。
      - **预期结果：**用户切换成功，可以在Message Direction处看到MME与S-GW之间有消息交互。

        **说明** 

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      - **异常结果：**观察不到MME与S-GW之间有消息交互。或观察到MME与S-GW之间的消息异常。