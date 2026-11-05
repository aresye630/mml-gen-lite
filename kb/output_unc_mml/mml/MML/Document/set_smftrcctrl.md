# 设置SMF跟踪控制功能（SET SMFTRCCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

修改该命令可能导致跟踪功能不可用，请谨慎使用并联系华为技术支持协助操作。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置SMF跟踪功能控制参数。

## 注意事项

- 该命令执行后立即生效。

- 该命令中的部分参数取值（TOPO、GTPSIG、GTPC）已废弃，由SET COMMTRCCTRL命令取代。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LAN5GNOTREPORT   | BRC5GNOTREPORT   | RPTFLOWCTRLMSG   |
|:-----------------|:-----------------|:-----------------|
| DISABLE          | DISABLE          | DISABLE          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称             | 参数说明                                                                                                                                                                                                                                                                                                |
|:----------------|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E2EIEIGNORE     | E2E信元忽略开关        | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否忽略E2E跟踪信元。当忽略E2E跟踪信元时，系统不会上报E2E跟踪消息，也不会向下游网元传递跟踪信元。  数据来源：本端规划 取值范围： SMC（SMC）CM4G（CM4G）CM5G（CM5G）POLICY4G（POLICY4G）POLICY5G（POLICY5G）ACCT（ACCT）UESM（UESM）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                        |
| E2ENOTREPORT    | E2E跟踪不上报开关       | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报E2E跟踪消息。  数据来源：本端规划 取值范围： SMC（SMC）CM4G（CM4G）CM5G（CM5G）POLICY4G（POLICY4G）POLICY5G（POLICY5G）ACCT（ACCT）UESM（UESM）UPC（UPC）“TOPO（TOPO）”：已废弃。“GTPSIG（GTPSIG）”：已废弃。VNGM（VNGM）DHCP（DHCP）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无              |
| E2ENOTTRANSFER  | E2E跟踪信元不传递开关     | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否向下游网元传递跟踪信元。  数据来源：本端规划 取值范围： UPF（UPF）PGW（PGW）PCF（PCF）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                                                                                                                           |
| ITFNOTREPORT    | 接口跟踪不上报开关        | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报接口跟踪消息。  数据来源：本端规划 取值范围： “GTPC（GTPC）”：已废弃。N4（N4）USMGa（USM Ga）Gy（Gy）Gx（Gx）USMGTPU（USM GTPU）S6b（S6b）Gi（Gi）DHCP（DHCP）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                                                            |
| USERNOTREPORT   | 用户跟踪不上报开关        | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报用户跟踪消息。  数据来源：本端规划 取值范围： SMC（SMC）CM4G（CM4G）CM5G（CM5G）POLICY4G（POLICY4G）POLICY5G（POLICY5G）ACCT（ACCT）UESM（UESM）UPC（UPC）“TOPO（TOPO）”：已废弃。“GTPSIG（GTPSIG）”：已废弃。VNGM（VNGM）DHCP（DHCP）SMSECM（SMSECM）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无 |
| RANDOMNOTREPORT | 随机用户跟踪不上报开关      | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报随机跟踪消息。  数据来源：本端规划 取值范围： SMC（SMC）CM4G（CM4G）CM5G（CM5G）POLICY4G（POLICY4G）POLICY5G（POLICY5G）ACCT（ACCT）UESM（UESM）UPC（UPC）“TOPO（TOPO）”：已废弃。VNGM（VNGM）SMSECM（SMSECM）DHCP（DHCP）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                      |
| LAN5GNOTREPORT  | 5G LAN组会话跟踪不上报开关 | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报5G LAN组会话跟踪消息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                                                                                                                        |
| BRC5GNOTREPORT  | 5G广播跟踪不上报开关      | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否不上报5G广播跟踪消息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                                                                                                                             |
| RPTFLOWCTRLMSG  | 上报跟踪流控的消息开关      | 可选必选说明：可选参数  参数含义：该参数用于指定系统是否上报跟踪流控消息。当开关为DISABLE时，不上报跟踪流控消息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。  配置原则：无                                                                                                                         |

## 使用实例

假设需要关闭SMC模块的用户跟踪功能时，可以执行如下命令：

```
SET SMFTRCCTRL:USERNOTREPORT=SMC-1&CM4G-0&CM5G-0&POLICY4G-0&POLICY5G-0&ACCT-0&UESM-0;
```