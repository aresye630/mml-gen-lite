# 删除服务回调信息（RMV NFSRVNTFSUBS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、NEF、NWDAF、SCF**

该命令用于删除服务实例的回调信息。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                |
|:---------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数  参数含义：本参数用于指定回调信息对应的NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则：  本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。                                                                 |
| SRVINSTANCEID  | 服务实例标识 | 可选必选说明：必选参数  参数含义：本参数用于指定回调信息对应的服务实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则： 本参数与ADD CPNFSERVICE命令中的SRVINSTANCEID值一致时生效。本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型   | 可选必选说明：必选参数  参数含义：本参数用于指定回调URI通知类型。  数据来源：全网规划 取值范围： NtfInvalid（NtfInvalid）N1Msg（N1Msg）N2Info（N2Info）LocNty（LocNty）DataRmvNtf（DataRmvNtf）DataChgNtf（DataChgNtf）NtfMax（NtfMax）  默认值：无  配置原则：无        |

## 使用实例

运营商A需要删除NFINSTANCENAME为AMF\_Instance\_0，SRVINSTANCEID为Service\_Instance\_0的服务实例下通知类型为N1Msg的回调信息。

```
RMV NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=N1Msg;
```