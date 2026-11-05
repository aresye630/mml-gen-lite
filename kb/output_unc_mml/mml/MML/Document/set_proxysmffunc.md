# 设置proxy SMF功能配置（SET PROXYSMFFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于在对接归属地SMF时配置proxy SMF功能控制。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令参数NRFPRISW已弃用。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QUERYTYPE   | EPSIWKSW   | DIFFNSSMFSW   | NRFPRISW   | ACCTPSW   | CTRLTYPE   |
|:------------|:-----------|:--------------|:-----------|:----------|:-----------|
| IMSI_FIRST  | ENABLE     | DISABLE       | DISABLE    | DISABLE   | REJECT     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称                         | 参数说明                                                                                                                                                                                                                                                                                 |
|:------------|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE   | 归属地SMF实例标识的查询                | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF特性中根据本地IMSI或者MSISDN查找归属地SMF实例标识。  数据来源：本端规划 取值范围： “IMSI_FIRST（优先查询IMSI）”：查找归属地SMF标识时优先查询IMSI。“MSISDN_FIRST（优先查询MSISDN）”：查找归属地SMF标识时优先查询MSISDN。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：无                             |
| EPSIWKSW    | 是否优先选择支持互操作能力的归属地SMF         | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF是否优先选择支持互操作能力的归属地SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：无                                                                                                              |
| DIFFNSSMFSW | 是否选择相同DNN和不同S-NSSAI会话的归属地SMF | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF是否选择相同DNN和不同S-NSSAI会话的归属地SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：无                                                                                                      |
| NRFPRISW    | 是否优先向NRF发现归属地SMF             | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF是否优先向NRF发现归属地SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：  该参数已弃用。                                                                                                          |
| ACCTPSW     | 是否根据接入类型过滤归属地SMF             | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF是否根据接入类型过滤归属地SMF。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：无                                                                                                                  |
| CTRLTYPE    | 控制类型                         | 可选必选说明：可选参数  参数含义：该参数用于控制Proxy SMF特性接入列表功能中IMSI和MSISDN同时匹配时是否允许接入。  数据来源：本端规划 取值范围： ALLOW（允许）REJECT（拒绝）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PROXYSMFFUNC查询当前参数配置值。  配置原则：  配置为REJECT，表示IMSI和MSISDN同时匹配时，二者中任意一个配置为REJECT则拒绝接入；配置为ALLOW，表示IMSI和MSISDN同时匹配时，二者中任意一个配置为ALLOW则允许接入。 |

## 使用实例

假设运营商需要增加一个proxy SMF功能控制时，添加proxy SMF配置，控制查询类型为IMSI\_FIRST，支持互操作的开关为ENABLE，选择相同DNN和不同S-NSSAI会话的归属地SMF的开关为DISABLE，优先向NRF发现归属地SMF的开关为DISABLE，根据接入类型过滤归属地SMF的开关为DISABLE，控制类型为ALLOW。

```
SET PROXYSMFFUNC: QUERYTYPE = IMSI_FIRST,EPSIWKSW = ENABLE,DIFFNSSMFSW = DISABLE,NRFPRISW = DISABLE,ACCTPSW = DISABLE,CTRLTYPE = ALLOW;
```