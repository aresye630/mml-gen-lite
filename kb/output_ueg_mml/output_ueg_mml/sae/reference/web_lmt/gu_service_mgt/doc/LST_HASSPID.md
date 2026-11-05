# 查询IMPU或PUSI对应的AS-ServiceProfileId(LST HASSPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定IMPU或PUSI关联的AS-ServiceProfileId，需要输入唯一标识该数据记录的关键参数IMPU或PUSI。

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指示系统需要查询的哪个IMPU关联的AS-ServiceProfileId，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| PUSI   | PUSI   | 用于指示系统需要查询的那个PUSI关联的AS-ServiceProfileId，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

查询IMPU对应的AS-ServiceProfileId。IMPU：sip:impuinfo@huawei.com。

```
LST HASSPID: IMPU="sip:impuinfo@huawei.com";
```

## 输出结果说明

| 参数标识   | 参数说明                          |
|:-------|:------------------------------|
| ASSPID | 显示在AS上签约的AS-ServiceProfileId。 |