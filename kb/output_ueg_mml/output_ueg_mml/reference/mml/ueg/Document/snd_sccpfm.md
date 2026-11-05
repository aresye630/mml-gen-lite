# 发送SCCP伪消息(SND SCCPFM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令为维护类命令，用于请求系统仿真一个SCCP用户或MTP，并发送伪消息到SCCP层进行处理，以完成特定的测试项目。

该命令仅适用于测试场景，操作员可以通过该命令提供的仿真协议接口以完成某些特定的测试项目，而在其他情况下，请勿使用该命令。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                           |
|:-------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MN     | CCU模块号   | 用于指定处理SCCP协议的CCU进程的模块号。 取值范围：1~1023 默认值：无。 说明：必选参数。                                                                                                                                                                                                                                            |
| SPID   | 发送方PID   | 用于指定伪消息的发送方。该参数配置原则如下： PID TCAP：从TCAP向SCCP发送伪消息。 PID MTP：从MTP向SCCP发送伪消息。 取值范围： “PIDTCAP(PID TCAP)”“PIDMTP(PID MTP)” 默认值：“PIDMTP(PID MTP)” 说明：可选参数。                                                                                                                                             |
| MT     | 消息类型     | 用于指定来自MTP的原语类型。： 取值范围： “TI(MTP TRANSFER IND)”“PI(MTP PAUSE IND)”“RI(MTP RESUME IND)”“CI(CONGESTION IND)”“UI(MTP UPU IND)”“DS(MTP DSP STATE)” 默认值： “TI(MTP TRANSFER IND)” 说明：可选参数。                                                                                                              |
| SUP    | SCCP用户原语 | 来自SCCP用户的SCCP原语类型，该参数配置原则如下： UNIDATA REQ：向SCCP发送N_UNITDATA_REQ原语。 STATE UOS：向SCCP发送N_STATE_UOS原语。 STATE UIS：向SCCP发送N_STATE_UIS原语。 L_UNIDATA_REQ：向SCCP发送N_L_UNITDATA_REQ原语。 取值范围： “UR(UNIDATA REQ)”“SUOS(STATE UOS)”“SUIS(STATE UIS)”“LUR(L_UNIDATA_REQ)” 默认值：“UR(UNIDATA REQ)” 说明：可选参数。        |
| PM     | 参数       | 用于指定所发送的消息内容。消息的参数为十六进制格式，且必须符合MTP3协议所定义的消息格式（如最多272个八位位组并以空格分隔），且消息格式必须与SCCP和其外围模块间的接口结构一致。例如，来自MTP的MTP_TRANSFER_IND原语的格式如下所示： |---SIO---|---DPC---|---OPC---|---SLS---|---Message type---| 8比特 14/24比特 14/24比特 1字节中的4比特 8比特 针对不同的消息类型，后续的消息内容必须符合SCCP消息格式。 取值范围：长度不超过815的字符串 默认值：无。 说明：可选参数。 |

## 使用实例

发送SCCP伪消息，“CCU模块号”为“5”，“发送方PID”为“PIDTCAP”，“SCCP用户原语”为“UR”，“参数”为“c3 00 00 00 02 03 07 00 04 43 aa 00 8e 04 43 bb 00 8e”：

```
SND SCCPFM: MN=5, SPID=PIDTCAP, SUP=UR, PM="c3 00 00 00 02 03 07 00 04 43 aa 00 8e 04 43 bb 00 8e";
```

```
%%SND SCCPFM: MN=5, SPID=PIDTCAP, SUP=UR, PM="c3 00 00 00 02 03 07 00 04 43 aa 00 8e 04 43 bb 00 8e";%%   
RETCODE = 0  操作成功
---    END
```