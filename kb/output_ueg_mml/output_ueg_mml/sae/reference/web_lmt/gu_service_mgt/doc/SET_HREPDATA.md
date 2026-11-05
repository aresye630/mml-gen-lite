# 设置透明数据(SET HREPDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中设置、修改、删除指定IMPU或PUSI的透明数据，包含普通透明数据和别名透明数据，别名透明数据对应的IMPU必须属于别名组，可以通过操作LST HSUB查询。

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。
- 当参数IMPU存在时，REPTYPE必须存在，参数PUSI存在时，REPTYPE不能存在。
- 当参数REPDATA存在时，参数SERVICEID和SERVICEDATA不能存在，当参数REPDATA不存在时，参数SERVICEID必须存在。
- 当“SH\_ALIASREPDATA\_SUPPORT\_DATAREFERENCE0”参数（可以通过命令LST HSYSTEMPARA查询）取值为“TRUE”时，“REPDATA”和“REPTYPE”参数必须为普通透明数据格式和类型。
- 执行该命令设置透明数据时，只支持处理一个ServiceIndication数据。

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                       |
|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU        | IMPU    | 用于设置透明数据的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                                                                                                                                             |
| PUSI        | PUSI    | 用于设置透明数据的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                                                                                                                                             |
| REPDATA     | 透明数据    | 用于设置指定的IMPU或PUSI的透明数据，此值可以为普通透明数据或者别名透明数据，如果存在字符“=”、“;”、“\”、“,”、“"”和“'”，需要在该字符前添加转义字符“\”。 透明数据格式：<?xml version\=\"1.0\"?><Sh-Data><RepositoryData><ServiceIndication></ServiceIndication><SequenceNumber></SequenceNumber><ServiceData></ServiceData></RepositoryData></Sh-Data> 取值范围：长度不超过16380的字符串 缺省值：无 |
| SERVICEID   | 服务标识    | 用于设置指定的IMPU或PUSI的服务标识。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                                                                                                                                                                           |
| SERVICEDATA | 服务数据    | 用于设置指定的IMPU或PUSI的服务数据。 取值范围： 长度不超过7718的字符串 缺省值： 无                                                                                                                                                                                                                                                          |
| REPTYPE     | 透明数据的类型 | 用于指定透明数据的类型，REPTYPE取值为ALIASREPDATA表示为别名透明数据，取值为REPDATA，表示为普通透明数据。 取值范围：ALIASREPDATA(Aliasrepository data)REPDATA(repository data) 缺省值： 无                                                                                                                                                                   |
| DATASOURCE  | 数据源     | 仅当“透明数据”参数输入时该参数有效，用于标识输入的“透明数据”参数的数据来源。 取值范围： PROV（业务发放系统）：透明数据来源于业务发放系统。CSSYNDATAProv（CS同步业务发放）：透明数据来源于业务发放系统，且自动同步到CS域。 缺省值：PROV（业务发放系统）                                                                                                                                                                |

## 使用实例

1. 设置透明数据。IMPU：sip:impuinfo@huawei.com，服务标识：“3”，服务数据：“SH\_RSI\_DATA”，透明数据的类型：REPDATA。

a.以“服务标识”和“服务数据”的方式设置：

```
SET HREPDATA: IMPU="sip:impuinfo@huawei.com", SERVICEID="3", SERVICEDATA="SH_RSI_DATA", REPTYPE=REPDATA;
```

b.以“透明数据”的方式且“ServiceData”不为空的设置：

```
SET HREPDATA: IMPU="sip:impuinfo@huawei.com", REPDATA="<?xml version\=\"1.0\"?><Sh-Data><RepositoryData><ServiceIndication>3</ServiceIndication><SequenceNumber>0</SequenceNumber><ServiceData><any>SH_RSI_DATA</any></ServiceData></RepositoryData></Sh-Data>", REPTYPE=REPDATA;
```

c.以“透明数据”的方式且“ServiceData”为空的设置：

```
SET HSYSTEMPARA: SERVICEDATA_WITHNOUT_CONTENT_METHOD=INSERT;
SET HREPDATA: IMPU="sip:impuinfo@huawei.com", REPDATA="<?xml version\=\"1.0\"?><Sh-Data><RepositoryData><ServiceIndication>3</ServiceIndication><SequenceNumber>0</SequenceNumber><ServiceData></ServiceData></RepositoryData></Sh-Data>", REPTYPE=REPDATA;
```

2. 修改透明数据。IMPU：sip:impuinfo@huawei.com，服务标识：“3”，服务数据：“SH\_STR\_DATA”，透明数据的类型：REPDATA。

```
SET HREPDATA: IMPU="sip:impuinfo@huawei.com", SERVICEID="3", SERVICEDATA="SH_STR_DATA", REPTYPE=REPDATA;
```

3. 删除透明数据。IMPU：sip:impuinfo@huawei.com，服务标识：“3”，透明数据的类型：REPDATA。

```
SET HREPDATA: IMPU="sip:impuinfo@huawei.com", SERVICEID="3", REPTYPE=REPDATA;
```

**说明** 

删除透明数据之前，需确保该透明数据已经添加，可通过**LST HREPDATA**查询。

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释              | 原因分析                                                                                                          | 处理建议                                                                                                                                    |
|----------:|:-------------------|:--------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| 900001008 | 参数不足               | “IMPU”或“PUSI”参数均未输入。                                                                                          | “IMPU”或“PUSI”必须存在且只能存在一个。                                                                                                               |
| 900001009 | 参数冲突               | 可能原因为如下之一： “IMPU”和“PUSI”两个参数同时输入。“PUSI”和“透明数据的类型”参数同时输入。“透明数据”和“服务标识”参数同时输入或同时未输入。“IMPU”参数输入时，“透明数据的类型”参数未输入。 | 根据实际情况，重新输入参数，确保满足以下几点： 参数“IMPU”和参数“PUSI”必须存在且只能存在一个。参数“PUSI”存在时，“透明数据的类型”不能存在。参数“透明数据”和参数“服务标识”不能同时输入或同时不输入。参数“IMPU”存在时，“透明数据的类型”必须存在。 |
| 900003060 | 请求消息中的IMPU不存在      | “IMPU”参数取值实际不存在，即用户对应的IMPU未开户。                                                                                | 需要重新输入“IMPU”，使用LST HSUB命令查询已存在的IMPU后，重新确认待设置透明数据的IMPU值。                                                                                 |
| 900003092 | PUSI不存在            | “PUSI”参数取值实际不存在，即对应的PUSI用户未开户。                                                                                | 需要重新输入“PUSI”，使用LST HPSI命令查询已存在的PUSI后，重新确认待设置透明数据的PUSI值。                                                                                 |
| 900003195 | 无效的sequence number | “透明数据”参数取值中的“SequenceNumber”字段取值无效。                                                                           | 需要重新输入“透明数据”参数，使用LST HREPDATA命令查询“SequenceNumber”，确保每次更新时比数据库中的“SequenceNumber”多加1。如果是第一次增加透明数据，则该参数需取值为“0”。                            |
| 900003196 | 透明数据格式无效           | “透明数据”参数取值不满足透明数据格式要求。                                                                                        | 需要重新输入“透明数据”参数，确保该参数取值满足透明数据格式要求。                                                                                                       |
| 900003198 | 透明数据超过最大限制         | 指定IMPU或PUSI对应的透明数据已超过最大限制。                                                                                    | 指定IMPU或PUSI对应的透明数据不能超过64条，若需要添加此条透明数据，请执行此命令删除添加的无用透明数据信息。                                                                              |
| 900003246 | IMPU不属于别名IMPUs     | 输入的用户IMPU不属于任何一个别名IMPU组。                                                                                      | 重新输入IMPU参数，确保该参数属于该用户的一个别名IMPU组中，可通过SET HALIASPU添加该IMPU至一个已存在的别名IMPU组中。                                                                 |
| 900003250 | 透明数据的长度超长          | “透明数据”参数取值长度超过16380个字符。                                                                                       | 重新输入参数取值，确保符合参数取值长度不能超过16380个字符。                                                                                                        |
| 900003476 | 透明数据类型不合法          | 当SET HSYSTEMPARA命令中的参数“别名透明数据是否支持datareference为0”设置为“TRUE”时，“透明数据的类型”参数设置为“ALIASREPDATA”。                     | 当SET HSYSTEMPARA命令中的参数“别名透明数据是否支持datareference为0”设置为“TRUE”时，“透明数据的类型”参数不能设置为“ALIASREPDATA”，仅可以取值为“REPDATA”。                             |
|      1001 | 无效的命令              | 输入的命令名称不正确。                                                                                                   | 请核对输入命令名称的正确性，并重新输入正确的命令。                                                                                                               |
| 900001004 | 无效的参数名             | 输入的参数标识不正确。                                                                                                   | 根据实际情况，重新输入提示错误的参数标识，确保参数标识正确。                                                                                                          |
| 900001007 | 无效的参数值             | 输入的参数取值不在其取值范围内。                                                                                              | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                        |
| 900001010 | 参数重复               | 输入命令中的同一参数重复出现。                                                                                               | 根据实际情况，重新输入命令，确保命令中每一个参数只出现一次。                                                                                                          |