# 设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN**

该命令用来配置在SAE架构下，Rel-8 QoS参数和Pre Rel-8 (R99/R98) QoS参数的映射规则。关于本命令所配置参数的具体含义参见协议3GPP TS 23.107。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 用户通过GnGp SGSN接入UNC，由于GnGp SGSN和UNC之间交互的是GTPv0和GTPv1信令，故UNC需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。Rel-8 QoS参数和Pre Rel-8（R99/R98）QoS参数的默认映射规则如下：
- QCI=1映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=CONVERSATIONAL，SRCSTATDESC=SPEECH，SDUERRRATIO=1E\_2，RESIDUALBER=1E\_5，TRANSDELAY=100；
- QCI=2映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=CONVERSATIONAL，SRCSTATDESC=UNKNOWN，SDUERRRATIO=1E\_3，RESIDUALBER=1E\_5，TRANSDELAY=150；
- QCI=3映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=CONVERSATIONAL，SRCSTATDESC=UNKNOWN，SDUERRRATIO=1E\_3，RESIDUALBER=1E\_5，TRANSDELAY=80；
- QCI=4映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=STREAMING，SRCSTATDESC=UNKNOWN，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5，TRANSDELAY=300；
- QCI=5映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=INTERACTIVE，THP=HIGH，SIGNALIND=OPTIMIZE，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5；
- QCI=6映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=INTERACTIVE，THP=HIGH，SIGNALIND=DONT\_OPTIMIZE，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5；
- QCI=7映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=INTERACTIVE，THP=NORMAL，SIGNALIND=DONT\_OPTIMIZE，SDUERRRATIO=1E\_3，RESIDUALBER=1E\_5；
- QCI=8映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=INTERACTIVE，THP=LOW，SIGNALIND=DONT\_OPTIMIZE，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5；
- QCI=9映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=BACKGROUND，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5；
- QCI值为128~254（Non-GBR）映射到Pre Rel-8（R99/R98）的Qos参数TRAFFICCLASS=BACKGROUND，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5；
- QCI值为128~254（GBR）映射到Pre Rel-8（R99/R98）的Qos参数：TRAFFICCLASS=STREAMING，SRCSTATDESC=UNKNOWN，SDUERRRATIO=1E\_4，RESIDUALBER=1E\_5，TRANSDELAY=300；
- 当QCI值为1~4时，TRAFFICCLASS不允许为INTERACTIVE或BACKGROUND；
- 当QCI值为5~9时，TRAFFICCLASS不允许为CONVERSATIONAL或STREAMING；
- 参考STDQOSID以及EXTENDQCIMAP中的配置，资源类型为GBR的QCI，TRAFFICCLASS不允许为INTERACTIVE或BACKGROUND；资源类型为Non-GBR的QCI，TRAFFICCLASS不允许为CONVERSATIONAL或STREAMING；
- 当QCI值为2时，TRANSDELAY的取值必须大于或者等于150ms；当QCI值为3时，TRANSDELAY的取值必须小于150ms；
- 当前命令已支持扩展QCI。
- STDQOSID命令的默认配置会对本配置的非关键参数DELIVERYORDER参数进行赋值，赋值为2。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

|   QCI | TRAFFICCLASS   | THP    | SIGNALIND     | SRCSTATDESC   |   MAXSDU | DELIVERRORSDU   |   TRANSDELAY | SDUERRRATIO   | RESIDUALBER   |
|------:|:---------------|:-------|:--------------|:--------------|---------:|:----------------|-------------:|:--------------|:--------------|
|     1 | CONVERSATIONAL | nan    | DONT_OPTIMIZE | SPEECH        |     1500 | NO_DETECT       |          100 | EN_1E_2       | EN_1E_5       |
|     2 | CONVERSATIONAL | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |          150 | EN_1E_3       | EN_1E_5       |
|     3 | CONVERSATIONAL | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           80 | EN_1E_3       | EN_1E_5       |
|     4 | STREAMING      | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |          300 | EN_1E_4       | EN_1E_5       |
|     5 | INTERACTIVE    | HIGH   | OPTIMIZE      | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|     6 | INTERACTIVE    | HIGH   | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|     7 | INTERACTIVE    | NORMAL | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_3       | EN_1E_5       |
|     8 | INTERACTIVE    | LOW    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|     9 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   128 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   129 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   130 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   131 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   132 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   133 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   134 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   135 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   136 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   137 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |
|   138 | BACKGROUND     | nan    | DONT_OPTIMIZE | UNKNOWN       |     1500 | NO_DETECT       |           10 | EN_1E_4       | EN_1E_5       |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                          |
|:--------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QCI           | QCI值          | 可选必选说明：必选参数  参数含义：该参数表示Qos流量级别值。  数据来源：全网规划  取值范围：整数类型，取值范围是1~255。  默认值：无。  配置原则：无                                                                                                                                                                                                                            |
| TRAFFICCLASS  | 业务类型          | 可选必选说明：必选参数  参数含义：该参数表示业务类型。  数据来源：全网规划 取值范围： “CONVERSATIONAL（会话类）”：表示用户签约信息中traffic class的级别为会话层面，优先级高。“STREAMING（流媒体类）”：表示用户签约信息中traffic class的级别为流媒体层面。“INTERACTIVE（交互类）”：表示用户签约信息中traffic class的级别为交互层面。“BACKGROUND（后台类）”：表示用户签约信息中traffic class的级别为后台层面。  默认值：无。  配置原则：无                                 |
| THP           | 通信处理优先级       | 可选必选说明：可选参数  参数含义：该参数表示通信处理优先级。  数据来源：全网规划 取值范围： NA（N/A）“HIGH（高）”：表示优先级高。“NORMAL（中）”：表示优先级中。“LOW（低）”：表示优先级低。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：  通信处理优先级只对交互类业务起作用，对会话业务，流媒体业务和后台业务不起作用，与R99版本中的值相同。                                                                      |
| SIGNALIND     | 信令传输优化        | 可选必选说明：可选参数  参数含义：该参数表示是否对信令传输进行优化。  数据来源：全网规划 取值范围： “DONT_OPTIMIZE（不优化）”：不对信令传输进行优化。“OPTIMIZE（优化）”：对信令传输进行优化。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                                                                                                                        |
| SRCSTATDESC   | 源统计描述         | 可选必选说明：可选参数  参数含义：该参数表示源统计描述。  数据来源：全网规划 取值范围： “UNKNOWN（未知）”：未知“SPEECH（语音）”：语音  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                                                                                                                                                        |
| MAXSDU        | 最大SDU长度(byte) | 可选必选说明：可选参数  参数含义：该参数表示最大SDU尺寸。  数据来源：全网规划  取值范围：整数类型，取值范围是10~1520，单位是字节。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                                                                                                                                                             |
| DELIVERRORSDU | 发送错误的SDU      | 可选必选说明：可选参数  参数含义：该参数表示是否发送错误的SDU（信令数据单元）。  数据来源：全网规划 取值范围： “NO_DETECT（不检测）”：不检测错误。“ERR_DELIV（发送错误）”：发送错误的SDU。“ERR_NOT_DELIV（不发送错误）”：不发送错误的SDU。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                                                                                       |
| TRANSDELAY    | 传输时延(毫秒)      | 可选必选说明：可选参数  参数含义：该参数表示传输时延。  数据来源：全网规划  取值范围：整数类型，取值范围是10~4000。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                                                                                                                                                                      |
| SDUERRRATIO   | SDU误码率        | 可选必选说明：可选参数  参数含义：该参数表示SDU误码率（QoS-SDU error ratio）。  数据来源：全网规划 取值范围： “EN_1E_2（1E-2）”：1E-2“EN_7E_3（7E-3）”：7E-3“EN_1E_3（1E-3）”：1E-3“EN_1E_4（1E-4）”：1E-4“EN_1E_5（1E-5）”：1E-5“EN_1E_6（1E-6）”：1E-6“EN_1E_1（1E-1）”：1E-1  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无                     |
| RESIDUALBER   | 残留比特误码率       | 可选必选说明：可选参数  参数含义：该参数表示残留比特误码率。  数据来源：全网规划 取值范围： “EN_5E_2（5E-2）”：5E-2“EN_1E_2（1E-2）”：1E-2“EN_5E_3（5E-3）”：5E-3“EN_4E_3（4E-3）”：4E-3“EN_1E_3（1E-3）”：1E-3“EN_1E_4（1E-4）”：1E-4“EN_1E_5（1E-5）”：1E-5“EN_1E_6（1E-6）”：1E-6“EN_6E_8（6E-8）”：6E-8  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EPSQCI2PRER8查询当前参数配置值。  配置原则：无 |

## 使用实例

配置Rel-8 QoS参数和Pre Rel-8 (R99/R98) QoS参数的映射规则，“QoS流量级别”值为“1”时，“业务类型”为“CONVERSATIONAL”，“通信处理优先级”为“HIGH”：

```
SET EPSQCI2PRER8: QCI=1, TRAFFICCLASS=CONVERSATIONAL, THP=HIGH;
```