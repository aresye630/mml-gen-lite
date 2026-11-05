# 配置到CBC的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到CBC的路由数据后，可通过配置SBc接口数据建立MME到CBC的逻辑连接。

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

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.1.1.1  10.1.1.2 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 1 |  | SBc接口的SCTP协议参数与S1接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。 |
|  | SCTP协议参数名（SCTPPARANAME） | For\_SBc-AP |  |  |
| ****ADD CBC**** | CBC索引（CBCIDX） | 0 |  | 增加CBC配置（假设有两个CBC IP）。 |
|  | CBC归属的MCC（MCC） | 123 |  |  |
|  | CBC归属的MNC（MNC） | 03 |  |  |
|  | IP地址类型（IPTYPE） | IPV4 |  |  |
|  | CBC IPv4地址1（IPV4\_1） | 10.2.3.4 |  |  |
|  | CBC IPv4地址2（IPV4\_2） | 10.2.3.5 |  |  |
|  | CBC名称（CBCNAME） | CBC1 |  |  |
| ****ADD SBCAPLE**** | 本端实体号（LLEINDEX） | 0 |  | 用户可根据需要将MME配置成服务器端或客户端，当存在与多个CBC连接时，也可将MME同时配置成服务器端和客户端。  当MME作为客户端时，配置对端IP必须在CBC配置表中存在，链接才会建立。 |
|  | IP地址类型（IPTYPE） | IPV4 |  |  |
|  | 本地IPv4地址1（LOCALIPV4\_1） | 10.1.1.1 |  |  |
|  | 本地IPv4地址2（LOCALIPV4\_2） | 10.1.1.2 |  |  |
|  | 本地端口号（LOCALPORT） | 29168 |  |  |
|  | 交叉路径是否可用（CROSSIPFLAG） | NO |  |  |
|  | SCTP协议参数索引（SCTPINDX） | 1 |  |  |
|  | 本端实体名称（LLENAM） | toCBC1 |  |  |
| ****ADD SBCAPLNK**** | 链路索引（LNKINDEX） | 0 |  | 用户可根据需要将MME配置成服务器端或客户端，当存在与多个CBC连接时，也可将MME同时配置成服务器端和客户端。  当MME作为客户端时，配置对端IP必须在CBC配置表中存在，链接才会建立。 |
|  | IP地址类型（IPTYPE） | IPV4 |  |  |
|  | 本地IPv4地址1（LOCALIPV4\_1） | 10.1.1.1 |  |  |
|  | 本地IPv4地址2（LOCALIPV4\_2） | 10.1.1.2 |  |  |
|  | 本地端口号（LOCALPORT） | 29168 |  |  |
|  | 对端IPv4地址1（PEERIPV4\_1） | 10.2.3.4 |  |  |
|  | 对端IPv4地址2（PEERIPV4\_2） | 10.2.3.5 |  |  |
|  | 对端端口号（PEERPORT） | 29168 |  |  |
|  | SCTP协议参数索引（SCTPINDX） | 1 |  |  |
|  | 交叉路径是否可用（CROSSIPFLAG） | NO |  |  |
|  | 链路名称（LINKNAM） | SBCAPLNK1 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置SBc接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.1.1.1", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.1.1.2", VPNINSTNAME="VPN_SIG";
   ```
3. 配置SBc接口基于IP的宽带信令SCTP偶联协议参数。

   ```
   ADD SCTPPARA: SCTPPARAINDEX=1,SCTPPARANAME="For_SBc-AP";
   ```
4. 增加CBC配置。

   ```
   ADD CBC: CBCIDX=0, MCC="123", MNC="03", IPTYPE=IPV4, IPV4_1="10.2.3.4", IPV4_2="10.2.3.5", CBCNAME="CBC1";
   ```
5. 配置SBc-AP链路参数。

   * 当MME作为服务器端时，增加SBc链路本地实体，用于SBc链路建立。

     ```
     ADD SBCAPLE:  LLEINDEX=0, IPTYPE=IPV4, LOCALIPV4_1="10.1.1.1", LOCALIPV4_2="10.1.1.2", LOCALPORT=29168, CROSSIPFLAG=NO, SCTPINDX=1, LLENAM="toCBC1";
     ```
   * 当MME作为客户端时，增加一条SBc链路。

     ```
     ADD SBCAPLNK:  LNKINDEX=0, IPTYPE=IPV4, LOCALIPV4_1="10.1.1.1", LOCALIPV4_2="10.1.1.2", LOCALPORT=29168, PEERIPV4_1="10.2.3.4", PEERIPV4_2="10.2.3.5", PEERPORT=29168, SCTPINDX=1, CROSSIPFLAG=NO, LINKNAM="SBCAPLNK1";
     ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查MME与对端网元的路由是否正常。

   **PING**: IPVERSION=IPv4, DESTIPV4ADDRESS=目的IPv4地址;

   **PING**: IPVERSION=IPv6, DESTIPV6ADDRESS=目的IPv6地址;

   * **预期结果：**正常情况下会看到响应报文，并且报文中有成功收发包的个数。
   * **异常结果：**无法收到对端的响应报文。

     根据对端网元与本端网元间路由的类型，**参见调测静态路由（IPv4）、调测动态路由（IPv4）、调测静态路由（IPv6）**或**调测动态路由（IPv6）**。
3. 检查到CBC之间的链路状态。

   **DSP CBC**: CBCIDX="CBC索引";

   * **预期结果：**显示已经配置SBc链路的连接状态。

     ```
     %%DSP CBC: CBCIDX=0;%%
     RETCODE = 0  操作成功。

     输出结果如下：
     -------------------------
          CBC索引  =  0
           进程号  =  6
           RU名称  =  USN_SP_RU_0064
        IP地址类型  =  IPv4
         本地地址1  =  10.2.62.20
         本地地址2  =  255.255.255.255
        本地端口号  =  29168
         对端地址1  =  172.27.168.1
         对端地址2  =  255.255.255.255
        对端端口号  =  29168
           VPN名称  =  _public_
          链路状态  =  正常
     (结果个数 = 1)
     ```
   * **异常结果：**异常处理过程参见**ALM-80674 SBCAP链路故障**。
4. 进行业务测试。

   1. 创建SBc接口跟踪。
   2. 从CBC发起小区服务广播服务。

      **预期结果：**CBS流程中，SBc接口跟踪可以看到相应的Write-Replace Warning Request和Write-Replace Warning Response消息。

版权所有 © 华为技术有限公司
