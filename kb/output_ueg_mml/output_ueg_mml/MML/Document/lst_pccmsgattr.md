# 查询PCC消息属性（LST PCCMSGATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询配置在Gx接口上CCR-I、CCR-U、CCR-T和RAA消息中可选AVP的携带方式。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                |
|:--------|:-------|:------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE | 消息类型   | 可选必选说明：可选参数 参数含义：该参数用于设置Gx接口上的消息类型。 数据来源：对端协商 取值范围：枚举类型。 CCRI：消息类型为CCR-I。CCRU：消息类型为CCR-U。CCRT：消息类型为CCR-T。RAA：消息类型为RAA。 默认值：无 配置原则：无 |

#### 使用实例

- 显示CCR-I消息的配置信息：

  ```
  LST PCCMSGATTR:MSGTYPE=CCRI;
  ```

  ```
  RETCODE = 0  操作成功

  PCC消息属性信息
  ---------------
                                              消息类型  =  CCR-I
  Charging-Rule-Base-Name和Charging-Rule-Name子AVP开关  =  不使能
                              3GPP-MS-TimeZone AVP开关  =  使能
                                 3GPP-RAT-Type AVP开关  =  使能
     Subscription-Id-Type和Subscription-Id携带IMSI开关  =  使能
                 3GPP-Charging-Characteristics AVP开关  =  不使能
                             3GPP-GGSN-Address AVP开关  =  不使能
                           3GPP-Selection-Mode AVP开关  =  不使能
                          Dynamic-Address-Flag AVP开关  =  不使能
                Dynamic-Address-Flag-Extension AVP开关  =  不使能
                    PDN-Connection-Charging-ID AVP开关  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 显示Gx接口的全部配置信息：

  ```
  LST PCCMSGATTR:;
  ```

  ```
  RETCODE = 0  操作成功

  PCC消息属性信息
  ---------------
  消息类型  Charging-Rule-Base-Name和Charging-Rule-Name子AVP开关  3GPP-MS-TimeZone AVP开关  3GPP-RAT-Type AVP开关  Subscription-Id-Type和Subscription-Id携带IMSI开关  Subscription-Id-Type和Subscription-Id携带MSISDN开关  Called-Station-ID AVP开关  User-Equipment-Info AVP开关  Framed-IP-Address AVP开关  RAT-Type AVP开关  Experiment-Result-Code AVP开关  Framed-IPv6-Prefix AVP开关  CL切换更新时携带Network-Request-Support AVP开关  User-Location-Info-Time AVP开关  NetLoc-Access-Support AVP开关  Access-Network-Charging-Address AVP开关  Dynamic-Address-Flag-Extension AVP开关  PDN-Connection-Charging-ID AVP开关  3GPP-Selection-Mode AVP开关  3GPP-GGSN-Address AVP开关  Dynamic-Address-Flag AVP开关  3GPP-Charging-Characteristics AVP开关  QoS-Information AVP开关  Default-EPS-Bearer-QoS AVP开关  3GPP-SGSN-MCC-MNC AVP开关 3GPP-SGSN-Address AVP开关 3GPP-User-Location-Info AVP开关  Access-Network-Charging-Identifier-Value AVP开关

  CCR-I     不使能                                                使能                      使能                   使能                                               NULL                                                 NULL                       NULL                         NULL                       NULL              NULL                            NULL                        NULL                                             NULL                             NULL                           NULL                                     不使能                                  不使能                              不使能                       不使能                     不使能                        不使能                                 NULL                     NULL                      NULL                        NULL                       NULL                         NULL
  CCR-U     NULL                                                  使能                      使能                   使能                                               使能                                                 不使能                     不使能                       不使能                     不使能            NULL                            不使能                      不使能                                           不使能                           NULL                           不使能                                   NULL                                    NULL                                NULL                         NULL                       NULL                          NULL                                   不使能                   不使能                      不使能                       不使能                      不使能                        不使能
  CCR-T     NULL                                                  NULL                      NULL                   不使能                                             不使能                                               不使能                     不使能                       不使能                     NULL              NULL                            不使能                      NULL                                             不使能                           NULL                           不使能                                   NULL                                    NULL                                NULL                         NULL                       NULL                          NULL                                   NULL                     NULL                    NULL                         NULL                         NULL                        不使能
  RAA       NULL                                                  NULL                      NULL                   NULL                                               NULL                                                 NULL                       NULL                         NULL                       NULL              不使能                          NULL                        NULL                                             NULL                             不使能                         NULL                                     NULL                                    NULL                                NULL                         NULL                       NULL                          NULL                                   NULL                     NULL                NULL                          NULL                        NULL                       不使能
  (结果个数 = 4)

  ---    END
  ```

#### 输出结果说明

参见SET PCCMSGATTR的参数说明。