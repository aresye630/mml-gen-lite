# 删除GUSS数据(RMV HGUSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中删除指定IMPI的GUSS数据，删除GBA用户安全设置数据时使用该操作。

## 注意事项

- 如果“GAA服务类型”存在，删除的是“IMPI”下的一条“GAA服务类型”的GUSS数据。
- 如果“GAA服务类型”不存在，删除的是“IMPI”下的所有“GAA服务类型”的GUSS数据。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPI   | IMPI    | 标识一条IMPI的GUSS数据记录的关键参数之一，用于指定需要删除哪个IMPI的GUSS数据记录。要求输入的IMPI值符合NAI格式，字母区分大小写。 取值范围： 长度不超过127的字符串 默认值： 无 说明：必选参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| GSID   | GAA服务类型 | 标识一条IMPI的GUSS数据记录的关键参数之一，用于指定需要删除哪一条“GAA服务类型”的GUSS数据记录，操作员可以使用LST HGUSS操作查询获得。 取值范围： UNSPECIFIC_SERVICE(Unspecific service)：表示系统取值为0。PKI-PORTAL(PKI-Portal)：表示系统取值为1。AUTHENTICATION_PROXY(Authentication Proxy)：表示系统取值为2。PRESENCE(Presence)：表示系统取值为3。MBMS(MBMS)：表示系统取值为4。LIBERTY_ALLIANCE_PROJECT(Liberty Alliance Project)：表示系统取值为5。UICC-TERMINAL_KEY_ESTABLISHMENT(UICC-Terminal Key Establishment)：表示系统取值为6。TERMINAL-REMOTE_DEVICE_KEY_ESTABLISHMENT(Terminal-Remote Device Key Establishment)：表示系统取值为7。ANDSF(ANDSF)：表示系统取值为8。GBA_PUSH(GBA Push)：表示系统取值为9。IMS_BASED_PSS_MBMS(IMS based PSS MBMS)：表示系统取值为10。OPENID_GBA_INTERWORKING(OpenID GBA Interworking)：表示系统取值为11。GENERIC_PUSH_LAYER(Generic Push Layer)：表示系统取值为12。OPENID_INTERWORKING(OpenID Interworking)：表示系统取值为13。 默认值：无。 说明：可选参数。 |

## 使用实例

删除GUSS数据。“IMPI”为“impiinfo”，“GAA服务类型”为“PKI-PORTAL”。

```
RMV HGUSS: IMPI="impiinfo", GSID=PKI-PORTAL;
```