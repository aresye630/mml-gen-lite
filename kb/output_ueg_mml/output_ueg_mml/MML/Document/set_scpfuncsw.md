# 设置间接路由功能（SET SCPFUNCSW）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

指定网元之间网络部署未调整时，执行该命令会导致实际功能不生效。

间接路由和直连路由模式间切换，可能存在业务呼损。

**适用NF：AMF、SMF、SMSF、NCG、NWDAF、NEF、SCF**

该命令用于设置是否开启间接路由功能和服务发现代理功能。可通过指定本端和对端的NF类型进行设置。

- 当间接路由开关为ON且服务发现代理开关为ON，区域位置开关为OFF，且已经加载相关License时候，开启ModelD模式。
- 当间接路由开关为ON，服务发现代理开关为OFF，区域位置开关为OFF，已经加载相关License时候，开启ModelC模式（不判断是否同大区）。
- 当间接路由开关为ON，服务发现代理开关为OFF，区域位置开关为ON，已经加载相关License时候，需要判断是否同大区。跨大区则使用ModelC，否则使用直连模式。
- 当间接路由开关为OFF，发现代理为OFF，区域位置开关为OFF时，与NF对应的业务消息交互和服务发现均处于直连模式。
- 当拨测开关为ON，启动拨测阶段。反之则走正常流程。
- 直连不支持拨测。

## 注意事项

- 该命令执行后立即生效。

- SCP网元添加完成（通过命令ADD PNFPROFILE添加）以后才允许设置间接路由开关和服务发现代理开关同时为ON；
- 删除最后一条SCP配置前（通过命令RMV PNFPROFILE删除），所有记录的间接路由开关和服务发现代理开关需要先设置为OFF。
- 间接路由开关为OFF时，服务发现代理不允许为ON。
- 当前仅支持AMF-UDM;AMF-AUSF;AMF-PCF;AMF-SMF;AMF-SMSF;AMF-AMF;SMSF-UDM;SMSF-AMF;SMF-UDM;SMF-PCF;SMF-CHF;SMF-SMF;SMF-AMF;CHF-CUSTOM\_OSC;AMF-5G-EIR；AMF-NSSF;AMF-GMLC;AMF-LMF;AMF-CBCF;NWDAF-PCF;NWDAF-NWDAF开启modelC功能。
- 当前仅支持AMF-UDM;AMF-AUSF;AMF-PCF;AMF-AMF;SMF-UDM;SMF-PCF;SMF-CHF;CHF-CUSTOM\_OSC;AMF-5G-EIR;AMF-NSSF;AMF-GMLC;AMF-LMF;AMF-CBCF开启modelC区域使能功能。
- 当前仅支持AMF-UDM;AMF-AUSF;AMF-PCF;AMF-SMSF;SMSF-UDM;SMSF-AMF;SMF-UDM;SMF-PCF;SMF-CHF;NWDAF-PCF;NWDAF-NWDAF开启modelD功能。
- 如果PnfProfile里没有配置scp，但是开关设置为了scp模式。那么会返回服务发现失败的响应，不会滑落为直连状态。
- 不支持ModelC和ModelD之间的直接切换。
- ModelC模式下，将拨测开关为设置为ON，存量用户依然保持ModelC模式。
- 关闭ModelC模式后，如果间接路由功能开关和拨测开关同时设置为ON，存量用户依然保持ModelC模式。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LNFTYPE   | PNFTYPE    | SCPROUTESW   | SCPDISCSW   | REGIONSW   | DIALTESTSW   |
|:----------|:-----------|:-------------|:------------|:-----------|:-------------|
| AMF       | UDM        | OFF          | OFF         | OFF        | OFF          |
| AMF       | AUSF       | OFF          | OFF         | OFF        | OFF          |
| AMF       | PCF        | OFF          | OFF         | OFF        | OFF          |
| SMF       | UDM        | OFF          | OFF         | OFF        | OFF          |
| SMF       | PCF        | OFF          | OFF         | OFF        | OFF          |
| SMF       | CHF        | OFF          | OFF         | OFF        | OFF          |
| SMSF      | UDM        | OFF          | OFF         | OFF        | OFF          |
| CHF       | CUSTOM_OCS | OFF          | OFF         | OFF        | OFF          |
| AMF       | SMF        | OFF          | OFF         | OFF        | OFF          |
| AMF       | AMF        | OFF          | OFF         | OFF        | OFF          |
| SMF       | AMF        | OFF          | OFF         | OFF        | OFF          |
| SMSF      | AMF        | OFF          | OFF         | OFF        | OFF          |
| SMF       | SMF        | OFF          | OFF         | OFF        | OFF          |
| AMF       | SMSF       | OFF          | OFF         | OFF        | OFF          |
| AMF       | EIR        | OFF          | OFF         | OFF        | OFF          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LNFTYPE    | 本端NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定本端NF的类型。  数据来源：全网规划 取值范围： “AMF（AMF）”：NF类型为AMF“SMF（SMF）”：NF类型为SMF“SMSF（SMSF）”：NF类型为SMSF“CHF（CHF）”：NF类型为CHF“NWDAF（NWDAF）”：NF类型为NWDAF  默认值：无。  配置原则：无                                                                                                                                                                                                                                                            |
| PNFTYPE    | 对端NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定对端NF的类型。  数据来源：全网规划 取值范围： “UDM（UDM）”：NF类型是UDM“AUSF（AUSF）”：NF类型为AUSF“PCF（PCF）”：NF类型为PCF“CHF（CHF）”：NF类型为CHF“CUSTOM_OCS（CUSTOM_OCS）”：NF类型为CUSTOM_OCS“AMF（AMF）”：NF类型为AMF“SMF（SMF）”：NF类型为SMF“SMSF（SMSF）”：NF类型为SMSF“EIR（5G-EIR）”：NF类型为5G-EIR“NSSF（NSSF）”：NF类型为NSSF“GMLC（GMLC）”：NF类型为GMLC“LMF（LMF）”：NF类型为LMF“CBCF（CBCF）”：NF类型是CBCF“NWDAF（NWDAF）”：NF类型为NWDAF  默认值：无。  配置原则：无                                          |
| SCPROUTESW | 间接路由功能开关 | 可选必选说明：可选参数  参数含义：该参数用于设置间接路由功能，如果设置为ON，则指定的本端和对端类型的NF之间通过SCP转发。  数据来源：全网规划 取值范围： OFF（OFF）ON（ON）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPFUNCSW查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                  |
| SCPDISCSW  | 服务发现代理开关 | 可选必选说明：可选参数  参数含义：该参数用于设置是否使用SCP代理NF的服务发现功能，如果设置为ON，则指定的本端和对端类型之间的NF服务发现功能通过SCP间接实现。注意，不是通过直接和SCP进行服务发现交互，而是在业务消息交互的过程中，SCP解码业务消息获得用户号码等信息进行消息路由或抽取业务消息里携带的服务发现头到NRF进行服务发现。  数据来源：全网规划 取值范围： OFF（OFF）ON（ON）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPFUNCSW查询当前参数配置值。  配置原则：无                                                                                                                                                       |
| REGIONSW   | 区域位置开关   | 可选必选说明：可选参数  参数含义：该参数用于指定Model C间接路由模式下，是否对请求方NF和目标NF进行同区域判断以便进行对应的直接/间接路由策略。当开关设置为“ON”时，系统对请求方NF和目标NF进行区域判断，当两者属于同一区域时，NF间使用直连路由的方式；当两者属于不同区域时，NF间使用Model C间接路由方式。当开关设置为“OFF”时，系统不对请求方NF和目标NF进行区域判断，直接使用Model C间接路由。请求方NF和目标NF进行同区域判断时，NF所在的区域信息在SET NFREGIONINFO中配置。 该参数在"SCPROUTESW"设置为"ON"，"SCPDISCSW"设置为"OFF"的Model C场景下才有效。  数据来源：本端规划 取值范围： OFF（OFF）ON（ON）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPFUNCSW查询当前参数配置值。  配置原则：无 |
| DIALTESTSW | 拨测开关     | 可选必选说明：可选参数  参数含义：该参数用于指定是否开启Model-D或Model-C模式的业务拨测阶段。 拨测只支持基于SUPI号段、GPSI号段、ROUTINGIND及PLMN控制。 Model-D拨测支持的对端NF类型只包括：UDM、PCF、AUSF。 Model-C拨测目前支持的本端NF类型只包括：AMF、SMF。 当该参数取值为ON时，只针对通过ADD PNFSUPI、ADD PNFGPSI、ADD PNFROUTEIND及ADD PNFPLMN命令配置的用户生效Model-D或Model-C模式，并且NFINSTANCEID配置为"sbidialtest"。 直连不支持拨测。  数据来源：本端规划 取值范围： OFF（OFF）ON（ON）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCPFUNCSW查询当前参数配置值。  配置原则：无                        |

## 使用实例

运营商A为了减少AMF和UDM之间的HTTP链路数量，在两者中间引入了SCP网元，AMF和UDM之间需要开启间接路由功能和服务发现代理功能；

```
SET SCPFUNCSW:LNFTYPE=AMF,PNFTYPE=UDM,SCPROUTESW=ON,SCPDISCSW=ON, REGIONSW=OFF;
```