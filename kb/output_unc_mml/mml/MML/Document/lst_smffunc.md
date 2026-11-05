# 查询SMF扩展功能（LST SMFFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询会话管理相关的功能控制，如是否支持兴趣区、是否支持本地数据网络、支持哪种业务和会话连续性模式等参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询所有SMFFUNC记录：

```
%%LST SMFFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                                    兴趣区  =  不支持
                                  本地网络  =  不支持
                              本地网络策略  =  释放
                                   SSC模式  =  模式一
                  SMF是否支持向AMF分配EBID  =  支持
                   是否支持PaaMask私有信元  =  支持
                   是否支持QerType私有信元  =  不支持
                        IPv6本地UP分流策略  =  BP优先
                            SMF是否支持BSF  =  不支持
                        SMF是否支持AMF容灾  =  不支持
                 是否去激活故障AMF上的用户  =  不支持
         SMF是否支持隐式去订阅签约数据通知  =  不支持
            订阅签约数据通知超时时间(分钟)  =  1440
                                UE可达功能  =  不支持
                  是否在EPS获取签约的NSSAI  =  否
                       SMF是否支持野卡接入  =  不支持
                               PPI功能开关  =  使能
                 故障原因值重选UPF功能开关  =  不使能
                        事件订阅与上报功能  =  不支持
                    是否支持建立5G LAN会话  =  不支持
                        跨切片保护功能开关  =  关闭
                             V-SMF特性开关  =  不支持
                             QoS流通知控制  =  不支持
                       AMF服务发现控制开关  =  不使能
        5G LAN会话是否向UDM查询VnGroupData  =  支持
                       冗余PDU会话特性开关  =  不支持
                             I-SMF核查开关  =  关闭
                            RedCap特性开关  =  不支持
              通用DNN会话UE IP地址处理开关  =  不支持
       SMF支持基于binding的AMF热备特性开关  =  支持
                        ProxySMFS8特性开关  =  不支持
BSF支持基于DNN过滤查询会话绑定信息特性开关  =  不支持
                      访地专网策略处理开关  =  不支持
     SMF支持异厂商信令安全网关热备特性开关  =  不支持
                           N16aSMF核查开关  =  关闭
                      网络切片替换功能开关  =  不支持
  WLAN切换NG-RAN失败转EPS FallBack功能开关  =  不支持
                           PDU Set Qos开关  =  不支持
         PacketDelayBudget信元下发控制开关  =  不支持
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                           | 输出项解释                                                                                                                                                                                                                                                                                                                                                         |
|:--------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 兴趣区                             | 该参数用于指定SMF是否支持兴趣区。若SMF支持兴趣区，PCF等网元可以向SMF订阅兴趣区，当UE进出这些兴趣区的时候，SMF会通知订阅的网元。                                                                                                                                                                                                                                                                                      |
| 本地网络                            | 该参数用于指定SMF是否支持本地数据网络。一个本地数据网络的PDU会话仅能在特定LADN Service Area内接入DN。                                                                                                                                                                                                                                                                                               |
| 本地网络策略                          | 该参数用于指定本地数据网络策略，即用户离开本地数据网络服务区域时，SMF的处理策略。                                                                                                                                                                                                                                                                                                                    |
| SSC模式                           | 该参数用于指定SMF支持的业务和会话连续性模式。                                                                                                                                                                                                                                                                                                                                      |
| SMF是否支持向AMF分配EBID               | 该参数用于指定SMF是否支持4G。                                                                                                                                                                                                                                                                                                                                             |
| 是否支持PaaMask私有信元                 | 该参数用于指定SMF是否支持PaaMask私有信元。                                                                                                                                                                                                                                                                                                                                    |
| 是否支持QerType私有信元                 | 该参数用于指定SMF是否支持QerType私有信元。                                                                                                                                                                                                                                                                                                                                    |
| IPv6本地UP分流策略                    | 该参数用于指定IPv6本地UP分流策略。在5G场景下，UE可以有多个路径访问目标DN。比如归属地为上海的用户来到北京，可以在上海锚点不变的情况下，通过北京的UP来分流，进而访问北京的DN。在选择UP时，有两种选项：一个是多个分流路径是平等的，都是主锚点，即Bp；另一种是多个分流路径中，一个为主锚点，其余为辅锚点，主锚点UPF不变，辅锚点路径可变，即ULCL。IPv4由于地址紧缺，只支持ULCL。IPv6场景下，选择UP时，可以选择使用Bp还是ULCL。                                                                                                                          |
| SMF是否支持BSF                      | 该参数用于指定SMF是否支持BSF。                                                                                                                                                                                                                                                                                                                                            |
| SMF是否支持AMF容灾                    | 该参数用于控制SMF是否支持AMF容灾功能，当该参数配置Support时，当主AMF故障，SMF会重选AMF；当该参数配置成NotSupport时，当主AMF故障，SMF不会重选AMF。                                                                                                                                                                                                                                                                 |
| 是否去激活故障AMF上的用户                  | 该参数用于控制AMF故障且无备份时，是否去激活该AMF上的用户；若配置为Support，则去激活用户，若为NotSupport，则不去激活。                                                                                                                                                                                                                                                                                        |
| SMF是否支持隐式去订阅签约数据通知              | 该参数用于控制SMF在发送签约数据订阅通知请求消息中implicitUnsubscribe的值。配置为Support，则表示implicitUnsubscribe的值为true；配置为NotSupport，则表示implicitUnsubscribe的值为false。                                                                                                                                                                                                                        |
| 订阅签约数据通知超时时间(分钟)                | 该参数用于设置SMF在签约数据订阅通知消息中implicitUnsubscribe的值为false时，请求的签约数据订阅通知超时时间。                                                                                                                                                                                                                                                                                           |
| UE可达功能                          | 该参数用于控制SMF是否支持UE可达功能。当该参数配置Support时，当SMF作为N16aSMF，SMF会向UDM订阅UE可达事件，用于UDM修改签约数据发起PDU修改时，如果UE不可达，SMF缓存UDM发起的修改签约数据内容；当UE可达后，UDM或者AMF把UE可达事件通知SMF，SMF重新发起PDU修改；当该参数配置成NotSupport时，SMF不会向UDM订阅UE可达事件。                                                                                                                                                             |
| 是否在EPS获取签约的NSSAI                | 该参数用于5G用户在EPS网络建立PDN连接时，控制SMF是否向UDM获取签约的切片和DNN。                                                                                                                                                                                                                                                                                                               |
| SMF是否支持野卡接入                     | 该参数用于控制SMF是否支持野卡接入。配置为Support，则表示支持野卡接入；配置为NotSupport，则表示不支持野卡接入。                                                                                                                                                                                                                                                                                             |
| PPI功能开关                         | 该参数用于指定PPI（寻呼策略指示）功能开关。                                                                                                                                                                                                                                                                                                                                       |
| 故障原因值重选UPF功能开关                  | 该参数用于在U面分配用户地址且非AAA鉴权场景下控制是否基于故障原因值重选UPF。故障原因值由SMF和UPF协商配置，其中SMF配置命令为ADD RESELECTUPCAUSE。                                                                                                                                                                                                                                                                     |
| 事件订阅与上报功能                       | 该参数用于控制SMF是否支持事件订阅和上报功能。                                                                                                                                                                                                                                                                                                                                      |
| 是否支持建立5G LAN会话                  | 该参数用于控制SMF是否支持建立5G LAN会话。                                                                                                                                                                                                                                                                                                                                     |
| 跨切片保护功能开关                       | 该参数用于控制SMF是否打开跨切片保护功能。当跨切片保护功能打开时，SMF给NRF发Token Request消息时携带Requester Snssais，并且SMF收到其他NF发的Http请求消息时，检查切片是否为本NF支持的切片。                                                                                                                                                                                                                                         |
| V-SMF特性开关                       | 该参数用于指定V-SMF功能开关。                                                                                                                                                                                                                                                                                                                                             |
| QoS流通知控制                        | 该参数用于指定SMF是否支持QoS流通知控制功能。若SMF支持QoS流通知控制，PCF等网元可以向SMF订阅该功能，当RAN上报QoS流通知时，SMF会通知订阅的网元。                                                                                                                                                                                                                                                                          |
| AMF服务发现控制开关                     | 该参数用于控制4到5切换、XN切换、N2切换和移动注册更新插入I-SMF/V-SMF或者改变I-SMF/V-SMF流程中，I-SMF/V-SMF是否向NRF发送一个Nnrf_NFDiscovery_Request消息来查询AMF以获取AMF的IP地址等信息。                                                                                                                                                                                                                             |
| 5G LAN会话是否向UDM查询VnGroupData     | 该参数用于控制5G LAN场景下，当UDM在签约数据中携带5G LAN组ID时，SMF是否支持基于SharedDataId向UDM发送一次Nudm_SDM_GetSharedData Request查询消息来获取VnGroupData。若配置为Support时，当UDM返回的签约数据中包括5G LAN组ID和SharedDataID时，SMF会基于SharedDataID向UDM发送一次查询消息来查询该5G LAN组ID对应的VnGroupData。如果UDM返回的签约数据中不包括5G LAN组ID和SharedDataID，则不发起查询。若配置为NotSupport时，无论UDM返回的签约数据中是否包括5G LAN组ID和SharedDataID，都不发起查询。智家随行功能也使用此字段。 |
| 冗余PDU会话特性开关                     | 该参数用于控制SMF是否支持冗余PDU会话功能。                                                                                                                                                                                                                                                                                                                                      |
| I-SMF核查开关                       | 该参数用于表示N16aSMF发起的数据一致性核查功能开关。当该开关打开时，N16aSMF进行数据一致性核查，N16aSMF给I-SMF发送Nsmf_PDUSession_Update Request消息，根据返回消息判断会话数据是否一致。当该开关关闭时，N16aSMF不进行数据一致性核查。                                                                                                                                                                                                             |
| RedCap特性开关                      | 该参数用于控制SMF是否支持RedCap功能。                                                                                                                                                                                                                                                                                                                                       |
| 通用DNN会话UE IP地址处理开关              | 该参数用于指定通用DNN漫游分流场景下，专网SMF是否支持处理N16a口携带的通用DNN会话的UE IP地址（扩展私有字段），并下发给专网会话的锚点UPF，指示专网UPF做UE IP地址NAT转换。                                                                                                                                                                                                                                                           |
| SMF支持基于binding的AMF热备特性开关        | 该参数用于控制SMF是否支持基于binding的AMF热备。                                                                                                                                                                                                                                                                                                                                |
| ProxySMFS8特性开关                  | 该参数用于指定ProxySMFS8功能开关。                                                                                                                                                                                                                                                                                                                                        |
| BSF支持基于DNN过滤查询会话绑定信息特性开关        | 该参数用于指定BSF支持基于DNN过滤查询会话绑定信息特性开关。                                                                                                                                                                                                                                                                                                                              |
| 访地专网策略处理开关                      | 该参数用于指定SMF是否支持N11口中携带的访地专网策略控制处理。                                                                                                                                                                                                                                                                                                                             |
| SMF支持异厂商信令安全网关热备特性开关            | 该参数用于控制SMF是否支持对接异厂商信令安全网关场景下的热备特性。                                                                                                                                                                                                                                                                                                                            |
| N16aSMF核查开关                     | 该参数用于表示I-SMF发起的数据一致性核查功能开关。当该开关打开时，I-SMF进行数据一致性核查，I-SMF给N16aSMF发送Nsmf_PDUSession_Update Request消息，根据返回消息判断会话数据是否一致。当该开关关闭时，I-SMF不进行数据一致性核查。                                                                                                                                                                                                                   |
| 网络切片替换功能开关                      | 该参数用于控制SMF是否支持网络切片替换功能。                                                                                                                                                                                                                                                                                                                                       |
| WLAN切换NG-RAN失败转EPS FallBack功能开关 | 该参数用于控制SMF是否支持WLAN切换NG-RAN失败转EPS FallBack功能。                                                                                                                                                                                                                                                                                                                  |
| PDU Set Qos开关                   | 该参数用于控制SMF是否支持传递PDU Set Qos相关参数。                                                                                                                                                                                                                                                                                                                              |
| PacketDelayBudget信元下发控制开关       | 该参数用于控制标准5QI规则是否支持通过Dynamic 5QI下发PacketDelayBudget信元。                                                                                                                                                                                                                                                                                                         |