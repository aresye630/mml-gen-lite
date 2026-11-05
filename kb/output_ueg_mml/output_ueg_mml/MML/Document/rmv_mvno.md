# 删除MVNO信息表记录(RMV MVNO)

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
- 每次只能删除一条记录。
- 删除的记录不能在MVNONET表（**LST MVNONET**）、MVNORES表（**LST MVNORES**）、MVNOFUN表（**LST MVNOFUN**）、归属网络信息管理（**LST HNOINFO**）、互连PLMN表（**LST CONNECTPLMN**）、SM属性配置表（**LST IMSISMCHAR**）、GGSN/P-GW选择策略表（**LST GWSELPLCY**）、RFSP配置表（**LST RFSP**）、VOICEDEPLOY配置表（**LST VOICEDEPLOY**）、EMGCFG配置表（**LST EMGCFG**）、S1ACCAREALST配置表（**LST S1ACCAREALST**）、ZCCONVERT配置表（**LST ZCCONVERT**）、M2MPLCY配置表（**LST M2MPLCY**）、S1SUBRRLST配置表（**LST S1SUBRRLST**）、IUSUBRRLST配置表（**LST IUSUBRRLST**）、GBSUBRRLST配置表（**LST GBSUBRRLST**）、GTPCINTFATTR配置表（**LST GTPCINTFATTR**）、GTPUINTFATTR配置表（**LST GTPUINTFATTR**）、UFCSFB配置表（**LST UFCSFB**）、NSACTRLPLCY配置表（**LST NSACTRLPLCY**）、MAPCMPTBYIMSI配置表（**LST MAPCMPTBYIMSI**）、MMERESELPLCY配置表（**LST MMERESELPLCY**）、QOSCAP配置表（**LST QOSCAP**）、N26GWSELPLCY配置表（**LST N26GWSELPLCY**）、N26IWKPLCY配置表（**LST N26IWKPLCY**）和DMCMPTBYIMSI配置表（**LST DMCMPTBYIMSI**）中使用。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                             |
|:-------|:-------|:-------------------------------------------------|
| MVNOID | MVNO标识 | 可选必选说明：必选参数 参数含义：该参数用于指定MVNO的标识。 取值范围：1～64 默认值：无 |

#### 使用实例

删除MVNO标识为1的MVNO：

RMV MVNO: MVNOID=1;