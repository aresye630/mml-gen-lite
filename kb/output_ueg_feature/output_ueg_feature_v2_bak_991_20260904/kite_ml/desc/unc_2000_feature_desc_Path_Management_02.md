# 激活路径管理（适用于SGSN/MME/AMF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活路径管理特性的操作过程。

路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。

**说明** 

适用于SGSN、MME、AMF。

## 必备事项

前提条件

请仔细阅读WSFD-010600 路径管理特性概述。

数据

该操作无需准备数据。

## 操作步骤

1. 配置SGSN/MME GTP-C路径管理。GTP-C路径是用于在UEG与对端之间传输信令消息的路径。

   1. 配置GTP-C路径管理参数。

      **SET GTPPUB**
   2. 配置T3N3参数。

      **SET T3N3**
   3. 配置GTP信息表中管控GTP-C路径状态的时间参数。 一般不要设置，均存在系统初始设置值。

      **SET UGTP**
   4. 配置GTP-C路径自定义配置策略参数。

      **ADD GTPCPATHDP**
2. 配置SGSN GTP-U路径管理。GTP-U路径是用于在UEG与对端之间传输用户数据的路径。

   1. 配置GTP-U路径管理参数。

      **SET GTPUPARA**
   2. 配置用户面控制参数。

      **SET GTPUCTRL**
   3. 配置GTP-U路径自定义配置策略参数。

      **ADD GTPUPATHDP**
3. 配置AMF GTP-C路径管理。

   1. 配置GTP-C路径管理参数。

      **SET GTPCFUNCPARA**
   2. 配置T3N3参数。

      **ADD GTPCT3N3**
   3. 配置GTP-C路径自定义配置策略参数。

      **ADD GTPCPATHMP**

## 任务示例

任务描述

配置SGSN/MME的GTP-C路径管理和SGSN的GTP-U路径管理。具体配置如下：

- GTP-C路径：发送Echo请求间隔为60s，路径数过载门限为80%，路径数过载恢复为75%，路径数拥塞门限为90%，路径数拥塞恢复为85%。同时，GTP版本设置为V0版本，T3定时器设置为7s，发送Echo探测消息最大尝试次数为2次。想减少闪断漫游路径告警的上报，设置钝化系数为3，并将漫游路径告警设置为独立告警，以便于屏蔽。
- GTP-U路径：GTPU路径Echo探测发送间隔为240s，GTPU路径的Echo探测的T3 Response时长为6s，GTPU路径的Echo探测的消息发送次数为2次。路径数过载门限为80%，路径数过载恢复为75%，路径数拥塞门限为90%，路径数拥塞恢复为85%。想减少闪断漫游路径告警的上报，设置钝化系数为3，并将漫游路径告警设置为独立告警，以便于屏蔽。

脚本

- 配置SGSN/MME的GTP-C路径管理。

  //配置GTP-C路径管理参数。

  ```
  SET GTPPUB: ECHOSIG=ALL, EI=60, POTHD=80, PNTHD=75, PCTHD=90, PRTHD=85;
  ```

  //配置T3N3参数。

  ```
  SET T3N3: GTPVER=GTPv0, V0MSGCLS=PM, V0SPMMSGTYPE=ECHO_REQ, T3RES=7, N3REQ=2;
  ```

  //配置GTP-C漫游路径自定义配置策略。

  ```
  ADD GTPCPATHDP: RANGE=ROAMING, PAS_COE=3, GP_ALMID=INDEP;
  ```
- 配置SGSN的GTP-U路径管理。

  //配置GTP-U路径管理参数。

  ```
  ADD GTPUPATHDP: RANGE=ROAMING, PAS_COE=3, GP_ALMID=INDEP;
  ```

  //配置GTP-U漫游路径自定义配置策略。

  ```
  SET GTPUPARA: GTPUUPECHO=ON, GTPUDNECHO=ON, GTPUEI=240, GTPUT3=6, GTPUN3=2, POTHD=80, PNTHD=75, PCTHD=90, PRTHD=85;
  ```