# 配置到SMC的数据（Over IP）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增SMC或SGSN时，在配置完成SGSN到SMC的路由数据后，可通过配置M3UA链路数据建立SGSN到SMC的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 |  | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  | 参见“水平网设LLD文档 ”。 | 增加业务IP。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.11.129.120 |  |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |  |
| ****SET SIGATTR**** | 国际网标志（IF） | LABEL24 |  |  | 配置本局信令网属性。 |
|  | 国际备用网标志（IRF） | LABEL14 |  |  |  |
|  | 国内网标志（NF） | LABEL14 |  |  |  |
|  | 国内备用网标志（NRF） | LABEL14 |  |  |  |
|  | M3UA STP功能（M3UASTPF） | ENABLE |  |  |  |
|  | 是否支持BSSAP+（BSSAPPF） | ENABLE |  |  |  |
|  | BSSAP+子系统号（BSSAPPNO） | 252 |  |  |  |
|  | BSSAP+所在信令网（BSSAPPNI） | DISUSED |  |  |  |
|  | MAP所在信令网（MAPNI） | NAT |  |  |  |
|  | 信令网协议类型（SS7T） | ITUT\_SS7 |  |  |  |
| ****ADD M3LE**** | 本地实体索引（LEX） | 0 |  |  | 配置M3UA信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本地实体编码（OPC） | 0x30a |  |  |  |
|  | 本地实体类型（LET） | IPSP |  |  |  |
|  | 本地实体名（LEN） | to SS7 |  |  |  |
| ****ADD M3DE**** | 目的实体索引（DEX） | 3 |  |  |  |
|  | 本地实体索引（LEX） | 0 |  |  |  |
|  | 目的实体编码（DPC） | 0x20b |  |  |  |
|  | 链路集选择掩码（SLSSM） | B0000 |  |  |  |
|  | 目的实体类型（DET） | IPSP |  |  |  |
|  | 相邻标记（ADJF） | TRUE |  |  |  |
|  | M3UA协议版本（PVER） | RFC3332 |  |  |  |
|  | 目的实体名（DEN） | to SMC |  |  |  |
| ****ADD M3LKS**** | 链路集索引（LSX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 3 |  |  |  |
|  | 链路选择掩码（SLSM） | B0010 |  |  |  |
|  | 工作模式（WM） | IPSP |  |  |  |
|  | 业务模式（TM） | LOADSHARE |  |  |  |
|  | 链路集名（LSN） | to SMC |  |  |  |
| ****ADD M3RT**** | 路由索引（RTX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 3 |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | 信令路由名（RTN） | to SMC |  |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 1 |  |  |  |
|  | SCTP协议参数名（SCTPPARANAME） | sctppara1 |  |  |  |
| ****ADD M3LNK**** | 链路号（LNK） | 1 |  |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |  |
|  | IP类型（IPT） | IPV4 |  |  |  |
|  | 本地IPv4地址1（LOCIPV41） | 10.11.150.1 |  |  |  |
|  | 本地IPv4地址2（LOCIPV42） | 10.11.182.1 |  |  |  |
|  | 本地端口号（LOCPORT） | 2906 |  |  |  |
|  | 对端IP地址1（PEERIPV41） | 10.11.128.25 |  |  |  |
|  | 对端IP地址2（PEERIPV42） | 10.11.160.25 |  |  |  |
|  | 对端端口号（PEERPORT） | 2905 |  |  |  |
|  | C/S模式（CS） | C |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | 主备标识（ASF） | ACT |  |  |  |
|  | 优先级（PRI） | 0 |  |  |  |
|  | 交叉路径是否可用（CROSSIP） | YES |  |  |  |
|  | SCTP 参数索引（SCTPINDX） | 1 |  |  |  |
|  | 链路名（LKN） | To SMC LINK1 |  |  |  |
| **ADD SCCPOPC** | 本局信令点索引（OPX） | 1 |  |  | 配置SCCP信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本局信令点编码（OPC） | 0x30a |  |  |  |
|  | 信令点用途（SPN） | IUANDCORE |  |  |  |
|  | 本局SGSN号（SGSNN） | 8613912345 |  |  |  |
|  | 本局信令点名（OPN） | TO RNC AND SS7 |  |  |  |
| ****ADD SCCPDPC**** | 目的信令点索引（DPX） | 3 |  |  |  |
|  | 本局信令点索引（OPX） | 1 |  |  |  |
|  | 目的信令点编码（DPC） | 0x20b |  |  |  |
|  | 负荷分担类型（LDP） | NOUSE |  |  |  |
|  | 子系统号（DPN） | TO SMC |  |  |  |
| ****ADD SCCPSSN**** | 子系统索引（SSNX） | 0 |  |  |  |
|  | 子系统号（SSN） | SCMG |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 目的信令点编码（DPC） | 0x20b |  |  |  |
|  | 本局信令点编码（OPC） | 0x30a |  |  |  |
|  | 子系统名（SSNNAME） | to SMC |  |  |  |
| ****ADD SCCPGT**** | GT码索引（GTX） | 0 |  |  | 配置GT翻译数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 翻译结果类型（RT） | DPC |  |  |  |
|  | GT码表示语（GTEXP） | FOUR |  |  |  |
|  | 编号计划（NP） | ISDNP |  |  |  |
|  | 地址性质表示语（ADDREXP） | INTDN |  |  |  |
|  | 地址信息（ADDR） | 8613900123 |  |  |  |
|  | 目的信令点编码（DPC） | 0x20b |  |  |  |
|  | SCCP GT名称（NAME） | to SMC |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 增加业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.129.120", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.161.120", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.150.1", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.182.1", VPNINSTNAME="VPN_SIG";
   ```
3. 配置本局信令网属性。

   ```
   SET SIGATTR: IF=LABEL24, IRF=LABEL14, NF=LABEL14, NRF=LABEL14, M3UASTPF=ENABLE, BSSAPPF=ENABLE, BSSAPPNO=252, BSSAPPNI=DISUSED, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
4. 配置M3UA信令数据

   1. 增加M3UA本地实体

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x30a", LET=IPSP, LEN="to SS7";
      ```
   2. 配置M3UA目的信令点。

      ```
      ADD M3DE: DEX=3, LEX=0, DPC="0x20b", SLSSM=B0000, DET=IPSP, ADJF=TRUE, PVER=RFC3332, DEN="to SMC";
      ```
   3. 配置M3UA信令链路集。

      ```
      ADD M3LKS: LSX=1, DEX=3, SLSM=B0010, WM=IPSP, TM=LOADSHARE, LSN="to SMC";
      ```
   4. 配置到SMC的M3UA信令路由。

      ```
      ADD M3RT: RTX=1, DEX=3, LSX=1, RTN="to SMC";
      ```
   5. 配置SCTP协议参数。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=1, SCTPPARANAME="sctppara1";
      ```
   6. 配置M3UA信令链路，增加两条信令链路，分别在不同的SGP进程上，采用SCTP多归属方式与对端设备通信，本端为客户端模式。

      ```
      ADD M3LNK: LNK=1, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.11.150.1", LOCIPV42="10.11.182.1", LOCPORT=2906, PEERIPV41="10.11.128.25", PEERIPV42="10.11.160.25", PEERPORT=2905, CS=C, LSX=1,ASF=ACT, PRI=0, CROSSIP=YES, SCTPINDX=1, LKN="To SMC LINK1";
      ADD M3LNK: LNK=1, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.11.129.120", LOCIPV42="10.11.161.120", LOCPORT=2906, PEERIPV41="10.11.128.25", PEERIPV42="10.11.160.25", PEERPORT=2905, CS=C, LSX=1,ASF=ACT, PRI=0, CROSSIP=YES, SCTPINDX=1, LKN="To SMC LINK1";
      ```
5. 配置SCCP信令数据。

   1. 增加SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=1, NI=NAT, OPC="0x30a", SPN=IUANDCORE, SGSNN="8613912345", OPN="TO RNC AND SS7";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=3, OPX=1, DPC="0x20b", LDP=NOUSE, DPN="TO SMC";
      ```
   3. 增加SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=0, SSN=SCMG, NI=NAT, DPC="0x30a", OPC="0x30a", SSNNAME="SGSN TO SGSN";
      ADD SCCPSSN: SSNX=1, SSN=SGSN, NI=NAT, DPC="0x30a", OPC="0x30a", SSNNAME="SGSN TO SGSN";
      ```
   4. 配置SMC的SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=3, SSN=SCMG, NI=NAT, DPC="0x20b", OPC="0x30a", SSNNAME="to SMC";
      ADD SCCPSSN: SSNX=4, SSN=MSC, NI=NAT, DPC="0x20b", OPC="0x30a", SSNNAME="to SMC";
      ```
6. 配置GT翻译数据。

   1. 增加本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=0, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613912345", DPC="0x30a", NAME="TO SGSN";
      ```
   2. 配置到本地SMC的GT翻译数据。

      ```
      ADD SCCPGT: GTX=2, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613900123", DPC="0x20b", NAME="to SMC";
      ```

      翻译结果类型也可以选择为DPC+SSN。

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查M3UA链路的状态

   **DSP M3LNK**
   * **预期结果：**“链路状态”字段为“激活”。

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
   * **异常结果：**“链路状态”字段不为“激活”。

     异常处理过程参见ALM-80633 M3UA链路故障。
3. 检查M3UA路由的状态。

   **DSP M3RT**
   * **预期结果：**“路由状态”字段为“可用”。

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
   * **异常结果：**“路由状态”字段不为“可用”。

     异常处理过程参见ALM-10336 M3UA路由不可用。
4. 检查M3UA目的信令点的状态。

   **DSP M3DE**
   * **预期结果：**“是否可达”字段为“是”。

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
   * **异常结果：**“是否可达”字段为“否”。

     异常处理过程参见ALM-10337 M3UA目的实体不可达。
5. 检查SCCP目的信令点状态。

   **DSP SCCPDPC**
   * **预期结果：**“信令点状态”字段为“允许”。

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
   * **异常结果：**“信令点状态”字段为“禁止”。

     异常处理过程参见ALM-10341 SCCP目的信令点不可达。
6. 检查SMC SCCP子系统的状态。

   ****DSP SCCPSSN****

   * **预期结果：**“子系统状态”字段为“允许”。

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
   * **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。

版权所有 © 华为技术有限公司
