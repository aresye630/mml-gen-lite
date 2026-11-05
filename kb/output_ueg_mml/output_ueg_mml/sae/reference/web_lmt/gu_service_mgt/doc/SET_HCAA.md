# 设置CAVEAKA鉴权能力(SET HCAA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中增加、修改或删除指定IMPI的CAVEAKA鉴权能力。

## 注意事项

- 当CAVEAKAFLG参数为TRUE时，UIMID参数必须存在。
- 当CAVEAKAFLG参数为FALSE时，UIMID参数可以不存在，此时如果该参数存在，将被忽略。
- 如果用户不支持CAVEAKA鉴权，使用SET HCAA命令，参数CAVEAKAFLG为TRUE且UIMID参数存在，则属于增加CAVEAKA鉴权信息。
- 如果用户已经支持CAVEAKA鉴权，使用SET HCAA命令，参数CAVEAKAFLG为TRUE且UIMID参数存在，则属于修改CAVEAKA鉴权信息
- 如果SET HCAA时指定关闭该用户的CAVEAKA鉴权，则表示是删除该用户的CAVEAKA鉴权信息。

## 参数说明

| 参数标识       | 参数名称        | 参数说明                                                                                                                               |
|:-----------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| IMPI       | IMPI        | 用于定义一个IMPI，此IMPI必须已经和IMSI建立了关联关系，且该IMPI的@符号前面的内容要与关联的IMSI相同，该参数的配置原则是要求输入的IMPI值符合username@realm形式的NAI格式。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| CAVEAKAFLG | CAVEAKA鉴权标识 | 用于定义IMPI的Cave AKA鉴权标识，其值域类型为布尔值。TRUE:支持Cave AKA鉴权。FALSE:不支持Cave AKA鉴权。 取值范围： FALSE(False)TRUE(True) 缺省值： 无                         |
| UIMID      | UIMID       | UIM卡的ID号码，是CDMA UIMID的最后4个字节，要求输入16进制字符，字母不区分大小写。 取值范围： 长度等于8的16进制字符串。 缺省值： 无                                                      |

## 使用实例

设置Cave AKA鉴权能力。IMPI：460001234567890@huawei.com，CAVEAKA鉴权标识：TRUE，UIMID：12345678。

```
SET HCAA: IMPI="460001234567890@huawei.com", CAVEAKAFLG=TRUE, UIMID="12345678";
```