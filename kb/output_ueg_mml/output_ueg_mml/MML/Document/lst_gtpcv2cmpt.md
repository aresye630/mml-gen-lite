# 查询GTP-C V2协议兼容性(LST GTPCV2CMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询GTP-C V2协议兼容性配置，相关配置可以控制UNC发送的GTPCv2消息是否携带特定信元以及定义相关信元的格式。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称                            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------|:--------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGCLS    | 消息分类                            | 可选必选说明：可选参数 参数含义：该参数用于指示消息分类。 取值范围：“PM(路径管理)”“TM(隧道管理)”“MM(移动管理)”“SV(SV接口)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MMMSGTYPE | 消息类型                            | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息分类为移动管理时的消息类型。 前提条件：当“MSGCLS”取值为“MM(移动管理)”时，该参数有效。 取值范围：“FWD_RLC_REQ(Forward Relocation Request)”“CTX_RSP(Context Response)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| FWDRLCREQ | Forward Relocation Request的信元类型 | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。 前提条件：当“MMMSGTYPE”取值为“FWD_RLC_REQ(Forward Relocation Request)”时，该参数有效。 取值范围：“SERNET(Serving Network)”：该信元标识源MME/S4 SGSN选择的服务网络。用于多HPLMN特性中将源MME/S4-SGSN选择的服务网络通知对端。“SRVCCMMCTXT(Additional MM context for SRVCC)”：源MME/S4-SGSN获取了可用的MS Classmark2，MS Classmark3 and the Supported Codec，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。“SRVCCFLG(Additional flags for SRVCC)”：源MME/S4-SGSN获取了可用的ICS Indicator信元，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。“STN-SR(Session Transfer Number for SRVCC)”：源MME/S4-SGSN获取了可用的Session Transfer Number for SRVCC，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。“C-MSISDN(Correlation MSISDN)”：源MME/S4-SGSN获取了可用的Correlation MSISDN，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。“INDICATION(Indication)”：源MME/S4-SGSN发送给目标MME/S4-SGSN的一组处理指示。用于目标MME/S4-SGSN根据标识进行处理，处理策略参见ADD GTPCV2CMPT命令的“FWDRLCREQIND”。 默认值：无 |
| CTXRSP    | Context Response的信元类型           | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Context Response时的信元类型。 前提条件：当“MMMSGTYPE”取值为“CTX_RSP(Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：“INDICATION(Indication)”：源MME/S4-SGSN发送给目标MME/S4-SGSN的一组处理指示。用于目标MME/S4-SGSN根据标识进行处理，处理策略参见ADD GTPCV2CMPT命令的“CTXRSPIND”。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SVMSGTYPE | 消息类型                            | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息分类为SV接口时的消息类型。SV接口是MME或SGSN和MSC之间用于SRVCC的接口。 前提条件：当“MSGCLS”取值为“SV(SV接口)”时，该参数有效。 数据来源：整网规划 取值范围：“PS_TO_CS_REQ(SRVCC PS to CS Request)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSTOCSREQ | SRVCC PS to CS Request的信元类型     | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为SRVCC PS to CS Request时的信元类型。 前提条件：当“SVMSGTYPE”取值为“PS_TO_CS_REQ(SRVCC PS to CS Request)”时，该参数有效。 数据来源：整网规划 取值范围：“STN-SR(Session Transfer Number for SRVCC)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TMMSGTYPE | 消息类型                            | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息分类为隧道管理时的消息类型。 前提条件：当“MSGCLS”取值为“TM(隧道管理)”时，该参数有效。 数据来源：整网规划 取值范围：“CRT_SES_REQ(Create Session Request)”“MOD_BR_REQ(Modify Bearer Request)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CRTSESREQ | Create Session Request的信元类型     | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Create Session Request时的信元类型 前提条件：该参数在“消息类型”参数配置为“Create Session Request”后生效。 数据来源：整网规划 取值范围：“INDICATION(Indication)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MODBRREQ  | Modify Bearer Request的信元类型      | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Modify Bearer Request时的信元类型 前提条件：当“TMMSGTYPE”取值为“MOD_BR_REQ(Modify Bearer Request)”时，该参数有效。 数据来源：整网规划 取值范围：“BCMOD(Bearer Contexts to be modified)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

#### 使用实例

查询GTP-C V2协议兼容性的配置：

LST GTPCV2CMPT:;

```
%%LST GTPCV2CMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                                  索引  =  1
                              消息分类  =  隧道管理
                              消息类型  =  Create Session Request
                              信元类型  =  UP Function Selection Indication Flags
                              携带方式  =  NULL
                              编码方式  =  NULL
                      Indication Bit位  =  NULL
                            F-TEID取值  =  NULL
UP Function Selection Indication Flags  =  Dual connectivity with NR
           是否支持LTE-M类型的RAT TYPE  =  不支持

(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**ADD GTPCV2CMPT**命令的参数说明。