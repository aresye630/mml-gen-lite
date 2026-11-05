# 显示SMF当前信元携带的信息（DSP CURSMFIEADAPTER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于显示当前SMF在流程中某一协议消息中的信元携带情况。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                           |
|:------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ITFNODEROLE | 接口和网元类型 | 可选必选说明：必选参数  参数含义：该参数用于指定需要控制的接口和网元类型。  数据来源：本端规划 取值范围： “N16_VSMF（N16_VSMF）”：N16接口上本端网元为V-SMF“N16_HSMF（N16_HSMF）”：N16接口上本端网元为H-SMF“N16a_ISMF（N16a_ISMF）”：N16a接口上本端网元为I-SMF“N16a_HSMF（N16a_HSMF）”：N16a接口上本端网元为H-SMF“N7（N7）”：N7接口“N40（N40）”：N40接口“N16_PROXYSMF（N16_PROXYSMF）”：N16接口上本端网元为PROXYSMF  默认值：无  配置原则：无 |
| PROCTYPE    | 流程类型    | 可选必选说明：必选参数  参数含义：该参数用于指定需要控制的流程类型。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~128。  默认值：无  配置原则：无                                                                                                                                                                                                                        |
| PROCMSGID   | 流程消息标识  | 可选必选说明：必选参数  参数含义：该参数用于指定需要控制的流程消息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~128。  默认值：无  配置原则：无                                                                                                                                                                                                                        |

## 使用实例

查询当前VSMF会话创建流程中发送给HSMFN16的创建消息中的信元携带情况，执行如下命令：

```
%%DSP CURSMFIEADAPTER: ITFNODEROLE=N16_VSMF, PROCTYPE="PduSessionEstAsVsmf", PROCMSGID="PostPduSessionsParameters";%%
RETCODE = 0  操作成功

结果如下
------------------------
名称                                                  结果值  

BinaryDatas                                           enable        
PduSessionCreateData                                  enable        
PduSessionCreateData.AddUeLocation                    enable        
PduSessionCreateData.AdditionalAnType                 disable       
PduSessionCreateData.AdditionalCnTunnelInfo           disable       
PduSessionCreateData.AlwaysOnRequested                disable       
PduSessionCreateData.AmfNfId                          enable        
PduSessionCreateData.AnType                           enable        
PduSessionCreateData.ChargingId                       enable        
PduSessionCreateData.DnaiList                         disable       
PduSessionCreateData.Dnn                              enable        
PduSessionCreateData.EpsBearerCtxStatus               disable       
PduSessionCreateData.EpsBearerId                      disable       
PduSessionCreateData.EpsInterworkingInd               enable        
PduSessionCreateData.Gpsi                             enable        
PduSessionCreateData.Guami                            enable        
PduSessionCreateData.HPcfId                           enable        
PduSessionCreateData.HoPreparationIndication          disable       
PduSessionCreateData.HplmnSnssai                      disable       
PduSessionCreateData.ISmfServiceInstanceId            disable       
PduSessionCreateData.IcnTunnelInfo                    disable       
PduSessionCreateData.IsmfId                           disable       
PduSessionCreateData.IsmfPduSessionUri                disable       
PduSessionCreateData.MaxIntegrityProtectedDataRateDl  enable        
PduSessionCreateData.MaxIntegrityProtectedDataRateUl  enable        
PduSessionCreateData.N1SmInfoFromUe                   enable        
PduSessionCreateData.N9ForwardingTunnelInfo           disable       
PduSessionCreateData.OldPduSessionId                  disable       
PduSessionCreateData.PcfId                            disable       
PduSessionCreateData.PduSessionId                     enable        
PduSessionCreateData.Pei                              enable        
PduSessionCreateData.PgwS8CFteid                      disable       
PduSessionCreateData.PresenceInLadn                   enable        
PduSessionCreateData.RatType                          enable        
PduSessionCreateData.RecoveryTime                     disable       
PduSessionCreateData.RequestType                      enable        
PduSessionCreateData.RoamingChargingProfile           enable        
PduSessionCreateData.RoutingIndicator                 enable        
PduSessionCreateData.SNssai                           enable        
PduSessionCreateData.SecondaryRatUsageInfo            disable       
PduSessionCreateData.SelMode                          enable        
PduSessionCreateData.SelectedDnn                      enable        
PduSessionCreateData.ServingNetwork                   enable        
PduSessionCreateData.Supi                             enable        
PduSessionCreateData.SupportedFeatures                enable        
PduSessionCreateData.UdmGroupId                       enable        
PduSessionCreateData.UeLocation                       enable        
PduSessionCreateData.UeTimeZone                       enable        
PduSessionCreateData.UnauthenticatedSupi              enable        
PduSessionCreateData.UnknownN1SmInfo                  disable       
PduSessionCreateData.UpSecurityInfo                   disable       
PduSessionCreateData.VSmfServiceInstanceId            disable       
PduSessionCreateData.VcnTunnelInfo                    enable        
PduSessionCreateData.VplmnQos                         enable        
PduSessionCreateData.VsmfId                           enable        
PduSessionCreateData.VsmfPduSessionUri                enable        
(结果个数 = 56)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 名称      | 查询结果名称。 |
| 结果值     | 查询的结果值。 |