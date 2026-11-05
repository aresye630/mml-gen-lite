# 显示客户端运行状态信息（DSP SSHCSTATUSINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SSH客户端运行状态信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识       | 参数名称      | 参数说明                                                                                                |
|:-----------|:----------|:----------------------------------------------------------------------------------------------------|
| QUERYTYPE  | 查询状态信息的类型 | 可选必选说明：必选参数 参数含义：该参数查询状态信息的类型。 数据来源：本端规划 取值范围：枚举类型。 GLOBALSTATUS：全局状态信息。SESSIONSTATUS：会话状态信息。 默认值：无 |
| MASTERTYPE | OMU类型     | 可选必选说明：可选参数 参数含义：该参数表示网元的主备类型。 数据来源：本端规划 取值范围：枚举类型。 MASTER：主。SLAVE：备。 默认值：MASTER                    |

#### 使用实例

- 显示主SSH客户端运行状态的全局信息：

  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=GLOBALSTATUS,MASTERTYPE=MASTER;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         OMU类型  =  主
  Socket注册状态  =  ACTIVE
        批备状态  =  INIT
    组件倒换状态  =  INIT
  批备消息定时器  =  NOT RUNNING
  倒换结束定时器  =  NOT RUNNING
        总会话数  =  7
  (结果个数 = 1)
  ---    END
  ```
- 显示备SSH客户端运行状态的全局信息：

  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=GLOBALSTATUS,MASTERTYPE=SLAVE;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         OMU类型  =  备
  Socket注册状态  =  ACTIVE
        批备状态  =  INIT
    组件倒换状态  =  INIT
  批备消息定时器  =  NOT RUNNING
  倒换结束定时器  =  NOT RUNNING
        总会话数  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示主SSH客户端运行状态的会话信息：

  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=SESSIONSTATUS,MASTERTYPE=MASTER;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  OMU类型          会话号           通道ID         会话ID         SSH版本          用户名        服务类型         会话主状态            会话子状态               会话用户状态        Socket拥塞定时器      保持连接定时器      Socket状态                   Socket下一个状态          对端端口        对端地址        本地地址      VPN索引  Socket文件描述符    管道ID              Ctos加密算法                  Stoc加密算法             Ctos HMAC算法         Stoc HMAC算法          Ctos压缩算法                Stoc压缩算法
  主               1                0              6              2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING             SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   830             192.168.0.2     192.168.0.1   2        22                  524300              AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  主               2                0              260            2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING             SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   22              192.168.0.3     192.168.0.1   2        18                  1048585             AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  (结果个数 = 2)
  ---    END
  ```
- 显示备SSH客户端运行状态的会话信息：

  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=SESSIONSTATUS,MASTERTYPE=SLAVE;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  OMU类型          会话号           通道ID         会话ID         SSH版本          用户名        服务类型         会话主状态            会话子状态               会话用户状态        Socket拥塞定时器      保持连接定时器       Socket状态                   Socket下一个状态          对端端口        对端地址        本地地址      VPN索引  Socket文件描述符    管道ID              Ctos加密算法                  Stoc加密算法             Ctos HMAC算法         Stoc HMAC算法          Ctos压缩算法                Stoc压缩算法

  备               1                0              6              2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING              SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   830             192.168.0.2     192.168.0.1   2        22                  524300              AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  备               2                0              260            2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING              SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   22              192.168.0.3     192.168.0.1   2        18                  1048585             AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称       | 输出项解释            |
|:------------|:-----------------|
| OMU类型       | 表示网元的主备类型。       |
| Socket注册状态  | 表示Socket注册状态。    |
| 批备状态        | 表示批备状态。          |
| 组件倒换状态      | 表示组件倒换状态。        |
| 批备消息定时器     | 表示批备消息定时器。       |
| 倒换结束定时器     | 表示倒换结束定时器。       |
| 总会话数        | 表示总会话数。          |
| 会话号         | 表示会话号。           |
| 通道ID        | 表示通道ID。          |
| 会话ID        | 表示会话ID。          |
| SSH版本       | 表示SSH版本。         |
| 用户名         | 表示用户名。           |
| 服务类型        | 表示服务类型。          |
| 会话主状态       | 表示会话主状态。         |
| 会话子状态       | 表示会话子状态。         |
| 会话用户状态      | 表示会话用户状态。        |
| Socket拥塞定时器 | 表示Socket拥塞定时器。   |
| 保持连接定时器     | 表示保持连接定时器。       |
| Socket状态    | 表示Socket状态。      |
| Socket下一个状态 | 表示Socket下一个状态。   |
| 对端端口        | 表示对端端口。          |
| 对端地址        | 表示对端地址。          |
| 本地地址        | 表示本地地址。          |
| VPN索引       | 表示VPN索引。         |
| Socket文件描述符 | 表示Socket文件描述符。   |
| 管道ID        | 表示管道ID。          |
| Ctos加密算法    | 表示Ctos加密算法。      |
| Stoc加密算法    | 表示Stoc加密算法。      |
| Ctos HMAC算法 | 表示Ctos HMAC加密算法。 |
| Stoc HMAC算法 | 表示Stoc HMAC加密算法。 |
| Ctos压缩算法    | 表示Ctos压缩算法。      |
| Stoc压缩算法    | 表示Stoc压缩算法。      |