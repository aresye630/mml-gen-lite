# 查询用户基础信息（LST PSUBINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询用户的基础信息，用户可以通过指定键值查询到用户的SID，方便问题定位。

## 注意事项

主从用户场景，由于主从用户共用同一个SID，当使用SID查询用户基础信息时，主用户及所有的从用户基础信息都会显示。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                 |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEYTYPE  | 键值类型   | 可选必选说明：必选参数 用于标识查询用户信息时所使用的键值类型。 取值范围： SID：用户的内部ID。SUBSCRIBERIDENTIFIER：用户名或用户ID。源自PGW Web LMT上的开户命令ADD PSUB中的参数“USRIDENTIFIER”。SUBSCRIBERIDENTIFIER2：用户的第二用户名或第二用户ID。源自PGW Web LMT上的开户命令ADD PSUB中的参数“USRSECONDIDENTIFIER”。 默认值：SUBSCRIBERIDENTIFIER |
| KEYVALUE | 键值     | 可选必选说明：必选参数 用于标识查询用户信息时所使用的键值。 取值范围： 当“键值类型”配置为“SID”时，该参数取值：长度固定为16且不包含"0x"前缀的十六进制字符串。当“键值类型”配置为“SUBSCRIBERIDENTIFIER”或“SUBSCRIBERIDENTIFIER2”时，该参数取值：长度不超过255的字符串。 默认值：无。                                                                           |

## 使用实例

查询用户基础信息：“键值类型”为“SUBSCRIBERIDENTIFIER”，“键值”为“46010381014\*\*\*\*”：

```
LST PSUBINFO: KEYTYPE=SUBSCRIBERIDENTIFIER, KEYVALUE="46010381014****";
```

```
%%LST PSUBINFO: KEYTYPE=SUBSCRIBERIDENTIFIER, KEYVALUE="46010381014****";%%
RETCODE = 0 Operation succeeded

Sub Info
SID:0502E952D6C5451E,SUBSCRIBERSN:0502E951D6C5451E,SUBSCRIBERIDENTIFIER:46010381014****

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息，输出项说明如表1所示。

| 输出项名称                | 输出项解释                                 |
|:---------------------|:--------------------------------------|
| SID                  | 表示用户的内部ID。                            |
| SUBSCRIBERSN         | 表示主从用户的内部ID，主从用户的SID相同SUBSCRIBERSN不同。 |
| SUBSCRIBERIDENTIFIER | 表示用户的用户名或用户ID。                        |