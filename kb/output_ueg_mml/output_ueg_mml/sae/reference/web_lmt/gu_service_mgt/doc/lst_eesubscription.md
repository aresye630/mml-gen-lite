# 查询NEF订阅事件记录(LST EESUBSCRIPTION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询数据库中用户的NEF监视事件：

- 若需要查询用户所有的NEF请求订阅的监视事件，请输入用户标识。
- 若需要查询用户某个NEF请求订阅的所有监视事件，请输入用户标识和“订阅ID”。
- 若需要查询用户某个NEF请求订阅的单个监视事件，请输入用户标识、“订阅ID”和“事件ID”。
- 若需要查询用户某个NEF请求订阅的某类监视事件，请输入用户标识、“订阅ID”和“事件类型”。
- 若需要查询用户所有NEF请求订阅的某类监视事件，请输入用户标识和“事件类型”。

  **说明** 

  用户标识分为以下三类：

  - 单个用户，请输入“IMSI”或“MSISDN”。
  - 多个连续用户，请输入“IMSI”与“用户个数”的组合，或者“MSISDN”与“用户个数”的组合。
  - 多个不连续用户，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。
- “用户个数”必须与“IMSI”或“MSISDN”中的一个同时存在。
- “事件ID”不能与“事件类型”同时配置。
- 输入“事件ID”时，必须同时输入“订阅ID”。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                    |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个IMSI号码的NEF监视事件。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                      |
| ISDN        | MSISDN    | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个MSISDN号码的NEF监视事件。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                    |
| RECORDCOUNT | 用户个数      | 可选必选说明：可选参数 参数含义：用于指示系统需要查询连续多少个用户的NEF监视事件。 当需要查询连续号码的多个用户的NEF监视事件时配置该参数，配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续多个用户的NEF监视事件。 取值范围：1～10000 默认值：无。 配置原则：该参数是查询连续的多个号码的NEF监视事件，当只有一个用户时，该参数不必配置。当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。                                       |
| IMSIFILE    | IMSI文件名   | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个IMSI批操作文件中包含的用户的NEF监视事件。 IMSI批操作文件包含多个不连续的需要查询NEF监视事件的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstee.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                       |
| ISDNFILE    | MSISDN文件名 | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个MSISDN批操作文件中包含的用户的NEF监视事件。 MSISDN批操作文件包含多个不连续的需要查询NEF监视事件的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstee.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                 |
| EVENTSUBID  | 订阅ID      | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个NEF配置的监视事件。 取值范围：1～16位十六进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                         |
| REFERENCEID | 事件ID      | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪个事件ID对应的NEF监视事件。 取值范围：0～4294967295 默认值：无。 配置原则：无。                                                                                                                                                                                                           |
| EVENTTYPE   | 事件类型      | 可选必选说明：可选参数 参数含义：用于指示系统需要查询哪种类型的NEF监视事件。 取值范围： LOSS_OF_CONNECTIVITYUE_REACHABILITY_FOR_DATAUE_REACHABILITY_FOR_SMSLOCATION_REPORTINGCHANGE_OF_SUPI_PEI_ASSOCIATIONROAMING_STATUSCOMMUNICATION_FAILUREAVAILABILITY_AFTER_DDN_FAILURECN_TYPE_CHANGEPDN_CONNECTIVITY_STATUS 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“IMSI”号码为“4600000000009”，“订阅ID”为“611DB13ACDF80072”，“事件ID”为“1111111111”的NEF监视事件：

   ```
   LST EESUBSCRIPTION: IMSI="4600000000009", EVENTSUBID="611DB13ACDF80072", REFERENCEID=1111111111;
   ```

   ```
   %%LST EESUBSCRIPTION: IMSI="4600000000009";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                             IMSI = 4600000000009
                             ISDN = 13596322667

                       EVENTSUBID = 611DB13ACDF80072
                      CALLBACKURI = http://172.16.202.146:8020/nudm-eenotification
                SUPPORTEDFEATURES = 0000000000123456
                      REFERENCEID = 1111111111
                       INSTANCEID = 4947a69a-f61b-4bc1-b9da-47c9c5d14b64
                        EVENTTYPE = ROAMING_STATUS
                    IMMEDIATEFLAG = FALSE
                          EVTTIME = 2021-08-19 01:17:46
                        SCPRTFLAG = FALSE
              NOTIFYCORRELATIONID = 10101309111804040045

                       EVENTSUBID = 611DB158CDF80082
                      CALLBACKURI = http://172.16.202.146:8020/nudm-eenotification
                SUPPORTEDFEATURES = 0000000000123456
                      REFERENCEID = 1111111111
                       INSTANCEID = 4947a69a-f61b-4bc1-b9da-47c9c5d14b64
                        EVENTTYPE = ROAMING_STATUS
                    IMMEDIATEFLAG = FALSE
                          EVTTIME = 2021-08-19 01:18:16
                        SCPRTFLAG = FALSE
              NOTIFYCORRELATIONID = 10101309111804040047

   Total count = 22

   There is together 1 report

   ---    END
   ```
2. 查询3个连续号码的用户的“订阅ID”为“5F871A4E2D540027”的NEF监视事件，这3个MSISDN号码分别为“86123110601929”、“86123110601930”、“86123110601931”：

   ```
   LST EESUBSCRIPTION: ISDN="86123110601929", RECORDCOUNT=3, EVENTSUBID="5F871A4E2D540027";
   ```

   ```
   %%LST EESUBSCRIPTION: ISDN="86123110601929", RECORDCOUNT=3, EVENTSUBID="5F871A4E2D540027";%%
   RETCODE = 0 SUCCESS0001:Operation is successful Batch ID: 15. CHK BATSTAT can be used to obtain the status of batch operation

   There is together 1 report

   ---    END
   ```
3. 查询3个非连续号码的用户的“事件类型”为“UE\_REACHABILITY\_FOR\_DATA”的NEF监视事件，这3个MSISDN号码分别为“86123110601921”、“86123110601923”、“86123110601925”，已保存在“MSISDN文件名”为“lstee.txt”的文件中：

   ```
   LST EESUBSCRIPTION: ISDNFILE="lstee.txt", EVENTTYPE=UE_REACHABILITY_FOR_DATA;
   ```

   ```
   %%LST EESUBSCRIPTION: ISDNFILE="lstee.txt", EVENTTYPE=UE_REACHABILITY_FOR_DATA;%%
   RETCODE = 0 SUCCESS0001:Operation is successful Batch ID: 16. CHK BATSTAT can be used to obtain the status of batch operation

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**LST EESUBSCRIPTION**

命令的参数说明，表1列出的是未包含在

**LST EESUBSCRIPTION**

命令参数说明中的输出项。

| 输出项名称                          | 输出项解释                                                                                                                                                      |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 批操作ID                          | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。                                                                                                                 |
| NFSUBID                        | UDM向对端网元订阅时由对端网元生成的订阅ID。                                                                                                                                   |
| CALLBACKURI                    | UDM向订阅的对端网元发送数据变更通知时使用的URI路径。                                                                                                                              |
| MAXNUMOFREPORTS                | 监视事件的最大上报次数。                                                                                                                                               |
| EXPIRY                         | 监视事件的失效时间。                                                                                                                                                 |
| SUPPORTEDFEATURES              | UDM向对端网元订阅时，对端网元支持的特性能力标识。                                                                                                                                 |
| INSTANCEID                     | NEF的实例ID。                                                                                                                                                  |
| IMMEDIATEFLAG                  | 监视事件配置后是否立即上报事件信息。 FALSE：不立即响应TRUE：立即响应                                                                                                                    |
| CURRENTLOCATION                | LOCATION_REPORTING事件上报时是否寻呼UE并返回UE的位置信息。 FALSE：不寻呼，返回UE的最近的可用位置。TRUE：寻呼并返回UE的最新位置。                                                                         |
| ONETIME                        | LOCATION_REPORTING事件的参数，表示监视事件的上报类型。 FALSE：一次性上报事件。TRUE：连续上报事件。                                                                                            |
| ACCURACY                       | LOCATION_REPORTING事件配置的3GPP位置信息上报精度。 CELL_LEVEL：上报cell粒度的位置。TA_LEVEL：上报TA粒度的位置。                                                                            |
| N3GPPACCURACY                  | LOCATION_REPORTING事件配置的非3GPP位置信息上报精度。 CELL_LEVEL：上报cell粒度的位置。TA_LEVEL：上报TA粒度的位置。                                                                           |
| ASSOCIATIONTYPE                | CHANGE_OF_SUPI_PEI_ASSOCIATION事件的上报条件。 IMEI_CHANGE：IMEI改变时上报事件，仅SV变化时不上报。IMEISV_CHANGE：IMEI、SV或两者都变化时上报事件。                                                 |
| DNN                            | 下列事件的参数，表示数据网名称。AVAILABILITY_AFTER_DDN_FAILUREPDN_CONNECTIVITY_STATUS                                                                                      |
| SNSSAI                         | AVAILABILITY_AFTER_DDN_FAILURE事件的参数，表示网络切片选择辅助信息。                                                                                                          |
| MAXDETECTIONTIME               | LOSS_OF_CONNECTIVITY事件配置的最大检测时间。                                                                                                                           |
| MAXLATENCY                     | UE_REACHABILITY_FOR_DATA事件配置的最大延迟时长。                                                                                                                       |
| MAXRESPONSETIME                | UE_REACHABILITY_FOR_DATA事件配置的最大响应时长。                                                                                                                       |
| SUGGESTEDPACKETNUMDI           | UE_REACHABILITY_FOR_DATA事件配置的下行报文建议数。                                                                                                                      |
| EVTTIME                        | 监视事件的登记时间或者最近修改时间。                                                                                                                                         |
| SCPRTFLAG                      | SCP路由标识，用于指示系统标识用户订阅请求消息是否经过SCP路由，默认为未经过SCP路由。 TRUE：表示经过SCP路由。FALSE：表示未经过SCP路由。 说明：该参数不支持通过营帐系统查询。                                                         |
| SMFSUBID1~SMFSUBID10           | PDN_CONNECTIVITY_STATUS事件的参数，表示UDM向SMF订阅时由SMF生成的订阅ID。该输出项最多有10个，表示PDN_CONNECTIVITY_STATUS事件可被最多10个SMF订阅。                                                   |
| SMFINSTANCEID1~SMFINSTANCEID10 | PDN_CONNECTIVITY_STATUS事件的参数，表示SMF实例ID。该输出项最多有10个，表示PDN_CONNECTIVITY_STATUS事件可被最多10个SMF订阅。                                                                 |
| ReachForDataConfig             | UE_REACHABILITY_FOR_DATA事件的参数，表示UE数据可达性事件的配置。 DIRECT_REPORT：表示在AMF中检测到UE可达，由AMF上报事件。INDIRECT_REPORT：表示在AMF和UDM中检测到UE可达，由UDM上报事件。                           |
| MININTERVAL                    | UE_REACHABILITY_FOR_DATA事件的参数，表示报告事件的最小时间间隔。                                                                                                               |
| ReachForSmsConfig              | UE_REACHABILITY_FOR_SMS事件的参数，表示UE短消息可达性事件的配置。 REACHABILITY_FOR_SMS_OVER_NAS：表示在UE可通过注册的SMSF访问SMS时上报事件。REACHABILITY_FOR_SMS_OVER_IP：表示在UE可通过IP进行SMS访问时上报事件。 |
| NOTIFYCORRELATIONID            | 表示NF服务消费者在订阅中呈现的通知关联ID。                                                                                                                                    |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                                                  | 处理建议                                                                                                                                        |
|:--------|:-----------|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                                              | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                                    |
| ERR1009 | 参数丢失       | 可能原因为如下之一： “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。输入“事件ID”时，没有输入“订阅ID”。                                     | 根据实际情况，重新输入参数，确保满足以下要求： “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。输入“事件ID”时，必须同时输入“订阅ID”。                                   |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                                      | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                                          |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。“事件ID”与“事件类型”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下要求：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。“事件ID”不能与“事件类型”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                                          |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                                 | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                                                |