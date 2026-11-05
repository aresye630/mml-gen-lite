# 设置I-SMF/SGW的计费模式和CHF选择参数（SET SERVINGCHGCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、SMF**

该命令用于控制UNC作为I-SMF/SGW时的计费模式和CHF选择参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HOMEQBCSW   | ROAMQBCSW   | VISITQBCSW   |
|:------------|:------------|:-------------|
| DISABLE     | DISABLE     | DISABLE      |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                                                                                                                               |
|:----------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOMEQBCSW       | 归属地用户QBC计费开关 | 可选必选说明：可选参数  参数含义：该参数用于设置I-SMF/SGW上的归属地用户进行QBC计费。  数据来源：全网规划 取值范围： “DISABLE（不使能）”：关闭QBC计费功能“ENABLE（使能）”：打开QBC计费功能  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SERVINGCHGCTRL查询当前参数配置值。  配置原则：无                                                                        |
| ROAMQBCSW       | 漫游用户QBC计费开关  | 可选必选说明：可选参数  参数含义：该参数用于设置I-SMF/SGW上的漫游用户进行QBC计费。  数据来源：全网规划 取值范围： “DISABLE（不使能）”：关闭QBC计费功能“ENABLE（使能）”：打开QBC计费功能  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SERVINGCHGCTRL查询当前参数配置值。  配置原则：无                                                                         |
| VISITQBCSW      | 拜访地用户QBC计费开关 | 可选必选说明：可选参数  参数含义：该参数用于设置I-SMF/SGW上的拜访地用户进行QBC计费。  数据来源：全网规划 取值范围： “DISABLE（不使能）”：关闭QBC计费功能“ENABLE（使能）”：打开QBC计费功能  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SERVINGCHGCTRL查询当前参数配置值。  配置原则：无                                                                        |
| PRIMARYCHFGRP   | 用户主用CHF组     | 可选必选说明：可选参数  参数含义：该参数用于设置I-SMF/SGW用户主CHF组的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SERVINGCHGCTRL查询当前参数配置值。  配置原则：  该参数使用ADD TNFGRP命令配置生成。  当PRIMARYCHFGRP和SECONDARYCHFGRP均未配置时，用户使用SELECTCHFGBYCC，GLBDFTCHFGROUP配置选择CHF。  |
| SECONDARYCHFGRP | 用户备用CHF组     | 可选必选说明：可选参数  参数含义：该参数用于设置I-SMF/SGW用户备用CHF组的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SERVINGCHGCTRL查询当前参数配置值。  配置原则：  该参数使用ADD TNFGRP命令配置生成。  当PRIMARYCHFGRP和SECONDARYCHFGRP均未配置时，用户使用SELECTCHFGBYCC，GLBDFTCHFGROUP配置选择CHF。 |

## 使用实例

配置I-SMF/SGW上归属地用户、漫游用户、拜访地用户进行QBC计费，用户主用CHF组为“CHFGRP1”，备用CHF组为“CHFGRP2”：

```
SET SERVINGCHGCTRL: HOMEQBCSW=ENABLE, ROAMQBCSW=ENABLE, VISITQBCSW=ENABLE, PRIMARYCHFGRP="CHFGRP1", SECONDARYCHFGRP="CHFGRP2";
```