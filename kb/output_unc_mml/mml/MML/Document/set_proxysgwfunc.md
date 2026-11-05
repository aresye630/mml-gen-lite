# 设置Proxy SGW功能参数（SET PROXYSGWFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C**

该命令用于设置Proxy S-GW特性的功能参数。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QUERYTYPE   | CTRLTYPE   | ANALYSETYPE   | PERMIT4TO2   | FWDSRUDRSW   | FWD5GSIWKISW   | FWD5GCNRISW   |
|:------------|:-----------|:--------------|:-------------|:-------------|:---------------|:--------------|
| IMSI_FIRST  | REJECT     | LOCAL_FIRST   | ENABLE       | ENABLE       | ENABLE         | ENABLE        |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                      |
|:-------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE    | 查询类型          | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SGW特性中根据本地配置查找归属地PGW地址时的查询类型。  数据来源：本端规划 取值范围： IMSI_FIRST（IMSI优先）MSISDN_FIRST（MSISDN优先）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：无                                                                                                                            |
| CTRLTYPE     | 控制类型          | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SGW特性接入列表功能中IMSI和MSISDN同时匹配时是否允许接入。  数据来源：本端规划 取值范围： ALLOW（允许）REJECT（拒绝）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  配置为REJECT，表示IMSI和MSISDN同时匹配时，二者中任意一个配置为REJECT则拒绝接入；配置为ALLOW，表示IMSI和MSISDN同时匹配时，二者中任意一个配置为ALLOW则允许接入。                                      |
| ANALYSETYPE  | 解析方式          | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SGW获取归属地PGW地址的方式。  数据来源：本端规划 取值范围： “LOCAL_FIRST（本地配置优先）”：本地配置未命中时尝试使用DNS Server数据“SERVER_FIRST（DNS Server配置优先）”：DNS Server数据未命中时尝试使用本地配置  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  配置为LOCAL_FIRST时，表示优先从本地配置获取归属PGW-C的IP；配置为DNS_FIRST时，表示优先从DNS获取归属PGW-C的IP。 |
| PERMIT4TO2   | 是否允许4切2       | 可选必选说明：可选参数  参数含义：该参数用于控制UNC作为Proxy SGW-C时，是否允许用户从4G切换到2G。  数据来源：本端规划 取值范围： ENABLE（使能）DISABLE（不使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  若配置为DISABLE，则Proxy SGW-C接收到切换的Update PDP Context Request消息时，拒绝该消息并且删除会话。                                                                       |
| FWDSRUDRSW   | 透传NSA流量开关     | 可选必选说明：可选参数  参数含义：该参数用于控制UNC作为Proxy SGW-C时，是否允许透传Secondary RAT Usage Data Report信元给PGW-C。  数据来源：全网规划 取值范围： ENABLE（使能）DISABLE（不使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  若配置为DISABLE，则Proxy SGW-C接收到从SGW-C发送的携带有Secondary RAT Usage Data Report信元的消息时，不透传流量给PGW-C。                       |
| FWD5GSIWKISW | 透传5GSIWKI标志开关 | 可选必选说明：可选参数  参数含义：该参数用于控制作为Proxy SGW-C时，是否允许透传5GS Interworking Indication标志给PGW-C。  数据来源：全网规划 取值范围： ENABLE（使能）DISABLE（不使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  若配置为DISABLE，则Proxy SGW-C接收到从SGW-C发送的Create Session Request消息中存在5GS Interworking Indication标志时，不将该标志透传给PGW-C。           |
| FWD5GCNRISW  | 透传5GCNRI标志开关  | 可选必选说明：可选参数  参数含义：该参数用于控制作为Proxy SGW-C时，是否允许透传5GC Not Restricted Indication标志给PGW-C。  数据来源：全网规划 取值范围： ENABLE（使能）DISABLE（不使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSGWFUNC查询当前参数配置值。  配置原则：  若配置为DISABLE，则Proxy SGW-C接收到从SGW-C发送的Create Session Request消息中存在5GC Not Restricted Indication标志时，不将该标志透传给PGW-C。       |

## 使用实例

配置Proxy S-GW功能参数的查询类型为IMSI\_FIRST，控制类型为ALLOW，解析方式为LOCAL\_FIRST，是否允许4切2为ENABLE，透传NSA流量开关为ENABLE，透传5GSIWKI标志开关为ENABLE，透传5GCNRI标志开关为ENABLE，执行如下命令：

```
SET PROXYSGWFUNC: QUERYTYPE=IMSI_FIRST, CTRLTYPE=ALLOW, ANALYSETYPE=LOCAL_FIRST, PERMIT4TO2=ENABLE, FWDSRUDRSW=ENABLE, FWD5GSIWKISW=ENABLE, FWD5GCNRISW=ENABLE;
```