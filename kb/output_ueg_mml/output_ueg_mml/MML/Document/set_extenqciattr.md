# 设置应用扩展QCI参数属性（SET EXTENQCIATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令可用来控制网关对扩展QCI的资源的管理。包括：是否允许非漫游用户发起non-GBR资源申请流程和漫游用户使用扩展QCI进行接入网络、控制Ga接口话单中QCI参数的取值范围、控制Gy接口CCR消息中QCI信元的取值范围、控制RADIUS Access Request和Accounting Request消息中QCI参数的取值范围和控制N40接口的消息中QCI信元的取值范围。当运营商需要控制扩展QCI相关的参数时，可使用SET EXTENQCIATTR命令对扩展QCI参数进行配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QCICTRLFLAG   | GASHOWFLAG   | GYSHOWFLAG   | RADIUSSHOWFLAG   | N40SHOWFLAG   | EXTENDQCIRANGE   |   EXTQCIMAPDEFQCI |
|:--------------|:-------------|:-------------|:-----------------|:--------------|:-----------------|------------------:|
| DISABLE       | DISABLE      | DISABLE      | DISABLE          | DISABLE       | FROM128TO254     |                 9 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                   |
|:----------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QCICTRLFLAG     | 用户接入的扩展QCI控制开关       | 可选必选说明：可选参数  参数含义：该参数用于指定本地用户是否申请non-GBR资源以及漫游用户是否使用扩展QCI进行接入。该开关仅适用网元为S-GW、P-GW、SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：无                                                                                  |
| GASHOWFLAG      | Ga接口话单的扩展QCI控制开关     | 可选必选说明：可选参数  参数含义：该参数用于指定在Ga接口话单消息里是用标准QCI还是用扩展QCI。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：无                                                                                                                    |
| GYSHOWFLAG      | Gy接口CCR消息的扩展QCI控制开关  | 可选必选说明：可选参数  参数含义：该参数用于指定Gy接口CCR消息是用标准QCI还是用扩展QCI。该开关仅适用网元为P-GW、SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：无                                                                                                   |
| RADIUSSHOWFLAG  | Radius请求信令的扩展QCI控制开关 | 可选必选说明：可选参数  参数含义：该参数用于指定Radius鉴权和计费请求消息里是用标准QCI还是用扩展QCI。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：无                                                                                                              |
| N40SHOWFLAG     | N40接口请求消息的扩展QCI控制开关  | 可选必选说明：可选参数  参数含义：该参数用于指定N40接口请求消息是用标准QCI还是用扩展QCI。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：  该参数值为“ENABLE（使能）”时，表示N40接口请求消息使用扩展QCI。该参数值为“DISABLE（不使能）”时，表示N40接口请求消息使用标准QCI。                                      |
| EXTENDQCIRANGE  | 扩展QCI取值范围            | 可选必选说明：可选参数  参数含义：用来配置扩展QCI的取值范围。  数据来源：本端规划 取值范围： “FROM128TO254（扩展QCI的范围为128到254）”：扩展QCI的范围为128到254“FROM10TO255（扩展QCI的范围为10到255）”：扩展QCI的范围为10到255  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：无                                                             |
| EXTQCIMAPDEFQCI | 扩展QCI映射为标准QCI的缺省值    | 可选必选说明：可选参数  参数含义：该参数用于指定扩展QCI映射为标准QCI的缺省值。该参数缺省值为9。  数据来源：本端规划  取值范围：整数类型，取值范围是1~255。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST EXTENQCIATTR查询当前参数配置值。  配置原则：  该缺省值仅对未配置映射关系的扩展QCI生效，如果在命令ADD EXTENDQCIMAP已配置了映射关系，则该缺省值不生效。  标准QCI/5QI的范围包括1~9和命令ADD STDQOSID中配置的数值，除此以外都属于扩展QCI/5QI。 |

## 使用实例

当用户需要配置允许用户在以上消息中使用扩展QCI时，进行相应指定参数设置。配置参数如下设置“QCICTRLFLAG”为“ENABLE”，“GASHOWFLAG”为“ENABLE”，“GYSHOWFLAG”为“ENABLE”，“RADIUSSHOWFLAG”为“ENABLE”，“N40SHOWFLAG”为“ENABLE”，“EXTQCIMAPDEFQCI”=“1”：

```
SET EXTENQCIATTR:QCICTRLFLAG=ENABLE,GASHOWFLAG=ENABLE,GYSHOWFLAG=ENABLE,RADIUSSHOWFLAG=ENABLE,N40SHOWFLAG=ENABLE,EXTQCIMAPDEFQCI=1;
```