# 删除IMEISV号段（RMV IMEISVSEG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于删除IMEISVSEG号段。

支持批量删除。

#### 注意事项

- 该命令执行后立即生效。
- 如果引用了该IMEISVSEG的UPBindUPG的记录存在，则不允许删除IMEISVSEG记录。通过LST UPBINDUPG查询绑定关系记录。
- 如果引用了该IMEISVSEG的SUBSCRIBERIDSEGGRP的记录存在，则不允许删除IMEISVSEG记录。通过LST SUBSCRIBERIDSEGGRP查询绑定关系记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                    |
|:------------|:-----------|:------------------------------------------------------------------------------------------------------------------------|
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：可选参数 参数含义：该参数用于指定IMEISV号段名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：若未指定该参数，则删除所有IMEISVSEG号段。 |

#### 使用实例

删除IMEISV号段：SEGMENTNAME为TestSegmentName：

```
RMV IMEISVSEG:SEGMENTNAME="TestSegmentName";
```