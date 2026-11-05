# 基于时间段的带宽控制

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

在不同的时间段，对P2P流量进行不同规则的流量控制。

**说明** 

适用于PGW-U、UPF。

## 必备事项

前提条件

- 请仔细阅读GWFD-022701 基于业务感知的带宽控制。
- UEG与网络实体之间的网络环境已经构建完成。

数据

| 类别                 | 参数名称                         | 取值样例                  | 获取方法     | 说明                                                                                                                              |
|:-------------------|:-----------------------------|:----------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------|
| ADD BWMSERVICE     | 带宽控制业务名称（BWMSERVICENAME）     | my-bwm-service8       | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | 业务类型（BWMSERVICETYPE）         | TOS                   | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos配置类型（TOSCFGTYPE）          | CLASS                 | 本端规划     | -                                                                                                                               |
| ADD BWMSERVICE     | Tos分类类型（TOSCLASSTYPE）        | CS7                   | 本端规划     | -                                                                                                                               |
| ADD BWMCONTROLLER  | 带宽管理控制器名称（BWMCNAME）          | bc1 bc2 bc3           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 带宽管理控制类型（CTRLTYPE）           | CAR                   | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺信息速率（千比特/秒）（CIR）           | 30 300 3000           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 承诺突发能缓存信息的数量（字节）（CBS）        | 1000 10000 100000     | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值信息速率（千比特/秒）（PIR）           | 50 500 5000           | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 峰值突发能缓存信息的数量（字节）（PBS）        | 1200 12000 120000     | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 绿色（GREEN）                    | PASS                  | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 黄色（YELLOW）                   | REMARK                | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 黄色重标记类型（YELLOWREMARKT）       | DSCPVALUE             | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 黄色重标记值（YELLOWREMARKV）        | 10 15 20              | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD BWMCONTROLLER  | 红色（RED）                      | DISCARD               | 本端规划     | 推荐配置：CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍）CBS >= CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） |
| ADD TIMERANGE      | 时间段名称（TIMERANGENAME）         | timerange1 timerange2 | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 时间段名称（TIMERANGENAME）         | timerange1 timerange2 | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 周期时间段序号（PERITMRANGESEQ）      | 1                     | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 周期时间段配置方式（PERITIMETYPE）      | DAYSOFWEEK            | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 周日期（DAYOFWEEK）               | DAILY                 | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 起始时间，格式HH:MM（STARTTIME）      | 8&30 22&00            | 本端规划     | -                                                                                                                               |
| ADD PERITIMERANGE  | 结束时间，格式HH:MM（ENDTIME）        | 10&00 23&00           | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP        | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组名称（USERGROUPNAME）         | ugroup8               | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组优先级（USERGROUPPRI）         | 1                     | 本端规划     | -                                                                                                                               |
| ADD BWMUSERGROUP   | 用户组级业务类型（USERGLEVSRVTYPE）    | TOS                   | 本端规划     | -                                                                                                                               |
| ADD BWMRULE        | 用户组类型（USERGROUPTYPE）         | SPECIFIC_GROUP        | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 用户组名称（USERGROUPNAME）         | ugroup8               | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 带宽管理规则类型（BWMRULETYPE）        | GROUP_SPECIFIC        | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 带宽管理规则名称（BWMRULENAME）        | my-bw-rule8           | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 带宽控制业务名称（BWMSERVICENAME）     | my-bwm-service8       | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 上行带宽管理控制器名称一（UPBWMCTRLNAME1） | bc2                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 下行带宽管理控制器名称一（DNBWMCTRLNAME1） | bc2                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 时间段名称一（TIMERANGENAME1）       | timerange1            | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 上行带宽管理控制器名称二（UPBWMCTRLNAME2） | bc3                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 下行带宽管理控制器名称二（DNBWMCTRLNAME2） | bc3                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 时间段名称二（TIMERANGENAME2）       | timerange2            | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 上行带宽管理控制器名称三（UPBWMCTRLNAME3） | bc1                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 下行带宽管理控制器名称三（DNBWMCTRLNAME3） | bc1                   | 已配置数据中获取 | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD BWMRULE        | 带宽管理规则优先级（BWMRULEPRI）        | 1                     | 本端规划     | BwmService已通过ADD BWMSERVICE命令配置； BwmController已通过 ADD BWMCONTROLLER命令配置。 绑定的时间段已通过ADD TIMERANGE命令配置。                            |
| ADD APNBINDBWMUSRG | 用户组名称（USERGROUPNAME）         | ugroup8               | 本端规划     | -                                                                                                                               |
| ADD APNBINDBWMUSRG | APN名称（APN）                   | apn-test              | 本端规划     | 通过ADD APN(风筝S)/ADD UPAPN(风筝M或L)命令配置，可以使用LST APN(风筝S)/LST UPAPN(风筝M或L)命令进行查询。                                                    |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. 配置BWM业务。
   1. 用TOS定义BWM业务。

      **ADD BWMSERVICE**
   2. 配置两个BWM控制器，设置CAR参数。

      **ADD BWMCONTROLLER**
3. 配置多个时间段。

   **ADD TIMERANGE**

   **ADD PERITIMERANGE**
4. 配置带宽管理用户组。
   1. 定义带宽管理用户组，配置优先级和业务类型。

      **ADD BWMUSERGROUP**
   2. 配置带宽控制规则,设置不同时间段的带宽控制器。

      **ADD BWMRULE**
   3. 将APN下的用户包含到该用户组。

      **ADD APNBINDBWMUSRG**

## 任务示例

任务描述

配置多个时间段及三种业务规则，将业务规则与对应时间段绑定。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5TCSA01",SWITCH=ENABLE;
```

//配置BWM业务。

```
ADD BWMSERVICE:BWMSERVICENAME="my-bwm-service8",BWMSERVICETYPE=TOS,TOSCFGTYPE=CLASS,TOSCLASSTYPE=CS7;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc1",CTRLTYPE=CAR,CIR=30,CBS=1000,PIR=50,PBS=1200,GREEN=PASS,YELLOW=REMARK,YELLOWREMARKT=DSCPVALUE,YELLOWREMARKV=10,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc2",CTRLTYPE=CAR,CIR=300,CBS=10000,PIR=500,PBS=12000,GREEN=PASS,YELLOW=REMARK,YELLOWREMARKT=DSCPVALUE,YELLOWREMARKV=15,RED=DISCARD;
```

```
ADD BWMCONTROLLER:BWMCNAME="bc3",CTRLTYPE=CAR,CIR=3000,CBS=100000,PIR=5000,PBS=120000,GREEN=PASS,YELLOW=REMARK,YELLOWREMARKT=DSCPVALUE,YELLOWREMARKV=20,RED=DISCARD;
```

//配置多个时间段。

```
ADD TIMERANGE:TIMERANGENAME="timerange1";
```

```
ADD TIMERANGE:TIMERANGENAME="timerange2";
```

```
ADD PERITIMERANGE:TIMERANGENAME="timerange1",PERITMRANGESEQ=1,PERITIMETYPE=DAYSOFWEEK,DAYOFWEEK=DAILY,STARTTIME=8&30,ENDTIME=10&00;
```

```
ADD PERITIMERANGE:TIMERANGENAME="timerange2",PERITMRANGESEQ=1,PERITIMETYPE=DAYSOFWEEK,DAYOFWEEK=DAILY,STARTTIME=22&00,ENDTIME=23&00;
```

//配置用户组。

```
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ugroup8",USERGROUPPRI=1,USERGLEVSRVTYPE=TOS;
```

```
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ugroup8",BWMRULETYPE=GROUP_SPECIFIC,BWMRULENAME="my-bw-rule8",BWMSERVICENAME="my-bwm-service8",UPBWMCTRLNAME1="bc2",DNBWMCTRLNAME1="bc2",TIMERANGENAME1="timerange1",UPBWMCTRLNAME2="bc3",DNBWMCTRLNAME2="bc3",TIMERANGENAME2="timerange2",UPBWMCTRLNAME3="bc1",DNBWMCTRLNAME3="bc1",BWMRULEPRI=1;
```

```
ADD APNBINDBWMUSRG:USERGROUPNAME="ugroup8",APN="apn-test";
```