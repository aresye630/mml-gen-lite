# 设置IMPU的游牧控制标志(SET HNNCFLAG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定IMPU的游牧控制功能标志。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                                                     |
|:--------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| IMPU    | IMPU     | 用于指定一个需要设置游牧控制功能标识的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                 |
| NNCFLAG | 游牧功能控制标志 | NNCFLAG取值为ACTIVE表示设置游牧控制功能标志，NNCFLAG取值为DEACTIVE表示取消游牧控制功能标志。 取值范围： DEACTIVE(Deactive)：取消游牧控制功能标志 ACTIVE(Active)：设置游牧控制功能标志 缺省值： DEACTIVE |

## 使用实例

设置IMPU的游牧控制标志。IMPU：sip:impuinfo@huawei.com，游牧功能控制标志：ACTIVE。

```
SET HNNCFLAG: IMPU="sip:impuinfo@huawei.com", NNCFLAG=ACTIVE;
```