# 配置事件计费功能

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当部署事件计费，基于用户访问某业务的次数计费时，可参考本章节操作。

**说明** 

适用于GGSN、PGW-C、SMF。

## 必备事项

前提条件

- 请仔细阅读WSFD-109007 支持事件计费。
- 完成激活离线计费、激活Gy/Diameter在线计费或激活支持融合计费。
- 完成激活内容计费。
- 完成加载License。

数据

| 类别                | 参数名称                         | 取值样例      | 获取方法   | 说明                                                 |
|:------------------|:-----------------------------|:----------|:-------|:---------------------------------------------------|
| SET CHFINIT       | CCTMPLTNAME（融合计费模板名称）        | cct-test  | 本端规划   | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。           |
| SET CHFINIT       | CHFINIT（CHF交互使能开关）           | SENDREQ   | 本端规划   | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。           |
| SET CHFINIT       | CCRINITRGNUM（初始RG个数）         | 10        | 本端规划   | 配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。           |
| ADD URR           | URRNAME（使用量上报规则名称）           | urr1      | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | URRID（URR标识）                 | 1000      | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | USAGERPTMODE（使用量上报模式）        | ONLINE    | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | ONLCOMPOUNDTYPE（在线计费标识组成类型）  | ONLYRG    | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | ONLINERG（在线计费组）              | 100       | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | ONLMETERINGTYPE（在线计费统计类型）    | EVENT     | 本端规划   | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
| ADD URR           | URRNAME（使用量上报规则名称）           | urr2      | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URR           | URRID（URR标识）                 | 1002      | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URR           | USAGERPTMODE（使用量上报模式）        | OFFLINE   | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URR           | OFFCOMPOUNDTYPE （离线计费标识组成类型） | ONLYRG    | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URR           | RG （离线计费组）                   | 102       | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URR           | OFFMETERINGTYPE （离线计费统计类型）   | EVENT     | 本端规划   | 配置离线计费用户的事件计费属性。                                   |
| ADD URRGROUP      | URRGROUPNAME（使用量上报规则组名称）     | urrgroup1 | 本端规划   | 配置融合计费和在线计费的URR Group和User Profile。                |
| ADD URRGROUP      | UPURRNAME1（上行发起URR名称1）       | urr1      | 本端规划   | 配置融合计费和在线计费的URR Group和User Profile。                |
| ADD URRGROUP      | DOWNURRNAME1（下行发起URR名称1）     | urr1      | 本端规划   | 配置融合计费和在线计费的URR Group和User Profile。                |
| ADD USERPROFILE   | USERPROFILENAME（用户模板名称）      | up-test   | 全网规划   | 配置融合计费和在线计费的URR Group和User Profile。                |
| ADD PCCPOLICYGRP  | PCCPOLICYGRPNM（PCC策略组名称）     | cg-test   | 本端规划   | 配置事件计费使用的Rule。                                     |
| ADD RULE          | RULENAME（规则名称）               | rule-test | 本端规划   | 配置事件计费使用的Rule。                                     |
| ADD RULE          | POLICYTYPE（策略类型）             | PCC       | 本端规划   | 配置事件计费使用的Rule。                                     |
| ADD RULE          | POLICYNAME（策略名称）             | cg-test   | 本端规划   | 配置事件计费使用的Rule。                                     |
| ADD CCT           | CCTMPLTNAME（融合计费模板名称）        | cct-test  | 本端规划   | 配置融合计费的CCT模板。                                      |
| SET USRPROFCHARGE | USRPROFNAME（用户模板名称）          | up-test   | 本端规划   | 配置融合计费的CCT模板。                                      |
| SET USRPROFCHARGE | CCTEMPLATE（融合计费模板名称）         | cct-test  | 本端规划   | 配置融合计费的CCT模板。                                      |
| ADD DCCTEMPLATE   | DCCTMPLTNAME（融合计费模板名称）       | dcc-test  | 本端规划   | 配置在线计费的DCC模板。                                      |
| SET USRPROFCHARGE | USRPROFNAME（用户模板名称）          | up-test   | 本端规划   | 配置在线计费的DCC模板。                                      |
| SET USRPROFCHARGE | DCCTEMPLATE（DCC模板名称）         | dcc-test  | 本端规划   | 配置在线计费的DCC模板。                                      |
| ADD RULEBINDING   | USERPROFILENAME（用户模板名称）      | up-test   | 本端规划   | 将Rule绑定到UserProfile上。                              |
| ADD RULEBINDING   | RULENAME（规则名称）               | rule-test | 本端规划   | 将Rule绑定到UserProfile上。                              |
| ADD USRPROFGROUP  | USERPROFGNAME（用户模板组名称）       | upg-test  | 本端规划   | 将Rule绑定到UserProfile上。                              |
| ADD UPBINDUPG     | USERPROFGNAME（用户模板组名称）       | upg_test  | 全网规划   | 将UserProfile绑定到UserProfile组上。                      |
| ADD UPBINDUPG     | UPBINDTYPE（用户模板绑定类型）         | DEFAULT   | 全网规划   | 将UserProfile绑定到UserProfile组上。                      |
| ADD UPBINDUPG     | USERPROFILENAME（用户模板名称）      | up_test   | 本端规划   | 将UserProfile绑定到UserProfile组上。                      |
| ADD APN           | APN（APN名称）                   | apn-test  | 全网规划   | 将UserProfile组绑定到DNN上。                              |
| ADD APNUSRPROFG   | APN（APN名称）                   | apn-test  | 全网规划   | 将UserProfile组绑定到DNN上。                              |
| ADD APNUSRPROFG   | USERPROFGNAME（用户模板组名称）       | upg-test  | 全网规划   | 将UserProfile组绑定到DNN上。                              |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开事件计费的License配置开关。

   **SET LICENSESWITCH**
3. **可选：**配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互建立计费会话。

   **SET CHFINIT**
4. **可选：**配置事件计费使用的计费属性。

   1. 配置事件计费的RG使用的URR组及相应URR。

      **ADD URR**

      **ADD URRGROUP**
   2. 配置UserProfile。

      **ADD USERPROFILE**
5. 配置事件计费使用的Rule，将URR组绑定到对应的Rule上。

   1. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。

      **ADD PCCPOLICYGRP**
   2. 配置Rule，将PCC策略组绑定到Rule上。

      **ADD RULE**
6. 配置融合计费模板或在线计费模板。

   - 配置融合计费模板。

     **ADD CCT**

     **SET USRPROFCHARGE**

   - 配置在线计费模板。

     **ADD DCCTEMPLATE**

     **SET USRPROFCHARGE**
7. 绑定该UserProfile使用的Rule。

   **ADD RULEBINDING**
8. 配置UserProfile绑定的UserProfile组及DNN实例。

   1. 配置UserProfile组，将UserProfile绑定到UserProfile组上。

      **ADD USRPROFGROUP**

      **ADD UPBINDUPG**
   2. 配置DNN，将UserProfile组绑定到指定DNN实例上。

      **ADD APN**

      **ADD APNUSRPROFG**

## 任务示例

任务描述

任务一：为RG=100的费率标识业务进行事件计费（适用于融合计费用户或在线计费用户）。

任务二：为RG=102的费率标识业务进行事件计费（适用于离线计费用户）。

脚本

//打开事件计费的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3W9EBCS12", SWITCH=ENABLE;
```

任务一：为RG=100的费率标识业务进行事件计费（适用于融合计费用户或在线计费用户）。

//配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。

```
SET CHFINIT: CCTMPLTNAME="cct-test", CHFINIT=SENDREQ, CCRINITRGNUM=10;
```

//配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。

```
ADD URR: URRNAME="urr1", URRID=1000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=EVENT;
ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="urr1", DOWNURRNAME1="urr1";
ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
```

//配置事件计费使用的Rule，绑定事件计费使用的URR组。

```
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";
ADD RULE: RULENAME="rule-test", POLICYTYPE=PCC, POLICYNAME="cg-test";
```

//配置UserProfile下的CCT模板（适用于融合计费用户）。

```
ADD CCT: CCTMPLTNAME="cct-test";
SET USRPROFCHARGE: USRPROFNAME="up-test", CCTEMPLATE="cct-test";
```

//配置UserProfile下的DCC Template模板（适用于在线计费用户）。

```
ADD DCCTEMPLATE:DCCTMPLTNAME="dcc-test";
SET USRPROFCHARGE: USRPROFNAME="up-test", DCCTEMPLATE="dcc-test";
```

//配置事件计费的UserProfile。

```
ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="rule-test";
ADD USRPROFGROUP:USERPROFGNAME="upg-test";
ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
ADD APN:APN="apn-test";
ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";
```

//任务二：为RG=102的费率标识业务进行事件计费（适用于离线计费用户）。

```
ADD URR: URRNAME="urr2", URRID=1002, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=102, OFFMETERINGTYPE=EVENT;
```