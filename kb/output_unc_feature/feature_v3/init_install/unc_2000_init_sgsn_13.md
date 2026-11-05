# 配置到SGW的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增SGW或SGSN时，在配置完成SGSN到SGW的路由数据后，可通过配置S4接口数据建立SGSN到SGW的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

| 类别 | 参数名称 | 取值样例 |  | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| **ADD DNSS** | IP地址（IP） | 10.29.147.3 |  | 参见“水平网设LLD文档 ”。 | DNS数据。 |
|  | 域名服务器优先级（PRI） | PRI1 |  |  |  |
| **ADD DNSLE** | IP地址类型（IPT） | IPV4 |  |  |  |
|  | IPv4地址（IPV4） | 10.2.3.1 |  |  |  |
|  | 本地端口号（LOCPORT） | 15001 |  |  |  |
|  | VPN名称（VPNNAME） | VPN\_CN |  |  |  |
| **ADD IPV4DNSH** | 主机名索引（HSINDEX） | 1 |  |  | S-GW解析数据。 |
|  | 主机名（HOSTNAME） | topon.eth1.gw32.nodes |  |  |  |
|  | IPv4地址1（IPV4ADDR1） | 10.100.0.0 |  |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1(1) |  |  |  |
| **ADD DNSN** | FQDN（FQDN） | RAC01.LAC01.RAC.EPC.EPC.MNC001.MCC308.3GPPNETWORK.ORG |  |  |  |
|  | 主机名索引（HSINDEX） | 1 |  |  |  |
|  | 网元类型（ENTITY） | SGW |  |  |  |
|  | 接口类型（INTYPE） | S4 |  |  |  |
|  | S5接口协议类型（S5PROTOCOL） | GTP |  |  |  |
|  | S8接口协议类型（S8PROTOCOL） | GTP |  |  |  |
|  | 优先级（PRIORITY） | 10 |  |  |  |
|  | 权重（WEIGHT） | 104 |  |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 配置数据请参考配置到S-GW的数据。

## 验证方法

调测数据请参考配置到S-GW的数据。

版权所有 © 华为技术有限公司
