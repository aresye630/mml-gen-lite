# 增加PUSI基本信息模板(ADD HPUSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中添加一个PUSI基本信息模板。在该操作中，以下关键参数需要与对端网元（AS）协商： PUSI的AS地址。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称      | 参数说明                                                                                                                                                                            |
|:---------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TPLID    | PUSI模板ID  | 可选必选说明：必选参数 参数含义：用于定义PUSI基本信息模板的序号，以方便对PUSI基本信息模板进行查询和引用，配置原则是不能与已有的PUSI基本信息模板的模板ID重复。 取值范围：0～254 缺省值： 无                                                                        |
| TPLNAME  | PUSI模板名称  | 可选必选说明：可选参数 参数含义：该参数用于具体描述一个PUSI基本信息模板，以便于识别。 取值范围： 长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 缺省值： 无                                                                                 |
| AS       | PUSI的AS地址 | 可选必选说明：可选参数 参数含义：HSS与对端网元（AS）对接的参数之一，用于指定PUSI需要用到的对端网元的地址，地址格式必须为SIP格式。需要和对端网元配置的地址协商一致，若不一致，HSS将无法完成发往对端网元的业务处理。 取值范围： 长度不超过127的字符串 缺省值： 无                                     |
| BAR      | 闭锁标志      | 可选必选说明：必选参数 参数含义：指定PUSI的闭锁状态。 取值范围： FALSE(False)：解除闭锁TRUE(TRUE)：闭锁 缺省值： 无                                                                                                       |
| ACTSTATE | 激活状态      | 可选必选说明：必选参数 参数含义：指定PUSI的激活状态。 取值范围： FALSE(False)：未激活 TRUE(TRUE)：激活 缺省值： 无                                                                                                       |
| SERPRVID | 服务提供商标识   | 可选必选说明：可选参数 参数含义：指定的Service Provider ID(服务提供商标识) 取值范围： 长度不超过39的字符串 缺省值： 无                                                                                                       |
| LRI      | 松路由指示信息   | 可选必选说明：可选参数 参数含义：指定PUSI是否签约松路由指示。不指定该参数表示去签约松路由指示。 取值范围： LOOSE_ROUTE_NOT_REQUIRED(LOOSE_ROUTE_NOT_REQUIRED)：去签约松路由指示。LOOSE_ROUTE_REQUIRED(LOOSE_ROUTE_REQUIRED)：签约松路由指示。 缺省值： 无 |
| COMMENT  | 模板注释说明    | 可选必选说明：可选参数 参数含义：该参数用于具体描述一个PUSI基本信息模板的注释信息，以便于理解和使用。 取值范围： 长度不超过512的字符串 缺省值： 无                                                                                                 |

## 使用实例

增加PUSI基本信息模板。PUSI模板ID：10，PUSI模板名称：PUSI Template，PUSI的AS地址：sip:as@huawei.com，闭锁标志：FALSE，激活状态：TRUE，服务提供商标识：1，松路由指示信息：LOOSE\_ROUTE\_NOT\_REQUIRED，模板注释说明：PUSI Template For ADD HTPLPSI。

```
ADD HPUSITPL: TPLID=10, TPLNAME="PUSI Template", AS="sip:as@huawei.com", BAR=FALSE, ACTSTATE=TRUE, SERPRVID="1", LRI=LOOSE_ROUTE_NOT_REQUIRED, COMMENT="PUSI Template For ADD HTPLPSI";
```