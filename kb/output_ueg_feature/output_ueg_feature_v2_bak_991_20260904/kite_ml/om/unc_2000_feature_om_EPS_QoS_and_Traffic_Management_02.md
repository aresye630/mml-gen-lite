# 激活QoS与流量管理（适用于PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

通过配置QoS与流量管理，可实现以下需求：

- 为了保证在资源紧缺时，运营商能够为高优先级用户优先分配资源。
- 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。

QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项

前提条件

- 完成配置普通APN。

数据

| 类别               | 参数名称                         | 取值样例          | 获取方法      | 说明                                                                |
|:-----------------|:-----------------------------|:--------------|:----------|:------------------------------------------------------------------|
| SET QOSREMARK    | 下行标记（DOWNLINK）               | ENABLE        | 本端规划      | 配置整机使能用户的上下行Remark功能。                                             |
| SET QOSREMARK    | 上行标记（UPLINK）                 | ENABLE        | 本端规划      | 配置整机使能用户的上下行Remark功能。                                             |
| SET CPQOSGLOBAL  | Qos Profile名（QOSPROFILENAME） | gp1           | 本端规划      | 配置基于全局的QoS Profile。                                               |
| ADD EPSREMARK    | Qos Profile名（QOSPROFILENAME） | globalqos gp1 | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | QCI（QCI）                     | 1             | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | ARP的优先级别（ARPPL）              | 1             | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | 标记类型（REMARKTYPE）             | DSCP          | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | DSCP（DSCP）                   | EF            | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | S1U DSCP配置开关（S1UDSCPSWITCH）  | ENABLE        | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD EPSREMARK    | S1-U DSCP（S1UDSCP）           | EF            | 全网规划      | 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。                             |
| ADD QOSPROFILE   | QoS名称（QOSPROFILENAME）        | gp1           | 本端规划      | 配置QosProfile，并进入Qos实例。                                            |
| ADD CPAPN        | APN名称（APN）                   | apn           | 本端规划      | 配置指定APN实例。                                                        |
| SET CPAPNQOSATTR | APN名称（APN）                   | apn           | 从已配置数据中获取 | 为该APN实例绑定QOSPROFILE。 如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。 |
| SET CPAPNQOSATTR | 有Qos Profile（HASQOSPROFILE）  | ENABLE        | 从已配置数据中获取 | 为该APN实例绑定QOSPROFILE。 如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。 |
| SET CPAPNQOSATTR | Qos Profile名（QOSPROFILENAME） | gp1           | 本端规划      | 为该APN实例绑定QOSPROFILE。 如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。 |
| SET QCI2ARP      | 标准QCI（QCI）                   | 9             | 全网规划      | 配置QCI和ARP的对应关系。                                                   |
| SET QCI2ARP      | ARP的可抢占能力（ARPPCI）            | 0             | 全网规划      | 配置QCI和ARP的对应关系。                                                   |
| SET QCI2ARP      | ARP的优先级别（ARPPL）              | 1             | 全网规划      | 配置QCI和ARP的对应关系。                                                   |
| SET QCI2ARP      | QCI的被抢占能力（ARPPVI）            | 1             | 全网规划      | 配置QCI和ARP的对应关系。                                                   |
| SET DEFEPSQOS    | QCI值（QOSCLASSID）             | 6             | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | ARP值(ARPVALUE)               | 1             | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 上行保证带宽(千比特/秒)（GBRUL）         | 230           | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 下行保证带宽(千比特/秒)（GBRDL）         | 200           | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 下行最大带宽(千比特/秒)（MBRDL）         | 300           | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 上行最大带宽(千比特/秒)（MBRUL）         | 300           | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 下行APN AMBR(千比特/秒)（APNAMBRDL） | 1000          | 本端规划      | 配置EPS QoS纠错参数。                                                    |
| SET DEFEPSQOS    | 上行APN AMBR(千比特/秒)（APNAMBRUL） | 1000          | 本端规划      | 配置EPS QoS纠错参数。                                                    |

## 操作步骤

- 配置基于全局的EPS QoS到DSCP/ToS的映射关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置整机使能用户的上下行Remark功能。

     ****SET QOSREMARK****
  3. 配置基于全局的QoS Profile。

     **SET CPQOSGLOBAL**
  4. 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

     **ADD EPSREMARK**
- **可选：**配置基于APN的EPS QoS到DSCP/ToS的映射关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置整机使能用户的上下行Remark功能。

     ****SET QOSREMARK****
  3. 配置QosProfile。

     **ADD QOSPROFILE**
  4. 配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

     ****ADD EPSREMARK****
  5. 配置指定AP实例。

     **ADD CPAPN**
  6. 为该APN实例绑定QOSPROFILE。

     **SET CPAPNQOSATTR**
- 配置QCI和ARP的对应关系。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置QCI和ARP的对应关系。

     **SET QCI2ARP**
- 配置EPS QoS纠错参数。
  1. 进入“MML命令行-UEG”窗口。
  2. 配置EPS QoS纠错参数。

     **SET DEFEPSQOS**

## 任务示例

任务描述

- 配置基于全局的EPS QoS到DSCP/ToS的映射关系。
- 配置基于APN的EPS QoS到DSCP/ToS的映射关系。
- 配置QCI和ARP的对应关系。

脚本

- 配置基于全局的EPS QoS到DSCP/ToS的映射关系。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  //配置整机使能用户的上下行Remark功能。

  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```

  //配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

  ```
  LST CPQOSGLOBAL:;
  ADD EPSREMARK:QOSPROFILENAME="globalqos", QCI=1,ARPPL=1,REMARKTYPE=DSCP,DSCP=EF,S1UDSCPSWITCH=ENABLE,S1UDSCP=EF;
  ```

- 配置基于APN的EPS QoS到DSCP/ToS的映射关系。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  //配置整机使能用户的上下行Remark功能。

  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```

  //配置QosProfile，并进入QoS实例。

  ```
  ADD QOSPROFILE:QOSPROFILENAME="gp1";
  ```

  //配置在EPC架构下，QoS参数到IP报文头中的DSCP/ToS的映射规则。

  ```
  ADD EPSREMARK:QOSPROFILENAME="gp1",QCI=1,ARPPL=1,REMARKTYPE=DSCP,DSCP=EF,S1UDSCPSWITCH=ENABLE,S1UDSCP=EF;
  ```

  //查找APN实例。

  ```
  LST CPAPN:;
  ```

  //为该APN实例绑定QOSPROFILE。

  ```
  SET CPAPNQOSATTR:APN="apn",HASQOSPROFILE=ENABLE,QOSPROFILENAME="gp1";
  ```
- 配置QCI和ARP的对应关系。

  //配置QCI和ARP的对应关系。

  ```
  SET QCI2ARP:QCI=9,ARPPCI=0,ARPPL=1,ARPPVI=1;
  ```