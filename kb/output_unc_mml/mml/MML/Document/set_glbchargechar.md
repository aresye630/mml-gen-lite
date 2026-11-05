# 设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于设置对本地用户、漫游用户、拜访用户所采用的计费属性。

#### 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 基于用户漫游、拜访、本地属性来控制是否提供在线计费和离线计费功能时需要使用SET GLBCHARGECHAR。
- 在5G网络中，当UDM下发签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由SET GLBCHARGECHAR命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用UDM下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。
- 在4G网络中，由左侧MME/SGW携带签约CC（MME从HSS获取的签约CC/SGW通过MME得到签约CC）、并且本地基于全局配置CC场景下，HOMESGSN、ROAMSGSN、VISITSGSN参数配置为ENABLE时，表示使用MME/SGW携带的签约CC，当配置为DISABLE时，表示使用本地全局配置的CC。
- 在2/3G网络中，由左侧SGSN携带签约CC（SGSN从HLR获取得签约CC）。当SGSN携带签约CC、并且本地基于全局配置CC场景下，HOMESGSN、ROAMSGSN、VISITSGSN参数配置为ENABLE时，表示使用SGSN携带的签约CC，当配置为DISABLE时，表示使用本地全局配置的CC。
- 如果配置为使用左侧携带的CC，当UDM、MME/SGW、SGSN未携带CC值或携带错误时，则使用本地配置的CC。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | HOME   | ROAM   | VISIT   | HOMESGSN   | ROAMSGSN   | VISITSGSN   |
|:-------|:-------|:-------|:--------|:-----------|:-----------|:------------|
| 初始值    | 0x0800 | 0x0800 | 0x0800  | ENABLE     | ENABLE     | ENABLE      |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识      | 参数名称             | 参数说明                                                                                                                                                                                                                                                    |
|:----------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOME      | 本地用户计费类型         | 可选必选说明：可选参数 参数含义：HOME是全局配置的本地用户CC，表示本地用户计费类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：输入单空格将删除该参数已有配置项。                                                                    |
| ROAM      | 漫游用户计费类型         | 可选必选说明：可选参数 参数含义：表示漫游用户计费类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：输入单空格将删除该参数已有配置项。                                                                                     |
| VISIT     | 拜访用户计费类型         | 可选必选说明：可选参数 参数含义：表示拜访用户计费类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。 默认值：无 配置原则：输入单空格将删除该参数已有配置项。                                                                                     |
| HOMESGSN  | 本地用户使用SGSN计费属性标志 | 可选必选说明：可选参数 参数含义：本地用户使用serving-node计费属性标志。当HOMESGSN配置为ENABLE时，表示本地用户使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则： DISABLE：禁止本地用户使用servning-node计费属性时配置DISABLE。ENABLE：允许本地用户使用servning-node计费属性时配置ENABLE。   |
| ROAMSGSN  | 漫游用户使用SGSN计费属性标志 | 可选必选说明：可选参数 参数含义：漫游用户使用serving-node计费属性标志。当ROAMSGSN配置为ENABLE时，表示漫游用户使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则： DISABLE：禁止漫游用户使用servning-node计费属性时配置DISABLE。ENABLE：允许漫游用户使用servning-node计费属性时配置ENABLE。   |
| VISITSGSN | 拜访用户使用SGSN计费属性标志 | 可选必选说明：可选参数 参数含义：拜访用户使用servning-node计费属性标志。当VISITSGSN配置为ENABLE时，表示拜访用户使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则： DISABLE：禁止拜访用户使用servning-node计费属性时配置DISABLE。ENABLE：允许拜访用户使用servning-node计费属性时配置ENABLE。 |

#### 使用实例

设置本地用户、漫游用户、拜访用户所采用的计费属性，HOME为“1”，ROAM为“1”，VISIT为“1”，HOMESGSN为“ENABLE”，ROAMSGSN为“ENABLE”，VISITSGSN为“ENABLE”：

```
SET GLBCHARGECHAR:HOME="0x1",ROAM="0x1", VISIT="0x1", HOMESGSN=ENABLE, ROAMSGSN=ENABLE,VISITSGSN=ENABLE;
```