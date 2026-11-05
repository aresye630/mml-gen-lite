# 查询NGAP协议参数（LST NGAPPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于显示NGAP协议参数配置信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                    |
|:------------|:-----------|:--------------------------------------------------------------------------------------------------------|
| NGAPPARAIDX | NGAP协议参数索引 | 可选必选说明：可选参数  参数含义：该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。  数据来源：本端规划  取值范围：整数类型，取值范围是0~31。  默认值：无  配置原则：无 |

## 使用实例

- 查询系统中当前配置的NGAP接口协议控制参数，执行如下命令：

  ```
  %%LST NGAPPARA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NGAP协议参数索引  AMF Configuration Update消息超时定时器(s)  AMF Configuration Update消息重发次数 (times)  Reset超时定时器(s)  Reset消息重发次数 (times)  重发NG SETUP REQUEST时长 (s)  等待时间指示器  

  0                 20                                         3                                             20                  3                          60                            否              
  1                 32                                         3                                             22                  3                          20                            否              
  (结果个数 = 2)

  ---    END
  ```
- 查询NGAPPARAIDX为1的当前配置的NGAP接口协议控制参数，执行如下命令：

  ```
  %%LST NGAPPARA: NGAPPARAIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                              NGAP协议参数索引  =  1
     AMF Configuration Update消息超时定时器(s)  =  32
  AMF Configuration Update消息重发次数 (times)  =  3
                            Reset超时定时器(s)  =  22
                     Reset消息重发次数 (times)  =  3
                  重发NG SETUP REQUEST时长 (s)  =  20
                                等待时间指示器  =  否
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称                                  | 输出项解释                                                                                                                                                                                                             |
|:---------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NGAP协议参数索引                             | 该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。                                                                                                                                                                             |
| AMF Configuration Update消息超时定时器(s)     | 该参数用于指定AMF配置变更消息的超时时长，当AMF发送AMF Configuration Request消息以后启动该定时器，等待对端NG RAN回AMF Configuration Acknowledge消息，在定时器超时时未收到该消息则认为AMF配置更新失败。AMF需要重发该消息。                                                                  |
| AMF Configuration Update消息重发次数 (times) | 该参数用于指定AMF配置更新消息的重发次数，当AMF发送AMF Configuration Request消息以后，等待对端NG RAN回AMF Configuration Acknowledge消息，在“AMFCFGUPTTMR”时间内未收到该消息或收到携带TimeToWait信元的AMF Configuration Update Failure消息，则AMF配置更新消息需要重发，重发的最大次数即为此参数的取值。 |
| Reset超时定时器(s)                          | 该参数用于指定Reset消息的超时时长。在AMF向NG RAN发送Reset消息以后，启动该定时器。在该定时器超时前没有收到NG-RAN回AMF Configuration Acknowledge消息，则AMF需要重新发送Reset消息。                                                                                           |
| Reset消息重发次数 (times)                    | 该参数用于指定Reset消息的最大重发次数。当AMF向NG RAN发送Reset消息超时次数达到该配置值后将不再重发。                                                                                                                                                       |
| 重发NG SETUP REQUEST时长 (s)               | 此参数用于设置NG Setup Failure消息中Time to Wait信元的值。该信元用于指示RAN再次发送NG Setup流程的等待时间。该参数在“等待时间指示器”参数设置为“YES(是)”时有效。                                                                                                           |
| 等待时间指示器                                | 该参数用于指定是否在NGAP层的NG Setup Failure消息中携带Time to wait信元。                                                                                                                                                              |