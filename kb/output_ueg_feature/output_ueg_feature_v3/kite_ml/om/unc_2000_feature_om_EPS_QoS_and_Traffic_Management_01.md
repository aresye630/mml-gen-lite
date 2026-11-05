# 激活QoS与流量管理（适用于SMF）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

通过配置QoS与流量管理，可实现以下需求：

* 保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。
* 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。

QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项

前提条件

* 完成配置普通APN。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****SET QOSREMARK**** | 下行标记（DOWNLINK） | ENABLE | 本端规划 | 配置整机使能用户的上下行Remark功能。 |
|  | 上行标记（UPLINK） | ENABLE |  |  |
| **SET CPQOSGLOBAL** | Qos Profile名（QOSPROFILENAME） | gp1 | 本端规划 | 配置基于全局的QoS Profile。 |
| **ADD 5GCREMARK** | Qos Profile名（QOSPROFILENAME） | globalqos  gp1 | 全网规划 | 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。 |
|  | 5QI（FIVEQI） | 1 |  |  |
|  | ARP的优先级别（ARPPL） | 1 |  |  |
|  | 标记类型（REMARKTYPE） | DSCP |  |  |
|  | DSCP（DSCP） | EF |  |  |
|  | N3 DSCP配置开关（N3DSCPSWITCH） | ENABLE |  |  |
|  | N3 DSCP（N3DSCP） | EF |  |  |
| **ADD QOSPROFILE** | QoS名称（QOSPROFILENAME） | gp1 | 本端规划 | 配置QosProfile，并进入Qos实例。 |
| **ADD CPAPN** | APN名称（APN） | apn | 本端规划 | 配置指定APN实例。 |
| **SET CPAPNQOSATTR** | APN名称（APN） | apn | 从已配置数据中获取 | 为该APN实例绑定QOSPROFILE。  如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。 |
|  | 有Qos Profile（HASQOSPROFILE） | ENABLE | 本端规划 |  |
|  | Qos Profile名（QOSPROFILENAME） | gp1 | 本端规划 |  |
| **SET QCI2ARP** | 标准QCI（QCI） | 9 | 全网规划 | 配置5QI和ARP的对应关系。 |
|  | ARP的可抢占能力（ARPPCI） | 0 |  |  |
|  | ARP的优先级别（ARPPL） | 1 |  |  |
|  | QCI的被抢占能力（ARPPVI） | 1 |  |  |
| ****SET 5GCQOSCORRT**** | 下行Session AMBR(千比特/秒)（AMBRDL） | 20000 | 本端规划 | 配置5G QoS纠错参数。 |
|  | 上行Session AMBR(千比特/秒)（AMBRUL） | 20000 |  |  |
|  | 5QI值（FIVEQI） | 5 |  |  |
|  | ARP值（ARPVALUE） | 3 |  |  |
|  | 上行保证带宽(千比特/秒)（GFBRUL） | 4000 |  |  |
|  | 下行保证带宽(千比特/秒)（GFBRDL） | 4000 |  |  |
|  | 下行最大带宽(千比特/秒)（MFBRDL） | 5000 |  |  |
|  | 上行最大带宽(千比特/秒)（MFBRUL） | 5000 |  |  |
|  | 5QI优先级（QOS5QIPL） | 10 |  |  |

## 操作步骤

* 配置基于全局的3GPP QoS到DSCP/ToS的映射关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置整机使能用户的上下行Remark功能。

     ****SET QOSREMARK****
  3. 配置基于全局的QoS Profile。

     **SET CPQOSGLOBAL**
  4. 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

     **ADD 5GCREMARK**
* 配置基于APN的3GPP QoS到DSCP/ToS的映射关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置整机使能用户的上下行Remark功能。

     ****SET QOSREMARK****
  3. 配置QosProfile。

     **ADD QOSPROFILE**
  4. 配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

     ****ADD 5GCREMARK****
  5. 配置指定APN实例。

     **ADD CPAPN**
  6. 为该APN实例绑定QOSPROFILE。

     **SET CPAPNQOSATTR**
* 配置5QI和ARP的对应关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置5QI和ARP的对应关系。

     **SET QCI2ARP**
* 配置5G QoS纠错参数。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置5G QoS纠错参数。

     ****SET 5GCQOSCORRT****

## 任务示例

任务描述

* 配置基于全局的3GPP QoS到DSCP/ToS的映射关系。
* 配置基于APN的3GPP QoS到DSCP/ToS的映射关系。
* 配置5QI和ARP的对应关系。
* 配置QoS纠错参数。

脚本

* 配置基于全局的3GPP QoS到DSCP/ToS的映射关系。

  //配置整机使能用户的上下行Remark功能。

  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```

  //配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

  ```
  SET CPQOSGLOBAL:QOSPROFILENAME="globalqos";
  ADD 5GCREMARK:QOSPROFILENAME="globalqos", FIVEQI=1,ARPPL=1,REMARKTYPE=DSCP,DSCP=EF,N3DSCPSWITCH=ENABLE,N3DSCP=EF;
  ```

* 配置基于APN的3GPP QoS到DSCP/ToS的映射关系。

  //配置整机使能用户的上下行Remark功能。

  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```

  //配置QosProfile，并进入Qos实例。

  ```
  ADD QOSPROFILE:QOSPROFILENAME="gp1";
  ```

  //配置在5GC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

  ```
  ADD 5GCREMARK:QOSPROFILENAME="gp1",FIVEQI=1,ARPPL=1,REMARKTYPE=DSCP,DSCP=EF,N3DSCPSWITCH=ENABLE,N3DSCP=EF;
  ```

  //查找APN实例。

  ```
  LST CPAPN:;
  ```

  //为指定APN实例绑定QOSPROFILE。

  ```
  SET CPAPNQOSATTR:APN="apn",HASQOSPROFILE=ENABLE,QOSPROFILENAME="gp1";
  ```
* 配置5QI和ARP的对应关系。

  //配置5QI和ARP的对应关系。

  ```
  SET QCI2ARP:QCI=9,ARPPCI=0,ARPPL=1,ARPPVI=1;
  ```
* 配置QoS纠错参数。

  //配置QoS纠错参数。

  ```
  SET 5GCQOSCORRT:FIVEQI=5, QOS5QIPL=10, ARPVALUE=3, AMBRDL=20000,AMBRUL=20000,GFBRUL=4000,GFBRDL=4000,MFBRUL=5000,MFBRDL=5000;
  ```

版权所有 © 华为技术有限公司
