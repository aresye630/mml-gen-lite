# 查询用户的Service provider ID(服务提供商标识)(LST HSERPRV)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定的IMPU或者PUSI的Service provider ID(服务提供商标识)。

## 注意事项

参数IMPU和参数PUSI必须存在且仅能存在一个。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                         |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要查询Service provider ID(服务提供商标识)的IMPU。要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| PUSI   | PUSI   | 用于指定一个需要查询Service provider ID(服务提供商标识)的PUSI。要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

查询指定IMPU的Service provider ID。IMPU：sip:impuinfo@huawei.com。

```
LST HSERPRV: IMPU="sip:impuinfo@huawei.com";
```

## 输出结果说明

| 参数标识     | 参数说明          |
|:---------|:--------------|
| SERPRVID | 显示用户的服务提供商标识。 |