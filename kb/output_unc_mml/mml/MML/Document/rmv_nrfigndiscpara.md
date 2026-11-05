# 删除NF服务发现忽略参数规则（RMV NRFIGNDISCPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于删除NF服务发现忽略参数配置。忽略参数被删除后，对应目标NF发现时，NRF会将此参数重新作为发现参数进行目标NF选择。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE      | 网元类型     | 可选必选说明：必选参数  参数含义：该参数用于表示忽略发现参数规则对应的目标NF类型。其中，ALL表示适用于所有目标NF类型。  数据来源：本端规划 取值范围： ALL（表示适用于所有NF类型）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                               |
| IGNDISCPARA | 服务发现忽略参数 | 可选必选说明：必选参数  参数含义：该参数表示NRF忽略的服务发现参数。NRF在处理指定目标NF类型服务发现时，会忽略该发现参数，当做该参数没有携带，匹配其他条件进行服务发现。  数据来源：本端规划 取值范围： PreferredLocality（preferred-locality）ServingScope（serving-scope）PreferredTai（preferred-tai）Tai（tai）Dnn（dnn）Snssais（snssais）Supi（supi）Gpsi（gpsi）RoutingIndicator（routing-indicator）UeIpv4Address（ue-ipv4-address）UeIpv6Prefix（ue-ipv6-prefix）Ipdomain（ip-domain）GroupIdList（group-id-list）TargetPlmnList（target-plmn-list）SmfServingArea（smf-serving-area）MaxPayloadSize（max-payload-size）MaxPayloadSizeExt（max-payload-size-ext）Reserved1（字段预留，为热补丁预留）Reserved2（字段预留，为热补丁预留）Reserved3（字段预留，为热补丁预留）PlmnSpecificSnssaiList（plmn-specific-snssai-list）NwdafEventList（nwdaf-event-list）  默认值：无  配置原则：无 |

## 使用实例

删除网元类型为NRF、服务发现忽略参数为Tai的NF服务发现忽略参数规则。

```
RMV NRFIGNDISCPARA: NFTYPE=NRF, IGNDISCPARA=Tai;
```