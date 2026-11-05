# 显示NETCONF会话信息（DSP NCSSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示NETCONF会话信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称        | 参数说明                                                                                                                                                                                      |
|:----------------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SESSIONID       | NETCONF会话ID | 可选必选说明：可选参数 参数含义：NETCONF会话标识。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。 默认值：无                                                                                                                     |
| VERBOSEFLG      | 详细信息标志位     | 可选必选说明：可选参数 参数含义：该参数用于表示详细信息标志位。 数据来源：本端规划 取值范围：整数类型，取值范围为0～1。“0”代表查询简要的会话信息，“1”代表查询详细的会话信息。 默认值：无 配置原则：如果需要指定详细信息标志位，则必须先指定NETCONF会话ID。 该命令不带参数“VERBOSEFLG” 和带参数“VERBOSEFLG=0”最终的显示是一致的。 |
| SERVICEINSTANCE | 服务实例        | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                              |

#### 使用实例

- 显示NETCONF会话的信息：

  ```
  DSP NCSSESSION:SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  NETCONF会话ID  用户名        通道ID  会话状态  事务状态  查询状态  多语种类型  通知状态  AAA认证会话ID  用户组ID  用户级别  会话是否被锁  协商能力集  NETCONF客户端能力集  待处理的get-next请求  任务组列表  

  59             VNFP_SYSTEM   134305  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  60             internaluser  134337  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  61             internaluser  134561  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  62             internaluser  134593  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  64             internaluser  134657  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  182            HAFG          134626  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  256            VNFP_SYSTEM   134690  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  5140           internaluser  134557  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  6282           internaluser  134828  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  9423           internaluser  134407  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  10463          internaluser  134487  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  11817          internaluser  134277  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  (结果个数 = 12)

  ---    END
  ```
- 显示指定NETCONF会话的信息：

  ```
  DSP NCSSESSION:SESSIONID=169,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
         NETCONF会话ID  =  59
                用户名  =  VNFP_SYSTEM
                通道ID  =  134305
              会话状态  =  READY
              事务状态  =  NEUTRAL
              查询状态  =  QUERY
            多语种类型  =  GENERAL
              通知状态  =  0
         AAA认证会话ID  =  1
              用户组ID  =  10
              用户级别  =  65535
          会话是否被锁  =  否
            协商能力集  =  NULL
   NETCONF客户端能力集  =  NULL
  待处理的get-next请求  =  NULL
            任务组列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 显示指定NETCONF会话的详细信息：

  ```
  DSP NCSSESSION:SESSIONID=169,VERBOSEFLG=1,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
         NETCONF会话ID  =  59
                用户名  =  VNFP_SYSTEM
                通道ID  =  134305
              会话状态  =  READY
              事务状态  =  NEUTRAL
              查询状态  =  QUERY
            多语种类型  =  GENERAL
              通知状态  =  0
         AAA认证会话ID  =  1
              用户组ID  =  10
              用户级别  =  65535
          会话是否被锁  =  否
            协商能力集  =  Base                     public   1.0
  Base                     private  2.0
  Writable-Running         public   1.0
  Candidate                public   1.0
  Distinct Startup         public   1.0
  Rollback on Error        public   1.0
  Confirmed Commit         public   1.0
  Exchange                 private  1.0
  Action                   private  2.0
   NETCONF客户端能力集  =  Total number of capabilities received : 7

  urn:ietf:params:netconf:base:1.0
  http://www.huawei.com/netconf/capability/action/1.0
  urn:ietf:params:netconf:capability:startup:1.0
  urn:ietf:params:netconf:capability:writable-running:1.0
  http://www.huawei.com/netconf/capability/exchange/1.0
  http://www.huawei.com/netconf/capability/base/2.0
  http://www.huawei.com/netconf/capability/action/2.0
  待处理的get-next请求  =  Total number of pending get-next requests : 0

            任务组列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称          | 输出项解释               |
|:---------------|:--------------------|
| NETCONF会话ID    | NETCONF会话标识。        |
| 用户名            | 建立NETCONF会话使用的用户名。  |
| 通道ID           | NETCONF通道标识。        |
| 会话状态           | NETCONF会话状态。        |
| 事务状态           | NETCONF事务状态。        |
| 查询状态           | NETCONF查询状态。        |
| 多语种类型          | NETCONF多语种类型。       |
| 通知状态           | NETCONF通知状态。        |
| AAA认证会话ID      | AAA认证会话标识。          |
| 用户组ID          | 用户所属的用户组标识。         |
| 用户级别           | 用户的级别。              |
| 会话是否被锁         | NETCONF会话是否被锁定。     |
| 协商能力集          | NETCONF协商的能力集。      |
| NETCONF客户端能力集  | NETCONF Client的能力集。 |
| 待处理的get-next请求 | 待处理的get-next请求个数。   |
| 任务组列表          | 允许的任务组列表。           |