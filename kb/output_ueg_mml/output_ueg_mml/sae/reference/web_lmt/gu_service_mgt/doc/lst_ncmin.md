# 以格式2查询CAMEL IN数据(LST NCMIN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户CAMEL IN数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                                                                                                                          |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。                                                                                                          |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。                                                                                                        |
| TYPE   | 查询类型   | 此参数用于设置查询CAMEL IN数据的类型。 取值范围： ALL：查询用户所有CAMEL IN数据。INCS-1：查询CAMEL IN数据中CS-1部分的内容。SMSIN：查询CAMEL IN数据中短消息智能业务部分相关的内容。SSHADNCS1：查询IN数据中ALS辅号码CS-1部分的内容。 说明：可选参数。 |

## 使用实例

查询用户CAMEL IN数据，以指定的数据格式返回。命令如下：

```
LST NCMIN: IMSI="461380000000000";
```

```
%%LST NCMIN: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                IN SERVICES
                     
    IMSI...INTERNATIONAL MOBILE SUBSCRIBER IDENTITY....461380000000000
                     
    CS-1 AND IN CAT:
    INSP...INTELLIGENT NETWORK SERVICE PROFILE..FULL
    SSET...SERVICE SET INDEX....................N

    MOBILITY MANAGEMENT:
    DP.....DETECTION POINT......................N
    SCP....SERVICE CONTROL POINT ADDRESS........N
    SKEY...SERVICE KEY..........................0
    TRT....TRANSACTION TYPE.....................N
    ACT....ACTIVATION STATUS OF SERVICE.........D

    SUPPLEMENTARY SERVICES HANDLING:
    DP.....DETECTION POINT......................N
    SCP....SERVICE CONTROL POINT ADDRESS........N
    SKEY...SERVICE KEY..........................0
    SSCODE.SUPPLEMENTARY SERVICE CODE...........N
    ACT....ACTIVATION STATUS OF SERVICE.........D

    SHORT MESSAGE SERVICE HANDLING:
    DP.....DETECTION POINT......................N
    SCP....SERVICE CONTROL POINT ADDRESS........N
    SKEY...SERVICE KEY..........................0
    TAMM...TRIGGERING ALL MULTIPLE MESSAGES.....N
    ACT....ACTIVATION STATUS OF SERVICE.........D

                      
COMMAND EXECUTED

Total count = 21

There is together 1 report

---    END
```