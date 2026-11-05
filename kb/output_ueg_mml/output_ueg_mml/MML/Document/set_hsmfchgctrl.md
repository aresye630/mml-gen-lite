# 设置漫游用户在归属地的计费方式和漫游参数的协商方式（SET HSMFCHGCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于控制漫游用户在归属地的计费方式和Roaming Charging Profile的协商方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHGMODE   | FBCNEGRCPSW   | LOCALRCPSELMODE   |
|:----------|:--------------|:------------------|
| FBC       | DISABLE       | LOCALCFG          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                          |
|:----------------|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHGMODE         | 计费模式          | 可选必选说明：可选参数  参数含义：该参数用于设置漫游用户在归属地的计费方式。  数据来源：全网规划 取值范围： “FBC（FBC计费）”：漫游用户在归属地使用FBC计费。“QBC（QBC计费）”：漫游用户在归属地使用QBC计费。“NOCHG（不计费）”：漫游用户在归属地不做计费功能。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。  配置原则：无                                                                                                        |
| FBCNEGRCPSW     | FBC计费漫游参数协商开关 | 可选必选说明：可选参数  参数含义：该参数用于设置漫游用户在归属地做FBC计费时是否和H-CHF进行Roaming Charging Profile的协商。  数据来源：全网规划 取值范围： “DISABLE（不使能）”：不和H-CHF协商Roaming Charging Profile。“ENABLE（使能）”：和H-CHF协商Roaming Charging Profile。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。  配置原则：  该配置为全局配置，当ADD VPLMNCHGMODE的CHGMODE参数配置成FBC计费时，也受本参数控制。 |
| LOCALRCPSELMODE | 本地漫游参数获取方式    | 可选必选说明：可选参数  参数含义：该参数用于设置漫游用户在归属地未从H-CHF获取到Roaming Charging Profile时，Roaming Charging Profile协商结果的获取方式。  数据来源：全网规划 取值范围： “LOCALCFG（使用本地配置）”：使用本地配置生成Roaming Charging Profile。“VSMF（使用V-SMF携带的参数）”：使用V-SMF携带的Roaming Charging Profile。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。  配置原则：无                  |

## 使用实例

设置漫游用户在归属地的计费方式为QBC，未从H-CHF获取到Roaming Charging Profile时，使用本地配置生成：

```
SET HSMFCHGCTRL: CHGMODE=QBC, LOCALRCPSELMODE=LOCALCFG;
```