# 清除VOLTE用户IMS域动态信息(CLR VOLTEIMSSTATE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该操作会清除用户IMS域动态信息，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于清除VoLTE用户在EPS域相关数据中记录的IMS域的注册状态信息以及IP短消息网关地址信息，不会修改用户在IMS域的注册信息和注册状态。

## 注意事项

- 此操作会导致用户IMS域相关动态信息丢失，请谨慎操作。
- “IMSI”、“MSISDN”是条件可选参数，有且只能有一个参数出现。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                       |
|:-------|:-------|:-----------------------------------------------------------|
| IMSI   | IMSI   | 用于标识待清除IMS域动态信息用户的IMSI号码。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。    |
| ISDN   | MSISDN | 用于标识待清除IMS域动态信息用户的MSISDN号码。 取值范围：1～15位的十进制数字组成的字符串。 默认值：无。 |

## 使用实例

清除“IMSI”为“460000009123456”的VoLTE用户在IMS域的动态信息。

1. 执行**LST DYNSUB**命令查询用户的IMS注册状态信息和IP短消息网关地址信息。

   ```
   LST DYNSUB: IMSI="460000009123456", CONTENT=EPS;
   ```

   ```
   %%LST DYNSUB:IMSI = "460000009123456",CONTENT=EPS;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 8613900001234

   "Dynamic Status Information For IMS"
                UE-Register-AtIMS = TRUE

   "Short Message Dynamic Data for IP"
                             MCEF = FALSE
                             UNRI = FALSE
                             UNRR = No Reason
                         IP_SM_GW = 45656
                         URRP-MME = REACHABLE
                        URRP-SGSN = NOT_REACHABLE 

   Total count = 9

   There is together 1 report

   ---    END
   ```
2. 执行**CLR VOLTEIMSSTATE**命令清除用户的IMS注册状态信息和IP短消息网关地址信息。

   ```
   CLR VOLTEIMSSTATE: IMSI="460000009123456";
   ```

   ```
   %%CLR VOLTEIMSSTATE: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:操作成功

   There is together 1 report

   ---    END
   ```
3. 再次执行**LST DYNSUB**命令查询是否清除成功。

   ```
   LST DYNSUB: IMSI="460000009123456", CONTENT=EPS;
   ```

   ```
   %%LST DYNSUB:IMSI = "460000009123456",CONTENT=EPS;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 8613900001234

   "Dynamic Status Information For IMS"
                UE-Register-AtIMS = FALSE

   "Short Message Dynamic Data for IP"
                             MCEF = FALSE
                             UNRI = FALSE
                             UNRR = No Reason
                         URRP-MME = REACHABLE
                        URRP-SGSN = NOT_REACHABLE 

   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                            | 处理建议                                                                      |
|:--------|:--------|:--------------------------------|:--------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | “IMSI”和“MSISDN”两个参数一个都没有输入。     | 根据实际情况，重新输入参数，确保满足“IMSI”和“MSISDN”两个参数必须有且只能有一个参数出现的条件。                    |
| ERR1010 | 参数冲突    | “IMSI”和“MSISDN”两个参数同时输入。        | 根据实际情况，重新输入参数，确保满足“IMSI”和“MSISDN”两个参数必须有且只能有一个参数出现的条件。                    |
| ERR3001 | 用户未开户   | 用户输入的“IMSI”或“MSISDN”参数对应的用户未开户。 | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明该用户已销户，不需要再执行命令，否则重新输入正确的IMSI号码或MSISDN号码。 |