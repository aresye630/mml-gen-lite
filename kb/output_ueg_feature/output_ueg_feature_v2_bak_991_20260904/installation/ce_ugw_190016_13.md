# 配置静态路由+BFD组网（IPv6）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。

在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD双向/单向转发检测机制为链路提供双向/单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。

如图1所示为VNF与周边网元的静态路由互通组网示意图。VNF与网关运行静态路由协议而接入运营商网络/企业网络，PE（Provider Edge）或DC-GW作网关。VNF和DC-GW之间采用单臂BFD探测。PE的路由配置请参考运营商的网络规划配置，DC-GW的配置请参考对应型号设备的产品文档。

**图1** 静态路由+BFD组网

## 必备事项

前提条件

- 请阅读并熟悉特性IPFD-020503 静态路由和IPFD-020403 BFD特性概述。
- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

- VNF与网络实体之间的网络环境已经构建完成。

数据

VNF使用静态路由绑定静态BFD检测功能与对端设备建立可靠的IP连接。

- 在VNF上配置静态路由与对端建立链路。
- 在VNF上配置静态BFD功能增强链路检测可靠性。
- 在VNF上推荐采用子接口的外联口与外部网络对接。

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别在每个CSLB各规划2个子接口负荷分担承载流量，后续扩容CSLB后自动在每个CSLB上扩展2个子接口承载流量。实际场景可根据网设规划进行适配。

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                      | 参数名称                             | 取值样例                                    | 获取方法                                                                                                                                                          | 说明                                                                                                                              |
|:------------------------|:---------------------------------|:----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| ADD L3VPNINST           | VPN实例名称（VRFNAME）                 | VPN_Access                              | 参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。                 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。                                                                                      |
| ADD VPNINSTAF           | 地址族名称(AFTYPE)                    | ipv6uni                                 | -                                                                                                                                                             | IPv6组网场景下，该参数选择ipv6uni。                                                                                                         |
| SET BFD                 | BFD使能标志（BFDENABLE）               | TRUE                                    | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。                                                                                                                   | 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。                                                                   |
| ADD AUTOSCALINGETHTRUNK | 以太Trunk模板ID（ETHTRUNKTMPID）       | 1                                       | 本端规划                                                                                                                                                          | SR-IOV bonding组网需要规划。 只有MAC地址一样的VNIC才能加到同一个TRUNK里。                                                                              |
| ADD AUTOSCALINGETHTRUNK | 虚拟网卡ID列表（VNICLIST）               | 4 5                                     | 参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“虚拟网口”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。               | SR-IOV bonding组网需要规划。 只有MAC地址一样的VNIC才能加到同一个TRUNK里。                                                                              |
| ADD AUTOSCALINGSERVICE  | 服务名称（SERVICENAME）                | ServName_Access_100 ServName_Access_200 | 本端规划                                                                                                                                                          | 如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。                                                                                |
| ADD AUTOSCALINGSERVICE  | VPN实例名称（VPNNAME）                 | VPN_Access                              | 已规划数据中获取                                                                                                                                                      | 如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。                                                                                |
| ADD AUTOSCALINGSERVICE  | 地址族（AFTYPE）                      | IPv6                                    | 已规划数据中获取                                                                                                                                                      | 如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。                                                                                |
| ADD AUTOSCALINGSERVICE  | 虚拟网卡ID（VNICID）                   | 4 5                                     | 参见“5G Core LLD文档 > 业务IP对接设计 > 虚拟网口”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“虚拟网口”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。               | 非SR-IOV bonding组网需要规划。                                                                                                          |
| ADD AUTOSCALINGSERVICE  | 以太Trunk模板ID（ETHTRUNKTMPID）       | 1                                       | 已规划数据中获取                                                                                                                                                      | SR-IOV bonding组网需要规划。                                                                                                           |
| ADD AUTOSCALINGSERVICE  | VLAN ID（VLANID）                  | 100 200                                 | 参见“5G Core LLD文档 > 业务IP对接设计 > VLAN ID（VM）”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VLAN ID（VM）”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。 | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName_Access_100）。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| ADD AUTOSCALINGSERVICE  | 起始地址（BEGINADDR6）                 | FC00::10C2 FC00::10E2                   | 参见“5G Core LLD文档 > 业务IP对接设计 > 起始IP”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“起始IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。               | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName_Access_100）。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| ADD AUTOSCALINGSERVICE  | 结束地址（ENDADDR6）                   | FC00::10DE FC00::10FE                   | 参见“5G Core LLD文档 > 业务IP对接设计 > 结束IP”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“结束IP”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。               | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName_Access_100）。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| ADD AUTOSCALINGSERVICE  | 地址池掩码长度（MASKLEN）                 | 123 123                                 | 参见“5G Core LLD文档 > 业务IP对接设计 > 子网掩码”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“子网掩码”。逻辑接口包括N3if、N4if、N6等接口。此处以N3if为例。               | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划ServName_Access_100）。 此处规划的IP地址是与网关互通的外联口IP。 根据ISU VM的数量规划IPv6地址池掩码长度。 此处以123位掩码为例进行介绍，具体以网设规划为准。 |
| ADD AUTOSCALINGSRBFD    | 服务名称（SERVICENAME）                | ServName_Access_100 ServName_Access_200 | 已规划数据中获取                                                                                                                                                      | VNF所在硬件设备直连PE时需要规划，直连DC-GW时不需要规划。                                                                                               |
| ADD AUTOSCALINGSRBFD    | 地址族（IPVERSION）                   | IPv6                                    | 已规划数据中获取                                                                                                                                                      | VNF所在硬件设备直连PE时需要规划，直连DC-GW时不需要规划。                                                                                               |
| ADD AUTOSCALINGSRBFD    | 检测倍数（MULTIPLIER）                 | 4                                       | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。                                                                                                         | VNF所在硬件设备直连PE时需要规划，直连DC-GW时不需要规划。                                                                                               |
| ADD AUTOSCALINGSRBFD    | 最小接收间隔（ms）（MINRXINTERVAL）        | 500                                     | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。                                                                                                       | VNF所在硬件设备直连PE时需要规划，直连DC-GW时不需要规划。                                                                                               |
| ADD AUTOSCALINGSRBFD    | 最小发送间隔（ms）（MINTXINTERVAL）        | 500                                     | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-tx-interval(毫秒)”。                                                                                                       | VNF所在硬件设备直连PE时需要规划，直连DC-GW时不需要规划。                                                                                               |
| ADD AUTOSCALINGBFD      | 模板名称（TEMPLATENAME）               | BFD_1BFD_2                              | 本端规划                                                                                                                                                          | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | BFD类型（BFDTYPE）                   | Static                                  | 固定取值                                                                                                                                                          | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 服务名称（SERVICENAME）                | ServName_Access_100 ServName_Access_200 | 已配置数据中获取                                                                                                                                                      | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 地址族（IPVERSION）                   | IPv6                                    | 固定取值                                                                                                                                                          | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 目的地址（DESTADDR6）                  | FC00::10C1FC00::10E1                    | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > 对端IP地址”。                                                                                                                    | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 单臂Echo会话的收包间隔（ms）（MINECHORXINT）  | 500                                     | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > min-rx-interval(毫秒)”。                                                                                                       | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 检测倍数（DETECTMULTI）                | 4                                       | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > detect-multiplier”。                                                                                                         | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGBFD      | 单臂Echo（ONEARMECHO）               | TRUE                                    | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD类型”。 “BFD类型”为“BFD Echo”/“单臂BFD”时，该参数设置为“TRUE”。                                                                           | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。 参数“目的地址”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                          |
| ADD AUTOSCALINGSRROUTE  | 服务名称（SERVICENAME）                | ServName_Access_100 ServName_Access_200 | 已规划数据中获取                                                                                                                                                      | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | VPN实例名称 (VRFNAME)                | VPN_Access                              | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 本端VRF名称”。                                                                                                                  | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | 路由前缀IPv6（PREFIX6）                | FC00::2001:4 FC00::2002:4               | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。                                                                                                                     | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | 路由掩码长度（MASKLENGTH）               | 128                                     | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 子网掩码/掩码长度”。                                                                                                                | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | 路由下一跳IPv6（NEXTHOP6）              | FC00::10C1FC00::10E1                    | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 下一跳地址”。                                                                                                                    | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | 地址族（IPVERSION）                   | IPv6                                    | 已规划数据中获取                                                                                                                                                      | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | IPv6路由下一跳分配方式（NEXTHOPALLOCTYPE6） | CONFIG                                  | -                                                                                                                                                             | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“NEXTHOP6”是网关的接口IP。                                              |
| ADD AUTOSCALINGSRROUTE  | BFD使能标识 （BFDENABLE）              | TRUE                                    | 参见“5G Core LLD文档 > 路由设计 > BFD设计 > BFD是否使能”。                                                                                                                   | 开启BFD探测时，必须设置为“TRUE”。                                                                                                           |
| ADD AUTOSCALINGSRROUTE  | BFD模板名称（BFDTEMPLATENAME）         | BFD_1BFD_2                              | 已配置数据中获取                                                                                                                                                      | VNF所在硬件设备直连DC-GW时需要规划，直连PE时不需要规划。                                                                                               |

文档

获取网设LLD文档。

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_Access";
   ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv6uni;
   ```

   **说明** 

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```
3. 关闭自动配置开关。

   1. 查询自动配置开关。

      ```
      LST AUTOCONFIG:;
      ```

      如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。
   2. （可选）查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

      ```
      DSP OPSASSISTSTATE:;
      ```
   3. （可选）关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

      ```
      SET AUTOCONFIG:SWITCHFLAG=FALSE;
      ```
4. 接口采用SR-IOV bonding组网时，添加以太网隧道多虚拟网卡自动化配置模板。

   ```
   ADD AUTOSCALINGETHTRUNK: ETHTRUNKTMPID=1, VNICLIST="4 5";
   ```

   **说明** 

   - 在SR-IOV Bonding组网场景下，必须配置该模板。非SR-IOV bonding组网场景下，请跳过本步骤。
   - 如果要实现SR-IOV接口bonding功能，那么一个Eth-trunk接口下的两个成员接口必须MAC相同，且ID号连续。即：“VNICLIST”中配置的ID号为MAC相同且连续的两个以太网接口的ID。可使用**LST INTERFACE**命令查询以太网接口的mac地址与以太网接口名称。
5. 配置外联口自动部署模板。
   - 非SR-IOV bonding组网场景下：

     ```
     ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_100",VPNNAME="VPN_Access",AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG,AUTOCFGIFTYPE=VNIC,VNICID=4,VLANID=100, BEGINADDR6="FC00::10C2", ENDADDR6="FC00::10DE", MASKLEN=123;
     ```

     ```
     ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_200",VPNNAME="VPN_Access",AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG,AUTOCFGIFTYPE=VNIC,VNICID=5,VLANID=200, BEGINADDR6="FC00::10E2", ENDADDR6="FC00::10FE", MASKLEN=123;
     ```
   - SR-IOV bonding组网场景下：

     ```
     ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_100",VPNNAME="VPN_Access",AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=1, VLANID=100, BEGINADDR6="FC00::10C2", ENDADDR6="FC00::10DE", MASKLEN=123; 
     ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_200",VPNNAME="VPN_Access",AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=1, VLANID=200, BEGINADDR6="FC00::10E2", ENDADDR6="FC00::10FE", MASKLEN=123;
     ```

   **说明** 

   如果规划外联口使用IPv4v6双栈地址，则分别执行该命令对同一外联口配置IPv4和IPv6地址。
6. VNF所在硬件设备直连PE时，增加静态路由的动态BFD自动部署模板。

   ```
   ADD AUTOSCALINGSRBFD: SERVICENAME="ServName_Access_100", IPVERSION=IPv6, MINRXINTERVAL=500, MINTXINTERVAL=500, MULTIPLIER=4; 
   ADD AUTOSCALINGSRBFD: SERVICENAME="ServName_Access_200", IPVERSION=IPv6, MINRXINTERVAL=500, MINTXINTERVAL=500, MULTIPLIER=4;
   ```
7. VNF所在硬件设备直连DC-GW时，增加BFD会话自动部署模板。

   ```
   ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_1", BFDTYPE=Static, SERVICENAME="ServName_Access_100", IPVERSION=IPv6, DESTADDR6="FC00::10C1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
   ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_2", BFDTYPE=Static, SERVICENAME="ServName_Access_200", IPVERSION=IPv6, DESTADDR6="FC00::10E1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
   ```
8. 增加静态路由自动部署模板。

   VNF所在硬件设备直连PE时：

   ```
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_100", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2001:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10C1", BFDENABLE=TRUE, DESCRIPTION="VPN_Access_ROUTE1"; 
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_200", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2001:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10E1", BFDENABLE=TRUE, DESCRIPTION="VPN_Access_ROUTE2";
   ```

   ```
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_100", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2002:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10C1", BFDENABLE=TRUE, DESCRIPTION="VPN_Access_ROUTE1"; 
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_200", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2002:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10E1", BFDENABLE=TRUE, DESCRIPTION="VPN_Access_ROUTE2";
   ```

   VNF所在硬件设备直连DC-GW时：

   ```
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_100", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2001:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10C1", BFDENABLE=TRUE, BFDTEMPLATENAME="BFD_1", DESCRIPTION="VPN_Access_ROUTE1"; 
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_200", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2001:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10E1", BFDENABLE=TRUE, BFDTEMPLATENAME="BFD_2", DESCRIPTION="VPN_Access_ROUTE2";
   ```

   ```
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_100", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2002:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10C1", BFDENABLE=TRUE, BFDTEMPLATENAME="BFD_1", DESCRIPTION="VPN_Access_ROUTE1"; 
   ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_Access_200", VRFNAME="VPN_Access", IPVERSION=IPv6, PREFIX6="FC00::2002:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::10E1", BFDENABLE=TRUE, BFDTEMPLATENAME="BFD_2", DESCRIPTION="VPN_Access_ROUTE2";
   ```
9. 打开自动配置开关。

   ```
   SET AUTOCONFIG: SWITCHFLAG=TRUE;
   ```

   **说明** 

   - 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。
   - 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

     需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址。下一跳为VNF上外联口的IP地址，由于自动部署时外联口的IP地址是系统自动分配的，因此建议首先通过命令**LST IFIPV6ADDRESS**查看外联口的IP地址。

## 验证方法

1. 查看接口状态及信息是否与规划数据一致。

   ```
   LST INTERFACE:;
   ```

   ```
   LST IFIPV6ADDRESS:;
   ```

   ```
   LST IPBINDVPN:;
   ```

   - 如果一致，请执行3。
   - 如果不一致，请执行2。
2. 修改外联口自动部署模板。
   1. 关闭自动化配置开关。

      ```
      SET AUTOCONFIG: SWITCHFLAG=FALSE;
      ```
   2. 查询需要修改的外联口自动部署模板并记录服务名称、起始地址和结束地址等参数。

      ```
      LST AUTOSCALINGSERVICE:;
      ```
   3. 查询需要修改的子接口并记录查询结果。记录哪些接口的IP地址在2.b中记录的起始地址和结束地址范围内。

      ```
      LST IFIPV6ADDRESS:;
      ```
   4. 查询需要修改的静态路由自动部署模板并记录服务名称、VPN实例名称、路由前缀、路由掩码长度和路由下一跳等参数。

      ```
      LST AUTOSCALINGSRROUTE:;
      ```
   5. 查询需要修改的静态路由并记录查询结果。通过和2.d中的记录结果对比，记录待删除的静态路由。

      ```
      LST SRROUTE6:;
      ```
   6. 删除2.c中记录的所有子接口。

      **RMV INTERFACE**

      IPv4v6双栈场景，删除子接口时，会同时删除IPv4和IPv6地址。
   7. 删除配置错误的静态路由。

      **RMV SRROUTE6**
   8. 删除配置错误的静态路由自动化配置模板。

      **RMV AUTOSCALINGSRROUTE**
   9. 删除配置错误的BFD自动化配置模板。

      **RMV AUTOSCALINGBFD**（BFD echo）/**RMV AUTOSCALINGSRBFD**（BFD双向检测）
   10. 删除配置错误的外联口自动化配置模板。

       **RMV AUTOSCALINGSERVICE**
   11. 重新配置外联口自动化配置模板。

       **ADD AUTOSCALINGSERVICE**
   12. 重新配置BFD自动化配置模板。

       **ADD AUTOSCALINGBFD**（BFD echo）/**ADD AUTOSCALINGSRBFD**（BFD双向检测）
   13. 配置静态路由自动化配置模板。

       **ADD AUTOSCALINGSRROUTE**
   14. 打开自动化配置开关。

       ```
       SET AUTOCONFIG: SWITCHFLAG=TRUE;
       ```

       修改配置后，请重新执行1。
3. 检查BFD会话状态是否为up。

   **DSP BFDSESSION**:;

   - 如果状态为up，请执行5。
   - 如果为其他状态，请执行4。
4. 执行**PING**，查看VNF外联口IP与DCGW接口IP能否互通。

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_Access",DESTIPV6ADDRESS="对端网关地址";
   ```

   - 丢包率为0%，请执行5。
   - 丢包率不是0%，请检查物理接口及连线是否正常。正常后重新执行3。
5. 检查生成的IPv6静态路由是否与规划数据一致。

   ****DSP SRROUTE6****: AFTYPE=ipv6unicast, VRFNAME="VPN\_Access";
   - 如果一致，调测结束。
   - 如果不一致，请执行6。
6. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。