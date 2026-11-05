# 设置SOAP报文格式(SET SOAPFORMAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会使发送给Provision的SOAP报文发生改变，导致Provision解析报文出错，因此执行该命令前，需要与Provision约定好请求报文格式。

该命令用于设置UDM发送给业务发放系统的通知消息里SOAP报文格式的配置信息。

## 注意事项

- 一个“HLR序列号”里的“消息类型”只能添加一种SOAP报文。
  - 若“HLR序列号”和“消息类型”中不存在SOAP报文记录，则执行该命令为新增记录，此时“请求消息内容”和“响应消息关键信息”参数必须输入，“响应消息结果”参数默认为“SUCCESS”；
  - 若“HLR序列号”和“消息类型”中已存在SOAP报文记录，则执行该命令为更新已存在的记录，此时“消息名称”、“请求消息内容”、“响应消息关键信息”和“响应消息结果”四个参数中必须输入一个参数。可通过**LST SOAPFORMAT**命令查询已存在的记录。
- 在发送通知消息时，SOAP报文中存在需要根据实际值去替换的参数，这些参数在配置时需要配置为“%xxx%”，例如“%IMSI%”。目前可支持的替换参数有“%AutoProvisioningType%”、“%HLRSN%”，“%msgId%”，“%IMSI%”，“%MSISDN%”，“%IMEI%”，“%SRVCC-Capability%”，“%sessionId%”和“%transactionId%”。

  发送自动开户通知消息时，替换规则为：
  - “%AutoProvisioningType%”：若用户是LTE到VoLTE，该参数替换为“1”；否则不携带该参数。
  - “%HLRSN%”替换为用户的HLRSN
  - “%msgId%”替换为自动机的消息ID
  - “%IMSI%”替换为用户的IMSI
  - “%MSISDN%”替换为用户的MSISDN
  - “%IMEI%”替换为用户的IMEI
  - “%SRVCC-Capability%”：若用户是VoLTE自动开户且用户具有SRVCC能力，该参数替换为“1”；否则不携带该参数。
  - “%sessionId%”使用locationID+CCU模块号+随机数生成一个唯一的值
  - “%transactionId%”替换为当前时间，格式为月日时分秒毫秒

  发送5G自动开户通知消息时，替换规则为：

  - “%HLRSN%”替换为用户的HLRSN
  - “%msgId%”替换为自动机的消息ID
  - “%IMSI%”替换为用户的IMSI
  - “%MSISDN%”替换为用户的MSISDN
  - “%ProvisionType%”该参数必选，且固定替换为“2”表示5G自动开户场景
  - “%IMEI%”替换为用户的IMEI
  - “%VOLTETAG%”：若用户是VoLTE用户，该参数替换为“1”；否则替换为“0”
  - “%sessionId%”使用locationID+微服务serviceid+随机数生成一个唯一的值
  - “%transactionId%”替换为当前时间，格式为月日时分秒毫秒

  发送用户漫游出国和漫游回国的通知消息时，替换规则为：
  - “%HLRSN%”替换为用户的HLRSN
  - “%msgId%”替换为自动机的消息ID
  - “%IMSI%”替换为用户的IMSI
  - “%MSISDN%”替换为用户的MSISDN
  - “%IMEI%”替换为用户的IMEI
- 该命令不允许进行批操作。

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-----------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN      | HLR序列号   | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                                                                                                                                                                                                                                                                                                                                                                              |
| MSGNAME    | 消息名称     | 用于标识UDM发送给业务发放系统的通知消息的名称。 取值范围：1～60位字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                |
| MSGTYPE    | 消息类型     | 用于标识UDM发送给业务发放系统的通知消息的类型。 取值范围：AUTOPRV：自动开户的通知消息。 OUTROAM：用户漫游出国的通知消息，表示用户从国内（包含国内本网和国内跨网）漫游到国际（包含国际跨网和国际本网）时下发的SOAP订阅通知消息格式。 INROAM：用户漫游回国的通知消息，表示用户从国际（包含国际跨网和国际本网）漫游回国内（包含国内本网和国内跨网）时下发的SOAP订阅通知消息格式。 5GAUTOPROV：5G自动开户的通知消息。VOLTEAUTOPROVCUS：定制的VoLTE自开通消息。 默认值：无。 说明：该参数的取值“OUTROAM”和“INROAM”需要配合命令SET MAPCONF的参数“是否支持CS域漫游状态发生变化时触发订阅通知”一起使用。仅当参数“是否支持CS域漫游状态发生变化时触发订阅通知”设置为“TRUE”时，“OUTROAM”和“INROAM”订阅通知消息的格式才生效。 |
| REQMSGDATA | 请求消息内容   | 用于标识UDM发送给业务发放系统的通知消息里SOAP报文的内容。 取值范围：由字母、十进制数字或者“/”、“.”、“"”、“'”、“//”、“?”、“=”、“<”、“>”、“-”、“:”、“_”、空格等特殊字符组成的长度不超过4096的字符串。 默认值：无。 配置约束：该参数的配置需要满足SOAP标准协议，如果输入中包含“'”、“"”和“=”这三个特殊字符，则在这些特殊字符前添加转义字符“\”。                                                                                                                                                                                                                   |
| RESMSGKEY  | 响应消息关键信息 | 用于标识UDM收到业务发放系统返回的响应消息后，在响应报文中要检索的关键信息。 取值范围：由字母、十进制数字或者“/”、“.”、“"”、“'”、“//”、“?”、“=”、“<”、“>”、“-”、“:”、“_”、空格等特殊字符组成的长度不超过1024的字符串。 默认值：无。 配置约束：该参数的配置需要满足SOAP标准协议，如果输入中包含“'”、“"”和“=”这三个特殊字符，则在这些特殊字符前添加转义字符“\”。                                                                                                                                                                                                            |
| RESRESULT  | 响应消息结果   | 用于标识当UDM收到业务发放系统返回的响应消息中含有参数“响应消息关键信息”中设置的信息时，对于该请求的处理结果是成功还是失败。 取值范围：SUCCESS：成功FAIL：失败 默认值：无。                                                                                                                                                                                                                                                                                                                            |

## 使用实例

- 增加一条自动开户通知消息的SOAP报文：“HLR序列号”为“1”，“消息名称”为“autoprovision”，“消息类型”为“AUTOPRV”，“请求消息内容”为“<?xml version\=\'1.0\' ?><soapenv:Envelope xmlns:soapenv\=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:lte\=\"http://xmlns.du.ae/EAI/LTE\_EAI\_REQUEST\"><soapenv:Header/><soapenv:Body><REQUEST><lte:Header><lte:Trans><lte:serviceName>broadcast</lte:serviceName><lte:msgId>%msgId%</lte:msgId><lte:connId>321</lte:connId></lte:Trans></lte:Header><lte:Body><lte:trigger><lte:object><lte:IMSI>%IMSI%</lte:IMSI><lte:MSISDN>%MSISDN%</lte:MSISDN></lte:object></lte:trigger></lte:Body></REQUEST></soapenv:Body></soapenv:Envelope>”，“响应消息关键信息”为“<lte:ResultCode>0</lte:ResultCode>”，“响应消息结果”为“SUCCESS”：

  ```
  SET SOAPFORMAT: HLRSN=1, MSGNAME="autoprovision", MSGTYPE=AUTOPRV, REQMSGDATA="<?xml version\=\'1.0\' ?><soapenv:Envelope xmlns:soapenv\=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:lte\=\"http://xmlns.du.ae/EAI/LTE_EAI_REQUEST\"><soapenv:Header/><soapenv:Body><REQUEST><lte:Header><lte:Trans><lte:serviceName>broadcast</lte:serviceName><lte:msgId>%msgId%</lte:msgId><lte:connId>321</lte:connId></lte:Trans></lte:Header><lte:Body><lte:trigger><lte:object><lte:IMSI>%IMSI%</lte:IMSI><lte:MSISDN>%MSISDN%</lte:MSISDN></lte:object></lte:trigger></lte:Body></REQUEST></soapenv:Body></soapenv:Envelope>", RESMSGKEY="<lte:ResultCode>0</lte:ResultCode>", RESRESULT=SUCCESS;
  ```
- 增加一条5G自动开户通知消息的SOAP报文：“HLR序列号”为“1”，“消息名称”为“autoprovision”，“消息类型”为“5GAUTOPROV”，“请求消息内容”为“<soapenv:Envelope xmlns:soapenv\=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:hss\=\"www.xxxx.com/HSS/\"><soapenv:Header><hss:Trans><hss:serviceName>broadcast</hss:serviceName><hss:msgId>%msgId%</hss:msgId><hss:connId>0001</hss:connId></hss:Trans></soapenv:Header><soapenv:Body><hss:trigger><hss:object CmdName\=\"AutoProvision\"><hss:IMSI>%IMSI%</hss:IMSI><hss:MSISDN>%MSISDN%</hss:MSISDN><hss:ProvisionType>2</hss:ProvisionType></hss:object></hss:trigger></soapenv:Body></soapenv:Envelope>”，“响应消息关键信息”为“<hss:ResultCode>0</hss:ResultCode>”，“响应消息结果”为“SUCCESS”：

  ```
  SET SOAPFORMAT: HLRSN=1, MSGNAME="autoprovision", MSGTYPE=5GAUTOPROV, REQMSGDATA="<soapenv:Envelope xmlns:soapenv\=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:hss\=\"www.xxxx.com/HSS/\"><soapenv:Header><hss:Trans><hss:serviceName>broadcast</hss:serviceName><hss:msgId>%msgId%</hss:msgId><hss:connId>0001</hss:connId></hss:Trans></soapenv:Header><soapenv:Body><hss:trigger><hss:object CmdName\=\"AutoProvision\"><hss:IMSI>%IMSI%</hss:IMSI><hss:MSISDN>%MSISDN%</hss:MSISDN><hss:ProvisionType>2</hss:ProvisionType></hss:object></hss:trigger></soapenv:Body></soapenv:Envelope>", RESMSGKEY="<hss:ResultCode>0</hss:ResultCode>", RESRESULT=SUCCESS;
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                        | 处理建议                                                                                                                       |
|:--------|:--------|:------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 可能原因为如下之一：新增SOAP报文记录时，“请求消息内容”或“响应消息关键信息”参数没有输入。修改SOAP报文记录时，“消息名称”、“请求消息内容”、“响应消息关键信息”和“响应消息结果”四个参数一个都没有输入。 | 根据实际情况，重新输入参数，确保满足以下两点：新增SOAP报文记录时，“请求消息内容”和“响应消息关键信息”参数必须输入。修改SOAP报文记录时，“消息名称”、“请求消息内容”、“响应消息关键信息”或“响应消息结果”四个参数中必须输入一个参数。 |
| ERR3007 | 记录不存在   | 输入的“HLR序列号”未定义。                                                                                             | 根据实际情况，重新输入参数，确保输入的“HLR序列号”已定义。可通过LST HLRSN命令查询已定义的HLR序列号。                                                                 |