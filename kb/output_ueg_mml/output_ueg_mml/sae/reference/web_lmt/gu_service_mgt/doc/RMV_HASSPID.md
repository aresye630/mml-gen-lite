# 删除IMPU或PUSI对应的AS-ServiceProfileId(RMV HASSPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中删除IMPU或PUSI关联的AS-ServiceProfileId的数据记录。

## 注意事项

- ASSPID参数不存在表示删除IMPU或PUSI下所有的ASSPID。
- 参数IMPU和参数PUSI必须存在且只能存在一个。

## 参数说明

| 参数标识   | 参数名称                  | 参数说明                                                                                                                                             |
|:-------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU   | IMPU                  | 标识一条IMPU的AS-ServiceProfileId数据记录的关键参数之一，用于指定需要删除哪一条IMPU的AS-ServiceProfileId数据记录，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| PUSI   | PUSI                  | 标识一条PUSI的AS-ServiceProfileId数据记录的关键参数之一，用于指定需要删除哪一条PUSI的AS-ServiceProfileId数据记录，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| ASSPID | AS service profile ID | 标识一条IMPU或PUSI的AS-ServiceProfileId数据记录的关键参数之一，用于指定需要删除哪一条AS-ServiceProfileId数据记录。 取值范围：0～255 缺省值： 无                                               |

## 使用实例

删除IMPU或PUSI对应的AS-ServiceProfileId。IMPU：sip:impuinfo@huawei.com，AS-ServiceprofileId：10。

```
RMV HASSPID: IMPU="sip:impuinfo@huawei.com", ASSPID=10;
```