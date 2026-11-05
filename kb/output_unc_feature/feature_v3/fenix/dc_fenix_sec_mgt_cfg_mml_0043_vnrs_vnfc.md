# 配置MPLS LDP安全

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

## 操作场景

MD5（Message-Digest Algorithm 5）是RFC 1321定义的国际标准摘要密码算法。MD5的典型应用是针对一段信息计算出对应的信息摘要，从而防止信息被篡改。MD5信息摘要是通过不可逆的字符串变换算法产生的，结果唯一。因此，不管信息内容在传输过程中发生任何形式的改变，只要重新计算就会产生不同的信息摘要，接收端就可以由此判定收到的是一个不正确的报文。

Keychain是一种增强型加密算法，类似于MD5，Keychain也是针对同一段信息计算出对应的信息摘要，实现LDP报文防篡改校验。Keychain允许用户定义一组密码，形成一个密码串，并且分别为每个密码指定加解密算法（包括MD5，SHA-1等）及密码使用的有效时间。

为了保证更好的安全性，建议不要使用MD5和SHA-1算法。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

该操作无需准备数据。

## 操作步骤

* 对所有对等体配置LDP MD5认证。

  在“MML命令行-UNC”窗口上执行：

  **MOD LDPINSTANCE**: VRFNAME="VPN实例名称", LSRID="实例的LSR ID", AUTHENMODE=MODE\_ENABLE, AUTHENTYPE=MD5, MD5PASSWORD="LDP全局MD5密码";
* 对所有对等体配置Keychain认证。

  在“MML命令行-UNC”窗口上执行：

  **MOD LDPINSTANCE**: VRFNAME="VPN实例名称", LSRID="实例的LSR ID", AUTHENMODE=MODE\_ENABLE, AUTHENTYPE=KEYCHAIN, KEYCHAINNAME="LDP全局KeyChain名字";

版权所有 © 华为技术有限公司
