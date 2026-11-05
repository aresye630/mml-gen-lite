# 去激活DSCP到VLAN优先级的映射（VNRS）

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍，在运行网络中，去激活DSCP到VLAN优先级映射功能的操作过程。

## 对系统的影响

无

## 必备事项

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- 已经激活DSCP到VLAN优先级映射功能。

数据

无需准备数据。

## 操作步骤

1. 删除对应的DSCPMAP。

   在“MML命令行-UNC”窗口上执行：

   **RMV DSCPMAP**: DSCP=DSCP值,TYPE=优先级类型,VALUE=优先级数值;

## 任务示例

任务描述

- 删除已配置的DSCPMAP。

脚本

//删除已配置的DSCPMAP。

```
RMV DSCPMAP:DSCP=8,VALUE=6,TYPE=8021p;
```