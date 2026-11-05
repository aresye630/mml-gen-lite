# 查询用户的AS订阅数据信息(LST HASSUBDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询指定IMPU用户或PUSI用户中被AS订阅的数据信息。

AS可以通过向HSS发送SNR消息订阅指定用户的某类签约数据，完成订阅后，该数据更新时HSS会通过PNR消息将更新的数据发送给订阅的AS。

当命令的“参数标识”指定为“IMPU”时，可以查询：

- 对IMSUserState的订阅数据。
- 对S-CSCFName的订阅数据。
- 对iFC的订阅数据。
- 对RepositoryData的订阅数据。
- 对别名RepositoryData的订阅数据。
- 对别名IMPUs的订阅数据。
- 对IMSI的订阅数据。
- 对UE-SRVCC-Capability的订阅数据。
- 对ChargingInformation的订阅数据。
- 对IP-address-secure-binding-information的订阅数据。
- 对IMSPrivateUserIdentity的订阅数据。
- 对隐式注册集IMPUs的订阅数据。
- 对注册IMPUs的订阅数据。
- 对所有IMPUs的订阅数据。
- 订阅数据失效日期。

当命令的“参数标识”指定为“PUSI”时，可以查询：

- 对S-CSCFName的订阅数据。
- 对iFC的订阅数据。
- 对RepositoryData的订阅数据。
- PUSI的激活状态的订阅通知。
- 对ChargingInformation的订阅数据。
- 对隐式注册集IMPUs的订阅数据。
- 对所有IMPUs的订阅数据。
- 订阅数据失效日期。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                     |
|:-------|:-------|:-----------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指示需要查询哪个IMPU用户的AS订阅数据。 要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无。 |
| PUSI   | PUSI   | 用于指示需要查询哪个PUSI用户的AS订阅数据。 要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无。 |

## 使用实例

查询用户的AS订阅数据，“IMPU”为“sip:TC\_FS\_001\_1100\_impu\_1\_1@huawei.com”：

`LST HASSUBDATA: IMPU="sip:TC_FS_001_1100_impu_1_1@huawei.com";`

返回结果如下:

```
%%LST HASSUBDATA: IMPU="sip:TC_FS_001_1100_impu_1_1@huawei.com";%%
RETCODE = 0 SUCCESS0001:操作成功

SUBASID   DATATYPE                      ASNAME                                                                                                                          SRVIND                                                                                                                          ALIASID   IMPI                                                                                                                            ExpiryTime
34        8                                                                                                                                                                                                                                                                                             1         TC_FS_001_1100_impi_1@huawei.com                                                                                0

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表1所示。

| 参数标识       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBASID    | 用于返回订阅用户数据的Diameter对端实体AS的设备标识。若SET HSYSTEMPARA命令中“ASID管理方式”参数取值为“STORE_IN_USCDB”，则该参数的取值为执行ADD HASHOST命令配置的“ASID”参数的值。若SET HSYSTEMPARA命令中“ASID管理方式”参数取值为“STORE_IN_OMU”，则该参数的取值为在“UDM MML命令”窗口执行ADD DMPE命令时，系统自动生成的“Diameter对端实体设备标识”参数的值。                                                                                                                                                                                          |
| DATATYPE   | 订阅数据类型。 取值范围： IMSUserState(0)S-CSCFName(1)InitialFilterCriteria(2)RepositoryData(3)PSIActivation(4)AliasesRepositoryData(5)AliasesIMPU(6)IMSI(7)UE-SRVCC-Capability(8)ChargingInformation(9)IP-address-secure-binding-information(10)IMSPrivateUserIdentity(11)ImplicitIMPU(12)RegisteredIMPU(13)AllIMPU(14) 例如：返回报文中“DATATYPE = 3”表示订阅的数据类型为RepositoryData，即透明数据。 说明：AliasesIMPU，ImplicitIMPU，RegisteredIMPU和AllIMPU都属于IMPU订阅数据类型。 |
| ASNAME     | AS名称，即订阅数据的对端AS主机名。                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SRVIND     | 用于返回IMPU或PUSI关联的透明数据的唯一标识，即ServiceIndication。若用户订阅的数据类型为RepositoryData或AliasesRepositoryData（返回报文中“DATATYPE”值为“3”或“5”），此输出项显示为用户订阅的透明数据的ServiceIndication。若用户订阅的数据类型不为RepositoryData或AliasesRepositoryData（返回报文中“DATATYPE”值不为“3”或“5”），此输出项显示为空。                                                                                                                                                                                     |
| ALIASID    | 别名组ID，用于标识IMPU所在的别名组。                                                                                                                                                                                                                                                                                                                                                                                                               |
| IMPI       | 用来显示AS订阅UE-SRVCC-Capability数据时User-Name AVP携带的用户IMPI。 订阅信息中不包含IMPI时此输出项显示为空。                                                                                                                                                                                                                                                                                                                                                        |
| ExpiryTime | 订阅数据的失效日期。取值为0时表示订阅数据不会失效。                                                                                                                                                                                                                                                                                                                                                                                                          |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|       错误码 | 错误码解释         | 原因分析                                                                         | 处理建议                                                |
|----------:|:--------------|:-----------------------------------------------------------------------------|:----------------------------------------------------|
| 900001004 | 无效的参数名        | 该命令中的任意一个参数输入不正确。                                                            | 检查提示的错误参数，并输入正确的。                                   |
| 900001007 | 无效的参数值        | 可能原因为如下之一：“IMPU”或“PUSI”参数的取值不符合SIP URI或TEL URI格式。“IMPU”或“PUSI”取值的字符串长度超过127。 | 根据实际情况，重新输入“IMPU”或“PUSI”的取值，确保其取值符合要求。              |
| 900001008 | 参数不足          | 参数“IMPU”和“PUSI”都没有输入。                                                        | 根据实际情况，重新输入参数，确保“IMPU”和“PUSI”两个参数必须有且只能有一个参数出现。     |
| 900001009 | 参数冲突          | 同时输入了参数“IMPU”和“PUSI”。                                                        | 根据实际情况，重新输入参数，确保“IMPU”和“PUSI”两个参数必须有且只能有一个参数出现。     |
| 900001010 | 参数重复          | 重复输入该命令中的任意参数。                                                               | 核实输入的命令，若命令中任意参数输入两次以上，则删除多余的重复参数后，重新执行该命令。         |
| 900003060 | 请求消息中的IMPU不存在 | “IMPU”参数取值实际不存在，即用户对应的IMPU未定义。                                               | 需要重新输入“IMPU”，使用LST HSUB命令查询已存在的IMPU后，重新确认要查询的IMPU值。 |
| 900003092 | PUSI不存在       | “PUSI”参数取值实际不存在，即用户对应的PUSI未定义。                                               | 需要重新输入“PUSI”，使用LST HPSI命令查询已存在的PUSI后，重新确认要查询的PUSI值。 |
| 900003257 | 表中没有任何记录      | 输入的“IMPU”或“PUSI”没有被AS订阅的数据信息。                                                | 无需处理。                                               |