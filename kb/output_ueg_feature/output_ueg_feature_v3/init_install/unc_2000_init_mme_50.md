# 配置S11-U接口数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署NBIoT分组交换网，新增MME或SGW-U时，在配置完成MME到SGW-U的路由数据后，可通过配置S11-U接口数据建立MME到SGW-U的逻辑连接。

S11-U接口是MME与S-GW/SGW-U间的用户面接口，用于传递MME与S-GW/SGW-U间的上下行用户面数据，实现物联网业务。

S11-U接口协议栈如图1所示。

**图1** S11-U接口协议栈

GTP-U（GPRS Tunnelling Protocol for the user plane）：利用隧道协议在骨干网的GSN间传输用户数据，使用隧道协议传输数据，屏蔽上层协议影响，同时提供会话级的双向快速传输通道。GTP协议用户面除数据包外，还包括数据传输出错指示、Echo消息、支持的扩展头列表等用户面传输辅助信令。GTP-U版本为GTPv1。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 已完成组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 如需在UE在4G网络附着选择合一SGW-C/PGW-C，则需要开通“S-GW/P-GW 拓扑选择”特性，即加载对应的License项“82205919 LKV2SELGW03 S-GW/P-GW 拓扑选择”。
* 已经获取网设LLD文档。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。  S11-U和S11-C的VPN实例相同。 |
|  | 业务IPv4地址（SERVICEIPV4） | 192.168.140.20 | 192.168.140.21 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  |  |
| ****ADD GTPULE**** | 组号（GROUPID） | 0 |  |  | 配置本端的S11接口的GTP-U IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。 |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |  |
|  | IPv4地址（leIpv4） | 192.168.140.20 | 192.168.140.21 |  |  |
|  | VPN名称（vpnName） | VPN\_CN |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. **可选：**在NBIoT场景下，配置S11-U接口，用于MME与SGW-U传输用户面数据。

   1. 配置S11-U接口业务IP。

      ```
      //DC1
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.20", VPNINSTNAME="VRF_CN";
      //DC2
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.21", VPNINSTNAME="VRF_CN";
      ```
   2. 配置GTP数据。
      * 配置S11-U接口与其他接口共部署时，GTPU本端实体对应的组号配置为0。

        配置MME在S11-U接口的GTP-U IP。

        ```
        //DC1
        ADD GTPULE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.20",VPNNAME="VRF_CN";
        //DC2
        ADD GTPULE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.21",VPNNAME="VRF_CN";
        ```
      * 当需要将S11-U接口与其他接口分离部署时，配置S11-U接口分离。此时将GTPU本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。
        1. 配置MME在S11-U接口的GTP-U IP。

           ```
           //DC1
           ADD GTPULE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.20",VPNNAME="VRF_CN";
           //DC2
           ADD GTPULE: GROUPID=3, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.140.21",VPNNAME="VRF_IOT_CN";
           ```
        2. 配置GTPU接口属性。

           ```
           //DC1
           ADD GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=S11, GRPID=3;
           //DC2
           ADD GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=S11, GRPID=3;
           ```

## 验证方法

1. 进入“MML命令行-UEG”窗口。
2. 检查GTPU路径对端是否可达。

   查看MME上S11-U接口地址与对端SGW-U上S11-U接口地址间的路由连接是否正常。

   ```
   INNERPING: IPVERSION=IPv4, VPNNAME="VRF_CN", SOURCEIPV4ADDRESS="192.168.140.20", DESTIPV4ADDRESS="10.10.132.1", SERVICEINSTANCE="LINK_VNFC";
   ```

   如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。

   * 如果收到对端网元的响应且响应报文中有成功收发包的个数，表明连接正常，调测结束。
   * **异常结果：**对端不可达。

     异常处理过程参见**ALM-80661 GTPU路径故障**。
3. 进行业务测试。

   进行业务测试前，需要首先完成UNC与eNodeB、UEG、HSS的链路配置。

   其次进行业务测试时，需要保证DNS的配置正确。

   进行业务测试的手机必须是在对接的HSS开户的手机。

   1. 创建用户跟踪任务。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. **可选：**创建S11 GTPU协议接口跟踪。

      参数选择如下：
      * Ru名称：资源单元的名称。
      * 本端IPv4/6地址：填本端IP地址。
      * 对端IPv4/6地址：填对端SGW-U的IP。
      * 其它参数：选择默认值。
   3. 用户开机附着。
   4. **可选：**查看S11-U接口跟踪结果。
      * **预期结果：**可以在跟踪包中看到MME和SGW-U之间有用户数据包。
      * **异常结果：**观察不到MME与SGW-U之间的用户数据包。

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

版权所有 © 华为技术有限公司
