# 设置APN RADIUS计费控制参数（SET APNRDSACCTCTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于配置基于APN的RADIUS客户端计费信令控制属性，用来控制RADIUS客户端计费信令处理流程。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 当前版本不支持此命令的BUFFERTIMEVALUE、CACHEACCTSTOPSW、CFCATETRIGGER、CRBNCHANGE参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   |   TIMETHRESHOLD |   VOLUMETHRESHOLD | ACCTALLBEAR   | SRVTRIGGER   |   BUFFERTIMEVALUE | SUPPORTACCTRSP   | DEACTIVE   | SUPPORTACCTSTOP   | SUPPORTACCTUPD   | IPRELEASETRIGER   | QOSTRIGGER   | RATTRIGGER   | SGSNTRIGGER   | ULITRIGGER   | UELOCIPTRIGGER   | CACHEACCTSTOPSW   | SUPPORTUPDRSP   |
|:-------|----------------:|------------------:|:--------------|:-------------|------------------:|:-----------------|:-----------|:------------------|:-----------------|:------------------|:-------------|:-------------|:--------------|:-------------|:-----------------|:------------------|:----------------|
| 初始值    |               0 |                 0 | ALL           | DISABLE      |                 0 | DISABLE          | DEACTIVE   | DISABLE           | ENABLE           | DISABLE           | ENABLE       | ENABLE       | ENABLE        | ENABLE       | DISABLE          | DISABLE           | DISABLE         |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------------|:-----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN             | APN名称                                    | 可选必选说明：必选参数 参数含义：基于该APN配置RADIUS计费控制参数。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：配置APN前，需要先使用ADD CPAPN命令配置APN信息。                                                                                                                                                                                                                                                                    |
| TIMETHRESHOLD   | 时间阈值（分）                                  | 可选必选说明：可选参数 参数含义：控制用户使用流量时间到达该配置时间阈值时，进行RADIUS计费信息上报。 数据来源：本端规划 取值范围：整数类型，取值范围为0～1440，单位是分钟。 默认值：无 配置原则： 流量和阈值都没有配置时，不支持实时计费。只配置时间阈值时，支持基于时间的实时计费。配置流量和时间阈值时，支持基于时长加流量的实时计费。该参数修改后只对新激活用户生效。                                                                                                                                                                                           |
| VOLUMETHRESHOLD | 流量阈值（千字节）                                | 可选必选说明：可选参数 参数含义：控制用户使用流量大小到达该配置流量阈值时，进行RADIUS计费信息上报。 数据来源：本端规划 取值范围：整数类型，取值范围为0，20～4294967295，单位是千字节。 默认值：无 配置原则： 流量和阈值都没有配置时，不支持实时计费。只配置流量时，支持基于流量实时计费。配置流量和时间阈值时，支持基于时长加流量的实时计费。该参数修改后只对新激活用户生效。                                                                                                                                                                                    |
| ACCTALLBEAR     | 全部类型承载或PDP上下文均开启radius计费                 | 可选必选说明：可选参数 参数含义：指定开启RADIUS计费的承载或PDP上下文的类型。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT_BEARER：表示仅缺省承载/一次上下文开启radius计费。ALL：表示全部类型承载/PDP上下文均开启radius计费。 默认值：无 配置原则：无                                                                                                                                                                                                                                   |
| SRVTRIGGER      | 业务报文（通过3/4层规则配置）时触发计费请求消息                | 可选必选说明：可选参数 参数含义：指定是在用户上线时触发计费请求消息，还是在用户访问特殊业务报文（通过3/4层规则配置）时触发计费请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：表示在用户上线时，发送计费请求消息。ENABLE：表示在用户发出特定应用报文时，发送计费请求消息。 默认值：无 配置原则： 在SRVTRIGGER配置为ENABLE的情况下，参数ACCTALLBEAR、SUPPORTACCTRSP、DEACTIVE、SUPPORTACCTSTOP、SUPPORTACCTUPD、IPRELEASETRIGER、QoSTRIGGER、RATTRIGGER、SGSNTEIGGER、ULITRIGGER的配置失效。在SRVTRIGGER配置为ENABLE的情况下，仅支持默认承载触发。                  |
| BUFFERTIMEVALUE | 业务报文延时时间（秒）                              | 可选必选说明：条件可选参数 前提条件：该参数在“SRVTRIGGER”配置为“ENABLE”时为可选参数。 参数含义：指定业务触发RADIUS消息发送时的业务报文延时时间。 数据来源：本端规划 取值范围：整数类型，取值范围为0～6，单位是秒。 默认值：无 配置原则：该配置与RULE下的RDSBUFFERTIME同时用来控制业务触发radius消息发送时的业务报文延时时间。 其中RULE下的RDSBUFFERTIME为收到报文后的报文缓存时间，APNRDSACCTCTRL下的BUFFERTIMEVALUE为发出Radius Accounting Request Start消息后的报文缓存时间。 在两条配置同时配置的场景下，建议配置APNRDSACCTCTRL下BUFFERTIMEVALUE的值小于RULE下的RDSBUFFERTIME的值。 |
| SUPPORTACCTRSP  | 等待计费开始响应消息后才回应激活成功应答消息                   | 可选必选说明：可选参数 参数含义：指定是否等待计费开始响应消息后才回应激活成功应答消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：表示在激活PDP上下文的过程中，不需要等待计费开始响应消息，直接回应激活成功应答，如果等待响应超时，则根据Deactive判断是否去活上下文。ENABLE：表示在PDP上下文激活的过程中，需要等待计费开始响应消息才能回应激活成功应答消息，如果等待超时则PDP上下文激活失败。 默认值：无 配置原则：无                                                                                                                                                       |
| DEACTIVE        | Acct请求超时是否去活用户                           | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTRSP”配置为“DISABLE”时为可选参数。 参数含义：指定未收到计费请求响应消息是否去活用户。UNC发送Accounting Start消息以后，如果在指定的时间内没有收到Accounting Start Response消息，使用此开关控制是否去活用户上下文。 数据来源：本端规划 取值范围：枚举类型。 DEACTIVE：去活用户上下文。CONTINUE：不去活用户上下文。 默认值：无 配置原则：无                                                                                                                                         |
| SUPPORTACCTSTOP | 未收到Accounting Response （START）是否发送计费停止消息 | 可选必选说明：条件可选参数 前提条件：该参数在“DEACTIVE”配置为“CONTINUE”时为可选参数。 参数含义：当DEACTIVE参数为CONTINUE且未收到Accounting-Request START的响应时，使用此开关控制是否发送计费停止消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不发送消息。ENABLE：发送消息。 默认值：无 配置原则：无                                                                                                                                                                                        |
| SUPPORTACCTUPD  | MME或SGSN/SGW发起PDP上下文更新时，是否支持发送计费更新       | 可选必选说明：可选参数 参数含义：指定MME或SGSN/SGW发起PDP上下文更新时是否支持发送计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不发送消息。ENABLE：发送消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                                                             |
| IPRELEASETRIGER | IPv4 Address释放触发计费更新消息                   | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：指定IPv4v6双栈用户IPv4地址提前释放时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                   |
| QOSTRIGGER      | QoS变化触发计费更新消息                            | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制QoS改变时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                                  |
| RATTRIGGER      | RAT变化触发计费更新消息                            | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制RAT改变时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                                  |
| SGSNTRIGGER     | SGSN/SGW变化触发计费更新消息                       | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制SGSN/SGW/AMF/I-SMF改变时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                   |
| ULITRIGGER      | ULI变化触发计费更新消息                            | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制ULI改变时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数修改后，再次触发更新请求消息后生效。                                                                                                                                                                                                                  |
| UELOCIPTRIGGER  | WLAN地址变化触发计费更新消息                         | 可选必选说明：可选参数 参数含义：控制WLAN地址改变时是否触发计费更新请求消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                 |
| CACHEACCTSTOPSW | 缓存Account Stop消息开关                       | 可选必选说明：可选参数 参数含义：控制当RADIUS服务器没有响应时，UNC是否将发往RADIUS的Accounting Stop Request消息缓存到硬盘上。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不缓存。ENABLE：缓存。 默认值：无 配置原则：无                                                                                                                                                                                                                                            |
| SUPPORTUPDRSP   | 等待计费更新响应消息                               | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制是否等待计费更新响应消息。如果设置不等待(DISABLE)，UNC将忽略计费更新响应消息；如果设置等待(ENABLE)，UNC在超时未收到计费更新响应消息时会去活用户。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：表示UNC将忽略计费更新响应消息。ENABLE：表示UNC在超时未收到计费更新响应消息时会去活用户。 默认值：无 配置原则：无                                                                                                                                     |
| CFCATETRIGGER   | URL过滤规则变化触发计费更新消息                        | 可选必选说明：可选参数 参数含义：控制URL过滤规则变化是否触发计费更新消息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                   |
| CRBNCHANGE      | CRBN变化                                   | 可选必选说明：条件可选参数 前提条件：该参数在“SUPPORTACCTUPD”配置为“ENABLE”时为可选参数。 参数含义：控制CRBN规则变化是否触发计费更新消息，包括CRBN增加、删除和重新安装。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不触发消息。ENABLE：触发消息。 默认值：无 配置原则：该参数配置为触发计费更新消息，需要在ADD/MOD RDSACCTATTTEMP命令的RULEBASENAME参数配置为MULTI_CRBN时，才会生效。                                                                                                                                         |

#### 使用实例

新增名为“apn1”的APN的RADIUS客户端计费信令控制属性，访问业务报文（通过3/4层规则配置）时不触发计费更新消息，不等待计费开始响应消息后才回应激活成功应答消息，MME或SGSN/SGW发起PDP上下文更新时支持发送计费更新：

```
SET APNRDSACCTCTRL:APN="apn1",SRVTRIGGER=DISABLE,SUPPORTACCTRSP=DISABLE,SUPPORTACCTUPD=ENABLE;
```