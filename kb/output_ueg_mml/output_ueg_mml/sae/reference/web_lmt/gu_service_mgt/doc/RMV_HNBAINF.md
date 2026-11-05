# 删除IMPI的NASS Bundled鉴权信息(RMV HNBAINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于从HSS的业务数据库中删除支持NASS Bundled鉴权的IMPI，或删除IMPI的指定NASS Bundled鉴权信息。

## 注意事项

- 如果指定IMPI仅支持NBA鉴权并且IMPI未被使用，此操作用于删除IMPI。
- 如果指定IMPI支持NBA鉴权外还支持其它鉴权，此操作仅删除IMPI下的NBA鉴权信息。

## 参数说明

| 参数标识      | 参数名称      | 参数说明                                                                                                                                    |
|:----------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------|
| IMPI      | IMPI      | 标识一条IMPI的NASS Bundled鉴权信息的数据记录的关键参数之一，用于指定需要删除哪一条IMPI数据记录，操作员可以使用LST HNBAINF操作查询获得。要求输入的IMPI值符合NAI格式，字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |
| LINEIDIDX | Line ID索引 | 标识一条IMPI的NASS Bundled鉴权信息的数据记录的关键参数之一，用于指定需要删除哪一条Line ID索引数据记录，操作员可以使用LST HNBAINF操作查询获得。 取值范围：1～5 缺省值： 无                                |

## 使用实例

删除IMPI的NASS Bundled鉴权信息。IMPI：impiinfo。

```
RMV HNBAINF: IMPI="impiinfo";
```