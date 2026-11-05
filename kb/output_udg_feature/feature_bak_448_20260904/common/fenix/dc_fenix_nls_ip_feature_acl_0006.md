# 去激活支持ACL

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中去激活ACL功能特性的操作过程。

ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- 支持包过滤功能特性已经激活。

数据

无

## 操作步骤

1. 删除接口ACL规则。

   在“MML命令行-UDG”窗口上执行：

   **RMV ACLRULEIF**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称";
2. 删除以太ACL规则。

   在“MML命令行-UDG”窗口上执行：

   **RMV ACLRULEETH**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称";
3. 删除高级ACL规则。

   在“MML命令行-UDG”窗口上执行：

   **RMV ACLRULEADV4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称";
4. 删除基本ACL规则。

   在“MML命令行-UDG”窗口上执行：

   **RMV ACLRULEBAS4**: ACLNAME="ACL规则组标识", ACLRULENAME="规则名称";
5. 删除ACL规则组。

   在“MML命令行-UDG”窗口上执行：

   **RMV ACLGROUP**: ACLNAME="ACL规则组标识";

## 任务示例

任务描述

删除ACL规则组。

脚本

//删除ACL规则。删除规则名称为"adv\_2"和"adv\_3"规则。

```
RMV ACLRULEADV4: ACLNAME="3001", ACLRULENAME ="adv_2";
```

```
RMV ACLRULEADV4: ACLNAME="3001", ACLRULENAME ="adv_3";
```

//删除ACL规则组。删除规则组号为3001的扩展规则组。

```
RMV ACLGROUP: ACLNAME="3001";
```