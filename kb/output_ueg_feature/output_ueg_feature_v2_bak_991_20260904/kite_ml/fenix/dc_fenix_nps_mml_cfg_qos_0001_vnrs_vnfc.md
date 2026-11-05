# 激活QoS简单流分类特性（VNRS\_VNFC）

- 操作场景
- 对系统的影响
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络配置基于简单流分类的Qos策略的操作过程。

在Ethernet接口、Ethernet子接口或Eth-Trunk接口上配置基于简单流分类的QoS策略，比如说IP报文、VLAN报文的优先级。可以先在该接口上配置DiffServ域， 然后对该DS域配置各种优先级的映射关系，接口上的报文会按照DiffServ域中的映射关系进行简单流分类映射。

简单流分类通常配置在网络的核心位置。

当需要对来自上游设备的VLAN报文进行QoS调度的时候，可以通过本命令配置DiffServ域中VLAN报文的802.1p优先级到路由器内部服务等级之间的映射，并为报文着色。对于IP报文，则是将DSCP值映射成内部服务等级，并着色。将DiffServ域绑定到报文的入接口后，QoS将根据报文映射的路由器内部服务等级和颜色进行拥塞管理和拥塞避免。

对于下行报文则将路由器内部的服务等级和颜色映射成对应的DSCP值或者802.1p值。

**说明** 

NP卡场景下，不支持接口重定向到指定VPN功能。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

已经创建对应DiffServ域。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如表1所示。

| 类别                       | 参数                       | 取值样例            | 获取方法   | 相关命令              |
|:-------------------------|:-------------------------|:----------------|:-------|:------------------|
| QOSIFTRUST接口绑定DS域        | DS域名(DSNAME)             | ds1             | 本端规划   | ADD QOSIFTRUST    |
| QOSIFTRUST接口绑定DS域        | 接口名称（IFNAME）             | Ethernet 64/0/3 | 本端规划   | ADD QOSIFTRUST    |
| QOSIFTRUST接口绑定DS域        | 8021p标志(FLAG8021P)       | 否               | 本端规划   | ADD QOSIFTRUST    |
| QOSDIFFERSERV配置DiffServ域 | DS域名(DSNAME)             | ds1             | 本端规划   | ADD QOSDIFFERSERV |
| QOSBA报文映射                | DS域名(DSNAME)             | ds1             | 本端规划   | SET QOSBA         |
| QOSBA报文映射                | ba类型(BATYPE)             | ip_dscp         | 本端规划   | SET QOSBA         |
| QOSBA报文映射                | ba值(BAVALUE)             | 1               | 本端规划   | SET QOSBA         |
| QOSBA报文映射                | 服务分类(SERVICECLASS)       | be              | 本端规划   | SET QOSBA         |
| QOSBA报文映射                | 颜色分类(COLOR)              | green           | 本端规划   | SET QOSBA         |
| 设置QoS PHB                | DS域名(DSNAME)             | ds1             | 本端规划   | SET QOSPHB        |
| 设置QoS PHB                | PHB类型(PHBTYPE)           | 8021p           | 本端规划   | SET QOSPHB        |
| 设置QoS PHB                | PHB值(PHBVALUE)           | 1               | 本端规划   | SET QOSPHB        |
| 设置QoS PHB                | 服务分类(SERVICECLASS)       | be              | 本端规划   | SET QOSPHB        |
| 设置QoS PHB                | 颜色分类(COLOR)              | green           | 本端规划   | SET QOSPHB        |
| 添加禁止QoS优先级映射的类型          | 接口名称（IFNAME）             | Ethernet64/0/3  | 本端规划   | ADD QOSIFPHB      |
| 添加禁止QoS优先级映射的类型          | 出接口报文的优先级字段映射类型(PHBTYPE) | dscp            | 本端规划   | ADD QOSIFPHB      |
| QOSRDRVPN重定向VPN          | 接口名称（IFNAME）             | Ethernet 64/0/3 | 本端规划   | ADD QOSRDRVPN     |
| QOSRDRVPN重定向VPN          | VPN名称(VRFNAME)           | vpn1            | 本端规划   | ADD QOSRDRVPN     |

## 操作流程

激活QoS简单流分类特性操作流程如图1所示。

**图1** 激活QoS简单流分类特性操作流程

## 操作步骤

1. 当不使用默认存在两个DiffServ域（default和5p3d）时，配置DiffServ域。

   在“MML命令行-UEG”窗口上执行：

   **ADD QOSDIFFERSERV**: DSNAME="DS名称";
2. 当需要修改上行或者下行的映射关系时，通过**SET QOSBA**修改“服务分类”、“颜色分类”，通过**SET QOSPHB**修改“PHB值”，其中5p3d域不允许修改。

   在“MML命令行-UEG”窗口上执行：

   **SET QOSBA**: DSNAME="DS域名",BATYPE=ba类型,BAVALUE=ba值,SERVICECLASS=服务分类,COLOR=颜色分类;

   **SET QOSPHB**: DSNAME="DS域名",PHBTYPE=PHB类型,PHBVALUE=PHB值,SERVICECLASS=服务分类,COLOR=颜色分类;
3. 配置接口绑定相应的DiffServ域。

   在“MML命令行-UEG”窗口上执行：

   **ADD QOSIFTRUST**: DSNAME="ds域", IFNAME="接口名称";

   **说明** 

   只有Ethernet子接口和GE子接口支持802.1p映射。
4. 当需要将流量指定到VPN时，配置接口重定向到指定VPN。

   在“MML命令行-UEG”窗口上执行：

   **ADD QOSRDRVPN**: IFNAME="接口名称", VRFNAME ="VPN名称";

   **说明** 

   必须先创建相应的VPN实例，只支持在以太主接口和GE主接口进行配置。
5. 当只需要检查BA表时，激活QoS不检查PHB表。

   在“MML命令行-UEG”窗口上执行：

   **ADD QOSIFPHB**: IFNAME="接口名称", PHBTYPE=出接口报文的优先级字段映射类型;

## 任务示例

任务描述

VNF1与路由器接口Ethernet64/0/2在同一个网段，VNF2与路由器接口Ethernet64/0/3在同一个网段，在接口Ethernet64/0/2绑定DiffServ域default，在接口Ethernet64/0/3绑定DiffServ域5p3d。在VNF1上ping VNF2，并设置dscp值，在VNF2上查看收到的ping报文的dscp值，在经过入接口Ethernet64/0/2，从dscp到路由内部服务等级及报文着色映射，在经过出接口Ethernet64/0/3，从路由内部服务等级及报文颜色到外部dscp值的映射，最终dscp映射值是否与预期的一致。在简单流分类的下行，由于报文的服务等级、颜色等信息被存放在PHB表中，当报文转发时，检查PHB表，识别报文的业务优先级，进而根据DS域中的映射关系将路由器内部业务优先级映射成外部业务优先级。报文在接口64/0/3下行转发时不会检查PHB表。

**图2** QoS简单流分类配置示意图

脚本

//对以太接口Ethernet64/0/2绑定DiffServ域default。

```
ADD QOSIFTRUST: DSNAME="default", IFNAME="Ethernet64/0/2";
```

//对以太接口Ethernet64/0/3绑定DiffServ域5p3d。

```
ADD QOSIFTRUST: DSNAME="5p3d", IFNAME="Ethernet64/0/3";
```

//在VNF1 ping的时候设置报文dscp值为0，最终在VNF2上得到的报文dscp值将是0。

```
Default domain:ip-dscp-inbound 0 phb be green
5p3d domain:ip-dscp-outbound be green map 0
```

//对以太接口Ethernet64/0/3去激活QoS不检查PHB表。

```
ADD QOSIFPHB: IFNAME="Ethernet64/0/3",PHBTYPE=dscp;
```