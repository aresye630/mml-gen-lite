# 设置计费接口选择方式（SET CHGMODE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

配置计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置在不同类型终端接入不同网络时所选择的计费接口。

## 注意事项

- 该命令执行后立即生效。

- 4G/5G互操作流程的计费接口不变。2G/3G/4G互操作流程的计费接口不变。
- 当需要使用本命令配置2G接入使用Nchf接口时，需要提前和对端CHF确认是否支持。
- 当5G终端5G接入时，若该命令配置为gagy模式，需要开启特定License项，请提前联系华为技术支持确认。
- 当非5G终端4G接入时，若通过该命令修改参数“FORCED”的取值，则对应的参数“BYIWKUEN5GR4G”的取值会被同步修改成“False（否）”。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMACCTYPE     | BY5GSIWKI   | BYIWKUEN5GR4G   | FORCED   | FORSGWONLY   | FORVSMFONLY   | ISMFCHGSW   | BY5GCNRI   |
|:--------------|:------------|:----------------|:---------|:-------------|:--------------|:------------|:-----------|
| UE5G_RAT4G    | True        | False           | INVALID  | Inherit      | NchfMode      | DISABLE     | False      |
| UE5G_RAT5G    | False       | False           | NchfMode | Inherit      | NchfMode      | DISABLE     | False      |
| UENON5G_RAT4G | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |
| RAT2G         | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |
| RATNBIOT      | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |
| NON_3GPP      | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |
| RATLTEM       | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |
| RAT3G         | False       | False           | GaGyMode | Inherit      | NchfMode      | DISABLE     | False      |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:--------------|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMACCTYPE     | 指定终端和接入类型                 | 可选必选说明：必选参数  参数含义：该参数用于指定终端和接入类型。  数据来源：本端规划 取值范围： “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。“UE5G_RAT5G（5G终端5G接入）”：5G终端5G接入是指在5G接入的PDU激活流程。“UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。“RAT2G（2G接入）”：2G接入是指在2G接入的一次PDP激活流程。“RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。“NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。“RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。“RAT3G（3G接入）”：3G接入是指在3G接入的PDP一次激活流程。  默认值：无。  配置原则：无                                                                                                  |
| BY5GSIWKI     | 按5GS互操作指示选择计费接口           | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT4G"时为条件可选参数。  参数含义：该参数用于配置是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S11、SS5/S8、S2b接口的“5GS Interworking Indication”参数。  数据来源：全网规划 取值范围： False（否）True（是）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：  本参数为TRUE时，当对端携带“5GS Interworking Indication”参数为1时，选择Nchf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择GaGy接口。  本参数为FALSE且BY5GCNRI参数为FALSE时，根据FORCED参数选择计费接口，需要配置FORCED参数。                                                                                      |
| BYIWKUEN5GR4G | 非5G终端4G接入时按5GS互操作指示选择计费接口 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"时为条件可选参数。  参数含义：该参数专用于配置非5G终端4G接入场景下是否按5GS互操作标识的取值来选择计费接口。“5GS互操作标识”是指S11、S5/S8、S2b接口的“5GS Interworking Indication”参数。  数据来源：全网规划 取值范围： False（否）True（是）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：  本参数为TRUE时，当对端携带“5GS Interworking Indication”参数为1时，选择Nchf接口；当对端携带“5GS Interworking Indication”参数为0，或者对端未携带“5GS Interworking Indication”参数时，选择GaGy接口。  本参数为FALSE且BY5GCNRI参数为FALSE时，根据FORCED参数选择计费接口，需要配置FORCED参数。                                                                       |
| FORCED        | 指定的计费接口                   | 可选必选说明：该参数在"TMACCTYPE"配置为"RAT2G"、"RATNBIOT"、"NON_3GPP"、"RATLTEM"、"RAT3G"时为条件必选参数。该参数在"TMACCTYPE"配置为"UE5G_RAT5G"、"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。  参数含义：该参数用于指定计费接口。  数据来源：全网规划 取值范围： “GaGyMode（GaGy模式）”：GaGy模式“NchfMode（Nchf模式）”：Nchf模式“INVALID（无效值）”：无效计费模式  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：  当前版本取值为INVALID，将会选择Nchf模式。                                                                                                                                                                                          |
| FORSGWONLY    | 作为SGW计费模式                 | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。  参数含义：作为SGW时的计费模式。  数据来源：全网规划 取值范围： GaGyMode（GaGy模式）NchfMode（Nchf模式）Inherit（继承其他选项）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：  当前版本取值为Inherit，将会选择GaGy模式。                                                                                                                                                                                                                                                                                                         |
| FORVSMFONLY   | 作为V-SMF计费模式               | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT5G"时为条件可选参数。  参数含义：该参数用于指定作为V-SMF时的计费模式。  数据来源：全网规划 取值范围： “GaGyMode（GaGy模式）”：GaGy模式“NchfMode（Nchf模式）”：Nchf模式  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                        |
| ISMFCHGSW     | I-SMF是否支持计费               | 可选必选说明：该参数在"TMACCTYPE"配置为"UE5G_RAT5G"时为条件可选参数。  参数含义：作为I-SMF计费模式。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                             |
| BY5GCNRI      | 按5GC无限制接入标识选择计费接口         | 可选必选说明：该参数在"TMACCTYPE"配置为"UENON5G_RAT4G"、"UE5G_RAT4G"时为条件可选参数。  参数含义：该参数用于配置是否按5GC无限制接入标识的取值来选择计费接口。“5GC无限制接入标识”是指S11、S5/S8、S2b接口的“5GC Not Restricted Indication Selection”参数。  数据来源：本端规划 取值范围： False（否）True（是）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGMODE查询当前参数配置值。  配置原则：  本参数为TRUE时，当对端携带“5GC Not Restricted Indication Selection”参数为1时，选择Nchf接口；当对端携带“5GC Not Restricted Indication Selection”参数为0，或者对端未携带“5GC Not Restricted Indication Selection”参数时，选择GaGy接口。  本参数为FALSE且BY5GSIWKI参数或BYIWKUEN5GR4G参数或为FALSE时，根据FORCED参数选择计费接口，需要配置FORCED参数。 |

## 使用实例

指定5G终端4G接入的计费接口为Nchf。

```
SET CHGMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=False, FORCED=NchfMode;
```