# 查询MSISDN（LST ISDN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的MSISDN号码：

- 如果需要查询单个用户的MSISDN号码信息，请输入“IMSI”或“MSISDN”参数。
- 如果需要查询多个连续用户的MSISDN号码信息，请输入“IMSI”（或“MSISDN”）和“用户个数”参数。
- 如果需要查询多个不连续用户的MSISDN号码信息，请输入“IMSI文件名”或“MSISDN文件名”参数。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数是互斥参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                       |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于指示系统按照哪个“IMSI号码”来查询用户的MSISDN号码。 取值范围：6～15位的十进制数字组成的字符串。                                                                                                                                  |
| ISDN        | MSISDN    | 用于指示系统按照哪个“主MSISDN号码”来查询用户的辅MSISDN号码或者用哪个“辅MSISDN号码”来查询用户的主MSISDN号码。 “主MSISDN号码”和“辅MSISDN号码”请参见多MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。                                                           |
| RECORDCOUNT | 用户个数      | 用于指示系统需要查询MSISDN的用户个数。 当需要查询连续号码的MSISDN时配置该参数，选择后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询出连续号码的多个用户的MSISDN信息。 取值范围：1～10000 说明：该参数用于查询连续号码的多个用户的MSISDN数据，当只有一个用户时，该参数不必配置。                            |
| IMSIFILE    | IMSI文件名   | 用于指示系统按照哪个“IMSIFILE批操作文件”来查询用户的MSISDN号码。 IMSI批操作文件包含多个不连续的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。   |
| ISDNFILE    | MSISDN文件名 | 用于指示系统按照哪个“MSISDN批操作文件”来查询用户的MSISDN号码。 MSISDN批操作文件包含多个不连续的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 |

## 使用实例

1. 查询“IMSI”为“460030913121001”的用户的MSISDN号码信息：

   ```
   LST ISDN: IMSI="460030913121001";
   ```

   ```
   %%LST ISDN: IMSI="460030913121001";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460030913121001
                             ISDN = 2013521
                        INDICATOR = MASTER
                      DEFAULTCALL = Telephony (TS11)
                           DSCODE = Telephony (TS11)

                             ISDN = 2013522
                        INDICATOR = AUXILIARY
                      DEFAULTCALL = General-dataCDA (BS20)
                           DSCODE = General-dataCDA (BS20)
                              ITC = Unrestricted Digital Info
                               TM = CM
                              RCR = Dual/Half Rate Channel
                             MODE = Bit Transparent Mode of Operation
                           STRUCT = UNSTR
                             COMP = FALSE
                              SAP = I.440/450
                               RA = No Rate Adaption
                            ASYNC = TRUE
                               UR = 9.6kbit/s Recommendation X.1 and V.110
                              NDB = 8 Bits
                              NSB = 1 Bit
                           PARITY = NONE
                            NICRX = FALSE
                            NICTX = FALSE
                           INTRAT = 16 KBIT/S
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
                             UL1P = Default Layer 1 Protocol
                              OMT = No Other Type
                              ACC = TCH/All  Acceptable
                             NOTC = 4TCH
                             UIMI = User Initiated Modification Not Allowed/Required/Applicable
                              CCE = TCH/F48.0 And F28.0
                               AI = Channel Coding Symmetry Preferred
                         SER_TYPE = OCMN

                             ISDN = 2013523
                        INDICATOR = AUXILIARY
                      DEFAULTCALL = General-dataCDA (BS20)
                           DSCODE = General-dataCDA (BS20)
                              ITC = Unrestricted Digital Info
                               TM = CM
                              RCR = Dual/Half Rate Channel
                             MODE = Bit Transparent Mode of Operation
                           STRUCT = UNSTR
                             COMP = FALSE
                              SAP = I.440/450
                               RA = No Rate Adaption
                            ASYNC = TRUE
                               UR = 9.6kbit/s Recommendation X.1 and V.110
                              NDB = 8 Bits
                              NSB = 1 Bit
                           PARITY = NONE
                            NICRX = FALSE
                            NICTX = FALSE
                           INTRAT = 16 KBIT/S
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
                             UL1P = Default Layer 1 Protocol
                              OMT = No Other Type
                              ACC = TCH/All  Acceptable
                             NOTC = 4TCH
                             UIMI = User Initiated Modification Not Allowed/Required/Applicable
                              CCE = TCH/F48.0 And F28.0
                               AI = Channel Coding Symmetry Preferred

                             ISDN = 2013524
                        INDICATOR = AUXILIARY
                      DEFAULTCALL = General-dataCDA (BS20)
                           DSCODE = General-dataCDA (BS20)
                              ITC = Unrestricted Digital Info
                               TM = CM
                              RCR = Dual/Half Rate Channel
                             MODE = Bit Transparent Mode of Operation
                           STRUCT = UNSTR
                             COMP = FALSE
                              SAP = I.440/450
                               RA = No Rate Adaption
                            ASYNC = TRUE
                               UR = 9.6kbit/s Recommendation X.1 and V.110
                              NDB = 8 Bits
                              NSB = 1 Bit
                           PARITY = NONE
                            NICRX = FALSE
                            NICTX = FALSE
                           INTRAT = 16 KBIT/S
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
                             UL1P = Default Layer 1 Protocol
                              OMT = No Other Type
                              ACC = TCH/All  Acceptable
                             NOTC = 4TCH
                             UIMI = User Initiated Modification Not Allowed/Required/Applicable
                              CCE = TCH/F48.0 And F28.0
                               AI = Channel Coding Symmetry Preferred

   Total count = 120

   There is together 1 report

   ---    END
   ```
2. 查询第一个“MSISDN”为“13310911001”的连续3个用户的MSISDN号码信息：

   ```
   LST ISDN: ISDN="13310911001", RECORDCOUNT=3;
   ```

   ```
   %%LST ISDN: ISDN="13310911001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：27. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lstisdn.txt”的用户的MSISDN号码信息：

   ```
   LST ISDN: ISDNFILE="lstisdn.txt";
   ```

   ```
   %%LST ISDN: ISDNFILE="lstisdn.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435484. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数含义，表1列出的是未包含在本命令参数含义中的输出项。

| 输出项名称       | 输出项解释                                                                   |
|:------------|:------------------------------------------------------------------------|
| INDICATOR   | 用于返回查询出的MSISDN号码是主号还是辅号。 主号：指开户时使用的MSISDN号码。辅号：指新增的MSISDN号码，可配置不同的业务。   |
| DEFAULTCALL | 用于返回没有携带呼叫类型参数的入呼的缺省呼叫类型。缺省值为“TS11”。具体请参见ADD SUB命令中的“缺省呼叫类型”参数。         |
| SER_TYPE    | 用于返回多号码用户辅号的业务类型，该输出项只有当SET MULTISDN命令中设置的辅号的“多MSISDN业务类型”为“OCMN”时才会显示。 |
| 其他输出项       | 请参见ADD BCALIAS命令中的参数解释。                                                 |
| 批操作ID       | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。                              |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数是互斥参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                             | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据ISDNFILE文件格式和IMSIFILE文件格式，重新确定对应的批操作文件格式。                                                                            |