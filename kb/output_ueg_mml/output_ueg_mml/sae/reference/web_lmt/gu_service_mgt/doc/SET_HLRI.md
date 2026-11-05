# 设置IMPU或PUSI的松路由标志(SET HLRI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定IMPU或PUSI的松路由指示。

## 注意事项

参数IMPU和参数PUSI必须存在且只能存在一个。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                       |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要设置松路由指示的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                      |
| PUSI   | PUSI   | 用于指定一个需要设置松路由指示的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                      |
| LRI    | 松路由指示  | 指定IMPU是否签约松路由指示： LOOSE_ROUTE_REQUIRED：签约松路由指示； LOOSE_ROUTE_NOT_REQUIRED：去签约松路由指示。 取值范围：LOOSE_ROUTE_NOT_REQUIRED(Loose route not required)LOOSE_ROUTE_REQUIRED(Loose route required) 缺省值： 无 |

## 使用实例

设置IMPU或PUSI的松路由指示。IMPU：sip:impuinfo@huawei.com，松路由指示：LOOSE\_ROUTE\_NOT\_REQUIRED。

```
SET HLRI: IMPU="sip:impuinfo@huawei.com", LRI=LOOSE_ROUTE_NOT_REQUIRED;
```