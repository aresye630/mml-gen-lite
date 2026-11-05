# 显示NRF管理的链路信息（DSP NRFLINKINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令可以查询NRF管理的链路信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                              |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PEERID     | 对端标识   | 可选必选说明：可选参数  参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的对端标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                                                                                             |
| PEERIDTYPE | 对端标识类型 | 可选必选说明：可选参数  参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的对端标识类型。  数据来源：本端规划 取值范围： NRFLAYER（NRF分层链路）CALLBACKURL（状态通知回调链路）ASFWD（主备转发链路）NRFREG（NRF向北向NRF注册的链路）NFDETECT（NRF向NF的主动探测链路）OTHER（其他动态链路）  默认值：无  配置原则：无 |
| LINKSTATUS | 链路状态   | 可选必选说明：可选参数  参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的链路状态。  数据来源：本端规划 取值范围： INVALID（未知状态 ）FAULT（故障状态 ）NORMAL（正常状态）OVERLOAD（过载状态）  默认值：无  配置原则：无                                                            |

## 使用实例

查询NRF管理的链路信息：

```
%%DSP NRFLINKINFO: PEERIDTYPE=CALLBACKURL;%%
RETCODE = 0  操作成功

结果如下
------------------------
Link information  =  {
	"PeerId": "10.70.200.1:5164",
	"PeerIdType": "CALLBACKURL",
	"LinkStatus": "NORMAL",
	"RetryAfterSeconds": 0,
	"AddrMsgStatus": "NotRecv",
	"LinkUpdateTime": "2020-03-16T21:17:06+08:00",
	"RecordCreateTime": "2020-03-16T21:17:06+08:00",
	"OverLoadBeginTime": "1970-01-01T08:00:00+08:00",
	"LogicLink": "AAEBRhNGyAEsFADFnRyBAAA=",
	"SbiInfo": {
		"NotifyType": "Add",
		"InfoType": "Callback",
		"PeerId": "10.70.200.1:5164",
		"NFType": "AMF",
		"Scheme": "http",
		"Fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
		"Ipv4Addresses": [
			"10.70.200.1:5164"
		],
		"Ipv6Addresses": null
	}
}
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                      |
|:--------|:---------------------------|
| 链路信息    | 该参数用于表示NRF链路管理表中维护的当前链路信息。 |