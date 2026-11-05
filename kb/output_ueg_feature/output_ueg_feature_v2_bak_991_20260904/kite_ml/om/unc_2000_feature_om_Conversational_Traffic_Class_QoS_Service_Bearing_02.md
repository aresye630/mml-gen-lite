# 激活会话类QoS保证（适用于SGW-C/PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。

**说明** 

适用于SGW-C、PGW-C。

## 必备事项

前提条件

- 完成配置普通APN **ADD CPAPN**。
- 完成加载License。

数据

| 类别               | 参数名称                            | 取值样例                 | 获取方法   | 说明                                          |
|:-----------------|:--------------------------------|:---------------------|:-------|:--------------------------------------------|
| SET CPQOSGLOBAL  | QOSPROFILENAME (QoS Profile名)   | qos1                 | 本端规划   | 配置全局的QoS信息。                                 |
| SET CPQOSGLOBAL  | BINDEPSSUBQOS（EPS用户QOS）         | ENABLE               | 本端规划   | 配置全局的QoS信息。                                 |
| SET CPQOSGLOBAL  | EPSSUBQOS（EPS用户QOS索引）           | 1                    | 本端规划   | 配置全局的QoS信息。                                 |
| SET DEFEPSQOS    | QOSCLASSID（QCI值）                | 1                    | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | ARPVALUE（ARP值）                  | 1                    | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | GBRDL (下行GBR(千比特/秒))            | 200bit/s             | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | GBRUL（上行保证带宽）                   | 230bit/s             | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | MBRDL（下行最大带宽）                   | 300bit/s             | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | MBRUL（上行最大带宽）                   | 300bit/s             | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | APNAMBRDL（下行APN AMBR）           | 1000bit/s            | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| SET DEFEPSQOS    | APNAMBRUL（上行APN AMBR）           | 1000bit/s            | 本端规划   | 配置EPS QoS缺省QoS参数。                           |
| ADD QOSPROFILE   | QOSPROFILENAME (QoS Profile名)   | qos2                 | 本端规划   | 配置QosProfile的配置信息。                          |
| ADD EPSQOSACTION | QOSPROFILENAME (QoS Profile名)   | qos2                 | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | QCI（QCI值）                       | 1                    | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | GBRDL（下行保证带宽）                   | 256bit/s             | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | GBRDLACTION（超过下行GBR的处理）         | DEGRADE(降级)          | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | GBRUL（上行保证带宽）                   | 128bit/s             | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | GBRULACTION（超过上行GBR的处理）         | DEGRADE(降级)          | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | MBRDL（下行最大带宽）                   | 384bit/s             | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | MBRDLACTION （超过下行MBR的处理）        | DEGRADE(降级)          | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | MBRUL（上行最大带宽）                   | 192bit/s             | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD EPSQOSACTION | MBRULACTION （超过上行MBR的处理）        | DEGRADE(降级)          | 本端规划   | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| ADD CPAPN        | APN (APN名称)                     | apn1                 | 本端规划   | 指定APN实例。                                    |
| SET CPAPNQOSATTR | APN (APN名称)                     | apn1                 | 本端规划   | 为APN实例绑定QosProfile。                         |
| SET CPAPNQOSATTR | HASQOSPROFILE（是否配置QosProfile）   | ENABLE               | 本端规划   | 为APN实例绑定QosProfile。                         |
| SET CPAPNQOSATTR | QOSPROFILENAME (QoS Profile名)   | qos1                 | 本端规划   | 为APN实例绑定QosProfile。                         |
| SET QOSREMARK    | DOWNLINK (下行标记)                 | ENABLE               | 本端规划   | 整机上下行QosRemark功能开关。                         |
| SET QOSREMARK    | UPLINK（上行标记）                    | ENABLE               | 本端规划   | 整机上下行QosRemark功能开关。                         |
| ADD EPSREMARK    | QOSPROFILENAME（QoS Profile名）    | qos1                 | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | QCI（QCI值）                       | 1                    | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | ARPPL（ARP的优先级别）                 | 1                    | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | REMARKTYPE（标记类型）                | DSCP                 | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | DSCP                            | EF(对应的DSCP的值为101110) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S1UDSCPSWITCH（S1-U DSCP配置开关）    | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S1UDSCP（S1-U DSCP）              | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S1UDSCPVALUE（S1-U DSCP值）        | 22                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5SDSCPSWITCH（SGW S5 DSCP配置开关）  | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5SDSCP（SGW S5 DSCP）            | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5SDSCPVALUE（SGW S5 DSCP值）      | 23                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5PDSCPSWITCH（PGW S5 DSCP配置开关）  | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5PDSCP（PGW S5 DSCP）            | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S5PDSCPVALUE（PGW S5 DSCP值）      | 24                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8SDSCPSWITCH（SGW S8 DSCP配置开关）  | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8SDSCP（SGW S8 DSCP）            | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8SDSCPVALUE（SGW S8 DSCP值）      | 25                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8PDSCPSWITCH（PGW S8 DSCP配置开关）  | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8PDSCP（PGW S8 DSCP）            | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | S8PDSCPVALUE（PGW S8 DSCP值）      | 26                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | SGIDSCPSWITCH（PGW SGi DSCP配置开关） | ENABLE               | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | SGIDSCP（PGW SGi DSCP）           | DSCP_VALUE(映射的DSCP值) | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD EPSREMARK    | SGIDSCPVALUE（PGW SGi DSCP值）     | 27                   | 全网规划   | 配置EPS QoS到DSCP或者TOS的映射规则。                   |
| ADD USRPROFGROUP | USERPROFGNAME (用户模板组名称)         | usrg                 | 本端规划   | 配置用户模板组User Profile Group                   |
| ADD UPBINDUPG    | USERPROFGNAME (用户模板组名称)         | usrg                 | 全网规划   | 将UserProfile绑定到用户模板组                        |
| ADD UPBINDUPG    | UPBINDTYPE                      | DEFAULT              | 全网规划   | 将UserProfile绑定到用户模板组                        |
| ADD UPBINDUPG    | USERPROFILENAME（用户模板名称）         | profile1             | 本端规划   | 将UserProfile绑定到用户模板组                        |
| ADD APNUSRPROFG  | APN (APN名称)                     | apn1                 | 全网规划   | 将UserProfile Group绑定到APN                    |
| ADD APNUSRPROFG  | USERPROFGNAME（用户模板组名称）          | usrg                 | 全网规划   | 将UserProfile Group绑定到APN                    |
| SET QOSCTRL      | USERTYPE (用户漫游类型)               | VISITING             | 全网规划   | 配置用户带宽控制的全局开关                               |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开License配置开关。

   **SET LICENSESWITCH**
3. 设置全局的QoS信息。

   **SET CPQOSGLOBAL**
4. 配置EPS QoS缺省QoS参数。

   **SET DEFEPSQOS**
5. 配置EPS QoS协商控制。

   - 进入“MML命令行-UEG”窗口。
   - 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

     **ADD QOSPROFILE**
   - 配置会话类QoS上下行最高带宽门限、会话类QoS上下行保证带宽门限以及带宽超过门限值时对此类QoS用户的处理动作。

     **ADD EPSQOSACTION**

     **ADD EPSQOSACTION**
   - 配置APN实例。

     **ADD CPAPN**
   - 为APN实例绑定QoS profile。

     **SET CPAPNQOSATTR**
6. 配置EPS QoS到DSCP的映射关系。

   - 配置用户的上下行remark功能开关

     **SET QOSREMARK**
   - 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

     **ADD QOSPROFILE**
   - 配置EPS QoS到DSCP的映射规则。

     **ADD EPSREMARK**
   - 配置用户模板组User Profile Group。

     **ADD USRPROFGROUP**
   - 将UserProfile绑定到用户模板组UserProfileGroup。

     **ADD UPBINDUPG**
   - 配置APN实例。

     **ADD CPAPN**
   - 将UserProfile Group绑定到APN。

     **ADD APNUSRPROFG**
   - 为APN实例绑定QoS profile。

     **SET CPAPNQOSATTR**
7. 配置QoS带宽控制。

   **SET QOSCTRL**

## 任务示例

任务描述

- 配置基于全局的EPS QoS信息。
- 配置基于全局的EPS缺省QoS参数。
- 配置基于APN的EPS QoS协商控制。
- 配置基于APN的EPS QoS到DSCP的映射关系。
- 配置基于全局的EPS QoS带宽控制。

脚本

- 配置基于全局的EPS QoS信息。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  ```
  SET CPQOSGLOBAL:QOSPROFILENAME="qos1",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=1;
  ```
- 配置基于全局的EPS缺省QoS参数。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  ```
  SET DEFEPSQOS: QOSCLASSID=1, ARPVALUE=1, GBRDL=200, GBRUL=230, MBRDL=300, MBRUL=300, APNAMBRDL=1000, APNAMBRUL=1000;
  ```
- 配置基于APN的EPS QoS协商控制。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  //配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

  ```
  ADD QOSPROFILE:QOSPROFILENAME="qos2";
  ```

  //配置会话类QoS上下行最高带宽门限、QoS上下行保证带宽门限以及带宽超过门限值时对此类QoS用户的处理动作。

  ```
  ADD EPSQOSACTION:QOSPROFILENAME="qos2",QCI=1,GBRDL=256,GBRDLACTION=DEGRADE,GBRUL=128,GBRULACTION=DEGRADE,MBRDL=384,
  MBRDLACTION=DEGRADE,MBRUL=192,MBRULACTION=DEGRADE;
  ```

  //进入指定APN实例。

  ```
  ADD CPAPN:APN="apn1";
  ```

  //为该APN实例绑定QosProfile。

  ```
  SET CPAPNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="qos2";
  ```
- 配置基于APN的EPS QoS到DSCP的映射关系

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  //配置用户的上下行remark功能。

  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```

  //配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。

  ```
  ADD QOSPROFILE:QOSPROFILENAME="gp1";
  ```

  //配置EPS QoS到DSCP的映射规则。

  ```
  ADD EPSREMARK: QOSPROFILENAME="qosprofile1", QCI=1, ARPPL=1, REMARKTYPE=DSCP, DSCP=EF, S1UDSCPSWITCH=ENABLE, S1UDSCP=DSCP_VALUE, S1UDSCPVALUE=22, S5SDSCPSWITCH=ENABLE, S5SDSCP=DSCP_VALUE, S5SDSCPVALUE=23, S5PDSCPSWITCH=ENABLE, S5PDSCP=DSCP_VALUE, S5PDSCPVALUE=24, S8SDSCPSWITCH=ENABLE, S8SDSCP=DSCP_VALUE, S8SDSCPVALUE=25, S8PDSCPSWITCH=ENABLE, S8PDSCP=DSCP_VALUE, S8PDSCPVALUE=26, SGIDSCPSWITCH=ENABLE, SGIDSCP=DSCP_VALUE, SGIDSCPVALUE=27;
  ```

  //配置控制信令的DSCP值。

  ```
  SET IFDSCP: MSGCLS=SIGNALLING, INTFTP_SHOW=GTP_PROTOCOL_SIGNALING, DSCPV=63, CCDSCP=EF;
  ```

  //配置UserProfile Group。

  ```
  ADD USRPROFGROUP:USERPROFGNAME="usrg";
  ```

  //将UserProfile绑定到UserProfileGroup。

  ```
  ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";
  ```

  //进入指定APN实例。

  ```
  ADD CPAPN:APN="apn1";
  ```

  //将UserProfile Group绑定到APN。

  ```
  ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";
  ```

  //为该APN实例绑定QosProfile。

  ```
  SET CPAPNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="gp1";
  ```
- 配置基于全局的EPS QoS带宽控制。

  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```

  ```
  SET QOSCTRL USERTYPE=VISITING;
  ```