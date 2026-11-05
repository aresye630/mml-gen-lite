# 测试服务发现（TST NFDISC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于测试本NRF的服务发现流程，并呈现服务发现结果。

服务发现参数在此命令中输入格式要求及参考信息如下：

此命令服务发现参数输入格式与服务发现消息中的JSON格式有一定差异，需要将标准JSON格式报文中的" " 用\进行转义。

例如：根据targetNfType，requesterNfType进行服务发现，标准的JSON格式如下{"targetNfType":4,"requesterNfType":3}，转义后的结果（即此命令参数需要输入格式）为{\"targetNfType\":4,\"requesterNfType\":3}。

此命令参数中针对枚举字段的取值进行了整数的替换对应。服务发现参数中涉及的枚举值与其对应的整数如下：

NFType:

NRF = 1。

UDM = 2。

AMF = 3。

SMF = 4。

AUSF = 5。

NEF = 6。

PCF = 7。

SMSF = 8。

NSSF = 9。

UDR = 10。

LMF = 11。

GMLC = 12。

5G\_EIR = 13。

SEPP = 14。

UPF = 15。

N3IWF = 16。

AF = 17。

UDSF = 18。

BSF = 19。

CHF = 20。

NWDAF = 21。

PCSCF = 22。

CUSTOM\_OCS = 23。

ServiceName:

nnrfNfm = 1。

nnrfDisc = 2。

nudmSdm = 3。

nudmUecm = 4。

nudmUeau = 5。

nudmEe = 6。

nudmPp = 7。

namfComm = 8。

namfEvts = 9。

namfMt = 10。

namfLoc = 11。

nsmfPdusession = 12。

nsmfEventExposure = 13。

nausfAuth = 14。

nausfSorprotection = 15。

nausfUpuprotection = 16。

nnefPfdmanagement = 17。

npcfAmPolicyControl = 18。

npcfSmpolicycontrol = 19。

npcfPolicyauthorization = 20。

npcfBdtpolicycontrol = 21。

npcfEventexposure = 22。

npcfUePolicyControl = 23。

nsmsfSms = 24。

nnssfNsselection = 25。

nnssfNssaiavailability = 26。

nudrDr = 27。

nlmfLoc = 28。

n5gEirEic = 29。

nbsfManagement = 30。

nchfSpendinglimitcontrol = 31。

nchfConvergedcharging = 32。

nnwdafEventssubscription = 33。

nnwdafAnalyticsinfo = 34。

nocsSpendinglimitcontrol = 35。

nocsConvergedcharging = 36。

ngmlcLoc = 37。

DataSetId:

SUBSCRIPTION = 1。

POLICY = 2。

EXPOSURE = 3。

APPLICATION = 4。

PduSessionType:

IPV4 = 1。

IPV6 = 2。

IPV4V6 = 3。

UNSTRUCTURED = 4。

ETHERNET = 5。

AccessType:

3GPP\_ACCESS = 1。

NON\_3GPP\_ACCESS = 2。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                     |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DISCINPUTSTR | 服务发现参数 | 可选必选说明：必选参数  参数含义：该参数表示服务发现的输入参数，按照JSON格式组装报文。 服务发现包含的参数请参考《5G Core信令分析》中的“Nnrf_NFDiscovery specific Data Types”。服务发现参数中target-nf-type，requester-nf-type字段为必选，其余为可选参数。  数据来源：本端规划  取值范围：任意类型，取值范围是0~5120。  默认值：无  配置原则：无 |

## 使用实例

AMF向NRF发起服务发现请求，发现SMF。发现请求中携带参数targetNfType，requesterNfType，snssais，dnn，其中SMF作为nfType的枚举值对应的整数是4，AMF作为nfType的枚举值对应的整数是3，支持的切片信息为sst =1 sd = 010101，支持的dnn为huawei.com。

```
TST NFDISC: DISCINPUTSTR="{\"targetNfType\":4,\"requesterNfType\":3,\"snssais\":[{\"sst\":1,\"sd\":\"010101\"}],\"dnn\":\"huawei.com\"}";
%%TST NFDISC: DISCINPUTSTR="{\"targetNfType\":4,\"requesterNfType\":3,\"snssais\":[{\"sst\":1,\"sd\":\"010101\"}],\"dnn\":\"huawei.com\"}";%%
RETCODE = 0  操作成功

结果如下
------------------------ 
服务发现结果     
{
    "NF Discovery InstanceID List": [
        "ff01-1"
    ]
}
{
    "NF Discovery Profile List": [
        {
            "capacity": 0,
            "fqdn": "tac-123.epc.mnc003.mcc460.3gppnetwork.org",
            "heartBeatTimer": 3600,
            "ipv4Addresses": [
                "10.10.10.10"
            ],
            "ipv6Addresses": [
                "2001:db8:0:1:1:1:1:1"
            ],
            "load": 0,
            "locality": "china",
            "nfInstanceId": "ff01-1",
            "nfServicePersistence": false,
            "nfServices": [
                {
                    "apiPrefix": "web",
                    "capacity": 0,
                    "chfServiceInfo": {
                        "primaryChfServiceInstance": "chfserviceinstance_1"
                    },
                    "fqdn": "tac-123.epc.mnc003.mcc460.3gppnetwork.org",
                    "ipEndPoints": [
                        {
                            "ipv4Address": "10.10.10.11",
                            "transport": "TCP",
                            "port": 5031
                        }
                    ],
                    "load": 0,
                    "nfServiceStatus": "REGISTERED",
                    "priority": 0,
                    "recoveryTime": "2019-03-01T20:20:20Z",
                    "scheme": "http",
                    "serviceInstanceId": "service_instance_0",
                    "serviceName": "nsmf-pdusession",
                    "supportedFeatures": "e345",
                    "versions": [
                        {
                            "apiVersionInUri": "v1",
                            "apiFullVersion": "1.0.0.0"
                        }
                    ]
                }
            ],
            "nfStatus": "REGISTERED",
            "nfType": "SMF",
            "nsiList": [
                "nsilist1",
                "nsilist2"
            ],
            "plmnList": [
                {
                    "mcc": "460",
                    "mnc": "03"
                }
            ],
            "priority": 0,
            "recoveryTime": "2019-03-01T20:20:20Z",
            "sNssais": [
                {
                    "sst": 1,
                    "sd": "010101"
                }
            ],
            "smfInfo": {
                "sNssaiSmfInfoList": [
                    {
                        "sNssai": {
                            "sst": 1,
                            "sd": "010101"
                        },
                        "dnnSmfInfoList": [
                            {
                                "dnn": "huawei.com"
                            }
                        ]
                    }
                ],
                "pgwFqdn": "tac-123.epc.mnc003.mcc460.3gppnetwork.org",
                "accessType": [
                    "3GPP_ACCESS",
                    "NON_3GPP_ACCESS"
                ]
            }
        }
    ]
}  
(结果个数 = 1)
```