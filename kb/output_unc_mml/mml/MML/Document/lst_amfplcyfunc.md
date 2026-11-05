# 查询AMF策略功能（LST AMFPLCYFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF策略功能。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询AMF策略功能，执行如下命令：

```
%%LST AMFPLCYFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
        AM策略关闭实时通知PCF开关  =  是
        UE策略关闭实时通知PCF开关  =  是
            N14接口是否传递AM策略  =  是
                 灵活选频功能开关  =  是
                     RFSP清除方式  =  未携带RFSP
                         默认RFSP  =  0
               是否开启动态NI功能  =  是
                   默认运营商全称  =  FullName
                   默认运营商简称  =  ShortName
                 重叠区域生效策略  =  公网区域
             相邻位置区域处理开关  =  否
               高铁AM偶联老化开关  =  否
          高铁AM偶联老化时长(min)  =  120
            N14接口是否传递UE策略  =  是
           延迟释放AM策略偶联开关  =  是
                   AM偶联老化开关  =  是
              AM偶联老化时长(min)  =  120
                   hpcfId更新开关  =  否
                   hpcfId更新策略  =  随签约数据变更流程更新
       服务发现H-PCF时间间隔(min)  =  30
      AM策略更新失败后是否重选PCF  =  否
AM策略更新失败后重选PCF的流程类型  =  Xn切换 & Intra N2切换不伴随移动注册 & 服务请求
  AM策略更新失败重试时间间隔(min)  =  30
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称               | 输出项解释                                                                                                                                                                                                                                                                                |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM策略关闭实时通知PCF开关     | 该参数用于指示AMF关闭指定的用户（群）创建AM策略偶联功能时，对于已经建立AM策略偶联的用户是否实时向PCF通知删除AM策略偶联。                                                                                                                                                                                                                   |
| UE策略关闭实时通知PCF开关     | 该参数用于指示AMF关闭指定的用户（群）创建UE策略偶联功能时，对于已经建立UE策略偶联的用户是否实时向PCF通知删除UE策略偶联。                                                                                                                                                                                                                   |
| N14接口是否传递AM策略       | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否给新侧AMF传递AM策略信息。                                                                                                                                                                                                                                    |
| 灵活选频功能开关            | 该参数用于设置是否开启灵活选频功能。                                                                                                                                                                                                                                                                   |
| RFSP清除方式            | 该参数用于设置清除PCF签约RFSP方式。                                                                                                                                                                                                                                                                |
| 默认RFSP              | 该参数用于设置PCF签约的RFSP被清除后，AMF给基站下发的RFSP。                                                                                                                                                                                                                                                 |
| 是否开启动态NI功能          | 该参数用于配置是否开启动态NI功能。此功能对应动态UE Logo下发功能。                                                                                                                                                                                                                                                |
| 默认运营商全称             | 该参数用于指定移动网络运营商的全称。AM-PCF取消动态NI时，下发给UE的Configuration Update Command消息中携带的“Full name for network”信元值来源于本参数。                                                                                                                                                                            |
| 默认运营商简称             | 该参数用于指定移动网络运营商的简称。AM-PCF取消动态NI时，下发给UE的Configuration Update Command消息中携带的“Short name for network”信元值优先来源于本参数。                                                                                                                                                                         |
| 重叠区域生效策略            | 该参数用于指定高铁和公网区域重叠时，区域的生效类型。                                                                                                                                                                                                                                                           |
| 相邻位置区域处理开关          | 该参数用于设置是否开启相邻位置区域处理功能。开关开启时，公网用户在两个连续公网区域MecArea1和MecArea2之间移动，若MecArea1和MecArea2的PCF发现参数servingscope不相同，AMF先释放MecArea1的AM偶联，再建立MecArea2的AM偶联；若MecArea1和MecArea2的PCF发现参数servingscope相同，AMF复用AM偶联策略且不受本开关控制。                                                                          |
| 高铁AM偶联老化开关          | 该参数用于设置是否开启高铁AM偶联老化功能。开关开启，当用户离开高铁区域后，AM-PCF没有通知AMF删除AM偶联且"高铁AM偶联老化时长"超时后，AMF释放残留的AM偶联策略。当该开关打开时，本功能仅针对ADD MECAREA命令且参数“AREATYPE”配置为“HIGH_RAIL_AREA”的场景下创建的AM偶联进行老化。                                                                                                                 |
| 高铁AM偶联老化时长(min)     | 该参数用于设置高铁AM偶联老化时长。当用户离开高铁区域后，AM-PCF没有通知AMF删除AM偶联且该参数超时后，AMF释放残留的AM偶联策略。                                                                                                                                                                                                              |
| N14接口是否传递UE策略       | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否给新侧AMF传递UE策略信息。                                                                                                                                                                                                                                    |
| 延迟释放AM策略偶联开关        | 该参数用于指示AMF是否支持AM-PCF下发的AM策略偶联延迟释放功能。                                                                                                                                                                                                                                                 |
| AM偶联老化开关            | 该参数用于设置是否开启AM偶联老化功能。开关开启，当用户离开MEC区域后，AM-PCF没有通知AMF删除AM偶联且"AM偶联老化时长"超时后，AMF释放残留的AM偶联策略。当该开关打开时，本功能仅针对ADD MECAREA命令且参数“AREATYPE”配置为“PUBLIC_AREA”的场景下创建的AM偶联进行老化。                                                                                                                       |
| AM偶联老化时长(min)       | 该参数用于设置AM偶联老化时长。当用户离开MEC区域后，AM-PCF没有通知AMF删除AM偶联且该参数超时后，AMF释放残留的AM偶联策略。                                                                                                                                                                                                               |
| hpcfId更新开关          | 该参数用于指示当满足以下条件时AMF是否对跨省漫游用户服务发现H-PCF并向AM-PCF发送Npcf_AMPolicyControl_Update Request消息，消息中携带hpcfId，具体条件为： （1）ADD AMUEPLCYCTRL命令中参数“DNNAMPLCYSW”为“YES”； （2）ADD PCFSELPLCY命令中参数“CROSSPROVSW”设置为“YES”； （3）跨省漫游用户签约的DNN与ADD AMUEPLCYCTRL命令中的参数“DNNAMPLCYKEYWD”一致，且AMF未向当前注册AM-PCF下发过hpcfId。 |
| hpcfId更新策略          | 该参数用于指示hPcfId的更新策略。                                                                                                                                                                                                                                                                  |
| 服务发现H-PCF时间间隔(min)  | 该参数用于指定跨省漫游用户在AMF服务发现H-PCF失败时，后续AM策略更新流程中重新服务发现H-PCF的最小时间间隔。                                                                                                                                                                                                                         |
| AM策略更新失败后是否重选PCF    | 该参数用于指定当AMF向PCF发送AM策略偶联更新请求消息且对端返回状态码为5xx时是否重选PCF。 本参数设置为“YES”，AMF向PCF发送AM策略偶联更新请求消息且对端返回状态码为5xx时，AMF重新选择PCF并向新的PCF发送Npcf_AMPolicyControl_AmPolicyAssociationCreate Request消息。服务发现PCF失败或AM策略偶联创建失败后不再重试，失败后AMF的处理按照ADD AMUEPLCYCTRL中AMFAILPLCY参数取值生效。                                |
| AM策略更新失败后重选PCF的流程类型 | 该参数用于指定AM策略更新失败后AMF重选PCF的流程类型。                                                                                                                                                                                                                                                       |
| AM策略更新失败重试时间间隔(min) | 该参数用于指定AM策略更新失败且重选PCF失败时，再次重选PCF的最小时间间隔。                                                                                                                                                                                                                                             |