# 设置内部资源QOS映射关系。（SET RESCTRLQOSMAP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置内部资源QOS映射关系。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为64。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | QOSMAPTYPE   |   DSCPVALUE | PRIORITY   |
|:-------|:-------------|------------:|:-----------|
| 初始值    | DSCP_VALUE   |           0 | NORMAL     |
| 初始值    | DSCP_VALUE   |           1 | NORMAL     |
| 初始值    | DSCP_VALUE   |           2 | NORMAL     |
| 初始值    | DSCP_VALUE   |           3 | NORMAL     |
| 初始值    | DSCP_VALUE   |           4 | NORMAL     |
| 初始值    | DSCP_VALUE   |           5 | NORMAL     |
| 初始值    | DSCP_VALUE   |           6 | NORMAL     |
| 初始值    | DSCP_VALUE   |           7 | NORMAL     |
| 初始值    | DSCP_VALUE   |           8 | NORMAL     |
| 初始值    | DSCP_VALUE   |           9 | NORMAL     |
| 初始值    | DSCP_VALUE   |          10 | NORMAL     |
| 初始值    | DSCP_VALUE   |          11 | NORMAL     |
| 初始值    | DSCP_VALUE   |          12 | NORMAL     |
| 初始值    | DSCP_VALUE   |          13 | NORMAL     |
| 初始值    | DSCP_VALUE   |          14 | NORMAL     |
| 初始值    | DSCP_VALUE   |          15 | NORMAL     |
| 初始值    | DSCP_VALUE   |          16 | NORMAL     |
| 初始值    | DSCP_VALUE   |          17 | NORMAL     |
| 初始值    | DSCP_VALUE   |          18 | NORMAL     |
| 初始值    | DSCP_VALUE   |          19 | NORMAL     |
| 初始值    | DSCP_VALUE   |          20 | NORMAL     |
| 初始值    | DSCP_VALUE   |          21 | NORMAL     |
| 初始值    | DSCP_VALUE   |          22 | NORMAL     |
| 初始值    | DSCP_VALUE   |          23 | NORMAL     |
| 初始值    | DSCP_VALUE   |          24 | NORMAL     |
| 初始值    | DSCP_VALUE   |          25 | NORMAL     |
| 初始值    | DSCP_VALUE   |          26 | NORMAL     |
| 初始值    | DSCP_VALUE   |          27 | NORMAL     |
| 初始值    | DSCP_VALUE   |          28 | NORMAL     |
| 初始值    | DSCP_VALUE   |          29 | NORMAL     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称    | 参数说明                                                                                                           |
|:-----------|:--------|:---------------------------------------------------------------------------------------------------------------|
| QOSMAPTYPE | QoS映射类型 | 可选必选说明：必选参数 参数含义：该参数用于指定QOS映射类型。 数据来源：本端规划 取值范围： DSCP_VALUE：DSCP值。 默认值：无 配置原则：无                                |
| DSCPVALUE  | DSCP值   | 可选必选说明：条件必选参数 前提条件：该参数在“QOSMAPTYPE”配置为“DSCP_VALUE”时为必选参数。 参数含义：该参数用于指定DSCP值。 数据来源：全网规划 取值范围：0-63。 默认值：无 配置原则：无 |
| PRIORITY   | 优先级     | 可选必选说明：可选参数 参数含义：该参数用于设置映射的优先级。 数据来源：本端规划 取值范围： NORMAL：普通优先级。HIGH：高优先级。 默认值：无 配置原则：无                           |

#### 使用实例

当前网络上大量异常IP分片报文，导致系统进行重组时资源过载，为了优先保障高优先级业务（比如语音、信令等），开启资源隔离功能，预留部分资源，当资源过载时，DSCP优先级高的IP分片报文使用预留资源，低优先级的IP分片报文被丢弃：

```
SET RESCTRLQOSMAP: QOSMAPTYPE=DSCP_VALUE, DSCPVALUE=46, PRIORITY=HIGH;
SET RESCTRLPARA: RESTYPE=OUTER_IPFRAG_REASS, RESISOBYDSCP=ENABLE, HRSVRATIO=10;
```