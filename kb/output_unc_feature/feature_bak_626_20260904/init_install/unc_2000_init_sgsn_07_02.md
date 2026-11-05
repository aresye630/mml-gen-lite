# 配置到SMC的数据（SG Over IP）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增SMC或SGSN时，在配置完成SGSN到SMC的路由数据后，可通过配置SG与SMC建立逻辑连接。

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

| 类别            | 参数名称                      | 取值样例          | 取值样例.1        | 获取方法            | 说明          |
|:--------------|:--------------------------|:--------------|:--------------|:----------------|:------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4          | IPv4          | 参见“水平网设LLD文档 ”。 | 增加业务IP。     |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.11.95.5    | 10.11.95.5    | 参见“水平网设LLD文档 ”。 | 增加业务IP。     |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_SIG       | VPN_SIG       | 参见“水平网设LLD文档 ”。 | 增加业务IP。     |
| SET SIGATTR   | 国际网标志（IF）                 | LABEL24       | LABEL24       | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | 国际备用网标志（IRF）              | LABEL14       | LABEL14       | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | 国内网标志（NF）                 | LABEL14       | LABEL14       | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | 国内备用网标志（NRF）              | LABEL14       | LABEL14       | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | M3UA STP功能（M3UASTPF）      | ENABLE        | ENABLE        | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | 是否支持BSSAP+（BSSAPPF）       | ENABLE        | ENABLE        | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | BSSAP+子系统号（BSSAPPNO）      | 252           | 252           | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | BSSAP+所在信令网（BSSAPPNI）     | DISUSED       | DISUSED       | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | MAP所在信令网（MAPNI）           | NAT           | NAT           | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| SET SIGATTR   | 信令网协议类型（SS7T）             | ITUT_SS7      | ITUT_SS7      | 参见“水平网设LLD文档 ”。 | 配置本局信令网属性。  |
| ADD M3LE      | 本地实体索引（LEX）               | 0             | 0             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 网络指示语（NI）                 | NAT           | NAT           | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 本地实体编码（OPC）               | 0x1064        | 0x1064        | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 本地实体类型（LET）               | ASP           | ASP           | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 路由上下文（RC）                 | 123456        | 123456        | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 网络外貌（NA）                  | 789456        | 789456        | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LE      | 本地实体名（LEN）                | SGSN          | SGSN          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 目的实体索引（DEX）               | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 本地实体索引（LEX）               | 0             | 0             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 目的实体编码（DPC）               | 0x2880        | 0x2880        | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 链路集选择掩码（SLSSM）            | B0001         | B0001         | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 目的实体类型（DET）               | SGP           | SGP           | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 相邻标记（ADJF）                | TRUE          | TRUE          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 路由上下文（RC）                 | 123456        | 123456        | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | M3UA协议版本（PVER）            | RFC3332       | RFC3332       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3DE      | 目的实体名（DEN）                | SG_ A         | SG_ A         | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 链路集索引（LSX）                | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 目的实体索引（DEX）               | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 链路选择掩码（SLSM）              | B0010         | B0010         | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 工作模式（WM）                  | ASP           | ASP           | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 业务模式（TM）                  | LOADSHARE     | LOADSHARE     | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LKS     | 链路集名（LSN）                 | to_SG_A       | to_SG_A       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3RT      | 路由索引（RTX）                 | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3RT      | 目的实体索引（DEX）               | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3RT      | 链路集索引（LSX）                | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3RT      | 优先级（PRI）                  | 3             | 3             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3RT      | 信令路由名（RTN）                | SG_A          | SG_A          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | sctppara1     | sctppara1     | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 链路号（LNK）                  | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | VPN名称（VPNNAME）            | VPN_SIG       | VPN_SIG       | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | IP类型（IPT）                 | IPV4          | IPV4          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 本地IPv4地址1（LOCIPV41）       | 10.11.95.5    | 10.11.95.5    | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 本地IPv4地址2（LOCIPV42）       | 10.11.127.5   | 10.11.127.5   | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 本地端口号（LOCPORT）            | 2906          | 2906          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 对端IP地址1（PEERIPV41）        | 10.11.75.107  | 10.11.75.107  | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 对端IP地址2（PEERIPV42）        | 10.11.107.107 | 10.11.107.107 | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 对端端口号（PEERPORT）           | 2905          | 2905          | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | C/S模式（CS）                 | C             | C             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 链路集索引（LSX）                | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | SCTP 参数索引（SCTPINDX）       | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD M3LNK     | 链路名（LKN）                  | Link1_to_SG_A | Link1_to_SG_A | 参见“水平网设LLD文档 ”。 | 配置M3UA信令数据。 |
| ADD SCCPOPC   | 本局信令点索引（OPX）              | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPOPC   | 网络指示语（NI）                 | NAT           | NAT           | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPOPC   | 本局信令点编码（OPC）              | 0x1064        | 0x1064        | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPOPC   | 信令点用途（SPN）                | COREONLY      | COREONLY      | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPOPC   | 本局SGSN号（SGSNN）            | 8613912345    | 8613912345    | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPOPC   | 本局信令点名（OPN）               | SGSN_BER1     | SGSN_BER1     | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 目的信令点索引（DPX）              | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 本局信令点索引（OPX）              | 1             | 1             | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 目的信令点编码（DPC）              | 0x2880        | 0x2880        | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 负荷分担类型（LDP）               | LOADSHARE     | LOADSHARE     | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 负荷分担目的信令点索引（SDPX）         | 2             | 2             | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPDPC   | 子系统号（DPN）                 | SG_A          | SG_A          | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 子系统索引（SSNX）               | 0             | 0             | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 子系统号（SSN）                 | SCMG          | SCMG          | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 网络指示语（NI）                 | NAT           | NAT           | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 目的信令点编码（DPC）              | 0x1064        | 0x1064        | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 本局信令点编码（OPC）              | 0x1064        | 0x1064        | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPSSN   | 子系统名（SSNNAME）             | SGSN_BER1-SSN | SGSN_BER1-SSN | 参见“水平网设LLD文档 ”。 | 配置SCCP信令数据。 |
| ADD SCCPGT    | GT码索引（GTX）                | 0             | 0             | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 网络指示语（NI）                 | NAT           | NAT           | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 翻译结果类型（RT）                | DPC           | DPC           | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | GT码表示语（GTEXP）             | FOUR          | FOUR          | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 编号计划（NP）                  | ISDNP         | ISDNP         | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 地址性质表示语（ADDREXP）          | INTDN         | INTDN         | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 地址信息（ADDR）                | 8613912345    | 8613912345    | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | 目的信令点编码（DPC）              | 0x1064        | 0x1064        | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |
| ADD SCCPGT    | SCCP GT名称（NAME）           | SGSN_BER1-GT  | SGSN_BER1-GT  | 参见“水平网设LLD文档 ”。 | 配置GT翻译数据。   |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置本局信令网属性。

   ```
   SET SIGATTR: IF=LABEL24, IRF=LABEL14, NF=LABEL14, NRF=LABEL14, M3UASTPF=ENABLE, BSSAPPF=ENABLE, BSSAPPNO=252, BSSAPPNI=DISUSED, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
3. 增加业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.95.5", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.127.5", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.127.6", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.95.6", VPNINSTNAME="VPN_SIG";
   ```
4. 配置M3UA信令数据。

   1. 增加M3UA本地实体。

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x1064", LET=ASP, RC=123456, NA=789456, LEN="SGSN";
      ```
   2. 配置M3UA目的信令点。

      ```
      ADD M3DE: DEX=1, LEX=0, DPC="0x2880", SLSSM=B0001, DET=SGP, ADJF=TRUE, RC=123456, PVER=RFC3332, DEN="SG_A";
      ADD M3DE: DEX=2, LEX=0, DPC="0x2881", SLSSM=B0001, DET=SGP, ADJF=TRUE, RC=123456, PVER=RFC3332, DEN="SG_B";
      ```
   3. 配置到SG的M3UA信令链路集。

      ```
      ADD M3LKS: LSX=1, DEX=1, SLSM=B0010, WM=ASP, TM=LOADSHARE, LSN="to_SG_A";
      ADD M3LKS: LSX=2, DEX=2, SLSM=B0010, WM=ASP, TM=LOADSHARE, LSN="to_SG_B";
      ```
   4. 配置M3UA信令路由。

      ```
      ADD M3RT: RTX=1, DEX=1, LSX=1, PRI=3, RTN="SG_A";
      ADD M3RT: RTX=2, DEX=1, LSX=2, PRI=5, RTN="SG_A";
      ADD M3RT: RTX=3, DEX=2, LSX=2, PRI=3, RTN="SG_B";
      ADD M3RT: RTX=4, DEX=2, LSX=1, PRI=5, RTN="SG_B";
      ```
   5. 配置SCTP协议参数，SCTP协议参数索引为1。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=1, SCTPPARANAME="sctppara1";
      ```
   6. 配置M3UA信令链路。

      ```
      ADD M3LNK:LNK=1,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.11.95.5",LOCIPV42="10.11.127.5",LOCPORT=2906,PEERIPV41="10.11.75.107",PEERIPV42="10.11.107.107",PEERPORT=2905,CS=C,LSX=1,SCTPINDX=1,LKN="Link1_to_SG_A";
      ADD M3LNK:LNK=2,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.11.127.6",LOCIPV42="10.11.95.6",LOCPORT=2906,PEERIPV41="10.11.107.109",PEERIPV42="10.11.75.109",PEERPORT=2905,CS=C,LSX=1,SCTPINDX=1,LKN="Link2_to_SG_A";
      ADD M3LNK:LNK=3,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.11.95.5",LOCIPV42="10.11.127.5",LOCPORT=2906,PEERIPV41="10.11.70.107",PEERIPV42="10.11.102.107",PEERPORT=2905,CS=C,LSX=2,SCTPINDX=1,LKN="Link1_to_SG_B";
      ADD M3LNK:LNK=4,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.11.127.6",LOCIPV42="10.11.95.6",LOCPORT=2906,PEERIPV41="10.11.102.109",PEERIPV42="10.11.70.109",PEERPORT=2905,CS=C,LSX=2,SCTPINDX=1,LKN="Link2_to_SG_B";
      ```
5. 配置SCCP信令数据。

   1. 增加SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=1, NI=NAT, OPC="0x1064", SPN=COREONLY, SGSNN="8613912345", OPN="SGSN_BER1";
      ```
   2. 配置SCCP目的信令点

      ```
      ADD SCCPDPC: DPX=1, OPX=1, DPC="0x2880", LDP=LOADSHARE, SDPX=2, DPN="SG_A";
      ADD SCCPDPC: DPX=2, OPX=1, DPC="0x2881", LDP=LOADSHARE, SDPX=1, DPN="SG_B";
      ```
   3. 增加SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=0, SSN=SCMG, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN_BER1-SSN";
      ADD SCCPSSN: SSNX=1, SSN=SGSN, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN interna";
      ```
   4. 配置SG的SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=2, SSN=SCMG, NI=NAT, DPC="0x2880", OPC="0x1064", SSNNAME="SG_A";
      ADD SCCPSSN: SSNX=3, SSN=SCMG, NI=NAT, DPC="0x2881", OPC="0x1064", SSNNAME="SG_B";
      ```
6. 配置GT翻译数据。

   1. 增加本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=0, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613912345", DPC="0x1064", NAME="SGSN_BER1-GT";
      ```
   2. 配置到SG的GT翻译数据。

      ```
      ADD SCCPGT: GTX=1, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="86139", DPC="0x2881";
      ```

      **说明** 

      编号计划（NP）为ISDNP的地址信息（ADDR）也可以配置为0～9号段。

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. SMC的寻址方式为DPC+SSN？
   - 是：4
   - 否：结束。
3. 检查M3UA链路的状态

   **DSP M3LNK**
   - **预期结果：**“链路状态”字段为“激活”。

     ```
     %%DSP M3LNK: SRT=STATUS;%%
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
4. 检查M3UA路由的状态。

   **DSP M3RT**
   - **预期结果：**“路由状态”字段为“可用”。

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
5. 检查M3UA目的信令点的状态。

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
6. 检查SCCP目的信令点状态。

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
7. 检查SMC SCCP子系统的状态。

   ****DSP SCCPSSN****
   - **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN:;%%
     RETCODE = 0  执行成功

     查询SCCP子系统状态
     -----------------------------
      子系统索引       子系统号       网络指示语   目的信令点编码 本局信令点编码 子系统状态 是否测试状态 测试忽略标志

      1                SCMG(1)        国内网       0x308401       0x308401       允许       否           否
      2                SGSN(149)      国内网       0x308401       0x308401       允许       否           否         
      3                MSC            国内网       0x308401       0x308401       允许       否           否         
      4                SCMG(1)        国内网       0x2201         0x308401       允许       否           否               
      5                MSC            国内网       0x2201         0x308401       允许       否           否                 
     (Number of results = 5)

     ---    END
     ```
   - **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。