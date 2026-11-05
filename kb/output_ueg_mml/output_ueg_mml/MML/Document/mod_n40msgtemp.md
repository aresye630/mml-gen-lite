# 修改N40消息属性模板（MOD N40MSGTEMP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改N40消息属性模板，用于控制N40消息中是否携带对应字段。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称                               | 参数说明                                                                                                                                                                                                                                |
|:-------------|:-----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TEMPLATENAME | N40消息属性模板名                         | 可选必选说明：必选参数  参数含义：该参数用于指定N40消息字段模板名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：无                                                                                                                                      |
| SECRATUSAGE  | RANSecondaryRATUsageReport         | 可选必选说明：可选参数  参数含义：N40消息中是否携带RANSecondaryRATUsageReport。  数据来源：本端规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：  该参数配置为DISABLE时，ADD CCT中SECRUTHRESHOLD功能不生效。                                                                    |
| NBEXTENDATTR | NB扩展属性                             | 可选必选说明：可选参数  参数含义：控制NB-IOT、LTEM接入时N40消息是否携带扩展属性信息，包括APN Rate Control、Serving PLMN Rate Control、CP only indication和PtP隧道。  数据来源：本端规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：  仅在SET N40APIVER的FEATURE使能NBIOTCHG或LTEMCHG时生效。 |
| QFIDOWNLINK  | QFI容器中的DownLinkVolume              | 可选必选说明：可选参数  参数含义：N40消息中MultipleQFIcontainer信元是否携带DownLinkVolume。  数据来源：本端规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：无                                                                                                      |
| HOMECHGID    | HomeProvidedChargingID             | 可选必选说明：可选参数  参数含义：N40消息中是否携带HomeProvidedChargingID。  数据来源：本端规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：无                                                                                                                    |
| HWQBCIDCT    | huaweiQBCIndication                | 可选必选说明：可选参数  参数含义：QBC计费时N40消息中是否携带huaweiQBCIndication信元。  数据来源：全网规划 取值范围： DISABLE（不携带该字段）ENABLE（携带该字段）  默认值：无  配置原则：  如果CHF需要SMF显示指示N40消息为QBC计费的消息，开启该功能，开启前请确认对端CHF是否支持该信元。                                                        |
| APPSVCPROVID | applicationserviceProviderIdentity | 可选必选说明：可选参数  参数含义：该参数用于控制N40消息中是否携带applicationserviceProviderIdentity（应用提供商标识）。  数据来源：全网规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：无                                                                                        |
| RCP          | 是否支持携带roamingChargingProfile       | 可选必选说明：可选参数  参数含义：该参数用于控制RCP不协商场景，N40消息中RoamingQBCInformation信元是否携带RoamingChargingProfile。  数据来源：本端规划 取值范围： ENABLE（携带该字段）DISABLE（不携带该字段）  默认值：无  配置原则：  该参数仅在SET HVNEGRCPSW命令的参数VSMFSW或HSMFSW设为DISABLE的场景生效。                        |

## 使用实例

修改名为“n40attr”的模板，配置N40消息中携带RANSecondaryRATUsageReport字段：

```
MOD N40MSGTEMP: TEMPLATENAME="n40attr", SECRATUSAGE=ENABLE;
```