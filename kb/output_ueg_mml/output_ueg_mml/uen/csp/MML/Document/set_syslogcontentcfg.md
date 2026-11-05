# 设置日志内容配置（SET SYSLOGCONTENTCFG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

本命令用于设置上报给第三方Syslog服务器的日志内容配置。

## 注意事项

无。

## 参数说明

| 参数标识              | 参数名称         | 参数说明                                                                                                                                                                                                                                                                                                                                   |
|:------------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOGCONTENTCFG     | Syslog报文内容配置 | 可选必选说明：必选参数。 参数含义：用于设置上报给第三方Syslog服务器的日志内容配置。 取值范围： CONTENT_APP_NAME(报文头APP-NAME)CONTENT_IP(报文头IP) 默认值：无。 配置原则：无。                                                                                                                                                                                                                      |
| LOGCONTENTAPPNAME | 报文头APP-NAME  | 可选必选说明：该参数在“Syslog报文内容配置”配置为“CONTENT_APP_NAME(报文头APP-NAME)”时为条件必选参数。 参数含义：Syslog日志报文头中APP-NAME属性的类型。 取值范围： “LOG_TYPE(日志类型)”：APP-NAME属性显示为具体的日志类型。“APP_INFO(综合应用信息)”：当日志类型为操作日志、安全日志、OS日志、OS安全日志、事件日志、系统日志时，APP-NAME属性显示为详细应用信息；当日志类型为Web日志、DB日志时，APP-NAME属性显示为“-”；当日志类型为运行日志时，APP-NAME属性不受该参数控制。 默认值：APP_INFO(综合应用信息) 配置原则：参见参考信息进行配置。 |
| LOGCONTENTIPTYPE  | 报文头IP        | 可选必选说明：该参数在“Syslog报文内容配置”配置为“CONTENT_IP(报文头IP)”时为条件必选参数。 参数含义：Syslog日志报文头中IP属性的类型。 取值范围： “NONE(-)”：IP属性显示为“-”。“VIRTUAL_IP(网元浮动IP)”：IP属性显示为网元浮动IP地址。 默认值：VIRTUAL_IP(网元浮动IP) 配置原则：参见参考信息进行配置。                                                                                                                                            |

## 使用实例

```
%%SET SYSLOGCONTENTCFG: LOGCONTENTCFG=CONTENT_IP, LOGCONTENTIPTYPE=VIRTUAL_IP;%%
RETCODE = 0  操作成功

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见的错误码如表1所示。

|    错误码 | 错误码解释   | 原因分析     | 处理建议          |
|-------:|:--------|:---------|:--------------|
| 101100 | 请求参数不合法 | 请求参数不合法。 | 请检查输入参数并重新输入。 |
| 101108 | 系统内部错误  | 系统内部错误。  | 请联系华为技术支持。    |

## 参考信息

日志内容示例。

- 当使用该命令配置“报文头APP-NAME”为“LOG\_TYPE(日志类型)”，“报文头IP”为“VIRTUAL\_IP(网元浮动IP)”时，Syslog操作日志内容显示如下：

  `498 <14>1 2024-04-28T03:48:23.858Z xxx.xxx.xxx.xxx OperationLog - - - OperationLog%%{***}`

  其中*“xxx.xxx.xxx.xxx”*通过“报文头IP”进行控制，“OperationLog”通过“报文头APP-NAME”进行控制。

- 当使用该命令配置“报文头APP-NAME”为“APP\_INFO(综合应用信息)”，“报文头IP”为“NONE(-)”时，Syslog操作日志内容显示如下：

  `583 <14>1 2024-04-26T22:03:38.086Z - {"LogId":"OperationLog_Q26496","logType":"OperationLog","meId":"0","neType":"CSP","reportIdIpv4":"xxx.xxx.xxx.xxx","reportIdIpv6":""} - - - OperationLog%%{***}`

  其中“-”通过“报文头IP”进行控制，“{"LogId":"OperationLog\_Q26496","logType":"OperationLog","meId":"0","neType":"CSP","reportIdIpv4":"xxx.xxx.xxx.xxx","reportIdIpv6":""}”通过“报文头APP-NAME”进行控制。