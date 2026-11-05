# 配置到MSC的数据（Sv接口）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC的路由数据后，可通过配置Sv接口数据建立MME到MSC的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

**表1** Sv接口准备的数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.1.3 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |
| ****ADD GTPCLE**** | 组号（GROUPID） | 1 |  | Sv接口本、对端的GTPC IP地址不能与SGs接口重复。 |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |
|  | IPv4地址（LEIPV4） | 10.10.1.3 |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |
| ****ADD GTPCINTFATTR**** | 用户范围（SUBRANGE） | ALL\_USER |  | 为增加网络安全性，建议将Sv接口和S10/S11接口分离部署。  * Sv接口采用单独的IP地址，并绑定到VRF中。 * VRF建议包括S6a/S6d/Gb/Iu\_c(IP)/Gr/Sv接口。 |
|  | 接口类型（INTFTP） | Sv |  |  |
|  | 组号 （GRPID） | 1 |  |  |
| ****SET UGTP**** | 空闲计数器扫描间隔（秒）（ICI） | 180 |  | 设置GTP-C路径扫描参数。 |
|  | SM信令路径空闲计数器（SSI） | 60 |  |  |
|  | MM信令路径空闲计数器（MSI） | 60 |  |  |
|  | GTPMAP路径空闲计数器（GMSI） | 60 |  |  |
|  | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60 |  |  |
| ****SET GTPPUB**** | 发送私有信息（PRVEXT） | OFF |  | 设置GTP-C协议参数。 |
|  | 发送ECHO Request的路径（ECHOSIG） | ALL |  |  |
|  | 乱序信元（OTSIE） | DENY |  |  |
|  | 路径数过载门限（%）（POTHD） | 85 |  |  |
|  | 路径数过载恢复（%）（PNTHD） | 80 |  |  |
|  | 路径数拥塞门限（%）（PCTHD） | 95 |  |  |
|  | 路径数拥塞恢复（%）（PRTHD） | 90 |  |  |
|  | 企业号（PEID） | 2011 |  |  |
|  | 私有信息（PE） | USN |  |  |
|  | 检查GTP扩展头类型个数上限（GTPEXT） | 10 |  |  |
|  | 检查GTP扩展头列表个数上限（GTPSUPEXTLIST） | 100 |  |  |
|  | 检查GTP扩展头类型长度上限（GTPEXLEN） | 100 |  |  |
|  | 本端可处理的请求消息的最高GTP版本（GTPVER） | GTPv2 |  |  |
|  | 缺省SGSN透传源端口号开关（POOLSRCPORTSW） | ON |  |  |
|  | 对端Recovery处理开关（PEERRECOVERYSW） | OFF |  |  |
|  | GTPC路径断去激活开关（PATHDOWNDEASW） | OFF |  |  |
|  | V0版本GTPC路径尝试使用V1版本探测开关（PATHVERDETECTSW） | ON |  |  |
|  | 过滤故障状态的GTPC路径开关（DNSGTPCPATHFILTERSW） | ON |  |  |
|  | 本端recovery更新开关（LOCRECOVERYSW） | ON |  |  |
|  | GTPC报文校验功能开关（UDPCHKSW） | ON |  |  |
| ****SET MSCSELPLCY**** | Sv接口域名解析策略（DNSPLCY） | LAI |  | 设置MSC域名解析策略。 |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 1 |  | 配置IPV4 DNS Hostfile记录。 |
|  | 主机名（HOSTNAME） | topon.sv.eth7.mnc001.mcc123.org |  |  |
|  | 主机地址段号（ADDRSECTION） | SECTION1 |  |  |
|  | IPV4地址1（IPV4ADDR1） | 10.22.133.145  10.22.133.146 |  |  |
| ****ADD DNSN**** | 全称标准规范的域名（FQDN） | LAC5101.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG |  | 增加Hostfile文件的NAPTR解析记录。 |
|  | 主机名索引（HSINDEX） | 1 |  |  |
|  | 网元类型（ENTITY） | MSC |  |  |
|  | 接口类型（INTYPE） | Sv |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Sv接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.3", VPNINSTNAME="VPN_SIG";
   ```
3. 配置GTP数据。

   * 配置Sv接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。
     1. 配置MME在Sv接口的GTPC IP。

        ```
        ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.10.1.3",VPNNAME="VPN_SIG";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60; 
        SET GTPPUB: PRVEXT=OFF, ECHOSIG=ALL, OTSIE=DENY, POTHD=85, PNTHD=80, PCTHD=95, PRTHD=90, PEID=2011, PE="USN", GTPEXT=10, GTPSUPEXTLIST=100, GTPEXLEN=100, GTPVER=GTPv2, POOLSRCPORTSW=ON, PEERRECOVERYSW=OFF, PATHDOWNDEASW=OFF, PATHVERDETECTSW=ON, DNSGTPCPATHFILTERSW=ON, LOCRECOVERYSW=ON, UDPCHKSW=ON;
        ```
   * 当需要将Sv接口与其他接口分离部署时，配置Sv接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
     1. 配置MME在Sv接口的GTPC IP。

        ```
        ADD GTPCLE: GROUPID=1, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.10.1.3",VPNNAME="VPN_SIG";
        ```
     2. 配置GTP路径管理参数。

        ```
        SET UGTP:ICI=180,SSI=60,MSI=60,PATHVERCHKINT=60; 
        SET GTPPUB: PRVEXT=OFF, ECHOSIG=ALL, OTSIE=DENY, POTHD=85, PNTHD=80, PCTHD=95, PRTHD=90, PEID=2011, PE="USN", GTPEXT=10, GTPSUPEXTLIST=100, GTPEXLEN=100, GTPVER=GTPv2, POOLSRCPORTSW=ON, PEERRECOVERYSW=OFF, PATHDOWNDEASW=OFF, PATHVERDETECTSW=ON, DNSGTPCPATHFILTERSW=ON, LOCRECOVERYSW=ON, UDPCHKSW=ON;
        ```
     3. 配置GTPC接口属性。

        ```
        ADD GTPCINTFATTR: SUBRANGE=ALL_USER,INTFTP=SV,GRPID=1;
        ```
   * **可选：**配置Sv接口GTP路径白名单功能。

     ****ADD GTPCWHITELIST****

     如果MME与MSC存在不能互通的本端IP和对端IP地址，当SRVCC流程中选择了此类本、对端IP地址对时，SRVCC流程会失败。为保证此种组网下SRVCC流程成功，需要执行本步骤，指定Sv接口允许使用的GTP-C路径，可保证SRVCC流程成功。配置Sv接口GTP路径白名单功能后，本端IP地址选择如下：
     + 如果对端IP地址落入Sv接口GTP路径白名单范围内，只能选择对应白名单内的GTP路径。
     + 如果对端IP地址不在Sv接口GTP路径白名单范围内：

       - 若配置了Sv接口IP地址分离功能（执行了Sv接口与其他接口分离部署），则从Sv接口IP地址分离的配置中随机选择一个本端IP地址。
       - 若未配置Sv接口IP地址分离功能，则从3.a配置组号的GTP-C IP中随机选择一个本端IP地址。
4. **可选：**配置DNS服务器的数据。

   如果现网已经完成DNS服务器的数据配置，则无需执行本步骤。

   **ADD DNSLE**命令中：
   * 配置了GTP-C IP的UNC必须同时配置DNS客户端IP才能进行相关的业务。
   * 此IP地址为UNC中定义的IP地址。
5. 配置MSC解析数据。
   1. 设置MSC域名解析策略。

      ```
      SET MSCSELPLCY: DNSPLCY=LAI;
      ```
   2. **可选：**增加位置区域DNS域名。

      当网络中存在连续的位置区和MSC对应时，建议执行本命令，简化域名配置。

      ****ADD AREADNS****
   3. 配置Hostfile记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=1, HOSTNAME="topon.sv.eth7.mnc001.mcc123.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.22.133.145", IPV4ADDR2="10.22.133.146";
      ADD DNSN: FQDN="LAC5101.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=MSC, INTYPE=Sv;
      ```

## 验证方法

1. 检查GTPC路径对端状态。

   进入“MML命令行-UNC”窗口。

   **TST GTPCPATH**

   * **预期结果：**对端可达。

     ```
     %%TST GTPCPATH: GTPVER=GTPv2, IPTYPE=IPV4, LOCIPV4ADDR="10.10.1.3", PEERIPV4ADDR="10.22.133.145";%% 
     RETCODE = 0  操作成功  

     操作结果如下: 
     ------------------------- 
     本端IPv4地址  =  10.10.1.3 
     对端IPv4地址  =  10.22.133.145    
        GTP版本  =  GTPv2 
     (结果数目 = 1)  
     ---    END
     ```
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
2. 验证SRVCC业务。

   进行业务测试前，需要首先完成MME与MSC的链路配置。

   进行业务测试的终端具备SRVCC功能。

   1. 创建用户跟踪。
   2. 创建S1-MME接口跟踪。
   3. 创建GTPC跟踪。
   4. 被测UE发起IMS语音业务。

      被测UE在IMS语音通话过程中从E-UTRAN覆盖区向UTRAN覆盖区移动，触发Handover流程指示进行SRVCC业务。

      预期结果：UE成功进行SRVCC业务。

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

版权所有 © 华为技术有限公司
