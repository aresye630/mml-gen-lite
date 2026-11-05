# 删除IMPI的SIP Digest鉴权信息(RMV HSDAINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于从HSS的业务数据库中删除一条SIP Digest鉴权的“IMPI”的数据记录，或删除一条“IMPI”的SIP Digest信息的数据记录。

## 注意事项

- 如果指定“IMPI”仅支持SIP Digest鉴权并且“IMPI”未被使用，此操作用于删除“IMPI”。
- 如果指定“IMPI”支持SIP Digest鉴权外还支持其它鉴权，此操作仅删除“IMPI”下的SIP Digest鉴权信息。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                               |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------|
| IMPI   | IMPI   | 标识一个IMPI的SIP Digest鉴权信息的关键字段，用于指定需要删除哪一个IMPI的SIP Digest鉴权信息，操作员可以使用命令LST HAUTHINF查询该IMPI对应的鉴权方式。 取值范围：长度不超过127的字符串 默认值：无。 说明：必选参数。 |

## 使用实例

删除IMPI的SIP Digest鉴权信息，“IMPI”为“impiinfo”：

```
RMV HSDAINF: IMPI="impiinfo";
```