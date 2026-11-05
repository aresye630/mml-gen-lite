# 去激活QoS复杂流分类功能（VNRS\_VNFC）

* 操作场景
* 对系统的影响
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍如何在运行网络中去激活QoS复杂流分类功能特性。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* QoS复杂流分类功能已经激活。

数据

无需准备数据。

## 操作流程

去激活QoS复杂流分类功能操作流程如图1所示。

**图1** 去激活QoS复杂流分类功能操作流程

## 操作步骤

1. 删除接口出方向绑定流策略。

   在“MML命令行-UEG”窗口上执行：

   **RMV QOSAPPLICATION**: IFNAME="接口名称",DIRECTION=报文方向;
2. 删除绑定的流分类和流行为。

   在“MML命令行-UEG”窗口上执行：

   **RMV MQCPOLICYNODE**: POLICYNAME="策略名称",CLASSIFIERNAME="分类名称",BEHAVIORNAME="行为名称";
3. 删除流策略。

   在“MML命令行-UEG”窗口上执行：

   **RMV MQCPOLICY**: POLICYNAME="策略名称";
4. 当需要删除流分类绑定ACL规则。
5. 删除流分类。

   在“MML命令行-UEG”窗口上执行：

   **RMV MQCCLASSIFIER**: CLASSIFIERNAME="分类名称";
6. **可选：**当需要删除流动作。

   * 当需要删除重定向下一跳动作：

     在“MML命令行-UEG”窗口上执行：

     **RMV QOSACTRDRNHP**:BEHAVIORNAME="行为名称";
   * 当需要删除重标记：

     在“MML命令行-UEG”窗口上执行：

     **RMV SQOSREMARK**:BEHAVIORNAME="流行为名称";
   * 当需要删除级联流策略：

     在“MML命令行-UEG”窗口上执行：

     **RMV QOSACTRDRPOLICY**: BEHAVIORNAME="行为名称";
   * 当需要删除重定向VPN组：

     在“MML命令行-UEG”窗口上执行：

     **RMV SQOSRDRVPNGROUP**: BEHAVIORNAME="行为名称";
   * 当需要删除安全URPF：

     在“MML命令行-UEG”窗口上执行：

     **RMV SQOSURPF**: BEHAVIORNAME="流行为名称";
   * 当需要删除CAR配置：

     在“MML命令行-UEG”窗口上执行：

     **RMV SQOSCAR**: BEHAVIORNAME="流行为名称";
7. 删除流行为。

   在“MML命令行-UEG”窗口上执行：

   **RMV MQCBEHAVIOR**: BEHAVIORNAME="行为名称";
8. **可选：**清除端口流量策略报文统计。

   在“MML命令行-UEG”窗口上执行：

   **RTR SQOSPOLICYSTC**: IFNAME=接口名称, DIRECTION=方向;

## 任务示例

任务描述

去激活复杂流分类功能。

脚本

//删除接口出方向绑定流策略。

```
RMV QOSAPPLICATION: IFNAME="Ethernet64/0/3",DIRECTION =outbound;
```

//删除绑定的流分类和流行为。

```
RMV MQCPOLICYNODE: POLICYNAME="policy1",CLASSIFIERNAME="class1",BEHAVIORNAME="behavior1";
```

//删除流策略。

```
RMV MQCPOLICY: POLICYNAME="policy1";
```

//删除流分类。

```
RMV MQCCLASSIFIER: CLASSIFIERNAME="class1";
```

//删除流行为。

```
RMV MQCBEHAVIOR: BEHAVIORNAME="behavior1";
```

版权所有 © 华为技术有限公司
