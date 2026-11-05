# 增加IMPI的NASS Bundled鉴权信息(ADD HNBAINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中增加支持NASS Bundled鉴权的IMPI的数据记录，或为已经存在的IMPI添加NASS Bundled鉴权信息。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称      | 参数说明                                                                                   |
|:----------|:----------|:---------------------------------------------------------------------------------------|
| IMPI      | IMPI      | 用于定义一个IMPI，该参数的配置原则是要求输入的IMPI必须唯一。要求输入的IMPI值符合NAI格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| LINEIDIDX | Line ID索引 | 用于定义一个Line ID索引。 取值范围： 1～5 缺省值： 无                                                      |
| LINEID    | Line ID   | 用于定义一个Line ID。 取值范围： 长度不超过127的字符串 缺省值： 无                                               |

## 使用实例

增加IMPI的NASS Bundled鉴权信息。IMPI:impiinfo，Line ID索引：1，Line ID：huawei。

```
ADD HNBAINF: IMPI="impiinfo", LINEIDIDX=1, LINEID="huawei";
```