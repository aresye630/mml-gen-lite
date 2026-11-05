# 增加S-CSCF名称(ADD HCAPSCSCF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中增加一个指派S-CSCF到指定IMS用户或PSI用户的能力集中。当IMPU发起注册请求时，I-CSCF能够根据能力集中的指派S-CSCF名称选择S-CSCF。

## 注意事项

- SUBID参数和PISI参数必须存在且仅能存在一个。
- 该命令最多支持增加5个S-CSCF到指定IMS用户或PSI用户的能力集中。

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                           |
|:-------|:---------|:-----------------------------------------------------------------------------------------------|
| SUBID  | SUBID    | 用于指定一个添加S-CSCF名称的SUBID。一般通过ADD HSUB在数据库中添加。SUBID字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无             |
| PISI   | PISI     | 用于指定一个添加S-CSCF名称的PISI，一般通过ADD HPSI在数据库中添加。要求输入的PISI值符合NAI格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| SCSCF  | S-CSCF名称 | 用于定义新增的S-CSCF名字，必须为SIP格式。 取值范围： 长度不超过127的字符串 缺省值： 无                                            |

## 使用实例

增加S-CSCF名称。SUBID：subinfo，S-CSCF名称：sip:scscf@huawei.com。

```
ADD HCAPSCSCF: SUBID="subinfo", SCSCF="sip:scscf@huawei.com";
```