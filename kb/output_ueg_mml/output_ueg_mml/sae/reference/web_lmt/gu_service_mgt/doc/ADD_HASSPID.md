# 增加IMPU或PUSI对应的AS-ServiceProfileId(ADD HASSPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中增加一个IMPU或PUSI关联的AS-ServiceProfileId的数据记录。

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。
- 一个IMPU或PUSI最多关联32个AS-ServiceProfileId。

## 参数说明

| 参数标识   | 参数名称                | 参数说明                                                                                                                            |
|:-------|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| IMPU   | IMPU                | 用于指定一个需要增加AS-ServiceProfileId的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                             |
| PUSI   | PUSI                | 用于指定一个需要增加AS-ServiceProfileId的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                             |
| ASSPID | AS-ServiceprofileId | 用于定义一个AS-ServiceProfileId，IMPU或PUSI在AS上签约了那些服务，用AS-ServiceProfileId来表示，其值域类型为数字，不能和已有的AS-ServiceProfileId重复。 取值范围： 0~255 缺省值： 无 |

## 使用实例

增加IMPU对应的AS-ServiceProfileId。IMPU：sip:impuinfo@huawei.com，AS-ServiceprofileId：1。

```
ADD HASSPID: IMPU="sip:impuinfo@huawei.com", ASSPID=1;
```