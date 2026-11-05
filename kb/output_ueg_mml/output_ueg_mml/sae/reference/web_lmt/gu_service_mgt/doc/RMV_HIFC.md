# 删除iFC(RMV HIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于从HSS的业务数据库中删除指定IMPU或指定PUSI相关的Service Profile所包含的指定优先级的iFC。

## 注意事项

参数IMPU和参数PUSI必须存在且只能存在一个。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                |
|:---------|:-------|:------------------------------------------------------------------------------------|
| IMPU     | IMPU   | 用于指定一个需要删除iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无   |
| PUSI     | PUSI   | 用于指定一个需要删除iFC信息的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无 |
| PRIORITY | 优先级    | 用于指定一个被删除iFC的优先级。 取值范围：0～65535 缺省值：无                                                |

## 使用实例

删除iFC。IMPU：sip:impuinfo@huawei.com，优先级：1。

```
RMV HIFC: IMPU="sip:impuinfo@huawei.com", PRIORITY=1;
```