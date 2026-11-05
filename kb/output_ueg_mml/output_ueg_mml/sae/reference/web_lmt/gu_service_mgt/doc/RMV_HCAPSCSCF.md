# 删除S-CSCF名称(RMV HCAPSCSCF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于从HSS的业务数据库中的指定Subscription或PSI用户能力集中删除一个指派S-CSCF。

## 注意事项

SUBID参数和PISI参数必须存在且仅能存在一个。

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                        |
|:-------|:---------|:----------------------------------------------------------------------------|
| SUBID  | SUBID    | 用于指定一个需要删除S-CSCF名称的Subscription ID，SUBID字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无  |
| PISI   | PISI     | 用于指定一个需要删除S-CSCF名称的PISI，要求输入的PISI值符合NAI格式，字母区分大小写 取值范围： 长度不超过127的字符串 缺省值： 无 |
| SCSCF  | S-CSCF名称 | 用于指定需要删除的S-CSCF名称。必须为SIP格式。 取值范围： 长度不超过127的字符串 缺省值： 无                       |

## 使用实例

删除S-CSCF名称。SUBID：subinfo，S-CSCF名称：sip:scscf@huawei.com。

```
RMV HCAPSCSCF: SUBID="subinfo", SCSCF="sip:scscf@huawei.com";
```