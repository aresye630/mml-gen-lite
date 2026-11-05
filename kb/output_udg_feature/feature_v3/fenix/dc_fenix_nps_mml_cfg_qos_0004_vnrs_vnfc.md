# 激活QoS复杂流分类功能（VNRS\_VNFC）

* 操作场景
* 对系统的影响
* 必备事项
* 操作流程
* 操作步骤
* 验证方法
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活QoS复杂流分类功能特性的操作过程。

QoS复杂流分类涉及到流策略、流分类、流行为三个概念。一个流分类和流行为可以组成一个CB对，在具体的流策略中绑定。流策略可以绑定到指定的Ethernet接口、Ethernet子接口、Eth-Trunk接口或Eth-Trunk子接口的出入方向，经过的报文会匹配流分类中的规则，匹配上后会按照流行为中指定的动作进行处理。

流分类中指定了具体的报文匹配规则。ACL规则的配置请见ACL配置手册。

流行为中指定了报文匹配成功后对应的处理动作。目前动作类型有：允许、拒绝、指定下一跳、级联流策略。

NP卡场景下，不支持流策略统计功能以及以下ACL流行为。

* 级联流策略动作
* 重定向VPN组
* 安全URPF
* CAR

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

操作人员已经登录网络管理系统NMS（Network Management System）。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如表1所示。

**表1** 需要准备的数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| 增加ACL规则组 | ACL规则组标识（ACLNAME） | acl1 | 本端规划 | **ADD ACLGROUP** |
| 增加高级ACL规则 | ACL规则组标识（ACLNAME） | acl1 | 本端规划 | **ADD ACLRULEADV4** |
|  | 规则名称（ACLRULENAME） | rule\_6 |  |  |
|  | 规则行为（ACLACTION） | deny |  |  |
|  | 协议类型值（ACLPROTOCOL） | 0 |  |  |
| 增加基本ACL规则 | ACL规则组标识（ACLNAME） | acl1 | 本端规划 | **ADD ACLRULEBAS4** |
|  | 规则名称（ACLRULENAME） | rule\_6 |  |  |
|  | 规则行为（ACLACTION） | deny |  |  |
| MQCBEHAVIOR流行为 | 行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD MQCBEHAVIOR** |
| MQCCLASSIFIER流分类 | 分类名称（CLASSIFIERNAME） | class1 | 本端规划 | **ADD MQCCLASSIFIER** |
|  | 关系类型（OPERATOR） | or |  |  |
| MQCPOLICY流策略 | 策略名称（POLICYNAME） | policy1、policy2 | 本端规划 | **ADD MQCPOLICY** |
| QOSACTFILER流行为过滤 | 行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **SET QOSACTFILTER** |
|  | 行为状态（FILTER） | permit、deny |  |  |
| QOSACTRDRNHP重定向下一跳 | 流行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD QOSACTRDRNHP** |
|  | IP协议版本（IPVERSION） | IPv4 |  |  |
|  | 下一跳地址（NEXTHOP） | 192.168.2.3（公网IP） |  |  |
| SQOSREMARK重标记 | 流行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD SQOSREMARK** |
|  | IPv4的DSCP值（V4DSCPVALUE） | 5 |  |  |
|  | IPv6的DSCP值（V6DSCPVALUE） | 5 |  |  |
|  | DF值（DFVALUE） | 1 |  |  |
| QOSACTRDRPOLICY级联流策略 | 行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD QOSACTRDRPOLICY** |
|  | 策略名称（POLICYNAME） | policy2 |  |  |
| SQOSRDRVPNGROUP重定向VPN组 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **ADD SQOSRDRVPNGROUP** |
|  | 行为名称（BEHAVIORNAME） | behavior1 | 本端规划 |  |
| SQOSURPF安全URPF配置 | 流行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD SQOSURPF** |
|  | URPF检查类型（URPFTYPE） | strict | 本端规划 |  |
|  | 匹配默认路由（URPFDEFAULT） | disallow | 本端规划 |  |
| SQOSCAR CAR配置 | 流行为名称（BEHAVIORNAME） | behavior1 | 本端规划 | **ADD SQOSCAR** |
|  | 承诺信息速率（kbps）（CIR） | 10 | 本端规划 |  |
| QOSRULEACL依据名称和数据编号配置 | 分类名称（CLASSIFIERNAME） | class1 | 本端规划 | **ADD QOSRULEACL** |
|  | IP协议版本（IPVERSION） | IPv4 |  |  |
|  | ACL类型（ACLTYPE） | acl-name |  |  |
|  | ACL名称（ACLNAME） | acl1 |  |  |
| MQCPOLICYNODE流策略配置 | 策略名称（POLICYNAME） | policy1 | 本端规划 | **ADD MQCPOLICYNODE** |
|  | 行为名称（BEHAVIORNAME） | behavior1 |  |  |
|  | 分类名称（CLASSIFIERNAME） | class1 |  |  |
|  | 优先级（PRECEDENCE） | 1 |  |  |
| QOSAPPLICATION接口绑定流策略 | 接口名称（IFNAME） | Ethernet64/0/3 | 本端规划 | **ADD QOSAPPLICATION** |
|  | 报文方向（DIRECTION） | 出方向 |  |  |
|  | 策略名称（POLICYNAME） | policy1 |  |  |
| 使能流策略统计 | 策略名称（POLICYNAME） | policy1 | 本端规划 | **MOD MQCPOLICY** |
|  | 统计使能标志（STCENABLE） | enable |  |  |

## 操作流程

激活QoS复杂流分类功能操作流程如图1所示。

**图1** QoS复杂流分类功能操作流程

## 操作步骤

1. 配置ACL规则组。

   ACL4规则组参见激活支持ACL的配置，ACL6规则组参见激活支持ACL6的配置。
2. 增加流行为。

   在“MML命令行-UDG”窗口上执行：

   **ADD MQCBEHAVIOR**:BEHAVIORNAME="行为名称";
3. 当需要指定对应的流动作时，增加对应的流动作：

   在“MML命令行-UDG”窗口上执行：

   * 当需要配置重定向下一跳动作：

     **ADD QOSACTRDRNHP**:BEHAVIORNAME="流行为名称", IPVERSION=IPv4, NEXTHOP="下一跳地址";
   * 当需要配置重标记：

     **ADD SQOSREMARK**:BEHAVIORNAME="流行为名称", V4DSCPVALUE="IPv4的DSCP值", V6DSCPVALUE="IPv6的DSCP值", DFVALUE="DF值";
   * 当需要配置deny动作：

     **SET QOSACTFILTER**:BEHAVIORNAME="行为名称", FILTER=deny;
   * 当需要配置级联流策略动作：

     **ADD QOSACTRDRPOLICY**:BEHAVIORNAME="行为名称", POLICYNAME="策略名称";
   * 当需要配置重定向VPN组：

     **ADD SQOSRDRVPNGROUP**:VPNGROUPNAME="VPN组名称", BEHAVIORNAME="行为名称";

     需要先使用 **ADD SQOSVPNGROUP**命令添加VPN组，使用**ADD L3VPNINST**命令添加VPN实例，使用 **ADD SQOSVPNGROUPMEM**命令向VPN组添加VPN成员。
   * 当需要配置安全URPF：

     **ADD SQOSURPF**:BEHAVIORNAME="流行为名称", URPFTYPE="URPF检查类型", URPFDEFAULT="匹配默认路由";
   * 当需要配置CAR：

     **ADD SQOSCAR** :BEHAVIORNAME="流行为名称", CIR="承诺信息速率";

   流动作permit可以和其他动作共存，其他都是互斥的。
4. 增加流分类。

   在“MML命令行-UDG”窗口上执行：

   **ADD MQCCLASSIFIER**:CLASSIFIERNAME="分类名称";
5. 当需要流分类绑定ACL规则。

   在“MML命令行-UDG”窗口上执行：

   * 绑定基于名称和编号的ACL规则：

     **ADD QOSRULEACL**:CLASSIFIERNAME="分类名称",IPVERSION=IPv4,ACLTYPE=acl-name,ACLNAME="ACL名称";
6. 增加流策略，并绑定流行为和流分类。

   在“MML命令行-UDG”窗口上执行：

   * 增加流策略：

     **ADD MQCPOLICY**:POLICYNAME="策略名称";
   * 绑定流分类和流行为：

     **ADD MQCPOLICYNODE**:POLICYNAME="策略名称",CLASSIFIERNAME="分类名称",BEHAVIORNAME="行为名称";
7. 将流策略应用到指定的接口视图。

   在“MML命令行-UDG”窗口上执行：

   **ADD QOSAPPLICATION**:POLICYNAME="策略名称",IFNAME="接口名称",DIRECTION=报文方向;
8. 使能流策略统计。

   在“MML命令行-UDG”窗口上执行：

   **MOD MQCPOLICY**:POLICYNAME="策略名称",STCENABLE=统计使能标志;

## 验证方法

具体请参见调测QoS复杂流分类功能。

## 任务示例

任务描述

配置在接口中使用QoS复杂流分类功能。组网情况如图1所示，VNF1的接口Ethernet64/0/4的IP地址为192.168.2.1， VNF2的接口Ethernet64/0/5的IP地址为192.168.2.3。添加acl1规则组，并添加“adv\_3”，以VNF3的IP地址192.168.1.3为源IP地址，192.168.2.1为目的IP地址，动作为deny，还有“adv\_4”号规则，以VNF4的IP地址192.168.1.4为源IP地址，192.168.2.1为目的IP地址，动作为permit。

在DeviceA上创建流分类class1，流分类引用acl1规则组，创建流行为behavior1，流动作为重定向下一跳到192.168.2.3。创建流策略policy1，绑定到接口Ethernet64/0/3出方向。

**预期结果**：分别从VNF3 和VNF4上向VNF1和VNF2发送报文，结果应该是VNF1没收到VNF3和VNF4的报文，而VNF2能收到来自VNF4的报文。

**图2** 应用QoS复杂流分类组图

脚本

//添加ACL规则组。添加组标识为acl1的规则组。

```
ADD ACLGROUP: ACLNAME="acl1";
```

//添加ACL规则。添加规则名称为"adv\_3"和"adv\_4"的规则。

```
ADD ACLRULEADV4: ACLNAME="acl1", ACLRULENAME="adv_3", ACLACTION=Deny, ACLPROTOCOL=0, ACLSOURCEIP="192.168.1.3", ACLSRCWILD="0.0.0.0", ACLDESTIP="192.168.2.1", ACLDESTWILD="0.0.0.0";
ADD ACLRULEADV4: ACLNAME="acl1", ACLRULENAME="adv_4", ACLACTION=Permit, ACLPROTOCOL=0, ACLSOURCEIP="192.168.1.4", ACLSRCWILD="0.0.0.0", ACLDESTIP="192.168.2.1", ACLDESTWILD="0.0.0.0";
```

//增加流分类。

```
ADD MQCCLASSIFIER: CLASSIFIERNAME="class1";
```

//配置流分类引用ACL。

```
ADD QOSRULEACL: CLASSIFIERNAME="class1", IPVERSION=IPv4, ACLTYPE=acl-name, ACLNAME="acl1";
```

//增加流行为。

```
ADD MQCBEHAVIOR: BEHAVIORNAME="behavior1";
```

//配置对应的动作。

```
ADD QOSACTRDRNHP: BEHAVIORNAME="behavior1", IPVERSION=IPv4, NEXTHOP="192.168.2.3";
```

//增加流策略。

```
ADD MQCPOLICY: POLICYNAME="policy1";
```

//流策略绑定流分类和流行为。

```
ADD MQCPOLICYNODE: POLICYNAME="policy1", BEHAVIORNAME="behavior1", CLASSIFIERNAME="class1";
```

//将流策略绑定到指定的接口。

```
ADD QOSAPPLICATION: POLICYNAME="policy1", IFNAME="Ethernet64/0/3", DIRECTION=outbound;
```

//使能流策略统计。

```
MOD MQCPOLICY: POLICYNAME="policy1", STCENABLE = enable;
```

版权所有 © 华为技术有限公司
