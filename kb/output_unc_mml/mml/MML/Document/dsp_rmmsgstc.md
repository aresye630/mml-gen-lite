# 查询路由管理消息统计信息（DSP RMMSGSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询路由管理消息统计信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                        |
|:--------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|
| VERBOSE | 是否详细信息     | 可选必选说明：必选参数 参数含义：该参数用于表示是否详细信息。 数据来源：本端规划 取值范围：枚举类型。 true：是。false：否。 默认值：无                                                  |
| AFTYPE  | 地址族        | 可选必选说明：必选参数 参数含义：该参数用于表示路由所属VPN的地址族。 数据来源：本端规划 取值范围：枚举类型。 ipv4unicast：IPv4单播。ipv6unicast：IPv6单播。 默认值：无                      |
| PID     | Partner ID | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSE”配置为“true”时为必选参数。 参数含义：该参数用于表示Partner ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无 |

#### 使用实例

- 查询路由管理消息统计信息：

  ```
  DSP RMMSGSTC:AFTYPE=ipv4unicast,VERBOSE=false;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  Partner ID    接收数目    丢弃数目    发送数目    发送失败数目    重传数目    序列号异常数目    流控数目

  0x1           0           0           0           0               0           0                 0
  0x0           0           0           0           0               0           0                 0
  0x10004       0           0           0           0               0           0                 0
  0x60000B      0           0           0           0               0           0                 0
  0x660016      0           0           0           0               0           0                 0
  0x670015      12          0           12          0               0           0                 0
  0x69002D      0           0           0           0               0           0                 0
  0x6A0017      3753        0           5809        0               0           0                 0
  0x6F0001      281         0           20          0               1           0                 0
  0x700002      254         0           5           0               1           0                 0
  0x740020      0           0           0           0               0           0                 0
  0x770008      0           0           0           0               0           0                 0
  0x790014      0           0           0           0               0           0                 0
  0x7A0013      0           0           0           0               0           0                 0
  0xA60025      3           0           3           0               0           0                 0
  0xE7000A      0           0           0           0               0           0                 0
  0x80710060    145         0           511         0               0           0                 0
  (结果个数 = 17)
  ---    END
  ```
- 查询路由管理消息统计详细信息：

  ```
  DSP RMMSGSTC:AFTYPE=ipv4unicast,VERBOSE=true,PID="700002";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  消息类型                                类ID                               接收数目    发送数目

  MSG_RMI_ADD_PRODUCER                    CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_DELETE_PRODUCER                 CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_BATCH_ADD_PRODUCER_BEGIN        CLASS_RMI_DEFAULT                  1           1
  MSG_RMI_BATCH_ADD_PRODUCER              CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_BATCH_ADD_PRODUCER_END          CLASS_RMI_DEFAULT                  1           1
  MSG_RMI_COLLECT_PRODUCER                CLASS_RMI_DEFAULT                  1           2
  MSG_RMI_SMOOTH_REQUEST                  CLASS_RMI_ROUTE                    0           0
  MSG_RMI_UPDATE                          CLASS_RMI_PATH                     125         0
  MSG_RMI_UPDATE                          CLASS_RMI_IID                      125         0
  MSG_RMI_BATCH_UPDATE_BEGIN              CLASS_RMI_PATH                     0           0
  MSG_RMI_BATCH_UPDATE_BEGIN              CLASS_RMI_IID                      0           0
  MSG_RMI_BATCH_UPDATE                    CLASS_RMI_PATH                     0           0
  MSG_RMI_BATCH_UPDATE                    CLASS_RMI_IID                      0           0
  MSG_RMI_BATCH_UPDATE_END                CLASS_RMI_PATH                     0           0
  MSG_RMI_BATCH_UPDATE_END                CLASS_RMI_IID                      0           0
  MSG_RMI_APPLY_SERVICE                   CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_RELEASE_SERVICE                 CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_SUBSCRIBE                       CLASS_RMI_SINGLE_ROUTE             0           0
  MSG_RMI_SUBSCRIBE                       CLASS_RMI_IMPORT_ROUTE             0           0
  MSG_RMI_SUBSCRIBE                       CLASS_RMI_SUBSCRIBE_POLICY         0           0
  MSG_RMI_UNSUBSCRIBE                     CLASS_RMI_SINGLE_ROUTE             0           0
  MSG_RMI_UNSUBSCRIBE                     CLASS_RMI_IMPORT_ROUTE             0           0
  MSG_RMI_UNSUBSCRIBE                     CLASS_RMI_SUBSCRIBE_POLICY         0           0
  MSG_RMI_SUBSCRIBE_UPDATE                CLASS_RMI_SINGLE_ROUTE             0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_BEGIN    CLASS_RMI_IMPORT_PATH              0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_BEGIN    CLASS_RMI_IMPORT_IID               0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_BEGIN    CLASS_RMI_SUBSCRIBE_POLICY_PATH    0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_BEGIN    CLASS_RMI_SUBSCRIBE_POLICY_IID     0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE          CLASS_RMI_IMPORT_PATH              0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE          CLASS_RMI_IMPORT_IID               0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE          CLASS_RMI_SUBSCRIBE_POLICY_PATH    0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE          CLASS_RMI_SUBSCRIBE_POLICY_IID     0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_END      CLASS_RMI_IMPORT_PATH              0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_END      CLASS_RMI_IMPORT_IID               0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_END      CLASS_RMI_SUBSCRIBE_POLICY_PATH    0           0
  MSG_RMI_SUBSCRIBE_BATCH_UPDATE_END      CLASS_RMI_SUBSCRIBE_POLICY_IID     0           0
  MSG_RMI_QUERY                           CLASS_RMI_ATTR                     0           0
  MSG_RMI_UPDATE_TABLE_STATE              CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_NOTIFY_EVENT                    CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_VERIFICATION_REQUEST            CLASS_RMI_DEFAULT                  0           0
  MSG_RMI_NOTIFY_EVENT                    CLASS_RMI_PATH                     0           0
  MSG_RMI_NOTIFY_EVENT                    CLASS_RMI_IID                      0           0
  MSG_RMI_VERIFICATION_REQUEST            CLASS_RMI_PRODUCER                 0           0
  MSG_RMI_VERIFICATION_REQUEST            CLASS_RMI_ROUTE                    0           0
  (结果个数 = 44)
  ---    END
  ```

#### 输出结果说明

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| Partner ID | 用于表示Partner ID。 |
| 接收数目       | 用于表示接收数目。       |
| 丢弃数目       | 用于表示丢弃数目。       |
| 发送数目       | 用于表示发送数目。       |
| 发送失败数目     | 用于表示发送失败数目。     |
| 重传数目       | 用于表示重传数目。       |
| 序列号异常数目    | 用于表示序列号异常数目。    |
| 流控数目       | 用于表示流控数目。       |
| 消息类型       | 用于表示消息类型。       |
| 类ID        | 用于表示类ID。        |