# 以格式2查询用户数据(LST NSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                   |
|:-------|:-------|:-------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。   |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。 |

## 使用实例

查询用户数据，以指定数据格式返回。命令如下：

```
LST NSUB: IMSI="461380000000000";
```

```
%%LST NSUB: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                SUBSCRIBER INFORMATION:
                                                
        INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461380000000000
        MOBILE STATION ISDN NUMBER ................. 461380000000000
        ATTACHED IMSI ..............................
        MOBILE STATION CATEGORY .................... OR
        ROUTING CATEGORY ........................... N
        ADDITIONAL ROUTING CATEGORY ................ N
        SERVICE AREA OF MSISDN ..................... ALL
        ACTIVATION STATUS .......................... A
        VLR-ADDRESS ................................ 
        SIGNALLING POINT CODE ...................... 00000000
        MSC-ADDRESS ................................ 
        PRIMARY BASIC SERVICE CODE ................. B16
        PRIMARY BASIC SERVICE CODE INDEX ........... 000
        ROAMING PROFILE INDEX ...................... N
        FRAUD PROFILE .............................. N
        CALLING LINE IDENTIFICATION ENHANCEMENT .... N
        COMMON MSISDN NUMBER ....................... N
        OVERRIDE COMMON CLI PARAMETERS ............. N
        CMSISDN IS HUNTING GROUP NUMBER ............ N
        DENY DIRECT CALLS .......................... N
        DENY USSD WITH MEMBER NUMBER ............... N
        DENY DIRECT SMS ............................ N
                                                
        ZONE CODES:
                                                
                                                
        MSC AREA RESTRICTED ........................ N
        SGSN AREA RESTRICTED ....................... N
                                                
        HLRU IDENTITY .............................. 0
                                                
        HOME COUNTRY CODE .......................... N
        NETWORK DESTINATION CODE ................... N
                                                
        INTERNATIONAL MOBILE EQUIPMENT IDENTITY .... 
        LATEST LOCATION UPDATE   0000-00-00  00:00:00,00

Total count = 37

There is together 1 report

---    END
```