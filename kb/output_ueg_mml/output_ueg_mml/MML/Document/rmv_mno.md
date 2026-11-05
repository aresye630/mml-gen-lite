# 删除MNO配置信息(RMV MNO)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于删除MNO的配置信息。

#### 注意事项

- 该命令执行后立即生效。
- 删除的记录不能在本地PLMN管理表（**LST HPLMN**）、归属网络信息管理表（**LST HNOINFO**）、互连PLMN管理表（**LST CONNECTPLMN**）、SM属性配置表（**LST IMSISMCHAR**）、GGSN/P-GW选择策略表（**LST GWSELPLCY**）、RFSP配置表（**LST RFSP**）、VOICEDEPLOY配置表（**LST VOICEDEPLOY**）、EMGCFG配置表（**LST EMGCFG**）、S1ACCAREALST配置表（**LST S1ACCAREALST**）、ZCCONVERT配置表（**LST ZCCONVERT**）、M2MPLCY配置表（**LST M2MPLCY**）、LCSPARAEX配置表（**LST LCSPARAEX**）、S1SUBRRLST配置表（**LST S1SUBRRLST**）、IUSUBRRLST配置表（**LST IUSUBRRLST**）、GBSUBRRLST配置表（**LST GBSUBRRLST**）、GTPCINTFATTR配置表（**LST GTPCINTFATTR**）、GTPUINTFATTR配置表（**LST GTPUINTFATTR**）、UFCSFB配置表（**LST UFCSFB**）、NSACTRLPLCY配置表（**LST NSACTRLPLCY**）、MAPCMPTBYIMSI配置表（**LST MAPCMPTBYIMSI**）、MMERESELPLCY配置表（**LST MMERESELPLCY**）、QOSCAP配置表（**LST QOSCAP**）、N26GWSELPLCY配置表（**LST N26GWSELPLCY**）、N26IWKPLCY配置表（**LST N26IWKPLCY**）和DMCMPTBYIMSI配置表（**LST DMCMPTBYIMSI**）中被使用。
- 一次只能删除一条记录。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                        |
|:-------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MNOID  | MNO标识  | 可选必选说明：必选参数 参数含义：待删除MNO的标识。 取值范围：0，128~254 默认值：无  说明： 0为系统初始值。由于系统初始化后，已存在一条“MNOID”为0的记录，当MNOID参数为0时，执行ADD MNO的效果等同于执行MOD MNO命令。默认记录“MNOID”为0不能被删除。删除该配置前，需要删除引用了该配置中的“MNOID”的ADD CONNECTPLMN和ADD HPLMN等命令。 |

#### 使用实例

删除“MNO标识”为“128”的MNO：

RMV MNO: MNOID=128;