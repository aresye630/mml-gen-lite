# 修改QoS特征（MOD QOSCHARS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用来修改QoS特征，其中包括资源类型、5QI优先级、包时延预算、包错误率、平均窗口、最大数据突发。

业务触发专载流程，如果PCF下发了这些参数，以PCF下发的为准，否则读取该配置中的Qos参数。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称        | 参数说明                                                                                                                                                                                                                       |
|:----------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FQI             | 5QI或QCI     | 可选必选说明：必选参数  参数含义：该参数用于配置5QI或QCI，不同的5QI或QCI的业务流需使用不同的承载。  数据来源：全网规划  取值范围：整数类型，取值范围是1~255。  默认值：无  配置原则：无                                                                                                                  |
| RESOURCETYPE    | QoS资源类型     | 可选必选说明：可选参数  参数含义：该参数用于表示QoS流是“NON_GBR”、 “Critical_GBR”还是“NON_CRITICAL_GBR”。  数据来源：全网规划 取值范围： NON_GBR（非GBR QoS流）NON_CRITICAL_GBR（非时延关键GBR QoS流）CRITICAL_GBR（延迟关键GBR QoS流）  默认值：无  配置原则：无                                   |
| PRIORITYLEVEL   | 5QI优先级      | 可选必选说明：可选参数  参数含义：该参数用于表示5QI或QCI优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~127。  默认值：无  配置原则：  取值越小，优先级越高。                                                                                                                          |
| PACKETDELBUDGET | 包时延预算(毫秒)   | 可选必选说明：可选参数  参数含义：该参数用于指示数据包延迟预算。  数据来源：全网规划  取值范围：整数类型，取值范围是1~1000，单位是毫秒。  默认值：无  配置原则：  请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。                                                         |
| PACKETERRRATE   | 包错误率        | 可选必选说明：可选参数  参数含义：该参数用于表示数据包错误率。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~32。  默认值：无  配置原则：  请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。                                                               |
| AVERWINDOW      | 平均窗口(毫秒)    | 可选必选说明：该参数在"RESOURCETYPE"配置为"NON_CRITICAL_GBR"、"CRITICAL_GBR"时为条件必选参数。  参数含义：该参数用于指示平均窗口。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4095，单位是毫秒。  默认值：无  配置原则：  请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。 |
| MAXDATABURSTVOL | 最大数据突发量(字节) | 可选必选说明：该参数在"RESOURCETYPE"配置为"CRITICAL_GBR"时为条件必选参数。  参数含义：该参数用于指示最大数据突发量。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4095，单位是字节。  默认值：无  配置原则：  请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。                 |

## 使用实例

修改一个5QI为“12”的QOS特征，资源类型为GBR，5QI优先级为10，包时延预算为1，包错误率为“4E-6”，平均窗口为1。

```
MOD QOSCHARS: FQI=12, RESOURCETYPE=NON_CRITICAL_GBR, PRIORITYLEVEL=10, PACKETDELBUDGET=1, PACKETERRRATE="4E-6", AVERWINDOW=1;
```