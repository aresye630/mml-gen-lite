# 增加GMLC权限配置(ADD GMLCAU)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：MME**

此命令用于增加GMLC权限配置。配置指定的GMLC的定位权限信息，MME根据该权限信息来实现对GMLC发起的定位请求的接入控制。

对GMLC的接入权限进行控制，允许/禁止定位请求，只允许接入指定的客户端类型、LCS业务类型的定位请求。

#### 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为160，即最多支持160个GMLC标识不同的记录，但每次执行记录数可以超过160条。
- 一个GMLC标识最多可对应512条权限控制记录，即一个GMLC标识最大支持4个客户端类型，一个指定的(GMLC标识，客户端类型)最大支持128个LCS业务类型。
- 如果只输入GMLCID，则允许接入指定GMLC标识的所有客户端类型及所有LCS业务类型。
- 如果只输入GMLCID与CLTTYPE，则允许指定GMLC标识的指定客户端类型的所有LCS业务类型。
- 如果输入GMLCID、CLTTYPE、SERTYPE，则允许指定的GMLC标识的指定客户端类型的指定LCS业务类型。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                                                                                    |
|:--------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMLCID  | GMLC 标识    | 可选必选说明：必选参数 参数含义：该参数用于指定GMLC标识。 数据来源：整网规划 取值范围：0～639 默认值 ：无 配置原则： GMLC ID必须和ADD GMLC配置表中的GMLC ID一致。                                                                                     |
| CLTTYPE | 支持的客户端类型   | 可选必选说明：可选参数 参数含义：该参数用于标识客户端（LCS Client）类型。 数据来源：整网规划 取值范围：“EMERGENCY_SERVICES（紧急业务）”“VALUE_ADDED_SERVICES（增值业务）”“PLMN_OPERATOR_SERVICES（运营商业务）”“LAWFUL_INTERCEPT_SERVICES（合法定位）” 默认值 ：无 |
| SERTYPE | 支持的LCS业务类型 | 可选必选说明：条件可选参数 参数含义：该参数用于标识LCS Client的指定定位业务。 前提条件：该参数在“支持的客户端类型”输入时有效。 数据来源：整网规划 取值范围： 0～127 默认值 ：无 配置原则：请参考表1。                                                                         |

#### 使用实例

增加一条“GMLC标识”为“1”，“支持的客户端类型”为“VALUE\_ADDED\_SERVICES（增值业务）”，“支持的LCS业务类型”为“3”的GMLC权限配置记录：

ADD GMLCAU: GMLCID=1, CLTTYPE=VALUE\_ADDED\_SERVICES, SERTYPE=3;

#### 参考信息

| 基于服务名称的位置                                     | 标准服务名称                                        | 号码分配    |
|:----------------------------------------------|:----------------------------------------------|:--------|
| Reserved                                      | Reserved                                      | 0       |
| Public Safety Services                        | Emergency Services                            | 1       |
| Public Safety Services                        | Emergency Alert Services                      | 2       |
| Public Safety Services                        | Reserved                                      | 3~5     |
| Location Sensitive Charging                   | Location Sensitive Charging                   | 6       |
| Location Sensitive Charging                   | Reserved                                      | 7~9     |
| Tracking Services                             | Person Tracking                               | 10      |
| Tracking Services                             | Fleet Management                              | 11      |
| Tracking Services                             | Asset Management                              | 12      |
| Tracking Services                             | Reserved                                      | 13~19   |
| Traffic Monitoring                            | Traffic Congestion Reporting                  | 20      |
| Traffic Monitoring                            | Reserved                                      | 21~24   |
| Reserved                                      | Reserved                                      | 25~29   |
| Enhanced Call Routing                         | Roadside Assistance                           | 30      |
| Enhanced Call Routing                         | Routing to Nearest Commercial Enterprise      | 31      |
| Enhanced Call Routing                         | Reserved                                      | 32~35   |
| Reserved                                      | Reserved                                      | 36~39   |
| Location Based Information Services           | Traffic and public transportation information | 40      |
| Location Based Information Services           | City Sightseeing                              | 41      |
| Location Based Information Services           | Localized Advertising                         | 42      |
| Location Based Information Services           | Mobile Yellow Pages                           | 43      |
| Location Based Information Services           | Weather                                       | 44      |
| Location Based Information Services           | Asset and Service Finding                     | 45      |
| Location Based Information Services           | Reserved                                      | 46~59   |
| Entertainment and Community Services          | Gaming                                        | 60      |
| Entertainment and Community Services          | Find Your Friend                              | 61      |
| Entertainment and Community Services          | Dating                                        | 62      |
| Entertainment and Community Services          | Chatting                                      | 63      |
| Entertainment and Community Services          | Route Finding                                 | 64      |
| Entertainment and Community Services          | Where-am-I                                    | 65      |
| Entertainment and Community Services          | Reserved                                      | 66~69   |
| Reserved                                      | Reserved                                      | 70~99   |
| Service Provider & Operator Specific Services | Defined by Service Provider & Operator        | 100~127 |