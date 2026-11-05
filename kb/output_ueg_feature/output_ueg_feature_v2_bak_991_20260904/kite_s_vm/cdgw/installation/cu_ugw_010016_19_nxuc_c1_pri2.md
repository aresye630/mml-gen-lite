# 配置Nxuc接口数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

UEG作为UPF，与MPF对接时，需要配置Nxuc接口与MPF通过VXLAN（VXLAN-GPE）隧道互通。

本页面仅给出Nxuc接口的配置指导。VXLAN隧道及分流到MPF的规则的配置，请参见配置VXLAN隧道及分流规则。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
- 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别           | 参数名称                       | 取值样例            | 获取方法                                                         | 说明                                                       |
|:-------------|:---------------------------|:----------------|:-------------------------------------------------------------|:---------------------------------------------------------|
| ADD VPNINST  | VPN实例名（VPNINSTANCE）        | VPN_Nxuc        | 参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。 | 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。          |
| ADD LOGICINF | 逻辑接口名称（NAME）               | Nxucif1/1/0     | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口”。                | 一个VNF上最多可以配置32个Nxuc接口，最后一个数字取值范围是0～31。                   |
| ADD LOGICINF | 逻辑接口的IP版本（IPVERSION）       | IPV4            | -                                                            | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。 |
| ADD LOGICINF | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.1.8.1        | 参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口IP”。              | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。 |
| ADD LOGICINF | 逻辑接口的IPv4掩码1（IPV4MASK1）    | 255.255.255.255 | 固定取值                                                         | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。 |
| ADD LOGICINF | VPN实例名称（VPNINSTANCE）       | VPN_Nxuc        | 参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。 | -                                                        |

文档

获取网设LLD文档。

## 操作步骤

配置Nxuc接口IP地址及VPN实例

1. 进入“MML命令行-UEG”窗口。
2. 配置Nxuc逻辑接口所属的VPN实例。

   ```
   ADD VPNINST: VPNINSTANCE ="VPN_Nxuc";
   ```

   **说明** 

   逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。
3. 配置Nxuc逻辑接口。

   ```
   ADD LOGICINF:NAME="Nxucif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.8.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Nxuc";
   ```

## 验证方法

1. 执行**SRVPING**命令，查看Nxuc与MPF之间的逻辑接口IP能否互通。

   ```
   SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="Nxucif1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.8.1", DSTIPV4ADDR="10.2.8.1";
   ```

   - 如果收到MPF的响应且响应报文中有成功收发包的个数，表明连接正常，调测结束。
   - 如果连续出现timeout，表明连接异常，请执行2。
2. 执行**PING**命令，查看Nxuc对应的外联口与MPF的外联口IP能否互通。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_Nxuc",SOURCEIPV4ADDRESS="Nxuc对应的外联口IP",DESTIPV4ADDRESS="Nxua对应的外联口IP";
   ```

   - 如果收到MPF的响应且响应报文中有成功收发包的个数，请执行3。
   - 如果连续出现timeout，表明连接异常，请执行4。
3. 检查直连路由器上是否存在到MPF逻辑接口IP的路由，下一跳是外联口IP。
   - 是，请执行5。
   - 否，请联系路由器工程师，增加相关路由后重新调测。
4. 请参考配置VNF侧IP路由数据，修正配置后请执行1。

   重新调测仍存在问题，请执行5。
5. 收集信息并寻求技术支持。
   1. 在“MML命令行-UEG”窗口上执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。