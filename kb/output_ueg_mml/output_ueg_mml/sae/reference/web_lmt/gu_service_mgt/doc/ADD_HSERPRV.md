# 增加用户的Service provider ID(服务提供商标识)(ADD HSERPRV)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中添加指定的IMPU或者PUSI的Service Provider ID(服务提供商标识)。

## 注意事项

- 参数IMPU和参数PUSI必须存在且仅能存在一个。
- 在设置指定的IMPU或者PUSI的Service Provider ID之前，指定的IMPU或者PUSI的Service Provider ID必须不存在，否则HSS返回失败。

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                         |
|:---------|:--------|:-------------------------------------------------------------------------------------------------------------|
| IMPU     | IMPU    | 用于指定一个需要设置Service provider ID(服务提供商标识)的IMPU。要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| PUSI     | PUSI    | 用于指定一个需要设置Service provider ID(服务提供商标识)的PUSI。要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| SERPRVID | 服务提供商标识 | 用于指定IMPU或者PUSI的Service provider ID(服务提供商标识)。 取值范围： 长度不超过39的字符串 缺省值： 无                                        |

## 使用实例

增加用户的Service provider ID(服务提供商标识)。IMPU：sip:impuinfo@huawei.com，服务提供商标识：huawei。

```
ADD HSERPRV: IMPU="sip:impuinfo@huawei.com", SERPRVID="huawei";
```