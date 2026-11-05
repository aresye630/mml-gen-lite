# 设置IMPU或PUSI的标准优先级(SET HSTDPRIOR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定的IMPU或PUSI的3GPP协议规定的优先级数据。

优先级数据分为标准优先级数据与扩展优先级数据，标准优先级数据由参数“标准优先级”指定，扩展优先级数据由参数“扩展优先级域名空间”与“扩展优先级”的组合指定。当需要对IMPU或PUSI号码设置优先级业务时，操作员可以使用**SET
HSTDPRIOR**命令完成。

## 注意事项

- 参数“IMPU”和参数“PUSI”必须存在且仅能存在一个。
- 参数“扩展优先级域名空间”或“用户自定义优先级域名空间”与“扩展优先级”必须同时存在或同时不存在。
- 参数“扩展优先级域名空间”与“扩展优先级”的组合和参数“标准优先级”至少存在一个。
- 参数“扩展优先级域名空间”和参数“用户自定义优先级域名空间”只能存在一个。

## 参数说明

| 参数标识      | 参数名称         | 参数说明                                                                                                                                                                                                                                 |
|:----------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU      | IMPU         | 用于指定一个需要设置优先级数据的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串。 默认值：无。 说明：可选参数。                                                                                                                                       |
| PUSI      | PUSI         | 用于指定一个需要设置优先级数据的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串。 默认值：无。 说明：可选参数。                                                                                                                                       |
| STDPRIOR  | 标准优先级        | 指定该IMPU或PUSI的标准优先级。 取值范围： HIGHEST-PRIORITY(HIGHEST-PRIORITY)HIGH-PRIORITY(HIGH-PRIORITY)MIDDLE-PRIORITY(MIDDLE-PRIORITY)LOW-PRIORITY(LOW-PRIORITY)LOWEST-PRIORITY(LOWEST-PRIORITY)INVALID-PRIORITY(INVALID-PRIORITY) 默认值：无。 说明：可选参数。 |
| NAMESPACE | 扩展优先级域名空间    | 指定该IMPU或PUSI的扩展优先级域名空间。 取值范围：WPS(wps) 默认值：无。 说明：可选参数。                                                                                                                                                                                |
| EXTPRIOR  | 扩展优先级        | 指定该IMPU或PUSI的扩展优先级。 取值范围： 0～4：用于表示用户的扩展优先级，其高低随数值的增加而降低。255：用于表示删除用户的扩展优先级。 默认值：无。 说明：可选参数。                                                                                                                                          |
| CNAMESP   | 用户自定义优先级域名空间 | 用于标识配置用户优先级的自定义域名空间。 取值范围：1～31位由数字、字母或特殊字符等组成的字符串。 默认值：无。                                                                                                                                                                            |

## 使用实例

1，设置IMPU或PUSI的优先级。“IMPU”为“sip:impuinfo@huawei.com”，“标准优先级”为“MIDDLE-PRIORITY”，“扩展优先级域名空间”为“WPS”，“扩展优先级”为“2”：

```
SET HSTDPRIOR: IMPU="sip:impuinfo@huawei.com", STDPRIOR=MIDDLE-PRIORITY, NAMESPACE=WPS, EXTPRIOR=2;
```

2，删除IMPU或PUSI的优先级。“IMPU”为“tel:+123”，“扩展优先级域名空间”为“WPS”，“扩展优先级”为“255”：

```
SET HSTDPRIOR: IMPU="tel:+123", NAMESPACE=WPS, EXTPRIOR=255;
```