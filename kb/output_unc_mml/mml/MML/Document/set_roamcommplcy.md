# 设置漫游通信策略（SET ROAMCOMMPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、CBC、CBCF**

该命令用于设置漫游场景下跨PLMN的网元之间的通信策略。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ROUTEMODE   | SEPPMODE   | HOSTFILLPLCY   | PORTSW   |
|:------------|:-----------|:---------------|:---------|
| SEPP        | HTTPPROXY  | USE_IP_FIRST   | OFF      |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                               |
|:-------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ROUTEMODE    | 漫游路由模式     | 可选必选说明：必选参数  参数含义：该参数用于指定漫游路由模式。  数据来源：全网规划 取值范围： “SEPP（通过SEPP通信）”：漫游跨PLMN的网元之间通过SEPP通信“SCP（优选SCP通信）”：漫游跨PLMN的网元之间优选SCP通信，如果根据本端NfType与对端NfType能找到ROAMSCPFUNCSW配置记录则通过SCP对接SEPP通信（如果没有配置SCP则无法通信）；如果根据本端NfType与对端NfType不能找到ROAMSCPFUNCSW配置记录则通过SEPP通信。“DIRECT（直连通信）”：漫游跨PLMN的网元之间通过直连通信（该枚举值仅用于测试场景）  默认值：无。  配置原则：无               |
| SEPPMODE     | 信令汇聚模式     | 可选必选说明：该参数在"ROUTEMODE"配置为"SEPP"、"SCP"时为条件必选参数。  参数含义：该参数用于指定漫游信令汇聚模式。仅在ROUTEMODE设置为SEPP或SCP时生效。  数据来源：全网规划 取值范围： “HTTPPROXY（Http Proxy）”：在服务请求消息的authority中填写目标NF的地址信息“TARGETAPIROOT（3gpp-Sbi-Target-apiroot）”：在服务请求消息的3gpp-Sbi-Target-apiroot中填写目标NF的地址信息  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMCOMMPLCY查询当前参数配置值。  配置原则：无 |
| HOSTFILLPLCY | SEPP域名填充策略 | 可选必选说明：该参数在"SEPPMODE"配置为"TARGETAPIROOT"时为条件可选参数。  参数含义：该参数用于指定通过3gpp-Sbi-Target-apiroot路由策略通信时，HTTP消息中host的填写策略。  数据来源：全网规划 取值范围： USE_IP_FIRST（优先填写IP）USE_FQDN_FIRST（优先使用FQDN）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMCOMMPLCY查询当前参数配置值。  配置原则：  该参数仅在SEPP通信场景下生效，SCP通信场景通过软参DWORD219 BIT28控制。                               |
| PORTSW       | 是否使用端口开关   | 可选必选说明：该参数在"HOSTFILLPLCY"配置为"USE_FQDN_FIRST"时为条件可选参数。  参数含义：该参数用于指定使用3gpp-Sbi-Target-apiroot路由策略通信时，HTTP中host填写SEPP的FQDN时是否携带端口号。  数据来源：全网规划 取值范围： OFF（OFF）ON（ON）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMCOMMPLCY查询当前参数配置值。  配置原则：无                                                                                          |

## 使用实例

运营商希望漫游跨PLMN的网元之间通过SEPP通信，且在服务请求消息的authority中填写目标NF的地址信息，需要设置漫游通信策略；

```
SET ROAMCOMMPLCY: ROUTEMODE=SEPP, SEPPMODE=HTTPPROXY;
```