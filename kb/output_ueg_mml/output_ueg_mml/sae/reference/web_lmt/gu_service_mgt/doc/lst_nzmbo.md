# 以格式2查询TS和BS数据(LST NZMBO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于以格式2查询用户的TS和BS数据，当输入用户的“IMSI”或“MSISDN”号码时，系统将以特定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                                                                                                                                  |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 默认值：无。                                                                                                                    |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，为1～15位的十进制数。 默认值：无。                                                                                                                  |
| BSG    | 数据业务码  | 用于控制显示用户某一个BSG（Basic Service Group）组的信息。 取值范围： TS11：语音业务。TS21：短消息终结业务。TS22：短消息始发业务。 TS62: 自动3类传真业务。 TSD1：双线路可选业务。 BS26：承载业务BS26。 BS20：承载业务BS20。 BS30：承载业务BS30。 默认值：无。 |

## 使用实例

查询IMSI号码为“461380000000000”的用户的TS和BS数据，以特定的数据格式返回。命令如下：

```
LST NZMBO: IMSI="461380000000000";
```

```
%%LST NZMBO: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

            BASIC SERVICE DATA:
                                  
        INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461380000000000
 
                                          
        MOBILE STATION ISDN NUMBER ................. 461380000000000
        BASIC SERVICE .............................. T11,000
        SERVICE AREA OF MSISDN ..................... ALL
                                          
        MOBILE STATION ISDN NUMBER ................. 461380000000111
        BASIC SERVICE .............................. B16,000
        SERVICE AREA OF MSISDN ..................... ALL
                                          
        RCR .... RADIO CHANNEL REQUIREMENT ......... FRC
        ITC .... INFORMATION TRANSFER CAPABILITY ... AUDIO
        RA ..... RATE ADAPTATION ................... NONE
        SAP .... SIGNALLING ACCESS PROTOCOL ........ I440
        NSB .... NUMBER OF STOP BITS ............... 1
        NDB .... NUMBER OF DATA BITS ............... 8
        IR ..... INTERMEDIATE RATE ................. 16
        NICT ... NETWORK INDEPENDENT CLOCK IN TX ... N
        NICR ... NETWORK INDEPENDENT CLOCK IN RX ... N
        NPB .... PARITY ............................ NONE
        MT ..... MODEM TYPE ........................ AUTO
        CE ..... CONNECTION ELEMENT ................ BNT
        UIL2P .. USER INFORMATION LAYER 2 PROTOCOL . NAV
                                          
COMMAND EXECUTED

Total count = 26

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                     | 处理建议                                                                               |
|:--------|:--------|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。 | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                           |
| ERR1009 | 参数丢失    | “IMSI”和“MSISDN”一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”必须有且只能有一个参数出现的条件。                                  |
| ERR1010 | 参数冲突    | “IMSI”和“MSISDN”同时被输入。                                                    | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”必须有且只能有一个参数出现的条件。                                  |
| ERR3001 | 用户未开户   | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                   | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。 |