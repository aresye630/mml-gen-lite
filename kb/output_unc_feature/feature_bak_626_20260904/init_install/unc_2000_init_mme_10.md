# 配置到MSC的数据（SGs接口）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC Server的路由数据后，可通过配置SGs接口数据建立MME到MSC Server的逻辑连接。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
- 当配置SGs链路时，MME仅作为客户端和MSC对接。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                      | 取值样例                                                      | 获取方法            | 说明                                                                                             |
|:--------------|:--------------------------|:----------------------------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPV4                                                      | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                      |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 192.168.140.1 192.168.140.17 192.168.140.2 192.168.140.18 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                      |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_SIG                                                   | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                      |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 0                                                         | 参见“水平网设LLD文档 ”。 | SGs接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。 |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | For_SGs                                                   | 参见“水平网设LLD文档 ”。 | SGs接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。 |
| ADD VLR       | VLR号（VN）                  | 111111111111111                                           | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLKS    | 链路集索引 （LSX ）              | 0                                                         | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLKS    | VLR号（VN）                  | 111111111111111                                           | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLKS    | 链路集名（LSN ）                | sgs1                                                      | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | 链路索引（LNK）                 | 0 1                                                       | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | VPN名称（VPNNAME）            | VPN_SIG                                                   | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | IP地址类型（IPTYPE）            | IPV4                                                      | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | VLR IPv4地址1（VLRIPV4_1）    | 10.80.47.4 10.80.47.5                                     | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | 本地IPv4地址1（LOCALIPV4_1）    | 192.168.140.1 192.168.140.2                               | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | 本地IPv4地址2（LOCALIPV4_2）    | 192.168.140.17 192.168.140.18                             | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | 链路集索引 （LSX ）              | 0                                                         | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD SGSLNK    | SCTP协议参数索引（SCTPINDX）      | 0                                                         | 参见“水平网设LLD文档 ”。 | 配置MME到指定MSC的SCTP偶联信息。                                                                          |
| ADD LAIVLR    | 起始LAI（BGNLAI）             | 308015101                                                 | 参见“水平网设LLD文档 ”。 | 添加LAI与VLR号对应关系。                                                                                |
| ADD LAIVLR    | VLR号（VLRNO）               | 111111111111111                                           | 参见“水平网设LLD文档 ”。 | 添加LAI与VLR号对应关系。                                                                                |
| ADD TAILAI    | 起始LAI（BGNLAI）             | 308015101                                                 | 参见“水平网设LLD文档 ”。 | 添加TAI与LAI的对应关系。                                                                                |
| ADD TAILAI    | 用户范围（SUBRANGE）            | ALL_USER                                                  | 参见“水平网设LLD文档 ”。 | 添加TAI与LAI的对应关系。                                                                                |
| ADD TAILAI    | LAI（LAI）                  | 308015101                                                 | 参见“水平网设LLD文档 ”。 | 添加TAI与LAI的对应关系。                                                                                |
| SET SGSPARA   | 位置更新定时器（TS6_1）            | 10                                                        | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | EPS分离定时器（TS8）             | 4                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | 显式IMSI分离定时器（TS9）          | 5                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | 隐式IMSI分离定时器（TS10）         | 5                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | EPS分离重发次数（NS8）            | 2                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | 显式IMSI分离重发次数（NS9）         | 2                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |
| SET SGSPARA   | 隐式IMSI分离重发次数（NS10）        | 3                                                         | 参见“水平网设LLD文档 ”。 | 设置SGs接口业务运行参数。                                                                                 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置SGs接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.1", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.2", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.18", VPNINSTNAME="VPN_SIG";
   ```
3. 配置SGs接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   ADD SCTPPARA:SCTPPARAINDEX=0,SCTPPARANAME="For_SGs";
   ```
4. 配置MME到指定MSC的SCTP偶联信息。

   ```
   ADD VLR:VN="111111111111111"; 
   ADD SGSLKS:LSX=0,VN="111111111111111",LSN="sgs1"; 
   ADD SGSLNK:LNK=0,VPNNAME="VPN_SIG",IPTYPE=IPV4,VLRIPV4_1="10.80.47.4",VLRIPV4_2="10.80.47.5",LOCALIPV4_1="192.168.140.1",LOCALIPV4_2="192.168.140.17",LSX=0,SCTPINDX=0; 
   ADD SGSLNK:LNK=1,VPNNAME="VPN_SIG",IPTYPE=IPV4,VLRIPV4_1="10.80.47.4",VLRIPV4_2="10.80.47.5",LOCALIPV4_1="192.168.140.2",LOCALIPV4_2="192.168.140.18",LSX=0,SCTPINDX=0;
   ```
5. 添加MSC覆盖的LA。

   ```
   ADD LAIVLR:BGNLAI="308015101",VLRNO="111111111111111";
   ```
6. 添加LA覆盖的TA范围。

   ```
   ADD TAILAI:BGNTAI="308015101",SUBRANGE=ALL_USER,LAI="308015101";
   ```
7. 设置SGs接口业务运行参数。

   ```
   SET SGSPARA:TS6_1=10,TS8=4,TS9=5,TS10=5,NS8=2,NS9=2,NS10=3;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 查询MME和MSC/VLR之间SCTP偶联状态是否正常。

   ****DSP SGSLNK****:VN=VLR号;

   - **预期结果：**显示到VLR链路状态信息为“正常”。

     ```
     %%DSP SGSLNK: SRT=VLR, VN="86139248";%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     RU名称            进程号    链路索引    链路集索引    VPN名称    VLR号       SGs链路状态  
     USN_SP_RU_0065    4         221         221           123        86139248    正常        
     USN_SP_RU_0064    1         476         221           123        86139248    正常        
     (结果个数 = 2) 
     ---    END
     ```

     **异常结果：**“SGs链路状态”字段不为“正常”。

     异常处理过程参见**ALM-14033 SGs口对端不可达**。
3. 业务测试。

   **说明** 

   - 进行业务测试前，需要首先完成MME与eNodeB、HSS的对接。
   - 进行业务测试的手机必须支持同时附着CS/EPS网络。

   1. 增加IMSI与MSC/VLR对应关系。

      进入“MML命令行-UNC”窗口。

      ****ADD IMSIVLR****:IMSI="123030000000001", VN="86139027";

      **说明** 

      假设用于拨测的用户的IMSI为"123030000000001"，待拨测MSC/VLR的VLR号为“86139027”。
   2. 创建用户跟踪任务。

      参数选择如下：

      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其他参数：选择默认值。
   3. 创建SGs接口跟踪。

      参数选择如下：

      VLR号：对端MSC提供的VLR号。
   4. 用户开机附着。
   5. 查看SGs接口跟踪结果。
      - **预期结果：**

        可以在Message Direction处看到MME和MSC/VLR之间、MM模块与SGsAP模块之间有消息交互，包括MM\_SGSAP\_LOCATION\_UPDATE\_REQ及SGSAP\_MM\_LOCATION\_UPDATE\_ACC。
      - **异常结果：**

        观察不到MME与MSC/VLR之间、MM模块与SGsAP模块之间的消息。
   6. 查看用户跟踪结果。

      **预期结果：**

      用户附着成功，可以在Message Direction处看到MME和MSC/VLR之间、MME与UE之间有消息交互，并且消息体中的ePS-attach-type为： combined-attach，ePS-attach-result为：combined-EPS-attach。

      **说明** 

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。

      - **异常结果：**

        观察消息体中的Attach result不是：combined-EPS-attach，而是：EPS attach。
   7. 查询用户MM上下文。

      进入“MML命令行-UNC”窗口。

      **DSP COMMMCTX**: QUERYOPT=BYIMSI, IMSI=IMSI;

      - **预期结果：**

        可以查询到用户的MM上下文，并且MM状态为ECM-CONNECT状态。可观察到用户的“SGs关联状态”为“关联已建立”、“VLR可靠性”为“可靠”。
      - **异常结果：**

        查询不到用户的MM上下文，“SGs关联状态”为“无关联”，“VLR可靠性”为“不可靠”。
   8. 删除IMSI与MSC/VLR对应关系。

      ****RMV IMSIVLR****:IMSI="123030000000001";