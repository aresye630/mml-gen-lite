# 设置CHR传输策略控制参数(SET CHRSNDPLCYCFG)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于设置CHR传输策略控制参数，通过配置自定义策略，以满足客户允许指定用户传输CHR的需求。

本命令中CHR传输策略选择为“整系统传输”时，按照**SET CHRSTORECFG**配置的整系统产生的CHR都传输至CloudUDN；CHR传输策略选择为“自定义策略传输”时，只有满足**ADD CHRSNDPLCY**指定策略的用户的CHR传输至CloudUDN。

#### 注意事项

- CHR传输开关打开（**SET CHRSTORECFG**命令中参数“CHR存储开关”设置为“OFF”或参数“CHR存储开关”设置为“ON”并且参数“存储类型”设置为“STORE\_AND\_SEND”），本命令参数“CHR传输策略选择”为“自定义策略传输”时，CHR按照**ADD CHRSNDPLCY**配置的策略进行传输，如果未配置**ADD CHRSNDPLCY**，本命令功能不生效，所有产生的CHR均会传输至CloudUDN。
- 本命令参数“CHR传输策略选择”从“整系统传输”变化为“自定义策略传输”后，功能10分钟内生效。
- 本命令功能不影响异常流程单据存储。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称             | 参数说明                                                                                                                                                                                                        |
|:-----------------|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHRSNDPLCYSELECT | CHR传输策略选择        | 可选必选说明：可选参数 参数含义：该参数用于指定CHR传输策略选择。 数据来源：本端规划 取值范围：“WHOLESYSTEM（整系统传输）”：表示按照SET CHRSTORECFG配置的整系统产生的CHR都传输至CloudUDN。“CUSTOMIZE（自定义策略传输）”：表示满足ADD CHRSNDPLCY指定策略的CHR传输至CloudUDN。 系统初始设置值：“WHOLESYSTEM（整系统传输）” |
| NOSUBSWITCH      | 未获取签约数据场景CHR传输开关 | 可选必选说明：条件可选参数 参数含义：该参数用于指定未获取签约数据时是否传输CHR。 前提条件：该参数在“CHR传输策略选择”配置为“CUSTOMIZE（自定义策略传输）”后生效。 数据来源：本端规划 取值范围：“OFF（关闭）”：表示未获取签约数据场景下，不传输至CloudUDN。“ON（打开）”：表示未获取签约数据场景下，传输至CloudUDN。 系统初始设置值：“ON（打开）”           |

#### 使用实例

增加CHR传输策略，CHR存盘配置（SET CHRSTORECFG）中参数CHR存储开关打开，“存储类型”设置为“存储和转发”；CHR传输策略控制参数（SET CHRSNDPLCYCFG）中的参数CHRSNDPLCYSELECT设置为“自定义策略传输”；CHR传输策略类型为“签约APNNI”，APNNI设置为“HUAWEI.COM”：

`SET CHRSTORECFG: STOREALLFLAG=ON, STOREALLTYPE=STORE_AND_SEND;`

`SET CHRSNDPLCYCFG: CHRSNDPLCYSELECT=CUSTOMIZE;`

`ADD CHRSNDPLCY: TYPE=APNNI, APNNI="HUAWEI.COM";`