# 查询事件订阅通知消息的兼容性控制参数（LST AMFEVENTCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF事件订阅的兼容性控制参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询AMF事件订阅的兼容性参数，执行如下命令。

```
%%LST AMFEVENTCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                        UE当前驻留的基站全局标识  =  否
位置事件上报ageOfLocationInformation信元携带开关  =  否
位置事件上报ageOfLocationInformation信元填充策略  =  向下取整
    Inter移动性流程reportUeReachable信元携带开关  =  否
  下行数据可达事件上报accessTypeList信元携带开关  =  否
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                                | 输出项解释                                                                                                                                                                                                   |
|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UE当前驻留的基站全局标识                        | 该参数用于控制上报事件订阅类型为LOCATION_REPORT、PRESENCE_IN_AOI_REPORT的通知消息时，是否携带UE当前驻留的基站全局标识。                                                                                                                         |
| 位置事件上报ageOfLocationInformation信元携带开关 | 该参数用于控制用户事件订阅类型为位置事件上报（LOCATION_REPORT）时，AMF是否在location中携ageOfLocationInformation信元。                                                                                                                    |
| 位置事件上报ageOfLocationInformation信元填充策略 | 该参数用于控制用户事件订阅类型为位置事件上报（LOCATION_REPORT）时，AMF针对用户位置信息非实时获取的场景下ageOfLocationInfo不足1分钟的处理策略。                                                                                                               |
| Inter移动性流程reportUeReachable信元携带开关    | 该参数用于控制AMF间移动性流程中源测AMF是否在ueContext中携带reportUeReachable信元。 该参数设置为YES，若用户事件订阅类型为可达事件上报（REACHABILITY_REPORT）且reachabilityFilter取值为UE_REACHABLE_DL_TRAFFIC，用户发起AMF间移动性流程，源测AMF携带reportUeReachable信元取值为true。 |
| 下行数据可达事件上报accessTypeList信元携带开关       | 该参数用于控制AMF上报下行数据可达事件时是否携带accessTypeList信元。 该参数设置为YES，若用户事件订阅类型为可达事件上报（REACHABILITY_REPORT）且reachabilityFilter取值为UE_REACHABLE_DL_TRAFFIC，当用户切换至连接态或可寻呼状态时，AMF上报下行数据可达事件携带accessTypeList信元。               |