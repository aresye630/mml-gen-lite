# 设置APN的上报属性（SET APNREPORTATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于修改SMF与PCRF/PCF交互的消息使用的APN类型、性能统计使用的APN类型、CG话单使用的APN类型、与AAA交互的鉴权消息和计费消息使用APN类型、以及与OCS/CHF交互使用的APN类型。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 每个APN支持一条配置。
- 当系统未配置时，使用该命令增加性能统计及和各网元交互使用的APN类型配置，当系统存在该配置时，使用该命令修改配置。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：CONGESTIONRPT：DISABLE，INTELLIGENTSEL：DISABLE，LOCATIONREPORT：DISABLE，MAPTRANSDATA：DISABLE，AAAACCT：SERVICE，AAAAUTH：SERVICE，CG：SERVICE，DIAMETERAAA：REQUESTED，OCS：SERVICE，CHF：REQUESTED，PCRF：SERVICE，PCF：REQUESTED，PERFORMANCE：SERVICE，UPF：SERVICE。
- 该配置仅当“APN名称（APN）”参数为真实APN时生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                         |
|:---------------|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称                       | 可选必选说明：必选参数  参数含义：该参数用于指定配置上报属性的APN。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。  默认值：无。  配置原则：  该参数使用ADD APN命令配置生成。                           |
| CONGESTIONRPT  | 拥塞控制                        | 可选必选说明：可选参数  参数含义：该参数用于是否使能基于APN的小区拥塞上报功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                                                  |
| INTELLIGENTSEL | 智能网关选择                      | 可选必选说明：可选参数  参数含义：该参数用于是否基于APN使能网关负荷信息上报功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：  该参数已弃用。                                                                                                         |
| LOCATIONREPORT | 实时位置                        | 可选必选说明：可选参数  参数含义：该参数用于是否使能基于APN的更新消息中所携带的位置信息上报给报表服务器的功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：  该参数已弃用。                                                                                          |
| MAPTRANSDATA   | 通过本地配置获取VLR ID/Global Title | 可选必选说明：可选参数  参数含义：该参数用于控制是否允许此APN下的用户通过本地配置获取VLR ID/Global Title。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：  该参数已弃用。                                                                                   |
| AAAACCT        | 上报给AAA计费的APN名               | 可选必选说明：可选参数  参数含义：该参数用于指定与AAA计费服务器交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                   |
| AAAAUTH        | 上报给AAA鉴权的APN名               | 可选必选说明：可选参数  参数含义：该参数用于指定与AAA鉴权服务器交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                   |
| CG             | 上报给CG的APN名                  | 可选必选说明：可选参数  参数含义：该参数用于指定话单里使用用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                                    |
| DIAMETERAAA    | 上报给Diameter AAA的APN名        | 可选必选说明：可选参数  参数含义：该参数用于指定网关与3GPP AAA服务器交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                              |
| OCS            | 上报给OCS的APN名                 | 可选必选说明：可选参数  参数含义：该参数用于指定与OCS交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                        |
| CHF            | 上报给CHF的APN名                 | 可选必选说明：可选参数  参数含义：该参数用于指定与CHF交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                        |
| PCRF           | 上报给PCRF的APN名                | 可选必选说明：可选参数  参数含义：该参数用于指定与PCRF交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                       |
| PCF            | 上报给PCF的APN名                 | 可选必选说明：可选参数  参数含义：该参数用于指定与PCF交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：无                                                                                        |
| PERFORMANCE    | 上报给话统的APN名                  | 可选必选说明：可选参数  参数含义：该参数用于指定基于APN的性能，是统计在用户请求的APN上，还是用户真正使用的APN上。  数据来源：本端规划  取值范围：当配置使用的APN类型为REQUESTED时：如果用户激活请求里的APN是别名APN，则对于性能统计使用的APN是别名APN对应的真实APN。 REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：  该参数的修改只对新激活用户生效。 |
| UPF            | 上报给用户面的APN名                 | 可选必选说明：可选参数  参数含义：该参数用于指定与用户面交互的消息里携带的APN是用户请求的APN，还是用户真正使用的APN。  数据来源：本端规划 取值范围： REQUESTED（请求的）SERVICE（真实的）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNREPORTATTR查询当前参数配置值。  配置原则：  对于存量APN，建议在SMF配置上报给UPF的APN为真实的APN，否则可能影响已有的用户面功能。对于新建APN，SMF和UPF的配置规划需保持一致。            |

## 使用实例

修改APN为huawei.com下性能统计，头增强，给报表服务器上报记录时或与其他网元交互时使用的APN类型。

```
SET APNREPORTATTR: APN="huawei.com", CONGESTIONRPT=ENABLE, INTELLIGENTSEL=ENABLE, LOCATIONREPORT=ENABLE, MAPTRANSDATA=ENABLE, AAAACCT=REQUESTED, AAAAUTH=SERVICE, CG=SERVICE, DIAMETERAAA=REQUESTED, OCS=REQUESTED, PERFORMANCE=REQUESTED;
```