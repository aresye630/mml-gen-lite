# 增加指定IMPU的ONEKEY数据(ADD HONEKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中为指定IMPU添加一组新的One Key数据。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称         | 参数说明                                                                                    |
|:----------|:-------------|:----------------------------------------------------------------------------------------|
| IMPU      | IMPU         | 用于指定一个需要增加One Key的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| WUSERNAME | Web 用户名      | 用于指定新增加的web username信息 取值范围： 长度不超过127的字符串 缺省值： 无                                        |
| HTOKEN    | Http Token信息 | 用于指定新增加的Http Token信息 取值范围： 长度不超过15的字符串 缺省值： 无                                           |
| AP        | 接入点信息        | 用于指定新增加的接入点信息 取值范围： 长度不超过255的字符串 缺省值： 无                                                 |

## 使用实例

增加One Key数据。IMPU：sip:impuinfo@huawei.com，Web用户名：WUSERNAME，Http token信息：HTOKEN，接入点信息：AP。

```
ADD HONEKEY: IMPU="sip:impuinfo@huawei.com", WUSERNAME="WUSERNAME", HTOKEN="HTOKEN", AP="AP";
```