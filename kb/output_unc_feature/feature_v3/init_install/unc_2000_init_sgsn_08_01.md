# 配置到GMLC的数据（Over IP）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增GMLC或SGSN时，在配置完成SGSN到GMLC的路由数据后，可通过配置M3UA链路数据建立SGSN到GMLC的逻辑连接。

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

**表1** 到GMLC准备的数据

| 类别 | 参数名称 | 取值样例 |  | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  | 参见“水平网设LLD文档 ”。 | 增加业务IP。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.1.1 |  |  |  |
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
| ****ADD M3LE**** | 本地实体索引（LEX） | 10 |  |  | 配置M3UA信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本地实体编码（OPC） | 0x2463 |  |  |  |
|  | 本地实体类型（LET） | IPSP |  |  |  |
|  | 路由上下文（RC） | 123456 |  |  |  |
|  | 网络外貌（NA） | 789456 |  |  |  |
|  | 本地实体名（LEN） | to SS7 |  |  |  |
| ****ADD M3DE**** | 目的实体索引（DEX） | 113 |  |  |  |
|  | 本地实体索引（LEX） | 10 |  |  |  |
|  | 目的实体编码（DPC） | 0x3113 |  |  |  |
|  | 链路集选择掩码（SLSSM） | B0000 |  |  |  |
|  | 目的实体类型（DET） | IPSP |  |  |  |
|  | 相邻标记（ADJF） | TRUE |  |  |  |
|  | 路由上下文（RC） | 123456 |  |  |  |
|  | M3UA协议版本（PVER） | RFC3332 |  |  |  |
|  | 目的实体名（DEN） | to GMLC |  |  |  |
| ****ADD M3LKS**** | 链路集索引（LSX） | 113 |  |  |  |
|  | 目的实体索引（DEX） | 113 |  |  |  |
|  | 链路选择掩码（SLSM） | B0010 |  |  |  |
|  | 工作模式（WM） | IPSP |  |  |  |
|  | 业务模式（TM） | LOADSHARE |  |  |  |
|  | 链路集名（LSN） | to GMLC |  |  |  |
| ****ADD M3RT**** | 路由索引（RTX） | 113 |  |  |  |
|  | 目的实体索引（DEX） | 113 |  |  |  |
|  | 链路集索引（LSX） | 114 |  |  |  |
|  | 信令路由名（RTN） | to GMLC |  |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 1 |  |  |  |
|  | SCTP协议参数名（SCTPPARANAME） | sctppara1 |  |  |  |
| ****ADD M3LNK**** | 链路号（LNK） | 1 |  |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |  |
|  | IP类型（IPT） | IPV4 |  |  |  |
|  | 本地IPv4地址1（LOCIPV41） | 10.10.1.1 |  |  |  |
|  | 本地IPv4地址2（LOCIPV42） | 10.10.1.2 |  |  |  |
|  | 本地端口号（LOCPORT） | 2906 |  |  |  |
|  | 对端IP地址1（PEERIPV41） | 10.10.1.165 |  |  |  |
|  | 对端IP地址2（PEERIPV42） | 10.10.1.166 |  |  |  |
|  | 对端端口号（PEERPORT） | 2905 |  |  |  |
|  | C/S模式（CS） | C |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | 主备标识（ASF） | ACT |  |  |  |
|  | 交叉路径是否可用（CROSSIP） | NO |  |  |  |
|  | SCTP 参数索引（SCTPINDX） | 1 |  |  |  |
|  | 链路名（LKN） | To GMLC LINK1 |  |  |  |
| **ADD SCCPOPC** | 本局信令点索引（OPX） | 21 |  |  | 配置SCCP信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本局信令点编码（OPC） | 0x2463 |  |  |  |
|  | 信令点用途（SPN） | IUANDCORE |  |  |  |
|  | 本局SGSN号（SGSNN） | 8613742383 |  |  |  |
|  | 本局信令点名（OPN） | TO RNC AND SS7 |  |  |  |
| ****ADD SCCPDPC**** | 目的信令点索引（DPX） | 113 |  |  |  |
|  | 本局信令点索引（OPX） | 21 |  |  |  |
|  | 目的信令点编码（DPC） | 0x3113 |  |  |  |
|  | 负荷分担类型（LDP） | NOUSE |  |  |  |
|  | 子系统号（DPN） | TO GMLC |  |  |  |
| ****ADD SCCPSSN**** | 子系统索引（SSNX） | 201 |  |  |  |
|  | 子系统号（SSN） | SGSN |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 目的信令点编码（DPC） | 0x2463 |  |  |  |
|  | 本局信令点编码（OPC） | 0x2463 |  |  |  |
|  | 子系统名（SSNNAME） | SGSN to SGSN |  |  |  |
| ****ADD SCCPGT**** | GT码索引（GTX） | 201 |  |  | 配置GT翻译数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 翻译结果类型（RT） | DPC |  |  |  |
|  | GT码表示语（GTEXP） | FOUR |  |  |  |
|  | 编号计划（NP） | ISDNP |  |  |  |
|  | 地址性质表示语（ADDREXP） | INTDN |  |  |  |
|  | 地址信息（ADDR） | 8613742383 |  |  |  |
|  | 目的信令点编码（DPC） | 0x2463 |  |  |  |
|  | SCCP GT名称（NAME） | TO SGSN |  |  |  |
| ****ADD GMLC**** | GMLC 标识 （GMLCID ） | 1 |  |  | 增加GMLC配置。 |
|  | GMLC所属MCC （MCC） | 640 |  |  |  |
|  | GMLC所属MNC （MNC） | 000 |  |  |  |
|  | GMLC IP地址类型 （GMLCIPT ） | IPV4 |  |  |  |
|  | GMLC IPV4地址 （GMLCIPV4 ） | 10.10.1.165 |  |  |  |
|  | GMLC 号码 （GMLCNO ） | 123456 |  |  |  |
|  | GMLC 主机名 （HSNM ） | gmlc1.epc.mnc015.mcc234.3gppnetwork.org |  |  |  |
|  | 接口类型（IFTYPE） | Lg-1 |  |  |  |

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
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_SIG";
   ```
4. 配置M3UA信令数据

   1. 增加M3UA本地实体

      ```
      ADD M3LE: LEX=10, NI=NAT, OPC="0x2463", LET=IPSP, RC=123456, NA=789456, LEN="to SS7";
      ```
   2. 配置M3UA目的信令点。

      ```
      ADD M3DE: DEX=113, LEX=10, DPC="0x3113", SLSSM=B0000, DET=IPSP, ADJF=TRUE, RC=123456, PVER=RFC3332, DEN="to GMLC";
      ```
   3. 配置M3UA信令链路集。

      ```
      ADD M3LKS: LSX=113, DEX=113, SLSM=B0010, WM=IPSP, TM=LOADSHARE, LSN="to GMLC";
      ```
   4. 配置到GMLC的M3UA信令路由。

      ```
      ADD M3RT: RTX=113, DEX=113, LSX=113, RTN="to GMLC";
      ```
   5. 配置SCTP协议参数。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=1, SCTPPARANAME="sctppara1";
      ```
   6. 配置M3UA信令链路。

      ```
      ADD M3LNK:LNK=1,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.1",LOCIPV42="10.10.1.2",LOCPORT=2906,PEERIPV41="10.10.1.165",PEERIPV42="10.10.1.166",PEERPORT=2905,CS=C,LSX=1,ASF=ACT,SCTPINDX=1,CROSSIP=NO,LKN="TO GMLC LINK1";
      ```
5. 配置SCCP信令数据。

   1. 增加SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=21, NI=NAT, OPC="0x2463", SPN=IUANDCORE, SGSNN="8613742383", OPN="TO RNC AND SS7";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=113, OPX=21, DPC="0x3113", LDP=NOUSE, DPN="TO GMLC";
      ```
   3. 增加SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=201, SSN=SGSN, NI=NAT, DPC="0x2463", OPC="0x2463", SSNNAME="SGSN TO SGSN";
      ADD SCCPSSN: SSNX=202, SSN=SCMG, NI=NAT, DPC="0x2463", OPC="0x2463", SSNNAME="SGSN TO SGSN";
      ```
   4. 配置GMLC的SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=605, SSN=SCMG, NI=NAT, DPC="0x3113", OPC="0x2463", SSNNAME="to GMLC";
      ADD SCCPSSN: SSNX=606, SSN=GMLC, NI=NAT, DPC="0x3113", OPC="0x2463", SSNNAME="to GMLC";
      ```
6. 配置GT翻译数据。

   1. 增加本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=201, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613742383", DPC="0x2463", NAME="TO SGSN";
      ```
   2. 配置到本地GMLC的GT翻译数据。

      ```
      ADD SCCPGT: GTX=2, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613900603", DPC="0x3154", NAME="to GMLC";
      ```

      翻译结果类型也可以选择为DPC+SSN。
7. 增加GMLC配置。

   ```
   ADD GMLC: GMLCID=1, MCC="640", MNC="000", GMLCIPT=IPV4, GMLCIPV4="10.10.1.165", GMLCNO="123456", HSNM="gmlc1.epc.mnc015.mcc234.3gppnetwork.org", IFTYPE=Lg-1;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查M3UA链路的状态

   **DSP M3LNK**
   * **预期结果：**“链路状态”字段为“激活”。

     ```
     查询M3UA链路状态
     ----------------
       RU名称  = USN_VSU1
       进程号  =  3
       链路号  =  3
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
     RETCODE = 0  执行成功

     查询M3UA路由状态
     ----------------
               路由索引  =  0
           目的实体索引  =  0
             链路集索引  =  0
               路由状态  =  可用
      SG和SEP间路由禁止  =  否
      SG和SEP间路由受限  =  否
           链路集不可用  =  否
               SLS(HEX)  =  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
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
     RETCODE = 0  操作成功

     查询M3UA目的实体状态
     --------------------
      目的实体索引  =  1
        网络指示语  =  国内网
      目的实体编码  =  0x123
      本地实体编码  =  0x12
          是否可达  =  是
          是否拥塞  =  否

     ---    END
     ```
   * **异常结果：**“是否可达”字段为“否”。

     异常处理过程参见ALM-10337 M3UA目的实体不可达。
5. 检查SCCP目的信令点状态。

   **DSP SCCPDPC**
   * **预期结果：**“信令点状态”字段为“允许”。

     ```
     %%DSP SCCPDPC: DPX=1;%%
     RETCODE = 0  执行成功

     查询SCCP目的信令点状态
     -----------------------------------------------
          目的信令点索引  =  1
               网络指示语  =  国内网
           目的信令点编码  =  0x18101
           本局信令点编码  =  0x308401
               信令点状态  =  允许
      负荷分担信令点状态  =  允许
           备用信令点状态  =  NULL
                  SCCP状态  =  允许
                    塞状态  =  非拥塞
     (Number of results = 1)

     ---    END
     ```
   * **异常结果：**“信令点状态”字段为“禁止”。

     异常处理过程参见ALM-10341 SCCP目的信令点不可达。
6. 检查目的信令点SCCP子系统的状态。

   ****DSP SCCPSSN****

   * **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN:;%%
     RETCODE = 0  执行成功

     查询SCCP子系统状态
     -----------------------------
      子系统索引       子系统号       网络指示语   目的信令点编码 本局信令点编码 子系统状态 是否测试状态 测试忽略标志

      1                SCMG(1)        国内网       0x12345        0x12345        允许       否           否         
      2                SGSN(149)      国内网       0x12345        0x12345        允许       否           否         
      3                SCMG(1)        国内网       0x23456        0x12345        允许       否           否               
      4                GMLC(6)         国内网       0x23456        0x12345        允许       否           否                 
     (Number of results = 4)

     ---    END
     ```
   * **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。
7. 进行业务测试。

   进行业务测试前，需要首先完成与BSS/RNC、GMLC的链路配置。

   1. 创建用户跟踪。

      参数选择如下：

      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其它参数：选择默认值。
   2. 创建接口跟踪

      参数选择如下：

      * Ru名称：资源单元的名称。
      * 进程序号：虚拟机内，SPP进程的同类进程序号。
      * 过滤参数：IMSI（1~15位的十进制数字）或者MSISDN（6~15位的十进制数字）。
      * 其它参数：选择默认值。
   3. 用户开机附着。
   4. GMLC发起LCS定位请求。
   5. 查看Lg接口跟踪结果。
      * **预期结果：**可以看到GMLC与SGSN之间的消息交互，如图1所示。

        **图1** Location Service流程消息（样例）
      * 异常结果：观察不到用户跟踪和Lg接口跟踪中LCS的相关信息，或观察到用户跟踪或Lg接口跟踪的消息异常。
   6. 查看用户跟踪结果。
      * **预期结果：**LCS业务请求成功，可以在消息方向处看到LCS模块与MAP模块之间有消息交互，如图2所示。

        **图2** 用户跟踪-LCS业务请求成功（样例）
      * **异常结果：**观察不到LCS模块与MAP模块之间的消息或观察到的消息异常。

版权所有 © 华为技术有限公司
