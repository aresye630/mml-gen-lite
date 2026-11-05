# 配置到SCEF的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增SCEF或MME时，在配置完成SCEF到MME的路由数据后，可通过配置T6a接口数据建立MME到SCEF的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.1.1  10.10.1.2  10.10.1.17  10.10.1.18 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_SIG |  |  |
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 0 |  | T6a接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过**LST SCTPPARA**来查询已存在的SCTP协议参数记录。 |
|  | SCTP协议参数名（SCTPPARANAME） | For\_T6a |  |  |
| ****ADD DMLE**** | 本地实体索引（LOINDEX） | 1 |  | 配置Diameter本地信息。  如果已经存在DMLE，请使用现有的DMLE，无需添加，跳过此步。  如果配置用于S13接口、SLg接口、T6a接口，本地实体索引（LOINDEX）需要配置为0。 |
|  | 本地实体主机名（LOHSTNAME） | mme1.epc.mnc000.mcc123.3gppnetwork.org |  |  |
|  | 本地实体域名（LORLMNAME） | epc.mnc000.mcc123.3gppnetwork.org |  |  |
|  | 本地实体名（LOINFONAME） | usn |  |  |
| ****ADD DMPE**** | 对端实体索引（PEERIDX） | 1 |  | 配置Diameter对端信息 |
|  | 对端主机名（PEERHTNAM） | scef1.epc.mnc015.mcc123.3gppnetwork.org |  |  |
|  | 对端实体名（PEERNAM） | SCEF1 |  |  |
|  | 节点支持的应用（APPCAP） | S6a/S6d-0&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-1 |  |  |
| ****ADD DMLKS**** | Diameter链路集索引（LINKSIDX） | 0 |  | 配置Diameter链路集 |
|  | 本地实体索引（LOCALIDX） | 0 |  |  |
|  | 对端实体索引（PEERIDX） | 1 |  |  |
|  | 选路模式（LSSELMODE） | SELMODE\_LOAD\_BALAN |  |  |
|  | 链路集名称（LINKSNAM） | LNKS1\_SCEF1 |  |  |
| ****ADD DMLNK**** | vpn名称（VPNNAME） | VPN\_SIG |  | 配置Diameter链路。 |
|  | 链路索引（LINKIDX） | 0 |  |  |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |
|  | 本端IP地址1（LOCALIPV4\_1） | 10.10.1.1  10.10.1.2 |  |  |
|  | 本端IP地址2（LOCALIPV4\_2） | 10.10.1.17  10.10.1.18 |  |  |
|  | 本端端口（LOCALPORT） | 5000 |  |  |
|  | 对端IP地址1（PEERIPV4\_1） | 10.11.1.3 |  |  |
|  | 对端IP地址2（PEERIPV4\_2） | 10.11.2.3 |  |  |
|  | 对端端口（PEERPORT） | 50480 |  |  |
|  | Diameter链路集索引（LINKSIDX） | 0 |  |  |
|  | SCTP协议参数索引（SCTPINDX） | 0 |  |  |
|  | 链路名称（LINKNAM） | To-SCEF1 |  |  |
| ****ADD DMRT**** | 路由索引（ROUTEIDX） | 0 |  | 配置Diameter路由。 |
|  | 应用名称（APPNAM） | T6A/T6AI/T6B/T6BI |  |  |
|  | 选路模式（RSELMODE） | SELMODE\_ROUND\_ROBIN |  |  |
|  | 目的实体域名（REALMNAME） | epc.mnc015.mcc123.3gppnetwork.org |  |  |
|  | 对端实体索引（PEERIDX） | 1 |  |  |
|  | 路由名称（ROUTENAM） | ROUTE1\_scef1 |  | 增加SCEF配置时，域名和主机名都需要添加。 |
| ****ADD SCEF**** | SCEF域名(SCEFRLM) | scef.mnc015.mcc123.3gppnetwork.org |  |  |
|  | SCEF主机名(SCEFHTN) | scef1.epc.mnc015.mcc123.3gppnetwork.org |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置T6a接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.17", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.18", VPNINSTNAME="VPN_SIG";
   ```
3. 配置T6a接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   ADD SCTPPARA: SCTPPARAINDEX=0, SCTPPARANAME="For_T6a";
   ```
4. **可选：**增加Diameter本端信息 。

   ```
   ADD DMLE: LOINDEX=1, LOHSTNAME="mme1.epc.mnc000.mcc123.3gppnetwork.org",LORLMNAME="epc.mnc000.mcc123.3gppnetwork.org",LOINFONAME="usn";
   ```
5. 增加Diameter对端信息。

   ```
   ADD DMPE: PEERIDX=1, PEERHTNAM="scef1.epc.mnc015.mcc123.3gppnetwork.org", PEERNAM="SCEF1", APPCAP=S6a/S6d-0&S13-0&SLg-0&T6a/T6ai/T6b/T6bi-1;
   ```
6. 配置Diameter链路集信息。

   ```
   ADD DMLKS: LINKSIDX=0, LOCALIDX=0, PEERIDX=1, LSSELMODE=SELMODE_LOAD_BALAN, LINKSNAM="LNKS1_SCEF1";
   ```
7. 配置Diameter链路信息，同一个链路集中可以存在两条链路，即同时建立多条SCTP偶联，每条链路对应的SCTP参数可根据具体需求配置。

   ```
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=0,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.1",LOCALIPV4_2="10.10.1.17",LOCALPORT=50480,PEERIPV4_1="10.11.1.3",PEERIPV4_2="10.11.2.3",PEERPORT=50480,LINKSIDX=0,SCTPINDX=0,LINKNAM="To-SCEF1"; 
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.2",LOCALIPV4_2="10.10.1.18",LOCALPORT=50480,PEERIPV4_1="10.11.1.3",PEERIPV4_2="10.11.2.3",PEERPORT=50480,LINKSIDX=0,SCTPINDX=0,LINKNAM="To-SCEF1";
   ```
8. **可选：**配置Diameter路由信息。

   ```
   ADD DMRT: ROUTEIDX=0, APPNAM=T6A/T6AI/T6B/T6BI, RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc.mnc015.mcc123.3gppnetwork.org", PEERIDX=1, ROUTENAM="ROUTE1_scef1";
   ```
9. 配置SCEF信息。

   ```
   ADD SCEF: SCEFRLM="epc.mnc015.mcc123.3gppnetwork.org", SCEFHTN="scef1.epc.mnc015.mcc123.3gppnetwork.org";
   ```

## 验证方法

1. 查询当前配置的本地实体信息。

   进入“MML命令行-UNC”窗口。

   ****LST DMLE****: LOINDEX=本地实体索引;

   ****DSP DMLE****: LOINDEX=本地实体索引;

   * **预期结果：**显示所有已经配置本地实体的配置信息、状态信息。

     ```
     %%LST DMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     --------------   
       本地实体索引  =  0 
     本地实体主机名  =  mme.epc.mnc015.mcc123.3gppnetwork.org   
       本地实体域名  =  epc.mnc015.mcc123.3gppnetwork.org         
             产品名  =  unc     
         本地实体名  =  unc 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP DMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------ 
     本地实体索引  =  0   
       本地实体名  =  unc     
         实体状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   * **异常结果：**无法显示所有已经配置本地实体的配置信息或状态信息。异常处理过程参见**ALM-80593 Diameter对等端不可达**。
2. 查询对端实体信息。

   ****LST DMPE****: PEERIDX=对端实体索引;

   ****DSP DMPE****: PEERIDX=对端实体索引;

   * **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST DMPE:;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     对端实体索引    对端主机名              对端实体名    节点支持的应用         对端拥塞避免开关  
     0               scef0.huawei.com.cn      scef0          T6a/T6ai/T6ab        关闭             
     1               scef1.huawei.com.cn      scef1          T6a/T6ai/T6ab        关闭            
     2               scef2.huawei.com.cn      scef2          T6a/T6ai/T6ab        关闭             
     3               scef3.huawei.com.cn      scef3          T6a/T6ai/T6ab        关闭             
     (结果个数 = 4) 
     ---    END
     ```

     ```
     %%DSP DMPE:;%% 
     RETCODE = 0  操作成功。  

     输出结果如下
     ------------ 
     对端实体索引    对端实体名    实体状态  
     0               scef0          正常     
     1               scef1          正常     
     2               scef2          正常     
     (结果个数 = 3) 
     ---    END
     ```
   * **异常结果：**无法显示所有已经配置对端实体的配置信息或状态信息。异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证UNC能够正确查询Diameter链路集状态。

   ****LST DMLKS****: LINKSIDX=Diameter链路集索引;

   ****DSP DMLKS****: LINKSIDX=Diameter链路集索引;

   * **预期结果：**显示所有已经配置Diameter链路集的配置信息、状态信息。

     ```
     %%LST DMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------ 
     Diameter链路集索引  =  0       
           本地实体索引  =  0       
           对端实体索引  =  0           
               选路模式  =  轮选        
             链路集名称  =  To-SCEF0 
     (结果个数 = 1) 
     ---    END
     ```

     ```
     %%DSP DMLKS: LINKSIDX=0;%% 
     RETCODE = 0  操作成功  

     输出结果如下： 
     -------------- 
     链路集索引  =  0 
     链路集名称  =  To-SCEF0 
     链路集状态  =  正常 
     (结果个数 = 1)
     ```
   * **异常结果：**无法显示所有已经配置Diameter链路集的配置信息或状态信息。异常处理过程参见**ALM-80591 Diameter链路故障**。
4. 验证UNC能够正确查询Diameter链路状态。

   ****LST DMLNK****: LINKIDX="链路索引";

   ****DSP DMLNK****: LINKIDX="链路索引";

   * **预期结果：**显示所有已经配置Diameter链路的配置信息、状态信息。

     ```
     %%LST DMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     --------------            
                vpn名称  =  UNC1           
               链路索引  =  0          
             IP地址类型  =  IPv4           
               协议类型  =  SCTP          
              本地地址1  =  192.168.15.10          
              本地地址2  =  255.255.255.255         
             本地端口号  =  3868          
              对端地址1  =  192.168.15.16           
              对端地址2  =  255.255.255.255         
             对端端口号  =  3868            
                C/S模式  =  服务器端 
     Diameter链路集索引  =  0   
       SCTP协议参数索引  =  0           
               链路名称  =  To-SCEF0   
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
   * **异常结果：**无法显示所有已经配置Diameter链路的配置信息或状态信息。异常处理过程参见**ALM-80591 Diameter链路故障**。
5. 验证UNC能够正确查询Diameter路由状态。

   ****LST DMRT****: ROUTEIDX=路由索引;

   ****DSP DMRT****: ROUTEIDX=路由索引;

   * **预期结果：**显示所有已经配置Diameter路由的配置信息、状态信息。

     ```
     %%LST DMRT: ROUTEIDX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------     
         路由索引  =  0     
         应用名称  =  T6a/T6ai/T6b 
     是否默认路由  =  否     
         选路模式  =  轮选 
     目的实体域名  =  scef1501.huawei03.com.cn 
     对端实体索引  =  1     
         路由名称  =  dmrt2scef1       
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
     -------------- 
     路由索引  =  0 
     路由名称  =  TO-SCEF0 
     路由状态  =  正常 
     (结果个数 = 1) 
     ---    END
     ```
   * **异常结果：**无法显示所有已经配置Diameter路由的配置信息或状态信息。异常处理过程参见**ALM-80592 Diameter路由不可用**。
6. 验证UNC能够正确查询SCEF的信息。

   ****LST SCEF****: SCEFRLM="scef.mnc015.mcc123.3gppnetwork.org";

   * **预期结果：**正确显示已经配置的SCEF信息。

     ```
     %%LST SCEF:;%%  
     RETCODE = 0  操作成功    

     操作结果如下：  
     --------------    
       SCEF域名  =  scef.mnc015.mcc123.3gppnetwork.org  
     SCEF主机名  =  scef1.epc.mnc015.mcc123.3gppnetwork.org  
     (结果个数 = 1)   
     ---    END
     ```
   * **异常结果**：观察不到已经配置的SCEF信息。
7. 进行业务测试。

   进行业务测试前，需要首先完成UNC与eNodeB、SCEF的链路配置。

   1. 创建用户跟踪任务。

      参数选择如下：
      * IMSI/MSISDN/用户索引号：被跟踪用户的IMSI、MSISDN或者用户索引号。
      * 其他参数：选择默认值。
   2. 创建Diameter接口跟踪。

      参数选择如下：

      链路号：Diameter Link的索引号。
   3. 用户开机，进行附着。
   4. 查看Diameter接口跟踪结果。

      **预期结果：**可以看到Reporting information request和Reporting information answer消息。

      * **异常结果**：观察不到Diameter接口跟踪消息或观察到的消息异常。

版权所有 © 华为技术有限公司
