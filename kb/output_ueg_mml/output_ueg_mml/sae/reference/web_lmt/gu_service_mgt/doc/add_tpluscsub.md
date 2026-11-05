# 统一模板开户(ADD TPLUSCSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于对GSM/UMTS/EPS/IMS/5G融合用户进行统一开户。

## 注意事项

- 开户前，请使用**ADD KI**命令加载KI。KI是用户鉴权的重要数据，若未加载KI，将无法进行开户操作。
- 当参数“IMPI2的鉴权类型”为“HDA”或者“SDA”时，存在“HA1值2”和“用户名称2”、“密码2”两种加密方式。对于一个“IMPI”，“HA1值2”和“用户名称2”、“密码2”只能存在一种，即只存在“HA1值2”或只存在“用户名称2”和“密码2”的组合。推荐使用HA1值2。
- 当**SET MAPCONF**命令中的“是否启用随机密钥”参数为“TRUE”，本命令中的“IMPI2的鉴权类型”参数为“HDA(HTTP Digest)”或“SDA(SIP Digest)”，执行该命令时如果未执行**SET DEFAULTK2SNO**命令设置默认K2，则执行该命令时会返回错误。
- 在混合组网环境执行该命令，若IMPI/IMPI2已存在，系统提示IMPI/IMPI2已与其它用户关联。
- 当通过**SET HSYSTEMPARA**命令设置“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参为“TRUE(TRUE)”时，执行该命令时会返回错误。
- 用户签约5G虚拟网络组时，对于同一个“切片标识”和“数据网名称”下的5G虚拟网络组，建议用户只签约一个。

## 参数说明

| 参数标识          | 参数名称               | 参数说明                                                                                                                                                                                                                                                                                                                                                                                      |
|:--------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号             | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。 取值范围：1～255 默认值：无。                                                                                                                                                                                                                                                                                                                            |
| IMSI          | IMSI               | 用于标识待开户用户的IMSI号码。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                           |
| ISDN          | MSISDN             | 用于标识待开户用户的MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                         |
| TPLID         | 模板ID               | 用于标识一个GSM/UMTS/EPS/5G业务的开户模板ID，该模板需要通过命令ADD SUBTPL定义，才能在此处索引。 取值范围：0～65534 默认值：无。                                                                                                                                                                                                                                                                                                         |
| LINE2NUM      | 线路2MSISDN          | 用于标识双线路可选业务ALS（Alternative Line Service）第二条线路的MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                     |
| STNSR         | SRVCC会话传输号码        | 用于标识一个STNSR（Session Transfer Number for SRVCC）号码。MME（Mobility Management Entity）使用该参数获取从PS域到CS域的网址路径会话传递。 取值范围：3～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                   |
| ANCHOR        | 锚定标志               | 用于标识是否给用户提供锚定功能。 取值范围：TRUE：无条件锚定。FALSE：不锚定。SELECTIVE：选择性锚定。TCSI：T-CSI锚定。PRE_FALSE：标识用户为未激活的VoWiFi预开户用户，其被叫业务不能锚定到IMS域进行处理，即不能使用IMS业务，只能使用CS业务。PRE_TRUE：标识用户为激活的VoWiFi预开户用户，其被叫业务可以锚定到IMS域进行处理，即可使用IMS业务。 默认值：无。 说明：如果选择“TCSI”，则必须签约T-CSI模板。                                                                                                                                               |
| SUBID         | SUBID              | 用于标识需要增加的IMS用户的SUBID。该参数的配置原则为：新增的SUBID不能与已有的相同，操作员可以登录“IMS-HSS业务管理”窗口，使用LST HSUB命令查询相关数据记录。 取值范围：1～127位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。                                                                                                                                                                                                                                             |
| IMPI          | IMPI               | 用于标识用户的IMPI值。 取值范围：1～127位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。 说明：输入的IMPI值应符合NAI格式，字母区分大小写。输入的IMPI未增加过鉴权信息，为新增的IMPI记录。                                                                                                                                                                                                                                                                    |
| IMPI2         | IMPI2              | 用于标识用户的第二个IMPI值。 取值范围：1～127位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。 说明：输入的IMPI2值应符合NAI格式，字母区分大小写。输入的IMPI2未增加过鉴权信息，为新增的IMPI记录。                                                                                                                                                                                                                                                               |
| IMPI2AUTHTYPE | IMPI2的鉴权类型         | 用于标识与签约用户关联的第二个IMPI的鉴权类型。 取值范围：HDA（HTTP Digest）：表示鉴权类型为HTTP Digest鉴权。EAA（Early AKA）：表示鉴权类型为Early AKA鉴权。TAA（Trusted Access）：表示鉴权类型为Trusted Access鉴权。SDA（SIP Digest）：表示鉴权类型为SIP Digest鉴权。 默认值：无。 说明： 当参数“IMPI2”存在时，该参数为必选参数。当该参数取值为“EAA（Early AKA）”时，必须设置SET HSYSTEMPARA命令中的参数“是否支持EAA鉴权下多个IMPI共享IMSI”为“TRUE”，否则执行失败，上报“900001009 参数冲突”错误。                                                  |
| HUSERNAME2    | 用户名称2              | 用于标识一个用户名。该参数的配置原则为： 用户名必须唯一。 取值范围：1～127位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。 说明：当参数“IMPI2的鉴权类型”为“HDA”或者“SDA”时，该参数有效。                                                                                                                                                                                                                                                                    |
| PWD2          | 密码2                | 用于标识一个用户密码。 取值范围：长度不超过128的字符串。 “密码2”参数支持输入的字符串类型由SET HSECPOLICY命令的“密码字符集”参数控制，默认支持输入大写字母、小写字母、数字。运营商设置支持输入特殊字符且输入的特殊字符中包含“;”、“,”时，则需要在特殊字符前添加转义字符“\”。例如参数输入“\;”，输出为“;”。 默认值：无。 说明：当参数“IMPI2的鉴权类型”为“HDA”或者“SDA”时，该参数有效。为提升系统的安全性，该参数在输入值时请参考已配置的密码强度检查策略。UDM在操作人员输入密码时会按照已配置的密码强度检查策略进行检查，若此参数的设置不符合检查策略，则会提示错误信息。密码强度检查策略可通过SET HSECPOLICY命令配置，通过LST HSECPOLICY命令查询，检查策略具体流程可参考密码强度检查流程图。 |
| REALM2        | 域名2                | 用于标识一个域名。 取值范围：由1～46位字母、数字、“-”和“.”组成的字符串。 默认值：无。 说明：当参数“IMPI2的鉴权类型”为“SDA”时，该参数为必选参数。该参数仅在域名后缀为“.3gppnetwork.org”（不区分大小写）的情况下支持32～46位域名输入，其他域名格式只支持到31位。当支持32～46位格式时由于域名后缀匹配不区分大小写，在使用相关查询命令查询时，域名后缀显示结果均按小写显示。例如输入“域名”参数为“SOFT300.IMS.mnc001.mcc001.3gPPNETwork.org”时，查询结果为“SOFT300.IMS.mnc001.mcc001.3gppnetwork.org”。                                                                   |
| HA12          | HA1值2              | 用于标识一个HA1值。 取值范围：长度等于32的16进制数字组成的字符串，字母不区分大小写。 默认值：无。 说明：当参数“IMPI2的鉴权类型”为“HDA”或“SDA”时，该参数有效。                                                                                                                                                                                                                                                                                              |
| IMPULIST      | IMPU列表             | 用于标识要添加的IMPU的值。该参数的配置原则为： 由1到10个IMPU以“&”连接组成（例如："sip:impuinfo1@huawei.com"&"sip:impuinfo2@huawei.com"，在字符"前需要添加转义字符\）。输入的IMPU值应符合SIP URI或TEL URI格式，字母区分大小写。 取值范围：1～1300位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。 说明：输入的IMPU为非通配型。当参数“IMPI2”存在时，IMPU将被设置为共享属性。                                                                                                                                |
| BARIMPULIST   | 闭锁的IMPU列表          | 用于标识要闭锁的IMPU的值。该参数的配置原则为： 由1到10个IMPU以“&”连接组成（例如："sip:impuinfo1@huawei.com"&"sip:impuinfo2@huawei.com"，在字符"前需要添加转义字符\）。输入的IMPU值应符合SIP URI或TEL URI格式，字母区分大小写。 取值范围：1～1300位由数字、字母或“.”、“_”、“—”等特殊字符组成的字符串。 默认值：无。 说明：输入的IMPU为非通配型，包含在“IMPU列表”中。并且被闭锁的IMPU不能为默认IMPU。                                                                                                                           |
| CONSFLG       | 一致性标识              | 用于标识一个IMS签约用户是否需要保持CS与IMS业务数据一致性。 取值范围：TRUE（True）：表示该用户需要保持CS与IMS业务数据一致性。FALSE（False）：表示该用户不需要保持CS与IMS业务数据一致性。 默认值：无。                                                                                                                                                                                                                                                                     |
| CHARGTPLID    | 计费模板ID             | 用于标识新增IMPI的计费地址模板，该模板需要登录“IMS-HSS业务管理”窗口，通过命令ADD HCHGTPL定义，才能在此处索引。 取值范围：0～254 默认值：无。 配置原则：ADD HCHGTPL命令中“计费地址模板ID”参数取值范围为0~1024，本参数仅支持引用0~254，超过该范围取值，系统上报“900003243：计费地址模板ID不存在”错误提示。                                                                                                                                                                                                   |
| IMPUTPLID     | IMPU基本信息模板ID       | 用于标识新增IMPU的IMPU基本信息模板，该模板需要登录“IMS-HSS业务管理”窗口，通过命令ADD HIMPUTPL定义，才能在此处索引。 取值范围：0～254 默认值：无。                                                                                                                                                                                                                                                                                                |
| SPTPLID       | ServiceProfile模板ID | 用于标识新增IMPU的Service Profile模板，该模板需要登录“IMS-HSS业务管理”窗口，通过命令ADD HSPTPL定义，才能在此处索引。 取值范围：0～254 默认值：无。 配置原则：ADD HSPTPL命令中“Service Profile模板ID”参数取值范围为0~1024，本参数仅支持引用0~254，超过该范围取值，系统上报“900003240：SP模板ID不存在”错误提示。                                                                                                                                                                                 |
| IRSID         | 隐式注册集ID            | 用于标识一个隐式注册集ID，将“IMPU列表”中的所有IMPU划为一个隐式注册集。 取值范围：0～255 默认值：无。 说明：当输入值为0时表示不设置隐式注册集。当输入值大于0时，“IMPU列表”中的IMPU个数必须大于1，第一个IMPU将被设置为默认IMPU。                                                                                                                                                                                                                                                       |
| ALIASID       | IMPU别名组ID          | 用于标识一个别名组IMPUID，将“IMPU列表”中的所有IMPU划为一个别名IMPU组。 取值范围：0～255 默认值：无。 说明：当输入值为0时表示不设置别名组。当输入值大于0时，IRSID必须存在且值大于0。                                                                                                                                                                                                                                                                               |
| CAPTPLID      | 能力集模板ID            | 用于标识新增用户的能力集模板，该模板需要登录“IMS-HSS业务管理”窗口，通过命令ADD HCAPTPL定义，才能在此处索引。 取值范围：0～254 默认值：无。 配置原则：ADD HCAPTPL命令中“能力集模板ID”参数取值范围为0~1024，本参数仅支持引用0~254，超过该范围取值，系统上报“900003239：能力集模板ID不存在”错误提示。                                                                                                                                                                                                        |
| INGROUPID     | 内部组ID              | 可选必选说明：可选参数 参数含义：用于标识移动网络内部设备之间通信时互相传递的组ID。该参数必须由ADD VNGROUP命令定义后才能在此处引用。 取值范围：10～38个十进制数字、十六进制数字或“-”组成的字符串。 默认值：无。 配置原则：该参数与“外部组ID”两个参数只能输入其中一个。该参数输入的字母不区分大小写。                                                                                                                                                                                                                          |
| EXTGROUPID    | 外部组ID              | 可选必选说明：可选参数 参数含义：用于标识移动网络对外能力开放接口中提供的组ID。该参数必须由ADD VNGROUP命令定义后才能在此处引用。 取值范围：3～128个字母、十进制数字、“@”、“.”、“-”或“_”组成的字符串。 默认值：无。 配置原则：该参数与“内部组ID”两个参数只能输入其中一个。该参数输入的字母不区分大小写。                                                                                                                                                                                                                    |

## 使用实例

1. 为GSM/UMTS/EPS/IMS/5G融合用户开户，参数取值如下：

   - HLRSN：1
   - IMSI：460000009123456
   - MSISDN：8613484929766
   - 开户模板ID：2
   - SUBID：subinfo
   - IMPI：impiinfo
   - IMPULIST：\"sip:impuinfo\_1@huawei.com\"&\"sip:impuinfo\_2@huawei.com\"
   - 隐式注册集ID：1
   - IMPU别名组ID：1

   执行命令如下：

   ```
   ADD TPLUSCSUB: HLRSN=1, IMSI="460000009123456", ISDN="8613484929766", TPLID=2, SUBID="subinfo", IMPI="impiinfo", IMPULIST="\"sip:impuinfo_1@huawei.com\"&\"sip:impuinfo_2@huawei.com\"", IRSID=1, ALIASID=1;
   ```
2. 为GSM/UMTS/EPS/IMS/5G融合用户开户，参数取值如下：

   - HLRSN：1
   - IMSI：460000009123456
   - MSISDN：8613484929766
   - 开户模板ID：200
   - 锚定标志：TRUE
   - SUBID：subinfo
   - IMPI：impiinfo
   - IMPI2：impiinfo2
   - IMPI2的鉴权类型：TAA
   - IMPU列表：\"sip:+8613484929766@huawei.com\"&\"tel:+8613484929766\"&\"sip:impuinfo\_1@huawei.com\"&\"sip:impuinfo\_2@huawei.com\"
   - 闭锁的IMPU列表：\"sip:impuinfo\_1@huawei.com\"&\"sip:impuinfo\_2@huawei.com\"
   - 一致性标识：TRUE
   - 计费模板ID：0
   - ServiceProfile模板ID：1
   - IMPU基本信息模板ID：1
   - 隐式注册集ID：1
   - IMPU别名组ID：1

   执行命令如下：

   ```
   ADD TPLUSCSUB: HLRSN=1, IMSI="460000009123456", ISDN="8613484929766", TPLID=200, ANCHOR=TRUE, SUBID="subinfo", IMPI="impiinfo", IMPI2="impiinfo2", IMPI2AUTHTYPE=TAA, IMPULIST="\"sip:+8613484929766@huawei.com\"&\"tel:+8613484929766\"&\"sip:impuinfo_1@huawei.com\"&\"sip:impuinfo_2@huawei.com\"", BARIMPULIST="\"sip:impuinfo_1@huawei.com\"&\"sip:impuinfo_2@huawei.com\"", CONSFLG=TRUE, CHARGTPLID=0, SPTPLID=1, IMPUTPLID=1, IRSID=1, ALIASID=1;
   ```
3. 为GSM/UMTS/EPS/IMS/5G融合用户开户，参数取值如下：

   - HLRSN：1
   - IMSI：460000009123456
   - MSISDN：8613484929766
   - 开户模板ID：2
   - SUBID：subinfo
   - IMPI：impiinfo
   - IMPI2：impiinfo2
   - IMPI2的鉴权类型：HDA
   - 用户名称：user\_name
   - 密码：A7Bh94
   - IMPULIST：\"sip:impuinfo\_1@huawei.com\"&\"sip:impuinfo\_2@huawei.com\"
   - 隐式注册集ID：1
   - IMPU别名组ID：1

   执行命令如下：

   ```
   ADD TPLUSCSUB: HLRSN=1, IMSI="460000009123456", ISDN="8613484929766", TPLID=2, SUBID="subinfo", IMPI="impiinfo", IMPI2="impiinfo2", IMPI2AUTHTYPE=HDA, HUSERNAME2="user_name", PWD2="*****",IMPULIST="\"sip:impuinfo_1@huawei.com\"&\"sip:impuinfo_2@huawei.com\"", IRSID=1, ALIASID=1;
   ```
4. 为GSM/UMTS/EPS/IMS/5G融合用户开户，参数取值如下：

   - HLRSN：1
   - IMSI：460000009123456
   - MSISDN：8613484929766
   - 开户模板ID：2
   - SUBID：subinfo
   - IMPI：impiinfo
   - IMPI2：impiinfo2
   - IMPI2的鉴权类型：HDA
   - HA1值2：11112222333344445555666677778888
   - IMPULIST：\"sip:impuinfo\_1@huawei.com\"&\"sip:impuinfo\_2@huawei.com\"
   - 隐式注册集ID：1
   - IMPU别名组ID：1

   执行命令如下：

   ```
   ADD TPLUSCSUB: HLRSN=1, IMSI="460000009123456", ISDN="8613484929766", TPLID=2, SUBID="subinfo", IMPI="impiinfo", IMPI2="impiinfo2", IMPI2AUTHTYPE=HDA, HA12="*****", IMPULIST="\"sip:impuinfo_1@huawei.com\"&\"sip:impuinfo_2@huawei.com\"", IRSID=1, ALIASID=1;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码       | 错误码解释                          | 原因分析                                                                                                                            | 处理建议                                                                                                                              |
|:----------|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| ERR1004   | 无效的参数值                         | 原因为下列情况中的一种：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                                                      | 根据实际情况，重新输入参数“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                        |
| ERR1010   | 参数冲突                           | 执行命令时同时输入“内部组ID”和“外部组ID”参数。                                                                                                     | “内部组ID”与“外部组ID”两个参数只能输入其中一个。                                                                                                      |
| ERR3097   | HLR序列号未定义                      | 参数“HLR序列号”输入错误，实际输入的参数“HLR序列号”未定义。                                                                                              | 根据实际情况,重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。                                                                  |
| 900001009 | 参数冲突                           | 当“IMPI2的鉴权类型”参数取值为“EAA（Early AKA）”时，SET HSYSTEMPARA命令中的参数“是否支持EAA鉴权下多个IMPI共享IMSI”未设置为“TRUE”。                                    | 当“IMPI2的鉴权类型”参数取值为“EAA（Early AKA）”时，必须设置SET HSYSTEMPARA命令中的参数“是否支持EAA鉴权下多个IMPI共享IMSI”为“TRUE”。                                     |
| 900003239 | 能力集模板ID不存在                     | “能力集模板ID”输入错误，实际输入的参数“能力集模板ID”未定义。                                                                                              | 如果输入的“能力集模板ID”确定正确，说明实际输入的参数“能力集模板ID”未定义，请先通过ADD HCAPTPL命令定义“能力集模板ID”。                                                            |
| 900003240 | SP模板ID不存在                      | 输入的Service Profile模板ID在系统中未定义。                                                                                                  | 根据实际情况，重新输入Service Profile模板ID，确保输入的Service Profile模板ID已定义。                                                                       |
| 900003489 | 密码长度不符合密码复杂度                   | 输入的密码长度小于SET HSECPOLICY命令中配置的“密码最小长度”参数取值。                                                                                      | 先执行LST HSECPOLICY命令查询已配置的密码最小长度值，然后重新输密码，确保其符合最小长度。                                                                               |
| 900003490 | 密码中不能包含用户名称                    | 输入的密码中包含了用户名称                                                                                                                   | 重新输入密码值，确保其不包含用户名称。                                                                                                               |
| 900003491 | 密码中不能包含3个或以上的顺序字符              | 输入的密码值中包含了三个或三个以上的顺序字符。                                                                                                         | 重新输入密码值，确保其不包含三个或三个以上的顺序字符。                                                                                                       |
| 900003492 | 密码中包含的字符不符合密码复杂度               | 输入的密码值中包含的字符不符合SET HSECPOLICY命令中已配置的字符集要求或相同字符连续个数限制。                                                                           | 先执行SET HSECPOLICY命令查询字符集的配置或相同字符连续个数限制，重新输入密码值，确保其符合要求。                                                                           |
| ERR4072   | 该用户的MSISDN在EPS的黑名单中，不能开通EPS业务  | 用户的“MSISDN”与SET BEPSLIST命令中所设置的EPS黑名单匹配，禁止开通EPS业务。                                                                              | 根据用户的“MSISDN”，通过SET BEPSLIST命令删除该条黑名单记录，然后重新执行该命令进行开户，并提供EPS业务。                                                                   |
| ERR4140   | 该HLRSN的5GS用户数量已经达到License的容量限制 | ADD HLRSN命令中配置“5GS最大用户数”的值后，当前HLRSN已有的5GS用户总数已超出系统中License的容量限制。                                                                | 请使用MOD HLRSN命令重新配置“5GS最大用户数”的值，确保修改后当前HLRSN已有的5GS用户总数在License的容量限制内或进行License扩容。                                                  |
| 900003099 | IMPI已与其它的SUB关联                 | 参数“IMPI”对应的取值已经与其它的“SUBID”关联。                                                                                                   | 请为待开户用户重新关联“IMPI”，确保其与已开户用户的IMPI不重复。可通过LST HSUB命令输入“IMPI”查询对应的“IMPI”是否已被关联。                                                       |
| 900003443 | IMPI2已与其它的SUB关联                | 参数“IMPI2”对应的取值已经与其它的“SUBID”关联。                                                                                                  | 请为待开户用户重新关联“IMPI2”，确保其与已开户用户的IMPI不重复。可通过LST HSUB命令输入“IMPI”查询对应的“IMPI2”是否已被关联。                                                     |
| 900003522 | 默认K2不存在                        | 当SET MAPCONF命令中的“是否启用随机密钥”参数为“TRUE”，本命令中的“IMPI2的鉴权类型”参数为“HDA(HTTP Digest)”或“SDA(SIP Digest)”，执行该命令时未执行SET DEFAULTK2SNO命令设置默认K2。 | 当SET MAPCONF命令中的“是否启用随机密钥”参数为“TRUE”，本命令中的“IMPI2的鉴权类型”参数为“HDA(HTTP Digest)”或“SDA(SIP Digest)”，执行该命令时需要先执行SET DEFAULTK2SNO命令设置默认K2。 |
| 900003523 | 密钥丢失                           | 当SET MAPSERV命令中的“随机密钥默认ID”参数为非0，“随机密钥默认ID”参数对应的随机密钥材料不存在或不完整。                                                                   | 联系华为技术支持处理。                                                                                                                       |
| 900003524 | 分权分域模式下不支持此命令                  | SET HSYSTEMPARA命令的“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参设置为“TRUE(TRUE)”。                                                      | 无需处理。                                                                                                                             |
| ERR4115   | 默认K2不存在                        | 执行本命令前，需设置默认K2数据。                                                                                                               | 通过SET DEFAULTK2SNO命令设置默认K2数据后，再执行本命令。                                                                                             |
| ERR4164   | 5G VN Group不存在                 | 输入的“内部组ID”或“外部组ID”对应的5G虚拟网络组数据记录不存在。                                                                                            | 根据实际情况，重新输入参数，确保输入的“内部组ID”或“外部组ID”对应的5G虚拟网络组数据记录已通过ADD VNGROUP命令增加。                                                               |
| ERR4176   | 5G LAN签约用户数已经达到License的容量限制    | 执行该命令时5G LAN签约用户数量超过License上限值。                                                                                                 | 可以根据需要重新申请License以满足功能需求，或者根据实际情况删掉不必要的数据再进行该命令的操作。                                                                               |