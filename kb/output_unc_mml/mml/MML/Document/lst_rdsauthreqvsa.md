# 查询RADIUS鉴权请求携带的私有扩展属性（LST RDSAUTHREQVSA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询发送到指定RADIUS服务器组的鉴权请求消息中是否携带3GPP（26/10415）扩展属性。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                                                                    |
|:--------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数  参数含义：该参数用于指定鉴权服务器组名。  数据来源：对端协商  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  配置RADIUS服务器组名前，需要先使用ADD RDSSVRGRP命令配置RADIUS服务器组信息。 |

## 使用实例

查询服务器组名称为rds的3GPP扩展属性在鉴权请求消息中是否支持：

```
%%LST RDSAUTHREQVSA:RDSSVRGRPNAME="rds";%%
RETCODE = 0  操作成功

结果如下
--------
              RADIUS服务器组名称  =  rds
            3GPP私有扩展属性开关  =  禁止
                       3GPP-IMSI  =  允许
                3GPP-Charging-ID  =  允许
                   3GPP-PDP-Type  =  允许
                 3GPP-CG-Address  =  允许
3GPP-GPRS-Negotiated-QoS-Profile  =  允许
          3GPP-SGSN(SGW)-Address  =  允许
               3GPP-GGSN-Address  =  允许
               3GPP-IMSI-MCC-MNC  =  允许
               3GPP-GGSN-MCC-MNC  =  允许
                      3GPP-NSAPI  =  允许
             3GPP-Selection-Mode  =  允许
   3GPP-Charging-Characteristics  =  允许
          3GPP-SGSN(SGW)-MCC-MNC  =  允许
                     3GPP-IMEISV  =  允许
                   3GPP-RAT-Type  =  允许
         3GPP-User-Location-Info  =  允许
                3GPP-MS-TimeZone  =  允许
            3GPP-Negotiated-DSCP  =  允许
          3GPP-SGSN-IPv6-Address  =  允许
          3GPP-GGSN-IPv6-Address  =  允许
            3GPP-CG-IPv6-Address  =  禁止
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                            | 输出项解释                                                   |
|:---------------------------------|:--------------------------------------------------------|
| RADIUS服务器组名称                     | 该参数用于指定鉴权服务器组名。                                         |
| 3GPP私有扩展属性开关                     | 该参数用于配置是否支持鉴权请求消息中携带26/10415这组属性。                       |
| 3GPP-IMSI                        | 该参数用于配置是否支持鉴权请求消息中携带3GPP-IMSI属性。                        |
| 3GPP-Charging-ID                 | 该参数用于配置是否支持鉴权请求消息中携带3GPP-Charging-ID属性。                 |
| 3GPP-PDP-Type                    | 该参数用于配置是否支持鉴权请求消息中携带3GPP-PDP-Type属性。                    |
| 3GPP-CG-Address                  | 该参数用于配置是否支持鉴权请求消息中携带3GPP-CG-Address属性。                  |
| 3GPP-GPRS-Negotiated-QoS-Profile | 该参数用于配置是否支持鉴权请求消息中携带3GPP-GPRS-Negotiated-QoS-Profile属性。 |
| 3GPP-SGSN(SGW)-Address           | 该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN（SGW）-Address属性。           |
| 3GPP-GGSN-Address                | 该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-Address属性。                |
| 3GPP-IMSI-MCC-MNC                | 该参数用于配置是否支持鉴权请求消息中携带3GPP-IMSI-MCC-MNC属性。                |
| 3GPP-GGSN-MCC-MNC                | 该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-MCC-MNC属性。                |
| 3GPP-NSAPI                       | 该参数用于配置是否支持鉴权请求消息中携带3GPP-NSAPI属性。                       |
| 3GPP-Selection-Mode              | 该参数用于配置是否支持鉴权请求消息中携带3GPP-Selection-Mode属性。              |
| 3GPP-Charging-Characteristics    | 该参数用于配置是否支持鉴权请求消息中携带3GPP-Charging-Characteristics属性。    |
| 3GPP-SGSN(SGW)-MCC-MNC           | 该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN（SGW）-MCC-MNC属性。           |
| 3GPP-IMEISV                      | 该参数用于配置是否支持鉴权请求消息中携带3GPP-IMEISV属性。                      |
| 3GPP-RAT-Type                    | 该参数用于配置是否支持鉴权请求消息中携带3GPP-RAT-Type属性。                    |
| 3GPP-User-Location-Info          | 该参数用于配置是否支持鉴权请求消息中携带3GPP-User-Location-Info属性。          |
| 3GPP-MS-TimeZone                 | 该参数用于配置是否支持鉴权请求消息中携带3GPP-MS-TimeZone属性。                 |
| 3GPP-Negotiated-DSCP             | 该参数用于配置是否支持鉴权请求消息中携带3GPP-Negotiated-DSCP属性。             |
| 3GPP-SGSN-IPv6-Address           | 该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN-IPv6-Address属性。           |
| 3GPP-GGSN-IPv6-Address           | 该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-IPv6-Address属性。           |
| 3GPP-CG-IPv6-Address             | 该参数用于配置是否支持鉴权请求消息中携带3GPP-CG-IPv6Address属性。              |