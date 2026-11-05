# 配置SBI接口（N10/N11）

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

**接口介绍**

SMF的服务化接口为Nsmf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。

**表1** 服务化接口与参考点模式对应关系

| 参考点 | 网元间的交互 | 服务化接口 |
| --- | --- | --- |
| N7 | SMF<->PCF | Nsmf、Npcf |
| N10 | SMF<->UDM | Nsmf、Nudm |
| N11 | AMF<->SMF | Namf、Nsmf |
| N40 | SMF<->NCG | Nsmf、Nchf |

**图1** 服务化接口协议栈图

服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。

HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。

TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。

**配置建议**

* SMF的服务化接口业务IP地址不能和SMF其他接口业务IP地址共用。
* SMF的服务化接口端口号没有明确时，使用HTTP知名端口号80。
* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署的NF数量分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81202714 LKV2V6IF01 逻辑接口支持IPv6”。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

* SMF服务化接口数据

  | 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- |
  | **ADD LOGICIP** | IP地址类型（IPVERSION） | IPv4 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Nsmf接口的逻辑IP地址。 |
  |  | IPv4地址（LOGICIPV4） | 10.16.0.6  10.16.0.7 |  |  |
  |  | VPN实例名称（VPNINSTNAME） | VRF\_SBI |  |  |
  |  | 描述（DESC） | FOR Server SBI  FOR Client SBI |  |  |
  | **ADD HTTPLEGRP** | INDEX（索引） | 2 | 本端规划 | 配置Nsmf接口的HTTP本端端点组信息。 |
  | **ADD HTTPLE** | HTTPLE本端实体索引（INDEX） | 3  4 | 本端规划 | 配置HTTP本端端点信息。 |
  |  | HTTP本端实体组标识（HTTPLEGRPIDX） | 2 | 全网规划 | 已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。 |
  |  | 本端实体类型（LETYPE） | SERVER  CLIENT | 本端规划 | - |
  |  | IP类型（IPTYPE） | IPv4 | 全网规划 |  |
  |  | IPv4地址（IPv4） | 10.16.0.6  10.16.0.7 | 全网规划 |  |
  |  | 端口号（PORT） | 8080  - | 全网规划 |  |
  |  | VPN名称（VPNNAME） | VRF\_SBI | 全网规划 |  |
  |  | 是否启用TLS（TLSFLG） | NO | 全网规划 |  |
  | **ADD SBIAPLE** | 索引（INDEX） | 2 | 全网规划 | 配置本端服务化接口接入点信息。 |
  |  | HTTP本端实体组标识（HTTPLEGRPIDX） | 2 | 全网规划 | 已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。 |
  |  | 本端NF类型（NFTYPE） | NFTypeSMF | 全网规划 | - |
* 到NRF的数据

  | 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- |
  | **ADD NRF** | NRF实例名称（NRFINSTANCENAME） | NRF\_Instance\_0  NRF\_Instance\_1 | 全网规划 | 配置NRF信息。  当配置非UUID格式的NRF实例名称时，请提前规划保证各NRF实例名称的前18位字符不能相同。 |
  |  | TLS（TLS） | FALSE | 全网规划 |  |
  |  | 优先级（PRIORITY） | 0  1 | 全网规划 |  |
  | **ADD NRFADDR** | NRF实例名称（NRFINSTANCENAME） | NRF\_Instance\_0  NRF\_Instance\_1 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置NRF的地址信息。 |
  |  | IP地址类型（IPADDRESSTYPE） | IPTypeV4 |  | - |
  |  | Ipv4地址（IPV4ADDRESS） | 172.16.0.7  172.26.0.7 |  | NRF的服务端地址信息。 |
  |  | 端口（PORT） | 8080 | 全网规划 | NRF的服务端端口信息。 |
  | **ADD NRFPARA** | NRF实例名称（NRFINSTANCENAME） | NRF\_Instance\_0  NRF\_Instance\_1 | 本端规划 | 配置NRF协议参数。 |
  |  | 等待时长（WAITINTERVAL） | 5 | 全网规划 |  |
  |  | 最大重传次数（MAXRETRYTIMES） | 3 | 全网规划 |  |
  |  | 心跳是否携带Load信息（LOADCARRYINHB） | FALSE | 与对端协商 |  |
  |  | 订阅流程开关（SUBSCRISWITCH） | ON | 全网规划 |  |
  |  | OAUTH2鉴权开关（OAUTH2SWITCH） | OFF | 全网规划 |  |
  | **ADD SUBCONDITION** | NF类型（NFTYPE） | NfAMF | 全网规划 | 增加订阅的目标NF的条件信息。  说明：  本示例以目标NF为AMF，订阅条件为NfInstanceId，通知事件为NF\_REGISTERED举例。请根据运营商网络实际情况进行配置。 |
  |  | 订阅条件（CONDITION） | NfInstanceId-1 |  |  |
  |  | 通知事件（REQNOTIFEVENT） | NF\_REGISTERED-1 |  |  |
  | **SET LICENSESWITCH** | License项（LICITEM） | LKV2NFDSM01  LKV2NFBSM01  LKV2NFASM01 | 本端规划 | 设置License配置开关**。** |
  |  | 开关（SWITCH） | ENABLE | 本端规划 |  |
  | **ACT NFONLINE** | NF实例标识（NFINSTANCENAME） | SMF\_Instance\_0 | 全网规划 | 激活SMF\_Instance\_0向NRF的注册。 |

文档

获取网设LLD文档。

## 操作步骤

**配置SMF服务化接口数据**

1. 进入“MML命令行-UNC”窗口。
2. **可选：**增加SMF服务化接口的IP地址。当需要通过FQDN信息获取其他NF的IP信息时，无需配置此步骤。

   ```
   ADD LOGICIP:IPVERSION=IPv4, LOGICIPV4="10.16.0.6", VPNINSTNAME="VRF_SBI", DESC="FOR Server SBI";
   ADD LOGICIP:IPVERSION=IPv4, LOGICIPV4="10.16.0.7", VPNINSTNAME="VRF_SBI", DESC="FOR Client SBI";
   ```
3. 配置SMF服务化接口的HTTP本端端点组及其包含的分别作为HTTP服务的服务端和客户端的本端端点信息。

   1. 配置HTTP本端端点组信息。

      ```
      ADD HTTPLEGRP:INDEX=2, DESC="SMF";
      ```
   2. 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

      ```
      ADD HTTPLE:INDEX=3, HTTPLEGRPIDX=2, LETYPE=SERVER, IPTYPE=IPv4, IPV4="10.16.0.6", PORT=8080, VPNNAME="VRF_SBI", TLSFLG=NO, DESC="SMF Server";
      ADD HTTPLE:INDEX=4, HTTPLEGRPIDX=2, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="10.16.0.7", VPNNAME="VRF_SBI", DESC="SMF Client";
      ```
4. 配置SMF服务化接口接入点信息。

   ```
   ADD SBIAPLE:INDEX=2, HTTPLEGRPIDX=2, NFTYPE=NFTypeSMF, DESCRIPTION="SMF";
   ```

**配置到NRF的数据**

如果网络中未部署NRF，则无法执行本步骤，需手工配置SMF与周边NF的逻辑连接，配置步骤参见配置和NF直连。

5. 配置NRF信息。

   当配置非UUID格式的NRF实例名称时，请提前规划保证各NRF实例名称的前18位字符不能相同。

   ```
   ADD NRF:NRFINSTANCENAME="NRF_Instance_0", TLS=FALSE, PRIORITY=0;
   ```
6. 配置NRF的地址信息。

   ```
   ADD NRFADDR:NRFINSTANCENAME="NRF_Instance_0", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="172.16.0.7", PORT=8080;
   ```
7. 配置NRF协议参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

   ```
   ADD NRFPARA:NRFINSTANCENAME="NRF_Instance_0", WAITINTERVAL=5, MAXRETRYTIMES=3, LOADCARRYINHB=FALSE, SUBSCRISWITCH=ON, OAUTH2SWITCH=OFF;
   ADD SUBCONDITION:NFTYPE=NfAMF, CONDITION=NfInstanceId-1, REQNOTIFEVENT=NF_REGISTERED-1;
   ```
8. 当网络中规划了双主或者主备NRF时，需要配置本步骤。双主NRF场景下，NF对接的优先级高的NRF为本地DC的NRF；主备NRF场景下，NF对接的优先级高的NRF为主NRF。

   ```
   ADD NRF:NRFINSTANCENAME="NRF_Instance_1", TLS=FALSE, PRIORITY=1;
   ADD NRFADDR:NRFINSTANCENAME="NRF_Instance_1", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="172.26.0.7", PORT=8080;
   ADD NRFPARA:NRFINSTANCENAME="NRF_Instance_1", WAITINTERVAL=5, MAXRETRYTIMES=3, LOADCARRYINHB=FALSE, SUBSCRISWITCH=ON, OAUTH2SWITCH=OFF;
   ```

   + 请保证已完成NF到双主或者主备NRF的路由数据配置。
   + 请提前规划**ADD NRFPARA**中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF对NRF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考WSFD-114002 NRF双活容灾特性概述中“原理概述”>“可靠性机制”小节。
9. 打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。

   ```
   SET LICENSESWITCH:LICITEM="LKV2NFBSM01", SWITCH=ENABLE;
   SET LICENSESWITCH:LICITEM="LKV2NFASM01", SWITCH=ENABLE;
   SET LICENSESWITCH:LICITEM="LKV2NFDSM01", SWITCH=ENABLE;
   ```
10. 激活SMF向NRF注册。

    ```
    ACT NFONLINE:NFINSTANCENAME="SMF_Instance_0";
    ```

版权所有 © 华为技术有限公司
