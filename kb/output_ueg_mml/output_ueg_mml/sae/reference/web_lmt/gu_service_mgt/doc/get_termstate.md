# 查询终端状态及位置信息(GET TERMSTATE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，当批量查询终端用户信息时，会增加网络负荷，可能导致网络侧消息时延增大，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于查询终端用户的状态、位置信息、注册时间、位置更新时间及Purge状态变更时间。包括：

- 终端状态：用户在HLR或网络侧（VLR/MSC/MME/AMF）的状态信息。
- 位置信息：用户的VLR号码、小区ID、EPS位置信息、5G终端信息或MME的主机地址。
- 位置更新时间：用户位置更新时间。
- 注册时间：用户在AMF的注册时间。
- 清除时间：用户Purge状态变更时间。

该命令支持如下三种查询方式：

- 本地查询：从HLR查询终端用户信息，此时返回Purge状态或VLR号码。
- 转接查询：从VLR、MME或AMF查询终端用户信息，此时返回VLR、MME或AMF中存储的用户终端状态。
- 寻呼查询：从MSC、MME或AMF发起寻呼后获取终端最新的位置和状态信息。

  **说明** 

  - 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
  - 在从运营商网络获取数据前，必须要获得运营商的授权。
  - 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- 参数“IMSI文件名”或“MSISDN文件名”配置时，参数“消息来源”、“是否查询终端位置信息”和“是否查询终端状态信息”不能配置。
- IMSI批操作文件和MSISDN批操作文件中，“消息来源”、“是否查询终端位置信息”、“是否查询终端状态信息”三个参数只能使用1、0来分别表示TRUE、FALSE。
- 执行该命令是否返回Purge状态变更时间，由**SET MAPCONF**命令中“支持查询用户的PURGE时间”参数控制。

## 参数说明

| 参数标识       | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI       | IMSI          | 用于标识要查询哪个IMSI号码对应用户的终端状态及位置信息。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                        |
| ISDN       | MSISDN        | 用于标识要查询哪个MSISDN号码对应用户的终端状态及位置信息。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                      |
| IMSIFILE   | IMSI文件名       | 用于标识IMSI批操作文件。 IMSI批操作文件包含用户的“IMSI”、“消息来源”、“是否查询终端位置信息”和“是否查询终端状态信息”，为文本编辑器编辑的文本文件（编码格式为ANSI），如“TERMSTATE.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见GET TERMSTATE命令中的IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                                                                                                                                                 |
| ISDNFILE   | MSISDN文件名     | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含用户的“MSISDN”、“消息来源”、“是否查询终端位置信息”和“是否查询终端状态信息”，为文本编辑器编辑的文本文件（编码格式为ANSI），如“TERMSTATE.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见GET TERMSTATE命令中的ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                                                                                                                                           |
| LOCATION   | 是否查询终端位置信息    | 用于标识是否查询终端位置信息。 取值范围： TRUE：查询。FALSE：不查询。 默认值：TRUE。                                                                                                                                                                                                                                                                                                                                                  |
| STATUS     | 是否查询终端状态信息    | 用于标识是否查询终端状态信息。 取值范围： TRUE：查询FALSE：不查询 默认值：TRUE。                                                                                                                                                                                                                                                                                                                                                    |
| OnHLR      | 消息来源          | 用于标识从哪种信息来源查询用户的终端状态和位置信息。 取值范围： TRUE：查询HLR中存储的信息。FALSE：查询VLR中存储的信息。DEPVLR：查询MSC中获取的信息。MME：查询MME中存储的信息。MME_PAGE：查询MME发起寻呼后获取到的信息。ALL：查询用户在HSS/HLR存储的MSC，SGSN，MME号码、相应的位置更新时间和Purge状态变更时间信息。ALLWITHAMF：查询用户在UDM存储的VLR Number，SGSN Number，MME主机名，AMF GUAMI、相应的位置更新、注册时间和Purge状态变更时间信息。AMF：查询AMF中存储的信息。AMF_PAGE：查询AMF发起寻呼后获取到的信息。 默认值：TRUE。 说明：当该参数取值为“MME”或“MME_PAGE”时，“是否显示详细的终端状态信息”参数不允许被置为“TRUE”。 |
| DetailFLAG | 是否显示详细的终端状态信息 | 仅当本命令中的“消息来源”参数为“TRUE”，“FALSE”，“DEPVLR”时该参数有效。用于标识是否显示通过PSI消息查询到的详细状态信息。 取值范围： TRUE：返回终端详细状态信息。FALSE：不返回终端详细状态信息。 默认值：FALSE。                                                                                                                                                                                                                                                                        |

## 使用实例

1. 查询IMSI号码为“460021001008001”的终端用户的状态信息和位置信息，信息来源为HLR中存储的信息：

   ```
   GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=TRUE, DetailFLAG=FALSE;
   ```

   ```
   %%GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=TRUE, DetailFLAG=FALSE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "IMSI"             "MSISDN"           "LOCATION"        "STATUS"     "OnHLR"   "LocationTime"                    "EPSLOCATION"                     "CISDN"
   460021001008001    8621001008001                        1            1                                                                             8621001008001

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询IMSI号码为“460021001008001”的终端用户的状态信息和位置信息，信息来源为VLR中存储的信息：

   ```
   GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=FALSE, DetailFLAG=FALSE;
   ```

   ```
   %%GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=FALSE, DetailFLAG=FALSE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "IMSI"             "MSISDN"           "LOCATION"        "STATUS"     "OnHLR"   "LocationTime"                    "EPSLOCATION"                     "CISDN"
   460021001008001    8621001008001                                     0                                                                             8621001008001

   Total count = 1

   There is together 1 report

   ---    END
   ```
3. 查询IMSI号码为“460021001008001”的终端用户的状态信息和位置信息，信息来源为MME发起寻呼后获取到的信息：

   ```
   GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=MME_PAGE, DetailFLAG=FALSE;
   ```

   ```
   %%GET TERMSTATE: IMSI="460021001008001", LOCATION=TRUE, STATUS=TRUE, OnHLR=MME_PAGE, DetailFLAG=FALSE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "IMSI"             "MSISDN"           "LOCATION"        "STATUS"     "OnHLR"   "LocationTime"                    "EPSLOCATION"                     "CISDN"
   460021001008001    8621001008001                                     4                                                                             8621001008001

   Total count = 1

   There is together 1 report

   ---    END
   ```
4. 查询IMSI号码为“460000009012345”的终端用户的位置更新时间，信息来源为“ALL”：

   ```
   GET TERMSTATE: IMSI="460000009012345", LOCATION=TRUE, OnHLR=ALL, DetailFLAG=FALSE;
   ```

   ```
   %%GET TERMSTATE: IMSI="460000009012345", LOCATION=TRUE, OnHLR=ALL, DetailFLAG=FALSE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "IMSI"             "MSISDN"           "LOCATION"        "OnHLR"   "EPSLOCATION"                     "SGSNLOCATION"                    "LocationTimeMSC"                "LocationTimeSGSN"                 "LocationTimeMME"                 "PurgeTimeMSC"                "PurgeTimeSGSN"                 "PurgeTimeMME"
   460000009012345    8600009012345                        5                                                                                                                                                 

   Total count = 1

   There is together 1 report

   ---    END
   ```
5. 查询IMSI号码为“460000009012345”的终端用户的位置更新和注册时间，信息来源为“ALLWITHAMF”：

   ```
   GET TERMSTATE: IMSI="460000009012345", LOCATION=TRUE, STATUS=TRUE, OnHLR=ALLWITHAMF
   ```

   ```
   %%GET TERMSTATE: IMSI="460000009012345", LOCATION=TRUE, STATUS=TRUE, OnHLR=ALLWITHAMF;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "IMSI"             "MSISDN"           "OnHLR"   "LOCATION"        "EPSLOCATION"                              "SGSNLOCATION"                    "AMFLOCATION"                        "LocationTimeMSC"                 "LocationTimeSGSN"                 "LocationTimeMME"                 "LocationTimeAMF"                 "PurgeTimeMSC"                "PurgeTimeSGSN"                 "PurgeTimeMME"                   "PurgeTimeAMF"
   460000009012345    86111311134001     6         86819211          s00000000saehss1.huawei.com                86819221                          045012-12-d1-16                      2002281051                         2002281051                        2002281051                        2002281051                          2305160943                    2305160943                      2305160943                       2305160943

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表1所示。

| 输出项名称            | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI             | 用于返回终端用户的IMSI号码。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MSISDN           | 用于返回终端用户的MSISDN号码。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| OnHLR            | 用于返回查询信息的来源。 取值范围： 1：信息来源为HSS/HLR中存储的信息。0：信息来源为VLR中存储的信息。2：信息来源为MSC获取到的信息。3：信息来源为MME中存储的信息。4：信息来源为MME发起寻呼后获取到的信息。5：信息来源为用户在HSS/HLR存储的MSC，SGSN，MME号码、相应的位置更新时间和Purge状态变更时间信息。6：信息来源为用户在HSS存储的VLR，SGSN，MME， AMF GUAMI、相应的位置更新、注册时间信息和Purge状态变更时间信息。7：信息来源为AMF中存储的信息。8：信息来源为AMF发起的下发寻呼后获取到的信息。                                                                                                                                                                                                                                                                                                                                    |
| LOCATION         | 用于返回终端用户的位置信息。 取值范围： 当“OnHLR”取值为“1”时，“LOCATION”表示终端用户所在VLR的VLR号码。当“OnHLR”取值为“0”或“2”时，“LOCATION”表示终端用户所在的小区ID。当“OnHLR”取值为“5”或“6”时，“LOCATION”表示终端用户所在VLR的VLR号码。                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| STATUS           | 用于返回终端用户的状态信息。 取值范围： 当“OnHLR”取值为“1”时，“STATUS”表示HLR中存储的终端用户的Purge状态：1：未被Purge0：被Purge 当“OnHLR”取值为“0”时，“STATUS”表示VLR中存储的终端用户的开/关机状态：1：开机0：关机 当“OnHLR”取值为“2”时，“STATUS”表示从MSC中获取到的终端用户的开/关机状态：1：开机0：关机 当“OnHLR”取值为“3”时，“STATUS”表示MME返回给系统的终端用户的状态：0：UE与网络分离1：UE附着网络，无任何激活的EPS承载，且该UE寻呼不可达2：UE附着网络，无任何激活的EPS承载，且该UE寻呼可达3：UE附着网络，至少有一条EPS承载激活，且该UE寻呼不可达4：UE附着网络，至少有一条EPS承载激活，且该UE寻呼可达5：保留 当“OnHLR”取值为“4”时，“STATUS”表示MME发起寻呼后返回给系统的终端用户的状态：0：UE与网络分离1：UE附着网络，无任何激活的EPS承载，且该UE寻呼不可达2：UE附着网络，无任何激活的EPS承载，且该UE寻呼可达3：UE附着网络，至少有一条EPS承载激活，且该UE寻呼不可达4：UE附着网络，至少有一条EPS承载激活，且该UE寻呼可达5：保留 说明：当“OnHLR”取值为“3”或“4”时，若“STATUS”取值为“5”，系统认为该UE寻呼不可达。 |
| LocationTime     | 当“OnHLR”取值为“0”、“1”或“2”时，用于返回终端用户的位置更新时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| EPSLOCATION      | 当“OnHLR”取值为“3”或“4”时用户的EPS位置信息。 当“OnHLR”取值为“5”或“6”时，用于返回MME的主机地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CISDN            | 用于返回终端用户的M2M Common MSISDN号码。 说明：当SET MAPCONF中参数“M2M_CISDN_REPORT”设置为“TRUE”并且用户存在M2M Common MSISDN号码的情况下该参数才会显示。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SGSNLOCATION     | 当“OnHLR”取值为“5”或“6”时，用于返回SGSN号码。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LocationTimeMSC  | 当“OnHLR”取值为“5”或“6”时，用于返回用户在MSC下的位置更新时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PurgeTimeMSC     | 当“OnHLR”取值为“5”或“6”时，用于返回用户在MSC下的Purge状态变更时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LocationTimeSGSN | 当“OnHLR”取值为“5”或“6”时，用于返回用户在SGSN下的位置更新时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PurgeTimeSGSN    | 当“OnHLR”取值为“5”或“6”时，用于返回用户在SGSN下的Purge状态变更时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| LocationTimeMME  | 当“OnHLR”取值为“5”或“6”时，用于返回用户在MME下的位置更新时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PurgeTimeMME     | 当“OnHLR”取值为“5”或“6”时，用于返回用户在MME下的Purge状态变更时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RMSTATE          | 当“OnHLR”取值为“7”或“8”时，用于返回用户在AMF上的注册状态。 取值范围：REGISTERED：已注册状态DEREGISTERED：去注册状态                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CMSTATE          | 当“OnHLR”取值为“7”或“8”时，用于返回用户在AMF的连接状态。IDLE：未激活状态CONNECTED：已连接状态                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Reachability     | 当“OnHLR”取值为“7”或“8”时，用于返回用户在AMF上的可达性状态。 取值范围：UNREACHABLE：不可达REACHABLE：可达REGULATORY_ONLY：仅用于管理策略优先级服务                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| AMF LOCATION     | 当“OnHLR”取值为“6”时，用于返回AMF携带的GUAMI，格式为<MCC><MNC><AMF Region ID><AMF Set ID><AMF Pointer>组成的字符串，如46001-8-20-2，其中<AMF Region ID><AMF Set ID><AMF Pointer>为16进制的字符串。 当“OnHLR”取值为“7”或“8”时，用于返回无线小区标识（NR Cell Identity），格式为<MCC><MNC>-NrCellId组成的字符串，如46001-B0082E3D2。                                                                                                                                                                                                                                                                                                                                                                 |
| LocationTimeAMF  | 当“OnHLR”取值为“6”时，用于返回用户在AMF下的注册时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PurgeTimeAMF     | 当“OnHLR”取值为“6”时，用于返回用户在AMF下的Purge状态变更时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                                                                 | 处理建议                                                                                                                                                    |
|:--------|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                                                             | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                                                    | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                                                     | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                                                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。参数“IMSI文件名”或“MSISDN文件名”被输入时，参数“消息来源”、“是否查询终端位置信息”或“是否查询终端状态信息”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。 参数“IMSI文件名”或“MSISDN文件名”配置时，参数“消息来源”、“是否查询终端位置信息”和“是否查询终端状态信息”不能配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                               | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                                                | 请根据GET TERMSTATE命令中的IMSIFILE文件格式和GET TERMSTATE命令中的ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                          |