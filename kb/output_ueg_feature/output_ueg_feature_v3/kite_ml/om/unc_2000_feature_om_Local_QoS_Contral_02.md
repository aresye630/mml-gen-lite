# 激活本地QOS控制（适用于SGW-C/PGW-C）

* 操作场景
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

运营商根据UEG本地配置的QoS参数对用户数据进行控制。

适用于SGW-C、PGW-C。

## 必备事项

前提条件

* 请仔细阅读GWFD-022303 本地QOS控制特性概述。
* 完成配置普通APN **ADD CPAPN**。
* 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET LICENSESWITCH** | LICITEM | LKV3W9LQOS12 | 本端规划 | 配置License配置开关 |
|  | SWITCH | ENABLE |  |  |
| **ADD EPSSUBQOS** | QCI（QCI） | 1 | 本端规划 | 配置4G用户的签约QoS属性。 |
|  | ARPPL（ARP的优先级别） | 2 |  |  |
|  | AMBRDL（下行APN AMBRR） | 1111 |  |  |
|  | AMBRUL（上行APN AMBRR） | 2222 |  |  |
|  | SUBQOSINDEX（用户QOS索引） | 200 |  |  |
| **SET CPQOSGLOBAL** | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 配置全局的QoS信息。 |
|  | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） |  |  |
|  | EPS用户QoS索引（EPSSUBQOS） | 200 |  |  |
| **SET DEFEPSQOS** | QOSCLASSID（QCI值） | 1 | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
|  | ARPVALUE（ARP值） | 1 |  |  |
|  | GBRDL（下行保证带宽） | 200bit/s |  |  |
|  | GBRUL（上行保证带宽） | 230bit/s |  |  |
|  | MBRDL（下行最大带宽） | 300bit/s |  |  |
|  | MBRUL（上行最大带宽） | 300bit/s |  |  |
|  | APNAMBRDL（下行APN AMBR） | 1000bit/s |  |  |
|  | APNAMBRUL（上行APN AMBR） | 1000bit/s |  |  |
| **SET QCI2ARP** | QCI（标准QCI） | 1 | 本端规划 | 可选：配置ARP和QCI的对应关系 |
|  | ARPPCI（ARP的可抢占能力） | 0 |  |  |
|  | ARPPL（ARP的优先级别） | 1 |  |  |
|  | ARPPVI（QCI的被抢占能力） | 0 |  |  |
| **ADD QOSPROFILE** | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | QosProfile的配置信息。 |
|  | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） |  |  |
|  | EPS用户QoS索引（EPSSUBQOS） | 200 |  |  |
| **ADD EPSQOSACTION** | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
|  | QCI（QCI值） | 1 |  |  |
|  | GBRDL（下行保证带宽） | 256bit/s |  |  |
|  | GBRDLACTION（超过下行保证带宽的处理） | DEGRADE(降级) |  |  |
|  | GBRUL（上行保证带宽） | 128bit/s |  |  |
|  | GBRULACTION（超过上行保证带宽的处理） | DEGRADE(降级) |  |  |
|  | MBRDL（下行最大带宽） | 384bit/s |  |  |
|  | MBRDLACTION  （超过下行最大带宽的处理） | DEGRADE(降级) |  |  |
|  | MBRUL（上行最大带宽） | 192bit/s |  |  |
|  | MBRULACTION  （超过上行最大带宽的处理） | DEGRADE(降级) |  |  |
| **ADD CPAPN** | APN（APN名称） | apn1 | 本端规划 | 指定APN实例。 |
| **SET CPAPNQOSATTR** | APN（APN名称） | apn1 | 本端规划 | 为APN实例绑定QosProfile。 |
|  | HASQOSPROFILE（是否配置QosProfile） | ENABLE |  |  |
|  | QOSPROFILENAME（QoS Profile名） | qos1 |  |  |

## 操作流程

如果APN下绑定了Qos-profile，则使用Qos-profile下的规则；否则使用QosGlobal下的规则。

全局和APN绑定Qos-profile控制方式相同，都可绑定本地签约QoS，具体如下：获取绑定的Qos-profile，根据Qos-profile下绑定的**ADD EPSQOSACTION**配置，根据QCI对应的带宽/THP门限进行比较，如果超过则根据动作进行降级还是拒绝用户接入。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. **可选**：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值

   **SET EPSQCI2PRER8**
4. **可选**：更改缺省的ARP和标准QCI的对应关系

   **SET QCI2ARP**
5. **可选**：配置本地签约的QoS信息。

   **ADD EPSSUBQOS**
6. 配置EPS QoS缺省QoS参数（用于纠错）。

   **SET DEFEPSQOS**
7. 设置全局的QoS信息。

   **SET CPQOSGLOBAL**
8. 配置基于APN的QoS策略。

   * 配置指定APN实例下的QosProfile名称，并进入QoS实例。

     **ADD QOSPROFILE**
   * 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

     **ADD EPSQOSACTION**
   * 配置APN实例。

     **ADD CPAPN**
   * 为APN实例绑定QoS profile。

     **SET CPAPNQOSATTR**

## 任务示例

任务描述

UEG对用户携带的QoS进行控制，然后对用户流量进行监管。

脚本

* 打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;
  ```
* **可选**：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值。

  ```
  SET EPSQCI2PRER8:QCI=4,TRAFFICCLASS=CONVERSATIONAL,THP=NORMAL,SIGNALIND=OPTIMIZE,SRCSTATDESC=SPEECH;
  ```
* **可选**：更改缺省的ARP和标准QCI的对应关系

  ```
  SET QCI2ARP:QCI=1,ARPPCI=0,ARPPL=1,ARPPVI=0;
  ```
* **可选**：配置本地签约的QoS信息。

  ```
  ADD EPSSUBQOS: SUBQOSINDEX=200, QCI=5, ARPPL=10, AMBRDL=564110, AMBRUL=300000;
  ```
* 配置基于EPS缺省QoS参数（用于纠错）。

  ```
  SET DEFEPSQOS: QOSCLASSID=1, ARPVALUE=1, GBRDL=200, GBRUL=230, MBRDL=300, MBRUL=300, APNAMBRDL=1000, APNAMBRUL=1000;
  ```
* 配置基于全局的EPS QoS信息。

  ```
  SET CPQOSGLOBAL:QOSPROFILENAME="qos2",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=200;
  ```
* 配置基于APN的QoS。

  //配置指定APN实例下的QosProfile名称，并进入QoS实例。

  ```
  ADD QOSPROFILE:QOSPROFILENAME="qos1",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=200;
  ```

  //配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

  ```
  ADD EPSQOSACTION:QOSPROFILENAME="qos1",QCI=1,GBRDL=256,GBRDLACTION=DEGRADE,GBRUL=128,GBRULACTION=DEGRADE,MBRDL=384,
  MBRDLACTION=DEGRADE,MBRUL=192,MBRULACTION=DEGRADE;
  ```

  //进入指定APN实例。

  ```
  ADD CPAPN:APN="apn1";
  ```

  //为该APN实例绑定QosProfile。

  ```
  SET CPAPNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="qos1";
  ```

版权所有 © 华为技术有限公司
