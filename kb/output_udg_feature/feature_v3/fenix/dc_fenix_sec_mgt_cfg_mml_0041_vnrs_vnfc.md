# 配置BGP安全

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

## 操作场景

网络上对BGP协议的攻击方法主要有DoS攻击、注入大量BGP路由、构造错误BGP协议报文、网络报文攻击，为了提升安全性，需要进行BGP的安全加固配置。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

该操作无需准备数据。

## 操作步骤

* 配置MD5认证

  BGP的MD5认证只是为TCP连接设置MD5认证密码，由TCP完成认证。如果认证失败，则不建立TCP连接。

  在“MML命令行-UDG”窗口上执行：

  **MOD BGPPEER**: VRFNAME="VPN实例名称",ADDRESSTYPE="地址类型",PEERADDR="对等体地址",PSWDTYPE=密码类型,PSWDCIPHERTEXT="密码";

  为了保证更好的安全性，建议不要使用MD5算法。
* 配置Keychain认证

  BGP对等体两端必须都配置Keychain认证，且配置的Keychain必须使用相同的加密算法和密码，才能正常建立TCP连接，交互BGP消息。

  在“MML命令行-UDG”窗口上执行：

  **MOD BGPPEER**: VRFNAME="VPN实例名称",ADDRESSTYPE="地址类型",PEERADDR="对等体地址",KEYCHAINNAME="Keychain名称";
* 配置BGP GTSM功能

  配置GTSM功能，通过检测IP报文头中的TTL值是否在一个预先定义好的特定范围内来对设备进行保护。

  在“MML命令行-UDG”窗口上执行：

  **MOD BGPPEER**: VRFNAME="VPN实例名称",ADDRESSTYPE="地址类型",PEERADDR="对等体地址",VALIDTTLHOPS=指定需要检测的TTL跳数值;
* 设置BGP路由超限

  BGP使用邻居路由限定为一个BGP路由器设置允许从其对等体收到的最大路由数量，超限路由被直接丢弃。

  在“MML命令行-UDG”窗口上执行：

  **MOD BGPPEERAF**: VRFNAME="VPN实例名称",AFTYPE=地址族类型,REMOTEADDRESS="IPv4对等体地址",ROUTELIMIT=路由超限阈值;

版权所有 © 华为技术有限公司
