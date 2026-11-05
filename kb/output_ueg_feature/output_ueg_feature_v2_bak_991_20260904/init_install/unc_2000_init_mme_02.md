# 配置S1-MME接口数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增eNodeB或MME时，在配置完成MME到eNodeB的路由数据后，可通过配置S1-MME接口数据建立MME到eNodeB的逻辑连接。

S1-MME接口是eNodeB和MME之间的控制面接口，S1-MME接口的信令连接功能为无线网络信令提供可靠的传输。

**图1** S1-MME接口协议栈  

**说明** 

- S1-AP (S1 Application Protocol)：eNodeB与MME之间的应用层协议。
- SCTP：此协议用于保证eNodeB与MME之间的信令消息传送。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

**说明** 

建议在eNodeB和Router之间部署外置IPsec网关。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- 已完成组网路由配置。
- 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
- 已经获取网设LLD文档。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别             | 参数名称                      | DC1取值样例                     | DC2取值样例                     | 获取方法            | 说明                                                                                                                                                                   |
|:---------------|:--------------------------|:----------------------------|:----------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP  | IP版本（IPVERSION）           | IPv4                        | IPv4                        | 参见“水平网设LLD文档 ”。 | 配置S1-MME接口的业务IP参数。                                                                                                                                                   |
| ADD SERVICEIP  | 业务IPv4地址（SERVICEIPV4）     | 10.254.140.15 10.254.140.16 | 10.254.140.17 10.254.140.18 | 参见“水平网设LLD文档 ”。 | 由于S1-MME接口传输层的SCTP协议支持多连接，且同一连接也存在多路径，可以配置多个业务IP地址支持多条链路，此处以两个业务IP地址为例。                                                                                              |
| ADD SERVICEIP  | VPN实例名称（VPNINSTNAME）      | VPN_Access                  | VPN_Access                  | 参见“水平网设LLD文档 ”。 | UEG风筝形态对外接口组网时，需运营商统一规划IP，VPN。                                                                                                                                       |
| ADD CPSCTPPARA | SCTP协议参数索引（SCTPPARAINDEX） | 1                           | 1                           | 参见“水平网设LLD文档 ”。 | 用于配置SCTP协议参数。S1–MME接口的SCTP协议参数与S6a接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                          |
| ADD CPSCTPPARA | SCTP协议参数名（SCTPPARANAME）   | For_S1AP                    | For_S1AP                    | 参见“水平网设LLD文档 ”。 | 用于配置SCTP协议参数。S1–MME接口的SCTP协议参数与S6a接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                          |
| ADD S1APLE     | 链路本地实体号（LLEINDEX）         | 1                           | 1                           | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE     | 本地IPv4地址1（LOCALIPV4_1）    | 10.254.140.15               | 10.254.140.17               | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE     | 本地IPv4地址2（LOCALIPV4_2）    | 10.254.140.16               | 10.254.140.18               | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE     | 本地端口号（LOCALPORT）          | 36412                       | 36412                       | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE     | SCTP协议参数索引（SCTPINDEX）     | 1                           | 1                           | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE     | VPN名称（VPNNAME）            | VPN_Access                  | VPN_Access                  | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。MME支持S1-MME接口采用的SCTP端口号可配置。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置S1-MME接口的业务IP。

   ```
   //DC1
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.254.140.15", VPNINSTNAME="VPN_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.254.140.16", VPNINSTNAME="VPN_Access";
   //DC2
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.254.140.17", VPNINSTNAME="VPN_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.254.140.18", VPNINSTNAME="VPN_Access";
   ```
3. 配置SCTP参数。

   ```
   //DC1
   ADD CPSCTPPARA:SCTPPARAINDEX=1,SCTPPARANAME="For_S1AP";
   //DC2
   ADD CPSCTPPARA:SCTPPARAINDEX=1,SCTPPARANAME="For_S1AP";
   ```
4. 增加S1AP链路本地实体，其中LOCALIPV4\_1为S1-MME接口的业务IP。

   ```
   //DC1
   ADD S1APLE:LLEINDEX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.254.140.15",LOCALIPV4_2="10.254.140.16",CROSSIPFLAG=NO,SCTPINDEX=1,LLNAME="To-eNodeB",VPNNAME="VPN_Access";
   //DC2
   ADD S1APLE:LLEINDEX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.254.140.17",LOCALIPV4_2="10.254.140.18",CROSSIPFLAG=NO,SCTPINDEX=1,LLNAME="To-eNodeB",VPNNAME="VPN_Access";
   ```

## 验证方法

1. 检查到eNodeB之间的链路状态。

   进入“MML命令行-UEG”窗口。

   执行****DSP S1APLNK****:;

   - **预期结果：**“链路状态”为“正常”，此处以IPv4为例。

     ```
     %%DSP S1APLNK:;%%
     RETCODE = 0  操作成功。

     操作结果如下
     ------------
     移动国家码    移动网号    IP地址类型1    eNodeB IP地址1    IP地址类型2    eNodeB IP地址2    eNodeB端口号    eNodeB类型    eNodeB标识    链路状态    S1AP本端实体标识    进程号    进程类型    RU名称            eNodeB名称    链路闪断次数

     460           03          IPv4地址       10.27.32.1       NULL           NULL              2012            MACRO_ENB     204818        正常        0                   4         SGP         LINK_SP_RU_0064    NONAME        0           
     460           03          IPv4地址       10.27.32.1       NULL           NULL              2011            MACRO_ENB     204817        正常        0                   0         SGP         LINK_SP_RU_0064    NONAME        0           
     (结果个数 = 2)
     ---    END
     ```
   - **异常结果：**“链路状态”为“故障”。

     异常处理过程参见**ALM-80589 S1ap链路故障**。
2. 进行业务测试。

   1. 创建用户跟踪任务。
   2. **可选：**创建S1接口跟踪。
   3. 用户开机附着。
   4. **可选：**查看S1接口跟踪结果。
      - **预期结果：**可以在Message Direction处看到MME和eNodeB之间有消息交互。

        如果打开安全开关的话，在Initial Context Setup消息之前应该存在两次Downlink NAS Transport和Uplink NAS Transport消息。
      - **异常结果：**观察不到MME与eNodeB之间的消息或观察到的消息异常。
   5. 查看用户跟踪结果。
      - **预期结果：**用户附着成功，可以在Message Direction处看到MM模块与S1AP模块之间、S1AP模块与S1APADP模块之间、S1APADP模块与SCTP模块之间有消息交互。

        **说明** 

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      - **异常结果：**观察不到MM模块与S1AP模块之间、S1AP模块与S1APADP模块之间、S1APADP模块与SCTP模块之间的消息。或观察到MM模块与S1AP模块之间、S1AP模块与S1APADP模块之间、S1APADP模块与SCTP模块之间的消息异常。