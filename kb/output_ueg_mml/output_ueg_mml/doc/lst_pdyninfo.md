# 查询用户动态信息（LST PDYNINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询用户动态信息。查询结果的第一行显示为用户动态信息，其余行显示为会话数据，具体行数根据实际情况显示。

## 注意事项

- 从用户改号后，主从用户重新上线之前，该命令查询的主从用户动态信息不可信。
- 若VRM\_DATAVIRTUALSUBIDSWITCH（数据会话虚拟用户标识开关）、VRM\_VIRTUALSUBIDSWITCH（虚拟用户标识开关）或VRM\_N15VIRTUALSUBIDSWITCH（N15会话虚拟用户标识开关）三个软参中，任一软参值被设置为“1”，则该命令返回的报文中“Serving PCRF”、“Online Status”、“Latest Online Or Offline Time”和“VOLTE Serving PCRF”四个字段的第一行输出结果不可信，请以第二行及以后的输出结果为准。

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                                 |
|:--------------|:-------|:-----------------------------------------------------|
| USRIDENTIFIER | 用户标识   | 用于指示系统需要按照哪个用户标识来查询用户动态信息。 取值范围：长度不超过255的字符串。 默认值：无。 |

## 使用实例

查询用户动态信息：“用户标识”为“46010381014\*\*\*\*”：

```
LST PDYNINFO: USRIDENTIFIER="46010381014****";
```

输出结果如下：

```
%%LST PDYNINFO: USRIDENTIFIER="46010381014****";%%
RETCODE = 0 操作成功

Serving PCRF      Online Status         Latest Online Or Offline Time  PLMN Name                         VOLTE Serving PCRF   Interface Type        SessionID                                                                                                                         N15 Serving PCRF
pcrf.huawei.com   Online                2025-03-07 15:59:02            NULL                              NULL                 NULL                  NULL                                                                                                                              NULL
pcrf.huawei.com   Online                NULL                           NULL                              NULL                 Gx                    39503234892Redundance_Data_SessSeparate_06_1339503234891                                                                          NULL
pcrf.huawei.com   Online                NULL                           NULL                              NULL                 N7                    1404c00522e45140403809611                                                                                                         NULL

Total count = 3

There is together 1 report

---    END
```

## 输出结果说明

| 输出项名称                         | 输出项解释                                                                                                                                                                                   |
|:------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serving PCRF                  | 用户的服务PCRF。 取值范围： NULL长度不超过64的字符串                                                                                                                                                        |
| Online Status                 | 用户的在线状态。 取值范围： OnlineOffline                                                                                                                                                            |
| Latest Online Or Offline Time | 用户最近的活动时间。用户在线时记录为最近的上线时间或在线过程中用户信息更新的时间；用户不在线时记录为最近的下线时间。时间格式为YYYY-MM-DD HH:MM:SS。 取值范围： NULL1970-01-01 00:00:00～2037-12-31 23:59:59：表示1970年01月01日00时00分00秒到2037年12月31日23时59分59秒之间的时间。 |
| PLMN Name                     | PLMN的名称。 取值范围： NULL长度不超过32字节的字符串                                                                                                                                                        |
| VoLTE Serving PCRF            | 表示用户的VoLTE业务服务PCRF。 取值范围： NULL长度不超过128字节的字符串  说明： 会话数据信息不区分是否为VoLTE会话，会话的服务PCRF信息均显示在“Serving PCRF”字段。                                                                                  |
| Interface Type                | 表示用户会话信息的接口类型。 取值范围： NULLGxN7N15N24                                                                                                                                                     |
| SessionID                     | 表示用户会话信息的会话ID。 NULL长度不超过128的字符串                                                                                                                                                         |
| N15 Serving PCRF              | 表示用户的N15业务服务PCRF。 取值范围： NULL长度不超过64字节的字符串                                                                                                                                               |