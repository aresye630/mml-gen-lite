# 设置缺省GBR承载参数（SET DFTGBRBEARER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于配置SMF是否支持创建default-gbr承载（提供最低带宽保障的any to any GBR专有承载），该承载可由PCF/PCRF发起创建，也可以由SMF发起创建。

#### 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- SESSIONTERMINSW参数修改后立即生效。
- 在每次执行ADD CPAPN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：DFTGBRBEARERSW=DISABLE,LOCQOSQCI=4,LOCQOSARP=15,LOCQOSPREEMPCAP=DISABLE,LOCQOSPREEMPVUL=ENABLE,LOCQOSMBRUL=64,LOCQOSMBRDL=64,LOCQOSGBRUL=64,LOCQOSGBRDL=64,SESSIONTERMINSW=DISABLE,ACCTYPE=RATNON5G。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                              | 参数说明                                                                                                                                                                                                                                                                                            |
|:----------------|:----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN             | APN名称                             | 可选必选说明：必选参数 参数含义：该参数用于指定APN名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。 默认值：无 配置原则：该参数使用ADD CPAPN命令配置生成。                                                                            |
| DFTGBRBEARERSW  | 缺省GBR承载开关                         | 可选必选说明：必选参数 参数含义：该参数用于设置缺省GBR承载开关，是否支持SMF创建default-gbr承载。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：1. 运营商根据价值用户需求规划。 2. DftGBRBearerSw配置为DISABLE时，其余可选参数恢复为默认配置。                                                                                                                  |
| LOCQOSQCI       | 缺省GBR承载QCI值                       | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载QCI值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～255。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                                                                                                    |
| LOCQOSARP       | 缺省GBR承载ARP值                       | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载ARP值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～15。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                                                                                                     |
| LOCQOSPREEMPCAP | 缺省GBR承载Pre-emption-Capability值    | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Pre-emption-Capability值。Pre-emption Capability即ARP的可抢占能力，代表资源限制时，业务是否可以抢占更低优先级别（Priority Level）的业务。取值范围为ENABLE和DISABLE，ENABLE表示具有抢占能力。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：运营商根据价值用户需求规划。       |
| LOCQOSPREEMPVUL | 缺省GBR承载Pre-emption-Vulnerability值 | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Pre-emption-Vulnerability值。Pre-emption-Vulnerability即ARP的被抢占能力，代表资源限制时，业务是否可以被更高优先级别（Priority Level）的业务抢占。取值范围为ENABLE和DISABLE，ENABLE表示允许被抢占。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：运营商根据价值用户需求规划。 |
| LOCQOSMBRUL     | 缺省GBR承载UL MBR值（千比特/秒）             | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Max-Requested-Bandwidth-UL值(kbit/s)。Max-Requested-Bandwidth-UL定义了上行方向允许的最大比特率。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                             |
| LOCQOSMBRDL     | 缺省GBR承载DL MBR值(千比特/秒)             | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Max-Requested-Bandwidth-DL值(kbit/s)。Max-Requested-Bandwidth-DL定义了下行方向允许的最大比特率。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                             |
| LOCQOSGBRUL     | 缺省GBR承载UL GBR值（千比特/秒）             | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Guaranteed-Bitrate-UL值(kbit/s)。Guaranteed-Bitrate-UL定义了上行方向允许的保障比特率。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                       |
| LOCQOSGBRDL     | 缺省GBR承载DL GBR值（千比特/秒）             | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载Guaranteed-Bitrate-DL值(kbit/s)。Guaranteed-Bitrate-DL定义了下行方向允许的保障比特率。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                       |
| SESSIONTERMINSW | 缺省GBR承载去活时去活PDU会话                 | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置缺省GBR承载去活时是否去活PDU会话。该参数修改后立即生效。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                                                                     |
| ACCTYPE         | 用户接入类型                            | 可选必选说明：条件可选参数 前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用以指定缺省GBR承载适用的用户接入类型。 数据来源：本端规划 取值范围：枚举类型。 RATNON5G：非5G接入类型。RAT5G：5G接入类型。ALL：所有接入类型。 默认值：无 配置原则：运营商根据价值用户需求规划。                                                                                                                |

#### 使用实例

假如运营商需要配置APN支持PCRF/UNC发起default-gbr承载的创建，UNC发起创建时使用本地配置的QoS参数，则使用该实例：

```
SET DFTGBRBEARER: APN="test1",DFTGBRBEARERSW=ENABLE,LOCQOSQCI=1,LOCQOSARP=2,LOCQOSPREEMPCAP=ENABLE,LOCQOSPREEMPVUL=ENABLE,LOCQOSMBRUL=64,LOCQOSMBRDL=64,LOCQOSGBRUL=60,LOCQOSGBRDL=60,SESSIONTERMINSW=ENABLE;
```