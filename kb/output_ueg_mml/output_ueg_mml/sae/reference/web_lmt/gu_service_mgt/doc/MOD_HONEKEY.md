# 修改指定IMPU的ONEKEY数据(MOD HONEKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中修改指定IMPU的One Key数据。

## 注意事项

Web用户名，Http Token信息，接入点信息三个参数必须存在一个。

## 参数说明

| 参数标识      | 参数名称         | 参数说明                                                                                  |
|:----------|:-------------|:--------------------------------------------------------------------------------------|
| IMPU      | IMPU         | 用于指定需要修改One Key的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| WUSERNAME | Web 用户名      | 用于指定需要修改的web username信息。 取值范围： 长度不超过127的字符串 缺省值： 无                                    |
| HTOKEN    | Http Token信息 | 用于指定需要修改的Http Token信息。 取值范围： 长度不超过15的字符串 缺省值： 无                                       |
| AP        | 接入点信息        | 用于指定需要修改的接入点信息。 取值范围： 长度不超过255的字符串 缺省值： 无                                             |

## 使用实例

修改One Key数据。IMPU：sip:impuinfo@huawei.com，Web用户名：WUSERNAME，Http Token信息：HTOKEN，接入点信息：AP。

```
MOD HONEKEY: IMPU="sip:impuinfo@huawei.com", WUSERNAME="WUSERNAME", HTOKEN="HTOKEN", AP="AP";
```