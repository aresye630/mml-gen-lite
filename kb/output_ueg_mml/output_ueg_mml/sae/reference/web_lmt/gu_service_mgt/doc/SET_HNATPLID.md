# 设置IMPU的游牧模板(SET HNATPLID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置指定IMPU的游牧权限模板。

## 注意事项

“游牧模板ID”参数和“NASS游牧模板名称”参数必须存在且仅能存在一个。

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                 |
|:--------|:-----------|:-------------------------------------------------------------------------------------|
| IMPU    | IMPU       | 用于指定一个需要设置游牧模板的IMPU。要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| NATPLID | 游牧模板ID     | 用于定义一个游牧模板ID，参数NATPLID取值为255时，表示删除该IMPU的原有游牧权限。 取值范围： 0~67108863 缺省值： 无              |
| TPLNAME | NASS游牧模板名称 | 用于定义一个游牧模板名称。 取值范围：长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 缺省值：无                        |

## 使用实例

1. 设置IMPU的游牧模板。IMPU：sip:impuinfo@huawei.com，游牧模板ID：10。

   ```
   SET HNATPLID: IMPU="sip:impuinfo@huawei.com", NATPLID=10;
   ```
2. 设置IMPU的游牧模板。IMPU：sip:impuinfo@huawei.com，NASS游牧模板名称：“07550011”。

   ```
   SET HNATPLID: IMPU="sip:impuinfo@huawei.com", TPLNAME="07550011";
   ```
3. 删除IMPU的游牧模板。IMPU：sip:impuinfo@huawei.com，游牧模板ID：255。

   ```
   SET HNATPLID: IMPU="sip:impuinfo@huawei.com",  NATPLID=255;
   ```