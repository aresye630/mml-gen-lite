# 查询全局生效离线计费模板配置（DSP GLBOFCTEMPCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看全局离线计费模板生效的配置信息。

如果全局离线计费配置未绑定离线计费模板，则显示全局缺省配置。显示信息中如果模板名字为NULL，则表示是全局缺省配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查看全局离线计费模板的具体配置信息：

```
DSP GLBOFCTEMPCFG:;
```

```
RETCODE = 0  操作成功

全局生效离线计费配置
--------------------
                           GGSN离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               GCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         GContainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                            PGW离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               PCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         Pcontainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                            SGW离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               SCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         Scontainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                       服务PLMN控制速率改变  =  使能
          CDR MO Exception Data Counter更新  =  使能
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
                          PCRF发起的QoS更新  =  不使能
                                 用户面更新  =  使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
                                 用户面更新  =  使能
                       服务PLMN控制速率改变  =  使能
                          PCRF发起的QoS更新  =  不使能
                                 用户面更新  =  使能
                          PCRF发起的QoS更新  =  不使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
        MO Exception Data Counter更新优先级  =  255
        MO Exception Data Counter更新优先级  =  255
        MO Exception Data Counter更新优先级  =  255
                                 eNodeB更新  =  使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
          CDR MO Exception Data Counter更新  =  使能
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
                                 eNodeB更新  =  使能
          CDR MO Exception Data Counter更新  =  使能
                                 eNodeB更新  =  使能
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
                       服务PLMN控制速率改变  =  使能
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                           | 输出项解释                                                                                           |
|:--------------------------------|:------------------------------------------------------------------------------------------------|
| GGSN离线计费模板                      | GPRS/UMTS接入时离线计费模板。                                                                             |
| 时长阈值                            | 产生话单的时间阈值。                                                                                      |
| 流量阈值                            | 产生话单的流量阈值。                                                                                      |
| 最小流量阈值                          | 产生话单的最小流量阈值。                                                                                    |
| 在线计费转离线计费后的时长阈值（分钟）             | 用于指定在线计费用户转离线后产生CDR话单的时间阈值。当用户在线达到配置的时间阈值，系统为用户产生一张中间话单，然后重新计时；0表示无效值，设置为0时，表示在线转离线后时间阈值不生效。    |
| 在线计费转离线计费后的流量阈值（千字节）            | 用于指定在线计费用户转离线后产生CDR话单的流量阈值。用户流量达到此流量阈值时系统生成中间话单；0表示无效值，设置为0时，表示在线转离线后流量阈值不生效。                   |
| 计费条件改变阈值                        | 产生话单的计费条件最大改变次数。                                                                                |
| Serving Node改变次数阈值              | 产生话单的SGSN/SGW-C的IP地址最大改变次数。                                                                     |
| 最大携带的业务容器数量                     | 话单中最多可以携带的业务容器数量。                                                                               |
| GCDR RAT更新                      | RAT更新是否触发产生话单。                                                                                  |
| RAT更新优先级                        | RAT更新触发产生话单开关的优先级。                                                                              |
| Serving Node更新                  | SGSN/SGW-C更新是否触发产生话单。                                                                           |
| Serving Node更新优先级               | SGSN/SGW-C更新触发产生话单开关的优先级。                                                                       |
| 计费条件改变                          | 计费条件改变次数达到配置的最大次数是否触发产生话单。                                                                      |
| 计费条件改变优先级                       | 计费条件改变次数达到配置的最大次数触发产生话单开关的优先级。                                                                  |
| MS时区更新                          | MS时区更新是否触发产生话单。                                                                                 |
| MS时区优先级                         | MS时区更新触发产生话单开关的优先级。                                                                             |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否触发产生话单。                                                                    |
| Serving Node PLMN标识优先级          | SGSN/SGW-C PLMN标识改变触发产生话单开关的优先级。                                                                |
| CDR MO Exception Data Counter更新 | 用于指示收到MO Exception Data Counter时是否产生话单。                                                         |
| MO Exception Data Counter更新优先级  | MO Exception Data Counter更新优先级。                                                                 |
| GContainer RAT更新                | RAT更新是否触发产生容器。                                                                                  |
| QoS更新                           | QoS更新是否触发产生容器。                                                                                  |
| Serving Node更新                  | SGSN/SGW-C地址改变是否触发产生容器。                                                                         |
| CGI/SAI更新                       | CGI/SAI改变是否触发产生容器。                                                                              |
| ECGI更新                          | ECGI改变是否触发产生容器。                                                                                 |
| TAI更新                           | TAI改变是否触发产生容器。                                                                                  |
| ULI更新                           | ULI改变是否触发产生容器。                                                                                  |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否产生容器。                                                                      |
| RAI更新                           | RAI改变是否触发产生容器。                                                                                  |
| 费率切换                            | 费率切换是否触发产生容器。                                                                                   |
| APN控制速率改变                       | 用于指定APN控制速率改变时是否产生话单容器。                                                                         |
| APN速率控制改变流量容器关闭原因值              | 用于指定APN控制速率改变时填充的流量容器关闭原因值。                                                                     |
| 用户面更新                           | 用于指定用户面改变时是否产生话单容器。                                                                             |
| 服务PLMN控制速率改变                    | 用于指定服务PLMN控制速率改变时是否产生话单容器。                                                                      |
| G-CDR版本                         | G-CDR话单版本。                                                                                      |
| PGW-CDR版本                       | PGW-CDR话单版本。                                                                                    |
| SGW-CDR版本                       | SGW-CDR话单版本。                                                                                    |
| 时长配额机制                          | 离线计费用户支持的time-quota-mechanism计费方式。                                                              |
| QCT时长                           | 离线计费配额空耗时间。                                                                                     |
| BTI时长                           | Base-Time-Interval时长。                                                                           |
| Record Sequence Number字段起始值     | 话单序列号字段的起始值。                                                                                    |
| 话单时间格式                          | 离线计费话单的时间格式。                                                                                    |
| QHT时长                           | 离线计费配额空闲时间。                                                                                     |
| PCRF发起的QoS更新                    | 这是个开关参数，表示部署IP-CAN-Type为3GPP-EPS的Gx接口时，仅根据Gx接口上PCRF指示的APN-AMBR或缺省承载QCI/ARP的更新情况触发生成新的PGW-CDR容器。 |
| eNodeB更新                        | eNodeB更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。                                                 |
| PGW离线计费模板                       | PGW形态离线计费模板。                                                                                    |
| 时长阈值                            | 产生话单的时间阈值。                                                                                      |
| 流量阈值                            | 产生话单的流量阈值。                                                                                      |
| 最小流量阈值                          | 产生话单的最小流量阈值。                                                                                    |
| 在线计费转离线计费后的时长阈值（分钟）             | 用于指定在线计费用户转离线后产生CDR话单的时间阈值。当用户在线达到配置的时间阈值，系统为用户产生一张中间话单，然后重新计时；0表示无效值，设置为0时，表示在线转离线后时间阈值不生效。    |
| 在线计费转离线计费后的流量阈值（千字节）            | 用于指定在线计费用户转离线后产生CDR话单的流量阈值。用户流量达到此流量阈值时系统生成中间话单；0表示无效值，设置为0时，表示在线转离线后流量阈值不生效。                   |
| 计费条件改变阈值                        | 产生话单的计费条件最大改变次数。                                                                                |
| Serving Node改变次数阈值              | 产生话单的SGSN/SGW-C的IP地址最大改变次数。                                                                     |
| 最大携带的业务容器数量                     | 话单中最多可以携带的业务容器数量。                                                                               |
| PCDR RAT更新                      | RAT更新是否触发产生话单。                                                                                  |
| RAT更新优先级                        | RAT更新触发产生话单开关的优先级。                                                                              |
| Serving Node更新                  | SGSN/SGW-C更新是否触发产生话单。                                                                           |
| Serving Node更新优先级               | SGSN/SGW-C更新触发产生话单开关的优先级。                                                                       |
| 计费条件改变                          | 计费条件改变次数达到配置的最大次数是否触发产生话单。                                                                      |
| 计费条件改变优先级                       | 计费条件改变次数达到配置的最大次数触发产生话单开关的优先级。                                                                  |
| MS时区更新                          | MS时区更新是否触发产生话单。                                                                                 |
| MS时区优先级                         | MS时区更新触发产生话单开关的优先级。                                                                             |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否触发产生话单。                                                                    |
| Serving Node PLMN标识优先级          | SGSN/SGW-C PLMN标识改变触发产生话单开关的优先级。                                                                |
| CDR MO Exception Data Counter更新 | 用于指示收到MO Exception Data Counter时是否产生话单。                                                         |
| MO Exception Data Counter更新优先级  | MO Exception Data Counter更新优先级。                                                                 |
| Pcontainer RAT更新                | RAT更新是否触发产生容器。                                                                                  |
| QoS更新                           | QoS更新是否触发产生容器。                                                                                  |
| Serving Node更新                  | SGSN/SGW-C地址改变是否触发产生容器。                                                                         |
| CGI/SAI更新                       | CGI/SAI改变是否触发产生容器。                                                                              |
| ECGI更新                          | ECGI改变是否触发产生容器。                                                                                 |
| TAI更新                           | TAI改变是否触发产生容器。                                                                                  |
| ULI更新                           | ULI改变是否触发产生容器。                                                                                  |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否产生容器。                                                                      |
| RAI更新                           | RAI改变是否触发产生容器。                                                                                  |
| 费率切换                            | 费率切换是否触发产生容器。                                                                                   |
| APN控制速率改变                       | 用于指定APN控制速率改变时是否产生话单容器。                                                                         |
| APN速率控制改变流量容器关闭原因值              | 用于指定APN控制速率改变时填充的流量容器关闭原因值。                                                                     |
| 用户面更新                           | 用于指定用户面改变时是否产生话单容器。                                                                             |
| 服务PLMN控制速率改变                    | 用于指定服务PLMN控制速率改变时是否产生话单容器。                                                                      |
| G-CDR版本                         | G-CDR话单版本。                                                                                      |
| PGW-CDR版本                       | PGW-CDR话单版本。                                                                                    |
| SGW-CDR版本                       | SGW-CDR话单版本。                                                                                    |
| 时长配额机制                          | 离线计费用户支持的time-quota-mechanism计费方式。                                                              |
| QCT时长                           | 离线计费配额空耗时间。                                                                                     |
| BTI时长                           | Base-Time-Interval时长。                                                                           |
| Record Sequence Number字段起始值     | 话单序列号字段的起始值。                                                                                    |
| 话单时间格式                          | 离线计费话单的时间格式。                                                                                    |
| QHT时长                           | 离线计费配额空闲时间。                                                                                     |
| PCRF发起的QoS更新                    | 这是个开关参数，表示部署IP-CAN-Type为3GPP-EPS的Gx接口时，仅根据Gx接口上PCRF指示的APN-AMBR或缺省承载QCI/ARP的更新情况触发生成新的PGW-CDR容器。 |
| eNodeB更新                        | eNodeB更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。                                                 |
| SGW离线计费模板                       | SGW形态离线计费模板。                                                                                    |
| 时长阈值                            | 产生话单的时间阈值。                                                                                      |
| 流量阈值                            | 产生话单的流量阈值。                                                                                      |
| 最小流量阈值                          | 产生话单的最小流量阈值。                                                                                    |
| 在线计费转离线计费后的时长阈值（分钟）             | 用于指定在线计费用户转离线后产生CDR话单的时间阈值。当用户在线达到配置的时间阈值，系统为用户产生一张中间话单，然后重新计时；0表示无效值，设置为0时，表示在线转离线后时间阈值不生效。    |
| 计费条件改变阈值                        | 产生话单的计费条件最大改变次数。                                                                                |
| Serving Node改变次数阈值              | 产生话单的SGSN/SGW-C的IP地址最大改变次数。                                                                     |
| 最大携带的业务容器数量                     | 话单中最多可以携带的业务容器数量。                                                                               |
| SCDR RAT更新                      | RAT更新是否触发产生话单。                                                                                  |
| RAT更新优先级                        | RAT更新触发产生话单开关的优先级。                                                                              |
| Serving Node更新                  | SGSN/SGW-C更新是否触发产生话单。                                                                           |
| Serving Node更新优先级               | SGSN/SGW-C更新触发产生话单开关的优先级。                                                                       |
| 计费条件改变                          | 计费条件改变次数达到配置的最大次数是否触发产生话单。                                                                      |
| 计费条件改变优先级                       | 计费条件改变次数达到配置的最大次数触发产生话单开关的优先级。                                                                  |
| MS时区更新                          | MS时区更新是否触发产生话单。                                                                                 |
| MS时区优先级                         | MS时区更新触发产生话单开关的优先级。                                                                             |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否触发产生话单。                                                                    |
| Serving Node PLMN标识优先级          | SGSN/SGW-C PLMN标识改变触发产生话单开关的优先级。                                                                |
| CDR MO Exception Data Counter更新 | 用于指示收到MO Exception Data Counter时是否产生话单。                                                         |
| MO Exception Data Counter更新优先级  | MO Exception Data Counter更新优先级。                                                                 |
| Scontainer RAT更新                | RAT更新是否触发产生容器。                                                                                  |
| QoS更新                           | QoS更新是否触发产生容器。                                                                                  |
| Serving Node更新                  | SGSN/SGW-C地址改变是否触发产生容器。                                                                         |
| CGI/SAI更新                       | CGI/SAI改变是否触发产生容器。                                                                              |
| ECGI更新                          | ECGI改变是否触发产生容器。                                                                                 |
| TAI更新                           | TAI改变是否触发产生容器。                                                                                  |
| ULI更新                           | ULI改变是否触发产生容器。                                                                                  |
| Serving Node PLMN标识更新           | SGSN/SGW-C PLMN标识改变是否产生容器。                                                                      |
| RAI更新                           | RAI改变是否触发产生容器。                                                                                  |
| 费率切换                            | 费率切换是否触发产生容器。                                                                                   |
| APN控制速率改变                       | 用于指定APN控制速率改变时是否产生话单容器。                                                                         |
| APN速率控制改变流量容器关闭原因值              | 用于指定APN控制速率改变时填充的流量容器关闭原因值。                                                                     |
| 用户面更新                           | 用于指定用户面改变时是否产生话单容器。                                                                             |
| 服务PLMN控制速率改变                    | 用于指定服务PLMN控制速率改变时是否产生话单容器。                                                                      |
| G-CDR版本                         | G-CDR话单版本。                                                                                      |
| PGW-CDR版本                       | PGW-CDR话单版本。                                                                                    |
| SGW-CDR版本                       | SGW-CDR话单版本。                                                                                    |
| 时长配额机制                          | 离线计费用户支持的time-quota-mechanism计费方式。                                                              |
| QCT时长                           | 离线计费配额空耗时间。                                                                                     |
| BTI时长                           | Base-Time-Interval时长。                                                                           |
| Record Sequence Number字段起始值     | 话单序列号字段的起始值。                                                                                    |
| 话单时间格式                          | 离线计费话单的时间格式。                                                                                    |
| QHT时长                           | 离线计费配额空闲时间。                                                                                     |
| PCRF发起的QoS更新                    | 这是个开关参数，表示部署IP-CAN-Type为3GPP-EPS的Gx接口时，仅根据Gx接口上PCRF指示的APN-AMBR或缺省承载QCI/ARP的更新情况触发生成新的PGW-CDR容器。 |
| eNodeB更新                        | eNodeB更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。                                                 |