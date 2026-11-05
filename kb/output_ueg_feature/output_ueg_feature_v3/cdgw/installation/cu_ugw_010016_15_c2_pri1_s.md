# 配置Pa(N9a/S5-P/S8-P/S2b)接口数据

## 操作场景

运营商在部署5G或4G/5G互操作的分组交换网时新增PSA UPF/PGW-U中的任一独立设备或融合设备，在完成配置UEG到ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG的路由数据后，可在UEG上配置Pa（N9a/S5-P/S8-P/S2b）接口数据使UEG与ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG建立逻辑连接。

* 考虑到4G/5G互操作和平滑演进，5GC需要支持4G/5G融合接入和互操作，因此协议规定了三类网元需要原生融合部署。
  + 用户数据：HSS+UDM融合，保证用户数据一致性。
  + 策略数据：PCRF+PCF融合，保证策略一致性、连续性。
  + 会话管理锚点：SMF+PGW-C融合，UPF+PGW-U融合，锚点不变保证数据连续性。从简化网络拓扑，优化转发路径考虑，一般建议EPC侧SGW-C融合到SMF+PGW-C、SGW-U融合到UPF+PGW-U。

  因此部署4G/5G互操作的网络时，PSA UPF、PGW-U需要融合部署在同一VNF上。
* 考虑到4G/5G互操作时数据锚点不变，PSA UPF+PGW-U融合部署时N9a、S5-P/S8-P的接口地址必须相同，因此UEG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5-P/S8-P接口。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）（风筝S）。
* 请阅读并熟悉特性GWFD-021312 Single IP。

数据

在UEG上配置Pa（N9a/S5-P/S8-P/S2b）接口数据，为UEG与ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG之间的数据路径建立逻辑连接。

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD VPNINST** | VPN实例名（VPNINSTANCE） | VPN\_Pa | 参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取 | 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。 |
| **ADD LOGICINF** | 逻辑接口名称（NAME） | Paif1/1/0 | 参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口”。  本端规划 | UEG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5/S8-P、S2b接口。 |
|  | 逻辑接口的IP版本（IPVERSION） | IPv4 | - | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER\_ALL”，分别配置IPv4和IPv6地址。  需要使用不同的IP地址与ULCL UPF/BP UPF/I-UPF/SGW-U建立逻辑连接时，请规划多个Paif接口。Paif接口编号为Paif1/1/N，N取值范围为0~31。 |
|  | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.1.3.1 | 参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口IP”。  全网规划 |  |
|  | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 |  |
|  | VPN实例名称（VPNINSTANCE） | VPN\_Pa | 参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取 | - |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置Pa（N9a/S5-P/S8-P/S2b）逻辑接口所属的VPN实例。

   ```
   ADD VPNINST: VPNINSTANCE ="VPN_Pa";
   ```

   逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。
3. 配置Pa（N9a/S5-P/S8-P/S2b）逻辑接口。

   ```
   ADD LOGICINF:NAME="Paif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.3.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Pa";
   ```

   UEG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5/S8-P、S2b接口。

## 验证方法

1. 进入“MML命令行-UEG”窗口。
2. 执行**LST LOGICINF**命令，查询逻辑接口信息是否与规划数据一致。
   * 一致，请执行3。
   * 不一致，请参考“操作步骤”重新配置，与规划数据一致后执行3。
3. 执行**SRVPING**命令，调测UEG到ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG的数据通信路径。

   * 如下“LOGICINFNAME”/“SRCIPV4ADDR”/“SRCIPV6ADDR”参数值仅为举例，实际调测时，请注意修改成**LST LOGICINF**查询到的Paif接口数据。
   * 如下“DSTIPV4ADDR”/“DSTIPV6ADDR”参数值仅为举例，实际调测时，请注意修改成对接的ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG地址。

   //IPv4地址：

   ```
   SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="Paif1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.3.1", DSTIPV4ADDR="10.2.3.1";
   ```

   //IPv6地址：

   ```
   SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="Paif1/1/0", IPVERSION=IPv6, SRCIPV6ADDR="FC00::10:1:3:1", DSTIPV6ADDR="FC00::10:2:3:1";
   ```

   * 返回“0.00% packet loss”，表明通信正常，调测结束。
   * 返回“100.00% packet loss”或其他非零丢包率，表明通信异常，请执行4。
4. 执行**SRVTRACERT**命令，查询通信路径中的故障点。

   //IPv4地址：

   ```
   SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="Paif1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.3.1", DSTIPV4ADDR="10.2.3.1";
   ```

   //IPv6地址：

   ```
   SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="Paif1/1/0", IPVERSION=IPv6, SRCIPV6ADDR="FC00::10:1:3:1", DSTIPV6ADDR="FC00::10:2:3:1";
   ```

   * 返回“1 \* \* Request timed out.”，请执行5。
   * 返回“n \* \* Request timed out.”，请联系最后1个地址所属的网元进行处理。
5. 执行**DSP ROUTE**/**DSP ROUTE6**命令，检查是否存在到对端IP的路由。
   * 存在，请执行7。
   * 不存在，请执行6。
6. 请检查外联口IP及路由配置是否正确。

   检查外联口IP及路由配置的详细步骤，请参见组网路由配置。

   * 是，请执行7。
   * 否，请修改配置后执行3。
7. 收集信息并寻求技术支持。

   1. 在OM Portal上创建“UEG用户跟踪”任务，执行3~6并保存报文和查询结果。
   2. 在“MML命令行-UEG”窗口上执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   3. 收集并保存上述所有查询信息。
   4. 查看并收集对端设备配置及接口状态信息。
   5. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司