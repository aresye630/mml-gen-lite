# 设置QoS控制配置（SET QOSCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、SGW-C、PGW-C**

该命令用于为指定漫游属性和无线接入类型的用户配置带宽控制的全局开关。当配置该功能后，UNC会对指定的漫游属性和接入类型的用户进行带宽控制，向UPF下发用户签约以及SMF本地配置协商的QoS带宽控制参数。

## 注意事项

- 命令执行后只对新接入用户生效。

- 初始记录中RATTYPE参数RAT类型不包含REDCAP。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| USERTYPE   | RATTYPE                                                                      |
|:-----------|:-----------------------------------------------------------------------------|
| ROAMING    | UNKOWN-1&UTRAN-1&GETRAN-1&WLAN-1&GAN-1&HSPAE-1&EUTRAN-1&EUTRAN_NB_IOT-1&NR-1 |
| VISITING   | UNKOWN-1&UTRAN-1&GETRAN-1&WLAN-1&GAN-1&HSPAE-1&EUTRAN-1&EUTRAN_NB_IOT-1&NR-1 |
| HOME       | UNKOWN-1&UTRAN-1&GETRAN-1&WLAN-1&GAN-1&HSPAE-1&EUTRAN-1&EUTRAN_NB_IOT-1&NR-1 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERTYPE | 用户漫游类型 | 可选必选说明：必选参数  参数含义：该参数用于指定用户的漫游属性。  数据来源：全网规划 取值范围： ROAMING（漫游用户）VISITING（拜访用户）HOME（本地用户）  默认值：无。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RATTYPE  | RAT类型  | 可选必选说明：可选参数  参数含义：该参数用于指定用户的接入类型。  数据来源：全网规划 取值范围： “UNKOWN（UNKOWN）”：RAT类型为未知类型“UTRAN（UTRAN）”：RAT类型为UTRAN类型“GETRAN（GETRAN）”：RAT类型为GERAN类型“WLAN（WLAN）”：RAT类型为WLAN类型“GAN（GAN）”：RAT类型为GAN类型“HSPAE（HSPAE）”：RAT类型为HSPAE类型“EUTRAN（EUTRAN）”：RAT类型为EUTRAN类型“EUTRAN_NB_IOT（EUTRAN_NB_IOT）”：RAT类型为EUTRAN-NB-IOT类型“NR（NR）”：RAT类型为NR类型“REDCAP（REDCAP）”：RAT类型为REDCAP类型  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSCTRL查询当前参数配置值。  配置原则：  SELECT ALL：表示UNKOWN，UTRAN，GERAN，WLAN，GAN，HSPAE，EUTRAN，EUTRAN-NB-IOT，NR，REDCAP，10种类型都选择。  CLEAR ALL：表示UNKOWN，UTRAN，GERAN，WLAN，GAN，HSPAE，EUTRAN，EUTRAN-NB-IOT，NR，REDCAP，10种类型都不选择。  GREYED ALL：表示UNKOWN，UTRAN，GERAN，WLAN，GAN，HSPAE，EUTRAN，EUTRAN-NB-IOT，NR，REDCAP，10种类型都置灰，都不选择。 |

## 使用实例

为接入类型为GETRAN，漫游属性为VISITING的用户打开带宽控制全局开关：

```
SET QOSCTRL USERTYPE=VISITING, RATTYPE=GETRAN-1;
```