# 以格式2查询用户EPS数据(LST NEPS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户EPS数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                   |
|:-------|:-------|:-------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。 说明：可选参数。   |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。 |

## 使用实例

查询用户数据，以特定的数据格式返回。命令如下：

```
LST NEPS：IMSI="461380000000000";
```

```
%%LST NEPS: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

LTE DATA PARAMETERS
                  
IMSI ........................ 461380000000000
EPS STATUS .................. GRANTED
MME ADDRESS PRESENT.......... N
APN OI REPLACEMENT MCC ...... 262
APN OI REPLACEMENT MNC ...... 77
DEFAULT PDN CONTEXT ID ...... 1
EPS SERVICE AREA ............ NAT
AMBR DOWNLINK ............... 50000
AMBR UPLINK ................. 10000
RFSP INDEX .................. 1
STNSR ....................... N
LATEST LTE LOCATION UPDATE .. 0000-00-00  00:00:00,00

Total count = 13

There is together 1 report

---    END
```