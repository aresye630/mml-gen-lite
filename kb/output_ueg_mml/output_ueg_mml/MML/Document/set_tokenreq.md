# 设置TOKEN请求配置（SET TOKENREQ）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

**须知** 

如果执行不当会影响业务处理，需联系华为技术支持确认后再执行。

该命令用于设置UPCF与CHF/BSF/UDR/NWDAF/HPCF对接时，UPCF作为客户端发起的Token请求配置信息。

## 注意事项

Model-D场景下不支持通过本命令控制发起Token请求功能。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                  |
|:-------|:--------|:------------------------------------------------------------------------------------------------------|
| CHF    | CHF开关   | 可选必选说明：可选参数 参数含义：用于指定UPCF对接CHF时，UPCF作为客户端是否发起Token请求的开关。 取值范围： On(On) Off(Off) 默认值：Off(Off) 配置原则：无。   |
| BSF    | BSF开关   | 可选必选说明：可选参数 参数含义：用于指定UPCF对接BSF时，UPCF作为客户端是否发起Token请求的开关。 取值范围： On(On) Off(Off) 默认值：Off(Off) 配置原则：无。   |
| UDR    | UDR开关   | 可选必选说明：可选参数 参数含义：用于指定UPCF对接UDR时，UPCF作为客户端是否发起Token请求的开关。 取值范围： On(On) Off(Off) 默认值：Off(Off) 配置原则：无。   |
| NWDAF  | NWDAF开关 | 可选必选说明：可选参数 参数含义：用于指定UPCF对接NWDAF时，UPCF作为客户端是否发起Token请求的开关。 取值范围： On(On) Off(Off) 默认值：Off(Off) 配置原则：无。 |
| HPCF   | HPCF开关  | 可选必选说明：可选参数 参数含义：用于指定UPCF对接HPCF时，UPCF作为客户端是否发起Token请求的开关。 取值范围： On(On) Off(Off) 默认值：Off(Off) 配置原则：无。  |

## 使用实例

增加一条UPCF对接CHF发起token请求配置信息，设置“CHF开关”为“On”，“BSF开关”为“Off”，“UDR开关”为“Off”，“NWDAF开关”为“Off”，“HPCF开关”为“Off”。

```
SET TOKENREQ:CHF=On,BSF=Off,UDR=Off,NWDAF=Off,HPCF=Off;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

## 参考信息

无