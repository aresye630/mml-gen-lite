# 激活支持ACL

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活ACL功能特性的操作过程。

ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

- 操作人员已经登录华为操作维护系统。

数据

需要准备全网规划和本端规划的数据，无需准备与对端网元协商的数据，如表1所示。

| 类别        | 参数                     | 取值样例           | 获取方法   | 相关命令            |
|:----------|:-----------------------|:---------------|:-------|:----------------|
| 增加ACL规则组  | ACL规则组标识（ACLNAME）      | 3000           | 本端规划   | ADD ACLGROUP    |
| 增加基本ACL规则 | ACL规则组标识（ACLNAME）      | 2000           | 本端规划   | ADD ACLRULEBAS4 |
| 增加基本ACL规则 | 规则名称（ACLRULENAME）      | rule_bas       | 本端规划   | ADD ACLRULEBAS4 |
| 增加基本ACL规则 | 规则行为（ACLACTION）        | Deny           | 本端规划   | ADD ACLRULEBAS4 |
| 增加基本ACL规则 | 源IP地址（ACLSOURCEIP）     | 10.1.2.2       | 全网规划   | ADD ACLRULEBAS4 |
| 增加基本ACL规则 | 源IP地址反掩码（ACLSRCWILD）   | 0.0.0.255      | 全网规划   | ADD ACLRULEBAS4 |
| 增加高级ACL规则 | ACL规则组标识（ACLNAME）      | 3000           | 本端规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 规则名称（ACLRULENAME）      | rule_adv       | 本端规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 规则行为（ACLACTION）        | Permit         | 本端规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 协议类型值（ACLPROTOCOL）     | 0              | 本端规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 源IP地址（ACLSOURCEIP）     | 10.1.2.2       | 全网规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 源IP地址反掩码（ACLSRCWILD）   | 0.0.0.255      | 全网规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 目的IP地址（ACLDESTIP）      | 192.168.1.1    | 全网规划   | ADD ACLRULEADV4 |
| 增加高级ACL规则 | 目的IP地址反掩码（ACLDESTWILD） | 0.0.0.255      | 全网规划   | ADD ACLRULEADV4 |
| 增加以太ACL规则 | ACL规则组标识（ACLNAME）      | 4000           | 本端规划   | ADD ACLRULEETH  |
| 增加以太ACL规则 | 规则名称（ACLRULENAME）      | rule_eth       | 本端规划   | ADD ACLRULEETH  |
| 增加以太ACL规则 | 规则行为（ACLACTION）        | Permit         | 本端规划   | ADD ACLRULEETH  |
| 增加以太ACL规则 | 源MAC地址（ACLSRCMAC）      | 00E0-FC11-2233 | 本端规划   | ADD ACLRULEETH  |
| 增加接口ACL规则 | ACL规则组标识（ACLNAME）      | 1000           | 本端规划   | ADD ACLRULEIF   |
| 增加接口ACL规则 | 规则名称（ACLRULENAME）      | rule_if        | 本端规划   | ADD ACLRULEIF   |
| 增加接口ACL规则 | 规则行为（ACLACTION）        | Permit         | 本端规划   | ADD ACLRULEIF   |
| 增加接口ACL规则 | 接口名（IFNAME）            | Ethernet64/0/5 | 本端规划   | ADD ACLRULEIF   |

## 操作步骤

1. 增加ACL规则组。

   在“MML命令行-UNC”窗口上执行：

   **ADD ACLGROUP**: ACLNAME="ACL规则组标识", ACLTYPE="ACL规则类型";

   **说明** 

   参数"ACLTYPE"（规则组类型）在"ACLNAME"（规则组名称）为数字字符串时可以不用输入。
2. 增加基本ACL规则

   在“MML命令行-UNC”窗口上执行：

   **ADD ACLRULEBAS4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", ACLSOURCEIP="源IP地址", ACLSRCWILD="源IP地址反掩码";

   **说明** 

   基本ACL的范围段为2000～2999，增加规则时ACL规则组必须创建。

   基本ACL只能基于源IP地址和掩码进行匹配。
3. 增加高级ACL规则。

   根据不同的协议选择不同的配置。

   **说明** 

   高级ACL的范围段为3000～3999，增加规则时ACL规则组必须创建。

   高级ACL可以基于五元组进行匹配（协议类型、本端IP地址、对端IP地址、本端端口、对端端口）。

   - 协议类型是IP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEADV4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", ACLPROTOCOL="协议类型值", ACLSOURCEIP="源IP地址", ACLSRCWILD="源IP地址反掩码", ACLDESTIP="目的IP地址", ACLDESTWILD="目的IP地址反掩码";
   - 协议类型是ICMP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEADV4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", ACLPROTOCOL="协议类型值", ACLSOURCEIP="源IP地址", ACLSRCWILD="源IP地址反掩码", ACLDESTIP="目的IP地址", ACLDESTWILD="目的IP地址反掩码", ACLICMPNAME="ICMP名称", ACLICMPTYPE="网络控制管理协议类型", ACLICMPCODE="网络控制管理协议消息码";

     **说明** 

     参数"ACLICMPNAME"可以直接输入知名ICMP报文类型，对于知名类型，"ACLICMPTYPE"和"ACLICMPCODE"不需要输入。

     参数"ACLICMPNAME"输入为"Custom"时，用户可以自定义输入"ACLICMPTYPE"和"ACLICMPCODE"。

     当ICMP类型和ICMP编码都不输入时，规则将匹配所有的ICMP报文；当仅输入ICMP类型时，规则将匹配该类型所有的ICMP报文；当ICMP类型不输入时输入的ICMP编码无效。
   - 协议类型是TCP或UDP

     在“MML命令行-UNC”窗口上执行：

     **ADD ACLRULEADV4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", ACLPROTOCOL="协议类型值", ACLSOURCEIP="源IP地址", ACLSRCWILD="源IP地址反掩码", ACLDESTIP="目的IP地址", ACLDESTWILD="目的IP地址反掩码", ACLSRCPORTOP="源端口范围类型", ACLSRCPORTBEGIN="源端口号开始端口号", ACLSRCPORTEND="源端口号结束端口号", ACLDESTPORTOP="目的端口范围类型", ACLDESTPORTBEGIN="目的端口号开始端口号", ACLDESTPORTEND="目的端口号结束端口号";

     **说明** 

     当端口号的操作符为"Lt"时，需要输入结束端口号，当端口号的操作符为"Gt"、"Eq"、"Neq"时，需要输入起始端口号，当端口号的操作符为"Range"时，起始端口号同结束端口号都需要输入
4. 增加以太ACL规则

   在“MML命令行-UNC”窗口上执行：

   **ADD ACLRULEETH**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", ACLSRCMAC="源MAC地址";
5. 增加接口ACL规则

   在“MML命令行-UNC”窗口上执行：

   **ADD ACLRULEIF**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称", ACLACTION="规则行为", IFNAME="接口名";

## 验证方法

具体请参见调测ACL。

## 任务示例

任务描述

配置在接口中使用ACL规则。如图1所示，VNF1的接口interface1的IP地址为192.168.1.1，并通过Device A与VNF2，Device B相连。添加3001规则组，并添加“adv\_2”和“adv\_3”号规则，分别以VNF2的IP地址10.1.1.2和Device B的IP地址10.1.2.2为源IP地址，192.168.1.1为目的IP地址。

**图1** 流策略中使用ACL图

脚本

//添加ACL规则组。添加组号为3001的扩展规则组。

```
ADD ACLGROUP:ACLNAME="3001";
```

//添加ACL规则。添加规则名称为"adv\_2"和"adv\_3"的规则。

```
ADD ACLRULEADV4:ACLNAME="3001", ACLRULENAME="adv_2", ACLACTION=Permit, ACLPROTOCOL=0, ACLSOURCEIP="10.1.1.2", ACLSRCWILD="0.0.0.0", ACLDESTIP="192.168.1.1", ACLDESTWILD="0.0.0.0";
ADD ACLRULEADV4:ACLNAME="3001", ACLRULENAME="adv_3", ACLACTION=Deny, ACLPROTOCOL=0, ACLSOURCEIP="10.1.2.2", ACLSRCWILD="0.0.0.255", ACLDESTIP="192.168.1.1", ACLDESTWILD="0.0.0.0";
```