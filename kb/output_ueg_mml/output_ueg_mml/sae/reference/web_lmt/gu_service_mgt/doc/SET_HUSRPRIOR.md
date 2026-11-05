# 设置IMPU或PUSI的优先级(SET HUSRPRIOR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定的IMPU或PUSI的优先级。

## 注意事项

参数IMPU和参数PUSI必须存在且仅能存在一个。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                          |
|:---------|:-------|:----------------------------------------------------------------------------------------------|
| IMPU     | IMPU   | 用于指定一个需要设置优先级的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无             |
| PUSI     | PUSI   | 用于指定一个需要设置优先级的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无             |
| USRPRIOR | 优先级    | 指定该IMPU或者PUSI的优先级。HIGH：高优先级。MIDDLE：中优先级。LOW：低优先级。 取值范围：HIGH(HIGH)MIDDLE(MIDDLE)LOW(LOW) 缺省值：无 |

## 使用实例

设置IMPU或PUSI的优先级。IMPU：sip:impuinfo@huawei.com，优先级：HIGH。

```
SET HUSRPRIOR: IMPU="sip:impuinfo@huawei.com", USRPRIOR=HIGH;
```