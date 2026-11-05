# 配置PGW-U/UPF与PDN/DN/UDG之间的GRE隧道

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

- 当用户通过WAP（Wireless Application Protocol）访问PDN/DN时，可以采用PGW-U/UPF与WAP网关之间建立GRE隧道的方式构建VPN。

具体组网如图1所示。

**图1** GRE隧道连通与PDN/DN组网图

- PGW-U/UPF与WAP网关之间建立GRE VPN，实现用户的业务访问。
- PGW-U/UPF与WAP网关之间必须支持Loopback接口建立GRE隧道。
- 当PGW-U/UPF外联口之间采用BGP/OSPF动态路由时，PGW-U/UPF的Loopback接口的IP地址网段必须对外发布。
- 用户的上行数据采用静态路由，出接口为Tunnel接口，对端接入设备必须配置到用户终端网段的静态路由。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

- VNF与网络实体之间的网络环境已经构建完成。

数据

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                | 参数名称                   | 取值样例                  | 获取方法     | 说明                                                                                                                 |
|:------------------|:-----------------------|:----------------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| ADD INTERFACE     | 接口名称（IFNAME）           | LoopBack1             | 本端规划     | -                                                                                                                  |
| ADD GRETUNNEL     | 隧道名称(TNLNAME)          | Tunnel1               | 本端规划     | -                                                                                                                  |
| ADD GRETUNNEL     | 隧道类型(TNLTYPE)          | gre                   | 本端规划     | 隧道地址采用IPv4地址类型时选择“gre”，隧道地址采用IPv6地址类型时选择“gre6”。                                                                    |
| ADD GRETUNNEL     | IPv4源类型(SRCTYPE)       | if_name               | 固定取值     | -                                                                                                                  |
| ADD GRETUNNEL     | 源接口名称(SRCIFNAME)       | LoopBack1             | 已配置数据中获取 | GRE隧道通过Loopback接口的IP地址作为隧道的源地址。                                                                                    |
| ADD GRETUNNEL     | 目的IPv4地址(DSTIPADDR)    | 10.4.4.11             | 全网规划     | GRE隧道的目的地址。                                                                                                        |
| ADD IPBINDVPN     | VPN名字(VRFNAME)         | VRF_Internet          | 已配置数据中获取 | Loopback接口和GRE隧道绑定的VPN必须与N6接口的VPN一致。                                                                               |
| ADD IPBINDVPN     | 接口名称（IFNAME）           | LoopBack1Tunnel1      | 已配置数据中获取 | -                                                                                                                  |
| ADD IFIPV4ADDRESS | 接口名称（IFNAME）           | LoopBack1Tunnel1      | 已配置数据中获取 | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是loopback接口和Tunnel地址标识。 |
| ADD IFIPV4ADDRESS | 接口IPv4地址（IFIPADDR）     | 10.3.3.11 10.10.1.201 | 全网规划     | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是loopback接口和Tunnel地址标识。 |
| ADD IFIPV4ADDRESS | 接口IPv4地址掩码（SUBNETMASK） | 255.255.255.255       | 全网规划     | 如果规划外联口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一外联口配置IPv4和IPv6地址。 此处规划的IP地址是loopback接口和Tunnel地址标识。 |
| ADD NETWORKROUTE  | VPN名字(VRFNAME)         | VRF_Internet          | 已配置数据中获取 | BGP动态协议场景中需要将Loopback接口路由引入到BGP动态路由表中。                                                                             |
| ADD NETWORKROUTE  | AFTYPE                 | ipv4uni               | 全网规划     | BGP动态协议场景中需要将Loopback接口路由引入到BGP动态路由表中。                                                                             |
| ADD NETWORKROUTE  | NETWORKADDRESS         | 10.3.3.11             | 全网规划     | BGP动态协议场景中需要将Loopback接口路由引入到BGP动态路由表中。                                                                             |
| ADD NETWORKROUTE  | MASKLEN                | 32                    | 全网规划     | BGP动态协议场景中需要将Loopback接口路由引入到BGP动态路由表中。                                                                             |
| ADD SRROUTE       | AFTYPE                 | ipv4unicast           | 全网规划     | -                                                                                                                  |
| ADD SRROUTE       | PREFIX                 | 10.0.0.172            | 全网规划     | -                                                                                                                  |
| ADD SRROUTE       | MASKLENGTH             | 32                    | 全网规划     | -                                                                                                                  |
| ADD SRROUTE       | VRFNAME                | VRF_Internet          | 已配置数据中获取 | -                                                                                                                  |
| ADD SRROUTE       | DESTVRFNAME            | VRF_Internet          | 与对端协商    | -                                                                                                                  |
| ADD SRROUTE       | IFNAME                 | Tunnel1               | 已配置数据中获取 | -                                                                                                                  |
| MOD GRETUNNEL     | 隧道名称(TNLNAME)          | Tunnel1               | 已配置数据中获取 | -                                                                                                                  |
| MOD GRETUNNEL     | 隧道类型(TNLTYPE)          | gre                   | 本端规划     | -                                                                                                                  |
| MOD GRETUNNEL     | CHECKSUMEN             | TRUE                  | 固定取值     | -                                                                                                                  |
| MOD GRETUNNEL     | KEEPALVEN              | TRUE                  | 固定取值     | -                                                                                                                  |

## 操作步骤

1. 已通过配置BGP over 静态路由+BFD（IPv4）完成外联口的IP路由配置。
2. 配置LoopBack接口并绑定VPN实例，其中VPN实例与对接PDN/DN的外联口绑定的VPN一致。

   ```
   ADD INTERFACE:IFNAME="LoopBack1";
   ADD IPBINDVPN:IFNAME="LoopBack1",VRFNAME="VRF_Internet";
   ADD IFIPV4ADDRESS: IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
   ```
3. LoopBack接口路由。

   采用BGP路由协议时，执行以下命令将LoopBack接口路由引入BGP。

   ```
   ADD NETWORKROUTE: VRFNAME="VRF_Internet", AFTYPE=ipv4uni, NETWORKADDRESS="10.3.3.11", MASKLEN=32;
   ```
4. 配置Tunnel隧道。

   ```
   ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11",DSTVPNNAME="VRF_Internet";
   ADD IPBINDVPN:IFNAME="Tunnel1",VRFNAME="VRF_Internet";
   ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.201", SUBNETMASK="255.255.255.0", ADDRTYPE=main;
   ```

   **说明** 

   为了不影响GRE隧道收发报文性能，建议使用**MOD INTERFACE**命令配置GRE Tunnel的MTU值，该MTU值小于等于（出接口的MTU值-GRE头的长度），GRE头封装格式为：GRE header + 外层IP header。
5. 配置隧道间静态路由。

   ```
   ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.0.0.172" ,MASKLENGTH=32,VRFNAME="VRF_Internet",DESTVRFNAME="VRF_Internet",IFNAME="Tunnel1",PREFERENCE=60,BFDENABLE=FALSE,TAG=0,DHCPENABLE=FALSE;
   ```
6. **可选：**当配置GRE隧道时，使能隧道端到端校验功能。

   ```
   MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;
   ```
7. **可选：**当配置GRE隧道时，使能隧道识别关键字功能。

   ```
   MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="*****";
   ```

   **说明** 

   如果在隧道两端设置识别关键字，则必须指定相同的识别关键字（即“GREKEY”参数值）；或隧道两端都不设置识别关键字。

   “GREKEYEN”参数设置为“TRUE”时，表明使能隧道识别关键字功能；“GREKEYEN”参数设置为“FALSE”时，表明不使能隧道识别关键字功能。
8. 当配置GRE隧道时，使能隧道Keepalive功能。

   ```
   MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
   ```

   **说明** 

   - “Keepalive报文发送周期（KEEPALVPERIOD）”不配置，则默认为5秒；
   - “不可达计数器参数（KEEPALVRETRYCNT）”不配置，则默认为3次。

## 验证方法

1. 在设备上Ping对端网元，查看设备到对端网元的隧道是否正常连通。

   **PING**:IPVERSION=IP协议版本号, DESTIPV4ADDRESS="目的IPv4地址", PACKETCOUNT=发包数, PACKETSIZE=报文字节数, INTERVAL=报文间隔(ms), TIMEOUT=超时时间(ms), TTL=TTL值;

   - **预期结果**：收到对端网元的响应。调测结束。

     ```
     PING: IPVERSION=IPv4, DESTIPV4ADDRESS="10.0.0.172";

       PING 10.0.0.172: 56  字节，按CTRL_Q中断

         答复从 10.0.0.172: 字节数=56 顺序号=1 生存时间=255 往返时间=1 毫秒

         答复从 10.0.0.172: 字节数=56 顺序号=2 生存时间=255 往返时间=1 毫秒

         答复从 10.0.0.172: 字节数=56 顺序号=3 生存时间=255 往返时间=1 毫秒

         答复从 10.0.0.172: 字节数=56 顺序号=4 生存时间=255 往返时间=1 毫秒

         答复从 10.0.0.172: 字节数=56 顺序号=5 生存时间=255 往返时间=1 毫秒

       --- 10.0.0.172 ping 统计 ---
         发送包数: 5
         接收包数: 5
         0.00% 包丢失
         往返时间 最小/平均/最大 = 1/1/1 毫秒

     共有9个报告
     ---    END
     ```
   - **异常结果**：没有收到对端网元的响应。

     异常处理过程请参见GRE隧道故障处理定位思路。
2. 检查GRE隧道配置是否正确。

   **LST INTERFACE**:IFNAME="接口名";

   **LST GRETUNNEL**:TNLNAME="隧道名称";

   **预期结果**：查询结果与规划值一致。