# 配置到SG的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增SG或SGSN时，在配置完成SGSN到SG的路由数据后，可通过配置M3UA链路数据建立SGSN到SG的逻辑连接。

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
|  | 业务IPv4地址（SERVICEIPV4） | 10.133.95.5、10.133.95.6、10.133.127.5、10.133.127.6 |  |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |  |
| ****SET SIGATTR**** | 国际网标志（IF） | INVALID |  |  | 配置本局信令网属性。 |
|  | 国际备用网标志（IRF） | INVALID |  |  |  |
|  | 国内网标志（NF） | LABEL14 |  |  |  |
|  | 国内备用网标志（NRF） | LABEL14 |  |  |  |
|  | M3UA STP功能（M3UASTPF） | DISABLE |  |  |  |
|  | 是否支持BSSAP+（BSSAPPF） | DISABLE |  |  |  |
|  | BSSAP+子系统号（BSSAPPNO） | 252 |  |  |  |
|  | BSSAP+所在信令网（BSSAPPNI） | NAT |  |  |  |
|  | MAP所在信令网（MAPNI） | NAT |  |  |  |
|  | 信令网协议类型（SS7T） | ITUT\_SS7(ITUT\_SS7) |  |  |  |
| ****ADD M3LE**** | 本地实体索引（LEX） | 0 |  |  | 配置M3UA信令数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本地实体编码（OPC） | 0x1064 |  |  |  |
|  | 本地实体类型（LET） | ASP |  |  |  |
|  | 本地实体名（LEN） | SGSN\_Gr |  |  |  |
| ****ADD M3LKS**** | 链路集索引（LSX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 1 |  |  |  |
|  | 链路选择掩码（SLSM） | B0001 |  |  |  |
|  | 工作模式（WM） | ASP |  |  |  |
|  | 业务模式（TM） | LOADSHARE |  |  |  |
|  | 链路集名（LSN） | To SG\_A |  |  |  |
| ****ADD M3DE**** | 目的实体索引（DEX） | 1 |  |  |  |
|  | 本地实体索引（LEX） | 0 |  |  |  |
|  | 目的实体编码（DPC） | 0x101a |  |  |  |
|  | 链路集选择掩码（SLSSM） | B0000 |  |  |  |
|  | 目的实体类型（DET） | SGP |  |  |  |
|  | 相邻标记（ADJF） | TRUE |  |  |  |
|  | M3UA协议版本（PVER） | RFC3332 |  |  |  |
|  | 目的实体名（DEN） | SG\_A |  |  |  |
| ****ADD M3RT**** | 路由索引（RTX） | 1 |  |  |  |
|  | 目的实体索引（DEX） | 1 |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | 优先级（PRI） | 0 |  |  |  |
|  | 信令路由名（RTN） | To SG\_A |  |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 1 |  |  |  |
|  | SCTP协议参数名（SCTPPARANAME） | sctppara1 |  |  |  |
| ****ADD M3LNK**** | 链路号（LNK） | 1 |  |  |  |
|  | VPN名称（VPNNAME） | VPN\_SIG |  |  |  |
|  | IP类型（IPT） | IPV4 |  |  |  |
|  | 本地IPv4地址1（LOCIPV41） | 10.133.95.5 |  |  |  |
|  | 本地IPv4地址2（LOCIPV42） | 10.133.95.6 |  |  |  |
|  | 本地端口号（LOCPORT） | 2905 |  |  |  |
|  | 对端IP地址1（PEERIPV41） | 10.10.137.143 |  |  |  |
|  | 对端IP地址2（PEERIPV42） | 10.10.137.207 |  |  |  |
|  | 对端端口号（PEERPORT） | 2905 |  |  |  |
|  | C/S模式（CS） | C |  |  |  |
|  | 链路集索引（LSX） | 1 |  |  |  |
|  | SCTP 参数索引（SCTPINDX） | 1 |  |  |  |
|  | 链路名（LKN） | To SG\_A |  |  |  |
| ****ADD SCCPSSN**** | 子系统索引（SSNX） | 0 |  |  | 配置SCCP信令数据。 |
|  | 子系统号（SSN） | SGSN |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 目的信令点编码（DPC） | 0x1064 |  |  |  |
|  | 本局信令点编码（OPC） | 0x1064 |  |  |  |
|  | 子系统名（SSNNAME） | SGSN internal |  |  |  |
| ****ADD IMSIGT**** | IMSI前缀（IMSIPRE） | 46000 | 60100 |  | 配置GT翻译数据。 |
|  | 国家代码\_网络接入号（GT） | 86139 | 213639 |  |  |
|  | 移动网络名称（MNNAME） | MOBLIE |  |  |  |
| ****ADD HPLMN**** | 移动国家码（MCC） | 460 |  |  |  |
|  | 移动网号（MNC） | 00 |  |  |  |
|  | 国家码（CC） | 86 |  |  |  |
| ****ADD CONNECTPLMN**** | 移动国家码（MCC） | 601 |  |  |  |
|  | 移动网号（MNC） | 00 |  |  |  |
|  | 国家码（CC） | 213 |  |  |  |
|  | 运营商标识（NOID） | 0 |  |  |  |
|  | 是否允许SM业务（SM） | YES |  |  |  |
|  | 是否允许SMS业务（SMS） | NO |  |  |  |
|  | 专属互连PLMN（EXCLUSIVEPLMN） | NO |  |  |  |
| ****ADD SCCPDPC**** | 目的信令点索引（DPX） | 1、2 |  |  | 配置SCCP信令数据。 |
|  | 本局信令点索引（OPX） | 1 |  |  |  |
|  | 目的信令点编码（DPC） | 0x101a、0x101b |  |  |  |
|  | 负荷分担类型（LDP） | LOADSHARE |  |  |  |
|  | 负荷分担目的信令点索引（SDPX） | 1、2 |  |  |  |
|  | 子系统号（DPN） | SG\_A、SG\_B |  |  |  |
| **ADD SCCPOPC** | 本局信令点索引（OPX） | 1 |  |  |  |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 本局信令点编码（OPC） | 0x1064 |  |  |  |
|  | 信令点用途（SPN） | COREONLY |  |  |  |
|  | 本局SGSN号（SGSNN） | 86139000704 |  |  |  |
|  | 本局信令点名（OPN） | For Gr |  |  |  |
| ****ADD SCCPGT**** | GT码索引（GTX） | 0 |  |  | 配置GT翻译数据。 |
|  | 网络指示语（NI） | NAT |  |  |  |
|  | 翻译结果类型（RT） | DPC |  |  |  |
|  | GT码表示语（GTEXP） | FOUR |  |  |  |
|  | 编号计划（NP） | ISDNP |  |  |  |
|  | 地址性质表示语（ADDREXP） | INTDN |  |  |  |
|  | 地址信息（ADDR） | 86139000704 |  |  |  |
|  | 目的信令点编码（DPC） | 0x1064 |  |  |  |
|  | SCCP GT名称（NAME） | SGSN |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置SG业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.133.95.5", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.133.95.6", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.133.127.5", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.133.127.6", VPNINSTNAME="VPN_SIG";
   ```
3. 配置SGSN网元上的本局信令网属性。

   ```
   SET SIGATTR: IF=INVALID, IRF=INVALID, NF=LABEL14, NRF=LABEL14, M3UASTPF=DISABLE, BSSAPPF=DISABLE, BSSAPPNO=252, BSSAPPNI=NAT, MAPNI=NAT, SS7T=ITUT_SS7;
   ```
4. **可选：**配置M3UA信令数据。

   1. 配置M3UA本地实体。

      ```
      ADD M3LE: LEX=0, NI=NAT, OPC="0x1064", LET=ASP, LEN="SGSN_Gr";
      ```
   2. 配置M3UA目的实体。

      ```
      ADD M3DE: DEX=1, LEX=0, DPC="0x101a", SLSSM=B0000, DET=SGP, ADJF=TRUE, PVER=RFC3332, DEN="SG_A";
      ADD M3DE: DEX=0, LEX=0, DPC="0x101b", SLSSM=B0000, DET=SGP, ADJF=TRUE, PVER=RFC3332, DEN="SG_B";
      ```
   3. 本局新增两个相邻的信令点SG A、SG B，配置两条信令链路集，分别到SG A和SG B，链路集的工作模式为ASP，业务模式为负荷分担模式，即到某一目的信令点（如HLR）的信令通过SG A和SG B负荷分担。

      ```
      ADD M3LKS: LSX=1, DEX=1, SLSM=B0001, WM=ASP, TM=LOADSHARE, LSN="To SG_A";
      ADD M3LKS: LSX=0, DEX=0, SLSM=B0001, WM=ASP, TM=LOADSHARE, LSN="To SG_B";
      ```
   4. 配置M3UA路由，分别到SG A和SG B。

      ```
      ADD M3RT: RTX=1, DEX=1, LSX=1, PRI=0, RTN="To SG_A";
      ADD M3RT: RTX=0, DEX=0, LSX=0, PRI=0, RTN="To SG_B";
      ```
   5. 配置SCTP协议参数。

      ```
      ADD SCTPPARA: SCTPPARAINDEX=1, SCTPPARANAME="sctppara1";
      ```
   6. 配置M3UA信令链路，到SG A和SG B均增加两条M3UA链路，两条信令链路实现负荷分担，并由对应框的物理链路来承载信令链路，每条链路均采用SCTP多归属方式，本地和对端端口号均为2905，本端为客户端模式。

      ```
      ADD M3LNK: LNK=1, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.133.95.5", LOCIPV42="10.133.95.6", LOCPORT=2905, PEERIPV41="10.10.137.143", PEERIPV42="10.10.137.207", PEERPORT=2905, CS=C, LSX=1, SCTPINDX=1, LKN="To SG_A"; 
      ADD M3LNK: LNK=2, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.133.127.6", LOCIPV42="10.133.127.5", LOCPORT=2905, PEERIPV41="10.10.137.143", PEERIPV42="10.10.137.207", PEERPORT=2905, CS=C, LSX=1, SCTPINDX=1, LKN="To SG_A"; 
      ADD M3LNK: LNK=3, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.133.95.5", LOCIPV42="10.133.95.6", LOCPORT=2905, PEERIPV41="10.10.137.148", PEERIPV42="10.10.137.212", PEERPORT=2905, CS=C, LSX=0, SCTPINDX=1, LKN="To SG_B"; 
      ADD M3LNK: LNK=4, VPNNAME="VPN_SIG",IPT=IPV4, LOCIPV41="10.133.127.6", LOCIPV42="10.133.127.5", LOCPORT=2905, PEERIPV41="10.10.137.148", PEERIPV42="10.10.137.212", PEERPORT=2905, CS=C, LSX=0, SCTPINDX=1, LKN="To SG_B";
      ```
5. 配置SCCP信令数据。

   1. 配置SCCP本局信令点。

      ```
      ADD SCCPOPC: OPX=1, NI=NAT, OPC="0x1064", SPN=COREONLY, SGSNN="86139000704", OPN="For Gr";
      ```
   2. 配置SCCP目的信令点。

      ```
      ADD SCCPDPC: DPX=2, OPX=1, DPC="0x101b", LDP=LOADSHARE, SDPX=1, DPN="SG_B"; ADD SCCPDPC: DPX=1, OPX=1, DPC="0x101a", LDP=LOADSHARE, SDPX=2, DPN="SG_A";
      ```
   3. 配置SCCP本局子系统。

      ```
      ADD SCCPSSN: SSNX=0, SSN=SGSN, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN internal"; 
      ADD SCCPSSN: SSNX=1, SSN=SCMG, NI=NAT, DPC="0x1064", OPC="0x1064", SSNNAME="SGSN internal";
      ```
   4. 配置到不同SG的SCCP子系统，均为SCMG子系统。

      ```
      ADD SCCPSSN: SSNX=7, SSN=SCMG, NI=NAT, DPC="0x101a", OPC="0x1064", SSNNAME="TO SG_A"; 
      ADD SCCPSSN: SSNX=8, SSN=SCMG, NI=NAT, DPC="0x101b", OPC="0x1064", SSNNAME="TO SG_B";
      ```
6. 配置GT翻译数据。

   1. 配置到本地HLR的IMSI-GT转换关系。

      ```
      ADD IMSIGT: IMSIPRE="46000", GT="86139";
      ```
   2. 配置到外网HLR的IMSI-GT转换关系。

      ```
      ADD IMSIGT: IMSIPRE="60100", GT="213639", MNNAME="MOBILE";
      ```
   3. 配置SGSN归属于一个PLMN。

      ```
      ADD HPLMN: MCC="460", MNC="00", CC="86";
      ```
   4. 配置SGSN归属的PLMN，实现用户在不同PLMN的漫游。

      ```
      ADD CONNECTPLMN: MCC="601", MNC="00", CC="213", NOID=0, SM=YES, SMS=NO, EXCLUSIVEPLMN=NO;
      ```

      为了寻址HLR，需要配置IMSI-GT转换关系。如果本网中规划与多个PLMN中的多个HLR互连，实现在多个不同PLMN之间用户的漫游，需要配置多条IMSI-GT转换关系，并相应配置互联PLMN。
   5. 配置本局GT翻译数据。

      ```
      ADD SCCPGT: GTX=0, NI=NAT, RT=DPC, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="86139000704", DPC="0x1064", NAME="SGSN";
      ```
   6. 配置到SG的GT翻译数据，由于SG A与SG B为负荷分担信令点，DPC为两者之一即可。

      ```
      ADD SCCPGT: GTX=25, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="9", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=24, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=23, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="7", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=22, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="6", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=21, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="5", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=20, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="4", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=19, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="3", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=18, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="2", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=17, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="1", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=16, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="0", DPC="0x101b", NAME="TO SG_B";

      ADD SCCPGT: GTX=35, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="0", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=34, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="1", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=33, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="2", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=32, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="3", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=31, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="4", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=30, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="5", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=29, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="6", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=28, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="7", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=27, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="8", DPC="0x101b", NAME="TO SG_B";
      ADD SCCPGT: GTX=26, NI=NAT, RT=DPCGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="9", DPC="0x101b", NAME="TO SG_B";
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查M3UA链路的状态。

   ****DSP M3LNK****

   * **预期结果：**“链路状态”字段为“激活”。

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

   ****DSP M3DE****

   * **预期结果：**“是否可达”字段为“是”。

     ```
     %%DSP M3DE: DEX=1;%%
     RETCODE = 0  操作成功。

     查询M3UA目的实体状态
     --------------------
     目的实体索引  =  1
       网络指示语  =  国内备用网
     目的实体编码  =  0x123
     本地实体编码  =  0x12
         是否可达  =  是
         是否拥塞  =  否
     (结果个数 = 1)
     ---    END
     ```
   * **异常结果：**“是否可达”字段为“否”。

     异常处理过程参见ALM-10337 M3UA目的实体不可达。
5. 检查SCCP目的信令点状态。

   ****DSP SCCPDPC****

   * **预期结果：**“信令点状态”字段为“允许”。

     ```
     %%DSP SCCPDPC: DPX=1;%%
     RETCODE = 0  操作成功。

     查询SCCP目的信令点状态
     ----------------------
         目的信令点索引  =  1
             网络指示语  =  国内备用网
         目的信令点编码  =  0x601
         本局信令点编码  =  0x2
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
6. 检查目的信令点SCCP子系统的状态。

   ****DSP SCCPSSN****

   * **预期结果：**“子系统状态”字段为“允许”。

     ```
     %%DSP SCCPSSN: SSNX=1;%%
     RETCODE = 0  操作成功。

     查询SCCP子系统状态
     ------------------
         子系统索引  =  1
           子系统号  =  SGSN（149）
         网络指示语  =  国内备用网
     目的信令点编码  =  0x601
     本局信令点编码  =  0x2
         子系统状态  =  允许
       是否测试标志  =  否
       测试忽略标志  =  否
     (结果个数 = 1)
     ---    END
     ```
   * **异常结果：**“子系统状态”字段为“禁止”。

     异常处理过程参见ALM-10342 SCCP子系统禁止。

版权所有 © 华为技术有限公司
