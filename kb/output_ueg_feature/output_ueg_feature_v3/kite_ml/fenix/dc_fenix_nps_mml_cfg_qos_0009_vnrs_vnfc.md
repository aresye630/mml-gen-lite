# 创建VPN组（VNRS\_VNFC）

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 验证方法
* 任务示例

## 操作场景

在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。

NP卡场景下，不支持创建VPN组。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

设备加电并正常启动。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如表1所示

**表1** 需要准备的数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| 增加VPN组 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **ADD SQOSVPNGROUP** |
| 增加VPN组成员 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **ADD SQOSVPNGROUPMEM** |
|  | VPN名称（VPNNAME） | vpn1 | 本端规划 |  |
|  | VPN优先级（VPNPRIORITY） | 2 | 本端规划 |  |

## 操作步骤

1. 增加VPN组

   在“MML命令行-UEG”窗口上执行：

   **ADD SQOSVPNGROUP**: VPNGROUPNAME="VPN组名称";
2. 增加VPN组成员

   在“MML命令行-UEG”窗口上执行：

   **ADD SQOSVPNGROUPMEM**: VPNGROUPNAME="VPN组名称", VPNNAME="VPN名称", VPNPRIORITY="VPN优先级";

## 验证方法

查询VPN组的信息是否与数据规划表中一致。

* 查询VPN组配置

  在“MML命令行-UEG”窗口上执行：

  **LST SQOSVPNGROUP**: VPNGROUPNAME="VPN组名称";

  **预期结果：**查询结果与规划值一致。

  ```
  RETCODE = 0  操作成功。                                                                                                                                结果如下                                                         
  ------------------------                                                         
  VPN组名称 = test1   
    VPN名称 = vpn1  
  VPN优先级 = 2                                                              
  (结果个数 = 1)                                                          
  ---    END
  ```

## 任务示例

任务描述

创建VPN组并增加VPN组成员。

脚本

//创建VPN组。

```
ADD SQOSVPNGROUP:VPNGROUPNAME="test1";
```

//增加VPN组成员。

```
ADD SQOSVPNGROUPMEM:VPNGROUPNAME="test1",VPNNAME="vpn1",VPNPRIORITY=2;
```

版权所有 © 华为技术有限公司
