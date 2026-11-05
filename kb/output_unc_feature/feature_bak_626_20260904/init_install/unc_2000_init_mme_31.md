# 配置到GMLC的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增GMLC或MME时，在配置完成MME到GMLC的路由数据后，可通过配置SLg接口数据建立MME到GMLC的逻辑连接。

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

| 类别            | 参数名称                      | 取值样例                                    | 取值样例.1                                  | 获取方法            | 说明               |
|:--------------|:--------------------------|:----------------------------------------|:----------------------------------------|:----------------|:-----------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                                    | IPv4                                    | 参见“水平网设LLD文档 ”。 | 配置Slg接口业务IP。     |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 10.11.11.11、10.11.11.12                 | 10.11.11.11、10.11.11.12                 | 参见“水平网设LLD文档 ”。 | 配置Slg接口业务IP。     |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_SIG                                 | VPN_SIG                                 | 参见“水平网设LLD文档 ”。 | 配置Slg接口业务IP。     |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置SCTP参数。        |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | For_SLg                                 | For_SLg                                 | 参见“水平网设LLD文档 ”。 | 配置SCTP参数。        |
| ADD DMPE      | 对端实体索引（PEERIDX）           | 1                                       | 1                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。  |
| ADD DMPE      | 对端主机名（PEERHTNAM）          | gmlc1.epc.mnc015.mcc123.3gppnetwork.org | gmlc1.epc.mnc015.mcc123.3gppnetwork.org | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。  |
| ADD DMPE      | 对端实体名（PEERNAM）            | gmlc1                                   | gmlc1                                   | 参见“水平网设LLD文档 ”。 | 配置Diameter对端信息。  |
| ADD DMLKS     | Diameter链路集索引（LINKSIDX）   | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集信息。 |
| ADD DMLKS     | 本地实体索引（LOCALIDX）          | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集信息。 |
| ADD DMLKS     | 本地实体索引（PEERIDX）           | 1                                       | 1                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集信息。 |
| ADD DMLKS     | 选路模式（LSSELMODE）           | SELMODE_LOAD_BALAN                      | SELMODE_LOAD_BALAN                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集信息。 |
| ADD DMLKS     | 链路集名称（LINKSNAM）           | LNKS1_GMLC1                             | LNKS1_GMLC1                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集信息。 |
| ADD DMRT      | 路由索引（ROUTEIDX）            | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMRT      | 是否默认路由（ISDEFAULT）         | NO                                      | NO                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMRT      | 选路模式（RSELMODE）            | SELMODE_ROUND_ROBIN                     | SELMODE_ROUND_ROBIN                     | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMRT      | 目的实体域名（REALMNAME）         | epc.mnc015.mcc123.3gppnetwork.org       | epc.mnc015.mcc123.3gppnetwork.org       | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMRT      | 对端实体索引（PEERIDX）           | 1                                       | 1                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMRT      | 路由名称（ROUTENAM）            | ROUTE1_GMLC1                            | ROUTE1_GMLC1                            | 参见“水平网设LLD文档 ”。 | 配置Diameter路由信息。  |
| ADD DMLNK     | 链路索引（LINKIDX）             | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | IP地址类型（IPTYPE）            | TPTADDR_TYPE_IPV4                       | TPTADDR_TYPE_IPV4                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 本地IPv4地址1（LOCALIPV4_1）    | 10.11.11.11                             | 10.11.11.11                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 本地IPv4地址2（LOCALIPV4_2）    | 10.11.11.12                             | 10.11.11.12                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 本地端口号（LOCALPORT）          | 3868                                    | 3868                                    | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 对端IPv4地址1（PEERIPV4_1）     | 10.2.3.4                                | 10.2.3.4                                | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 对端IPv4地址2（PEERIPV4_2）     | 10.2.3.5                                | 10.2.3.5                                | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 对端端口号（PEERPORT）           | 3868                                    | 3868                                    | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | Diameter链路集索引（LINKSIDX）   | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | SCTP协议参数索引（SCTPINDX）      | 0                                       | 0                                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD DMLNK     | 链路名称（LINKNAM）             | DMLNK1_GMLC1                            | DMLNK1_GMLC1                            | 参见“水平网设LLD文档 ”。 | 配置Diameter链路信息。  |
| ADD GMLC      | GMLC 标识 （GMLCID）          | 1                                       | 1                                       | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC所属MCC （MCC）           | 640                                     | 640                                     | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC所属MNC （MNC）           | 000                                     | 000                                     | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC IP地址类型 （GMLCIPT）     | IPV4                                    | IPV4                                    | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC IPV4地址 （GMLCIPV4）    | 10.2.3.4、10.2.3.5                       | 10.2.3.4、10.2.3.5                       | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC 号码 （GMLCNO）          | 123456                                  | 123456                                  | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | GMLC 主机名 （HSNM）           | gmlc1.epc.mnc015.mcc123.3gppnetwork.org | gmlc1.epc.mnc015.mcc123.3gppnetwork.org | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLC      | 接口类型（IFTYPE）              | SLg-1                                   | SLg-1                                   | 参见“水平网设LLD文档 ”。 | 增加GMLC配置。        |
| ADD GMLCAU    | GMLC 标识（GMLCID）           | 1                                       | 1                                       | 参见“水平网设LLD文档 ”。 | 配置GMLC的权限信息。     |
| ADD GMLCAU    | 支持的客户端类型 （CLTTYPE）        | VALUE_ADDED_SERVICES                    | VALUE_ADDED_SERVICES                    | 参见“水平网设LLD文档 ”。 | 配置GMLC的权限信息。     |
| ADD GMLCAU    | 支持的LCS业务类型 （SERTYPE）      | 3                                       | 3                                       | 参见“水平网设LLD文档 ”。 | 配置GMLC的权限信息。     |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Slg接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.11.11", VPNINSTNAME="VPN_SIG";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.11.11.12", VPNINSTNAME="VPN_SIG";
   ```
3. 配置SCTP参数。

   ```
   ADD SCTPPARA: SCTPPARAINDEX=0,SCTPPARANAME="For_SLg";
   ```
4. 配置Diameter对端信息

   ```
   ADD DMPE: PEERIDX=1, PEERHTNAM="gmlc1.epc.mnc015.mcc123.3gppnetwork.org", PEERNAM="gmlc1";
   ```
5. 配置Diameter链路集信息。

   ```
   ADD DMLKS: LINKSIDX=0, LOCALIDX=0, PEERIDX=1, LSSELMODE=SELMODE_LOAD_BALAN, LINKSNAM="LNKS1_GMLC1";
   ```
6. 配置Diameter路由信息。

   ```
   ADD DMRT: ROUTEIDX=0, ISDEFAULT=NO, RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc.mnc015.mcc123.3gppnetwork.org", PEERIDX=1, ROUTENAM="ROUTE1_GMLC1";
   ```
7. 配置Diameter链路信息。

   ```
   ADD DMLNK: LINKIDX=0, IPTYPE=TPTADDR_TYPE_IPV4, LOCALIPV4_1="10.11.11.11", LOCALIPV4_2="10.11.11.12", LOCALPORT=3868, PEERIPV4_1="10.2.3.4", PEERIPV4_2="10.2.3.5", PEERPORT=3868, LINKSIDX=0, SCTPINDX=0, LINKNAM="DMLNK1_GMLC1";
   ```
8. 增加GMLC配置。

   ```
   ADD GMLC: GMLCID=1, MCC="640", MNC="000", GMLCIPT=IPV4, GMLCIPV4="10.2.3.4", GMLCNO="123456", HSNM="gmlc1.epc.mnc015.mcc123.3gppnetwork.org", IFTYPE=SLg-1; 
   ADD GMLC: GMLCID=1, MCC="640", MNC="000", GMLCIPT=IPV4, GMLCIPV4="10.2.3.5", GMLCNO="123456", HSNM="gmlc1.epc.mnc015.mcc123.3gppnetwork.org", IFTYPE=SLg-1;
   ```
9. 配置GMLC的权限信息。

   ```
   ADD GMLCAU: GMLCID=1, CLTTYPE=VALUE_ADDED_SERVICES, SERTYPE=3;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 查询当前配置的本地实体信息。

   **LST DMLE**

   **DSP DMLE**
   - **预期结果：**显示所有已经配置本地实体的配置信息、状态信息。

     ```
     %%LST DMLE: LOINDEX=0;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
       本地实体索引  =  0
     本地实体主机名  =  mme.epc.mnc015.mcc123.3gppnetwork.org
       本地实体域名  =  epc.mnc015.mcc123.3gppnetwork.org
             产品名  =  MME
         本地实体名  =  mme
     (结果个数 = 1)
     ```

     ```
     %%DSP DMLE:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
     本地实体索引  =  0
       本地实体名  =  mme
         实体状态  =  正常
     (结果个数 = 1)
     ```
   - **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证UNC能够正确查询对端实体状态。

   **LST DMPE**

   **DSP DMPE**
   - **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST DMPE:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
      对端实体索引  对端主机名             对端实体名        节点支持的应用

      0        gmlc1.epc.mnc015.mcc123.3gppnetwork.org    NULL               SLG:2                      
      1        gmlc2.epc.mnc015.mcc123.3gppnetwork.org    NULL               SLG:2                      
     (Number of results = 2)

     ---    END
     ```

     ```
     %%DSP DMPE:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
      对端实体索引  对端实体名  实体状态

      0             huaweiGMLC1  正常    
      1             huaweiGMLC2  正常    
     (结果个数 = 2)

     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
4. 验证UNC能够正确查询Diameter链路集状态。

   **LST DMLKS**

   **DSP DMLKS**

   - **预期结果：**显示所有已经配置Diameter链路集的配置信息、状态信息。

     ```
     LST DMLKS:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
      Diameter链路集索引  本地实体索引  对端实体索引  选路模式  链路集名称

      0           0             0             主从      To-GMLC0    
      1           0             1             主从      To-GMLC1    
     (结果个数 = 2)
     ```

     ```
     %%DSP DMLKS:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
      Diameter链路集索引  链路集名称  链路集状态

      0                   To-GMLC0     正常      
      1                   To-GMLC1     故障      
     (结果个数 = 2)
     ```
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
5. 验证UNC能够正确查询Diameter路由状态。

   **LST DMRT**

   **DSP DMRT**
   - **预期结果：**显示所有已经配置Diameter路由的配置信息、状态信息。

     ```
     %%LST DMRT: ROUTEIDX=0;%%
     RETCODE = 0  操作成功

     输出结果如下：
     --------------
         路由索引  =  0
         应用名称  =  SLg
      是否默认路由  =  0
         选路模式  =  主从
      目的实体域名  =  gmlc1.epc.mnc015.mcc123.3gppnetwork.org
      对端实体索引  =  0
         路由名称  =  rt1
     (结果个数 = 1)

     ---    END
     ```

     ```
     %%DSP DMRT: ROUTEIDX=0;%%
     RETCODE = 0  操作成功

     输出结果如下：
     --------------
       路由索引  =  0
       路由名称  =  rt1
       路由状态  =  正常
      (结果个数 = 1)
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80592 Diameter路由不可用**。
6. 验证UNC能够正确查询Diameter链路状态。

   **LST DMLNK**: LINKIDX="链路索引";

   **DSP DMLNK**: LINKIDX="链路索引";
   - **预期结果：**显示所有已经配置Diameter链路的配置信息、状态信息，此处以IPv4为例。

     ```
     %%LST DMLNK:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
      链路索引  vpn名称  IP地址类型  协议类型  本地地址1      本地地址2        本地端口号  对端地址1      对端地址2        对端端口号  C/S模式   Diameter链路集索引  SCTP协议参数索引  链路名称  交叉路径是否可用

      0         UNC1    IPv4        SCTP      192.168.15.10     255.255.255.255  3868       192.168.15.16      255.255.255.255  3868       服务器端   0                   0                 To-GMLC0   否              
      1         UNC2    IPv4        SCTP      192.168.15.20     192.168.15.30       3868       192.168.15.26      192.168.15.36       3868       服务器端   1                   0                 To-GMLC1   是              
     (结果个数 = 2)
     ```

     ```
     %%DSP DMLNK:;%%
     RETCODE = 0  操作成功

     输出结果如下
     --------------
     链路索引    链路名称     RU名称            进程序号       链路状态

     2           noname       USN_SP_RU_0066    1              正常        
     1           noname       USN_SP_RU_0066    3              正常        
     0           noname       USN_SP_RU_0066    4              正常        
     6           noname       USN_SP_RU_0066    2              正常        
     (结果个数 = 4)
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
7. 进行业务测试。

   **说明** 

   进行业务测试前，需要首先完成UNC与eNodeB、GMLC、E-SMLC的链路配置。

   1. 创建用户跟踪。

      参数选择如下：
      - IMSI/MSISDN/用户索引号：被跟踪用户的IMSI、MSISDN或者用户索引号。
      - 其他参数：选择默认值。
   2. 创建Diameter接口跟踪。

      参数选择如下：

      链路号：Diameter Link的索引号。
   3. 用户开机，进行附着。
   4. GMLC发起LCS定位请求。
   5. 查看Diameter接口跟踪结果。
      - **预期结果：**可以看到Location Service Request和Location Service Response消息，如图1所示。

        **图1** Location Service流程消息（样例）
      - 异常结果：观察不到Diameter接口跟踪消息或观察到的消息异常。
   6. 查看用户跟踪结果。
      - **预期结果：**用户附着成功，可以在消息方向处看到LCS模块与UDM模块之间有消息交互，如图2所示。

        **图2** 用户跟踪-附着流程（样例）
      - **异常结果：**观察不到LCS模块与UDM模块之间的消息或观察到的消息异常。