# 显示服务器运行状态信息（DSP SSHSSTATUSINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SSH服务器运行状态信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识      | 参数名称      | 参数说明                                                                                                  |
|:----------|:----------|:------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询状态信息的类型 | 可选必选说明：必选参数 参数含义：该参数表示查询状态信息的类型。 数据来源：本端规划 取值范围：枚举类型。 GLOBALSTATUS：全局状态信息。SESSIONSTATUS：会话状态信息。 默认值：无 |

#### 使用实例

- 显示SSH服务器运行状态的全局信息：

  ```
  DSP SSHSSTATUSINFO:QUERYTYPE=GLOBALSTATUS;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         Socket注册状态  =  ACTIVE
               批备状态  =  INIT
           组件倒换状态  =  SWITCH_INIT
      STelnet最大连接数  =  21
         SFTP最大连接数  =  15
     SNetconf最大连接数  =  20
         批备消息定时器  =  NOT RUNNING
         倒换结束定时器  =  NOT RUNNING
               总会话数  =  1
          STelnet会话数  =  1
             SFTP会话数  =  0
         SNetconf会话数  =  0
  IPv4 Socket文件描述符  =  11
        IPv4 Socket状态  =  SOCK_STATE_LISTEN
  IPv6 Socket文件描述符  =  4294967295
        IPv6 Socket状态  =  SOCK_STATE_DOWN
  (结果个数 = 1)
  ---    END
  ```
- 显示SSH服务器运行状态的会话信息：

  ```
  DSP SSHSSTATUSINFO:QUERYTYPE=SESSIONSTATUS;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                 会话号  =  1
                SSH版本  =  2.0
                VTY索引  =  VTY 0
                 用户名  =  omuser
               服务类型  =  STELNET
               连接状态  =  Connected
             会话主状态  =  SSH_MAIN_SSH_PROCESS
             会话子状态  =  SSH_SUB1_SESSION
           会话用户状态  =  NONE
        会话RSA鉴权状态  =  SSH_SUB3_AUTH_PK
           会话鉴权状态  =  SSH_SUB2_AUTH_ACK
             空闲定时器  =  RUNNING
             认证定时器  =  NOT RUNNING
       Socket拥塞定时器  =  NOT RUNNING
          AAA请求定时器  =  NOT RUNNING
   Socket选项时间定时器  =  NOT RUNNING
        IPv4 Socket状态  =  SOCKCONN_STATE_UP
       Socket下一个状态  =  SSHS_SOCKCONN_ACT_NONE
               对端端口  =  3160
               对端地址  =  192.168.1.11
               本地地址  =  192.168.2.3
                VPN索引  =  1
  IPv4 Socket文件描述符  =  42
                 管道ID  =  3145733
                 通道ID  =  131078
               QX会话数  =  0
               应用类型  =  NULL
                    TEI  =  0
                 交易数  =  0
                EQX动作  =  NULL
               认证状态  =  NULL
              OSP通道ID  =  0
               QX通道ID  =  0
              AAA会话ID  =  0
    QX Socket文件描述符  =  0
             对端网元ID  =  0
             本地网元ID  =  0
             QX会话状态  =  NULL
        QX CAML消息状态  =  NULL
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称            | 输出项解释               |
|:-----------------|:--------------------|
| Socket注册状态       | 表示Socket注册状态。       |
| 批备状态             | 表示批备状态。             |
| 组件倒换状态           | 表示组件倒换状态。           |
| STelnet最大连接数     | 表示STelnet最大连接数。     |
| SFTP最大连接数        | 表示SFTP最大连接数。        |
| SNetconf最大连接数    | 表示SNetconf最大连接数。    |
| 批备消息定时器          | 表示批备消息定时器。          |
| 倒换结束定时器          | 表示倒换结束定时器。          |
| 总会话数             | 表示总会话数。             |
| STelnet会话数       | 表示STelnet会话数。       |
| SFTP会话数          | 表示SFTP会话数。          |
| SNetconf会话数      | 表示SNetconf会话数。      |
| IPv4 Socket文件描述符 | 表示Socket文件描述符。      |
| IPv4 Socket状态    | 表示Socket状态。         |
| IPv6 Socket文件描述符 | 表示IPv6 Socket文件描述符。 |
| IPv6 Socket状态    | 表示IPv6 Socket状态。    |
| 会话号              | 表示会话号。              |
| SSH版本            | 表示SSH版本。            |
| VTY索引            | 表示VTY索引。            |
| 用户名              | 表示用户名。              |
| 服务类型             | 表示服务类型。             |
| 连接状态             | 表示连接状态。             |
| 会话主状态            | 表示会话主状态。            |
| 会话子状态            | 表示会话子状态。            |
| 会话用户状态           | 表示会话用户状态。           |
| 会话RSA鉴权状态        | 表示会话RSA鉴权状态。        |
| 会话鉴权状态           | 表示会话鉴权状态。           |
| 空闲定时器            | 表示空闲定时器。            |
| 认证定时器            | 表示认证定时器。            |
| Socket拥塞定时器      | 表示Socket拥塞定时器。      |
| AAA请求定时器         | 表示AAA请求定时器。         |
| Socket选项时间定时器    | 表示Socket选项定时器。      |
| Socket下一个状态      | 表示Socket下一个状态。      |
| 对端端口             | 表示对端端口。             |
| 对端地址             | 表示对端地址。             |
| 本地地址             | 表示本地地址。             |
| VPN索引            | 表示VPN索引。            |
| 管道ID             | 表示管道ID。             |
| 通道ID             | 表示通道ID。             |
| QX会话数            | 表示QX会话数。            |
| 应用类型             | 表示应用类型。             |
| TEI              | 表示TEI。              |
| 交易数              | 表示交易数。              |
| EQX动作            | 表示EQX动作。            |
| 认证状态             | 表示认证状态。             |
| OSP通道ID          | 表示OSP通道ID。          |
| QX通道ID           | 表示QX通道ID。           |
| AAA会话ID          | 表示AAA会话ID。          |
| QX Socket文件描述符   | 表示QX Socket文件描述符。   |
| 对端网元ID           | 表示对端网元ID。           |
| 本地网元ID           | 表示本地网元ID。           |
| QX会话状态           | 表示QX会话状态。           |
| QX CAML消息状态      | 表示QX CAML消息状态。      |