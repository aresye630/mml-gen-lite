# 激活支持ACL6

* 操作场景
* 对系统的影响
* 必备事项
* 操作流程
* 操作步骤
* 验证方法
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活ACL6功能特性的操作过程。

ACL6是一种IPv6包过滤技术，通过对IPv6报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL6规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等，防止设备被非法报文攻击，保证网络安全。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。

数据

需要准备全网规划的数据，无需准备与对端网元协商的数据，如表1所示。

**表1** 需要准备的数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| 增加ACL6规则组 | IPv6 ACL规则组标识（ACLNAME） | 3000 | 本端规划 | **ADD ACLGROUP6** |
| 增加ACL6规则 | 源IPv6地址（ACLSOURCEIP） | 2001:db8::1 | 全网规划 | **ADD ACLRULEADV6**  **ADD ACLRULEBAS6** |
|  | 源IPv6地址正掩码长度（ACLSRCWILD） | 24 | 本端规划 |  |
|  | 规则行为（ACLACTION） | Permit | 本端规划 |  |
|  | IPv6 ACL规则组标识（ACLNAME） | 3000 | 本端规划 |  |
|  | 规则名称（ACLRULENAME） | rule\_5 | 本端规划 |  |

## 操作流程

激活ACL功能操作流程如图1所示。

**图1** 激活ACL6功能操作流程

## 操作步骤

1. 增加ACL6规则组。

   在“MML命令行-UNC”窗口上执行：

   **ADD ACLGROUP6**: ACLNAME="IPv6 ACL规则组标识", ACLTYPE=规则组类型;

   参数"ACLTYPE"（规则组类型）在"ACLNAME"（规则组名称）为数字字符串时可以不用输入。
2. 增加ACL6规则。

   根据不同的协议选择不同的配置。

   * 协议类型是IP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEBAS6**: ACLNAME="IPv6 ACL规则组标识", ACLRULENAME="规则名称", ACLACTION=规则行为, ACLSOURCEIP="源IPV6地址", ACLSRCWILD="源IPV6地址正掩码长度";

     **ADD ACLRULEADV6**: ACLNAME="IPv6 ACL规则组标识号", ACLRULENAME="规则名称", ACLACTION=规则行为, ACLPROTOCOLTYPE=协议选项类型, ACLPROTOCOL=协议类型值, ACLSOURCEIP="源IPV6地址", ACLSRCWILD="源IPV6地址正掩码长度", ACLDESTIP="目的IPV6地址", ACLDESTWILD="目的IPV6地址正掩码长度";

     基本ACL6的范围段为2000～2999，高级ACL的范围段为3000～3999，增加规则时ACL规则组必须创建。

     基本ACL6只能基于源IP地址和掩码进行匹配。

     高级ACL6可以基于五元组进行匹配（协议类型、本端IP地址、对端IP地址、本端端口、对端端口）。
   * 协议类型是ICMP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEADV6**: ACLNAME="IPv6 ACL规则组标识", ACLRULENAME="规则名称", ACLACTION=规则行为, ACLPROTOCOLTYPE=协议选项类型, ACLPROTOCOL=协议类型值, ACLSOURCEIP="源IPV6地址", ACLSRCWILD="源IPV6地址正掩码长度", ACLDESTIP="目的IPV6地址", ACLDESTWILD="目的IPV6地址正掩码长度", ACLICMPNAME="ICMP名称", ACLICMPTYPE=网络控制管理协议类型, ACLICMPCODE=网络控制管理协议消息码;

     参数"ACLICMPNAME"可以直接输入知名ICMP报文类型，对于知名类型，"ACLICMPTYPE"和"ACLICMPCODE"不需要输入。

     参数"ACLICMPNAME"输入为"Custom"时，用户可以自定义输入"ACLICMPTYPE"和"ACLICMPCODE"。

     当ICMP类型和ICMP编码都不输入时，规则将匹配所有的ICMP报文；当仅输入ICMP类型时，规则将匹配该类型所有的ICMP报文；当ICMP类型不输入时输入的ICMP编码无效。
   * 协议类型是TCP或UDP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEADV6**: ACLNAME="IPv6 ACL规则组标识", ACLRULENAME="规则名称", ACLACTION=规则行为, ACLPROTOCOLTYPE=协议选项类型, ACLPROTOCOL=协议类型值, ACLSOURCEIP="源IPV6地址", ACLSRCWILD="源IPV6地址正掩码长度", ACLDESTIP="目的IPV6地址", ACLDESTWILD="目的IPV6地址正掩码长度", ACLSRCPORTOP=源端口范围类型, ACLSRCPORTBEGIN=源端口号开始端口号, ACLSRCPORTEND=源端口号结束端口号, ACLDESTPORTOP=目的端口范围类型, ACLDESTPORTBEGIN=目的端口号开始端口号, ACLDESTPORTEND=目的端口号结束端口号;

     当端口号的操作符为"Lt"时，需要输入结束端口号。当端口号的操作符为"Gt"、"Eq"、"Neq"时，需要输入起始端口号。当端口号的操作符为"Range"时，起始端口号同结束端口号都需要输入。

## 验证方法

具体请参见调测ACL6。

## 任务示例

任务描述

创建3001和3002的ACL6规则组，添加相应的规则。

脚本

//添加ACL6规则组。添加组号为3000的扩展规则组。

```
ADD ACLGROUP6: ACLNAME ="3000";
```

//添加ACL6规则。添加规则名称为"rule\_5"的规则。

```
ADD ACLRULEADV6: ACLNAME="3000", ACLRULENAME="rule_5", ACLACTION=Permit, ACLPROTOCOL=0, ACLSOURCEIP="2001:db8::1", ACLSRCWILD=24;
```

版权所有 © 华为技术有限公司
