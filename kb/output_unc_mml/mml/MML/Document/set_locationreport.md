# 设置用户位置信息（SET LOCATIONREPORT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

实时位置上报特性可以采用PCF/PCRF下发位置trigger的方式来触发，也可以采用SMF/PGW-C/GGSN本地配置位置trigger的方式来触发。SMF/PGW-C/GGSN可以通过本命令来配置本地位置trigger。要开启基于本地位置trigger的实时位置上报特性，除本配置外，还受到全局位置上报功能（SET SMCOMMFUNC）和APN位置上报功能（ADD APN）的控制。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令是在没有部署PCRF/PCF或者PCRF/PCF没有订阅位置相关trigger时用于配置本地位置相关的event trigger。
- 当配置了位置相关trigger，由于存在众多用户移动位置的情况，这样会导致快速增加SGSN/MME/AMF网元与UNC网元间的位置更新消息交互，对网元性能有冲击。所以当需要使用时，位置trigger尽量要大粒度的（比如使用tai而不是ecgi）。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ULITRIGGERFLG   | RAITRIGGERFLG   | TAITRIGGERFLG   | ECGITRIGGERFLG   | NCGITRIGGERFLG   |   MSINFOTIMER |
|:----------------|:----------------|:----------------|:-----------------|:-----------------|--------------:|
| DISABLE         | DISABLE         | DISABLE         | DISABLE          | DISABLE          |           600 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------------|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ULITRIGGERFLG  | 配置用户位置信息的trigger    | 可选必选说明：可选参数  参数含义：该参数用来配置用户位置信息的trigger。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                 |
| RAITRIGGERFLG  | 配置路由区的trigger       | 可选必选说明：可选参数  参数含义：该参数用来配置路由区的trigger。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                    |
| TAITRIGGERFLG  | 配置跟踪区的trigger       | 可选必选说明：可选参数  参数含义：该参数用来配置跟踪区的trigger。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                    |
| ECGITRIGGERFLG | 配置演进的全球小区的trigger   | 可选必选说明：可选参数  参数含义：该参数用来配置演进的全球小区的trigger。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                |
| NCGITRIGGERFLG | 配置NR全球小区的trigger    | 可选必选说明：可选参数  参数含义：该参数用来配置5G NR全球小区的trigger。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                              |
| ULITRIROAMING  | 基于用户漫游属性控制ULI信息上报   | 可选必选说明：该参数在"ULITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户漫游属性控制ULI信息上报。  数据来源：本端规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"ULITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                                                                                                                           |
| RAITRIROAMING  | 基于用户漫游属性控制RAI信息上报   | 可选必选说明：该参数在"RAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户漫游属性控制RAI信息上报。  数据来源：本端规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"RAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                                                                                                                           |
| TAITRIROAMING  | 基于用户漫游属性控制TAI信息上报   | 可选必选说明：该参数在"TAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户漫游属性控制TAI信息上报。  数据来源：本端规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"TAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                                                                                                                           |
| ECGITRIROAMING | 基于用户漫游属性控制ECGI信息上报  | 可选必选说明：该参数在"ECGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户漫游属性控制ECGI信息上报。  数据来源：本端规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"ECGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                                                                                                                        |
| NCGITRIROAMING | 基于用户漫游属性控制NCGI信息上报  | 可选必选说明：该参数在"NCGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户漫游属性控制NCGI信息上报。  数据来源：本端规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"NCGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                                                                                                                        |
| ULITRIRAT      | 基于用户RAT类型控制ULI信息上报  | 可选必选说明：该参数在"ULITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户RAT类型控制ULI信息上报。  数据来源：本端规划 取值范围： UNKNOWN（未知）UTRAN（通用陆地无线接入网）GERAN（GSM/EDGE无线接入网）WLAN（无线局域网）GAN（通用访问网络）HSPA（高速分组接入）EUTRAN（演进型通用陆地无线接入网）EUTRAN_NB_IOT（窄带物联网）NGRAN（5G无线接入网）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"ULITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。如果需要通过此参数控制RatType为NR的会话，需要将SMF软件参数Dword1056Bit8设置为“1”。 |
| RAITRIRAT      | 基于用户RAT类型控制RAI信息上报  | 可选必选说明：该参数在"RAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户RAT类型控制RAI信息上报。  数据来源：本端规划 取值范围： UNKNOWN（未知）UTRAN（通用陆地无线接入网）GERAN（GSM/EDGE无线接入网）WLAN（无线局域网）GAN（通用访问网络）HSPA（高速分组接入）EUTRAN（演进型通用陆地无线接入网）EUTRAN_NB_IOT（窄带物联网）NGRAN（5G无线接入网）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"RAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                        |
| TAITRIRAT      | 基于用户RAT类型控制TAI信息上报  | 可选必选说明：该参数在"TAITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户RAT类型控制TAI信息上报。  数据来源：本端规划 取值范围： UNKNOWN（未知）UTRAN（通用陆地无线接入网）GERAN（GSM/EDGE无线接入网）WLAN（无线局域网）GAN（通用访问网络）HSPA（高速分组接入）EUTRAN（演进型通用陆地无线接入网）EUTRAN_NB_IOT（窄带物联网）NGRAN（5G无线接入网）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"TAITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。如果需要通过此参数控制RatType为NR的会话，需要将SMF软件参数Dword1056Bit8设置为“1”。 |
| ECGITRIRAT     | 基于用户RAT类型控制ECGI信息上报 | 可选必选说明：该参数在"ECGITRIGGERFLG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用来配置基于用户RAT类型控制ECGI信息上报。  数据来源：本端规划 取值范围： UNKNOWN（未知）UTRAN（通用陆地无线接入网）GERAN（GSM/EDGE无线接入网）WLAN（无线局域网）GAN（通用访问网络）HSPA（高速分组接入）EUTRAN（演进型通用陆地无线接入网）EUTRAN_NB_IOT（窄带物联网）NGRAN（5G无线接入网）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数在"ECGITRIGGERFLG"配置为"ENABLE"时，如果不勾选，表示所有类型都有效。                                                     |
| MSINFOTIMER    | 位置更新消息上报的迟滞控制时长(秒)  | 可选必选说明：可选参数  参数含义：该参数用来配置位置更新消息上报的迟滞控制时长(秒)。为了避免单会话内频繁发生更新的Trigger上报，UNC引入了迟滞控制，即控制相邻两次动作之间的最小时间间隔，避免动作频繁导致系统负荷增长。  数据来源：本端规划  取值范围：整数类型，取值范围是0~3600。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOCATIONREPORT查询当前参数配置值。  配置原则：  该参数仅适用于PGW-C。                                                                                                                                                                              |

## 使用实例

设置基于用户位置、跟踪区、全球演进小区、5G NR全球小区trigger的实时位置上报：

```
SET LOCATIONREPORT: ULITRIGGERFLG=ENABLE,RAITRIGGERFLG=DISABLE,TAITRIGGERFLG=ENABLE,ECGITRIGGERFLG=ENABLE,NCGITRIGGERFLG=ENABLE;
```