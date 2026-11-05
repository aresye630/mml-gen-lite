# 以格式2查询CAMEL CA数据(LST NCMCA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户CAMEL CA数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                                                                                             |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。                                                                             |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。                                                                           |
| TYPE   | 查询类型   | 此参数用于设置查询CAMEL CA数据的类型。 取值范围： ALL：查询用户所有CAMEL CA数据。CALLRELATED：查询CAMEL CA数据中呼叫相关的内容。CALLUNRELATED：查询CAMEL CA数据中呼叫无关的内容。 说明：可选参数。 |

## 使用实例

查询用户CAMEL CA数据，以指定数据格式返回。命令如下：

```
LST NCMCA: IMSI="461380000000000";
```

```
%%LST NCMCA: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

               IN SERVICES
   
   IMSI...INTERNATIONAL MOBILE SUBSCRIBER IDENTITY....461380000000000
   
CAMEL:
  
   ORIGINATING CAMEL SUBSCRIPTION INFORMATION: N

  
   TERMINATING CAMEL SUBSCRIPTION INFORMATION: N

   VISITED MSC TERMINATING CAMEL SUBSCRIPTION INFORMATION: N

   DIALLED SERVICES CAMEL SUBSCRIPTION INFORMATION: N

   MOBILE ORIGINATED SHORT MESSAGE SERVICE CAMEL SUBSCRIPTION INFORMATION: N

   MOBILITY MANAGEMENT EVENT NOTIFICATION CAMEL SUBSCRIPTION INFORMATION: N

   GPRS CAMEL SUBSCRIPTION INFORMATION: N

   SUPPLEMENTARY SERVICE NOTIFICATION CAMEL SUBSCRIPTION INFORMATION: N

   MOBILE TERMINATED SHORT MESSAGE SERVICE CAMEL SUBSCRIPTION INFORMATION: N

   MOBILITY MANAGEMENT FOR GPRS EVENT NOTIFICATION CAMEL SUBSCRIPTION
   INFORMATION: N

   DETECTION POINT UNRELATED CAMEL DATA:
   USSD...USSD PROFILE IDENTIFIER..............0
   TIF....TRANSLATION INFORMATION FLAG.........N

   NOTIFICATION OF SUBSCRIBER DATA CHANGE:
   SCP....SERVICE CONTROL POINT ADDRESS........N
   NOTIF..NOTIFICATION FLAG....................N

Total count = 19

There is together 1 report

---    END
```