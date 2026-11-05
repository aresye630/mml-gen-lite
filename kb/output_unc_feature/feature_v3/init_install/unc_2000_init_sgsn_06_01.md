# 配置到MSC/VLR的数据（Over IP）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MSC/VLR或SGSN时，在配置完成SGSN到MSC/VLR的路由数据后，可通过配置M3UA链路数据建立SGSN到MSC/VLR的逻辑连接。

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
| ****SET LICENSESWITCH**** | License项（LICITEM） | LKV2GSINTF02 |  | 参见“水平网设LLD文档 ”。 | 打开支持Gs接口特性的License配置开关。 |
|  | 开关（SWITCH） | ENABLE |  |  |  |
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
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 |  |  | 配置MSC/VLR业务IP。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.11.150.1 |  |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |  |
| ****ADD M3LE**** | 本地实体索引（LEX） | 0 |  |  | 配置M3UA信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本地实体编码（OPC） | 0x30a |  |  |  |
|  | 本地实体类型（LET） | IPSP |  |  |  |
|  | 路由上下文（RC） | 123456 |  |  |  |
|  | 网络外貌（NA） | 789456 |  |  |  |
|  | 本地实体名（LEN） | to SS7 |  |  |  |
| ****ADD M3LKS**** | 链路集索引（LSX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 3 |  |  |  |
|  | 链路选择掩码（SLSM） | B0010 |  |  |  |
|  | 工作模式（WM） | IPSP |  |  |  |
|  | 业务模式（TM） | LOADSHARE |  |  |  |
|  | 链路集名（LSN） | to HLR |  |  |  |
| ****ADD M3DE**** | 目的实体索引（DEX） | 3 |  |  |  |
|  | 本地实体索引（LEX） | 0 |  |  |  |
|  | 目的实体编码（DPC） | 0x20b |  |  |  |
|  | 链路集选择掩码（SLSSM） | B0000 |  |  |  |
|  | 目的实体类型（DET） | IPSP |  |  |  |
|  | 相邻标记（ADJF） | TRUE |  |  |  |
|  | 路由上下文（RC） | 123456 |  |  |  |
|  | M3UA协议版本（PVER） | RFC3332 |  |  |  |
|  | 目的实体名（DEN） | to HLR |  |  |  |
| ****ADD M3RT**** | 路由索引（RTX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 3 |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | 信令路由名（RTN） | to HLR |  |  |  |
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
|  | SCTP 参数索引（SCTPINDX） | 1 |  |  |  |
|  | 链路名（LKN） | To HLR LINK2 |  |  |  |
| ****ADD SCCPSSN**** | 子系统索引（SSNX） | 0 |  |  | 配置SCCP信令数据。 |
|  | 子系统号（SSN） | SGSN |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 目的信令点编码（DPC） | 0x30a |  |  |  |
|  | 本局信令点编码（OPC） | 0x30a |  |  |  |
|  | 子系统名（SSNNAME） | SGSN TO SGSN |  |  |  |
| ****ADD IMSIGT**** | IMSI前缀（IMSIPRE） | 46000 |  |  | 配置GT翻译数据。 |
|  | 国家代码\_网络接入号（GT） | 86139 |  |  |  |
|  | 移动网络名称（MNNAME） | MOBLIE |  |  |  |
| ****ADD HPLMN**** | 移动国家码（MCC） | 460 |  |  |  |
|  | 移动网号（MNC） | 00 |  |  |  |
|  | 国家码（CC） | 86 |  |  |  |
| ****ADD SCCPDPC**** | 目的信令点索引（DPX） | 3 |  |  | 配置SCCP信令数据。 |
|  | 本局信令点索引（OPX） | 1 |  |  |  |
|  | 目的信令点编码（DPC） | 0x20b |  |  |  |
|  | 负荷分担类型（LDP） | NOUSE |  |  |  |
|  | 子系统号（DPN） | TO HLR |  |  |  |
| **ADD SCCPOPC** | 本局信令点索引（OPX） | 1 |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本局信令点编码（OPC） | 0x30a |  |  |  |
|  | 信令点用途（SPN） | IUANDCORE |  |  |  |
|  | 本局SGSN号（SGSNN） | 8613912345 |  |  |  |
|  | 本局信令点名（OPN） | TO RNC AND SS7 |  |  |  |
| ****ADD SCCPGT**** | GT码索引（GTX） | 0 |  |  | 配置GT翻译数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 翻译结果类型（RT） | DPC |  |  |  |
|  | GT码表示语（GTEXP） | FOUR |  |  |  |
|  | 编号计划（NP） | ISDNP |  |  |  |
|  | 地址性质表示语（ADDREXP） | INTDN |  |  |  |
|  | 地址信息（ADDR） | 8613912345 |  |  |  |
|  | 目的信令点编码（DPC） | 0x30a |  |  |  |
|  | SCCP GT名称（NAME） | SGSN |  |  |  |
| ****ADD VLR**** | VLR号（VN） | 861390111 |  |  | 配置VLR相关数据。 |
|  | VLR名称（VNM） | noname |  |  |  |
| ****ADD LAIVLR**** | LAI（BGNLAI） | 460001234 |  |  |  |
|  | VLR号（VLRNO） | 861390111 |  |  |  |
| ****ADD NRA**** | LAI（LAI） | 460001234 |  |  |  |
|  | RAC（RAC） | 01 |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开支持Gs接口特性的License配置开关。

   ```
   SET LICENSESWITCH: LICITEM="LKV2GSINTF02", SWITCH=ENABLE;
   ```
3. 配置本局信令属性。

   ```
   SET SIGATTR: IF=LABEL24, IRF=LABEL14, NF=LABEL14, NRF=LABEL14, M3UASTPF=DISABLE, BSSAPPF=ENABLE, BSSAPPNO=252, BSSAPPNI=DISUSED, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
4. **可选：**配置MSC/VLR业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.151.113", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.151.114", VPNINSTNAME="VPN_SIG";
   ```
5. 配置M3UA信令数据。

   1. 配置M3UA本地实体。

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x1064", LET=IPSP, RC=123456, NA=789456, LEN="SGSN_Gs";
      ```
   2. 配置M3UA目的实体。

      ```
      ADD M3DE: DEX=0, LEX=0, DPC="0x106a", SLSSM=B0000, DET=IPSP, ADJF=TRUE, RC=123456, PVER=RFC3332, DEN="MSC";
      ```
   3. 配置到MSC/VLR的信令链路集。

      ```
      ADD M3LKS: LSX=0, DEX=0, SLSM=B0001, WM=IPSP, TM=LOADSHARE, LSN="To MSC";
      ```
   4. 配置到MSC/VLR的M3UA路由。

      ```
      ADD M3RT: RTX=0, DEX=0, LSX=0, PRI=0, RTN="To MSC";
      ```
   5. 配置M3UA信令链路。

      ```
      ADD M3LNK:LNK=1,VPNNAME="VPN_SIG",IPT=IPV4,LOCIPV41="10.10.151.113",LOCIPV42="10.10.151.114",PEERIPV41="10.22.133.143",PEERIPV42="10.22.133.144",PEERPORT=2905,CS=C,LSX=0,SCTPINDX=2,LKN="To MSC/VLR";
      ```
6. 配置SCCP信令数据。

   1. 增加SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=1, NI=NAT, OPC="0x1064", SPN=COREONLY, SGSNN="8613912345";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=1, OPX=1, DPC="0x106a", DPN="MSC";
      ```
   3. 增加SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=1, SSN=SCMG, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN internal";
      ADD SCCPSSN: SSNX=2, SSN=BSSAP+, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN internal";
      ```
   4. 配置SCCP子系统。

      ```
      ADD SCCPSSN: SSNX=3, SSN=SCMG, NI=NAT, DPC="0x106a", OPC="0x1064", SSNNAME="TO MSC";
      ADD SCCPSSN: SSNX=4, SSN=BSSAP+, NI=NAT, DPC="0x106a", OPC="0x1064", SSNNAME="TO MSC";
      ```
7. 配置GT翻译数据

   1. 增加本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=0, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613912345", DPC="0x1064", NAME="SGSN";
      ```
   2. 配置到MSC/VLR的GT翻译数据，翻译结果类型为DPC。

      ```
      ADD SCCPGT: GTX=1, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDR="861390111", DPC="0x106a", NAME="TO MSC";
      ```
8. 配置VLR相关数据。

   1. 配置VLR的号码。

      ```
      ADD VLR: VN="861390111", VNM="noname";
      ```
   2. 配置VLR的位置区。

      ```
      ADD LAIVLR: BGNLAI="460001234", VLRNO="861390111"; 
      ADD LAIVLR: BGNLAI="460001235", VLRNO="861390111"; 
      ADD LAIVLR: BGNLAI="460001236", VLRNO="861390111";
      ```
   3. 增加一个路由区标识为460001234的空路由区。

      ```
      ADD NRA: LAI="460001234", RAC="01";
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
6. 检查MSC/VLR SCCP子系统的状态。

   ****DSP SCCPSSN****

   * **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN:;%%
     RETCODE = 0  操作成功。

     查询SCCP子系统状态
     ------------------
     子系统索引    子系统号     网络指示语    目的信令点编码    本局信令点编码    子系统状态    是否测试标志    测试忽略标志

     2020          SCMG（1）    国内备用网    0x7EF             0x2               允许          否              否          
     2021          SCMG（1）    国内备用网    0x7F0             0x2               允许          否              否          
     2022          SCMG（1）    国内备用网    0x7F1             0x2               允许          否              否          
     2023          SCMG（1）    国内备用网    0x7F2             0x2               允许          否              否          
     2024          SCMG（1）    国内备用网    0x7F3             0x2               允许          否              否          
     (结果个数 = 5)
     ---    END
     ```
   * **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。
7. 进行业务测试。

   * 进行业务测试前，需要首先完成SGSN与RNC或PCU、HLR的对接。
   * 进行业务测试的手机必须支持同时附着CS/PS网络。

   1. 创建用户跟踪。

      参数选择如下：
      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其它参数：选择默认值。
   2. 创建Gs接口跟踪。

      参数选择如下：
      * Ru名称：资源单元的名称。
      * 进程序号：虚拟机内，SPP进程的同类进程序号。
      * VLR号：VLR号码，长度为15的数字串。
      * 过滤参数：IMSI（1~15位的十进制数字）或者MSISDN（6~15位的十进制数字）。
      * 其它参数：选择默认值。
   3. 用户开机附着。
   4. 查看Gs接口跟踪结果。
      * **预期结果：**可以看到SGSN和MSC间有消息交互，包括BSSAP+-LOCATION-UPDATE-REQUEST、BSSAP+-LOCATION-UPDATE-ACCEPT及BSSAP+-TMSI-REALLOCATION-COMPLETE消息。
      * **异常结果：**MSC temporarily not reachable。
   5. 查看用户跟踪结果。
      * **预期结果：**用户附着成功，可以观察到Attach Accept消息，如下图所示。

        **图1** 用户跟踪-附着（样例）

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**用户附着失败，观察到PMM\_ATTACH\_REJ消息。
   6. 查询用户MM上下文。

      **DSP COMMMCTX**

      * **预期结果：**可以查询到用户的MM上下文，并且状态为PMM-IDLE或PMM-CONNECTED状态。
      * **异常结果：**查询不到用户的MM上下文。

版权所有 © 华为技术有限公司
