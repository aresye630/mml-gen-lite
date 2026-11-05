# 基于用户/用户组/整机三级的带宽控制

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

保护带宽资源不被P2P/VoIP流量吞噬，确保应用公平分享带宽资源。并且确保每个用户公平分享带宽资源，每个用户组公平分享带宽资源，对整机的业务流量进行控制。

**说明** 

适用于PGW-U、UPF。

## 必备事项

前提条件

- 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
- UEG与网络实体之间的网络环境已经构建完成。

数据

| 类别                 | 参数名称                         | 取值样例                                                                          | 获取方法     | 说明                                                                                                                              |
|:-------------------|:-----------------------------|:------------------------------------------------------------------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------|
| ADD BWMSERVICE     | 带宽控制业务名称（BWMSERVICENAME）     | bs_subs_test bs_group_test                                                    | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | 业务类型（BWMSERVICETYPE）         | NONTOS TOS                                                                    | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | 非TOS业务类型（NONTOSSRVTYPE）      | PROTOCOL                                                                      | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | 协议名称（PROTOCOLNAME）           | http                                                                          | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos配置类型（TOSCFGTYPE）          | CLASS                                                                         | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos分类类型（TOSCLASSTYPE）        | BE                                                                            | 本端规划     | -                                                                                                                               |
| ADD BWMCONTROLLER  | 带宽管理控制器名称（BWMCNAME）          | bc-subs-up bc-subs-down bc-group-up bc-group-down bc-global-up bc-global-down | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 带宽管理控制类型（CTRLTYPE）           | CAR                                                                           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺信息速率（千比特/秒）（CIR）           | 30 30 300 300 3000 3000                                                       | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺突发能缓存信息的数量（字节）（CBS）        | 1000 1000 10000 10000 100000 100000                                           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值信息速率（千比特/秒）（PIR）           | 50 50 500 500 5000 5000                                                       | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值突发能缓存信息的数量（字节）（PBS）        | 1200 1200 12000 12000 120000 120000                                           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 绿色（GREEN）                    | PASS                                                                          | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 黄色（YELLOW）                   | PASS                                                                          | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 红色（RED）                      | DISCARD                                                                       | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMUSERGROUP   | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP                                                                | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组名称（USERGROUPNAME）         | ug_test                                                                       | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组优先级（USERGROUPPRI）         | 1                                                                             | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户级业务类型（USERLEVSRVTYPE）      | NONTOS                                                                        | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组级业务类型（USERGLEVSRVTYPE）    | TOS                                                                           | 本端规划     | -                                                                                                                               |
| ADD BWMRULE        | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP                                                                | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 用户组名称（USERGROUPNAME）         | ug_test                                                                       | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则类型（BWMRULETYPE）        | SUBSCRIBER_SPECIFIC GROUP_SPECIFIC                                            | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则名称（BWMRULENAME）        | br_subs_test br_group_test                                                    | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽控制业务名称（BWMSERVICENAME）     | bs_subs_test bs_group_test                                                    | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 上行带宽管理控制器名称一（UPBWMCTRLNAME1） | bc-subs-up bc-group-up                                                        | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 下行带宽管理控制器名称一（DNBWMCTRLNAME1） | bc-subs-down bc-group-down                                                    | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则优先级（BWMRULEPRI）        | 1                                                                             | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD APNBINDBWMUSRG | 用户组名称（USERGROUPNAME）         | ug_test                                                                       | 本端规划     | -                                                                                                                               |
| ADD APNBINDBWMUSRG | APN名称（APN）                   | apn-test                                                                      | 本端规划     | 通过ADD APN(风筝S)/ADD UPAPN(风筝M或L)命令配置，可以使用LST APN(风筝S)/LST UPAPN(风筝M或L)命令进行查询。                                                    |
| ADD BWMRULEGLOBAL  | 带宽管理规则名称（BWMRULENAME）        | br_global_test                                                                | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULEGLOBAL  | 带宽控制业务名称（BWMSERVICENAME）     | bs_group_test                                                                 | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULEGLOBAL  | 上行带宽管理控制器名称一（UPBWMCTRLNAME1） | bc-global-up                                                                  | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULEGLOBAL  | 下行带宽管理控制器名称一（DNBWMCTRLNAME1） | bc-global-down                                                                | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULEGLOBAL  | 带宽管理规则优先级（BWMRULEPRI）        | 1                                                                             | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. 配置BWM业务。
   1. 用http协议定义用户级的BWM业务，用TOS定义用户组级和整机的BWM业务。

      **ADD BWMSERVICE**
   2. 配置用户级、用户组级和整机的BWM控制器，设置CAR参数。

      **ADD BWMCONTROLLER**
3. 配置带宽管理用户组。
   1. 定义带宽管理用户组，配置优先级和业务类型。

      **ADD BWMUSERGROUP**
   2. 配置用户级和用户组级带宽控制规则。

      **ADD BWMRULE**
   3. 将APN下的用户包含到该用户组。

      **ADD APNBINDBWMUSRG**
4. 配置整机级带宽控制规则。

   **ADD BWMRULEGLOBAL**

## 任务示例

任务描述

本实例中，操作员在UEG上进行数据配置实现以下要求：

UEG对一个用户组下的每个用户的指定IP TOS等级的上行、下行用户面数据流量进行流量监管。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5TCSA01",SWITCH=ENABLE;
```

//配置BWM业务。

```
ADD BWMSERVICE:BWMSERVICENAME="bs_subs_test",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=PROTOCOL,PROTOCOLNAME="http";
```

```
ADD BWMSERVICE:BWMSERVICENAME="bs_group_test",BWMSERVICETYPE=TOS,TOSCFGTYPE=CLASS,TOSCLASSTYPE=BE;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-subs-up",CTRLTYPE=CAR,CIR=30,CBS=1000,PIR=50,PBS=1200,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-subs-down",CTRLTYPE=CAR,CIR=30,CBS=1000,PIR=50,PBS=1200,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-group-up",CTRLTYPE=CAR,CIR=300,CBS=10000,PIR=500,PBS=12000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-group-down",CTRLTYPE=CAR,CIR=300,CBS=10000,PIR=500,PBS=12000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-global-up",CTRLTYPE=CAR,CIR=3000,CBS=100000,PIR=5000,PBS=120000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-global-down",CTRLTYPE=CAR,CIR=3000,CBS=100000,PIR=5000,PBS=120000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

//配置带宽管理用户组。

```
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",USERGROUPPRI=1,USERLEVSRVTYPE=NONTOS,USERGLEVSRVTYPE=TOS;
```

```
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="br_subs_test",BWMSERVICENAME="bs_subs_test",UPBWMCTRLNAME1="bc-subs-up",DNBWMCTRLNAME1="bc-subs-down",BWMRULEPRI=1;
```

```
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",BWMRULETYPE=GROUP_SPECIFIC,BWMRULENAME="br_group_test",BWMSERVICENAME="bs_group_test",UPBWMCTRLNAME1="bc-group-up",DNBWMCTRLNAME1="bc-group-down",BWMRULEPRI=1;
```

```
ADD APNBINDBWMUSRG:USERGROUPNAME="ug_test",APN="apn-test";
```

//配置整机带宽规则。

```
ADD BWMRULEGLOBAL:BWMRULENAME="br_global_test",BWMSERVICENAME="bs_group_test",UPBWMCTRLNAME1="bc-global-up",DNBWMCTRLNAME1="bc-global-down",BWMRULEPRI=1;
```