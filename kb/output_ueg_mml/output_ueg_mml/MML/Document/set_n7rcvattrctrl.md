# 设置N7接收信元处理控制（SET N7RCVATTRCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于设置对接收到的N7接口消息中部分信元的处理方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOPKTFLTUSAGE     | MODQOSKEYATTR   | DFTQOSRULEGEN   | NTFRSRURI   | SCELLCHNR   | RSPLOCURI   |
|:------------------|:----------------|:----------------|:------------|:------------|:------------|
| SEND_PKTFLT_TO_UE | MOD_QOSFLOW     | PCC_RULE        | DISABLE     | DISABLE     | DISABLE     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                         | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------|:-----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NOPKTFLTUSAGE | 无PacketFilterUsage           | 可选必选说明：可选参数  参数含义：设置从N7接口收到的flowInfos属性中不包含PacketFilterUsage属性时的处理。  数据来源：本端规划 取值范围： “NOT_SEND_PKTFLT_TO_UE（不发送Packet Fliter给UE）”：对于PCF下发的动态规则，当PCF没有下发packFilterUsage属性时，SMF不将FlowInformation映射成的Filter推送给UE。注意：当规则上的Filter均没有推送给UE时，才允许PCF为该规则指定激活或去活时间，否则规则将安装失败。“SEND_PKTFLT_TO_UE（发送Packet Fliter给UE）”：对于PCF下发的动态规则，当PCF没有下发packFilterUsage属性时，SMF都将FlowInformation映射成的Filter推送给UE。注意：当规则上的Filter均没有推送给UE时，才允许PCF为该规则指定激活或去活时间，否则规则将安装失败。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：无 |
| MODQOSKEYATTR | 修改QoSData关键属性                | 可选必选说明：可选参数  参数含义：该参数用于设置当收到PCF修改QoSData关键属性消息时是更新QoSFlow还是删除当前QoSFlow重新创建QoSFlow。关键属性包括：5QI，Arp，QNC，priorityLevel，averWindow和maxDataBurstVol。  数据来源：本端规划 取值范围： “MOD_QOSFLOW（修改QoSFlow）”：根据PCF下发的QoS关键属性修改QoSFlow。“DEL_ADD_QOSFLOW（删除原有QoSFlow，新建QoSFlow）”：删除原有QoSFlow，新建QoSFlow。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                              |
| DFTQOSRULEGEN | 缺省QosRule生成方法                | 可选必选说明：可选参数  参数含义：该参数用于设置生成缺省QosRule的方法。  数据来源：本端规划 取值范围： “PCC_RULE（PCC规则）”：优先选择安装到缺省qosflow中match-all类型的PccRule作为缺省QosRule。如果缺省qosflow没有安装match-all类型的PccRule，并且PCF下发了预定义规则或者ADC规则，SMF生成match-all类型的PccRule作为缺省QosRule；否则选择优先级最低的PccRule作为缺省QosRule。“MATCH_ALL_RULE（匹配所有流的规则）”：优先选择安装到缺省qosflow中match-all类型的PccRule作为缺省QosRule。如果缺省qosflow没有安装match-all类型的PccRule，SMF生成match-all类型的PccRule作为缺省QosRule。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：无                                        |
| NTFRSRURI     | 基于Notify消息ResourceURI触发PCF重选 | 可选必选说明：可选参数  参数含义：该参数用于设置当收到PCF发送的UpdateNotify携带的ResourceURI与当前会话使用的PCF不同时，是否允许触发PCF重选。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：忽略PCF发送的UpdateNotify携带的ResourceURI，不触发PCF重选。“ENABLE（使能）”：根据PCF发送的UpdateNotify携带的ResourceURI触发PCF重选。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                    |
| SCELLCHNR     | SCELL_CH是否允许上报NCGI           | 可选必选说明：可选参数  参数含义：该参数用于控制当PCF下发SCELL_CH trigger或USER_LOCATION_CH trigger时，是否支持在NCGI变化时向PCF发送NCGI值。  数据来源：对端协商 取值范围： “DISABLE（不使能）”：PCF下发SCELL_CH trigger时不支持上报NCGI。“ENABLE（使能）”：PCF下发SCELL_CH trigger时支持上报NCGI。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                |
| RSPLOCURI     | 是否使用PCF返回的URI进行转发            | 可选必选说明：可选参数  参数含义：该参数用于设置当收到PCF发送的激活响应的消息头中携带URI变化时，是否使用响应消息中的URI用于后续消息发送。  数据来源：全网规划  取值范围：如需向新的URI标识的PCF进行转发，请使能该参数。 “DISABLE（不使能）”：当收到PCF发送的激活响应的消息头中携带URI变化时，不使用响应消息中的URI用于后续消息发送。“ENABLE（使能）”：当收到PCF发送的激活响应的消息头中携带URI变化时，使用响应消息中的URI用于后续消息发送。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。  配置原则：  该参数使能时，更新或去活失败时不进行Failover。                                                                                                                                                                 |

## 使用实例

假设与UNC对接的PCF未遵循3GPP协议，对于需要给UE下发packet filter的场景不携带PacketUsageFilter属性，运营商可以通过设置此命令实现UNC对于不携带PacketUsageFilter属性的场景默认向UE推送Packet Filter。

```
%%SET N7RCVATTRCTRL: NOPKTFLTUSAGE=NOT_SEND_PKTFLT_TO_UE;%%
RETCODE = 0  Operation succeeded
```