# 显示NF信息（DSP REGNFINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询NF实例的Profile信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                       |
|:-------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数  参数含义：该参数用于表示待查询的NF实例标识，可以通过DSP REGNFINSTANCE命令查询ID消息。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。  默认值：无  配置原则：无 |

## 使用实例

查询NF实例的Profile信息：

```
DSP REGNFINFO: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
%%DSP REGNFINFO: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

结果如下
------------------------
NF Profile Information  =  {
	"allowedNfDomains": [
		"domains1",
		"domains2"
	],
	},
	"capacity": 0,
	"fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
	"heartBeatTimer": 60,
	"interPlmnFqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
	"ipv4Addresses": [
		"10.0.0.0"
	],
	"ipv6Addresses": [
		"2001:db8:0:1:1:1:1:1"
	],
	"load": 0,
	"locality": "china",
	"nfInstanceId": "123e4567-e89b-12d3-a456-426655440000",
	"nfServicePersistence": false,
	"nfServices": [
		{
			"allowedNfDomains": [
				"domains1",
				"domains2"
			],
			"fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
			"interPlmnFqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
			"ipEndPoints": [
				{
					"ipv4Address": "10.0.0.1",
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
			"serviceName": "namf-comm",
			"supportedFeatures": "e345",
			"versions": [
				{
					"apiVersionInUri": "v1",
					"apiFullVersion": "1.0.0.0"
				}
			]
		}
	],

}
(结果个数 = 1)
```

## 输出结果说明

| 输出项名称        | 输出项解释                    |
|:-------------|:-------------------------|
| NF PROFILE信息 | 该参数用于表示特定NF实例的Profile信息。 |