# 删除所有iFC(RMV HALLIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于从HSS的业务数据库中删除指定IMPU相关的Service Profile所包含的所有iFC信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                |
|:-------|:-------|:------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要删除iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

删除指定IMPU的所有iFC。IMPU：sip:impuinfo@huawei.com。

```
RMV HALLIFC: IMPU="sip:impuinfo@huawei.com";
```