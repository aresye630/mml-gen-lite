# 设置集中点部署模式(SET CONCENPOINT)

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

**须知** 

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Gx、Gy、S6b接口。

此命令用于设置信令集中点的部署模式。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCALIP\_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
- LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
- 如果Gx/Gy/S6b集中点模式在LOCALIP\_PEER和LOCALPORT之间切换，需要使用命令RMV CPSCTPASSOC删除原模式下的SCTP耦联测量对象并重新配置。
- 如果需要系统提供足够多的Ga链路，可配置GACONCENMODE参数为MULTI\_PORT，并根据GAPORTPERPROC参数调整Ga链路数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | GACONCENMODE   | GXCONCENMODE   | GYCONCENMODE   | S6BCONCENMODE   |   GAPORTPERPROC |
|:-------|:---------------|:---------------|:---------------|:----------------|----------------:|
| 初始值    | SINGLE_CONNECT | LOCALIP_PEER   | LOCALIP_PEER   | LOCALIP_PEER    |               1 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                               |
|:--------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GACONCENMODE  | Ga集中点模式  | 可选必选说明：可选参数 参数含义：该参数用于指定Ga集中点的部署模式。 数据来源：本端规划 取值范围：枚举类型。 MULTI_PORT：表示使用group级接口，和对端建立多条连接，多条连接使用组级IP作为源IP，源端口号不同。SINGLE_CONNECT：表示使用group级接口，一个对端应用服务器和一个逻辑端口只有一条链路。 默认值：无 配置原则：无 |
| GXCONCENMODE  | Gx集中点模式  | 可选必选说明：可选参数 参数含义：该参数用于指定Gx应用的集中点部署模式。 数据来源：本端规划 取值范围：枚举类型。 LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。LOCALPORT：按照本端端口绑定Diameter集中点。 默认值：无 配置原则：无                                  |
| GYCONCENMODE  | Gy集中点模式  | 可选必选说明：可选参数 参数含义：该参数用于指定Gy集中点的部署模式。 数据来源：本端规划 取值范围：枚举类型。 LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。LOCALPORT：按照本端端口绑定Diameter集中点。 默认值：无 配置原则：无                                    |
| S6BCONCENMODE | S6b集中点模式 | 可选必选说明：可选参数 参数含义：该参数用于指定S6b集中点的部署模式。 数据来源：本端规划 取值范围：枚举类型。 LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。LOCALPORT：按照本端端口绑定Diameter集中点。 默认值：无 配置原则：无                                   |
| GAPORTPERPROC | Ga每进程端口数 | 可选必选说明：条件可选参数 前提条件：该参数在“GACONCENMODE”配置为“MULTI_PORT”时为可选参数。 参数含义：该参数用于指定Ga集中点模式为MULTI_PORT时为每个Ga进程提供的端口数。 数据来源：本端规划 取值范围：整数类型，取值范围为1~5。 默认值：无 配置原则：无                               |

#### 使用实例

根据网络规划，需要修改Ga集中点的部署模式为SINGLE\_CONNECT，则可以按如下配置：

```
SET CONCENPOINT: GACONCENMODE=SINGLE_CONNECT;
```