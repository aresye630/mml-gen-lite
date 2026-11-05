# 配置到DNS相关数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到DNS的路由数据后，可通过配置S10接口数据建立MME到DNS的逻辑连接，用于MME在以下流程中进行域名解析：

- 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。
- 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。

**说明** 

进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：

- DNS服务器是网络中专门提供域名解析服务的服务器。
- DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。
- 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。

MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及命名规范，具体内容请参见逻辑接口介绍。
- MME上的S10接口路由配置已经完成。

  **说明** 

  MME侧通过S10接口路由与DNS互通，因此只需确保MME上的S10接口路由配置完成，那么MME到DNS的路由配置也就完成了。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                      | 取值样例                      | 获取方法            | 说明                                                                                  |
|:--------------|:--------------------------|:--------------------------|:----------------|:------------------------------------------------------------------------------------|
| ADD SERVICEIP | IP版本（IPVERSION）           | IPv4                      | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                           |
| ADD SERVICEIP | 业务IPv4地址（SERVICEIPV4）     | 192.168.140.17 10.10.1.3  | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                           |
| ADD SERVICEIP | VPN实例名称（VPNINSTNAME）      | VPN_CN                    | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。                                                                           |
| ADD DNSLE     | IP地址类型（IPT）               | IPV4                      | 参见“水平网设LLD文档 ”。 | 配置DNS本端实体。 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。       |
| ADD DNSLE     | IPv4地址（IPV4）              | 192.168.140.17 10.10.1.3  | 参见“水平网设LLD文档 ”。 | 配置DNS本端实体。 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。       |
| ADD DNSLE     | 本地端口号（LOCPORT）            | 15001                     | 参见“水平网设LLD文档 ”。 | 配置DNS本端实体。 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。       |
| ADD DNSLE     | VPN名称 （VPNNAME）           | VPN_CN                    | 参见“水平网设LLD文档 ”。 | 配置DNS本端实体。 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。       |
| ADD DNSLE     | DNS本端实体名称（LENAME）         | Dnsle                     | 参见“水平网设LLD文档 ”。 | 配置DNS本端实体。 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。       |
| ADD DNSS      | IP地址（IP）                  | 10.176.153.1 10.176.152.1 | 参见“水平网设LLD文档 ”。 | 配置DNS服务器。 每个通用DNS服务器都具有不同的优先级。专用DNS服务器只用于PDN承载激活过程中的域名解析，并且只供特定APN OI或者特定PLMN的用户使用。 |
| ADD DNSS      | 域名服务器优先级（PRI）             | PRI1 PRI2                 | 参见“水平网设LLD文档 ”。 | 配置DNS服务器。 每个通用DNS服务器都具有不同的优先级。专用DNS服务器只用于PDN承载激活过程中的域名解析，并且只供特定APN OI或者特定PLMN的用户使用。 |
| SET DNS       | DNS探测开关（DDS）              | ON                        | 参见“水平网设LLD文档 ”。 | 配置DNS运行参数，包括一些定时器、计数器等参数。 系统为DNS运行参数提供了缺省值，一般不需要用户修改。                               |
| SET DNS       | DNS探测间隔（s）（DDI）           | 10                        | 参见“水平网设LLD文档 ”。 | 配置DNS运行参数，包括一些定时器、计数器等参数。 系统为DNS运行参数提供了缺省值，一般不需要用户修改。                               |
| SET DNS       | 故障判定阈值（SFT）               | 5                         | 参见“水平网设LLD文档 ”。 | 配置DNS运行参数，包括一些定时器、计数器等参数。 系统为DNS运行参数提供了缺省值，一般不需要用户修改。                               |
| SET DNS       | 持续失败最大时长（s）（FAILTM）       | 0                         | 参见“水平网设LLD文档 ”。 | 配置DNS运行参数，包括一些定时器、计数器等参数。 系统为DNS运行参数提供了缺省值，一般不需要用户修改。                               |
| SET DNS       | 二级Cache提前刷新时间（s）（RCUPDTM） | 0                         | 参见“水平网设LLD文档 ”。 | 配置DNS运行参数，包括一些定时器、计数器等参数。 系统为DNS运行参数提供了缺省值，一般不需要用户修改。                               |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.140.17", VPNINSTNAME="VPN_CN"; 
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.1.3", VPNINSTNAME="VPN_CN";
   ```
3. 配置DNS数据。
   1. 配置DNS客户端。

      ```
      ADD DNSLE:IPT=IPV4,IPV4="192.168.140.17",LOCPORT=15001,VPNNAME="VPN_CN",LENAME="Dnsle"; 
      ADD DNSLE:IPT=IPV4,IPV4="10.10.1.3",LOCPORT=15001,VPNNAME="VPN_CN",LENAME="Dnsle";
      ```
   2. 配置DNS服务器。

      ```
      ADD DNSS: IP="10.176.152.1", PRI=PRI1; 
      ADD DNSS: IP="10.176.153.1", PRI=PRI2;
      ```
   3. 配置DNS运行参数。

      ```
      SET DNS: DDS=ON, DDI=10, SFT=5, FAILTM=0, RCUPDTM=0;
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查USN\_VNFC到DNS的链路是否正常。

   **说明** 

   如果USN\_VNFC是通过DNS服务器进行域名解析的时候需要执行此步骤，如果使用本地主机信息表（Hostfile）进行域名配置时则不需要执行此步检测。

   ****SET DNS****:DDS=DNS探测开关;

   **说明** 

   参数“DDS”选择“ON(开)”。将使用Default detect domain name参数的配置进行路径探测，只要收到对端响应消息，即认为链路正常。

   - **预期结果：**在**DNS**跟踪中，“消息类型”勾选“维护探测消息”后，可以看到DNS和USN\_VNFC之间有DNS Detect Request和DNS Detect Ack消息交互。
   - **异常结果：**对端DNS异常。

     异常处理过程参见**ALM-80619 DNS链路故障**。
3. 检查指定域名能否被解析。

   ****TST DNS****:QRYTYPE=查询类型, FQDN="域名", RSVTP=解析类型;

   **说明** 

   - 参数“QRYTYPE”可以选择“A(A类型查询)”或者“NAPTR(NAPTR类型查询)”。通常情况下Pre R8的协议采用“A(A类型查询)”，R8以后的协议采用“NAPTR(NAPTR类型查询)”。
   - 参数“RSVTP”选择“HOSTFILE(主机文件)”，“L1CACHE(一级Cache)”，“L2CACHE(二级Cache)”，“SERVER(服务器)”，“ALL(所有)”。

   - **预期结果：**为保证进行GUL融合基本业务，指定域名能够被解析。Test报文中能返回探测域名的IP地址。
     - **探测到S-GW的DNS数据，该域名用于Attach/TAU/Handover流程中，根据TAI选择S-GW。**

       ```
       %%TST DNS: QRYTYPE=NAPTR,FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG",RSVTP=HOSTFILE,RUNAME="USN_SP_RU_0064";%% 
       RETCODE = 0  操作成功  

       操作结果如下: 
       ------------------------            
                 域名  =  TAC-LB01.TAC-HB11.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG        
             解析类型  =  hostfile      
           主机名数目  =  1          
               主机名  =  TOPON.SGW.SGW1.NODES.EPC.ENVID11.MNC03.MCC123.3GPPNETWORK.ORG          
               IP数目  =  1       
             网元类型  =  SGW       
             接口类型  =  S11 
       S5接口协议类型  =  GTP_PMIP 
       S8接口协议类型  =  GTP_PMIP            
                    ......      
            主机地址1  =  10.11.12.11           
                    ......          
                  TTL  =  4294967295 
       (结果个数 = 1) 
       ---    END
       ```
     - **探测到P-GW的DNS数据，该域名用于Attach/PDN连接建立流程中，根据APN选择P-GW。**

       ```
       %%TST DNS:QRYTYPE=NAPTR,FQDN="HUAWEI1.COM.APN.EPC.MNC003.MCC123.3GPPNETWORK.ORG",RSVTP=HOSTFILE,RUNAME="USN_SP_RU_0064";%% 
       RETCODE = 0  操作成功  

       操作结果如下:
       ------------------------            
                 域名  =  HUAWEI1.COM.APN.EPC.MNC003.MCC123.3GPPNETWORK.ORG        
             解析类型  =  hostfile      
           主机名数目  =  1          
               主机名  =  TOPON.PGW.GW1.NODES.EPC.MNC03.MCC123.3GPPNETWORK.ORG          
               IP数目  =  1        
             网元类型  =  PGW        
             接口类型  =  S5  
       S5接口协议类型  =  GTP_PMIP  
       S8接口协议类型  =  GTP
                   ......       
            主机地址1  =  10.10.10.10
                   ......            
                  TTL  =  4294967295 
       (结果个数 = 1) 
       ---    END
       ```
     - **探测到GGSN的DNS数据，该域名用于PDP激活流程中，根据APN选择GGSN。**

       ```
       %%TST DNS: QRYTYPE=A,FQDN="HUAWEI11.MNC003.MCC123.GPRS",RSVTP=SERVER;%% 
       RETCODE = 0  操作成功  

       操作结果如下: 
       ------------------------             
                 域名  =  HUAWEI11.MNC003.MCC123.GPRS         
             解析类型  =  server      
           主机名数目  =  0          
               主机名  =  NULL          
               IP数目  =  1        
             网元类型  =  NULL        
             接口类型  =  NULL  
       S5接口协议类型  =  NULL  
       S8接口协议类型  =  NULL
                   ......       
            主机地址1  =  10.11.11.14
                   ......            
                  TTL  =  85900 
       (结果个数 = 1)
        ---    END
       ```
     - **探测到MME的DNS数据，该域名用于Intra LTE的Handover流程中，根据TAI选择MME。**

       ```
       %%TST DNS: QRYTYPE=NAPTR,FQDN="TAC-LB04.TAC-HB12.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG",RSVTP=HOSTFILE,RUNAME="USN_SP_RU_0064";%% 
       RETCODE = 0  操作成功  

       操作结果如下: 
       ------------------------           
       域名  =  TAC-LB04.TAC-HB12.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG       
       解析类型  =  hostfile     
       主机名数目  =  1         
       主机名  =  TOPON.INTERMME.MME.NODES.EPC.ENVID11.MNC03.MCC123.3GPPNETWORK.ORG         
       IP数目  =  1       
       网元类型  =  MME       
       接口类型  =  S10 
       S5接口协议类型  =  NULL 
       S8接口协议类型  =  NULL
                   ......      
       主机地址1  =  10.2.12.1
                   ......            
       TTL  =  4294967295 
       (结果个数 = 1) 
       ---    END
       ```
     - **探测到MME的DNS数据，该域名用于Intra LTE的Attach/TAU流程中，根据GUMMEI选择MME。**

       ```
       %%TST DNS: QRYTYPE=NAPTR,FQDN="MMEC03.MMEGI8000.MME.EPC.MNC003.MCC123.3GPPNETWORK.ORG ",RSVTP=HOSTFILE,RUNAME="USN_SP_RU_0064";%% 
       RETCODE = 0  Operation succeeded  

       操作结果如下: 
       ------------------------             
                 域名  =  MMEC03.MMEGI8000.MME.EPC.MNC003.MCC123.3GPPNETWORK.ORG         
             解析类型  =  hostfile       
           主机名数目  =  1           
               主机名  =  TOPON.INTERMMESPIDER1.MME.NODES.EPC.ENVID11.MNC03.MCC123.3GPPNETWORK.ORG           
               IP数目  =  1         
             网元类型  =  MME         
             接口类型  =  S10   
       S5接口协议类型  =  NULL   
       S8接口协议类型  =  NULL
                    ......        
       主机地址1  =  10.11.12.15
                    ......              
       TTL  =  4294967295 
       (结果个数 = 1)
        ---    END
       ```
     - **探测到Gn/Gp SGSN的DNS数据，该域名用于RAU流程和Inter RAT的Attach/TAU/RAUNACC流程中，根据RAI/LAI选择Gn/Gp SGSN。**

       ```
       %%TST DNS: QRYTYPE=A,FQDN="RAC0001.LAC1201.MNC003.MCC123.GPRS",RSVTP=SERVER;%% 
       RETCODE = 0  Operation succeeded  

       操作结果如下: 
       ------------------------            
                 域名  =  RAC0001.LAC1201.MNC003.MCC123.GPRS        
             解析类型  =  server      
           主机名数目  =  0          
               主机名  =  NULL          
               IP数目  =  1        
             网元类型  =  NULL        
             接口类型  =  NULL  
       S5接口协议类型  =  NULL  
       S8接口协议类型  =  NULL
                    ......       
            主机地址1  =  10.2.12.1
                    ......            
                  TTL  =  85900 
       (结果个数 = 1)
        ---    END
       ```
     - **探测到Gn/Gp SGSN的DNS数据，该域名用于3G间的Reloction流程和Inter RAT的Handover流程中，根据RNC选择Gn/Gp SGSN。**

       ```
       %%TST DNS: QRYTYPE=A,FQDN="RNC0465.MNC003.MCC123.GPRS",RSVTP=SERVER;%% 
       RETCODE = 0  操作成功  

       操作结果如下:
       ------------------------            
                 域名  =  RNC0465.MNC003.MCC123.GPRS        
             解析类型  =  server      
           主机名数目  =  0          
               主机名  =  NULL          
               IP数目  =  1        
             网元类型  =  NULL        
             接口类型  =  NULL  
       S5接口协议类型  =  NULL  
       S8接口协议类型  =  NULL
                    ......       
            主机地址1  =  10.2.12.1
                   ......             
                  TTL  =  85900 
       (结果个数 = 1) 
       ---    END
       ```
     - **探测到Gn/Gp SGSN的DNS数据，该域名用于Inter RAU时流程中，DNS可解析出用户RAU后需要接入的SGSN的IP地址。**

       ```
       %%TST DNS: QRYTYPE=A,FQDN="RAC0001.LAC1201.MNC003.MCC123.GPRS",RSVTP=SERVER;%% 
       RETCODE = 0  Operation succeeded  

       The result is as follows 
       ------------------------            
                 域名  =  RAC0001.LAC1201.MNC003.MCC123.GPRS        
             解析类型  =  server      
           主机名数目  =  0           
               主机名  =  NULL           
               IP数目  =  1         
             网元类型  =  NULL         
             接口类型  =  NULL   
       S5接口协议类型  =  NULL   
       S8接口协议类型  =  NULL
                    ......        
            主机地址1  =  10.2.12.1
                    ......              
                 TTL  =  85900 
       (结果个数 = 1) 
       ---    END
       ```
   - **异常结果：**域名解析失败，异常处理过程参见GPRS/UMTS业务故障/LTE业务故障。