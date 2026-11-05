# 配置到E-SMLC的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到E-SMLC的路由数据后，可通过配置SLs接口数据建立MME到E-SMLC的逻辑连接。

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
|  | 业务IPv4地址（SERVICEIPV4） | 10.11.11.11  10.11.11.12 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 0 |  | SLs接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。 |
|  | SCTP协议参数名（SCTPPARANAME） | For\_SLs |  |  |
| ****ADD ESMLC**** | E-SMLC标识（ESMLCID） | 1 |  | 配置指定E-SMLC在MME上的SCTP偶联信息。 |
|  | 优先级（PRIORITY） | 1 |  |  |
|  | E-SMLC名称（ESMLCNAME） | esmlc1.epc.mnc015.mcc123.3gppnetwork.org |  |  |
| ****ADD LCSAPLNK**** | 链路索引 （LINKIDX ） | 3 |  | 配置E-SMLC的链路信息。 |
|  | E-SMLC标识（ESMLCID） | 1 |  |  |
|  | IP地址类型（IPTYPE ） | IPV4 |  |  |
|  | 本地IPv4地址1 （LOCALIPV4\_1 ） | 10.11.11.11 |  |  |
|  | 本地IPv4地址2 （LOCALIPV4\_2 ） | 10.11.11.12 |  |  |
|  | 本端端口号 （LOCALPORT ） | 9082 |  |  |
|  | 对端IPv4地址1 （PEERIPV4\_1） | 10.2.3.4 |  |  |
|  | 对端IPv4地址2（PEERIPV4\_2 ） | 10.2.3.5 |  |  |
|  | 对端端口号 （PEERPORT ） | 9082 |  |  |
|  | SCTP协议参数索引（SCTPINDX ） | 3 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置SLs接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.11.11", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.11.12", VPNINSTNAME="VPN_SIG";
   ```
3. 配置SLs接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   ADD SCTPPARA: SCTPPARAINDEX=0, SCTPPARANAME="For_SLs";
   ```
4. 配置指定E-SMLC在MME上的SCTP偶联信息。

   ```
   ADD ESMLC: ESMLCID=1, PRIORITY=1, ESMLCNAME="esmlc1.epc.mnc015.mcc123.3gppnetwork.org";
   ```
5. 配置E-SMLC的链路信息。

   ```
   ADD LCSAPLNK: LINKIDX=3, ESMLCID=1, IPTYPE=IPV4, LOCALIPV4_1="10.11.11.11", LOCALIPV4_2="10.11.11.12", LOCALPORT=9082, PEERIPV4_1="10.2.3.4", PEERIPV4_2="10.2.3.5", PEERPORT=9082, SCTPINDX=3;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查MME与对端网元的路由是否正常。

   ****PING****: IPVERSION=IPv4, DESTIPV4ADDRESS=目的IPv4地址;

   **PING**: IPVERSION=IPv6, DESTIPV6ADDRESS=目的IPv6地址;

   * **预期结果：**正常情况下会看到响应报文，并且报文中有成功收发包的个数。
   * **异常结果：**无法收到对端的响应报文。

     根据对端网元与本端网元间路由的类型，**参见调测静态路由（IPv4）、调测动态路由（IPv4）、调测静态路由（IPv6）**或**调测动态路由（IPv6）**。
3. 检查到E-SMLC之间的链路状态。

   **DSP ESMLCSTATE**: ESMLCID="E-SMLC 标识";

   * **预期结果：**与ESMLC之间的链路状态为“NORMAL（稳态）”。

     ```
     %%DSP ESMLCSTATE: ESMLCID=1;%%
     RETCODE = 0  操作成功。

     输出结果如下
     --------------
           E-SMLC 标识  =  1
           E-SMLC 状态  =  稳态
         E-SMLC 优先级  =  3
     E-SMLC 定位用户数  =  30
                链路数  =  3
     仍有后续报告输出
     ---    END

     %%DSP ESMLCSTATE: ESMLCID=1;%%
     RETCODE = 0  操作成功。

     输出结果如下
     --------------
     链路索引            RU名称            进程号      链路状态

     3                   USN_SP_RU_0064    0           稳态
     (结果个数 = 2)
     共有2个报告
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80676 LCSAP链路故障**。
4. 进行业务测试。

   进行业务测试前，需要首先完成UNC与eNodeB、GMLC、E-SMLC的链路配置。

   1. **创建用户跟踪任务**。

      参数选择如下：
      * IMSI/MSISDN/用户索引号：被跟踪用户的IMSI、MSISDN或者用户索引号。
      * 其他参数：选择默认值。
   2. 创建SLs接口跟踪。

      参数选择如下：

      链路号：LCSAP链路号。
   3. 用户开机，进行附着。
   4. GMLC发起LCS定位请求。
   5. 查看SLs接口跟踪结果。

      * **预期结果：**可以看到Location Request和Location Response消息。
      * 异常结果：观察不到SLs接口跟踪消息或观察到的消息异常。
   6. 查看用户跟踪结果。

      * **预期结果：**用户附着成功，可以在消息方向处看到LCS模块与LCSAP模块之间有消息交互。
      * **异常结果：**观察不到LCS模块与UDM模块之间的消息或观察到的消息异常。

版权所有 © 华为技术有限公司
