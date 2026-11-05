# 设置逻辑接口DSCP值（SET LOGIFDSCP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、SMSF、NCG、CBC、CBCF**

该命令用于设置信令报文的DSCP值。在IP承载网络中，通常使用DSCP标记来进行业务优先级的区分和QoS保证。为区分不同信令在IP承载网络中不同的转发优先级，UNC支持设置具体信令流报文的DSCP值，使不同的信令按照DSCP值进行优先级转发。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。

## 注意事项

- 该命令执行后立即生效。

- 该命令最大记录数为23。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE   | AMFIFTYPE   | SMFCGWIFTYPE   | NRFIFTYPE   | SMSFIFTYPE   | NSSFIFTYPE   | GIMSGTYPE   | NCGIFTYPE   |   DSCPVALUE |
|:---------|:------------|:---------------|:------------|:-------------|:-------------|:------------|:------------|------------:|
| AMF      | DEFAULT     | nan            | nan         | nan          | nan          | nan         | nan         |          46 |
| AMF      | N26         | nan            | nan         | nan          | nan          | nan         | nan         |          46 |
| AMF      | Namf        | nan            | nan         | nan          | nan          | nan         | nan         |          46 |
| AMF      | N2          | nan            | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | DEFAULT        | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | N4             | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | Nsmf           | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | Gi             | nan         | nan          | nan          | DEFAULT     | nan         |          46 |
| SMF      | nan         | Gi             | nan         | nan          | nan          | RADIUS      | nan         |          46 |
| SMF      | nan         | Gx             | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | Gy             | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | Ga             | nan         | nan          | nan          | nan         | nan         |          46 |
| SMF      | nan         | GTPCIF         | nan         | nan          | nan          | nan         | nan         |          46 |
| NSSF     | nan         | nan            | nan         | nan          | DEFAULT      | nan         | nan         |          46 |
| NSSF     | nan         | nan            | nan         | nan          | Nnssf        | nan         | nan         |          46 |
| SMSF     | nan         | nan            | nan         | DEFAULT      | nan          | nan         | nan         |          46 |
| SMSF     | nan         | nan            | nan         | Nsmsf        | nan          | nan         | nan         |          46 |
| NCG      | nan         | nan            | nan         | nan          | nan          | nan         | DEFAULT     |          46 |
| NCG      | nan         | nan            | nan         | nan          | nan          | nan         | Nchf        |          46 |
| NRF      | nan         | nan            | DEFAULT     | nan          | nan          | nan         | nan         |          46 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE       | NF类型     | 可选必选说明：必选参数  参数含义：该参数用于指定逻辑接口DSCP的NF类型。  数据来源：本端规划 取值范围： “AMF（AMF）”：AMF“SMF（SMF/PGW-C/SGW-C/GGSN-C）”：融合2345G功能，包含SMF/PGW-C/SGW-C/GGSN-C独立或融合的NF形态“NRF（NRF）”：NRF“NSSF（NSSF）”：NSSF“SMSF（SMSF）”：SMSF“NCG（NCG）”：NCG  默认值：无。  配置原则：  UNC产品包含多个NF，如AMF、SMF、NRF、NCG、NSSF、SMSF，这些NF中有些可以融合部署，也可以独立部署，有些必须独立部署，该配置中对部署不敏感。即只需要按NF类型配置，如果需要指定AMF的逻辑接口DSCP，则该参数需要选择为AMF。                                                                                                                           |
| AMFIFTYPE    | AMF接口类型  | 可选必选说明：该参数在"NFTYPE"配置为"AMF"时为条件必选参数。  参数含义：该参数用于指定AMF的接口类型。逻辑接口DSCP按逻辑接口进行配置，指定AMF的接口类型即为给指定接口配置DSCP值。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“N26（N26）”：N26“Namf（Namf）”：AMF的服务化接口，包括N8/N11/N12/N15/N22等“N2（N2）”：N2  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。                                                                                                                    |
| SMFCGWIFTYPE | SMF接口类型  | 可选必选说明：该参数在"NFTYPE"配置为"SMF"时为条件必选参数。  参数含义：该参数用于指定SMF的接口类型。逻辑接口DSCP按逻辑接口进行配置，指定SMF的接口类型即为给指定接口配置DSCP值。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“N4（N4）”：N4“Nsmf（Nsmf）”：SMF的服务化接口，包括N11/N16a/N10/N7/N40等“Gi（Gi）”：Gi“Gx（Gx）”：Gx“Gy（Gy）”：Gy“Ga（Ga）”：Ga“GTPCIF（GTPC协议接口）”：GTPC协议接口包括Gn/Gp/S2b/S4/S11/S5/S8接口“S6b（S6b）”：S6b“DHCP（DHCP）”：DHCP  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| NRFIFTYPE    | NRF接口类型  | 可选必选说明：该参数在"NFTYPE"配置为"NRF"时为条件必选参数。  参数含义：该参数用于指定NRF的逻辑接口类型。当前NRF仅支持服务化接口一种逻辑接口。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“Nnrf（Nnrf）”：NRF的服务化接口  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。                                                                                                                                                                                        |
| SMSFIFTYPE   | SMSF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"SMSF"时为条件必选参数。  参数含义：该参数用于指定SMSF的逻辑接口类型。当前SMSF仅支持服务化接口一种逻辑接口类型。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“Nsmsf（Nsmsf）”：SMSF的服务化接口  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。                                                                                                                                                                                |
| NSSFIFTYPE   | NSSF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"NSSF"时为条件必选参数。  参数含义：该参数用于指定NSSF的逻辑接口类型。当前NSSF仅支持服务化接口一种逻辑接口类型。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“Nnssf（Nnssf）”：NSSF的服务化接口  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。                                                                                                                                                                                |
| GIMSGTYPE    | Gi接口消息类型 | 可选必选说明：该参数在"SMFCGWIFTYPE"配置为"Gi"时为条件必选参数。  参数含义：该参数用于指定服务化接口的消息类型。服务化接口消息包括了注册消息、服务发现消息、心跳消息和信令消息。  数据来源：本端规划 取值范围： “DEFAULT（DEFAULT）”：未指定消息类型“RADIUS（RADIUS）”：Gi接口的Radius计费和鉴权信令  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  该参数指定为DEFAULT时，表示Gi接口下的指定消息按设置的DSCP值生效，未指定的消息按该DEFAULT配置的DSCP值生效。                                                                                                                                                                |
| NCGIFTYPE    | NCG接口类型  | 可选必选说明：该参数在"NFTYPE"配置为"NCG"时为条件必选参数。  参数含义：该参数用于指定NCG的接口类型。当前NCG仅支持服务化接口一种逻辑接口类型。  数据来源：本端规划 取值范围： “DEFAULT（未指定接口）”：未指定接口“Nchf（Nchf）”：NCG的服务化接口  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：  如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。                                                                                                                                                                                        |
| DSCPVALUE    | DSCP值    | 可选必选说明：可选参数  参数含义：该参数用于指定设置的DSCP值。  数据来源：本端规划  取值范围：整数类型，取值范围是0~63。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                |

## 使用实例

若运营商想设置AMF的逻辑接口N26的DSCP值为60，则可以使用如下命令：

```
SET LOGIFDSCP: NFTYPE=AMF, AMFIFTYPE=N26, DSCPVALUE=60；
```