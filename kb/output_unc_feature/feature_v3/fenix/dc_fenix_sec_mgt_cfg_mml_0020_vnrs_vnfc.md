# 配置OSPF安全

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

## 操作场景

网络上对OSPF协议的攻击方法主要为伪造报文攻击，可以通过配置报文认证手段来识别并丢弃这些报文。

可能的攻击手段有：

* 修改报文老化时间到最大老化时间，导致所有UNC设备废弃这个报文。
* 发布合法的Max Sequence Number的LSA或者接近Max Seq Num的报文。
* 邻居UNC设备重启时复位其加密序列号状态的时机，更改序列号。
* 修改Hello报文中的邻居列表。

OSPF支持报文验证功能，只有通过验证的报文才能接收，否则将不能正常建立邻居关系。使用区域验证时，一个区域中所有的UNC设备在该区域下的验证模式和口令必须一致。例如，在Area0内所有UNC设备上配置验证模式为简单验证，口令为abc。接口验证方式用于在相邻的UNC设备之间设置验证模式和口令，优先级高于区域验证方式。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

该操作无需准备数据。

## 操作步骤

1. 创建OSPF进程。

   在“MML命令行-UNC”窗口上执行：

   **ADD OSPF**: PROCID=进程号;
2. 增加OSPF区域。

   在“MML命令行-UNC”窗口上执行：

   **ADD OSPFAREA**: PROCID=进程号, AREAID="区域号";
3. 增加运行OSPF协议的接口。

   选择执行如下步骤之一：

   * 在“MML命令行-UNC”窗口上执行：

     **ADD OSPFINTERFACE**: PROCID=进程号, AREAID="区域标识", IFNAME="接口名";

     参数“AREAID”（区域号）与步骤2中的“AREAID”的取值相一致。
   * 在“MML命令行-UNC”窗口上执行：

     **ADD OSPFNETWORK**: PROCID=进程号, AREAID="区域号", IPADDRESS=IP地址, WILDCARDMASK=掩码;

     如果接口的IP地址在**ADD OSPFNETWORK**命令指定的网段范围内，接口就会自动运行OSPF协议。

     参数“AREAID”（区域号）与步骤2中的“AREAID”的取值相一致。
4. 配置OSPF接口验证参数。

   在“MML命令行-UNC”窗口上执行：

   **MOD OSPFINTERFACEAUTH**: PROCID=OSPF进程号, AREAID="区域号", IFNAME="接口名", AUTHENMODE=认证模式, AUTHTEXTSIMPLE=简单认证密码;

版权所有 © 华为技术有限公司
