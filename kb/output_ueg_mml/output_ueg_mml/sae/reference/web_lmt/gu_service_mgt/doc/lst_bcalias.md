# 查询承载能力别名(LST BCALIAS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询指定承载能力别名对应的承载能力参数。

## 注意事项

如果ALIASNAME缺省，那么所有的承载业务别名标识将会被返回。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                     |
|:----------|:-------|:-----------------------------------------|
| HLRSN     | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。 |
| ALIASNAME | 承载能力别名 | 承载能力别名，可选参数。最大10个字符组成的字符串。               |

## 使用实例

查询承载能力别名为BC20的承载能力参数。

LST BCALIAS: HLRSN=1, ALIASNAME="BC20";

```
%%LST BCALIAS: HLRSN=1, ALIASNAME="BC20";%%
RETCODE = 0 SUCCESS0001:操作成功

                     ALIASNAME = BC20
                        DSCODE = Bearer Service Code 20
                           ITC = Unrestricted Digital Info
                            TM = CM
                           RCR = Dual Rate Support MS/Full Rate Preferred
                          MODE = Bit Transparent Mode of Operation
                        STRUCT = UNSTR
                          COMP = FALSE
                           SAP = I.440/450
                            RA = V.110, I.460/X.30 Rate Adaption
                         ASYNC = TRUE
                            UR = 9.6Kbit/s Recommendation X.1 and V.110
                           NDB = 8 Bits
                           NSB = 1 Bit
                        PARITY = NONE
                         NICRX = FALSE
                         NICTX = FALSE
                        INTRAT = 16 Kbit/s
                            MT = NONE
                            CE = Transparent
                          FNUR = 56.0 Kbit/s Recommendation X.1 & V.110
                         WAIUR = 9.6 Kbit/s
                            CS = GSM Standardized Coding
                            DM = Full Duplex
                           CFG = Point to Point
                          NIRR = No Meaning
                          ESTD = Demand
                          OITC = Restricted Digital Information
                           ORA = V.120
                        MFESDL = Multiple Frame Establishment Not Supported only Frame Supported
                           LLI = Default LLI-256 only
                          ASGN = Message Originator is "Default Assignee"
                          UL1P = Default Layer 1 Protocol
                           OMT = Not Other Modem Type Specified
                           ACC = TCH/All  Acceptable
                          NOTC = 4TCH
                          UIMI = User Initiated Modification Not Allowed/Required/Applicable
                           CCE = TCH/F48.0 And F28.0
                            AI = Channel Coding Symmetry Preferred

Total count = 39

There is together 1 report

---    END
```