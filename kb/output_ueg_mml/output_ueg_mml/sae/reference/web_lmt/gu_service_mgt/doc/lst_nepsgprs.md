# 以格式2查询EPS用户GPRS数据(LST NEPSGPRS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询EPS用户的GPRS数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称          | 参数描述                                                   |
|:-------|:--------------|:-------------------------------------------------------|
| IMSI   | IMSI          | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。   |
| ISDN   | MSISDN        | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，为1～15位的十进制数。 说明：可选参数。 |
| CNTXID | PDP/PDN上下文索引值 | 此参数用于设置PDP/PDN上下文索引值。 取值范围：1～50。 说明：可选参数。              |

## 使用实例

查询EPS用户的GPRS数据，以指定的数据格式返回。命令如下：

```
LST NEPSGPRS: IMSI="461380000000000";
```

```
%%LST NEPSGPRS: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

   
PDN CONTEXT PARAMETERS
                                       
IMSI ................................ 461380000000000
CONTEXT NO. 1 OF 2
----------------------
CTXID ............................... 1
PDN TYPE ............................ IPV4
AP NAME ............................. abc.com
QOS CLASS IDENTIFIER ................ 5
PRIORITY LEVEL ...................... 1
PRE-EMPTION CAPABILITY .............. DISABLED
PRE-EMPTION VULNERABILITY ........... DISABLED
VPLMN DYNAMIC ADDRE ALLOWED ......... NO
PGW ALLOCATION TYPE ................. DYNAMIC
CHARGING CHARACTERISTICS ............ NORM
AMBR DOWNLINK ....................... 1
AMBR UPLINK ......................... 1
IPV4 ADDRESS OF THE PDN-GATEWAY ..... N
                                       
CONTEXT NO. 2 OF 2
----------------------
CTXID ............................... 2
PDN TYPE ............................ IPV4
AP NAME ............................. abcd.com
QOS CLASS IDENTIFIER ................ 5
PRIORITY LEVEL ...................... 1
PRE-EMPTION CAPABILITY .............. DISABLED
PRE-EMPTION VULNERABILITY ........... DISABLED
VPLMN DYNAMIC ADDRE ALLOWED ......... NO
PGW ALLOCATION TYPE ................. DYNAMIC
CHARGING CHARACTERISTICS ............ NORM
AMBR DOWNLINK ....................... 1
AMBR UPLINK ......................... 1
IPV4 ADDRESS OF THE PDN-GATEWAY ..... N

Total count = 34

There is together 1 report

---    END
```