# 查询SOAP报文格式(LST SOAPFORMAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UDM发送给业务发放系统的通知消息里SOAP报文格式的配置信息。

- 若需要查询全部的SOAP报文格式配置信息，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某条通知消息对应的SOAP报文格式配置信息，请同时输入“HLR序列号”和“消息类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                   |
|:--------|:-------|:-------------------------------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询SOAP报文格式的配置信息。                      |
| MSGTYPE | 消息类型   | 用于标识系统按照哪个消息类型来查询SOAP报文格式配置信息；若不输入，则表示所有的SOAP报文格式配置信息。 |

## 使用实例

1. 查询“HLR序列号”为“1”的所有SOAP报文格式配置信息：

   ```
   LST SOAPFORMAT: HLRSN=1;
   ```

   ```
   %%LST SOAPFORMAT: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

         "MSGNAME"                                                    "MSGTYPE"
         autoprovision                                                AUTOPRV
         outroamnotify                                                OUTROAM
         inroamnotify                                                 INROAM

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“消息类型”为“AUTOPRV”的SOAP报文格式配置信息：

   ```
   LST SOAPFORMAT: HLRSN=1, MSGTYPE=AUTOPRV;
   ```

   ```
   %%LST SOAPFORMAT: HLRSN=1, MSGTYPE=AUTOPRV;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                          MSGNAME = autoprovision
                          MSGTYPE = AUTOPRV
                       REQMSGDATA = <?xml version='1.0' ?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:lte="http://xmlns.du.ae/EAI/LTE_EAI_REQUEST"><soapenv:Header/><soapenv:Body><REQUEST><lte:Header><lte:Trans><lte:serviceName>broadcast</lte:serviceName><lte:msgId>%msgId%</lte:msgId><lte:connId>321</lte:connId></lte:Trans></lte:Header><lte:Body><lte:trigger><lte:object><lte:IMSI>%IMSI%</lte:IMSI><lte:MSISDN>%MSISDN%</lte:MSISDN></lte:object></lte:trigger></lte:Body></REQUEST></soapenv:Body></soapenv:Envelope>
                        RESMSGKEY = <lte:ResultCode>0</lte:ResultCode>
                        RESRESULT = SUCCESS

   Total count = 6

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”，“消息类型”为“OUTROAM”的SOAP报文格式配置信息：

   ```
   LST SOAPFORMAT: HLRSN=1, MSGTYPE=OUTROAM;
   ```

   ```
   %%LST SOAPFORMAT: HLRSN=1, MSGTYPE=OUTROAM;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                          MSGNAME = outroamnotify
                          MSGTYPE = OUTROAM
                       REQMSGDATA = <?xml version='1.0' ?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hss="www.xxxx.com/HSS/"><soapenv:Header><hss:Trans><hss:serviceName>broadcast</hss:serviceName><hss:msgId>2678</hss:msgId><hss:connId>0001</hss:connId></hss:Trans></soapenv:Header><soapenv:Body><hss:trigger><hss:object CmdName="AutoProvision"><hss:HLRSN>117</hss:HLRSN><hss:IMSI>460456301090001</hss:IMSI><hss:MSISDN>86456301090001</hss:MSISDN><hss:ProvisionType>10</hss:ProvisionType></hss:object></hss:trigger></soapenv:Body></soapenv:Envelope>
                        RESRESULT = SUCCESS

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                      | 处理建议                                                         |
|:--------|:--------|:----------------------------------------------------------|:-------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因为如下之一：“HLR序列号”未定义。 “HLR序列号”和“消息类型”对应的SOAP报文格式配置信息不存在。 | 根据实际情况，重新输入已定义的“HLR序列号”或“消息类型”，可通过LST HLRSN命令查询已定义的“HLR序列号”。 |