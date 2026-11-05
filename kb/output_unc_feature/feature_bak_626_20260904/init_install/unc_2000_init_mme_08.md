# 配置到DRA的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到DRA的路由数据后，可通过配置S6a接口数据建立MME到DRA的逻辑连接。

3GPP引入了DRA（Diameter Router Agent）实体，DRA完成类似GERAN/UTRAN网络中的STP（Signaling Translation Point）的功能，根据用户的IMSI、网络域等信息进行域内HSS的寻址或者域间DRA的寻址。根据运营商的网络部署，MME可以通过DRA和HSS对接。

本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据；漫游用户使用归属地HSS，配置指导见本节。不同场景的推荐配置方式见表1。

| 操作场景                  | 配置方式                                                         |
|:----------------------|:-------------------------------------------------------------|
| 漫游场景                  | 方式一：本地用户优先使用MME直连的HSS，配置指导请参考配置到HSS的数据，漫游用户使用归属地HSS，配置指导见本节。 |
| 漫游场景                  | 方式二：本地用户和漫游用户都使用MME直连的HSS，请参考配置到HSS的数据。                      |
| 新增MME(MME直接连HSS)或HSS  | 请参考配置到HSS的数据。                                                |
| 新增MME(MME通过DRA和HSS对接) | 请参考本节。                                                       |

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                      | 取值样例                                   | 获取方法            | 说明                                                                                                                                                                           |
|:--------------|:--------------------------|:---------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                                   | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                    |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 192.168.140.1 192.168.140.17           | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                    |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_SIG                                | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                                                                                                                    |
| ADD SCTPPARA  | SCTP协议参数索引（SCTPPARAINDEX） | 0                                      | 参见“水平网设LLD文档 ”。 | 与DRA对接的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                                              |
| ADD SCTPPARA  | SCTP协议参数名（SCTPPARANAME）   | For_S6a                                | 参见“水平网设LLD文档 ”。 | 与DRA对接的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过LST SCTPPARA来查询已存在的SCTP协议参数记录。                                                                              |
| ADD DMLE      | 本地实体索引（LOINDEX）           | 0                                      | 参见“水平网设LLD文档 ”。 | 系统配置的Diameter本端标识可以通过LST DMLE命令查询。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                               |
| ADD DMLE      | 本地实体主机名（LOHSTNAME）        | mme1.epc.mnc015.mcc123.3gppnetwork.org | 参见“水平网设LLD文档 ”。 | 系统配置的Diameter本端标识可以通过LST DMLE命令查询。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                               |
| ADD DMLE      | 本地实体域名（LORLMNAME）         | epc.mnc015.mcc123.3gppnetwork.org      | 参见“水平网设LLD文档 ”。 | 系统配置的Diameter本端标识可以通过LST DMLE命令查询。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                               |
| ADD DMLE      | 产品名（PDTNAME）              | MME                                    | 参见“水平网设LLD文档 ”。 | 系统配置的Diameter本端标识可以通过LST DMLE命令查询。 如果已经存在DMLE，请使用现有的DMLE，无需添加。                                                                                                               |
| ADD DMPE      | 对端实体索引（PEERIDX）           | 0                                      | 参见“水平网设LLD文档 ”。 | 与DRA对接时，Diameter对端信息是对应的DRA信息，而不是HSS的信息。PEERHTNAM是DRA主机名，而不是HSS的主机名。 如果当前配置中存在到某个HSS的直连链路，那么用户同该HSS的非首次接入交互，将优先走此直连链路。详细请参考Diameter路由查找整体层次。                                 |
| ADD DMPE      | 对端主机名（PEERHTNAM）          | dra1.epc.mnc015.mcc123.3gppnetwork.org | 参见“水平网设LLD文档 ”。 | 与DRA对接时，Diameter对端信息是对应的DRA信息，而不是HSS的信息。PEERHTNAM是DRA主机名，而不是HSS的主机名。 如果当前配置中存在到某个HSS的直连链路，那么用户同该HSS的非首次接入交互，将优先走此直连链路。详细请参考Diameter路由查找整体层次。                                 |
| ADD DMLKS     | Diameter链路集索引（LINKSIDX）   | 0                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                               |
| ADD DMLKS     | 本地实体索引（LOCALIDX）          | 0                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                               |
| ADD DMLKS     | 对端实体索引（PEERIDX）           | 0                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路集。                                                                                                                                                               |
| ADD DMLKS     | 链路集名称（LINKSNAM）           | LNKS1_DRA1                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | vpn名称（VPNNAME）            | VPN_SIG                                | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 链路索引（LINKIDX）             | 1                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | IP地址类型（IPTYPE）            | TPTADDR_TYPE_IPV4                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 本端IP地址1（LOCALIPV4_1）      | 192.168.140.1                          | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 本端IP地址2（LOCALIPV4_2）      | 192.168.140.17                         | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 本端端口（LOCALPORT）           | 3868                                   | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 对端IP地址1（PEERIPV4_1）       | 10.80.47.4                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 对端IP地址2（PEERIPV4_2）       | 10.80.47.5                             | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 对端端口（PEERPORT）            | 3868                                   | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | C/S模式（CLIORSER）           | DIAM_CONN_CLIENT                       | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | Diameter链路集索引（LINKSIDX）   | 0                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | SCTP协议参数索引（SCTPINDX）      | 0                                      | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 链路名称（LINKNAM）             | DMLNK1_DRA1                            | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMLNK     | 交叉路径是否可用（CROSSIPFLAG）     | NO                                     | 参见“水平网设LLD文档 ”。 | 配置Diameter链路。                                                                                                                                                                |
| ADD DMRT      | 路由索引（ROUTEIDX）            | 0                                      | 参见“水平网设LLD文档 ”。 | 当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。 当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考配置激活基于权重/优先级的Diameter负荷分担。 |
| ADD DMRT      | 选路模式（RSELMODE）            | SELMODE_MASTER_SLAVE                   | 参见“水平网设LLD文档 ”。 | 当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。 当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考配置激活基于权重/优先级的Diameter负荷分担。 |
| ADD DMRT      | 目的实体域名（REALMNAME）         | epc.mnc015.mcc123.3gppnetwork.org      | 参见“水平网设LLD文档 ”。 | 当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。 当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考配置激活基于权重/优先级的Diameter负荷分担。 |
| ADD DMRT      | 对端实体索引（PEERIDX）           | 0                                      | 参见“水平网设LLD文档 ”。 | 当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。 当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考配置激活基于权重/优先级的Diameter负荷分担。 |
| ADD DMRT      | 路由名称（ROUTENAM）            | rt to dra                              | 参见“水平网设LLD文档 ”。 | 当DRA采用冗余组网时，UNC需要配置多个Diameter对端。同时重复该步骤将多个不同对端实体加到同一个域路由中。 当同一路由下有多个对端，可以采用不同的方式选择Diameter对端，如轮选、主从、优先级权重、IMSI指定优选等。 如果需要按照优先级和权重方式选择对端进行负荷分担时，请参考配置激活基于权重/优先级的Diameter负荷分担。 |
| ADD IMSIHSS   | IMSI前缀（IMSIPRE）           | 46000                                  | 参见“水平网设LLD文档 ”。 | HSSRLM配置的是HSS的域名，而不是DRA的域名。 HSS通用域名格式定义：epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。 如果没有配置IMSI和HSS的映射关系，需要配置默认路由才能找到对端。默认路由的配置方法请参考“增加Diameter域路由配置（ADD DMRT）”。                   |
| ADD IMSIHSS   | HSS域名（HSSRLM）             | epc.mnc015.mcc123.3gppnetwork.org      | 参见“水平网设LLD文档 ”。 | HSSRLM配置的是HSS的域名，而不是DRA的域名。 HSS通用域名格式定义：epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。 如果没有配置IMSI和HSS的映射关系，需要配置默认路由才能找到对端。默认路由的配置方法请参考“增加Diameter域路由配置（ADD DMRT）”。                   |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.1", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_SIG";
   ```
3. 配置S6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
    ADD SCTPPARA:SCTPPARAINDEX=0,SCTPPARANAME="For_S6a";
   ```
4. **可选：**增加Diameter本端信息。

   ```
   ADD DMLE:LOINDEX=0,LOHSTNAME="mme1.epc.mnc015.mcc123.3gppnetwork.org",LORLMNAME="epc.mnc015.mcc123.3gppnetwork.org",PDTNAME="MME";
   ```
5. 增加Diameter对端信息。

   ```
   ADD DMPE:PEERIDX=0,PEERHTNAM="dra1.epc.mnc015.mcc123.3gppnetwork.org";
   ```
6. 配置Diameter链路集信息。

   ```
   ADD DMLKS:LINKSIDX=0,LOCALIDX=0,PEERIDX=0,LINKSNAM="LNKS1_DRA1";
   ```
7. 配置Diameter链路信息。同一个链路集中可以存在两条链路，即同时建立多条SCTP偶联，每条链路对应的SCTP参数可根据具体需求配置。 其中，LOCALIP为MME逻辑（业务）IP，PEERIP为DRA的IP，端口默认3868，需要和DRA协商一致。

   ```
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="192.168.140.1", LOCALIPV4_2="192.168.140.17", LOCALPORT=3868, PEERIPV4_1="10.80.47.4", PEERIPV4_2="10.80.47.5", PEERPORT=3868,CLIORSER=DIAM_CONN_CLIENT,LINKSIDX=0,SCTPINDX=0,LINKNAM="DMLNK1_DRA1",CROSSIPFLAG=NO;
   ```
8. 配置Diameter路由。
   1. 配置Diameter域路由。

      ```
      ADD DMRT:ROUTEIDX=0,RSELMODE=SELMODE_MASTER_SLAVE,REALMNAME="epc.mnc015.mcc123.3gppnetwork.org",PEERIDX=0,ROUTENAM="rt to dra";
      ```
   2. **可选：**配置Diameter路由组。

      ****ADD DMRTGRP****

      **说明** 

      1. 当域路由的选路模式为IMSI指定优选，即RSELMODE=SELMODE\_IMSI\_PRIORITY时，路由索引和对端实体索引必须配置。
      2. 建议全部与DRA连接的时“路由优选模式”选择域路由优先，与HSS直连时“路由优选模式”选择主机路由优先。

         如果与DRA连接时“路由优选模式”选择主机路由优先，需要DRA支持通过IMSI寻址HSS。
   3. **可选：**MME会自主学习HSS的主机名，后续通过自主学习的HSS的主机名寻找路由。当MME与HSS之间只有通过DRA连接的主机路由且没有可用的域路由时，需要将软参DWORD\_EX34 BIT3设置为“1”，对于Purge UE Request消息优先使用配置的HSS主机名。

      ```
      SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=34, VALUE=VALUE_1, POSITION=3;
      ```

      **说明** 

      当MME与HSS之间只有通过DRA连接的主机路由且没有可用的域路由时，如果软参DWORD\_EX34 BIT3设置为“0”，Purge UE Request消息会发送失败。
9. **可选：**配置IMSI与HSS的映射关系，用户可以根据该映射关系查找IMSI归属的HSS信息。

   ```
   ADD IMSIHSS:IMSIPRE="46000",HSSRLM="epc.mnc015.mcc123.3gppnetwork.org";
   ```

## 验证方法

1. 查询当前配置的本地实体信息。

   进入“MML命令行-UNC”窗口。

   ****LST DMLE****: LOINDEX="本地实体索引";

   ****DSP DMLE****: LOINDEX="本地实体索引";

   - **预期结果：**显示已经配置本地实体的配置信息、状态信息。

     ```
     %%LST DMLE: LOINDEX=3;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------   
       本地实体索引  =  3 
     本地实体主机名  =  mme2-huawei.com.cn   
       本地实体域名  =  huawei.com.cn         
             产品名  =  unc     
         本地实体名  =  mme2-huawei.com.cn 
     (结果个数 = 1)
      ---    END
     ```

     ```
     %%DSP DMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本地实体索引  =  0   
       本地实体名  =  mme0     
         实体状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
2. 验证UNC能够正确查询对端实体状态。

   进入“MML命令行-UNC”窗口。

   ****LST DMPE****: PEERIDX="对端实体索引";

   ****DSP DMPE****: PEERIDX="对端实体索引";

   - **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST DMPE:;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     对端实体索引    对端主机名              对端实体名    节点支持的应用         对端拥塞避免开关  
     0               hss0.huawei.com.cn      hss0          S6a/S6d & S13 & SLg    关闭             
     1               hss1.huawei.com.cn      hss1          S6a/S6d & S13 & SLg    关闭             
     (结果个数 = 2) 
     ---    END
     ```

     ```
     %%DSP DMPE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     对端实体索引    对端实体名    实体状态  
     0               hss0          正常     
     1               hss1          正常     
     (结果个数 = 2) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证UNC能够正确查询Diameter链路集状态。

   进入“MML命令行-UNC”窗口。

   ****LST DMLKS****: LINKSIDX="Diameter链路集索引";

   ****DSP DMLKS****: LINKSIDX="Diameter链路集索引";

   - **预期结果：**显示已经配置Diameter链路集的配置信息、状态信息。

     ```
     %%LST DMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     Diameter链路集索引  =  0       
           本地实体索引  =  0       
           对端实体索引  =  0           
               选路模式  =  轮选         
             链路集名称  =  Robin0 
     (结果个数 = 1)
      ---    END
     ```

     ```
     %%DSP DMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下
     ------------ 
     Diameter链路集索引  =  0         
             链路集名称  =  Robin0         
             链路集状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
4. 验证UNC能够正确查询Diameter链路状态。

   进入“MML命令行-UNC”窗口。

   ****LST DMLNK****: LINKIDX="链路索引";

   ****DSP DMLNK****: LINKIDX="链路索引";

   - **预期结果：**显示已经配置Diameter链路的配置信息、状态信息。

     ```
     %%LST DMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------            
                vpn名称  =  VPN_SIG           
               链路索引  =  1        
             IP地址类型  =  TPTADDR_TYPE_IPV4                   
              本地地址1  =  192.168.140.1          
              本地地址2  =  192.168.140.17         
             本地端口号  =  3868          
              对端地址1  =  10.80.47.4          
              对端地址2  =  10.80.47.5         
             对端端口号  =  3868            
                C/S模式  =  服务器端 
     Diameter链路集索引  =  0   
       SCTP协议参数索引  =  0           
               链路名称  =  DMLNK1_DRA1   
       交叉路径是否可用  =  否 
     (结果个数 = 1)
      ---    END
     ```

     ```
     %%DSP DMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     链路索引  =  0 
     链路名称  =  dmlnk0   
       RU名称  =  USN_SP_RU_0064   
       进程号  =  4 
     链路状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
5. 验证UNC能够正确查询Diameter路由状态。

   进入“MML命令行-UNC”窗口。

   ****LST DMRT****: ROUTEIDX="路由索引";

   ****DSP DMRT****: ROUTEIDX="路由索引";

   - **预期结果：**显示所有已经配置Diameter路由的配置信息、状态信息。

     ```
     %%LST DMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------     
         路由索引  =  0     
         应用名称  =  S6a/S6d 
     是否默认路由  =  否     
         选路模式  =  轮选 
     目的实体域名  =  hss0 
     对端实体索引  =  1     
         路由名称  =  dmrt2hss1       
           优先级  =  NULL         
             权重  =  NULL         
             描述  =  noname 
     (结果个数 = 1)
      ---    END
     ```

     ```
     %%DSP DMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。 

     输出结果如下 
     ------------ 
     路由索引  =  0 
     路由名称  =  dmrt2hss1 
     路由状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   - **异常结果：**异常处理过程参见**ALM-80592 Diameter路由不可用**。