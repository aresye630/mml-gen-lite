# 配置Sa/N3/S1-U接口数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

部署MEC解决方案时，新增UEG作为UL CL UPF+辅锚点UPF或主锚点UPF时，在完成配置UEG到无线(R)AN侧的路由数据后，可在UEG上配置Sa/N3/S1-U接口数据使UEG与无线(R)AN侧建立逻辑连接。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
- 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）（风筝S）/逻辑接口介绍（风筝M）/逻辑接口介绍（风筝L）。
- 请阅读并熟悉特性GWFD-021312 Single IP。

数据

在UEG上配置Sa/N3/S1-U接口数据，为UEG与eNodeB/gNodeB之间的数据路径建立逻辑连接。

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别           | 参数名称                       | 取值样例            | 获取方法                                                                                                                   | 说明                                                                                                                       |
|:-------------|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| ADD VPNINST  | VPN实例名（VPNINSTANCE）        | VPN_Access      | 参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。 已配置数据中获取 | 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。                                                                          |
| ADD LOGICINF | 逻辑接口名称（NAME）               | Saif1/1/0       | 参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口”。 本端规划                                                                              | N3、S1-U接口可独立配置，也可使用抽象接口Sa进行合一配置（推荐使用合一配置）。两种方式不可同时配置，如已配置独立接口，则配置抽象接口时系统会提示失败；如已配置抽象接口，则配置独立接口时系统会提示失败。 最后一位数字取值范围是0~31。 |
| ADD LOGICINF | 逻辑接口的IP版本（IPVERSION）       | IPv4            | -                                                                                                                      | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。                                                                 |
| ADD LOGICINF | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.1.1.1        | 参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口IP”。 全网规划                                                                            | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。                                                                 |
| ADD LOGICINF | 逻辑接口的IPv4掩码1（IPV4MASK1）    | 255.255.255.255 | 固定取值                                                                                                                   | 如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。                                                                 |
| ADD LOGICINF | VPN实例名称（VPNINSTANCE）       | VPN_Access      | 参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。 请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。 已配置数据中获取 | -                                                                                                                        |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置Sa/N3/S1-U逻辑接口所属的VPN实例。

   ```
   ADD VPNINST: VPNINSTANCE ="VPN_Access";
   ```

   **说明** 

   逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。
3. 配置Sa/N3/S1-U逻辑接口。

   ```
   ADD LOGICINF:NAME="Saif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Access";
   ```

## 验证方法

1. 进入“MML命令行-UEG”窗口。
2. 执行**LST LOGICINF**命令，查询逻辑接口信息是否与规划数据一致。
   - 一致，请执行3。
   - 不一致，请参考“操作步骤”重新配置，与规划数据一致后执行3。
3. 执行**SRVPING**命令，调测UEG到eNodeB/gNodeB的数据通信路径。

   **说明** 

   - 如下“LOGICINFNAME”/“SRCIPV4ADDR”/“SRCIPV6ADDR”参数值仅为举例，实际调测时，请注意修改成**LST LOGICINF**查询到的Saif/N3if/S1-uif接口数据。
   - 如下“DSTIPV4ADDR”/“DSTIPV6ADDR”参数值仅为举例，实际调测时，请注意修改成对接的eNodeB/gNodeB地址。

   //IPv4地址：

   ```
   SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="Saif1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.1", DSTIPV4ADDR="10.2.1.1";
   ```

   //IPv6地址：

   ```
   SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="Saif1/1/0", IPVERSION=IPv6, SRCIPV6ADDR="FC00::10:1:1:1", DSTIPV6ADDR="FC00::10:2:1:1";
   ```

   - 返回“0.00% packet loss”，表明通信正常，调测结束。
   - 返回“100.00% packet loss”或其他非零丢包率，表明通信异常，请执行4。
4. 执行**SRVTRACERT**命令，查询通信路径中的故障点。

   //IPv4地址：

   ```
   SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="Saif1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.1", DSTIPV4ADDR="10.2.1.1";
   ```

   //IPv6地址：

   ```
   SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="Saif1/1/0", IPVERSION=IPv6, SRCIPV6ADDR="FC00::10:1:1:1", DSTIPV6ADDR="FC00::10:2:1:1";
   ```

   - 返回“1 \* \* Request timed out.”，请执行5。
   - 返回“n \* \* Request timed out.”，请联系最后1个地址所属的网元进行处理。
5. 执行**DSP ROUTE**/**DSP ROUTE6**命令，检查是否存在到对端IP的路由。
   - 存在，请执行7。
   - 不存在，请执行6。
6. 请检查外联口IP及路由配置是否正确。

   检查外联口IP及路由配置的详细步骤，请参见组网路由配置。

   - 是，请执行7。
   - 否，请修改配置后执行3。
7. 收集信息并寻求技术支持。

   1. 在OM Portal上创建“UEG用户跟踪”任务，执行3~6并保存报文和查询结果。
   2. 在“MML命令行-UEG”窗口上执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   3. 收集并保存上述所有查询信息。
   4. 查看并收集对端设备配置及接口状态信息。
   5. 收集归纳所有信息并联系华为技术支持解决。