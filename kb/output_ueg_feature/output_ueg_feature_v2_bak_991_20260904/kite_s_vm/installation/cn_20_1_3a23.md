# 配置静态路由+BFD组网（IPv4）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

VNF与对端设备可通过静态路由绑定静态BFD探测的方式进行组网连接。

在网络拓扑结构比较简单时，通常使用静态路由方式组网，合理的静态路由可以改进网络性能，并为业务保证带宽。同时，利用BFD双向/单臂Echo转发检测机制为链路提供双向/单向、轻负荷且持续时间短的快速检测功能，提高链路可靠性。

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

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别规划在2个CSLB上，每个CSLB上各规划2个子接口负荷分担承载流量。实际场景可根据网设规划进行适配。

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                | 参数名称                           | 取值样例                                                                | 获取方法                                                         | 说明                                                                                                                                 |
|:------------------|:-------------------------------|:--------------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| ADD L3VPNINST     | VPN实例名称（VRFNAME）               | VPN_Access                                                          | 参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。                                                                                         |
| ADD VPNINSTAF     | 地址族类型（AFTYPE）                  | ipv4uni                                                             | -                                                            | IPv4组网场景下，该参数选择ipv4uni。                                                                                                            |
| MOD INTERFACE     | 接口名称（IFNAME）                   | Ethernet66/0/4 Ethernet66/0/5 Ethernet67/0/4 Ethernet67/0/5         | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。                  | -                                                                                                                                  |
| ADD INTERFACE     | 子接口名字（IFNAME）                  | Ethernet66/0/4.1 Ethernet66/0/5.1 Ethernet67/0/4.1 Ethernet67/0/5.1 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。                 | 非SR-IOV bonding组网需要规划。                                                                                                             |
| ADD INTERFACE     | 接口名称（IFNAME）                   | Eth-trunk1 Eth-trunk2                                               | 本端规划                                                         | SR-IOV bonding组网需要规划。                                                                                                              |
| ADD INTERFACE     | 接口名称（IFNAME）                   | Eth-trunk1.1 Eth-trunk1.2 Eth-trunk2.1 Eth-trunk2.2                 | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子端口”。                 | SR-IOV bonding组网需要规划。                                                                                                              |
| MOD TRUNKIF       | 接口名称（IFNAME）                   | Eth-trunk1 Eth-trunk2                                               | 已规划数据中获取                                                     | SR-IOV bonding组网下需要规划。 需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。                                                                         |
| MOD TRUNKIF       | 工作模式（WORKMODE）                 | Manual                                                              | 固定值                                                          | SR-IOV bonding组网下需要规划。 需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。                                                                         |
| ADD TRUNKMEMBER   | Trunk接口名（TRUNKIFNAME）          | Eth-trunk1 Eth-trunk2                                               | 已规划数据中获取                                                     | SR-IOV bonding组网下需要规划。 需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。                                                                         |
| ADD TRUNKMEMBER   | 成员接口名（MEMBERIFNAME）            | Ethernet66/0/4 Ethernet66/0/5 Ethernet67/0/4 Ethernet67/0/5         | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 端口”。                  | SR-IOV bonding组网下需要规划。 需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。                                                                         |
| ADD IPBINDVPN     | VPN名字(VRFNAME)                 | VPN_Access                                                          | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VRF”。                 | -                                                                                                                                  |
| ADD ETHSUBIF      | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100 200                                                             | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > VLAN序号”。              | 此处以双平面为例，单平面组网时，只需规划一条数据（例如只规划VLAN 100）。                                                                                           |
| ADD IFIPV4ADDRESS | 接口IPv4地址（IFIPADDR）             | 192.168.89.2 192.168.89.34 192.168.89.3 192.168.89.35               | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > IP”。                  | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是与网关互通的外联口IP。 此处以27位掩码为例进行介绍，具体以网设规划为准。 |
| ADD IFIPV4ADDRESS | 接口IPv4地址掩码（SUBNETMASK）         | 255.255.255.224                                                     | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 子网掩码”。                | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是与网关互通的外联口IP。 此处以27位掩码为例进行介绍，具体以网设规划为准。 |
| SET BFD           | 激活BFD（BFDENABLE）               | TRUE                                                                | 参见“5G Core LLD文档 > 路由设计 > 其他路由设计信息 > BFD设计 > BFD是否使能”。       | 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。                                                                      |
| ADD BFDSESSION    | 会话名称（SESSNAME）                 | BfdName21 BfdName22 BfdName23 BfdName24                             | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话名称”。                     | -                                                                                                                                  |
| ADD BFDSESSION    | IP协议版本号（ADDRTYPE）              | IPv4                                                                | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > IP协议版本号”。                  | -                                                                                                                                  |
| ADD BFDSESSION    | 本地标识符（LOCALDISCR）              | 121 122 123 124                                                     | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 本地标识符”。                    | VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。                                                                            |
| ADD BFDSESSION    | 远端标识符（REMOTEDISCR）             | 221 222 223 224                                                     | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 远端标识符”。                    | VNF上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。 “ONEARMECHO”为“TRUE”时，不需要规划远端标识符。                                           |
| ADD BFDSESSION    | IPv4目的地址（DESTADDR4）            | 192.168.89.1 192.168.89.33                                          | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 对端IP地址”。                   | 参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                          |
| ADD BFDSESSION    | 链路类型（LINKTYPE）                 | IP                                                                  | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 链路类型”。                     | 参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                          |
| ADD BFDSESSION    | IPv4会话创建方式（CREATETYPE4）        | SESS_STATIC                                                         | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 会话创建方式”。                   | 参数“DESTADDR4”是网关的接口IP，此处用于检测目的IP能否正常接收报文。                                                                                          |
| ADD BFDSESSION    | 出接口名称（IFNAME）                  | Ethernet66/0/4.1 Ethernet66/0/5.1 Ethernet67/0/4.1 Ethernet67/0/5.1 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。                    | 非SR-IOV bonding组网需要规划。                                                                                                             |
| ADD BFDSESSION    | 出接口名称（IFNAME）                  | Eth-trunk1.1 Eth-trunk1.2 Eth-trunk2.1 Eth-trunk2.2                 | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 出接口名称”。                    | SR-IOV bonding组网需要规划。                                                                                                              |
| ADD BFDSESSION    | VPN实例名称（VRFNAME）               | VPN_Access                                                          | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > VPN实例名称”。                  | VNF所在硬件设备直连DC-GW时“ONEARMECHO”取值为“TRUE”，直连PE时“ONEARMECHO”取值为“FALSE”。                                                                |
| ADD BFDSESSION    | IPv4单臂Echo（ONEARMECHO）         | FALSE                                                               | 参见“5G Core LLD文档 > 路由设计 > BFD会话 > 单臂Echo”。                   | VNF所在硬件设备直连DC-GW时“ONEARMECHO”取值为“TRUE”，直连PE时“ONEARMECHO”取值为“FALSE”。                                                                |
| ADD SRROUTE       | VPN实例名称 （VRFNAME）              | VPN_Access                                                          | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > VRF名称”。                   | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。 参数“NEXTHOP”是网关的接口IP。      |
| ADD SRROUTE       | 路由前缀（PREFIX）                   | 192.168.53.4 192.168.54.4                                           | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 路由前缀”。                    | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。 参数“NEXTHOP”是网关的接口IP。      |
| ADD SRROUTE       | 路由掩码长度（MASKLENGTH）             | 32                                                                  | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 掩码长度”。                    | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。 参数“NEXTHOP”是网关的接口IP。      |
| ADD SRROUTE       | 路由下一跳（NEXTHOP）                 | 192.168.89.1 192.168.89.33                                          | 已规划数据中获取                                                     | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。 参数“NEXTHOP”是网关的接口IP。      |
| ADD SRROUTE       | 静态BFD会话名（SESSIONNAME）          | BfdName21 BfdName22 BfdName23 BfdName24                             | 参见“5G Core LLD文档 > 路由设计 > 静态路由设计 > 静态BFD会话”。                 | SR-IOV bonding单平面组网时，需要规划1个路由下一跳地址。 双平面组网时，2个路由下一跳IP地址在不同网段。 参数“PREFIX”是目的IP，规划的是用于传输N3接口报文时，此处是基站的IP地址。 参数“NEXTHOP”是网关的接口IP。      |

文档

获取网设LLD文档。

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_Access";
   ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv4uni;
   ```

   **说明** 

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. 非SR-IOV bonding组网时，配置外联口IP地址。

   1. 查询接口名，确认CSLB上可使用的外联口的接口类型和接口编号。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet66/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet67/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet67/0/5",IFADMINSTATUS=up;
      ```
   3. 配置以太网子接口。

      ```
      ADD INTERFACE:IFNAME="Ethernet66/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet66/0/5.1";
      ADD INTERFACE:IFNAME="Ethernet67/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet67/0/5.1";
      ```
   4. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Ethernet66/0/4.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Ethernet66/0/5.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Ethernet67/0/4.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Ethernet67/0/5.1",VRFNAME="VPN_Access";
      ```
   5. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Ethernet66/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet66/0/5.1",VLANTYPEVID=200;
      ADD ETHSUBIF:IFNAME="Ethernet67/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet67/0/5.1",VLANTYPEVID=200;
      ```

      **说明** 

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   6. 配置外联口IP地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/4.1",IFIPADDR="192.168.89.2",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5.1",IFIPADDR="192.168.89.34",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Ethernet67/0/4.1",IFIPADDR="192.168.89.3",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Ethernet67/0/5.1",IFIPADDR="192.168.89.35",SUBNETMASK="255.255.255.224";
      ```

      **说明** 

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. SR-IOV bonding组网时，配置外联口IP地址。

   1. 查询接口名，确认CSLB上可使用的外联口的接口类型和接口编号。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet66/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet66/0/5",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet67/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet67/0/5",IFADMINSTATUS=up;
      ```
   3. 配置以太Trunk接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1";
      ADD INTERFACE:IFNAME="Eth-trunk2";
      ```
   4. 配置Eth-trunk接口的工作模式并添加成员端口。

      ```
      MOD TRUNKIF:IFNAME="Eth-Trunk1",WORKMODE=Manual;
      MOD TRUNKIF:IFNAME="Eth-Trunk2",WORKMODE=Manual;
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet66/0/4";
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet66/0/5";
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk2",MEMBERIFNAME="Ethernet67/0/4";
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk2",MEMBERIFNAME="Ethernet67/0/5";
      ```
   5. 配置以太Trunk子接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1.1";
      ADD INTERFACE:IFNAME="Eth-trunk1.2";
      ADD INTERFACE:IFNAME="Eth-trunk2.1";
      ADD INTERFACE:IFNAME="Eth-trunk2.2";
      ```
   6. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Eth-trunk1.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Eth-trunk1.2",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Eth-trunk2.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Eth-trunk2.2",VRFNAME="VPN_Access";
      ```
   7. 在以太Trunk子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Eth-trunk1.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Eth-trunk1.2",VLANTYPEVID=200;
      ADD ETHSUBIF:IFNAME="Eth-trunk2.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Eth-trunk2.2",VLANTYPEVID=200;
      ```

      **说明** 

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   8. 配置外联口IP地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="Eth-trunk1.1",IFIPADDR="192.168.89.2",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Eth-trunk1.2",IFIPADDR="192.168.89.34",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Eth-trunk2.1",IFIPADDR="192.168.89.3",SUBNETMASK="255.255.255.224";
      ADD IFIPV4ADDRESS:IFNAME="Eth-trunk2.2",IFIPADDR="192.168.89.35",SUBNETMASK="255.255.255.224";
      ```

      **说明** 

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
4. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```
5. 新建BFD会话。

   **说明** 

   - 必须全局使能BFD功能后该命令才可生效。
   - 如下为双向BFD探测的配置，采用单臂Echo时，将如下配置中的“ONEARMECHO”设置为“TRUE”，并删除“REMOTEDISCR”即可。

   - 非SR-IOV bonding组网场景下：
     - 双向BFD探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,REMOTEDISCR=221,IFNAME="Ethernet66/0/4.1";
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,REMOTEDISCR=222,IFNAME="Ethernet66/0/5.1";
       ADD BFDSESSION: SESSNAME="BfdName23",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=123,REMOTEDISCR=223,IFNAME="Ethernet67/0/4.1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,REMOTEDISCR=224,IFNAME="Ethernet67/0/5.1";
       ```
     - BFD单臂Echo探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,IFNAME="Ethernet66/0/4.1";
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,IFNAME="Ethernet66/0/5.1";
       ADD BFDSESSION: SESSNAME="BfdName23",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=123,IFNAME="Ethernet67/0/4.1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,IFNAME="Ethernet67/0/5.1";
       ```
   - SR-IOV bonding组网场景下：
     - 双向BFD探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,REMOTEDISCR=221,IFNAME="Eth-trunk1.1";
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,REMOTEDISCR=222,IFNAME="Eth-trunk1.2";
       ADD BFDSESSION: SESSNAME="BfdName23",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=123,REMOTEDISCR=223,IFNAME="Eth-trunk2.1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=FALSE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,REMOTEDISCR=224,IFNAME="Eth-trunk2.2";
       ```
     - BFD单臂Echo探测

       ```
       ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,IFNAME="Eth-trunk1.1";
       ADD BFDSESSION: SESSNAME="BfdName22",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=122,IFNAME="Eth-trunk1.2";
       ADD BFDSESSION: SESSNAME="BfdName23",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.1",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=123,IFNAME="Eth-trunk2.1";
       ADD BFDSESSION: SESSNAME="BfdName24",ADDRTYPE=IPv4,CREATETYPE4=SESS_STATIC,ONEARMECHO=TRUE,DESTADDR4="192.168.89.33",LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=124,IFNAME="Eth-trunk2.2";
       ```
6. 配置静态路由并绑定BFD会话。
   - 非SR-IOV bonding组网场景下：

     ```
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Ethernet66/0/4.1",SESSIONNAME="BfdName21";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Ethernet66/0/5.1",SESSIONNAME="BfdName22";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Ethernet67/0/4.1",SESSIONNAME="BfdName23";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Ethernet67/0/5.1",SESSIONNAME="BfdName24";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Ethernet66/0/4.1",SESSIONNAME="BfdName21";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Ethernet66/0/5.1",SESSIONNAME="BfdName22";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Ethernet67/0/4.1",SESSIONNAME="BfdName23";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Ethernet67/0/5.1",SESSIONNAME="BfdName24";
     ```
   - SR-IOV bonding组网场景下：

     ```
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Eth-trunk1.1",SESSIONNAME="BfdName21";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Eth-trunk1.2",SESSIONNAME="BfdName22";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Eth-trunk2.1",SESSIONNAME="BfdName23";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.53.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Eth-trunk2.2",SESSIONNAME="BfdName24";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Eth-trunk1.1",SESSIONNAME="BfdName21";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Eth-trunk1.2",SESSIONNAME="BfdName22";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.1",IFNAME="Eth-trunk2.1",SESSIONNAME="BfdName23";
     ADD SRROUTE:VRFNAME="VPN_Access",AFTYPE=ipv4unicast,PREFIX="192.168.54.4",MASKLENGTH=32,DESTVRFNAME="VPN_Access",NEXTHOP="192.168.89.33",IFNAME="Eth-trunk2.2",SESSIONNAME="BfdName24";
     ```

   **说明** 

   - 如果需要为静态路由绑定静态BFD会话，通过**ADD SRROUTE**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。
   - 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

     需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。

## 验证方法

1. 查看接口状态及信息是否与规划数据一致。

   ```
   LST INTERFACE:;
   ```

   ```
   LST IFIPV4ADDRESS:;
   ```

   ```
   LST IFIPV6ADDRESS:;
   ```

   ```
   LST IPBINDVPN:;
   ```

   - 如果一致，请执行2。
   - 如果不一致，请先删除错误的配置，然后参考“操作步骤”重新配置。
2. 检查BFD会话状态是否为up。

   **DSP BFDSESSION**:;

   - 如果状态为up，请执行4。
   - 如果为其他状态，请执行3。
3. 执行**PING**，查看VNF外联口IP与DCGW接口IP能否互通。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_Access",DESTIPV4ADDRESS="对端网关地址";
   ```

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_Access",DESTIPV6ADDRESS="对端网关地址";
   ```

   - 丢包率为0%，请执行5。
   - 丢包率不是0%，请检查物理接口及连线是否正常。正常后重新执行2。
4. 检查生成的IPv4静态路由是否与规划数据一致。

   ```
   DSP SRROUTE: AFTYPE=ipv4unicast, VRFNAME="VPN_Access";
   ```

   ```
   DSP SRROUTE6: AFTYPE=ipv6unicast, VRFNAME="VPN_Access";
   ```

   - 如果一致，调测结束。
   - 如果不一致，请执行5。
5. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。