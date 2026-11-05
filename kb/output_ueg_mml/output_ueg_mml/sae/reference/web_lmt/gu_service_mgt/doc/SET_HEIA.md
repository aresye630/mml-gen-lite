# 设置Early IMS鉴权模式(SET HEIA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置或取消指定IMPI的Early IMS鉴权模式。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                                                              |
|:--------|:--------|:--------------------------------------------------------------------------------------------------|
| IMPI    | IMPI    | 用于定义一个IMPI，此IMPI必须已经和IMSI建立了关联关系，该参数的配置原则是要求输入IMPI值符合NAI格式。 取值范围： 长度不超过127的字符串 缺省值： 无             |
| EIAFLAG | EIA鉴权标识 | 用于定义IMPI的Early IMS鉴权标识，其值域类型为布尔值。 TRUE:支持EIA鉴权。FALSE:不支持EIA鉴权。 取值范围：FALSE(False)TRUE(True) 缺省值： 无 |

## 使用实例

设置Early IMS鉴权模式。IMPI：impiinfo，EIA鉴权标识：TRUE。

```
SET HEIA: IMPI="impiinfo", EIAFLAG=TRUE;
```