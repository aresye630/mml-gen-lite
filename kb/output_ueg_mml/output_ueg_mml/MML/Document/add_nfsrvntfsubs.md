# 添加服务回调信息（ADD NFSRVNTFSUBS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、NEF、NWDAF、SCF**

该命令用于添加服务实例回调信息。在NF向NRF注册时，可以针对NF支持的每个服务实例提供默认的通知注册信息（defaultNotificationSubscription），供NF服务生产者向未在NF服务生产者中显式注册的NF服务消费者提供回调URI（Uniform Resource Identifier，通用资源标识符）信息。例如，作为隐式订阅的解决。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                |
|:---------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数  参数含义：本参数用于指定回调信息对应的NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则：  本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。                                                                 |
| SRVINSTANCEID  | 服务实例标识 | 可选必选说明：必选参数  参数含义：本参数用于指定回调信息对应的服务实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则： 本参数与ADD CPNFSERVICE命令中的SRVINSTANCEID值一致时生效。本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型   | 可选必选说明：必选参数  参数含义：本参数用于指定回调URI通知类型。  数据来源：全网规划 取值范围： NtfInvalid（NtfInvalid）N1Msg（N1Msg）N2Info（N2Info）LocNty（LocNty）DataRmvNtf（DataRmvNtf）DataChgNtf（DataChgNtf）NtfMax（NtfMax）  默认值：无  配置原则：无        |
| CALLBACKURI    | 回调URI  | 可选必选说明：可选参数  参数含义：除AMF回调URI由系统自动生成，其余网元可用此参数指定回调URI。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：  优先使用ipv4地址，格式为URI格式，例如：http://192.168.0.1:80/callbackFunc。                                |
| N1MESSAGECLASS | N1消息类别 | 可选必选说明：可选参数  参数含义：本参数用于指定N1消息类别。  数据来源：全网规划 取值范围： EN1Invalid（EN1Invalid）N1Mm（N1Mm）N1Sm（N1Sm）Lpp（Lpp）Sms（Sms）N1Updp（N1Updp）N1Reserved1（N1Reserved1）EN1Max（EN1Max）  默认值：无  配置原则：无                     |
| N2INFOCLASS    | N2消息类别 | 可选必选说明：可选参数  参数含义：本参数用于指定N2消息类别。  数据来源：全网规划 取值范围： EN2Invalid（EN2Invalid）N2Sm（N2Sm）Nrppa（Nrppa）Pws（Pws）PwsBcal（PwsBcal）PwsRf（PwsRf）N2Ran（N2Ran）N2Reserved1（N2Reserved1）EN2Max（EN2Max）  默认值：无  配置原则：无 |

## 使用实例

运营商A需要给NFINSTANCENAME为AMF\_Instance\_0，SRVINSTANCEID为Service\_Instance\_0的服务实例添加回调信息，通知类型为N1Msg，回调URI为http://192.168.0.1:80/callbackFunc。

```
ADD NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=N1Msg, CALLBACKURI="http://192.168.0.1:80/callbackFunc";
```