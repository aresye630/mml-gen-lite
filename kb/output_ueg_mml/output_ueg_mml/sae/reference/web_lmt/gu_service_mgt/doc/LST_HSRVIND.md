# 查询ServiceIndication对应的透明数据(LST HSRVIND)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定IMPU或PUSI关联的透明数据的Service Indication。

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。
- 当IMPU存在时，如果参数REPTYPE存在，表示查指定类型透明数据的Service Indication。
- 当IMPU存在时，如果参数REPTYPE不存在，表示查所有类型透明数据的Service Indication，参数PUSI存在时，REPTYPE不能存在。

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                                                                                                                                |
|:--------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU    | IMPU    | 用于指示系统需要查询哪个IMPU对应的透明数据对应的Service Indication。要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。                                               |
| PUSI    | PUSI    | 用于指示系统需要查询哪个PUSI对应的透明数据对应的Service Indication。要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。                                               |
| REPTYPE | 透明数据的类型 | 用于指定一个需要查询透明数据的Service Indication的透明数据类型。 取值范围：ALIASREPDATA(Aliasrepository data)：表示查询该透明数据的类型为别名透明数据。REPDATA(Repository data)：表示查询该透明数据的类型为普通透明数据。 默认值：无。 说明：可选参数。 |

## 使用实例

查询Service Indication对应的透明数据，“IMPU”为“sip:impuinfo@huawei.com”：

```
LST HSRVIND: IMPU="sip:impuinfo@huawei.com";
```

```
%%LST HSRVIND: IMPU="sip:impuinfo@huawei.com";%%
RETCODE = 0 操作成功

SRVIND        REPTYPE
3               1

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 参数标识    | 参数说明                                              |
|:--------|:--------------------------------------------------|
| SRVIND  | 显示透明数据的Service Indication。                        |
| REPTYPE | 显示透明数据的类型。 “0”：指透明数据类型为别名透明数据。“1”：指透明数据类型为普通透明数据。 |