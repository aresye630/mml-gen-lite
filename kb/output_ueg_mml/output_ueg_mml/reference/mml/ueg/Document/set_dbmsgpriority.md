# 设置DCI消息优先级(SET DBMSGPRIORITY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于设置DCI（DS Call Interface）消息优先级。UDM通过DCI接口（华为私有接口）与USCDB进行通信完成从数据服务子系统获取、修改用户数据。当USCDB出现流控时为防止USCDB丢弃重要消息，通过本命令设置DCI消息优先级，USCDB按照UDM携带的DCI消息优先级流控消息，优先丢弃优先级比较低的消息。

## 注意事项

该命令执行不当会造成业务消息丢失，请谨慎使用。

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-----------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE    | 业务消息     | 用于标识业务消息的类型。其中ULR和AIR为Diameter协议S6a/S6d接口应用层消息，其余均为MAP协议应用层消息。 取值范围：ULR(ULR)AIR(AIR)CANCEL_LOCATION(CANCEL_LOCATION)INSERT_SUBSCRIBER_DATA(INSERT_SUBSCRIBER_DATA)PROVIDE_SUBSCRIBER_INFO(PROVIDE_SUBSCRIBER_INFO)UPDATE_GPRS_LOCATION(UPDATE_GPRS_LOCATION)UPDATE_LOCATION(UPDATE_LOCATION)SEND_ROUTING_INFO_FOR_SM(SEND_ROUTING_INFO_FOR_SM)SEND_ROUTING_INFO_FOR_GPRS(SEND_ROUTING_INFO_FOR_GPRS)SEND_ROUTING_INFO_FOR_LCS(SEND_ROUTING_INFO_FOR_LCS)SEND_ROUTING_INFORMATION(SEND_ROUTING_INFORMATION)SEND_AUTHENTICATION_INFO(SEND_AUTHENTICATION_INFO)SEND_PARAMETERS(SEND_PARAMETERS)DER(DER)AAR(AAR)STR(STR)RTR(RTR)PPR(PPR) 默认值：无。 |
| DBPRIORITY | DCI访问优先级 | 用于标识UDM通过DCI接口访问USCDB消息的优先级。当USCDB出现流控后优先丢弃优先级低的消息。 取值范围：DCI_LOWEST_PRIORITY_MSG(DCI_LOWEST_PRIORITY_MSG)：优先级最低。DCI_LOW_PRIORITY_MSG(DCI_LOW_PRIORITY_MSG)：优先级较低。DCI_NORMAL_PRIORITY_MSG(DCI_NORMAL_PRIORITY_MSG)：优先级适中。DCI_HIGH_PRIORITY_MSG(DCI_HIGH_PRIORITY_MSG)：优先级较高。DCI_HIGHEST_PRIORITY_MSG(DCI_HIGHEST_PRIORITY_MSG)：优先级最高。 默认值：无。                                                                                                                                                                                                                                                                                                 |

## 使用实例

为防止USCDB出现流控时丢弃SEND\_PARAMETERS消息，通过本命令设置“业务消息”为“SEND\_PARAMETERS”消息的“DCI访问优先级”为“DCI\_HIGHEST\_PRIORITY\_MSG(DCI\_HIGHEST\_PRIORITY\_MSG)”：

```
SET DBMSGPRIORITY: MSGTYPE=SEND_PARAMETERS, DBPRIORITY=DCI_HIGHEST_PRIORITY_MSG;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。