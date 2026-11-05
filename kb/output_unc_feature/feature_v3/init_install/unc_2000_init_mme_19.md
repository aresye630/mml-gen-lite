# 配置到MME的数据（Sdup接口）

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，在配置完成MME到MME的路由数据后，可通过配置Sdup接口数据建立MME到MME的逻辑连接。

Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的用户信息备份及恢复，提升VoLTE业务的可靠性。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIPMCR**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 配置业务IP参数。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.80.57.1 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  |
| **ADD SDAPLE** | IPTYPE（IP地址类型） | TPTADDR\_TYPE\_IPV4 |  | 增加Sdup接口业务IP地址。 |
|  | LEIPV4（IPv4地址） | 10.80.57.1 |  |  |
| **SET SDAPINTF** | DETITVL（Sdup接口探测间隔时长） | 30 |  | 设置Sdup接口参数。 |
|  | ALMTHRSHD（Sdup链路告警阈值） | 2 |  |  |
| **ADD IPV4DNSH** | HSINDEX（主机名索引） | 7 |  | 配置Sdup接口MME的解析数据。 |
|  | HOSTNAME（主机名） | eth1.ring.mmec01.list001.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org |  |  |
|  | ADDRSECTION（地址区间号） | SECTION1 |  |  |
|  | IPV4ADDR1（IPv4地址1） | 10.80.57.1 |  |  |
|  | IPV4ADDR2（IPv4地址2） | 10.80.57.2 |  |  |
| **ADD DNSN** | FQDN（FQDN） | ring.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org |  |  |
|  | HSINDEX（主机名索引） | 7 |  |  |
|  | ENTITY（网元类型） | MME |  |  |
|  | INTYPE（接口类型） | Sdup |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 增加基础业务IP。

   ```
   ADD SERVICEIPMCR: IPVERSION=IPv4, SERVICEIPV4="10.80.57.1", VPNINSTNAME="VPN_CN";
   ADD SERVICEIPMCR: IPVERSION=IPv4, SERVICEIPV4="10.80.57.2", VPNINSTNAME="VPN_CN";
   ```
3. 增加Sdup接口业务IP地址。

   ```
   ADD SDAPLE: IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.80.57.1";
   ADD SDAPLE: IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="10.80.57.2";
   ```
4. **可选：**设置Sdup接口参数。

   ```
   SET SDAPINTF: DETITVL=30, ALMTHRSHD=2;
   ```
5. **可选：**配置Sdup接口MME的解析数据。链式备份环中的所有MME均需要配置该备份链所有MME的解析信息。假设备份环“list001.mmegi8001”上有mmec01和mmec02两个MME，配置如下：

   ```
   ADD IPV4DNSH: HSINDEX=7, HOSTNAME="eth1.ring.mmec01.list001.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.80.57.1", IPV4ADDR2="10.80.57.2";
   ADD IPV4DNSH: HSINDEX=8, HOSTNAME="eth1.ring.mmec02.list001.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.80.58.1", IPV4ADDR2="10.80.58.2";
   ADD DNSN: FQDN="ring.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org", HSINDEX=7, ENTITY=MME, INTYPE=Sdup;
   ADD DNSN: FQDN="ring.mmegi8001.mme.epc.mnc002.mcc640.3gppnetwork.org", HSINDEX=8, ENTITY=MME, INTYPE=Sdup;
   ADD DNSN: FQDN="ring.mmec01.list001.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org", HSINDEX=7, ENTITY=MME, INTYPE=Sdup;
   ADD DNSN: FQDN="ring.mmec02.list001.mmegi8001.mme.epc.mnc001.mcc640.3gppnetwork.org", HSINDEX=8, ENTITY=MME, INTYPE=Sdup;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 观察告警台，确认是否有未恢复的ALM-85000 USN容灾关系异常告警。

   * **预期结果：**无此告警。
   * **异常结果：**上报了此告警。异常处理过程参见ALM-85000 USN容灾关系异常。
3. 观察告警台，确认是否有未恢复的ALM-85002 容灾USN不可达告警。
   * **预期结果：**无此告警。
   * **异常结果：**上报了此告警。异常处理过程参见ALM-85002 容灾USN不可达。
4. 观察告警台，确认是否有未恢复的ALM-85001 Sdup链路故障告警。
   * **预期结果：**无此告警。
   * **异常结果：**上报了此告警。

     异常处理过程参见ALM-85001 Sdup链路故障。
5. 验证MME链式备份特性。

   如下验证过程在“一次呼叫恢复”模式下进行。

   1. 将容灾功能运行模式修改成“调测模式”。

      **SET RESTOFUNC**:
   2. 配置允许使用备份功能用户的IMSI号段，用于指定测试用户。

      **ADD RESTOUSR**
   3. 测试用户开机附着到S-USN覆盖的网络。
   4. 在S-USN上查询MME链式备份关系。

      **DSP RESTORELAT**
   5. 在R-USN上查询测试用户的备份信息。

      **DSP RESTOMMCTX**

      **DSP RESTOSMCTX**

      **预期结果**：在R-USN上可以查看到用户的备份信息
   6. 在S-USN上删除此用户，模拟S-USN故障。

      **RMV SERVUSR**
   7. 拨打此用户。

      **预期结果：**用户一次被叫成功。
   8. 删除测试用户。

      **RMV RESTOUSR**
   9. 将容灾功能运行模式修改成“运行模式”。

      **SET RESTOFUNC**

版权所有 © 华为技术有限公司
