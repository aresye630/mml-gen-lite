# 删除指定IMPU的ONEKEY数据(RMV HONEKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中删除指定IMPU的One Key数据。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                    |
|:-------|:-------|:----------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要删除One Key的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

删除One Key数据。IMPU：sip:impuinfo@huawei.com。

```
RMV HONEKEY: IMPU="sip:impuinfo@huawei.com";
```