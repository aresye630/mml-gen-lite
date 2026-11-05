# 查询VLR网元定时器（LST VLRTIMERPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMSF**

该命令用于查询VLR配置的相关业务定时器信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

运营商希望查询VLR相关的业务定时器信息，执行如下命令：

```
LST VLRTIMERPARA:;
%%LST VLRTIMERPARA:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
等待HLR发送MAP-OPEN Confirm定时器(秒)  =  6
等待HLR发送MAP-INSERT-SUBSCRIBER-DATA Indication定时器(秒)  =  6
          等待HLR响应MAP_UPDATE_LOCATION Confirm定时器(秒)  =  6
                 等待HLR响应MAP_PURGE_MS Confirm定时器(秒)  =  6
	     等待HLR响应MAP-READY-FOR-SM Confirm定时器(秒)  =  6
                        等待注册中心位置更新响应定时器(秒)  =  6
                            等待注册中心查询响应定时器(秒)  =  6
                            等待注册中心分离响应定时器(秒)  =  6
                          MO流程等待MME响应CpAck定时器(秒)  =  6
                        MT流程等待MME Paging响应定时器(秒)  =  6
                         MT流程等待MME Alert响应定时器(秒)  =  6
                             MT流程等待MME CpAck定时器(秒)  =  6
                    MT流程等待MME DELIVER REPORT定时器(秒)  =  6
                   等待NCG响应ChargingDataRequest定时器(秒)  =  6
       
(结果个数 = 1)
```

## 输出结果说明

| 输出项名称                                              | 输出项解释                                                                     |
|:---------------------------------------------------|:--------------------------------------------------------------------------|
| 等待HLR发送MAP-OPEN Confirm定时器(秒)                      | 该定时器用于控制VLR向HLR发送MAP-OPEN Request消息时，等待HLR响应消息的时长。                        |
| 等待HLR发送MAP-INSERT-SUBSCRIBER-DATA Indication定时器(秒) | 该定时器用于控制VLR等待HLR发送MAP-INSERT-SUBSCRIBER-DATA Indication消息的时长。             |
| 等待HLR响应MAP-UPDATE-LOCATION Confirm定时器(秒)           | 该定时器用于控制VLR向HLR发送MAP-UPDATE-LOCATION Request消息时，等待HLR响应消息的时长。该参数暂不生效。     |
| 等待HLR响应MAP-PURGE-MS Confirm定时器(秒)                  | 该定时器用于控制VLR向HLR发送MAP-PURGE-MS Request消息时，等待HLR响应消息的时长。                    |
| 等待HLR响应MAP-READY-FOR-SM Confirm定时器(秒)              | 该定时器用于控制VLR向HLR发送MAP-READY-FOR-SM Request消息时，等待HLR响应消息的时长。                |
| 等待注册中心位置更新响应定时器(秒)                                 | 该定时器用于控制VLR向注册中心发送位置更新请求消息时，等待注册中心响应消息的时长。                                |
| 等待注册中心查询响应定时器(秒)                                   | 该定时器用于控制VLR向注册中心发送查询请求消息时，等待注册中心响应消息的时长。                                  |
| 等待注册中心分离响应定时器(秒)                                   | 该定时器用于控制VLR向注册中心发送分离请求消息时，等待注册中心响应消息的时长。                                  |
| MO流程等待MME响应CpAck定时器(秒)                             | 该定时器用于控制VLR在MO流程等待MME响应CpAck消息的时长。                                        |
| MT流程等待MME Paging响应定时器(秒)                           | 该定时器用于控制VLR在MT流程向MME发送SGsAP-PAGING-REQUEST消息时，等待MME响应消息的时长。               |
| MT流程等待MME Alert响应定时器(秒)                            | 该定时器用于控制VLR在MT流程向MME发送SGsAP-ALERT-REQUEST消息时，等待MME响应消息的时长。                |
| MT流程等待MME CpAck定时器(秒)                              | 该定时器用于控制VLR在MT流程向MME发送携带了CpData的SGsAP-DOWNLINK-UNITDATA消息之后，等待MME响应消息的时长。 |
| MT流程等待MME DELIVER REPORT定时器(秒)                     | 该定时器用于控制在MT流程中VLR等待MME响应DELIVER REPORT消息的时长。                              |
| 等待NCG响应ChargingDataRequest定时器(秒)                   | 该定时器用于控制VLR向NCG发送ChargingDataRequest消息时，等待NCG响应消息的时长。                     |