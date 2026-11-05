# 配置到S4 SGSN的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增S4 SGSN或MME时，在配置完成MME到S4 SGSN的路由数据后，可通过配置S3接口数据建立MME到S4 SGSN的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81202714 LKV2V6IF01 逻辑接口支持IPv6”。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

**表1** S3接口准备的数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD SERVICEIP** | IP版本（IPVERSION） | IPv4 | 整网规划。 | 配置S3接口业务IP。 |
|  | 业务IPv4地址（SERVICEIPV4） | 192.168.140.17 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |
| **ADD GTPCLE** | 组号（GROUPID） | 0 |  | 配置MME上的S3接口业务IP。 |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |
|  | IPv4地址（LEIPV4） | 192.168.140.17 |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |
| **SET UGTP** | 空闲计数器扫描间隔（秒）（ICI） | 180 |  | 配置GTP路径管理参数。 |
|  | SM信令路径空闲计数器（SSI） | 60 |  |  |
|  | MM信令路径空闲计数器（MSI） | 60 |  |  |
|  | GTPMAP路径空闲计数器（GMSI） | 60 |  |  |
|  | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60 |  |  |
| **SET GTPPUB** | 发送ECHO Request的路径（ECHOSIG） | ALL |  | 配置GTP路径管理参数。 |
|  | 发送GTPv2 Echo请求间隔（s）（V2EI） | 239 |  |  |
|  | 乱序信元（OTSIE） | DENY |  |  |
|  | 路径数过载门限（%）（POTHD） | 85 |  |  |
|  | 路径数过载恢复（%）（PNTHD） | 80 |  |  |
|  | 路径数拥塞门限（%）（PCTHD） | 95 |  |  |
|  | 路径数拥塞恢复（%）（PRTHD） | 90 |  |  |
|  | 检查GTP扩展头类型个数上限（GTPEXT） | 10 |  |  |
|  | 检查GTP扩展头类型长度上限（GTPEXLEN） | 100 |  |  |
|  | 本端可处理的请求消息的最高GTP版本（GTPVER） | GTPv2 |  |  |
| **ADD IPV4DNSH** | 主机名索引（HSINDEX） | 1 |  | 配置S4 SGSN解析数据。 |
|  | 主机名（HOSTNAME） | topon.s3.eth6.mnc001.mcc308.gprs |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPv4地址1（IPV4ADDR1） | 10.80.47.1 |  |  |
| **ADD DNSN** | FQDN（FQDN） | RAC002B.LAC02D9.RAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG |  | 配置S4 SGSN解析数据。 |
|  | 主机名索引（HSINDEX） | 1 |  |  |
|  | 网元类型（ENTITY） | SGSN |  |  |
|  | 接口类型（INTYPE） | S3 |  |  |
|  | 优先级（PRIORITY） | 10 |  |  |
|  | 权重（WEIGHT） | 104 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S3接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_SIG";
   ```
3. 配置GTP数据。

   1. 配置MME上的S3接口业务IP。

      ```
      ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.17",VPNNAME="VPN_SIG";
      ```
   2. 配置GTP路径管理参数。

      ```
      SET UGTP:  ICI=180, SSI=60, MSI=60, GMSI=60, PATHVERCHKINT=60;
      SET GTPPUB: ECHOSIG=ALL, V2EI=239, OTSIE=DENY, POTHD=85, PNTHD=80, PCTHD=95, PRTHD=90, GTPEXT=10, GTPEXLEN=100, GTPVER=GTPv2;
      ```
4. 配置S4 SGSN解析数据。

   ```
   ADD IPV4DNSH: HSINDEX=1, HOSTNAME="topon.s3.eth6.mnc001.mcc308.gprs", ADDRSECTION=SECTION1, IPV4ADDR1="10.80.47.1";
   ADD DNSN: FQDN="RAC002B.LAC02D9.RAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGSN, INTYPE=S3, PRIORITY=10, WEIGHT=104;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查GTPC GTP路径对端是否可达。

   **TST GTPCPATH**

   * **预期结果：**对端可达。

     ```
     %%TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.140.17", PEERIPV4ADDR="10.80.47.1";%%
     RETCODE = 0  操作成功

     操作结果如下:
     -------------------------
      本端IPv4地址  =  192.168.140.17
      对端IPv4地址  =  10.80.47.1
        GTP版本  =  GTPv1
     (结果数目 = 1)

     ---    END
     ```
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80610 GTPC路径故障**。
3. 进行业务测试。

   进行业务测试前，需要首先完成UNC与eNodeB、UDG、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确，并且两套UNC之间互通。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. 创建GTPC协议接口跟踪（S3、S4、S10、S11、S16、Gn、Gp）。

      参数选择如下：
      * IP地址类型：填入跟踪的IP类型。一般默认都是IPv4类型。
      * 本端IPv4/6地址：填本端IP地址。
      * 对端IPv4/6地址：填对端MME的IP。
      * 其它参数：选择默认值。
   3. 用户开机在本端附着，然后进行Inter MME的切换以触发Handover流程。
   4. 查看S3接口跟踪结果。
      * **预期结果：**可以在Message Direction处看到MME与S4 SGSN之间有消息交互。

        如果是MME和S4 SGSN之间的Inter切换流程，应该存在Forward Relocation交互流程。S4 SGSN与MME之间Forward Relocation Response消息协议类型是GTPv2，cause信元为request accepted。
      * **异常结果：**观察不到MME和S4 SGSN之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。
      * **预期结果：**用户切换成功，可以在Message Direction处看到MME与S4 SGSN之间有消息交互，如图1所示。

        **图1** 用户跟踪-Inter Handover流程（样例）

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**观察不到MME与S4 SGSN之间有消息交互。或观察到MME与S4 SGSN之间的消息异常。

版权所有 © 华为技术有限公司
