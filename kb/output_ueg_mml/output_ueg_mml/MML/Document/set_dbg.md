# 设置软件调试参数（SET DBG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响业务处理或性能统计，需联系华为技术支持确认后再执行。

该命令用于设置软件调试参数。

**说明** 

当软参VRM\_QRYSPRPRIORITY取值非“0”且VRM\_SUBSRCIPTIONIDTYPE取值为“1”时，只能根据MSISDN来分发用户会话到指定的PES实例，不能根据IMSI来分发用户会话到指定的PES实例。

## 注意事项

- 软件调试会影响系统性能，仅限于华为工程师使用。
- 针对需要清除服务化接口会话的场景，“SERMT”选择“SER\_NGSRV”，“SERCMDTYPE”选择“SER\_CLR\_SESCB”，系统支持根据输入的“SESSIONID”清除对应的会话。目前此场景仅对N7和N5会话生效，其他服务化接口会话均不生效。
- 针对PDIAM控制块，该命令暂时仅支持处理Sy接口业务，即该场景下仅支持执行如下两条命令：

  ```
  SET DBG: SUBSYSTYPE=SER, SERMT=SER_PRO, SERCMDTYPE=SER_CLR_SESCB;
  SET DBG: SUBSYSTYPE=SER, SERMT=SER_UPM, SERCMDTYPE=SER_CLR_PROCBIDX;
  ```

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-----------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSYSTYPE | 子系统类型    | UPCF软件系统内部子系统名称。 取值范围： SER(业务组)：用于处理非用户组业务相关的调试能力。SER_SUBGROUP(用户组业务)：用于处理用户组业务相关的调试能力。ROUTE_MEMORY(路由缓存)：用于处理DLB服务内存缓存的调试能力。  说明： 这里的用户组是指由主从用户组成的用户组，以及由组用户/组成员用户组成的用户组。 默认值： 无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| INSTANCENO | 实例号      | 待调测的PES服务实例号。  说明： 实例号查询方法：执行DSP SERVICEINFO命令获取返回服务的实例号。 取值范围：长度不超过256的字符串。 默认值： 无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SERMT      | 业务子模块类型  | 用于标识业务子模块类型。该参数在“子系统类型”取值“SER(业务组)”和“SER_SUBGROUP(用户组业务)”时有效。 取值范围：SER_ALC(ALC子模块)SER_BLC(BLC子模块)SER_UPM(UPM子模块)SER_PRO(PRO子模块)SER_DISTRIBUTE(分发模块)SER_NGSRV(NGSRV模块)SER_BINDCFG(绑定配置)SER_GRPDISTIME(组成员散列时长)SER_PES(PES服务)SER_FSMMAXNUM（PES服务自动机最大数量） 默认值： 无。  说明： 当“业务子模块类型”选择“SER_DISTRIBUTE(分发模块)”时，“实例号”应填入DSP SERVICEINFO命令获取返回的“通信实例号”。当“业务子模块类型”选择“SER_GRPDISTIME(组成员散列时长)”时，该数据配置只对组成员用户生效，对普通用户/主从用户/组用户不生效。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SERCMDTYPE | 业务调试命令类型 | 用于标识业务调试命令类型。该参数在“子系统类型”取值“SER(业务组)”和“SER_SUBGROUP(用户组业务)”时有效。 取值范围：SER_CLR_USERCB(清除用户控制块)SER_CLR_SESCB(清除会话控制块)SER_CLR_PROCBIDX(清除协议索引)SER_CLR_ALCCBIDX(清除ALC会话索引)SER_CLR_BLCCBIDX(清除BLC会话索引)SER_CLR_UPMCBIDX(清除UPM用户索引)SER_SET_DISTRIBUTE(设置分发数据)SER_CLR_DISTRIBUTE(清除分发数据)SER_TEST_STACREATEACTION_ON(开启静态生成IMS动态pccRule下关联的Action)SER_TEST_STACREATEACTION_OFF(关闭静态生成IMS动态pccRule下关联的Action)SER_BINDCFG_EFFECTIVEONLINE_ON(开启绑定配置在线生效功能)SER_BINDCFG_EFFECTIVEONLINE_OFF(关闭绑定配置在线生效功能)SER_SET_GRPDISTIME(设置组成员散列时长)SER_CLR_GRPDISTIME(清除组成员散列时长)SER_CLR_SUBGROUP(清除用户组业务)SER_CLR_ALLSESSIONFORTEST(清除所有会话)SER_SET_FSMMAXNUM（设置PES服务自动机最大数量） 默认值：无。  说明： “SER_CLR_ALLSESSIONFORTEST(清除所有会话)”此参数仅适用于测试环境，用于构造会话备份的恢复场景，请勿在商用环境执行。同时，该数据配置只对普通用户生效，对主从用户、组用户/组成员用户不生效。当“业务调试命令类型”选择“SER_SET_GRPDISTIME(设置组成员散列时长)”和“SER_CLR_GRPDISTIME(清除组成员散列时长)”时，该数据配置只对组成员用户生效，对普通用户/主从用户/组用户不生效。当“业务调试命令类型”选择“SER_CLR_SUBGROUP(清除用户组业务)”时，该数据配置只对主从用户、组用户/组成员用户生效，对普通用户不生效。 |
| INDEX      | 索引       | 用于指定需要修改的索引值。 取值范围：0～4294967295                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PARATYPE   | 参数类型     | 用于设置参数类型。该参数在“子系统类型”取值“SER(业务组)”和“SER_SUBGROUP(用户组业务)”时有效。 取值范围：SUBID(用户标识)SESSIONID(会话标识) 默认值： 无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SUBID      | 用户标识     | 用于指定打印会话信息的用户标识、指定散列的组成员用户的用户标识、指定清理的组用户标识。当“参数类型”取值 “SUBID(用户标识)”时，需要输入此参数，才弹出该参数。 取值范围：长度不超过255的字符串。 默认值： 无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SESSIONID  | 会话标识     | 用于设置打印会话信息的会话标识。当“参数类型”取值“SESSIONID(会话标识)”时，需要输入此参数，才弹出该参数。 取值范围：长度不超过128的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DISTIME    | 组策略下发延时  | 用于指定延时的时间大小。当“业务调试命令类型”取值“SER_SET_GRPDISTIME(设置组成员散列时长)”时，需要输入此参数，才弹出该参数。 取值范围：5～30。 单位：秒。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SWITCH     | 开关       | 用于设置使用DLB服务内存缓存的开关。仅在参数“子系统类型”配置为“ROUTE_MEMORY(路由缓存)”时需要配置。 取值范围： TRUE(是)：表示不使用DLB服务的内存缓存。FALSE(否)：表示使用DLB服务的内存缓存。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| FSMMAXNUM  | 自动机最大数量  | 用于设置支持的PES自动机最大数量。当“业务调试命令类型”取值“SER_SET_FSMMAXNUM（设置PES服务自动机最大数量）”时，需要输入此参数，才弹出该参数。 取值范围：5～100000。 单位： 个。 默认值：100000  说明： PES服务重启后，该参数取值会恢复为默认值“100000”。只有当自动机使用率为“0”时才允许修改自动机最大数量，自动机使用率可以通过命令查询控制块信息（DSP CBINFO）查询获取。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## 使用实例

不同业务子模块支持的业务调试命令类型，如表1所示。(“√”代表支持，“-”代表不支持)

| 业务调试命令类型                                                   | SER_ALC(ALC子模块)   | SER_BLC(BLC子模块)   | SER_UPM(UPM子模块)   | SER_PRO(PRO子模块)   | SER_DISTRIBUTE(分发模块)   | SER_NGSRV(NGSRV模块)   | SER_BINDCFG(绑定配置)   | SER_GRPDISTIME(组成员散列时长)   | SER_PES(PES服务)   | SER_FSMMAXNUM（PES服务自动机最大数量）   |
|:-----------------------------------------------------------|:------------------|:------------------|:------------------|:------------------|:-----------------------|:---------------------|:--------------------|:--------------------------|:-----------------|:------------------------------|
| SER_CLR_USERCB(清除用户控制块)                                    | -                 | -                 | √                 | -                 | -                      | -                    | -                   | -                         | -                | -                             |
| SER_CLR_SESCB(清除会话控制块)                                     | √                 | √                 | -                 | √                 | -                      | √                    | -                   | -                         | -                | -                             |
| SER_CLR_PROCBIDX(清除协议索引)                                   | -                 | -                 | -                 | -                 | -                      | -                    | -                   | -                         | -                | -                             |
| SER_CLR_ALCCBIDX(清除ALC会话索引)                                | -                 | -                 | -                 | -                 | -                      | -                    | -                   | -                         | -                | -                             |
| SER_CLR_BLCCBIDX(清除BLC会话索引)                                | -                 | -                 | √                 | -                 | -                      | -                    | -                   | -                         | -                | -                             |
| SER_CLR_UPMCBIDX(清除UPM用户索引)                                | -                 | √                 | -                 | -                 | -                      | -                    | -                   | -                         | -                | -                             |
| SER_SET_DISTRIBUTE（设置分发数据）                                 | -                 | -                 | -                 | -                 | √                      | -                    | -                   | -                         | -                | -                             |
| SER_CLR_DISTRIBUTE（清除分发数据）                                 | -                 | -                 | -                 | -                 | √                      | -                    | -                   | -                         | -                | -                             |
| SER_TEST_STACREATEACTION_ON(开启静态生成IMS动态pccRule下关联的Action)  | -                 | -                 | -                 | -                 | -                      | √                    | -                   | -                         | -                | -                             |
| SER_TEST_STACREATEACTION_OFF(关闭静态生成IMS动态pccRule下关联的Action) | -                 | -                 | -                 | -                 | -                      | √                    | -                   | -                         | -                | -                             |
| SER_BINDCFG_EFFECTIVEONLINE_ON(开启绑定配置在线生效功能)               | -                 | -                 | -                 | -                 | -                      | -                    | √                   | -                         | -                | -                             |
| SER_BINDCFG_EFFECTIVEONLINE_OFF(关闭绑定配置在线生效功能)              | -                 | -                 | -                 | -                 | -                      | -                    | √                   | -                         | -                | -                             |
| SER_SET_GRPDISTIME(设置组成员散列时长)                              | -                 | -                 | -                 | -                 | -                      | -                    | -                   | √                         | -                | -                             |
| SER_CLR_GRPDISTIME(清除组成员散列时长)                              | -                 | -                 | -                 | -                 | -                      | -                    | -                   | √                         | -                | -                             |
| SER_CLR_SUBGROUP(清除用户组业务)                                  | -                 | -                 | -                 | -                 | -                      | -                    | -                   | -                         | √                | -                             |
| SER_CLR_ALLSESSIONFORTEST(清除所有会话)                          | -                 | -                 | -                 | -                 | -                      | -                    | -                   | -                         | √                | -                             |
| SER_SET_FSMMAXNUM（设置PES服务自动机最大数量）                          | -                 | -                 | -                 | -                 | -                      | -                    | -                   | -                         | -                | √                             |

**说明** 

- 当参数“业务子模块类型”设置为“SER\_PRO(PRO子模块)”时，参数“业务调试命令类型”如下枚举值的功能已废弃：“SER\_CLR\_ALCCBIDX(清除ALC会话索引)”和“SER\_CLR\_BLCCBIDX(清除BLC会话索引)”。
- 当参数“业务子模块类型”设置为“SER\_BLC(BLC子模块)”或“SER\_ALC(ALC子模块)”时，参数“业务调试命令类型”枚举值“SER\_CLR\_PROCBIDX(清除协议索引)”的相关功能已废弃。

针对不同业务子模块的调试命令举例如下：

**SER\_ALC模块**

1. 清除会话控制块。其中“INSTANCENO”为“539738218”。

   ```
   SET DBG: SUBSYSTYPE=SER, INSTANCENO="539738218", SERMT=SER_ALC, SERCMDTYPE=SER_CLR_SESCB, PARATYPE=SESSIONID, SESSIONID="1212";
   ```
2. 清除协议索引。其中“INSTANCENO”为“539738218”。

   ```
   SET DBG: SUBSYSTYPE=SER, INSTANCENO="539738218", SERMT=SER_ALC, SERCMDTYPE=SER_CLR_PROCBIDX, PARATYPE=SUBID, INDEX=1, SUBID="2234";
   ```

**SER\_UPM模块**

清除用户控制块。其中“INSTANCENO”为“539738218”。

```
SET DBG: SUBSYSTYPE=SER, INSTANCENO="539738218", SERMT=SER_UPM, SERCMDTYPE=SER_CLR_USERCB, PARATYPE=SUBID, SUBID="1234";
```

**SER\_BINDCFG模块**

1. 执行****DSP SERVICEINFO****查询PES服务实例号。假设“INSTANCENO”为“539738218”。
2. 执行**SET DBG**命令打开在线生效功能。

   ```
   SET DBG: SUBSYSTYPE=SER, INSTANCENO="539738218", SERMT=SER_BINDCFG, SERCMDTYPE=SER_BINDCFG_EFFECTIVEONLINE_ON;
   ```
3. 执行**SET BINDCFG**命令在线修改使其配置立即生效。如PES微服务出现重启，则该配置失效，需要按上述步骤示例重新设置软调。

**SER\_GRPDISTIME(组成员散列时长)**

设置组成员用户定时散列时间。其中“INSTANCENO”为“539738218”。

```
SET DBG: SUBSYSTYPE=SER_SUBGROUP, INSTANCENO="539738218", SERMT=SER_GRPDISTIME, SERCMDTYPE=SER_SET_GRPDISTIME, PARATYPE=SUBID, SUBID="46010381014", DISTIME=10;
```

**SER\_PES****(PES服务)**

强制释放PES服务中主从用户、组用户/组成员用户的资源信息。其中“INSTANCENO”为“539738218”。

```
SET DBG: SUBSYSTYPE=SER_SUBGROUP, INSTANCENO="539738218", SERMT=SER_PES, SERCMDTYPE=SER_CLR_SUBGROUP, PARATYPE=SUBID, SUBID="1234";
```

**SER\_FSMMAXNUM（PES服务自动机最大数量）**

设置PES服务自动机最大数量。其中“INSTANCENO”为“539738218”，“FSMMAXNUM”为“5000”。

```
SET DBG: SUBSYSTYPE=SER, INSTANCENO="539738218", SERMT=SER_FSMMAXNUM, SERCMDTYPE=SER_SET_FSMMAXNUM, FSMMAXNUM=5000;
```