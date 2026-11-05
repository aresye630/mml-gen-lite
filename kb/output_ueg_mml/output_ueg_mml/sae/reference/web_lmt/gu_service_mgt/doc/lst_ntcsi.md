# 查询非模板CSI业务(LST NTCSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户以非模板方式签约的CSI（CAMEL Subscription Information）业务：

- 若需要查询单个用户的CSI业务信息，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户的CSI业务信息，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户的CSI业务信息，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                |
|:------------|:----------|:------------------------------------|
| IMSI        | IMSI      | 用于指示系统需要查询哪个IMSI号码的用户CSI业务。         |
| ISDN        | MSISDN    | 用于指示系统需要查询哪个MSISDN号码的用户CSI业务。       |
| RECORDCOUNT | 用户个数      | 用于指示系统需要查询连续多少个用户CSI业务。             |
| IMSIFILE    | IMSI文件名   | 用于指示系统需要查询哪个IMSI批操作文件中包含的用户CSI业务。   |
| ISDNFILE    | MSISDN文件名 | 用于指示系统需要查询哪个MSISDN批操作文件中包含的用户CSI业务。 |

## 使用实例

1. 查询IMSI号码为“460000009123456”的用户的CSI业务：

   ```
   LST NTCSI: IMSI="460000009123456";
   ```

   ```
   %%LST NTCSI: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                           MSISDN = 13500001234

   OCSI DATA
                            CAMEL = PHASE3
                           OCSIDP = COLLECTINFO
                               SK = 1
                        GSMSCFADD = 11111
                      DEFAULTCALL = continueCall
                 VLR_NOTSUPPHASE1 = AllowLocationUpdateWithODBBAOC
                 VLR_NOTSUPPHASE2 = AllowLocationUpdateWithODBBAOC
                 VLR_NOTSUPPHASE3 = AllowLocationUpdateWithODBBAOC
                 VLR_NOTSUPPHASE4 = AllowLocationUpdateWithODBBAOC
                GMSC_NOTSUPPHASE1 = ReturnBAIC
                GMSC_NOTSUPPHASE2 = AllowMTCall
                GMSC_NOTSUPPHASE3 = ReturnBAIC
                GMSC_NOTSUPPHASE4 = ReturnLPT-CSI

   TCSI DATA
                            CAMEL = PHASE3
                           TCSIDP = TAA
                               SK = 1
                        GSMSCFADD = 111111
                      DEFAULTCALL = continueCall
                GMSC_NOTSUPPHASE1 = ReturnBAIC
                GMSC_NOTSUPPHASE2 = ReturnLPT-CSI
                GMSC_NOTSUPPHASE3 = ReturnLPT-CSI
                GMSC_NOTSUPPHASE4 = AllowMTCall
                          PSICONF = TRUE
                   AVAILABLE_PLMN = HPLMN

   Total count = 26

   There is together 1 report

   ---    END
   ```
2. 查询第一个MSISDN号码为“13500001234”的连续3个用户的CSI业务：

   ```
   LST NTCSI: ISDN="13500001234", RECORDCOUNT=3;
   ```

   ```
   %%LST NTCSI: ISDN="13500001234", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：7. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lstntcsi.txt”的用户的CSI业务：

   ```
   LST NTCSI: ISDNFILE="lstntcsi.txt";
   ```

   ```
   %%LST NTCSI: ISDNFILE="lstntcsi.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435464. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

请参见

**MOD NTCSI**

命令的参数说明，表1列出的是未包含在

**MOD NTCSI**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                      |
|:--------|:-------------------------------------------|
| 批操作ID   | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。 |