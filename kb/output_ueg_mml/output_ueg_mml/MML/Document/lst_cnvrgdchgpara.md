# 查询融合计费全局参数（LST CNVRGDCHGPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询融合计费全局参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询融合计费全局参数：

```
%%LST CNVRGDCHGPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                   多UPF场景配额管理  =  独立配额
               漫游用户归属地QBC计费  =  不使能
            位置信息必选信元缺失处理  =  不携带
             ChargingDataRef生成方式  =  CHF生成ChargingDataRef
               携带Start Trigger开关  =  不使能
        IPv6地址Interface Identifier  =  INITITFID
                 RG级Trigger填写方式  =  不使能
                  离线RG时长计算方式  =  PACKETTRIGGERED
             基于GrantedUnit上报用量  =  不使能
        延时上报PDU级Trigger携带方式  =  PDU级不携带
            PDU级门限Trigger适用范围  =  在线计费用户&离线计费用户&融合计费用户
             RG级门限Trigger适用范围  =  离线计费用户&融合计费用户
               RG VT事件合并上报开关  =  不使能
           忽略CHF响应消息的信元列表  =  NULL
       CHF响应消息信元错误的处理动作  =  去活会话
Trigger中是否支持填写AbnormalRelease  =  使能
      控制Nchf消息中时间戳的计算方式  =  四舍五入
          删除动态规则是否通知用户面  =  使能
            忽略CHF下发的Trigger列表  =  NULL
                      无业务上报开关  =  使能
             去活等待更新消息响应开关 =  不使能
            忽略CHF下发非法Triggers  =  使能
            缓存未开启放通告警开关  =  不使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                         | 输出项解释                                                                                                |
|:------------------------------|:-----------------------------------------------------------------------------------------------------|
| 多UPF场景配额管理                    | 该参数用于设置多UPF场景配额管理方式。                                                                                 |
| 漫游用户归属地QBC计费                  | 该参数用于设置漫游用户在归属地是否进行QBC计费。                                                                            |
| 位置信息必选信元缺失处理                  | 设置4、5G切换过程中，位置信息必选信元缺失时的处理方式。                                                                        |
| ChargingDataRef生成方式           | 该参数用于指定融合计费ChargingDataRef的生成方式。需要打开SMF本地缓存融合计费消息的功能时，请指定使用SMF生成。                                    |
| 携带Start Trigger开关             | 该参数用于表示新业务上报场景是否支持在业务容器中携带Start Trigger。                                                             |
| IPv6地址Interface Identifier    | 该参数用于设置N40接口用户IPv6地址interface identifier的填写方式。                                                       |
| RG级Trigger填写方式                | 该参数用于设置当仅对PDU会话有效的Trigger发生时，生成的业务容器是否携带同PDU会话一样的Trigger。                                            |
| 离线RG时长计算方式                    | 该参数用于设置CP指示UP离线RG的时长计费方式。                                                                            |
| 基于GrantedUnit上报用量             | 该参数用于设置是否基于GrantedUnit上报用量。                                                                          |
| 延时上报PDU级Trigger携带方式           | 该参数用于控制延时上报的PDU级Trigger在融合计费请求消息PDU级的携带方式。                                                           |
| PDU级门限Trigger适用范围             | 该参数用于设置PDU级门限Trigger的适用范围。                                                                           |
| RG级门限Trigger适用范围              | 该参数用于设置RG级门限Trigger的适用范围。                                                                            |
| RG VT事件合并上报开关                 | 该参数控制同时发生的RG VT事件合并上报。                                                                               |
| 忽略CHF响应消息的信元列表                | 该参数用于SMF处理CHF响应消息时，忽略CHF下发的指定信元。                                                                     |
| CHF响应消息信元错误的处理动作              | 该参数用于控制CHF的响应消息携带信元错误时SMF的处理动作。                                                                      |
| Trigger中是否支持填写AbnormalRelease | 该参数用于控制Trigger中是否支持填写AbnormalRelease。                                                                |
| 控制Nchf消息中时间戳的计算方式             | 该参数用于控制Nchf消息中时间戳的计算方式。控制的字段包含StartTime、StopTime、invocationTimeStamp。                                |
| 删除动态规则是否通知用户面                 | 该参数用于控制动态规则删除时，SMF是否显式地向UPF指示删除URR。本参数仅控制融合计费使用的，通过动态规则关联的动态URR删除场景。                                 |
| 忽略CHF下发的Trigger列表             | 该参数用于SMF处理CHF响应消息时，忽略CHF下发指定的Trigger控制，使用命令PDUTRIGGER、RGTRIGGER配置的Trigger控制，包含会话级Trigger和RG级Trigger。 |
| 无业务上报开关                       | 该参数用于控制会话级事件发生时，用户当前无业务需要上报的情况下SMF是否需要上报CHF。                                                         |
| ChargingDataRef格式             | 该参数用于配置ChargingDataRef的格式。                                                                           |
| 去活等待更新消息响应开关                  | 该参数用于用户去活时是否需要等待CHF更新请求消息的响应。                                                                        |
| ChargingDataRef使用方式           | 该参数用于指定融合计费ChargingDataRef的使用方式。                                                                     |
| 忽略CHF下发非法Triggers             | 该参数用于控制CHF下发的Triggers包含的所有Trigger均为非法信元时是否要忽略。该参仅控制Triggers信元包含的Trigger数量不为零，且所有的Trigger都存在非法子信元的场景。 |
| 缓存未开启放通告警开关                   | 该参数用于控制是否开启“融合计费用户放通不计费”告警功能。                                                                        |