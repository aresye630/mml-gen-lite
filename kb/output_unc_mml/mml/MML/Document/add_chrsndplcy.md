# 增加CHR传输策略(ADD CHRSNDPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于增加CHR传输策略，满足CHR传输策略的用户的CHR才会传输给CloudUDN。

#### 注意事项

- 此命令最大记录数为1000。
- CHR传输开关打开（**SET CHRSTORECFG**命令中参数“CHR存储开关”设置为“OFF”或参数“CHR存储开关”设置为“ON”并且参数“存储类型”设置为“STORE\_AND\_SEND”），且CHR传输策略控制参数（**SET CHRSNDPLCYCFG**）中的“CHRSNDPLCYSELECT”参数设置为“自定义策略传输”时，该命令执行后立即生效。
- 本命令参数“TYPE”选择为“签约APN”时：
  1. 如果传输CHR时尚未获取到用户的签约数据，该用户的CHR是否传输受**SET CHRSNDPLCYCFG**中的“NOSUBSWITCH”参数控制。
  2. 如果用户的签约数据中存在该命令配置的APNNI，该用户的CHR将传输给CloudUDN。
  3. 如果用户的签约数据中不存在该命令配置的APNNI，该用户的CHR不传输给CloudUDN。
- 本命令参数“TYPE”选择为“APNNI（签约APNNI）”时，只针对用户签约数据中的APNNI（如果用户配置了**ADD SMSUBDATA**，以修改后的签约数据为准）进行判断，不针对用户具体流程中请求的APNNI或者请求纠错后的APNNI进行判断；如果CHR传输时当前用户的网络类型与签约数据的网络类型不同，以签约数据的网络类型为准。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                 |
|:-------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | CHR传输策略类型 | 可选必选说明：必选参数 参数含义：该参数用于指定CHR传输策略类型。 数据来源：本端规划 取值范围：“APNNI（签约APNNI）”：表示签约数据中包含该APNNI的用户的CHR才会传输给CloudUDN。 默认值：无 配置原则：当前仅支持配置“签约APNNI”                                                                                                                                                  |
| APNNI  | APN网络标识   | 可选必选说明：条件必选参数 参数含义：该参数用于指定满足CHR传输策略的签约APNNI。 该参数在“CHR传输策略类型”参数配置为“APNNI（签约APNNI）”后生效。 数据来源：本端规划 取值范围：1~62位字符串 默认值：无 配置原则：APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔，每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。本命令中APNNI不允许配置为“*”。 |

#### 使用实例

增加CHR传输策略，CHR存盘配置（SET CHRSTORECFG）中参数CHR存储开关打开，“存储类型”设置为“存储和转发”；CHR传输策略控制参数（SET CHRSNDPLCYCFG）中的参数CHRSNDPLCYSELECT设置为“自定义策略传输”；CHR传输策略类型为“签约APNNI”，APNNI设置为“HUAWEI.COM”：

`SET CHRSTORECFG: STOREALLFLAG=ON, STOREALLTYPE=STORE_AND_SEND;`

`SET CHRSNDPLCYCFG: CHRSNDPLCYSELECT=CUSTOMIZE;`

`ADD CHRSNDPLCY: TYPE=APNNI, APNNI="HUAWEI.COM";`