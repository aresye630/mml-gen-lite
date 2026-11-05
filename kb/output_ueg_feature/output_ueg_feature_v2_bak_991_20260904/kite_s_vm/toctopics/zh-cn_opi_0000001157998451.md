# 基于用户组TOS的带宽控制

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

对于一个用户组基于TOS作为区分业务的条件，即UEG可以不进行业务的识别和解析，只是根据报文的DSCP就可以确定是否对其进行流量监管。

**说明** 

适用于PGW-U、UPF。

## 必备事项

前提条件

- 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
- UEG与网络实体之间的网络环境已经构建完成。

数据

| 类别                 | 参数名称                         | 取值样例           | 获取方法     | 说明                                                                                                                              |
|:-------------------|:-----------------------------|:---------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------|
| ADD BWMSERVICE     | 带宽控制业务名称（BWMSERVICENAME）     | bs_test        | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | 业务类型（BWMSERVICETYPE）         | TOS            | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos配置类型（TOSCFGTYPE）          | CLASS          | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos分类类型（TOSCLASSTYPE）        | BE             | 本端规划     | -                                                                                                                               |
| ADD BWMCONTROLLER  | 带宽管理控制器名称（BWMCNAME）          | bc-up bc-down  | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 带宽管理控制类型（CTRLTYPE）           | CAR            | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺信息速率（千比特/秒）（CIR）           | 300            | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺突发能缓存信息的数量（字节）（CBS）        | 10000          | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值信息速率（千比特/秒）（PIR）           | 500            | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值突发能缓存信息的数量（字节）（PBS）        | 12000          | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 绿色（GREEN）                    | PASS           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 黄色（YELLOW）                   | PASS           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 红色（RED）                      | DISCARD        | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| SET BANDWIDTHMNG   | 带宽管理生效范围（RANGE）              | SYSTEM         | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组名称（USERGROUPNAME）         | ug_test        | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组优先级（USERGROUPPRI）         | 1              | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组级业务类型（USERGLEVSRVTYPE）    | TOS            | 本端规划     | -                                                                                                                               |
| ADD BWMRULE        | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 用户组名称（USERGROUPNAME）         | ug_test        | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则类型（BWMRULETYPE）        | GROUP_SPECIFIC | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则名称（BWMRULENAME）        | br_test        | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽控制业务名称（BWMSERVICENAME）     | bs_test        | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 上行带宽管理控制器名称一（UPBWMCTRLNAME1） | bc-up          | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 下行带宽管理控制器名称一（DNBWMCTRLNAME1） | bc-down        | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD BWMRULE        | 带宽管理规则优先级（BWMRULEPRI）        | 1              | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。                                                        |
| ADD APNBINDBWMUSRG | 用户组名称（USERGROUPNAME）         | ug_test        | 本端规划     | -                                                                                                                               |
| ADD APNBINDBWMUSRG | APN名称（APN）                   | apn-test       | 本端规划     | 通过ADD APN(风筝S)/ADD UPAPN(风筝M或L)命令配置，可以使用LST APN(风筝S)/LST UPAPN(风筝M或L)命令进行查询。                                                    |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. 配置BWM业务。
   1. 用TOS来定义BWM业务。

      **ADD BWMSERVICE**
   2. 配置两个BWM控制器，设置CAR参数。

      **ADD BWMCONTROLLER**
   3. 配置BWM控制器中的用户组级业务带宽和连接数等配置数据是基于业务处理单元生效还是整机生效。

      **SET BANDWIDTHMNG**
3. 配置带宽管理用户组
   1. 定义带宽管理用户组，配置优先级和业务类型。

      **ADD BWMUSERGROUP**
   2. 配置用户组级带宽控制规则。

      **ADD BWMRULE**
   3. 将APN下的用户包含到该用户组。

      **ADD APNBINDBWMUSRG**

## 任务示例

任务描述

本实例中，操作员在UEG上进行数据配置实现以下要求：

UEG对一个用户组下的所有用户的指定IP TOS等级的上行、下行用户面数据流量进行流量监管。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5TCSA01",SWITCH=ENABLE;
```

//配置BWM业务。

```
ADD BWMSERVICE:BWMSERVICENAME="bs_test",BWMSERVICETYPE=TOS,TOSCFGTYPE=CLASS,TOSCLASSTYPE=BE;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-up",CTRLTYPE=CAR,CIR=300,CBS=10000,PIR=500,PBS=12000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc-down",CTRLTYPE=CAR,CIR=300,CBS=10000,PIR=500,PBS=12000,GREEN=PASS,YELLOW=PASS,RED=DISCARD;
```

```
SET BANDWIDTHMNG:RANGE=SYSTEM;
```

//配置带宽管理用户组。

```
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",USERGROUPPRI=1,USERGLEVSRVTYPE=TOS;
```

```
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",BWMRULETYPE=GROUP_SPECIFIC,BWMRULENAME="br_test",BWMSERVICENAME="bs_test",UPBWMCTRLNAME1="bc-up",DNBWMCTRLNAME1="bc-down",BWMRULEPRI=1;
```

```
ADD APNBINDBWMUSRG:USERGROUPNAME="ug_test",APN="apn-test";
```