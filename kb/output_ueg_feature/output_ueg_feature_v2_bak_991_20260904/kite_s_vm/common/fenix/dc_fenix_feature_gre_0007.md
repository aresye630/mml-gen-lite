# 去激活支持GRE

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中去激活GRE功能的操作过程。

## 对系统的影响

去激活GRE时，若GRE隧道上仍有报文通过，将导致业务中断。

## 必备事项

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- GRE隧道已建立。

数据

无需准备数据。

## 操作步骤

- 删除GRE隧道。

  在“MML命令行-UEG”窗口上执行：

  **RMV GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型;

## 任务示例

任务描述

删除配置的GRE隧道。

脚本

//删除配置的GRE隧道Tunnel1。

```
RMV GRETUNNEL: TNLNAME="Tunnel1",TNLTYPE=gre;
```