# 删除VPN组（VNRS\_VNFC）

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中删除VPN组的基本操作过程。支持删除VPN组或仅删除VPN组成员。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

* 设备加电并正常启动
* 该接口在设备上存在

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如表1所示。

**表1** 需要准备的数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| 删除VPN组 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **RMV SQOSVPNGROUP** |
| 删除VPN组成员 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **RMV SQOSVPNGROUPMEM** |
|  | VPN名称（VPNNAME） | vpn1 | 本端规划 |  |
|  | VPN优先级（VPNPRIORITY） | 2 | 本端规划 |  |

## 操作步骤

* 删除已经创建的VPN组

  在“MML命令行-UDG”窗口上执行：

  **RMV SQOSVPNGROUP**:VPNGROUPNAME="VPN组名称";
* 删除VPN组成员

  在“MML命令行-UDG”窗口上执行：

  **RMV SQOSVPNGROUPMEM** : VPNGROUPNAME="VPN组名称", VPNNAME="VPN名称";

## 任务示例

任务描述

删除已经创建的VPN组或删除VPN组成员。

脚本

//删除已经创建的VPN组test1。

```
RMV SQOSVPNGROUP:VPNGROUPNAME="test1";
```

//删除VPN组成员vpn1。

```
RMV SQOSVPNGROUPMEM:VPNGROUPNAME="test1",VPNNAME="vpn1";
```

版权所有 © 华为技术有限公司
