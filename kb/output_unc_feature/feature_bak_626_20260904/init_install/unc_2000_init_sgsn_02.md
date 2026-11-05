# 配置到RNC的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增RNC或SGSN时，在配置完成SGSN到RNC的路由数据后，可通过配置Iu接口数据建立SGSN到RNC的逻辑连接。

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

| 类别            | 参数名称                      | 取值样例                                                    | 获取方法            | 说明           |
|:--------------|:--------------------------|:--------------------------------------------------------|:----------------|:-------------|
| SET SIGATTR   | 国际网标志（IF）                 | INVALID                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | 国际备用网标志（IRF）              | INVALID                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | 国内网标志（NF）                 | LABEL24                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | 国内备用网标志（NRF）              | LABEL14                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | M3UA STP功能（M3UASTPF）      | DISABLE                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | 是否支持BSSAP+（BSSAPPF）       | DISABLE                                                 | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | BSSAP+子系统号（BSSAPPNO）      | 252                                                     | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | BSSAP+所在信令网（BSSAPPNI）     | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | MAP所在信令网（MAPNI）           | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| SET SIGATTR   | 信令网协议类型（SS7T）             | ITUT_SS7                                                | 参见“水平网设LLD文档 ”。 | 配置信令网属性。     |
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                                                    | 参见“水平网设LLD文档 ”。 | 配置Iu接口业务IP。  |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.29.147.113、10.29.147.116、10.29.147.121、10.29.147.124 | 参见“水平网设LLD文档 ”。 | 配置Iu接口业务IP。  |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_Access                                              | 参见“水平网设LLD文档 ”。 | 配置Iu接口业务IP。  |
| ADD M3LE      | 本地实体索引（LEX）               | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LE      | 网络指示语（NI）                 | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LE      | 本地实体编码（OPC）               | 0x1065                                                  | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LE      | 本地实体类型（LET）               | IPSP                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LE      | 本地实体名（LEN）                | SGSN_Iu-C                                               | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 目的实体索引（DEX）               | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 本地实体索引（LEX）               | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 目的实体编码（DPC）               | 0x1094                                                  | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 链路集选择掩码（SLSSM）            | B0000                                                   | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 目的实体类型（DET）               | IPSP                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 相邻标记（ADJF）                | TRUE                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | M3UA协议版本（PVER）            | RFC3332                                                 | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3DE      | 目的实体名（DEN）                | RNC                                                     | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 链路集索引（LSX）                | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 目的实体索引（DEX）               | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 链路选择掩码（SLSM）              | B0001                                                   | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 工作模式（WM）                  | IPSP                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 业务模式（TM）                  | LOADSHARE                                               | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LKS     | 链路集名（LSN）                 | To RNC                                                  | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3RT      | 路由索引（RTX）                 | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3RT      | 目的实体索引（DEX）               | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3RT      | 链路集索引（LSX）                | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3RT      | 优先级（PRI）                  | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3RT      | 信令路由名（RTN）                | To RNC                                                  | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | sctppara1                                               | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 链路号（LNK）                  | 0、1                                                     | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | VPN名称（VPNNAME）            | VPN_Access                                              | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | IP类型（IPT）                 | IPV4                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 本地IPv4地址1（LOCIPV41）       | 10.29.147.113、10.29.147.121                             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 本地IPv4地址2（LOCIPV42）       | 10.29.147.116、10.29.147.124                             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 对端IP地址1（PEERIPV41）        | 10.29.139.141、10.29.139.205                             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 对端IP地址2（PEERIPV42）        | 10.29.139.141、10.29.139.205                             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 对端端口号（PEERPORT）           | 2905                                                    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | C/S模式（CS）                 | C                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 链路集索引（LSX）                | 10                                                      | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | SCTP 参数索引（SCTPINDX）       | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD M3LNK     | 链路名（LKN）                  | To RNC_0、To RNC_1                                       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。  |
| ADD SCCPOPC   | 本局信令点索引（OPX）              | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPOPC   | 网络指示语（NI）                 | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPOPC   | 本局信令点编码（OPC）              | 0x1065                                                  | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPOPC   | 信令点用途（SPN）                | IUONLY                                                  | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPOPC   | 本局信令点名（OPN）               | For Iu-C                                                | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPDPC   | 目的信令点索引（DPX）              | 4                                                       | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPDPC   | 本局信令点索引（OPX）              | 1                                                       | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPDPC   | 目的信令点编码（DPC）              | 0x1094                                                  | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPDPC   | 负荷分担类型（LDP）               | NOUSE                                                   | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPDPC   | 目的信令点名（DPN）               | RNC                                                     | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 子系统索引（SSNX）               | 1、2、5、6                                                 | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 子系统号（SSN）                 | RANAP、SCMG                                              | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 网络指示语（NI）                 | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 目的信令点编码（DPC）              | 0x1065、0x1094                                           | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 本局信令点编码（OPC）              | 0x1065                                                  | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD SCCPSSN   | 子系统名（SSNNAME）             | SGSN、RNC                                                | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。  |
| ADD RNC       | RNC索引（RNCX）               | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | RNC名（RNCN）                | shanghai_RNC                                            | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | 移动国家代码（RNCMCC）            | 460                                                     | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | 移动网号（RNCMNC）              | 00                                                      | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | RNC标识（RNCID）              | 3                                                       | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | 网络指示语（NI）                 | NAT                                                     | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | 信令点编码（SPC）                | 0x1094                                                  | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD RNC       | RNC的协议版本（RNCVER）          | R5                                                      | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD IUPAGING  | 位置区标识（LAI）                | 460001155                                               | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD IUPAGING  | 路由区编码（RAC）                | 0x01                                                    | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD IUPAGING  | RNC索引（RNCINDEX）           | 0                                                       | 参见“水平网设LLD文档 ”。 | 配置RNC相关信息。   |
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                                                    | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.29.147.131 10.29.147.134 10.29.147.141 10.29.147.144 | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_CN                                                  | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD GTPULE    | 组号（GROUPID）               | 32                                                      | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD GTPULE    | IP地址类型（IPTYPE）            | TPTADDR_TYPE_IPV4                                       | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD GTPULE    | IPv4地址（LEIPV4）            | 10.29.147.131 10.29.147.134 10.29.147.141 10.29.147.144 | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |
| ADD GTPULE    | VPN名称（VPNNAME）            | VPN_CN                                                  | 参见“水平网设LLD文档 ”。 | 配置Iu接口用户面通道。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置本局信令属性。

   ```
   SET SIGATTR: IF=INVALID, IRF=INVALID, NF=LABEL24, NRF=LABEL14, M3UASTPF=DISABLE, BSSAPPF=DISABLE, BSSAPPNO=252, BSSAPPNI=NAT, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
3. 配置Iu接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.113", VPNINSTNAME="VPN_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.116", VPNINSTNAME="VPN_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.121", VPNINSTNAME="VPN_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.124", VPNINSTNAME="VPN_Access";
   ```
4. **可选：**配置M3UA信令数据。

   1. 配置M3UA本地实体。

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x1065", LET=IPSP, LEN="SGSN_Iu-C";
      ```
   2. 配置M3UA目的实体。

      ```
      ADD M3DE: DEX=10, LEX=0, DPC="0x1094", SLSSM=B0000, DET=IPSP, ADJF=TRUE, PVER=RFC3332, DEN="RNC";
      ```
   3. 配置M3UA信令链路集。

      ```
      ADD M3LKS: LSX=10, DEX=10, SLSM=B0001, WM=IPSP, TM=LOADSHARE, LSN="To RNC";
      ```
   4. 配置M3UA路由。

      ```
      ADD M3RT: RTX=10, DEX=10, LSX=10, PRI=0, RTN="To RNC";
      ```
   5. 配置SCTP协议参数。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=1, SCTPPARANAME="sctppara1";
      ```
   6. 配置M3UA信令链路。

      ```
      ADD M3LNK:LNK=0,VPNNAME="VPN_Access",IPT=IPV4,LOCIPV41="10.29.147.113",LOCIPV42="10.29.147.116",PEERIPV41="10.29.139.141",PEERIPV42="10.29.139.205",PEERPORT=2905,CS=C,LSX=10,SCTPINDX=1,LKN="To RNC_0";
      ADD M3LNK:LNK=1,VPNNAME="VPN_Access",IPT=IPV4,LOCIPV41="10.29.147.121",LOCIPV42="10.29.147.124",PEERIPV41="10.29.139.205",PEERIPV42="10.29.139.141",PEERPORT=2905,CS=C,LSX=10,SCTPINDX=1,LKN="To RNC_1";
      ```
5. 配置SCCP信令数据。

   1. 配置SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=1, NI=NAT, OPC="0x1065", SPN=IUONLY, OPN="For Iu-C";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=4, OPX=1, DPC="0x1094", LDP=NOUSE, DPN="RNC";
      ```
   3. 配置本局SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=1, SSN=RANAP, NI=NAT, DPC="0x1065", OPC="0x1065", SSNNAME="SGSN";
      ADD SCCPSSN: SSNX=2, SSN=SCMG, NI=NAT, DPC="0x1065", OPC="0x1065", SSNNAME="SGSN";
      ```
   4. 配置SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=5, SSN=RANAP, NI=NAT, DPC="0x1094", OPC="0x1065", SSNNAME="RNC";
      ADD SCCPSSN: SSNX=6, SSN=SCMG, NI=NAT, DPC="0x1094", OPC="0x1065", SSNNAME="RNC";
      ```
6. 配置RNC相关信息。

   1. 配置RNC信息。

      ```
      ADD RNC: RNCX=0, RNCN="shanghai_RNC", RNCMCC="460", RNCMNC="00", RNCID=3, NI=NAT, SPC="0x1094", RNCVER=R5;
      ```
   2. 配置3G寻呼表。

      ```
      ADD IUPAGING: LAI="460001155", RAC="0x01", RNCINDEX=0;
      ```
7. 配置Iu接口用户面通道。
   1. 增加业务IP。

      ```
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.131", VPNINSTNAME="VPN_CN"; 
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.134", VPNINSTNAME="VPN_CN"; 
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.141", VPNINSTNAME="VPN_CN"; 
      ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.29.147.144", VPNINSTNAME="VPN_CN";
      ```
   2. 增加GTPU本地实体。

      ```
      ADD GTPULE: GROUPID=32, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.29.147.131", VPNNAME="VPN_CN"; 
      ADD GTPULE: GROUPID=32, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.29.147.134", VPNNAME="VPN_CN"; 
      ADD GTPULE: GROUPID=32, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.29.147.141", VPNNAME="VPN_CN"; 
      ADD GTPULE: GROUPID=32, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.29.147.144", VPNNAME="VPN_CN";
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查M3UA链路的状态。

   **DSP M3LNK**
   - **预期结果：**“链路状态”字段为“激活”。

     ```
     %%DSP M3LNK: SRT=LINK, RUNAME="USN_VSU1", LNK=3;%%
     RETCODE = 0  操作成功。

     查询M3UA链路状态
     ----------------
       RU名称  = USN_VSU1
       链路号  =  3
       进程号  =  3
     链路状态  =  激活
       偶联ID  =  157
     是否锁定  =  否
     手工去活  =  否
     手工释放  =  否
     链路拥塞  =  否
     入流数目  =  17
     出流数目  =  17
          SLS  =  01 03 05 07 09 0B 0D 0F
     (结果个数 = 1)
     ---    END
     ```
   - **异常结果：**“链路状态”字段不为“激活”。

     异常处理过程参见ALM-80633 M3UA链路故障。
3. 检查M3UA路由的状态。

   **DSP M3RT**

   - **预期结果：**“路由状态”字段为“可用”

     ```
     %%DSP M3RT: RTX=0;%%
     RETCODE = 0  操作成功。

     查询M3UA路由状态
     ----------------
              路由索引  =  0
          目的实体索引  =  0
            链路集索引  =  0
              路由状态  =  可用
     SG和SEP间路由禁止  =  否
     SG和SEP间路由受限  =  否
          链路集不可用  =  否
                   SLS  =  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
     (结果个数 = 1)
     ---    END
     ```
   - **异常结果：**“路由状态”字段不为“可用”。

     异常处理过程参见ALM-10336 M3UA路由不可用。
4. 检查M3UA目的信令点的状态。

   **DSP M3DE**
   - **预期结果：**“是否可达”字段为“是”。

     ```
     %%DSP M3DE: DEX=1;%%
     RETCODE = 0  操作成功。

     查询M3UA目的实体状态
     --------------------
     目的实体索引  =  1
       网络指示语  =  国内备用网
     目的实体编码  =  0x601
     本地实体编码  =  0x2
         是否可达  =  是
         是否拥塞  =  否
     (结果个数 = 1)
     ---    END
     ```
   - **异常结果：**“是否可达”字段为“否”。

     异常处理过程参见ALM-10337 M3UA目的实体不可达。
5. 检查SCCP目的信令点状态。

   **DSP SCCPDPC**
   - **预期结果：**“信令点状态”字段为“允许”。

     ```
     %%DSP SCCPDPC: DPX=1;%%
     RETCODE = 0  操作成功。

     查询SCCP目的信令点状态
     ----------------------
         目的信令点索引  =  1
             网络指示语  =  国内备用网
         目的信令点编码  =  0x18101
         本局信令点编码  =  0x308401
         目的信令点状态  =  允许
     负荷分担信令点状态  =  允许
         备用信令点状态  =  NULL
               SCCP状态  =  允许
               拥塞状态  =  非拥塞
     (结果个数 = 1)
     ---    END
     ```
   - **异常结果：**“信令点状态”字段为“禁止”。

     异常处理过程参见ALM-10341 SCCP目的信令点不可达。
6. 检查RNC SCCP子系统的状态。

   **DSP SCCPSSN**
   - **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN:;%%
     RETCODE = 0  操作成功。

     查询SCCP子系统状态
     ------------------
      子系统索引  子系统号    网络指示语  目的信令点编码  本局信令点编码  子系统状态  是否测试标志  测试忽略标志

      0           SCMG(1)     国内备用网  0x2301          0x2301          允许        否            否          
      1           RANAP(142)  国内备用网  0x2301          0x2301          允许        否            否          
      375         SCMG(1)     国内备用网  0x3373          0x2301          允许        否            否          
      376         RANAP(142)  国内备用网  0x3373          0x2301          允许        否            否          
      (结果个数 = 4)
     ---    END
     ```
   - **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。
7. 检查到指定RNC用户面的通信情况。

   **TST GTPUPATH**
   - **预期结果：**执行结果显示GTP路径版本。

     ```
     %%TST GTPUPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="10.2.9.20", PEERIPV4ADDR="10.2.14.20";%%
     RETCODE = 0  操作成功。

     操作结果如下
     -------------------------
     本端IP地址  =  10.2.9.20
     对端IP地址  =  10.2.14.20
        GTP版本  =  GTPv1
     (结果数目 = 1)
     ---    END
     ```
   - **异常结果：**执行结果显示探测失败或执行超时。

     异常处理过程参见ALM-10342 SCCP子系统禁止。
8. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成SGSN与HLR、GGSN的对接。

   1. 创建用户跟踪。

      参数选择如下：

      - IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      - 其它参数：选择默认值。
   2. **可选：**创建Iu接口跟踪。

      参数选择如下：
      - Ru名称：资源单元的名称。
      - 进程序号：虚拟机内，SGP进程的同类进程序号。
      - RNC索引：对接RNC的索引。

        **LST RNC**
      - 其它参数：选择默认值。
   3. 用户在测试RNC下开机附着。
   4. 查看跟踪结果。
      - **预期结果：**可以观察到正常的附着消息流程，并且SGSN向手机下发Attach Accept消息，指示附着成功，如图1所示。

        **图1** 用户跟踪-附着（样例）
      - **异常结果：**用户附着失败。
   5. 查询用户MM上下文。

      **DSP COMMMCTX**
      - **预期结果：**可以查询到用户的MM上下文，并且状态为PMM-IDLE或PMM-CONNECTED状态。
      - **异常结果：**查询不到用户的MM上下文。
   6. 用户用手机浏览网页。
   7. 查看跟踪结果。
      - **预期结果：**可以观察到正常的激活消息流程，并且SGSN向手机下发Activate PDP Context Request消息，指示激活成功，如下图所示。

        **图2** 用户跟踪-激活（样例）
      - **异常结果：**用户激活失败。

      **说明** 

      此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
   8. 查询用户PDP上下文。

      **DSP SMCTX**
      - **预期结果：**可以查询到用户的PDP上下文。
      - **异常结果：**查询不到用户的PDP上下文。