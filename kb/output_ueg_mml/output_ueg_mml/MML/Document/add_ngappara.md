# 增加NGAP协议参数（ADD NGAPPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于增加NGAP（NG Application Protocol）协议参数。

## 注意事项

- 该命令执行后立即生效。

- 索引为0的记录为默认记录，用户没有配置时默认使用该记录配置参数。

- 最多可输入32条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

|   NGAPPARAIDX |   AMFCFGUPTTMR |   AMFCFGUPTCNT |   RESETTMR |   RESETCNT | TIMETOWAITTMR   | TIMETOWAITFLG   |
|--------------:|---------------:|---------------:|-----------:|-----------:|:----------------|:----------------|
|             0 |             20 |              3 |         20 |          3 | Sixty           | No              |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                                   | 参数说明                                                                                                                                                                                                                                                                                    |
|:--------------|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NGAPPARAIDX   | NGAP协议参数索引                             | 可选必选说明：必选参数  参数含义：该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。  数据来源：本端规划  取值范围：整数类型，取值范围是0~31。  默认值：无  配置原则：无                                                                                                                                                                                 |
| AMFCFGUPTTMR  | AMF Configuration Update消息超时定时器(s)     | 可选必选说明：可选参数  参数含义：该参数用于指定AMF配置变更消息的超时时长，当AMF发送AMF Configuration Request消息以后启动该定时器，等待对端NG RAN回AMF Configuration Acknowledge消息，在定时器超时时未收到该消息则认为AMF配置更新失败。AMF需要重发该消息。  数据来源：对端协商  取值范围：整数类型，取值范围是1~65534，单位是秒。  默认值：20  配置原则：无                                                             |
| AMFCFGUPTCNT  | AMF Configuration Update消息重发次数 (times) | 可选必选说明：可选参数  参数含义：该参数用于指定AMF配置更新消息的重发次数，当AMF发送AMF Configuration Request消息以后，等待对端NG RAN回AMF Configuration Acknowledge消息，在“AMFCFGUPTTMR”时间内未收到该消息或收到携带TimeToWait信元的AMF Configuration Update Failure消息，则AMF配置更新消息需要重发，重发的最大次数即为此参数的取值。  数据来源：对端协商  取值范围：整数类型，取值范围是1~3，单位是次。  默认值：3  配置原则：无 |
| RESETTMR      | Reset超时定时器(s)                          | 可选必选说明：可选参数  参数含义：该参数用于指定Reset消息的超时时长。在AMF向NG RAN发送Reset消息以后，启动该定时器。在该定时器超时前没有收到NG-RAN回AMF Configuration Acknowledge消息，则AMF需要重新发送Reset消息。  数据来源：对端协商  取值范围：整数类型，取值范围是1~65534，单位是秒。  默认值：20  配置原则：无                                                                                      |
| RESETCNT      | Reset消息重发次数 (times)                    | 可选必选说明：可选参数  参数含义：该参数用于指定Reset消息的最大重发次数。当AMF向NG RAN发送Reset消息超时次数达到该配置值后将不再重发。  数据来源：对端协商  取值范围：整数类型，取值范围是1~3，单位是次。  默认值：3  配置原则：无                                                                                                                                                       |
| TIMETOWAITTMR | 重发NG SETUP REQUEST时长 (s)               | 可选必选说明：可选参数  参数含义：此参数用于设置NG Setup Failure消息中Time to Wait信元的值。该信元用于指示RAN再次发送NG Setup流程的等待时间。该参数在“等待时间指示器”参数设置为“YES(是)”时有效。  数据来源：全网规划 取值范围： “One（1）”：1“Two（2）”：2“Five（5）”：5“Ten（10）”：10“Twenty（20）”：20“Sixty（60）”：60  默认值：Sixty  配置原则：无                                                  |
| TIMETOWAITFLG | 等待时间指示器                                | 可选必选说明：可选参数  参数含义：该参数用于指定是否在NGAP层的NG Setup Failure消息中携带Time to wait信元。  数据来源：对端协商 取值范围： “Yes（是）”：是“No（否）”：否  默认值：No  配置原则：无                                                                                                                                                             |

## 使用实例

增加NGAP接口协议控制参数：NGAP协议参数索引为1，AMF Configuration Update消息超时定时器(s)为20s，AMF Configuration Update消息重发次数 (times)为3，Reset超时定时器(s)为20s，Reset消息重发次数 (times)为3，重发NG SETUP REQUEST时长 (s)为60s，等待时间指示器为是。执行如下命令：

```
ADD NGAPPARA: NGAPPARAIDX=1, AMFCFGUPTTMR=20, AMFCFGUPTCNT=3, RESETTMR=20, RESETCNT=3, TIMETOWAITTMR=Sixty, TIMETOWAITFLG=Yes;
```