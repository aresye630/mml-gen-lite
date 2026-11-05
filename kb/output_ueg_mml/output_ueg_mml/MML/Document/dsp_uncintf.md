# 显示UNC接口名称（DSP UNCINTF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGSN、MME、SGW-C、AMF、PGW-C、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于显示已经上报至网管北向的UNC网元所有业务或者管理接口的名称。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRMVNFTYPE | 北向网元类型 | 可选必选说明：可选参数  参数含义：该参数用于指定UNC网元的北向网元类型。  数据来源：本端规划 取值范围： AMF（AMF）MME（MME）SGSN（SGSN）SMF（SMF）PGWC（PGWC）SGWC（SGWC）GGSNC（GGSNC）ProxySGWC（ProxySGWC）NRF（NRF）NSSF（NSSF）SMSF（SMSF）CHF（CHF）ProxySMF（ProxySMF）  默认值：无  配置原则：无 |

## 使用实例

- 显示已经上报至网管北向的北向网元类型为SMF的接口名称，执行以下命令：

  ```
  %%DSP UNCINTF: NRMVNFTYPE=SMF;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  北向网元类型  接口类型  

  SMF           Mgt       
  SMF           N10       
  SMF           N11       
  SMF           N16a      
  SMF           N4        
  SMF           N40       
  SMF           N7        
  SMF           Nbsf      
  SMF           Nnrf      
  SMF           Radius    
  (结果个数 = 10)

  ---    END
  ```
- 显示全量已经上报至网管北向的UNC网元所有业务或者管理接口的名称，执行以下命令：

  ```
  %%DSP UNCINTF:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  北向网元类型  接口类型  

  AMF           DnsQry    
  AMF           Mgt       
  AMF           N11       
  AMF           N12       
  AMF           N14       
  AMF           N15       
  AMF           N2        
  AMF           N22       
  AMF           N26-AMF   
  AMF           N8        
  AMF           NLg       
  AMF           NLs       
  AMF           Nnrf      
  MME           DnsQry    
  MME           Mgt       
  MME           N26-MME   
  MME           S1-MME    
  MME           S10       
  MME           S11-c     
  MME           S11-u     
  MME           S6a       
  MME           SGs       
  MME           SLg       
  MME           SLs       
  MME           Sv        
  SMF           Mgt       
  SMF           N10       
  SMF           N11       
  SMF           N16a      
  SMF           N4        
  SMF           N40       
  SMF           N7        
  SMF           Nbsf      
  SMF           Nnrf      
  SMF           Radius    
  PGWC          Ga        
  PGWC          Gx        
  PGWC          Gy        
  PGWC          Mgt       
  PGWC          Radius    
  PGWC          S5_P      
  PGWC          S8_P      
  PGWC          Sx        
  SGWC          Ga        
  SGWC          Mgt       
  SGWC          S11       
  SGWC          S5_S      
  SGWC          S8_S      
  SGWC          Sx        
  ProxySGWC     DnsQry    
  ProxySGWC     Mgt       
  ProxySGWC     S5_P      
  ProxySGWC     S8_S      
  ProxySGWC     Sx        
  NRF           Mgt       
  NRF           Nnrf      
  NSSF          Mgt       
  NSSF          Nnssf     
  CHF           Bx        
  CHF           Ga        
  CHF           Mgt       
  CHF           N40       
  CHF           Nnrf     
  SMSF          Mgt
  SMSF          N20
  SMSF          N21
  ProxySMF     Mgt
  ProxySMF     N4
  ProxySMF     N16a
  ProxySMF     N16
  ProxySMF     Nnrf
  (结果个数 = 71)

  ---    END
  ```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                   |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 北向网元类型  | 该参数用于指定UNC网元的北向网元类型。 取值说明： AMF（AMF）MME（MME）SGSN（SGSN）SMF（SMF）PGWC（PGWC）SGWC（SGWC）GGSNC（GGSNC）ProxySGWC（ProxySGWC）NRF（NRF）NSSF（NSSF）SMSF（SMSF）CHF（CHF）ProxySMF（ProxySMF） |
| 接口类型    | 该参数用于指定UNC网元的接口名称。其中，Mgt为网元和网管的对接接口；DnsQry为SGSN、MME、AMF网元的DNS本端实体与DNS服务器进行通信的接口；Bx为NCG网元与计费账务域交互的文件接口；其他为协议定义的接口。                                                       |