# 设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于设置全局终端接入的eDRX模式。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令仅对与AMF通过N11接口连接的SMF生效。
- 该命令的EDRXSW参数仅在License项LKV2RCEDRXSM01使能时生效，修改该参数前请使用DSP LICENSE命令确认对应License是否得到授权，并执行LST LICENSESWITCH命令确认License开关为“ENABLE（打开）”。
- 当SET PFCPCMPT的BAR参数设置为“NOT\_SUPPORT”时，SMF不向UPF下发下行包缓存数和下行包缓存时长。
- 当AMF未给SMF下发下行包缓存时长或下发的下行包缓存时长取值为0时，SMF不向UPF下发下行包缓存数和下行包缓存时长。
- 当APN对应的APNEDRXATTR命令记录存在时，该命令的EDRXSW、PKTCNTPRIORITY、DLBUFFPKTCNT和EXTDLBUFFTIME参数的值以APNEDRXATTR命令中同名参数的值为准。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EDRXSW   | PKTCNTPRIORITY   |   DLBUFFPKTCNT |   EXTDLBUFFTIME |
|:---------|:-----------------|---------------:|----------------:|
| DISABLE  | DLBUFFPKTCNT     |             10 |              10 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                           |
|:---------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDRXSW         | 支持eDRX模式开关  | 可选必选说明：可选参数  参数含义：该参数用于指定是否使能NR和NR RedCap终端接入时的eDRX模式。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBEDRXATTR查询当前参数配置值。  配置原则：  如果同时配置了ADD APNEDRXATTR命令中的EDRXSW参数，且ADD APNEDRXATTR命令中的EDRXSW参数不为“INHERIT”，则以ADD APNEDRXATTR命令中的EDRXSW参数的值为准。                            |
| PKTCNTPRIORITY | 下行包缓存数获取优先级 | 可选必选说明：该参数在"EDRXSW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定下行包缓存数获取优先级。  数据来源：全网规划 取值范围： “DLBUFFPKTCNT（优先从DLBUFFPKTCNT获取）”：优先从DLBUFFPKTCNT获取“UDM（优先从UDM签约数据获取）”：优先从UDM签约数据获取  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBEDRXATTR查询当前参数配置值。  配置原则：  当配置为从UDM签约数据获取时，若从UDM签约数据获取不到下行包缓存数，仍会尝试从DLBUFFPKTCNT参数获取下行包缓存数。 |
| DLBUFFPKTCNT   | 下行包缓存数      | 可选必选说明：该参数在"PKTCNTPRIORITY"配置为"DLBUFFPKTCNT"时为条件必选参数。该参数在"PKTCNTPRIORITY"配置为"UDM"时为条件可选参数。  参数含义：该参数用于指定下行包缓存数。  数据来源：全网规划  取值范围：整数类型，取值范围是1~65535。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBEDRXATTR查询当前参数配置值。  配置原则：  无特殊情况建议配置为10，否则联系华为技术支持。                                                            |
| EXTDLBUFFTIME  | 下行包缓存额外时长   | 可选必选说明：该参数在"EDRXSW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定SMF在AMF下发的下行包缓存时长的基础上额外增加的时长。  数据来源：全网规划  取值范围：整数类型，取值范围是0~200。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBEDRXATTR查询当前参数配置值。  配置原则：  无特殊情况建议配置为10，否则联系华为技术支持。                                                                                           |

## 使用实例

假如用户需要增加全局的终端接入的eDRX模式，打开eDRX模式，下行包缓存数获取优先级为从DLBUFFPKTCNT参数获取，给UPF携带下行包缓存数为100，额外下行包缓存时间为10秒时，则使用该实例：

```
SET GLBEDRXATTR: EDRXSW=ENABLE, PKTCNTPRIORITY=DLBUFFPKTCNT, DLBUFFPKTCNT=100, EXTDLBUFFTIME=10;
```