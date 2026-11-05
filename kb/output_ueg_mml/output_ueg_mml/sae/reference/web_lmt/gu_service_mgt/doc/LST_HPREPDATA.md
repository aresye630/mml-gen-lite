# 查询扩展业务数据(LST HPREPDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定IMPU的扩展业务数据。

## 注意事项

当查询指定IMPU的扩展业务数据时，如果返回报文“解密失败”，表示该数据属于透明数据，需要使用**LST HREPDATA**命令进行查询。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                             |
|:-------|:-------|:---------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于查询IMPU的扩展业务数据，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

查询IMPU的扩展业务数据。IMPU：sip:impuinfo@huawei.com。

```
LST HPREPDATA: IMPU="sip:impuinfo@huawei.com";
```

## 输出结果说明

| 参数标识                | 参数说明                                             |
|:--------------------|:-------------------------------------------------|
| IMSI                | 显示扩展业务数据中的IMSI。                                  |
| SELFSERVICE         | 显示扩展业务数据中的自助业务标识。                                |
| SMSCADDRESS         | 显示扩展业务数据中的短消息中心地址。                               |
| LOCATIONINFORMATION | 显示扩展业务数据中的VoBB用户的位置信息。                           |
| NPINDICATOR         | 显示扩展业务数据中的Numbering Plan Identity编码方案标识。         |
| CICINDICATOR        | 显示扩展业务数据中的Carrier Identification Code进行平等接入业务标识。 |
| BINDINDICATOR       | 显示扩展业务数据中的CS绑定标识。                                |