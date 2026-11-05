# 显示SIP注册上下文（DSP SIPCTX）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME****、AMF**

该命令用于查询用户IMS域的SIP注册信息。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                       |
|:---------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYOPT | 查询方式   | 可选必选说明：可选参数 参数说明：该参数用于指定查询IMS域的SIP上下文的查询方式 取值范围： “ALLNUM(查询总数)”：表示查询IMS域的SIP上下文总数。 “BYIMSI(指定IMSI)”：表示根据IMSI查询用户的上下文。 默认值：“BYIMSI(指定IMSI)” |
| IMSI     | IMSI   | 可选必选说明：条件必选参数 参数说明：该参数用于指定国际移动用户标识。 前提条件：此参数在“查询方式”设置为“BYIMSI(指定IMSI)”后生效。 取值范围：1～15位数字 默认值：无                                              |

#### 使用实例

- 当查询方式为ALLNUM时，直接显示IMS域的SIP注册上下文总数:

  DSP SIPCTX: QUERYOPT=ALLNUM;

  ```
  %%DSP SIPCTX: QUERYOPT=ALLNUM;%% 
  RETCODE = 0  操作成功  
  输出结果如下 
  ------------------------ 
  Result  =   
  RU Name        =  LINK_SP_RU_0064 
  Process No.    =  1 
  User Num       =  1  

  RU Name        =  LINK_SP_RU_0064 
  Process No.    =  0 
  User Num       =  0  

  All User Num   =  1 
  (结果个数 = 1)  
  ---    END
  ```

- 当查询方式为BYIMSI时，按照IMSI查询，显示IMS域的SIP注册上下文信息。

  DSP SIPCTX: QUERYOPT=BYIMSI, IMSI="123456789012345";

  ```
  %%DSP SIPCTX: QUERYOPT=BYIMSI, IMSI="123456789012345";%% 
  RETCODE = 0  操作成功  
  输出结果如下 
  ------------------------ 
  Result  =   
  RU Name           =  LINK_SP_RU_0064  
  Process No.       =  1  
  IMSI              =  123456789012345  
  UE Ipv4 Address   =  192.168.53.55  
  UE Ipv6 Address   =  null  
  IMS-AKA User      =  true  
  spiUc             =  570875792  
  spiUs             =  2743546591  
  spiPc             =  2490370  
  spiPs             =  4280680450  
  portUc            =  41883  
  portUs            =  44775  
  portPc            =  9950  
  portPs            =  9900  
  Register Time     =  2024-05-31  17:04:47 
  (结果个数 = 1)  

  ---    END
  ```

#### 输出结果说明

| 参数名称            | 参数描述                    |
|:----------------|:------------------------|
| RU Name         | 该参数表示用户所在的资源单元名。        |
| Process No.     | 该参数表示用户所在的SGP进程号。       |
| User Num        | 该参数表示该进程的用户数量。          |
| All User Num    | 该参数表示所有的用户数量。           |
| IMSI            | 该参数表示指定IMSI。            |
| UE Ipv4 Address | 该参数表示用户的Ipv4地址。         |
| UE Ipv6 Address | 该参数表示用户的Ipv6地址。         |
| IMS-AKA User    | 该参数表示是否为IMS-AKA用户。      |
| spiUc           | 该参数表示IMS-AKA用户的spi_uc。  |
| spiUs           | 该参数表示IMS-AKA用户的spi_us。  |
| spiPc           | 该参数表示IMS-AKA用户的spi_pc。  |
| spiPs           | 该参数表示IMS-AKA用户的spi_ps。  |
| portUc          | 该参数表示IMS-AKA用户的port_uc。 |
| portUs          | 该参数表示IMS-AKA用户的port_us。 |
| portPc          | 该参数表示IMS-AKA用户的port_pc。 |
| portPs          | 该参数表示IMS-AKA用户的port_ps。 |
| Register Time   | 该参数表示用户注册时间。            |