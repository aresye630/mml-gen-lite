# 显示所有NETCONF代理VNFC会话信息（DSP NCSPROXYSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示NETCONF代理VNFC会话信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                         |
|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------|
| SESSSTCFLG  | 会话统计标志位 | 可选必选说明：必选参数 参数含义：会话统计标志位。 数据来源：本端规划 取值范围：枚举类型。 PROXYSESSION：代理会话。PROXYSTC：统计标志位。 默认值：无                                       |
| EMSSESSID   | 网管会话ID  | 可选必选说明：条件可选参数，该参数在“SESSSTCFLG”配置为“PROXYSTC”时为可选参数。 参数含义：网管与网元的NETCONF会话标识。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。 默认值：无           |
| HISTORYFLG  | 会话历史标志  | 可选必选说明：条件可选参数，该参数在“SESSSTCFLG”配置为“PROXYSESSION”时为可选参数。 参数含义：NETCONF代理会话历史标志。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 |
| OVERTIMEFLG | 会话超时标志位 | 可选必选说明：条件可选参数，该参数在“SESSSTCFLG”配置为“PROXYSTC”时为可选参数。 参数含义：会话超时标志位。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无             |

#### 使用实例

- 显示所有NETCONF代理会话信息:

  ```
  DSP NCSPROXYSESSION:SESSSTCFLG=PROXYSESSION;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  网管会话ID  目标                     VNFC标识  VNFC类型   VNFC会话标识  VNFC会话状态  会话终止时间  VNFC名称       VNFC通道标识  用户名  会话统计信息  会话超时消息  

  72          SirpAgent=ACS            1         ACS_VNFC   120           READY         NULL          ACS            0             NULL    NULL          NULL                   
  72          SirpAgent=CSDB_VNFC_999  2         CSDB_VNFC  117           READY         NULL          CSDB_VNFC_999  0             NULL    NULL          NULL          
  72          SirpAgent=CSLB_VNFC_999  3         CSLB_VNFC  63            READY         NULL          CSLB_VNFC_999  0             NULL    NULL          NULL  
  (结果个数 = 3)
  ---    END
  ```

- 显示所有NETCONF代理会话历史信息：

  ```
  DSP NCSPROXYSESSION:SESSSTCFLG=PROXYSESSION,HISTORYFLG=TRUE;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  网管会话ID  目标  VNFC标识  VNFC类型  VNFC会话标识  VNFC会话状态    会话终止时间     VNFC名称     VNFC通道标识  用户名        会话统计信息  会话超时消息  
            
  39737       NULL  0         NULL      11067         carrier-closed  31/03:01:24:578  CSDB_VNFC_9  779           internaluser  NULL          NULL          
  39737       NULL  0         NULL      10936         carrier-closed  31/03:01:24:578  CSLB_VNFC_9  780           internaluser  NULL          NULL          
  39737       NULL  0         NULL      10850         carrier-closed  31/03:01:24:578  LINK_VNFC_9  781           internaluser  NULL          NULL          
  39737       NULL  0         NULL      10469         carrier-closed  31/03:01:24:578  VNRS_VNFC_9  782           internaluser  NULL          NULL          
  39737       NULL  0         NULL      10962         carrier-closed  31/03:01:24:578  XSF_VNFC_99  783           internaluser  NULL          NULL          
  39686       NULL  0         NULL      10567         carrier-closed  31/03:03:23:757  ACS          763           internaluser  NULL          NULL                  
  39686       NULL  0         NULL      11062         carrier-closed  31/03:03:23:757  CSDB_VNFC_9  765           internaluser  NULL          NULL          
  39686       NULL  0         NULL      10931         carrier-closed  31/03:03:23:757  CSLB_VNFC_9  766           internaluser  NULL          NULL          
  39686       NULL  0         NULL      10845         carrier-closed  31/03:03:23:757  LINK_VNFC_9  767           internaluser  NULL          NULL          
  39686       NULL  0         NULL      10464         carrier-closed  31/03:03:23:757  VNRS_VNFC_9  768           internaluser  NULL          NULL          
  39686       NULL  0         NULL      10955         carrier-closed  31/03:03:23:757  XSF_VNFC_99  769           internaluser  NULL          NULL          
  (结果个数 = 11)
  ---    END
  ```

- 显示所有活动的NETCONF代理VNFC会话统计：

  ```
  DSP NCSPROXYSESSION:SESSSTCFLG=PROXYSTC;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  网管会话ID  目标  VNFC标识  VNFC类型  VNFC会话标识  VNFC会话状态  会话终止时间  VNFC名称  VNFC通道标识  用户名  会话统计信息   会话超时消息  

  0           NULL  0         NULL      0             NULL          NULL          NULL      0             NULL    --------------Display  NETCONF proxy statistics------

  EMS-SessionId:72   CreateTime:2023-07-28, 23:42:59:314
  Packet statistics:
      Rpc requests received:12704 
      Rpc response sent:12703 
      Rpc requests delayed:0 
      Notifications sent:4143 

  Flow-control buffer statistics:
      Number of Messages in buffer:0 
      Number of Messages re-sent:0 

  Packet drop statistics:
      MallocFail:0 
      Invalid-State:9 
      FlowContrlBufOverflow:0 
      Invalid-req:11 
      Invalid-resp:16354 
      No match request:0 
      AddXmlPropfailed:0 
      XmlDump failed:0 
      RPC time-out:0 

  NLS statistics:
  ----------------------------------
  NLS-id:1   Session-id:120 
  Packet statistics:
      Rpc requests received:2765 
      Rpc response sent:2765 
      Rpc requests delayed:0 
      Notifications sent:4142 

  (结果个数 = 1)

  ---    END
  ```

- 显示所有NETCONF代理会话超时消息：

  ```
  DSP NCSPROXYSESSION:SESSSTCFLG=PROXYSTC,OVERTIMEFLG=TRUE;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  网管会话ID  目标  VNFC标识  VNFC类型  VNFC会话标识  VNFC会话状态  会话终止时间  VNFC名称  VNFC通道标识  用户名  会话统计信息  会话超时消息                                                                                                                                                                                                                                                                                                                                                                                                                   

  0           NULL  0         NULL      0             NULL          NULL          NULL      0             NULL    NULL          ----------------------------------------------------------------------------------------------------
  StartTime       EndTime         NlsChannelID  SessionID User           Terminal     MsgID    NlsName
  ----------------------------------------------------------------------------------------------------
  28/23:44:19:053 28/23:44:59:315 0x000000ce    0x0048    internaluser   172.16.253.35     tzone_updat XSF_VNFC_99  
  0           NULL  0         NULL      0             NULL          NULL          NULL      0             NULL    NULL          
  28/23:44:19:392 28/23:44:59:317 0x000000ce    0x0048    internaluser   172.16.253.35     conn_sub_0_ XSF_VNFC_99                                                                                                                                                                                                                                                                                                                
  0           NULL  0         NULL      0             NULL          NULL          NULL      0             NULL    NULL          
  28/23:44:19:393 28/23:45:19:453 0x000000ce    0x0048    internaluser   172.16.253.35     tzone_updat XSF_VNFC_99                                                                                                                                                                                                                                                                                                                
  0           NULL  0         NULL      0             NULL          NULL          NULL      0             NULL    NULL          
  28/23:44:49:049 28/23:45:19:486 0x000000ce    0x0048    internaluser   172.16.253.35     tzone_updat XSF_VNFC_99                                                                                                                                                                                                                                                                                                                
  (结果个数 = 4)

  ---    END
  ```

#### 输出结果说明

| 输出项名称    | 输出项解释                |
|:---------|:---------------------|
| 网管会话ID   | 网管与网元的NETCONF会话标识。   |
| 目标       | 代理转发的目的地。            |
| VNFC标识   | VNFC的标识。             |
| VNFC类型   | VNFC的类型。             |
| VNFC会话标识 | 代理与VNFC的NETCONF会话标识。 |
| VNFC会话状态 | 代理与VNFC的会话状态。        |
| 会话终止时间   | 网管与网元的会话终止时间。        |
| VNFC名称   | VNFC的名称。             |
| VNFC通道标识 | 代理与VNFC的通道标识。        |
| 用户名      | VNFC认证的用户名。          |
| 会话统计信息   | NETCONF代理会话统计信息。     |
| 会话超时消息   | 会话超时消息。              |