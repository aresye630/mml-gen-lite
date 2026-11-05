# 配置到EIR的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增EIR或SGSN时，在配置完成SGSN到EIR的路由数据后，可通过配置M3UA链路数据建立SGSN到EIR的逻辑连接。

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
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.1.1 |  |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |  |
| ****SET SIGATTR**** | 国际网标志（IF） | LABEL24 |  |  | 配置本局信令网属性。 |
|  | 国际备用网标志（IRF） | LABEL14 |  |  |  |
|  | 国内网标志（NF） | LABEL14 |  |  |  |
|  | 国内备用网标志（NRF） | LABEL14 |  |  |  |
|  | M3UA STP功能（M3UASTPF） | DISABLE |  |  |  |
|  | 是否支持BSSAP+（BSSAPPF） | DISABLE |  |  |  |
|  | BSSAP+子系统号（BSSAPPNO） | 252 |  |  |  |
|  | BSSAP+所在信令网（BSSAPPNI） | DISUSED |  |  |  |
|  | MAP所在信令网（MAPNI） | NAT |  |  |  |
|  | 信令网协议类型（SS7T） | ITUT\_SS7 |  |  |  |
| ****ADD M3LE**** | 本地实体索引（LEX） | 0 |  |  | 配置M3UA信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本地实体编码（OPC） | 0x2463 |  |  |  |
|  | 本地实体类型（LET） | ASP |  |  |  |
|  | 路由上下文（RC） | 123456 |  |  |  |
|  | 网络外貌（NA） | 789456 |  |  |  |
|  | 本地实体名（LEN） | SGSN |  |  |  |
| ****ADD M3DE**** | 目的实体索引（DEX） | 103 |  |  |  |
|  | 本地实体索引（LEX） | 10 |  |  |  |
|  | 目的实体编码（DPC） | 0x3103 |  |  |  |
|  | 链路集选择掩码（SLSSM） | B0001 |  |  |  |
|  | 目的实体类型（DET） | SGP |  |  |  |
|  | 相邻标记（ADJF） | TRUE |  |  |  |
|  | 路由上下文（RC） | 123453 |  |  |  |
|  | M3UA协议版本（PVER） | RFC3332 |  |  |  |
|  | 目的实体名（DEN） | SG\_A |  |  |  |
| ****ADD M3LKS**** | 链路集索引（LSX） | 103 |  |  |  |
|  | 目的实体索引（DEX） | 103 |  |  |  |
|  | 链路选择掩码（SLSM） | B0001 |  |  |  |
|  | 工作模式（WM） | ASP |  |  |  |
|  | 业务模式（TM） | LOADSHARE |  |  |  |
|  | 链路集名（LSN） | to\_SG\_A |  |  |  |
| ****ADD M3RT**** | 路由索引（RTX） | 103 |  |  |  |
|  | 目的实体索引（DEX） | 103 |  |  |  |
|  | 链路集索引（LSX） | 103 |  |  |  |
|  | 优先级（PRI） | 3 |  |  |  |
|  | 信令路由名（RTN） | SG\_A |  |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 2 |  |  |  |
|  | SCTP协议参数名（SCTPPARANAME） | sctppara2 |  |  |  |
| ****ADD M3LNK**** | 链路号（LNK） | 115 |  |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |  |
|  | IP类型（IPT） | IPV4 |  |  |  |
|  | 本地IPv4地址1（LOCIPV41） | 10.10.1.1 |  |  |  |
|  | 本地IPv4地址2（LOCIPV42） | 10.10.1.17 |  |  |  |
|  | 本地端口号（LOCPORT） | 2906 |  |  |  |
|  | 对端IP地址1（PEERIPV41） | 10.10.1.8 |  |  |  |
|  | 对端IP地址2（PEERIPV42） | 10.10.1.150 |  |  |  |
|  | 对端端口号（PEERPORT） | 2905 |  |  |  |
|  | C/S模式（CS） | C |  |  |  |
|  | 链路集索引（LSX） | 103 |  |  |  |
|  | SCTP 参数索引（SCTPINDX） | 4 |  |  |  |
|  | 链路名（LKN） | Link1\_to\_SG\_A |  |  |  |
| **ADD SCCPOPC** | 本局信令点索引（OPX） | 21 |  |  | 配置SCCP信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本局信令点编码（OPC） | 0x2463 |  |  |  |
|  | 信令点用途（SPN） | COREONLY |  |  |  |
|  | 本局SGSN号（SGSNN） | 8613742383 |  |  |  |
|  | 本局信令点名（OPN） | SGSN |  |  |  |
| ****ADD SCCPDPC**** | 目的信令点索引（DPX） | 103 |  |  |  |
|  | 本局信令点索引（OPX） | 21 |  |  |  |
|  | 目的信令点编码（DPC） | 0x3103 |  |  |  |
|  | 负荷分担类型（LDP） | LOADSHARE |  |  |  |
|  | 负荷分担目的信令点索引（SDPX） | 104 |  |  |  |
|  | 子系统号（DPN） | SG\_A |  |  |  |
| ****ADD SCCPSSN**** | 子系统索引（SSNX） | 201 |  |  |  |
|  | 子系统号（SSN） | SCMG |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 目的信令点编码（DPC） | 0x2463 |  |  |  |
|  | 本局信令点编码（OPC） | 0x2463 |  |  |  |
|  | 子系统名（SSNNAME） | SGSN\_BER1-SSN |  |  |  |
| ****ADD SCCPGT**** | GT码索引（GTX） | 201 |  |  | 配置GT翻译数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 翻译结果类型（RT） | DPC |  |  |  |
|  | GT码表示语（GTEXP） | FOUR |  |  |  |
|  | 编号计划（NP） | ISDNP |  |  |  |
|  | 地址性质表示语（ADDREXP） | INTDN |  |  |  |
|  | 地址信息（ADDR） | 8613742383 |  |  |  |
|  | 目的信令点编码（DPC） | 0x2463 |  |  |  |
|  | SCCP GT名称（NAME） | SGSN\_BER1-GT |  |  |  |
| ****SET MAPFUNC**** | 缺省EIR（EIR） | 8613900503 |  |  | 配置EIR号码。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 增加业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.17", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.18", VPNINSTNAME="VPN_SIG";
   ```
3. 配置本局信令网属性。

   ```
   SET SIGATTR: IF=LABEL24, IRF=LABEL14, NF=LABEL14, NRF=LABEL14, M3UASTPF=DISABLE, BSSAPPF=DISABLE, BSSAPPNO=252, BSSAPPNI=DISUSED, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
4. 配置M3UA信令数据

   1. 增加M3UA本地实体

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x2463", LET=ASP, RC=123456, NA=789456, LEN="SGSN";
      ```
   2. 配置M3UA目的信令点。

      ```
      ADD M3DE: DEX=103, LEX=10, DPC="0x3103", SLSSM=B0001, DET=SGP, ADJF=TRUE, RC=123453, PVER=RFC3332, DEN="SG_A"; 
      ADD M3DE: DEX=104, LEX=10, DPC="0x3104", SLSSM=B0001, DET=SGP, ADJF=TRUE, RC=123454, PVER=RFC3332, DEN="SG_B";
      ```
   3. 配置到SG的M3UA信令链路集。

      ```
      ADD M3LKS: LSX=103, DEX=103, SLSM=B0001, WM=ASP, TM=LOADSHARE, LSN="to_SG_A"; 
      ADD M3LKS: LSX=104, DEX=104, SLSM=B0001, WM=ASP, TM=LOADSHARE, LSN="to_SG_B";
      ```
   4. 配置M3UA路由。

      ```
      ADD M3RT: RTX=103, DEX=103, LSX=103, PRI=3, RTN="SG_A"; 
      ADD M3RT: RTX=104, DEX=104, LSX=104, PRI=3, RTN="SG_B";
      ```
   5. 配置SCTP协议参数。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=2, SCTPPARANAME="sctppara2";
      ```
   6. 配置M3UA信令链路。

      ```
      ADD M3LNK:LNK=115,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.1",LOCIPV42="10.10.1.17",LOCPORT=2906,PEERIPV41="10.10.1.8",PEERIPV42="10.10.1.150",PEERPORT=2905,CS=C,LSX=103,SCTPINDX=4,LKN="Link1_to_SG_A";
      ADD M3LNK:LNK=115,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.1",LOCIPV42="10.10.1.17",LOCPORT=2906,PEERIPV41="10.10.1.9",PEERIPV42="10.10.1.151",PEERPORT=2905,CS=C,LSX=103,SCTPINDX=2,LKN="Link1_to_SG_A";
      ADD M3LNK:LNK=116,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.2",LOCIPV42="10.10.1.18",LOCPORT=2906,PEERIPV41="10.10.1.10",PEERIPV42="10.10.1.152",PEERPORT=2905,CS=C,LSX=103,SCTPINDX=2,LKN="Link2_to_SG_A";
      ADD M3LNK:LNK=116,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.2",LOCIPV42="10.10.1.18",LOCPORT=2906,PEERIPV41="10.10.1.11",PEERIPV42="10.10.1.153",PEERPORT=2905,CS=C,LSX=103,SCTPINDX=2,LKN="Link2_to_SG_A";
      ADD M3LNK:LNK=117,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.1",LOCIPV42="10.10.1.17",LOCPORT=2906,PEERIPV41="10.10.1.12",PEERIPV42="10.10.1.154",PEERPORT=2905,CS=C,LSX=104,SCTPINDX=2,LKN="Link1_to_SG_B";
      ADD M3LNK:LNK=117,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.1",LOCIPV42="10.10.1.17",LOCPORT=2906,PEERIPV41="10.10.1.13",PEERIPV42="10.10.1.155",PEERPORT=2905,CS=C,LSX=104,SCTPINDX=2,LKN="Link1_to_SG_B";
      ADD M3LNK:LNK=118,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.2",LOCIPV42="10.10.1.18",LOCPORT=2906,PEERIPV41="10.10.1.14",PEERIPV42="10.10.1.156",PEERPORT=2905,CS=C,LSX=104,SCTPINDX=2,LKN="Link2_to_SG_B";
      ADD M3LNK:LNK=118,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.1.2",LOCIPV42="10.10.1.18",LOCPORT=2906,PEERIPV41="10.10.1.15",PEERIPV42="10.10.1.157",PEERPORT=2905,CS=C,LSX=104,SCTPINDX=2,LKN="Link2_to_SG_B";
      ```
5. 配置SCCP信令数据。

   1. 增加SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=21, NI=NAT, OPC="0x2463", SPN=COREONLY, SGSNN="8613742383", OPN="SGSN";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=103, OPX=21, DPC="0x3103", LDP=LOADSHARE, SDPX=104, DPN="SG_A"; 
      ADD SCCPDPC: DPX=104, OPX=21, DPC="0x3104", LDP=LOADSHARE, SDPX=103, DPN="SG_B";
      ```
   3. 增加SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=201, SSN=SCMG, NI=NAT, DPC="0x2463", OPC="0x2463", SSNNAME="SGSN_BER1-SSN"; 
      ADD SCCPSSN: SSNX=206, SSN=EIR, NI=NAT, DPC="0x2463", OPC="0x2463", SSNNAME="SGSN_BER1-SSN";
      ```
   4. 配置SG的SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=103, SSN=SCMG, NI=NAT, DPC="0x3103", OPC="0x2463", SSNNAME="SG_A"; 
      ADD SCCPSSN: SSNX=104, SSN=SCMG, NI=NAT, DPC="0x3104", OPC="0x2463", SSNNAME="SG_B";
      ```
6. 配置GT翻译数据。

   1. 增加本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=201, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613742383", DPC="0x2463", NAME="SGSN_BER1-GT";
      ```
   2. 配置到SG的GT翻译数据。

      ```
      ADD SCCPGT: GTX=103, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="86139", DPC="0x3103";
      ```
7. 配置EIR号码。

   ```
   SET MAPFUNC: EIR="8613900503";
   ```

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
6. 检查EIR SCCP子系统的状态。

   ****DSP SCCPSSN****

   * **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN:;%%
     RETCODE = 0  操作成功。

     查询SCCP子系统状态
     ------------------
     子系统索引    子系统号     网络指示语    目的信令点编码    本局信令点编码    子系统状态    是否测试标志    测试忽略标志

     2020          SCMG（1）    国内备用网    0x7EF             0x2               禁止          否              否          
     2021          SCMG（1）    国内备用网    0x7F0             0x2               禁止          否              否          
     2022          SCMG（1）    国内备用网    0x7F1             0x2               禁止          否              否          
     2023          SCMG（1）    国内备用网    0x7F2             0x2               禁止          否              否          
     (结果个数 = 4)
     ---    END
     ```
   * **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。
7. 进行业务测试。

   * 进行业务测试前，需要首先完成SGSN与RNC或PCU、GGSN、HLR的对接。
   * 进行业务测试的手机必须是在对接的EIR开户的手机。

   1. 创建用户跟踪。

      参数选择如下：

      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其它参数：选择默认值。
   2. 创建Gf接口跟踪。

      参数选择如下：

      * Ru名称：资源单元的名称。
      * 进程序号：虚拟机内，SPP进程的同类进程序号。
      * 过滤参数：IMSI（1~15位的十进制数字）或者MSISDN（6~15位的十进制数字）。
      * 其它参数：选择默认值。
   3. 用户开机附着。
   4. 查看Gf接口跟踪结果。
      * **预期结果：**可以看到在指定的检测点处SGSN和PEER间有MAP-OPEN Request/MAP-OPEN Confirm、MAP-SERVICE Request/MAP-SERVICE Confirm消息交互。
      * **异常结果：**观察不到SGSN和PEER之间的交互消息或观察到异常消息。
   5. 查看用户跟踪结果。
      * **预期结果：**用户附着成功，可以观察到Attach Accept消息，如下图所示。

        **图1** 用户跟踪-附着（样例）

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**用户附着失败，观察到Attach Reject消息。
   6. 查询用户MM上下文。

      **DSP COMMMCTX**
      * **预期结果：**可以查询到用户的MM上下文，并且状态为PMM-IDLE或PMM-CONNECTED状态。
      * **异常结果：**查询不到用户的MM上下文。

版权所有 © 华为技术有限公司
