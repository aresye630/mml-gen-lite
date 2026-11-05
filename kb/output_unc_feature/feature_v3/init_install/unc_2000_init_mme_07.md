# 配置到EIR的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到EIR的路由数据后，可通过配置S13接口数据建立MME到EIR的逻辑连接。

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
| ****ADD SCTPPARA**** | SCTP协议参数索引（SCTPPARAINDEX） | 6 |  | S13接口的SCTP协议参数与S1–MME接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过**LST SCTPPARA**来查询已存在的SCTP协议参数记录 |
|  | 心跳间隔（ms）（HBINTERVAL） | 5000 |  |  |
|  | 偶联最大重发次数（MAXASSOCRETR） | 10 |  |  |
|  | 路径最大重发次数（MAXPATHRETR） | 5 |  |  |
|  | SCTP协议参数名（SCTPPARANAME） | S13 |  |  |
| ****ADD DMPE**** | 对端实体索引（PEERIDX） | 1 |  | 配置Diameter对端信息。 |
|  | 对端主机名（PEERHTNAM） | EIR.epc.mnc015.mcc123.3gppnetwork.org |  |  |
|  | 对端实体名（PEERNAM） | EIR |  |  |
| ****ADD DMLKS**** | Diameter链路集索引（LINKSIDX） | 1 |  | 配置Diameter链路集。 |
|  | 本地实体索引（LOCALIDX） | 0 |  |  |
|  | 对端实体索引（PEERIDX） | 1 |  |  |
|  | 选路模式（LSSELMODE） | SELMODE\_LOAD\_BALAN |  |  |
|  | 链路集名称（LINKSNAM） | EIR |  | 配置Diameter链路。 |
| ****ADD DMLNK**** | vpn名称（VPNNAME） | VPN\_SIG |  |  |
|  | 链路索引（LINKIDX） | 0 |  |  |
|  | IP地址类型（IPTYPE） | TPTADDR\_TYPE\_IPV4 |  |  |
|  | 本端IP地址1（LOCALIPV4\_1） | 10.10.1.1  10.10.1.2 |  |  |
|  | 本端IP地址2（LOCALIPV4\_2） | 10.10.1.17  10.10.1.18 |  |  |
|  | 本端端口（LOCALPORT） | 50470  50471 |  |  |
|  | 对端IP地址1（PEERIPV4\_1） | 10.11.1.3 |  |  |
|  | 对端IP地址2（PEERIPV4\_2） | 10.11.2.3 |  |  |
|  | 对端端口（PEERPORT） | 50470  50471 |  |  |
|  | Diameter链路集索引（LINKSIDX） | 1 |  |  |
|  | SCTP协议参数索引（SCTPINDX） | 4 |  |  |
|  | 链路名称（LINKNAM） | To-HSS1 |  |  |
| ****ADD DMRT**** | 路由索引（ROUTEIDX） | 1 |  | 配置Diameter路由。 |
|  | 应用名称（APPNAM） | S13 |  |  |
|  | 选路模式（RSELMODE） | SELMODE\_ROUND\_ROBIN |  |  |
|  | 目的实体域名（REALMNAME） | epc.mnc015.mcc123.3gppnetwork.org |  |  |
|  | 对端实体索引（PEERIDX） | 1 |  |  |
|  | 路由名称（ROUTENAM） | EIR |  |  |
| ****ADD EIR**** | EIR域名（EIRRLM） | epc.mnc015.mcc123.3gppnetwork.org |  | 配置EIR。 |
|  | EIR主机名（EIRHTN） | EIR.epc.mnc015.mcc123.3gppnetwork.org |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S13接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.1", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.2", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.17", VPNINSTNAME="VPN_SIG"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.18", VPNINSTNAME="VPN_SIG";
   ```
3. 配置S13接口基于IP的宽带信令SCTP偶联配置的协议参数。

   ```
   ADD SCTPPARA:SCTPPARAINDEX=6,HBINTERVAL=5000,MAXASSOCRETR=10,MAXPATHRETR=5,SCTPPARANAME="S13";
   ```
4. **可选：**查看Diameter配置中“重连定时器（RECONNTIMER）”是否符合要求。如果“重连定时器（RECONNTIMER）”参数不为6s，则设置为6s。

   在Diameter链路建立后，如果发生链路迁移或者重建，UNC可以主动发送INIT消息给对端设备请求建链，可以使得链路不中断。但是如果对端设备不支持在UP状态时处理INIT消息，可能会导致链路中断，重建时间变长，具体时长取决于配置的“重连定时器（RECONNTIMER）”参数。

   该定时器系统默认为30s，在目前灰度升级、扩容缩容等发生链路迁移场景下，造成链路中断时间过长，因此根据对端设备处理方式，建议将该参数配置为6s。

   ```
   LST DMFUNC:;
   SET DMFUNC:RECONNTIMER=6;
   ```
5. **可选：**配置Diameter本地信息。

   ****ADD DMLE****

   如果已经存在本地实体索引（LOINDEX）为0的DMLE，请使用现有DMLE，无需添加，跳过此步。

   如果需要使用其他本地实体索引，请参考DWORD\_EX18 BIT1–6的配置说明。DWORD\_EX18 BIT6 控制UNC在发送S13接口消息时是否根据“DWORD\_EX18” BIT1-BIT5设置的“本地实体索引”携带对应的本地域名和本地主机名，DWORD\_EX18 BIT1-BIT5 控制UNC根据指定的ADD DMLE记录携带本地域名和本地主机名。
6. 增加Diameter对端信息。

   ```
   ADD DMPE: PEERIDX=1, PEERHTNAM="EIR.epc.mnc015.mcc123.3gppnetwork.org", PEERNAM="EIR";
   ```
7. 配置Diameter链路集信息。

   ```
   ADD DMLKS: LINKSIDX=1, LOCALIDX=0, PEERIDX=1, LSSELMODE=SELMODE_LOAD_BALAN, LINKSNAM="EIR";
   ```
8. 配置Diameter路由信息。

   ```
   ADD DMRT: ROUTEIDX=1, APPNAM=S13, RSELMODE=SELMODE_ROUND_ROBIN, REALMNAME="epc.mnc015.mcc123.3gppnetwork.org", PEERIDX=1, ROUTENAM="EIR";
   ```
9. 配置Diameter链路信息。

   ```
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=0,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.1",LOCALIPV4_2="10.10.1.17",LOCALPORT=50470,PEERIPV4_1="10.11.1.3",PEERIPV4_2="10.11.2.3",PEERPORT=50470,LINKSIDX=1,SCTPINDX=4,LINKNAM="To-HSS1"; 
   ADD DMLNK:VPNNAME="VPN_SIG",LINKIDX=1,IPTYPE=TPTADDR_TYPE_IPV4,LOCALIPV4_1="10.10.1.2",LOCALIPV4_2="10.10.1.18",LOCALPORT=50471,PEERIPV4_1="10.11.1.3",PEERIPV4_2="10.11.2.3",PEERPORT=50471,LINKSIDX=1,SCTPINDX=4,LINKNAM="To-HSS1";
   ```
10. 配置EIR。

    ```
    ADD EIR: EIRRLM="epc.mnc015.mcc123.3gppnetwork.org", EIRHTN="EIR.epc.mnc015.mcc123.3gppnetwork.org";
    ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 查询当前配置的本地实体信息。

   ****LST DMLE****: LOINDEX=本地实体索引;

   ****DSP DMLE****: LOINDEX=本地实体索引;

   * **预期结果：**显示所有已经配置本地实体的配置信息、状态信息。

     ```
     %%LST DMLE: LOINDEX=0;%% 
     RETCODE = 0  操作成功。  

     操作结果如下 
     ------------   
       本地实体索引  =  0 
     本地实体主机名  =  mme0.huawei.com.cn   
       本地实体域名  =  huawei.com.cn        
             产品名  =  MME     
         本地实体名  =  mme0 
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
   * **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
3. 验证UNC能够正确查询对端实体状态。

   ****LST DMPE****: PEERIDX=对端实体索引;

   ****DSP DMPE****: PEERIDX=对端实体索引;

   * **预期结果：**显示所有已经配置对端实体的配置信息、状态信息。

     ```
     %%LST DMPE:;%% 
     RETCODE = 0  操作成功。  

     操作结果如下
     ------------ 
     对端实体索引    对端主机名              对端实体名    节点支持的应用         对端拥塞避免开关  
     0               hss0.huawei.com.cn      hss0          S6a/S6d & S13 & SLg    关闭             
     1               hss1.huawei.com.cn      hss1          S6a/S6d & S13 & SLg    关闭             
     2               hss2.huawei.com.cn      hss2          S6a/S6d & S13 & SLg    关闭             
     3               hss3.huawei.com.cn      hss3          S6a/S6d & S13 & SLg    关闭             
     (结果个数 = 4)
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
     2               hss2          正常     
     (结果个数 = 3) 
     ---    END
     ```
   * **异常结果：**异常处理过程参见**ALM-80593 Diameter对等端不可达**。
4. 验证UNC能够正确查询Diameter链路集状态。

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
   * **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
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
   * **异常结果：**异常处理过程参见**ALM-80592 Diameter路由不可用**。
6. 验证UNC能够正确查询Diameter链路状态。

   ****LST DMLNK****: LINKIDX="链路索引";

   ****DSP DMLNK****: LINKIDX="链路索引";

   * **预期结果：**显示所有已经配置Diameter链路的配置信息、状态信息。

     ```
     %%LST DMLNK: LINKIDX=0;%% 
     RETCODE = 0  操作成功。  

     输出结果如下 
     ------------            
                vpn名称  =  123           
               链路索引  =  0         
             IP地址类型  =  IPv4           
               协议类型  =  SCTP          
              本地地址1  =  10.1.1.1          
              本地地址2  =  255.255.255.255         
             本地端口号  =  3868          
              对端地址1  =  10.1.1.1          
              对端地址2  =  255.255.255.255         
             对端端口号  =  3868           
                C/S模式  =  服务器端 
     Diameter链路集索引  =  0   
       SCTP协议参数索引  =  1           
               链路名称  =  dmlnk0   
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
   * **异常结果：**异常处理过程参见**ALM-80591 Diameter链路故障**。
7. 业务测试。

   进行业务测试前，需要首先完成UNC与eNodeB、UDG、EIR的链路配置。UNC的安全开关打开，且****MOD S1IMEICFG****中“ CHKIMEIPLC”设为“IMEI(检查IMEI)”。

   使用手机浏览网页。

   1. 创建用户跟踪任务。

      参数选择如下：

      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其他参数：选择默认值。
   2. 创建S13接口跟踪

      链路号：MME与EIR配置的Diameter链路号。

      其他参数：选择默认值。
   3. 用户开机附着。
   4. 查看S13接口跟踪结果。
      * **预期结果：**

        可以在Message Direction处看到MME和EIR之间有消息交互。

        跟踪到ME Identity Check Request与ME Identity Check Answer消息，且result-code信元为diameter-success。
      * **异常结果：**

        观察不到MME与EIR之间的消息或观察到的消息result-code信元不为diameter-success。
   5. 查看用户跟踪结果。

      * **预期结果：**

        用户附着成功，可以在Message Direction处看到MME和EIR之间、UDM模块与DIAM模块之间有消息交互。

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**

        观察不到MME与EIR之间、UDM模块与DIAM模块之间的消息。或观察到MME与EIR之间的消息result code信元不为diameter\_success。
   6. 查询用户MM上下文。

      **DSP COMMMCTX**: QUERYOPT=BYIMSI, IMSI=IMSI;

      * **预期结果：**

        可以查询到用户的MM上下文，并接状态为EMM-IDLE或是EMM-CONNECT状态。
      * **异常结果：**

        查询不到用户的MM上下文。

版权所有 © 华为技术有限公司
