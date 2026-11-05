# 通过AS地址删除指定IMPU的一组IFC(RMV HASIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于从HSS的业务数据库中删除指定IMPU所包含相同AS地址的一组iFC。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                |
|:-------|:-------|:------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要删除iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| SERVER | AS地址   | 用于指定一个被删除iFC的AS地址，AS地址只能为SIP URI格式。 取值范围： 长度不超过127的字符串 缺省值： 无                       |

## 使用实例

删除ASIFC。IMPU：sip:impuinfo@huawei.com，AS地址：sip:as@huawei.com。

```
RMV HASIFC: IMPU="sip:impuinfo@huawei.com", SERVER="sip:as@huawei.com";
```