# 模拟发送UDR消息获取IMS用户的普通（别名）透明数据（SND HUDR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于模拟AS向目标HSS发送UDR消息，获取并存储IMS用户或PSI用户的透明数据。

## 注意事项

- 本命令仅用于割接场景，其他场景下禁止执行该命令，否则会影响用户“CS与VoLTE补充业务数据一致性”业务的正常使用。
- 本命令不支持同步用户在2G/3G和IMS网络之间的补充业务数据。
- 执行该命令前需要完成与目标HSS之间的数据对接配置。
- 本命令执行不当会导致业务中断，执行前请联系华为技术支持。
- 本命令发送的数据量大时，会导致CPU产生一定的波动，不能在话务高峰期执行。
- 执行该命令触发UDR消息，收到的UDA消息携带“User-Data”AVP中的“SERVICEDATA”参数内容为空时透明数据的处理方式由**SET HSYSTEMPARA**命令的“透明数据中SERVICEDATA参数内容为空的实现方式”参数确定。
  - “透明数据中SERVICEDATA参数内容为空的实现方式”参数取值为“DELETE”时，如果用户已签约透明数据，则删除相应业务透明数据，该次消息流程成功。如果相应业务透明数据不存在，该次消息流程也成功。
  - “透明数据中SERVICEDATA参数内容为空的实现方式”参数取值为“INSERT”时，无论用户签约或者没有签约透明数据，支持插入更新空的透明数据。

## 参数说明

| 参数标识              | 参数名称                | 参数说明                                                                                                                                                                                                                                                                  |
|:------------------|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU              | IMPU                | 用于标识获取哪个IMPU或PUSI的用户透明数据。 配置原则： 输入的IMPU或PUSI符合SIP URI或TEL URI格式，字母区分大小写。如果该参数输入IMPU，则IMPU必须先由ADD HSUB、ADD HIMPI、ADD HIMPU或ADD HTPLIMPU命令定义，然后才能在此处索引。 如果该参数输入PUSI，则PUSI必须先由ADD HPSI或ADD HTPLPUSI命令定义，然后才能在此处索引。 取值范围：长度不超过127的字符串。 默认值：无                              |
| REPTYPE           | 透明数据的类型             | 用于标识需要获取的目标HSS中存储的透明数据的类型。 取值范围：ALIASREPDATA(Aliasrepository data)：别名透明数据REPDATA(Repository data)：普通透明数据 默认值：无 说明：PSI用户仅涉及普通透明数据，不涉及别名透明数据，因此当“IMPU”参数输入的是用户的PUSI时，需要设置该参数取值为“REPDATA(Repository data)”。                                                              |
| SRVINDLIST        | ServiceIndication列表 | 用于标识IMPU或PUSI的服务标识列表。 配置原则：ServiceIndication列表以“&”连接组成，且字符"前需要添加转义字符\（例如：\"ATS_DATA1\"&\"ATS_DATA2\"）。 取值范围：长度不超过1300的字符串。 默认值：无 说明：当该参数取值不满足配置原则时，会导致发送给目标HSS的UDR消息中携带的ServiceIndication AVP值错误。                                                                     |
| DESHOST           | 目标HSS主机名            | 用于标识接收UDR消息的目标HSS主机名称。 取值范围：长度不超过127的字符串。 默认值：无                                                                                                                                                                                                                       |
| DESREALM          | 目标HSS域名             | 用于标识接收UDR消息的目标HSS主机域名。 取值范围：长度不超过127的字符串。 默认值：无                                                                                                                                                                                                                       |
| UPDATEDB          | 是否更新数据库             | 用于标识是否将目标HSS返回的UDA消息中携带的透明数据更新到数据库中。 取值范围：TRUE：更新FALSE：不更新 默认值：FALSE                                                                                                                                                                                                  |
| SUPPORTEDFEATURES | 特性支持标示              | 用于标识目标HSS返回的UDR(User Data Request)消息中是否携带Supported-Features AVP数值。 取值范围： 全部选中：选中除“全部清空”外的所有取值。全部清空：清空所有取值。NOTIF-EFF：表示支持NOTIF-EFF功能，用于支持AS（Application Server）通过UDR消息从HSS下载多种用户数据。 默认值：无 说明：当“ServiceIndication列表”参数中有多个ServiceIndication AVP值息时，该参数需要勾选为“NOTIF-EFF”。 |

## 使用实例

1. 发送模拟UDR消息，获取如下IMS用户的透明数据：“IMPU”为“tel:+867558888”，“透明数据的类型”为“ALIASREPDATA”，“ServiceIndication列表”为“\"ATS\_DATA1\"&\"ATS\_DATA2\"”，“DESHOST”为“hss1.huawei.com”，“域名”为“huawei.com”，“是否更新数据库”为“FALSE”。

   `SND HUDR: IMPU="tel:+867558888", REPTYPE=ALIASREPDATA, SRVINDLIST="\"ATS_DATA1\"&\"ATS_DATA2\"", DESHOST="hss1.huawei.com", DESREALM="huawei.com", UPDATEDB=FALSE;`
2. 发送模拟UDR消息，获取如下PSI用户的透明数据：“IMPU”为“sip:+3696395276@huawei.com”，“透明数据的类型”为“REPDATA”，“ServiceIndication列表”为“\"ATS\_DATA3\"&\"ATS\_DATA4\"”“DESHOST”为“hss1.huawei.com”，“域名”为“huawei.com”，“是否更新数据库”为“FALSE”。

   `SND HUDR: IMPU="sip:+3696395276@huawei.com", REPTYPE=REPDATA, SRVINDLIST="\"ATS_DATA3\"&\"ATS_DATA4\"", DESHOST="hss1.huawei.com", DESREALM="huawei.com", UPDATEDB=FALSE;`

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释          | 原因分析                                                          | 处理建议                                                                                   |
|----------:|:---------------|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| 900001007 | 无效的参数值         | 输入的参数取值不在其取值范围内。                                              | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                       |
| 900001009 | 参数冲突           | 输入用户的PUSI的同时，“透明数据的类型”取值“ALIASREPDATA(Aliasrepository data)”。 | PSI用户仅涉及普通透明数据，不涉及别名透明数据，因此当“IMPU”参数输入的是用户的PUSI时，需要设置该参数取值为“REPDATA(Repository data)”。 |
| 900001010 | 参数重复           | 输入命令中的同一参数重复出现。                                               | 根据实际情况，删除重复的参数，确保命令中每一个参数只出现一次。                                                        |
| 900003060 | 请求消息中的IMPU不存在  | “IMPU”参数取值实际不存在，即用户对应的IMPU未定义。                                | 根据实际情况，重新输入参数，确保“IMPU”在IMS网络中已开户。可通过LST HSUB命令查询已存在的IMPU或通过LST HPSI命令查询已存在的PUSI。       |
| 900003246 | IMPU不属于别名IMPUs | 输入的用户IMPU不属于任何一个别名IMPU组。                                      | 重新输入IMPU参数，确保该参数属于该用户的一个别名IMPU组中，可通过SET HALIASPU添加该IMPU至一个已存在的别名IMPU组中。                |
|      1001 | 无效的命令          | 输入的命令名称不正确。                                                   | 重新输入正确的命令。                                                                             |