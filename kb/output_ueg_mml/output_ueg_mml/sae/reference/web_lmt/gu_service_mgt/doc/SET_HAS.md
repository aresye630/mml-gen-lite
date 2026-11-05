# 设置指定PUSI的AS地址(SET HAS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定PUSI的AS地址，其中AS地址必须是SIP格式。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                 |
|:-------|:-------|:-------------------------------------------------------------------------------------|
| PUSI   | PUSI   | 用于指定一个需要设置AS信息的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| AS     | AS     | 用于指定PUSI的AS地址。当参数AS不存在时，表示将PUSI的AS地址删除。 取值范围： 长度不超过127的字符串 缺省值： 无                    |

## 使用实例

设置指定PUSI的AS地址。PUSI：sip:pusiinfo@huawei.com，AS：sip:asinfo@huawei.com。

```
SET HAS: PUSI="sip:pusiinfo@huawei.com", AS="sip:asinfo@huawei.com";
```