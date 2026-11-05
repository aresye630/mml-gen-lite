# 配置到GnGp SGSN的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到Gn/Gp SGSN的路由数据后，可通过配置Gn接口数据建立MME到Gn/Gp SGSN的逻辑连接。

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

| 类别            | 参数名称                           | 取值样例                                                          | 获取方法            | 说明                                                                                                                                                          |
|:--------------|:-------------------------------|:--------------------------------------------------------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）                | IPv4                                                          | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                   |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）          | 10.10.0.1                                                     | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                   |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）           | VRF_CN                                                        | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                   |
| ADD GTPCLE    | 组号（GROUPID）                    | 0                                                             | 参见“水平网设LLD文档 ”。 | 融合配置时，各GTP接口的本端地址是统一配置。                                                                                                                                     |
| ADD GTPCLE    | IP地址类型（IPTYPE）                 | TPTADDR_TYPE_IPV4                                             | 参见“水平网设LLD文档 ”。 | 融合配置时，各GTP接口的本端地址是统一配置。                                                                                                                                     |
| ADD GTPCLE    | IPv4地址（LEIPV4）                 | 10.10.0.1                                                     | 参见“水平网设LLD文档 ”。 | 融合配置时，各GTP接口的本端地址是统一配置。                                                                                                                                     |
| ADD GTPCLE    | VPN名称（VPNNAME）                 | VPN_CN                                                        | 参见“水平网设LLD文档 ”。 | 融合配置时，各GTP接口的本端地址是统一配置。                                                                                                                                     |
| SET UGTP      | 空闲计数器扫描间隔（秒）（ICI）              | 180                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET UGTP      | SM信令路径空闲计数器（SSI）               | 60                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET UGTP      | MM信令路径空闲计数器（MSI）               | 60                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET UGTP      | 路径版本探测扫描周期（分钟）（PATHVERCHKINT）  | 60                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| ADD DNSS      | IP地址（IP）                       | 10.29.147.3                                                   | 参见“水平网设LLD文档 ”。 | 配置DNS服务器。                                                                                                                                                   |
| ADD DNSS      | 域名服务器优先级（PRI）                  | PRI1                                                          | 参见“水平网设LLD文档 ”。 | 配置DNS服务器。                                                                                                                                                   |
| ADD DNSLE     | IP地址类型（IPT）                    | IPV4                                                          | 参见“水平网设LLD文档 ”。 | 增加DNS本端实体。                                                                                                                                                  |
| ADD DNSLE     | IPv4地址（IPV4）                   | 10.10.0.1                                                     | 参见“水平网设LLD文档 ”。 | 增加DNS本端实体。                                                                                                                                                  |
| ADD DNSLE     | 本地端口号（LOCPORT）                 | 15001                                                         | 参见“水平网设LLD文档 ”。 | 增加DNS本端实体。                                                                                                                                                  |
| ADD DNSLE     | DNS本端实体名称（LENAME）              | Dnsle                                                         | 参见“水平网设LLD文档 ”。 | 增加DNS本端实体。                                                                                                                                                  |
| ADD IPV4DNSH  | 主机名索引（HSINDEX）                 | 1，7                                                           | 参见“水平网设LLD文档 ”。 | 配置SGSN的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | 主机名（HOSTNAME）                  | RAC002B.LAC02D9.MNC001.MCC123.GPRS RNC025B.MNC001.MCC123.GPRS | 参见“水平网设LLD文档 ”。 | 配置SGSN的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | 主机地址段号（ADDRSECTION）            | SECTION1                                                      | 参见“水平网设LLD文档 ”。 | 配置SGSN的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME格式定义详见配置Hostfile数据。 |
| ADD IPV4DNSH  | IPV4地址1（IPV4ADDR1）             | 10.10.1.2                                                     | 参见“水平网设LLD文档 ”。 | 配置SGSN的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 HOSTNAME格式定义详见配置Hostfile数据。 |
| SET GTPPUB    | 发送私有信息（PRVEXT）                 | ON                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 发送ECHO Request的路径（ECHOSIG）     | ALL                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 发送Echo请求间隔（s）（EI）              | 239                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 乱序信元（OTSIE）                    | DENY                                                          | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 路径数过载门限（%）（POTHD）              | 85                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 路径数过载恢复（%）（PNTHD）              | 80                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 路径数拥塞门限（%）（PCTHD）              | 95                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 路径数拥塞恢复（%）（PRTHD）              | 90                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 企业号（PEID）                      | 2011                                                          | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 私有信息（PE）                       | USN                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 检查GTP扩展头类型个数上限（GTPEXT）         | 10                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 检查GTP扩展头列表个数上限（GTPSUPEXTLIST）  | 100                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 检查GTP扩展头类型长度上限（GTPEXLEN）       | 100                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 本端可处理的请求消息的最高GTP版本（GTPVER）     | GTPv2                                                         | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | 对端Recovery处理开关（PEERRECOVERYSW） | OFF                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | GTPC路径断去激活开关（PATHDOWNDEASW）    | OFF                                                           | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |
| SET GTPPUB    | GTPC报文校验功能开关（UDPCHKSW）         | ON                                                            | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。                                                                                                                                                |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Gn接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.0.1", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。
   1. 配置GTPC业务IP。

      ```
      ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.10.0.1",VPNNAME="VPN_CN";
      ```
   2. **可选：**如果需要将Gn接口和其他接口分离部署，配置Gn接口GTPC逻辑接口隔离。

      ****ADD GTPCINTFATTR****
   3. **可选：**配置GTP路径管理参数。

      ```
      SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60; 
      SET GTPPUB:PRVEXT=ON,ECHOSIG=ALL,EI=239,OTSIE=DENY,POTHD=85,PNTHD=80,PCTHD=95,PRTHD=90,PEID=2011,PE="USN",GTPEXT=10,GTPSUPEXTLIST=100,GTPEXLEN=100,GTPVER=GTPv2,PEERRECOVERYSW=OFF,PATHDOWNDEASW=OFF,UDPCHKSW=ON;
      ```
   4. **可选：**配置GTPU本地实体。

      ****ADD GTPULE****
   5. **可选：**如果需要将Gn接口和其他接口分离部署，配置Gn接口GTPU逻辑隔离。

      ****ADD GTPUINTFATTR****
   6. **可选：**配置DNS服务器的数据。

      **说明** 

      如果现网已经完成DNS服务器的数据配置，则无需执行本步骤。

      **ADD DNSLE**命令中：
      - 配置了GTP-C IP的UNC必须同时配置DNS客户端IP才能进行相关的业务。
      - 此IP地址为UNC中定义的IP地址。
4. 配置SGSN的解析数据，增加Hostfile文件的A解析记录。
   1. Attach/TAU/NACC流程配置GnGp网元的DNS记录。

      ```
      ADD IPV4DNSH:HSINDEX=1,HOSTNAME="RAC002B.LAC02D9.MNC001.MCC123.GPRS",ADDRSECTION=SECTION1,IPV4ADDR1="10.10.1.2";
      ```
   2. Handover流程配置GnGp网元的DNS记录。

      ```
      ADD IPV4DNSH:HSINDEX=7,HOSTNAME="RNC025B.MNC001.MCC123.GPRS",ADDRSECTION=SECTION1,IPV4ADDR1="10.10.1.2";
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查GTPC GTP路径对端是否可达。

   **TST GTPCPATH**

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="10.10.0.1", PEERIPV4ADDR="10.10.1.2";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     ------------------------- 
     本端IP地址  =  10.10.0.1 
     对端IP地址  =  10.10.1.2    
        GTP版本  =  GTPv1 
     (结果数目 = 1) 
      ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
3. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成UNC与SGSN(GnGp)、eNodeB、SGW、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确，并且保证UNC与SGSN互通。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪任务。

      参数选择如下：
      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   2. 创建GTPC协议接口跟踪。

      参数选择如下：
      - IP地址类型：填入跟踪的IP类型。
      - 本端IPv4/6地址：填本端IP地址。
      - 对端IPv4/6地址：填对端MME的IP。
      - 其它参数：选择默认值。
   3. 用户开机在本端MME附着，之后进行Detach，然后在对端SGSN做了一次TAU。最后再到本端MME进行Inter RAT TAU流程。
   4. 查看Gn接口跟踪结果。
      - **预期结果：**可以在Message Direction处看到LOC和PEER之间有消息交互

        如果是Inter RAT TAU流程，应该存在SGSN Context Request/Response交互流程。PEER->LOC SGSN Context Response消息协议类型为GTPv1，cause信元为request accepted。
      - **异常结果：**观察不到LOC与PEER之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。
      - **预期结果：**用户切换成功，可以在Message Direction处看到MME与SGSN之间有消息交互。

        **说明** 

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      - **异常结果：**观察不到MME与SGSN之间有消息交互。或观察到MME与SGSN之间的消息异常。