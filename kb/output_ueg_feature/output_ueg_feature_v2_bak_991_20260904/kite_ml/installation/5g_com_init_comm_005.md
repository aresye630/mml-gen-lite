# 修改MTU值

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

修改MTU值为**高危操作**，例如：

- MTU修改可能导致整网分片增多，其他网元的分片重组能力的限制可能导致业务受影响。
- 部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。

**说明** 

网元外联口MTU值和直连下一跳网关（DCGW/路由器等）的接口MTU值必须一致，默认值是1500，如果运营商没有特殊要求和组网要求，建议保持默认值。

如下几种场景下，可参考本页面修改MTU值：

- 配合整网规划修改Fabric平面MTU值时。
- 配合整网规划修改Tunnel接口MTU值时。
- 配合整网规划修改外联口MTU值时。

**说明** 

- 为保证系统正常通信，**网卡MTU****≥Fabric的MTU>主接口的MTU≥子接口的MTU**。
- 建议子接口的MTU和主接口的配置一致。
- 网元实例化完成后，Fabric平面的MTU可以通过命令**SET FABRICMTU**修改。
- 修改硬件网卡的MTU的操作步骤请参考相应的硬件产品手册进行。

## 必备事项

前提条件

请阅读并熟悉IPFD-020201 接口管理特性概述。

数据

修改调整VNF的MTU值，确保通信正常。

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                     | 参数名称              | 取值样例           | 获取方法     | 说明                                                                                          |
|:-----------------------|:------------------|:---------------|:---------|:--------------------------------------------------------------------------------------------|
| SET FABRICMTU          | MTU值（MTUVALUE）    | 1800           | 本端规划     | 设置Fabric平面的MTU值。                                                                            |
| MOD INTERFACE          | 接口名（IFNAME）       | Tunnel6        | 已配置数据中获取 | 设置Tunnel接口MTU值。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。                                           |
| MOD INTERFACE          | 接口最大传输单元（IFMTU）   | 1500           | 全网规划     | 设置Tunnel接口MTU值。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。                                           |
| MOD INTERFACE          | 接口名（IFNAME）       | Ethernet64/0/4 | 全网规划     | 设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。          |
| MOD INTERFACE          | 接口最大传输单元（IFMTU）   | 1500           | 全网规划     | 设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。          |
| MOD INTERFACE          | 接口名（IFNAME）       | Eth-trunk1     | 全网规划     | 设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。 |
| MOD INTERFACE          | 接口最大传输单元（IFMTU）   | 1500           | 全网规划     | 设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。 IPv6接口MTU值通过SET IFIPV6ENABLE命令修改。 |
| MOD AUTOSCALINGSERVICE | 服务名称（SERVICENAME） | ServName_test1 | 已配置数据中获取 | 自动化配置模板名称，可通过LST AUTOSCALINGSERVICE命令查询。                                                    |
| MOD AUTOSCALINGSERVICE | 最大传输单元（MTU）       | 1500           | 全网规划     | 与MOD INTERFACE命令设置的MTU值相同。                                                                  |

文档

获取网设LLD文档。

## 操作步骤

修改Fabric平面的MTU值

1. Fabric平面的MTU值不满足要求时，修改Fabric平面的MTU值。

   NP卡加速场景，不支持通过MML修改Fabric MTU。

   ```
   SET FABRICMTU: MTUVALUE=1800;
   ```

修改Tunnel接口的MTU值

2. Tunnel接口的MTU值不满足要求时，修改Tunnel接口的MTU值。

   ```
   //IPv4 MTU
   MOD INTERFACE:IFNAME="Tunnel6",IFMTU=1500;
   ```

   ```
   //IPv6 MTU
   SET IFIPV6ENABLE:IFNAME="Tunnel6",ENABLEFLAG=TRUE,MTU=1500;
   ```

修改外联口的MTU值

3. Ethernet接口组网时，修改外联口（Ethernet接口做外联口）的MTU值。

   1. 修改外联口主接口的MTU值。

      ```
      //IPv4 MTU
      MOD INTERFACE:IFNAME="Ethernet64/0/4",IFMTU=1500;
      ```

      ```
      //IPv6 MTU
      SET IFIPV6ENABLE:IFNAME="Ethernet64/0/4",ENABLEFLAG=TRUE,MTU=1500;
      ```
   2. **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

      ```
      //IPv4 MTU
      MOD INTERFACE:IFNAME="Ethernet64/0/4.1",IFMTU=1500;
      ```

      ```
      //IPv6 MTU
      SET IFIPV6ENABLE:IFNAME="Ethernet64/0/4.1",ENABLEFLAG=TRUE,MTU=1500;
      ```

4. Eth-trunk接口组网时，修改外联口（Eth-trunk接口做外联口）的MTU值。

   **说明** 

   Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

   1. 修改外联口主接口的MTU值。

      ```
      //IPv4 MTU
      MOD INTERFACE:IFNAME="Eth-trunk1",IFMTU=1500;
      ```

      ```
      //IPv6 MTU
      SET IFIPV6ENABLE:IFNAME="Eth-trunk1",ENABLEFLAG=TRUE,MTU=1500;
      ```
   2. **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

      ```
      //IPv4 MTU
      MOD INTERFACE:IFNAME="Eth-trunk1.100",IFMTU=1500;
      ```

      ```
      //IPv6 MTU
      SET IFIPV6ENABLE:IFNAME="Eth-trunk1.100",ENABLEFLAG=TRUE,MTU=1500;
      ```
5. 自动部署模式时，建议同步修改自动化配置模板中的MTU值。

   **说明** 

   执行本步骤，可避免后续因模板MTU值与接口实际MTU值不一致产生告警ALM-232398849 接口自动化配置失败；后续扩容场景，也可避免新扩容接口仍需参考3/4逐个修改MTU值。

   1. 查询自动配置开关。

      ```
      LST AUTOCONFIG:;
      ```

      自动配置开关，与修改前配置保持一致：
      - “自动配置开关”取值为“是”，请依次执行5.b～5.d。
      - “自动配置开关”取值为“否”，请只执行5.c，不执行其他步骤。
   2. 关闭自动配置开关。

      **注意** 

      执行**DSP OPSASSISTSTATE**命令，直到“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”或者查询无该脚本时，才能关闭自动配置开关。否则可能影响业务。

      ```
      SET AUTOCONFIG:SWITCHFLAG=FALSE;
      ```
   3. 修改自动化配置模板的MTU值。

      ```
      MOD AUTOSCALINGSERVICE: SERVICENAME="ServName_test1", MTU=1500;
      ```
   4. 开启自动配置开关。

      ```
      SET AUTOCONFIG: SWITCHFLAG=TRUE;
      ```

## 验证方法

1. 执行命令**LST FABRICMTU**，查询Fabric平面的MTU值是否与规划值一致。

   ```
   LST FABRICMTU:;
   ```

   - 如果与规划值一致，请执行2。
   - 如果不一致，请检查配置并重新配置，然后执行2。
2. 查询接口的MTU值设置是否与规划值一致。
   1. 执行命令**LST INTERFACE** / **LST IFIPV6ENABLE**，查询接口配置信息，关注接口MTU取值是否与规划值一致。

      ```
      //IPv4 MTU
      LST INTERFACE:IFNAME="Ethernet64/0/4";
      ```

      ```
      //IPv6 MTU
      LST IFIPV6ENABLE:IFNAME="Ethernet64/0/4";
      ```

      - 如果与规划值一致，请执行2.b。
      - 如果不一致，请检查配置并重新配置，然后执行2.b。
   2. 执行命令**DSP IFSTATUS**，查询接口状态是否正常。

      ```
      DSP IFSTATUS:IFNAME="Ethernet64/0/4";
      ```

      - 如果接口状态为UP，且是自动部署模式时，请执行3。
      - 如果接口状态为UP，且是手动部署模式时，请执行4。
      - 如果接口状态为Down，请执行5。
3. 执行命令**LST AUTOSCALINGSERVICE**命令，查询自动配置模板的MTU值是否与规划值一致。

   ```
   LST AUTOSCALINGSERVICE:;
   ```

   - 如果与规划值一致，请执行4。
   - 如果不一致，请检查配置并重新配置，然后执行4。
4. 向接口（Ethernet64/0/4）发送报文长度不大于MTU值的报文，确认是否可以观察到接口进出报文，以及报文是否产生分片。
   - 如果可以查到且没有分片，则接口状态正常，调测结束。
   - 如果未查询到报文或报文产生分片，请执行5。
5. 收集信息并寻求技术支持。

   1. 执行EXP MML命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。