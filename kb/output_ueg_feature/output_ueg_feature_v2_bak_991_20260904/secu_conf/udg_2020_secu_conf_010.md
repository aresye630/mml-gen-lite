# 配置互访流量的重定向功能

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UEG内部同一VPN的UE用户之间报文转发的安全。

**说明** 

- 适用于PGW-U、UPF。
- 本文中的重定向设备以Firewall为例。
- PGW-U/UPF内置NAT功能时，不支持UE互访。

UEG报文重定向示意图如图1所示。

**图1** UEG报文重定向示意图

如图1，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：

- DC-GW上需完成ACL及重定向IP等策略路由的相关配置。
- UEG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。

## 必备事项

前提条件

如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。

数据

| 类别                   | 参数名称                           | 取值样例           | 获取方法   | 说明                                                                                                                                                                                      |
|:---------------------|:-------------------------------|:---------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 全局SGi重定向开关           | IPV4全局Gi重定向开关（V4GIREDIRSWITCH） | ENABLE         | 本端规划   | SET GIREDIRECTFUNC                                                                                                                                                                      |
| 全局SGi重定向开关           | IPV6全局Gi重定向开关（V6GIREDIRSWITCH） | ENABLE         | 本端规划   | SET GIREDIRECTFUNC                                                                                                                                                                      |
| 基于VPN的SGi接口重定向（IPv4） | 需绑定的VPN实例名（VPNINSTANCE）        | ispvpn1        | 本端规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv4） | 重定向的目的地址类型（IPTYPE）             | IPv4           | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv4） | IPv4重定向动作（V4REDIRIPTYPE）       | IPADDRESS      | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv4） | IPv4重定向IP地址（IPV4ADDRESS）       | 10.1.1.1       | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv6） | 需绑定的VPN实例名（VPNINSTANCE）        | ispvpn1        | 本端规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv6） | 重定向的目的地址类型（IPTYPE）             | IPv6           | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv6） | IPv6重定向动作（V6REDIRIPTYPE）       | IPADDRESS      | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
| 基于VPN的SGi接口重定向（IPv6） | IPv6重定向IP地址（IPV6ADDRESS）       | FC00::10:1:1:1 | 全网规划   | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。 ADD GIREDIRECTPARA “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。“IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |

## 操作步骤

1. 以下命令在“MML命令行 - UEG”窗口上执行。设置全局的SGi重定向开关。

   **SET GIREDIRECTFUNC**:V4GIREDIRSWITCH=ENABLE,V6GIREDIRSWITCH=ENABLE;

   **说明** 

   当全局的SGi接口重定向开关为不使能时，整个UEG的所有VPN的SGi接口重定向功能都会被关闭。使能全局的SGi接口重定向后，还要根据各个VPN的重定向配置来决定是否进行SGi接口的重定向。
2. 设置基于某个VPN的SGi重定向开关及重定向报文的目的地址。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="需绑定的VPN实例名",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="IPV4地址";
3. 设置默认VPN（\_public\_）用户的SGi重定向开关及重定向报文的目的地址。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="\_public\_",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="IPV4地址";
4. 设置IPv6 Gi redirect。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="VPN Instance to Bind",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="IPV6地址";

## 任务示例

任务描述

对同一UEG内部的UE之间报文进行重定向，APN绑定的VPN实例以ispvpn1为例。

脚本

1. 配置全局的Gi接口重定向功能。

   ```
   SET GIREDIRECTFUNC:V4GIREDIRSWITCH=ENABLE,V6GIREDIRSWITCH=ENABLE;
   ```
2. 配置VPN实例。

   ```
   //IPv4, IPv6, or IPv4v6:
   ADD L3VPNINST:VRFNAME="ispvpn1";
   ADD VPNINST: VPNINSTANCE="ispvpn1";

   //IPv4:
   ADD VPNINSTAF:VRFNAME="ispvpn1", AFTYPE=ipv4uni, VRFRD="192.168.225.138:100";

   //IPv6:
   ADD VPNINSTAF:VRFNAME="ispvpn1", AFTYPE=ipv6uni, VRFRD="192.168.225.138:100";
   ```
3. 配置基于VPN的Gi接口重定向。

   //IPv4：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="ispvpn1",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="10.1.1.1";
   ```

   //IPv6：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="ispvpn1",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="FC00::10:1:1:1";
   ```
4. 配置默认VPN用户的Gi接口重定向。

   //IPv4：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="10.1.1.1";
   ```

   //IPv6：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="FC00::10:1:1:1";
   ```