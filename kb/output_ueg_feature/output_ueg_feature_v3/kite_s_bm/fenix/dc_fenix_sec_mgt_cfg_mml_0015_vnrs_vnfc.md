# 配置基于接口的ACL功能

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

## 操作场景

为提高安全性，需要禁止非法地址或者网络对FENIX的访问。通过在接口上应用ACL策略，仅允许符合条件的报文通过（或拒绝符合条件的报文通过）。ACL可以与流分类功能配合使用，以实现数据包过滤等功能。

## 对系统的影响

可能会对设备的转发性能有一定影响。

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

该操作无需准备数据。

## 操作步骤

1. 配置ACL。详细步骤请参考激活支持ACL。
2. 增加流行为。

   在“MML命令行-UEG”窗口上执行：

   **ADD MQCBEHAVIOR**: BEHAVIORNAME="行为名称";
3. 增加对应的流动作。

   在“MML命令行-UEG”窗口上执行：

   配置重定向下一跳动作：

   **ADD QOSACTRDRNHP**: BEHAVIORNAME="流行为名称", IPVERSION=IPv4, NEXTHOP="下一跳地址";

   配置Deny动作：

   **SET QOSACTFILTER**: BEHAVIORNAME="行为名称", FILTER=deny;

   配置级联流策略动作：

   **ADD QOSACTRDRPOLICY**:BEHAVIORNAME="行为名称", POLICYNAME="策略名称";

   流动作permit可以和其他动作共存，其他都是互斥的。
4. 增加流分类。

   在“MML命令行-UEG”窗口上执行：

   **ADD MQCCLASSIFIER**: CLASSIFIERNAME="分类名称";
5. 流分类绑定ACL规则。

   在“MML命令行-UEG”窗口上执行：

   * 绑定基于名称和编号的ACL规则：

     **ADD QOSRULEACL**: CLASSIFIERNAME="分类名称",IPVERSION=IPv4,ACLTYPE="ACL类型",ACLNAME="ACL名称",ACLNUM="ACL编号";
6. 增加流策略，并绑定流行为和流分类。

   在“MML命令行-UEG”窗口上执行：

   * 增加流策略：

     **ADD MQCPOLICY**: POLICYNAME="策略名称";
   * 绑定流分类和流行为：

     **ADD MQCPOLICYNODE**: POLICYNAME="策略名称",CLASSIFIERNAME="分类名称",BEHAVIORNAME="行为名称";
7. 将流策略应用到指定的接口视图。

   在“MML命令行-UEG”窗口上执行：

   **ADD QOSAPPLICATION**: POLICYNAME="策略名称",IFNAME="接口名称",DIRECTION=报文方向;

版权所有 © 华为技术有限公司
