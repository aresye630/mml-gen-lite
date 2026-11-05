# 设置AMF策略功能（SET AMFPLCYFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF策略功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| AMNOTIFYSW   | UENOTIFYSW   | OLDAMPLCY   | DYNRFSPSW   | RFSPCLRMODE   |   DFTRFSP | DYNNISW   | OVERLAPAREAPLCY   | NEIGHBORLOCSW   | HRAMAGINGSW   |   HRAMAGINGTMR | OLDUEPLCY   |
|:-------------|:-------------|:------------|:------------|:--------------|----------:|:----------|:------------------|:----------------|:--------------|---------------:|:------------|
| NO           | NO           | YES         | YES         | WITHOUT_RFSP  |         0 | NO        | PUBLIC_AREA       | NO              | NO            |            120 | YES         |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AMNOTIFYSW      | AM策略关闭实时通知PCF开关 | 可选必选说明：可选参数  参数含义：该参数用于指示AMF关闭指定的用户（群）创建AM策略偶联功能时，对于已经建立AM策略偶联的用户是否实时向PCF通知删除AM策略偶联。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  当命令AMUEPLCYCTRL中的ISAMASSOC被设置为“NO”，且期望AMF对满足该条件的用户向PCF实时通知删除偶联信息时，参数设置为“YES”。                                                                                                                                                                                                                             |
| UENOTIFYSW      | UE策略关闭实时通知PCF开关 | 可选必选说明：可选参数  参数含义：该参数用于指示AMF关闭指定的用户（群）创建UE策略偶联功能时，对于已经建立UE策略偶联的用户是否实时向PCF通知删除UE策略偶联。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  当命令AMUEPLCYCTRL中的ISUEASSOC被设置为“NO”，且期望AMF对满足该条件的用户向PCF实时通知删除偶联信息时，参数设置为“YES”。                                                                                                                                                                                                                             |
| OLDAMPLCY       | N14接口是否传递AM策略   | 可选必选说明：可选参数  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否给新侧AMF传递AM策略信息。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  AMF在N14接口是否传递PCF相关信元同时受本参数和SET AMFSBICMPT下的OLDPCFID，OLDPCFSETID，OLDAMPLCYURI，OLDAMPLCYTRIG，OLDHPCFID和OLDSMFSELINFO控制。                                                                                                                                                                                                      |
| DYNRFSPSW       | 灵活选频功能开关        | 可选必选说明：可选参数  参数含义：该参数用于设置是否开启灵活选频功能。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  该功能需要和AM-PCF配合使用，需要开启“基于AM-PCF的RFSP功能”license。                                                                                                                                                                                                                                                                                                            |
| RFSPCLRMODE     | RFSP清除方式        | 可选必选说明：该参数在"DYNRFSPSW"配置为"YES"时为条件可选参数。  参数含义：该参数用于设置清除PCF签约RFSP方式。  数据来源：全网规划 取值范围： WITHOUT_RFSP（未携带RFSP）WITH_NULL（携带RFSP为null）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                    |
| DFTRFSP         | 默认RFSP          | 可选必选说明：该参数在"DYNRFSPSW"配置为"YES"时为条件可选参数。  参数含义：该参数用于设置PCF签约的RFSP被清除后，AMF给基站下发的RFSP。  数据来源：全网规划  取值范围：整数类型，取值范围是0~256。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  签约数据或者本地配置的RFSP（ADD NGMMSUBDATA）决策结果优先该参数配置。                                                                                                                                                                                                                                                                   |
| DYNNISW         | 是否开启动态NI功能      | 可选必选说明：可选参数  参数含义：该参数用于配置是否开启动态NI功能。此功能对应动态UE Logo下发功能。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  需要和AM-PCF配合使用，需要开启“基于AMPCF的NI功能”license。                                                                                                                                                                                                                                                                                               |
| FULLNAME        | 默认运营商全称         | 可选必选说明：该参数在"DYNNISW"配置为"YES"时为条件可选参数。  参数含义：该参数用于指定移动网络运营商的全称。AM-PCF取消动态NI时，下发给UE的Configuration Update Command消息中携带的“Full name for network”信元值来源于本参数。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  输入单空格将删除该参数已有配置项。 不允许使用“NULL”作为网络名称。当配置了本参数时，优先使用本参数作为AMF下发给UE的Configuration Update Command消息中携带的“Full name for network”信元值。当不配置本参数时，则使用ADD NITZPLCY的“运营商全称”作为AMF下发给UE的Configuration Update Command消息中携带的“Full name for network”信元值。     |
| SHORTNAME       | 默认运营商简称         | 可选必选说明：该参数在"DYNNISW"配置为"YES"时为条件可选参数。  参数含义：该参数用于指定移动网络运营商的简称。AM-PCF取消动态NI时，下发给UE的Configuration Update Command消息中携带的“Short name for network”信元值优先来源于本参数。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  输入单空格将删除该参数已有配置项。不允许使用“NULL”作为网络名称。当配置了本参数时，优先使用本参数作为AMF下发给UE的Configuration Update Command消息中携带的“Short name for network”信元值。当不配置本参数时，则使用ADD NITZPLCY的“运营商简称”作为AMF下发给UE的Configuration Update Command消息中携带的“Short name for network”信元值。 |
| OVERLAPAREAPLCY | 重叠区域生效策略        | 可选必选说明：可选参数  参数含义：该参数用于指定高铁和公网区域重叠时，区域的生效类型。  数据来源：全网规划 取值范围： PUBLIC_AREA（公网区域）HIGH_RAIL_AREA（高铁区域）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                 |
| NEIGHBORLOCSW   | 相邻位置区域处理开关      | 可选必选说明：可选参数  参数含义：该参数用于设置是否开启相邻位置区域处理功能。开关开启时，公网用户在两个连续公网区域MecArea1和MecArea2之间移动，若MecArea1和MecArea2的PCF发现参数servingscope不相同，AMF先释放MecArea1的AM偶联，再建立MecArea2的AM偶联；若MecArea1和MecArea2的PCF发现参数servingscope相同，AMF复用AM偶联策略且不受本开关控制。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                  |
| HRAMAGINGSW     | 高铁AM偶联老化开关      | 可选必选说明：可选参数  参数含义：该参数用于设置是否开启高铁AM偶联老化功能。开关开启，当用户离开高铁区域后，AM-PCF没有通知AMF删除AM偶联且"高铁AM偶联老化时长"超时后，AMF释放残留的AM偶联策略。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                    |
| HRAMAGINGTMR    | 高铁AM偶联老化时长(min) | 可选必选说明：该参数在"HRAMAGINGSW"配置为"YES"时为条件可选参数。  参数含义：该参数用于设置高铁AM偶联老化时长。当用户离开高铁区域后，AM-PCF没有通知AMF删除AM偶联且该参数超时后，AMF释放残留的AM偶联策略。  数据来源：全网规划  取值范围：整数类型，取值范围是1~1440，单位是分钟。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  此参数配置的时长需要大于NWDAF上HSTRAINCTRL命令配置PUBNETUERECTMR的时长，建议值为120min。                                                                                                                                                                                                     |
| OLDUEPLCY       | N14接口是否传递UE策略   | 可选必选说明：可选参数  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否给新侧AMF传递UE策略信息。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPLCYFUNC查询当前参数配置值。  配置原则：  AMF在N14接口是否传递PCF相关信元同时受本参数和SET AMFSBICMPT下的OLDPCFID，OLDPCFSETID，OLDUEPLCYURI和OLDUEPLCYTRIG控制。                                                                                                                                                                                                                              |

## 使用实例

运营商希望关闭AM策略偶联和UE策略偶联能够实时生效，执行如下命令：

```
SET AMFPLCYFUNC: AMNOTIFYSW=YES, UENOTIFYSW=YES;
```