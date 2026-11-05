# 配置到eNodeB的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增eNodeB或MME时，在配置完成MME到eNodeB的路由数据后，可通过配置S1-MME接口数据建立MME到eNodeB的逻辑连接。

**说明** 

建议在eNodeB和Router之间部署外置IPsec网关。

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

| 类别            | 参数名称                      | 取值样例          | 获取方法            | 说明                                                                                                                                                                   |
|:--------------|:--------------------------|:--------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4          | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                            |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.254.140.17 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                            |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VRF_Access    | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                            |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 1             | 参见“水平网设LLD文档 ”。 | 用于配置SCTP协议参数。S1–MME接口的SCTP协议参数与S6a接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                          |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | For_S1AP      | 参见“水平网设LLD文档 ”。 | 用于配置SCTP协议参数。S1–MME接口的SCTP协议参数与S6a接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                          |
| ADD S1APLE    | 链路本地实体号（LLEINDEX）         | 1             | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。UNC支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE    | 本地IPv4地址1（LOCALIPV4_1）    | 10.254.140.17 | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。UNC支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE    | 本地端口号（LOCALPORT）          | 36412         | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。UNC支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE    | SCTP协议参数索引（SCTPINDEX）     | 1             | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。UNC支持S1-MME接口采用的SCTP端口号可配置。 |
| ADD S1APLE    | VPN名称（VPNNAME）            | VRF_Access    | 参见“水平网设LLD文档 ”。 | 用于S1AP链路数据。在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。UNC支持S1-MME接口采用的SCTP端口号可配置。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S1-MME接口的业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.254.140.17", VPNINSTNAME="VRF_Access";
   ```
3. 配置SCTP参数。

   ```
   ADD SCTPPARA:SCTPPARAINDEX=1,SCTPPARANAME="For_S1AP";
   ```
4. 增加S1AP链路本地实体，其中LOCALIPV4\_1为S1-MME接口的业务IP。

   ```
   ADD S1APLE:LLEINDEX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.254.140.17",CROSSIPFLAG=NO,SCTPINDEX=1,LLNAME="To-eNodeB",VPNNAME="VRF_Access";
   ```

## 验证方法

1. 检查到eNodeB之间的链路状态。

   进入“MML命令行-UNC”窗口。

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

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2000上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      - **异常结果：**观察不到MM模块与S1AP模块之间、S1AP模块与S1APADP模块之间、S1APADP模块与SCTP模块之间的消息。或观察到MM模块与S1AP模块之间、S1AP模块与S1APADP模块之间、S1APADP模块与SCTP模块之间的消息异常。