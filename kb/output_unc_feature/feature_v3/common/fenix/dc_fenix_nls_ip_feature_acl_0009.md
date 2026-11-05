# 去激活支持ACL6

* 操作场景
* 对系统的影响
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中去激活ACL6功能特性的操作过程。

## 对系统的影响

该操作会影响使用了该规则的应用模块的报文处理。

## 必备事项

前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* 支持包过滤功能特性已经激活。

数据

无

## 操作流程

去激活ACL6功能操作流程如图1所示。

**图1** 去激活ACL6功能操作流程

## 操作步骤

1. 删除ACL6规则。

   在“MML命令行-UNC”窗口上执行：

   **RMV ACLRULEADV6**: ACLNAME="IPv6 ACL规则组标识", ACLRULENAME="规则名称";
2. 删除ACL6规则组。

   在“MML命令行-UNC”窗口上执行：

   **RMV ACLGROUP6**: ACLNAME="IPv6 ACL规则组标识";

## 任务示例

任务描述

删除ACL6规则组规则。

脚本

//删除ACL6规则。删除规则名称为"rule\_5"规则。

```
RMV ACLRULEADV6: ACLNAME="3000", ACLRULENAME ="rule_5";
```

//删除ACL6规则组。删除规则组号为3000的扩展规则组。

```
RMV ACLGROUP6: ACLNAME="3000";
```

版权所有 © 华为技术有限公司
