# 注销用户(DRG HUSER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于业务发放系统主动发起注销通知。该操作可以注销一个或者一组用户。

使用该命令后，HSS发送RTR消息至S-CSCF注销用户，RTR消息的Deregistration-Reason的reason-code值为server-change。

## 注意事项

- 参数“S-CSCF主机名”、“S-CSCF域名”都不输入时，IMPI和IMPU参数必须至少存在一个。
- 参数“S-CSCF主机名”、“S-CSCF域名”同时输入时，IMPI及IMPU必须同时输入。

## 参数说明

| 参数标识       | 参数名称      | 参数说明                                                                                                              |
|:-----------|:----------|:------------------------------------------------------------------------------------------------------------------|
| IMPI       | IMPI      | 用于指定一个被注销的IMPI，要求输入的IMPI值符合NAI格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                               |
| IMPU       | IMPU      | 用于指定一个被注销的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                   |
| SCSCFHOST  | S-CSCF主机名 | 用于指定一个被注销的S-CSCF主机名，要求输入S-CSCF主机名的值符合SIP格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 说明：可选参数，S-CSCF主机名和S-CSCF域名参数必须同时输入。 |
| SCSCFREALM | S-CSCF域名  | 用于指定一个被注销的S-CSCF域名，要求输入S-CSCF域名的值符合SIP格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 说明：可选参数，S-CSCF主机名和S-CSCF域名参数必须同时输入。   |

## 使用实例

注销用户。IMPI：impiinfo，IMPU：sip:impuinfo@huawei.com。

```
DRG HUSER: IMPI="impiinfo", IMPU="sip:impuinfo@huawei.com";
```