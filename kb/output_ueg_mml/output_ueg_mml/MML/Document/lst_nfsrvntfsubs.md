# 查询服务回调信息（LST NFSRVNTFSUBS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、NEF、NWDAF、SCF**

该命令用于查询服务实例的回调信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                |
|:---------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数  参数含义：本参数用于指定回调信息对应的NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则：  本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。                                                                 |
| SRVINSTANCEID  | 服务实例标识 | 可选必选说明：可选参数  参数含义：本参数用于指定回调信息对应的服务实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则： 本参数与ADD CPNFSERVICE命令中的SRVINSTANCEID值一致时生效。本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，Service_Instance_0。 |
| NTFICATIONTYPE | 通知类型   | 可选必选说明：可选参数  参数含义：本参数用于指定回调URI通知类型。  数据来源：全网规划 取值范围： NtfInvalid（NtfInvalid）N1Msg（N1Msg）N2Info（N2Info）LocNty（LocNty）DataRmvNtf（DataRmvNtf）DataChgNtf（DataChgNtf）NtfMax（NtfMax）  默认值：无  配置原则：无        |

## 使用实例

运营商A需要查询NFINSTANCENAME为AMF\_Instance\_0，SRVINSTANCEID为Service\_Instance\_0的服务实例的回调信息。

```
%%LST NFSRVNTFSUBS: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0";%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
服务实例标识  =  Service_Instance_0
    通知类型  =  N1Msg
     回调URI  =  http://192.168.0.1:80/callbackFunc
  N1消息类别  =  EN1Invalid
  N2消息类别  =  EN2Invalid
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                              |
|:--------|:-----------------------------------|
| NF实例名称  | 本参数用于指定回调信息对应的NF实例名称。              |
| 服务实例标识  | 本参数用于指定回调信息对应的服务实例标识。              |
| 通知类型    | 本参数用于指定回调URI通知类型。                  |
| 回调URI   | 除AMF回调URI由系统自动生成，其余网元可用此参数指定回调URI。 |
| N1消息类别  | 本参数用于指定N1消息类别。                     |
| N2消息类别  | 本参数用于指定N2消息类别。                     |