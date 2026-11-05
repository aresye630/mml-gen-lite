# 配置业务触发RADIUS功能

- 操作场景
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

需要使能业务触发RADIUS时，执行此任务。

**说明** 

适用于PGW-C、SMF

## 必备事项

前提条件

- 请仔细阅读GWFD-024303 Radius功能特性概述。
- UEG与周边网元的互通配置已经完成。
- 完成增加APN配置。
- **该功能需要与UPF/PGW-U共同完成配置**。配置该功能前，需要确保已在UPF/PGW-U上配置完成使用的过滤器和绑定的流过滤器、规则等业务感知信息。
- 已通过**ADD LOGICIP**配置完成逻辑接口使用到的逻辑IP。

数据

| 类别                                  | 参数名称                                  | 取值样例         | 获取方法     | 说明                                                                               |
|:------------------------------------|:--------------------------------------|:-------------|:---------|:---------------------------------------------------------------------------------|
| 当UEG的产品形态为风筝L时， ADD CPAPN           | APN名称（APN）                            | apn-test     | 全网规划     | -                                                                                |
| SET APNRDSACCTCTRL                  | APN名称（APN）                            | apn-test     | 已配置数据中获取 | 在指定APN下使能业务触发RADIUS功能。 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。        |
| SET APNRDSACCTCTRL                  | 业务报文（通过3/4层规则配置）时触发计费请求消息（SRVTRIGGER） | ENABLE       | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时， ADD CPSVCFLOWFILTER | 流过滤器名称（FLOWFILTERNAME）                | flowfilter_1 | 与对端协商    | 需要与UPF/PGW-U上规划的流过滤器保持一致。                                                        |
| 当UEG的产品形态为风筝L时， ADD CPRULE          | 规则名称（RULENAME）                        | rule_test1   | 本端规划     | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。                               |
| 当UEG的产品形态为风筝L时， ADD CPRULE          | 策略类型（POLICYTYPE）                      | SRV_TRIGGER  | 本端规划     | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。                               |
| 当UEG的产品形态为风筝L时， ADD CPRULE          | 全局优先级（PRIORITY）                       | 10           | 本端规划     | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。                               |
| 当UEG的产品形态为风筝L时， ADD CPUSERPROFILE   | 用户模板名称（USERPROFILENAME）               | up_test      | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时， ADD CPUSERPROFILE   | 用户模板类型（UPTYPE）                        | PCC          | 本端规划     | -                                                                                |
| 当UEG的产品形态为风筝L时， ADD CPRULEBINDING   | 规则名称（RULENAME）                        | rule_test1   | 已配置数据中获取 | User Profile绑定的业务规则，当UEG的产品形态为风筝L时，已通过ADD CPRULE配置，可以使用LST CPRULE命令进行查询。         |
| 当UEG的产品形态为风筝L时， ADD CPRULEBINDING   | 用户模板名称（USERPROFILENAME）               | up_test      | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPUSERPROFILE配置，可以使用LST CPUSERPROFIL命令进行查询。                |
| ADD USRPROFGROUP                    | 用户模板组名称（USERPROFGNAME）                | upg_test     | 本端规划     | -                                                                                |
| ADD UPBINDUPG                       | 用户模板组名称（USERPROFGNAME）                | upg_test     | 已配置数据中获取 | 已经通过ADD USRPROFGROUP命令配置完成，可以使用LST USRPROFGROUP查询。                               |
| ADD UPBINDUPG                       | 用户模板绑定类型（UPBINDTYPE）                  | DEFAULT      | 本端规划     | -                                                                                |
| ADD UPBINDUPG                       | 用户模板名称（USERPROFILENAME）               | up_test      | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPUSERPROFILE配置，可以使用LST CPUSERPROFIL命令进行查询。 。              |
| ADD APNUSRPROFG                     | APN名称（APN）                            | apn-test     | 已配置数据中获取 | 将User Profile Group绑定到指定APN下。 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。 |
| ADD APNUSRPROFG                     | 用户模板组名称（USERPROFGNAME）                | upg_test     | 已配置数据中获取 | 已经通过ADD USRPROFGROUP命令配置完成，可以使用LST USRPROFGROUP查询。                               |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置业务触发RADIUS功能。
   1. 配置APN。

      当UEG的产品形态为风筝L时，**ADD CPAPN**
   2. 使能业务触发RADIUS功能。

      **SET APNRDSACCTCTRL**
3. 配置业务使用的流过滤器。

   当UEG的产品形态为风筝L时，****ADD CPSVCFLOWFILTER****
4. 配置业务规则。

   当UEG的产品形态为风筝L时，**ADD CPRULE**
5. 配置业务策略组合。
   1. 配置UserProfile模板。

      当UEG的产品形态为风筝L时，**ADD CPUSERPROFILE**
   2. 将已配置的Rule绑定到UserProfile。

      当UEG的产品形态为风筝L时，ADD CPRULEBINDING
   3. 配置UsrProfGroup。

      **ADD USRPROFGROUP**
   4. 将UserProfile绑定到UsrProfGroup。

      **ADD UPBINDUPG**
   5. 将UsrProfGroup绑定到指定APN。

      **ADD APNUSRPROFG**

      **说明** 

      业务策略组合和APN建立绑定关系后，对该APN已经存在的用户无效，只对后续激活的用户生效。

## 验证方法

具体步骤请参见调测到AAA Server的数据。

## 任务示例

任务描述

本实例中，用户访问www.huawei.com时，UEG发送RADIUS Accounting-Request Start消息，携带用户信息发送给AAA Server。

脚本

//配置业务触发RADIUS功能。

当UEG的产品形态为风筝L时，

```
ADD CPAPN: APN="apn-test";
SET APNRDSACCTCTRL: APN="apn-test",SRVTRIGGER=ENABLE;
```

//配置业务规则（为了确保该功能生效，请在UDG上配置相同的业务规则，并绑定该业务触发使用的流过滤器。流过滤器的配置请参考UDG上内容感知相关章节。）。

当UEG的产品形态为风筝L时，

```
ADD CPRULE: RULENAME="rule_test1", POLICYTYPE=SRV_TRIGGER, PRIORITY=50;
```

//配置业务策略组合。

当UEG的产品形态为风筝L时，

```
ADD CPUSERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
ADD CPRULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
ADD USRPROFGROUP: USERPROFGNAME="upg_test";
ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";
ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
```