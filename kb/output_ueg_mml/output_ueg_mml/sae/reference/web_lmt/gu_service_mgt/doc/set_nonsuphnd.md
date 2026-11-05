# 设置系统不支持业务的替代功能(SET NONSUPHND)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成用户漫游到不支持某些业务的端局时业务完全失效，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于设置系统不支持业务的替代功能，当用户漫游所在的MSC/VLR/MME/S4SGSN不支持用户所签约的ODB、CUG、IST、DIC、ZC和EPC\_ZC业务时，系统使用该MSC/VLR/MME/S4SGSN所支持的业务替代上述业务。

## 注意事项

该命令不允许进行批操作。

## 参数说明

| 参数标识       | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                     |
|:-----------|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN      | HLR序列号                   | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                                                                                                                                                                                                                             |
| ODBAOC     | ODB-BAOC业务的替代处理          | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODB-BAOC业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBAOC：用补充业务BAOC（Barring of All Outgoing Calls）来替代。 系统初始设置值：RoamingRestrict                                                                      |
| ODBOIC     | ODB-BOIC业务的替代处理          | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODB-BOIC业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBOIC：用补充业务BOIC（Barring of All Outgoing International Calls）来替代。 系统初始设置值：RoamingRestrict                                                        |
| ODBOICEXHC | ODB-BOICExHC业务的替代处理      | 用于标识当用户漫游所在的MSC/VLR不支持ODB-BOICExHC业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。InducedBOICExHC：用补充业务BOIC-ExHC来替代。 系统初始设置值：RoamingRestrict                                                                                                  |
| ODBENTER   | ODB-Entertainment业务的替代处理 | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODB-Entertaiment业务时，HLR的处理方式。 取值范围： RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。NoProcess：不用其它补充业务来替代。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：NoProcess                                                                                                   |
| ODBINFO    | ODB-Information业务的替代处理   | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODB-Information业务时，HLR的处理方式。 取值范围： RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。NoProcess：不用其它补充业务来替代。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：NoProcess                                                                                                    |
| ODBSS      | ODB-SS业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODB-SS业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。 系统初始设置值：NoProcess                                                                                                                                      |
| ODBECT     | ODBECT业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ODBECT业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：NoProcess                                                                                                             |
| ODBDECT    | ODBDECT业务的替代处理           | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持呼入和呼出业务均由被服务用户付费的ODBECT业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：NoProcess                                                                                            |
| ODBMECT    | ODBMECT业务的替代处理           | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持被服务用户在同一MSC/VLR或SGSN中存在已被转移的呼叫的ODBECT业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：NoProcess                                                                              |
| ODBPOS     | ODBPOS业务的替代处理            | 用于标识当用户漫游所在的SGSN/MME不支持ODB-POS业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该SGSN/MME里漫游。RoamingRestrict_in_VPLMN：仅当用户漫游所在的SGSN/MME为本国本网时，不用其它补充业务来替代；否则禁止用户在该SGSN/MME里漫游。 系统初始设置值：NoProcess 说明：本国本网指SGSN/MME相对于UDM的网络类型为LOCAL、LOCALDOMESTIC、LOCALAREA。 |
| ODBPB1     | ODBPB1业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR不支持ODBPB1业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                |
| ODBPB2     | ODBPB2业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR不支持ODBPB2业务时，HLR的处理方式。 NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                      |
| ODBPB3     | ODBPB3业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR不支持ODBPB3业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                |
| ODBPB4     | ODBPB4业务的替代处理            | 用于标识当用户漫游所在的MSC/VLR不支持ODBPB4业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                |
| CUG        | CUG业务的替代处理               | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持CUG业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。InducedBAOC：用补充业务BAOC来替代。 系统初始设置值：RoamingRestrict                                                                                                          |
| ZC         | ZC业务的替代处理                | 用于标识当用户漫游所在的MSC/VLR或SGSN不支持ZC（Zone Code）漫游限制业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR或SGSN里漫游。 系统初始设置值：RoamingRestrict                                                                                                                     |
| ISTVMSC    | MSC/VLR不支持IST的替代处理       | 用于标识当用户漫游所在的MSC/VLR不支持IST业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                   |
| ISTGMSC    | GMSC不支持IST的替代处理          | 用于标识当用户漫游所在的GMSC不支持IST业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。ODBIC：使用ODBIC替代处理。 系统初始设置值：NoProcess                                                                                                                                                                     |
| DIC_DICR   | MSC/VLR不支持DIC_DICR的替代处理  | 用于标识当用户漫游所在的MSC/VLR不支持DIC_DICR时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：RoamingRestrict                                                                                                                                          |
| DIC_DICV   | MSC/VLR不支持DIC_DICV的替代处理  | 用于标识当用户漫游所在的MSC/VLR不支持DIC_DICV时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MSC/VLR里漫游。 系统初始设置值：NoProcess                                                                                                                                                |
| EPC_ZC     | EPC_ZC业务的替代处理            | 用于标识当用户漫游所在的MME/S4SGSN不支持EPC_ZC漫游限制业务时，HLR的处理方式。 取值范围： NoProcess：不用其它补充业务来替代。RoamingRestrict：禁止用户在该MME/S4SGSN里漫游。 系统初始设置值：NoProcess                                                                                                                                      |

## 使用实例

当运营商配置全局数据时，设置系统不支持业务的替代功能，使得当用户漫游所在的MSC/VLR不支持ODB-BAOC时，采用BAOC补充业务替代，当不支持ODB-BOICExHC时，采用BOICexHC业务替代：

```
SET NONSUPHND: HLRSN=1, ODBAOC=InducedBAOC, ODBOICEXHC=InducedBOICExHC;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                      | 处理建议                                                                                                                                                                        |
|:--------|:--------|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 除参数“HLR序列号”的其他参数均未选择有效取值。 | 根据实际情况，选择要设置系统不支持业务替代功能的相应参数，确保参数取值有效。                                                                                                                                      |
| ERR3007 | 记录不存在   | HLR序列号未定义。                | 根据实际情况选择：如果需要为某个HLR序列号设置系统不支持业务的替代功能，则执行ADD HLRSN命令先定义该HLR序列号，再为该HLR序列号设置系统不支持业务的替代功能。如果需要为已定义的HLR序列号设置系统不支持业务的替代功能，则执行LST HLRSN命令先查询已定义的HLR序列号，再为已定义的HLR序列号设置系统不支持业务的替代功能。 |