# 以格式2查询GPRS数据(LST NGPRS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户的GPRS数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                   |
|:-------|:-------|:-------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。   |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，为1～15位的十进制数。 说明：可选参数。 |

## 使用实例

查询用户的GPRS数据，以指定的数据格式返回。命令如下：

```
LST NGPRS: IMSI="461380000000000";
```

```
%%LST NGPRS: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

GPRS DATA PARAMETERS
 
IMSI ........................ 461380000000000
SGSN ADDRESS ................ 
MT-SMS VIA SGSN ............. N
CELL UPDATE INFORMATION ..... N
MT-SMS VIA GPRS SUPPRESSED .. N
NETWORK ACCESS .............. BOTH
CHARGING CHARACTERISTIC ..... N
GPRS ROAMING PROFILE ........ N
GPRS SERVICE AREA ........... N
                                          
COMMAND EXECUTED

Total count = 11

There is together 1 report

---    END
```