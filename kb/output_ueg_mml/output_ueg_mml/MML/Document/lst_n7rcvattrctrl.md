# 查询N7接收信元处理控制（LST N7RCVATTRCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

此命令用于查询N7接口接收到的消息中部分信元的处理方式。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询N7RcvAttrCtrl的值。

```
%%LST N7RCVATTRCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                 无PacketFilterUsage  =  不发送Packet Fliter给UE
                 修改QoSData关键属性  =  修改QoSFlow
                 缺省QosRule生成方法  =  PCC规则
基于Notify消息ResourceURI触发PCF重选  =  不使能
            SCELL_CH是否允许上报NCGI  =  不使能
          是否使用PCF返回的URI进行转发 = 不使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                        | 输出项解释                                                                                                                        |
|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| 无PacketFilterUsage           | 设置从N7接口收到的flowInfos属性中不包含PacketFilterUsage属性时的处理。                                                                            |
| 修改QoSData关键属性                | 该参数用于设置当收到PCF修改QoSData关键属性消息时是更新QoSFlow还是删除当前QoSFlow重新创建QoSFlow。关键属性包括：5QI，Arp，QNC，priorityLevel，averWindow和maxDataBurstVol。 |
| 缺省QosRule生成方法                | 该参数用于设置生成缺省QosRule的方法。                                                                                                       |
| 基于Notify消息ResourceURI触发PCF重选 | 该参数用于设置当收到PCF发送的UpdateNotify携带的ResourceURI与当前会话使用的PCF不同时，是否允许触发PCF重选。                                                        |
| SCELL_CH是否允许上报NCGI           | 该参数用于控制当PCF下发SCELL_CH trigger或USER_LOCATION_CH trigger时，是否支持在NCGI变化时向PCF发送NCGI值。                                             |
| 是否使用PCF返回的URI进行转发            | 该参数用于设置当收到PCF发送的激活响应的消息头中携带URI变化时，是否使用响应消息中的URI用于后续消息发送。                                                                     |