# 配置ACL防止UE或用户PDN/DN对运营商网络设备攻击

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

如果UE所属APN绑定的VPN与UEG的PDN/DN侧接口绑定的VPN相同，UE激活后存在攻击UEG以及与UEG的PDN/DN侧接口相连的路由器设备的可能性。另外如果VPN配置错误，恶意用户了解运营商网络设备IP地址的情况下，可能发起非法行访问或恶意攻击。组网如图1所示。

**图1** 防止UE对运营商网络设备的攻击示意图

禁止UE访问的运营商网络设备范围包括：

* UPF周边对接网元，网络数据参考水平网设文档。
* NFVI基础设施层，网络数据参考垂直网设文档。
* 日志服务器、NTP服务器等其他网络设备，网络数据需要根据运营商实际部署情况确定。

为防止恶意用户的以上攻击行为，收集以上运营商网络设备的网络数据，需要采取如下至少一种措施阻断恶意用户访问行为。

* 在外部PDN/DN网络和运营商网络设备之间部署防火墙，禁止用户访问运营商网络设备。
* 在UEG上配置包过滤策略，禁止用户访问运营商网络设备。过滤报文目的地址为：本运营商范围内与UE所属APN绑定同一VPN的接口可达的所有网段。

适用于SGW-U、PGW-U、UPF。

## 必备事项

前提条件

无。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 三四层的过滤规则 | 过滤器名字（FILTERNAME） | to-cn | 本端规划 | **ADD FILTER** |
|  | 三四层IPv4协议输入类型（L34PROTTYPE） | STRING | 本端规划 |  |
|  | 三四层协议类型（L34PROTOCOL） | UDP | 本端规划 |  |
|  | 手机IP地址配置模式（MSIPMODE） | IP | 全网规划 |  |
|  | 手机IP地址（MSIP） | 10.57.90.1 | 全网规划 |  |
|  | 手机IP地址掩码类型（MSIPMASKTYPE） | IPTYPE | 全网规划 |  |
|  | 手机IP地址反掩码（MSIPMASK） | 0.0.0.31 | 全网规划 |  |
|  | 服务器IP地址配置模式（SVRIPMODE） | IP | 全网规划 | 核心网侧服务器的IP地址及反掩码。 **ADD FILTER** |
|  | 服务器IP地址（SVRIP） | 192.168.95.67 | 全网规划 |  |
|  | 服务器IP地址掩码类型（SVRIPMASKTYPE） | IPTYPE | 全网规划 |  |
|  | 服务器IP地址反掩码（SVRIPMASK） | 0.0.0.31 | 全网规划 |  |
| ACL节点 | ACL节点名称（ACLNODENAME） | node-upflow-cn | 本端规划 | **ADD ACLNODE** |
|  | 过滤器名字（FILTERNAME） | to-cn | 已配置数据中获取 | 已通过**ADD FILTER**命令配置完成，可以使用**LST FILTER**命令进行查询。 |
|  | 动作类型（ACTIONTYPE） | GATE | 本端规划 | **ADD ACLNODE** |
|  | 门控动作（GATEACTION） | DISCARD | 本端规划 |  |
| ACL | ACL名称（ACLNAME） | acl-upflow | 本端规划 | **ADD ACL** |
|  | 匹配方式（MATCHORDER） | AUTO | 本端规划 |  |
| 绑定ACL节点 | ACL名称（ACLNAME） | acl-upflow | 已配置数据中获取 | 已通过**ADD ACL**命令配置完成，可以使用**LST ACL**命令进行查询。 |
|  | ACL节点名称（ACLNODENAME） | node-upflow-cn | 已配置数据中获取 | 已通过**ADD ACLNODE**命令配置完成，可以使用**LST ACLNODE**命令进行查询。 |
| APN  绑定ACL | APN名称（APN） | apn-test | 已配置数据中获取 | 已通过**ADD APN**命令配置完成，可以使用**LST APN**命令进行查询。 |
|  | 方向（DIRECTION） | UPIN | 本端规划 | **ADD ACLBINDAPN** |
|  | ACL名称（ACLNAME） | acl-upflow | 已配置数据中获取 | 已通过**ADD ACL**命令配置完成，可以使用**LST ACL**命令进行查询。 |

## 操作步骤

1. 在“MML命令行-UEG”窗口上配置ACL节点使用的过滤规则。
   1. 配置三四层的过滤规则。

      **ADD FILTER**: FILTERNAME=过滤器名字,L34PROTTYPE=三四层IPv4协议输入类型,L34PROTOCOL=三四层协议类型;
   2. 将新配置的filter置为生效。

      **SET REFRESHSRV**: REFRESHTYPE=USERPROFILE;
2. 在“MML命令行-UEG”窗口上配置ACL节点，并绑定到ACL。
   1. 配置ACL节点，即配置三四层过滤规则对应的动作。

      **ADD ACLNODE**: ACLNODENAME=ACL节点名称,FILTERNAME=过滤器名字,ACTIONTYPE=动作类型;
   2. 配置ACL名称、排序方式。

      **ADD ACL**: ACLNAME=ACL名称,MATCHORDER=排序方式;
   3. 配置绑定ACL节点到ACL下。

      **ADD ACLNODEBINDACL**: ACLNAME=ACL名称,ACLNODENAME=ACL节点名称;
3. 在“MML命令行-UEG”窗口上配置ACL与APN的绑定关系。
   1. 配置APN名称。

      **ADD APN**: APN=APN名称;
   2. 配置ACL绑定到APN下。

      **ADD ACLBINDAPN**: APN=APN名称,DIRECTION=方向,ACLNAME=ACL名称;
   3. 将新配置的ACL和ACL节点置为生效。

      **SET REFRESHSRV**: REFRESHTYPE=ACL;

## 任务示例

任务描述

在UEG上配置ACL，禁止UE非法访问运营商网络设备。

脚本

1. 配置ACL节点使用的三四层过滤规则，过滤规则名称为“to-cn”，三四层协议类型为UDP协议。禁止10.57.90.1/27网段的UE访问192.168.95.67/27网段的核心网设备。

   以下命令在“MML命令行-UEG”窗口上执行：

   ```
   ADD FILTER:FILTERNAME="to-cn",L34PROTTYPE=STRING,L34PROTOCOL=UDP,MSIPMODE=IP,MSIP="10.57.90.1",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.0.31",SVRIPMODE=IP,SVRIP="192.168.95.67",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.31";
   ```

   反掩码（wildcardmask）与子网掩码恰好相反，它是以0表示必须匹配的位，以1表示无需匹配的位，即先对wildcardmask取反，然后和IP address进行“与”运算，从而得出IP地址范围。例如：过滤规则“to-cn”中，由子网掩码255.255.255.224可计算出某核心网设备所在网段的网络地址为192.168.95.64。同样，反掩码也可同样计算出这个结果，如下：

   IP address= 192.168.95.67 11000000.10101000.1011111.01000011

   wildcardmask = 0.0.0.31 00000000.00000000.00000000.00011111

   网络地址 = 192.168.95.64 11000000.10101000.1011111.01000000

   ```
   SET REFRESHSRV:REFRESHTYPE=ALL;
   ```
2. 将过滤规则和流动作关联起来。配置ACL节点为“node-upflow-cn”，“to-cn”过滤规则对应的门控动作是拒绝通过。

   以下命令在“MML命令行-UEG”窗口上执行：

   ```
   ADD ACLNODE:ACLNODENAME="node-upflow-cn",FILTERNAME="to-cn",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACL:ACLNAME="acl-upflow",MATCHORDER=AUTO;
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-upflow",ACLNODENAME="node-upflow-cn";
   ```

   ```
   ADD APN:APN="apn-test",HASVPN=DISABLE,HASVPNIPV6=DISABLE,RESTORPGWSWITCH=INHERIT;
   ```
3. 将ACL“acl-upflow”绑定到该APN实例下。方向为上行进UEG，即“UPIN”。

   以下命令在“MML命令行-UEG”窗口上执行：

   ```
   ADD ACLBINDAPN:APN="apn-test",DIRECTION=UPIN,ACLNAME="acl-upflow";
   ```

   ```
   SET REFRESHSRV:REFRESHTYPE=ACL;
   ```

版权所有 © 华为技术有限公司
