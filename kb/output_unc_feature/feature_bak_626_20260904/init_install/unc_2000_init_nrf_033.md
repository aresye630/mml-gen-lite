# 配置SBI接口

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

**接口介绍**

NRF的服务化接口为Nnrf。

**图1** 服务化接口协议栈图

服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。

**说明** 

HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。

TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。

**配置建议**

- NRF的服务化接口端口号没有明确时，使用HTTP知名端口号80。
- 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
- 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别            | 参数名称                      | 取值样例                          | 获取方法                              | 说明                                      |
|:--------------|:--------------------------|:------------------------------|:----------------------------------|:----------------------------------------|
| ADD LOGICIP   | 逻辑IP地址类型（IPVERSION）       | IPV4                          | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Nnrf接口的逻辑IP地址。                        |
| ADD LOGICIP   | 逻辑IPv4地址（LOGICIPV4）       | 172.16.0.7 172.16.0.8         | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Nnrf接口的逻辑IP地址。                        |
| ADD LOGICIP   | VPN实例名称（VPNINSTNAME）      | VRF_SBI                       | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Nnrf接口的逻辑IP地址。                        |
| ADD LOGICIP   | 描述（DESC）                  | FOR Server SBI FOR Client SBI | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Nnrf接口的逻辑IP地址。                        |
| ADD HTTPLEGRP | 索引（INDEX）                 | 3                             | 本端规划                              | 配置Nnrf接口的HTTP本端端点组信息。                   |
| ADD HTTPLE    | HTTPLE本端实体索引（INDEX）       | 5 6                           | 本端规划                              | 配置作为HTTP服务的服务端和客户端的本端端点信息。              |
| ADD HTTPLE    | HTTP本端实体组标识（HTTPLEGRPIDX） | 3                             | 本端规划                              | 已通过ADD HTTPLEGRP配置，可以通过LST HTTPLEGRP查询。 |
| ADD HTTPLE    | 本端实体类型（LETYPE）            | SERVER CLIENT                 | 全网规划                              | -                                       |
| ADD HTTPLE    | IP类型（IPTYPE）              | IPv4                          | 全网规划                              | -                                       |
| ADD HTTPLE    | IPv4地址（IPv4）              | 172.16.0.7 172.16.0.8         | 全网规划                              | -                                       |
| ADD HTTPLE    | 端口号（PORT）                 | 8080 -                        | 全网规划                              | -                                       |
| ADD HTTPLE    | VPN名称（VPNNAME）            | VRF_SBI                       | 本端规划                              | -                                       |
| ADD HTTPLE    | 是否启用TLS（TLSFLG）           | NO                            | 全网规划                              | -                                       |
| ADD SBIAPLE   | 索引（INDEX）                 | 3                             | 全网规划                              | 配置Nnrf接入点信息。                            |
| ADD SBIAPLE   | HttpLEGRP索引（HTTPLEGRPIDX） | 3                             | 全网规划                              | 已通过ADD HTTPLEGRP配置，可以通过LST HTTPLEGRP查询。 |
| ADD SBIAPLE   | NF类型（NFTYPE）              | NFTypeNRF                     | 全网规划                              | -                                       |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. **可选：**增加NRF服务化接口的IP地址。当需要通过FQDN信息获取其他NF的IP信息时，无需配置此步骤。

   ```
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.7", VPNINSTNAME="VRF_SBI", DESC="FOR Server SBI";
   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.8", VPNINSTNAME="VRF_SBI", DESC="FOR Client SBI";
   ```
3. 配置NRF服务化接口的HTTP信息。
   1. 配置HTTP本端端点组信息。

      ```
      ADD HTTPLEGRP: INDEX=3, DESC="NRF";
      ```
   2. 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

      ```
      ADD HTTPLE: INDEX=5,HTTPLEGRPIDX=3, LETYPE=SERVER, IPTYPE=IPv4, IPV4="172.16.0.7", PORT=8080, VPNNAME="VRF_SBI", TLSFLG=NO, DESC="NRF Server";
      ADD HTTPLE: INDEX=6,HTTPLEGRPIDX=3, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="172.16.0.8", VPNNAME="VRF_SBI", DESC="NRF Client";
      ```
4. 配置NRF服务化接口的接入点信息。

   ```
   ADD SBIAPLE: INDEX=3, HTTPLEGRPIDX=3, NFTYPE=NFTypeNRF, DESCRIPTION="NRF";
   ```
5. **可选：**配置HTTP属性。在超大报文场景下，可以通过合理设置接收HTTP响应/请求消息体的超时时间、HTTP响应/请求消息体的最大大小、请求消息中JSON数据的最大叶子节点个数等参数，避免发送/请求报文不完整，导致业务处理异常。

   ```
   SET HTTPCONF: CLIENTRCVRSPTMT=15, SERVERRCVBDTMT=15, SERVERSNDRSPTMT=15, MAXBODYSIZE=10, MAXJSONLEAFNUM=100000;
   ```