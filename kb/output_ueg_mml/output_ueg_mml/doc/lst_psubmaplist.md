# 查询用户多卡用户列表（LST PSUBMAPLIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用来查询从用户下面关联的所有多卡用户。

## 注意事项

无。

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                          |
|:--------------|:-------|:----------------------------------------------|
| USRIDENTIFIER | 公共用户标识 | 用于标识多卡用户所属的从用户的用户标识。 取值范围：长度不超过20的字符串。 默认值：无。 |

## 使用实例

查询用户签约：“公共用户标识”为“MultiSim01”：

```
LST PSUBMAPLIST: USRIDENTIFIER="Master01Slave01";
```

```
%%LST PSUBMAPLIST: USRIDENTIFIER="Master01Slave01";%%
RETCODE = 0 Operation succeeded
Multi-SIM subscriber ID                   Multi-SIM subscriber Type
MultiSim01                                END_USER_E164     

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 输出项名称                     | 输出项解释                                                                                                             |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------|
| Multi-SIM subscriber ID   | 用于标识Multi-SIM用户的标识。 取值范围：长度不超过20的字符串。 默认值：无。                                                                      |
| Multi-SIM subscriber Type | 用于标识Multi-SIM用户的类型。 取值范围： 0:END_USER_E1641:END_USER_IMSI2:END_USER_SIP_URI3:END_USER_NAI4:END_USER_PRIVATE 默认值：无。 |