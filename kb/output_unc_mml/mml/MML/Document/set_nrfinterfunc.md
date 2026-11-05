# 设置国际漫游功能参数（SET NRFINTERFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

若ROAMINSUPIWLSW置为FUNC\_ON而未通过ADD ROAMINSUPIWL配置漫入SUPI服务发现白名单会导致漫入场景下在I-NRF上服务发现他网AUSF/UDM失败。

**适用NF：NRF**

此命令用于设置NRF国际漫游功能参数。

## 注意事项

- 该命令执行后立即生效。

- 某些参数支持基于PLMN粒度配置不同于默认值的其他取值，如果需要根据某些对端PLMN定制不同的功能，可使用“增加基于对端PLMN国际漫游功能参数（ADD NRFPMNINTERFUNC）”命令进一步做基于PLMN细分的功能配置。若某PLMN没有在NRFPMNINTERFUNC命令中配置，访问该HPLMN时就以本命令配置的默认功能为准。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DISCVSMFSW   | SUBLNKMODEUPSW   | FAILOVERCODE        | HNRFFQDNSW   | HNRFSCHEME   | INRF   | DISCFILTERSW   | PROXYSMFSW   | NOSMFFWDPLY   | PROXYSMFDNN   | ROAMINSUPIWLSW   | INTRAPXYSW   |
|:-------------|:-----------------|:--------------------|:-------------|:-------------|:-------|:---------------|:-------------|:--------------|:--------------|:-----------------|:-------------|
| FUNC_OFF     | FUNC_ON          | 429.500.502.503.504 | FUNC_OFF     | HTTP         | NO     | FUNC_OFF       | FUNC_OFF     | FWD           | ims           | FUNC_OFF         | FUNC_OFF     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:---------------|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DISCVSMFSW     | 服务发现V-SMF精确匹配开关         | 可选必选说明：可选参数  参数含义：该参数用于表示NRF在服务发现过程中是否对vsmf-support-ind进行精确匹配。 开关设置为FUNC_ON时：服务发现过程中，必须严格匹配携带的vsmf-support-ind参数，开关设置为FUNC_OFF时：服务发现过程中，NRF优先使用包含vsmf-support-ind在内的所有属性进行精确匹配，精确匹配有可用NF，就返回满足条件的NF Profile；没有精确匹配到或精确匹配上的NF不可用，就忽略掉该参数，满足其他条件的但没有显式指明V-SMF能力（NF Profile无vsmfSupportInd属性）的NF Profile。  数据来源：全网规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                          |
| SUBLNKMODEUPSW | 跨PLMN订阅更新是否返回404开关      | 可选必选说明：可选参数  参数含义：该参数用于表示国际漫游场景，NRF与NF的路由模式配置更改后，对于存量的跨PLMN订阅记录，是否在下一次收到订阅更新时返回404，用于触发拜访地NF重新发起订阅，刷新路由模式的nfStatusNotificationUri。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                              |
| FAILOVERCODE   | 故障重选状态码                 | 可选必选说明：可选参数  参数含义：该参数用于表示NRF通过SEPP转发请求时，进行对端NF故障重选的HTTP状态码。当对端NF返回的HTTP状态码在本参数的配置范围内时，NRF会进行故障重选，否则流程失败。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：  多个状态码用“.”分割，不配置此参数代表不匹配任何HTTP状态码。                                                                                                                                                                                                                                                            |
| HNRFFQDNSW     | HPLMN NRF的标准FQDN开关      | 可选必选说明：可选参数  参数含义：该参数用于表示本NRF作为拜访地NRF，收到跨PLMN请求时，若没有为目的HPLMN配置分层路由（可通过LST NRFPLMNRT命令查询），NRF是否自动为该HPLMN对应的归属地NRF生成标准FQDN，作为目的NRF的FQDN进行转发。开关设置为FUNC_ON时，允许NRF自动生成FQDN。开关设置为FUNC_OFF时，不自动生成，转发失败。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：  非国际漫游关口局NRF不要配置打开，关口局NRF按需打开。                                                                                                                                                  |
| HNRFSCHEME     | HPLMN NRF的协议模式          | 可选必选说明：该参数在"HNRFFQDNSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数用于指定NRF与对端HPLMN NRF的协议模式。NRF和本PLMN的SEPP之间的协议模式不受此参数控制。  数据来源：本端规划 取值范围： HTTP（HTTP）HTTPS（HTTPS）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                       |
| INRF           | 本NRF是否是国际漫游关口局NRF       | 可选必选说明：可选参数  参数含义：该参数用于表示本NRF是否为国际漫游关口局NRF。国际漫游关口局NRF用于对接SEPP并通过SEPP与其他HPLMN的NF进行交互。  数据来源：本端规划 取值范围： YES（是）NO（否）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                          |
| DISCFILTERSW   | 漫游服务发现InterPlmnFqdn过滤开关 | 可选必选说明：可选参数  参数含义：该参数表示目标NF注册未携带InterPlmnFqdn场景下，漫游服务发现该NF时，NRF是否返回该NF。 开关设置为FUNC_ON时，不返回；开关设置为FUNC_OFF时，正常返回该NF。  数据来源：全网规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                               |
| PROXYSMFSW     | ProxySMF功能开关            | 可选必选说明：可选参数  参数含义：该参数用于表示NRF的proxy SMF功能开关。开关为FUNC_ON表示NRF支持处理proxy SMF定制功能，开关为FUNC_OFF表示不支持处理proxy SMF定制功能。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                    |
| NOSMFFWDPLY    | ProxySMF不匹配时处理策略        | 可选必选说明：该参数在"PROXYSMFSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数表示ProxySMF功能开关开启场景下，NF发起跨PLMN的归属地SMF的服务发现，期望服务发现返回proxy SMF，但本NRF没有匹配的proxy SMF时NRF的处理策略。参数设置为DIRECTRETURN时，NRF直接返回服务发现失败；参数设置为FWD时，NRF继续转发给归属地I-NRF处理，返回归属地I-NRF处理后的最终发现结果。  数据来源：全网规划 取值范围： DIRECTRETURN（直接返回）FWD（转发至对端I-NRF）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                      |
| PROXYSMFDNN    | 发现ProxySMF的DNN网络标识列表    | 可选必选说明：该参数在"PROXYSMFSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数表示发现proxy SMF的DNN网络标识列表，当ProxySMF功能开关开启场景下，NF发起跨PLMN的归属地SMF的服务发现，若本参数的DNN网络标识列表包含服务发现携带的dnn参数的网络标识部分，则NRF判断本次请求期望返回proxy SMF，此时没有匹配上proxy SMF，根据“NOSMFFWDPLY”参数指定的处理策略进行进一步的处理，若匹配上proxy SMF，则正常返回proxy SMF。若不包含，则正常转发处理。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~2048。输入指定的DNN网络标识列表，每个DNN网络标识可输入的字符有字母、十进制数字、“-”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。允许输入多个DNN网络标识，多个DNN网络标识使用"#"分割。字母大小写不敏感。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无 |
| ROAMINSUPIWLSW | 漫入SUPI服务发现白名单开关         | 可选必选说明：可选参数  参数含义：该参数用于表示针对漫入场景，基于用户SUPI号码或SUPI号段列表（通过ADD ROAMINSUPIWL命令配置）I-NRF是否允许服务发现他网AUSF/UDM。 开关设置为FUNC_ON时，允许服务发现他网AUSF/UDM；开关设置为FUNC_OFF时，则返回服务发现失败。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                    |
| INTRAPXYSW     | 允许ProxySMF网内发现开关        | 可选必选说明：该参数在"PROXYSMFSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数表示ProxySMF功能开关开启场景下，NF发起网内（不跨PLMN）的服务发现SMF时，NRF是否允许proxy SMF被发现的开关。参数设置为FUNC_ON时，通过ADD NRFPROXYSMF命令配置的proxy SMF允许被网内发现；参数设置为FUNC_OFF时，则不允许被网内发现。  数据来源：全网规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFINTERFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                         |

## 使用实例

使用以下命令打开服务发现V-SMF精确匹配开关，开启跨PLMN订阅更新是否返回404开关，故障重选状态码设置为429.500.502.503，开启是否为HPLMN NRF生成标准FQDN开关，HPLMN NRF的协议模式设置为HTTP，本NRF设置为国际漫游关口局NRF，设置漫游服务发现InterPlmnFqdn过滤开关为FUNC\_ON，设置ProxySMF功能开关为FUNC\_ON，ProxySMF不匹配时处理策略设置为FWD，发现ProxySMF的DNN网络标识列表设置为ims，漫入SUPI服务发现白名单开关设置为FUNC\_ON，允许ProxySMF网内发现开关设置为FUNC\_ON：

```
SET NRFINTERFUNC: DISCVSMFSW=FUNC_ON, SUBLNKMODEUPSW=FUNC_ON, FAILOVERCODE="429.500.502.503", HNRFFQDNSW=FUNC_ON, HNRFSCHEME=HTTP, INRF=YES, DISCFILTERSW=FUNC_ON, PROXYSMFSW=FUNC_ON, NOSMFFWDPLY=FWD, PROXYSMFDNN="ims", ROAMINSUPIWLSW=FUNC_ON, INTRAPXYSW=FUNC_ON;
```