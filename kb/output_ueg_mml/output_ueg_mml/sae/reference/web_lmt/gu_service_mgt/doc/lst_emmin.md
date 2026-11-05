# 查询EMMIN业务(LST EMMIN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户签约的MMINT(Mobility Management IN Triggering)业务信息，执行时可分为查询所有状态和查询激活或去激活状态，以下为六种情况下对应的查询场景：

- 若要查询所有状态下单个用户签约的MMINT业务信息，请输入“IMSI”或“MSISDN”参数。
- 若要查询激活或去激活状态下单个用户签约的MMINT业务信息，请输入“IMSI”或“MSISDN”和“激活状态”参数的组合。
- 若要查询所有状态下连续用户签约的MMINT业务信息，输入“IMSI”或“MSISDN”参数的同时输入“用户个数”参数。
- 若要查询激活或去激活状态下连续用户签约的MMINT业务信息，输入“IMSI”或“MSISDN”参数的同时输入“用户个数”与“激活状态”参数。

- 若要查询所有状态下不连续用户签约的MMINT业务信息，请输入参数“IMSI文件名”或“MSISDN文件名”。
- 若要查询激活或去激活状态下不连续用户签约的MMINT业务信息，输入“IMSI文件名”或“MSISDN文件名”参数同时输入“激活状态”参数。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                    |
|:------------|:----------|:--------------------------------------------------------|
| IMSI        | IMSI      | 用于指示系统按照哪个IMSI号来查询用户签约的MMINT业务信息。                       |
| ISDN        | MSISDN    | 用于指示系统按照哪个MSISDN号来查询用户签约的MMINT业务信息。                     |
| RECORDCOUNT | 用户个数      | 用于指示系统查询多少个连续用户签约的MMINT业务信息。                            |
| IMSIFILE    | IMSI文件名   | 用于指示系统按照哪个IMSI文件名来查询用户签约的MMINT业务信息。                     |
| ISDNFILE    | MSISDN文件名 | 用于指示系统按照哪个MSISDN文件名来查询用户签约的MMINT业务信息。                   |
| ACTIVE      | 激活态       | 用于指示系统按照哪个状态查询用户签约的MMINT业务信息；若不输入，则表示查询所有状态下的MMINT业务信息。 |

## 使用实例

1. 查询“IMSI”号码为“1234567”的用户签约的MMINT业务信息：

```
LST EMMIN: IMSI="1234567";
```

```
%%LST EMMIN: IMSI="1234567";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 1234567
                          ISDN = 1234567
                            DP = 12
                            SK = 12
                       SCPADDR = 1234567
                        ACTIVE = TRUE

Total count = 6

There is together 1 report

---    END
```

2. 查询第一个“MSISDN”号码为“1234567”的连续3个用户的MMINT业务信息：

```
LST EMMIN: IMSI="1234567", RECORDCOUNT=3;
```

```
%%LST EMMIN: IMSI="1234567", RECORDCOUNT=3;%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：8. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

3. 查询“MSISDN文件名”为“lstemmin.txt”的用户的MMINT业务信息：

```
LST EMMIN: ISDNFILE="lstemmin.txt";
```

```
%%LST EMMIN: ISDNFILE="lstemmin.txt";%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：9. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD EMMIN**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释      | 原因分析                                                                     | 处理建议                                                                              |
|:--------|:-----------|:-------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| ERR3001 | 用户未开户      | 输入的“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”参数对应的用户未在网络中存在。                  | 重新输入已签约用户的MMINT业务信息。                                                              |
| ERR1010 | 参数冲突       | 用户输入参数时同时输入“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”参数中的两个或多个。               | 重新输入“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”参数，保证其只存在一个。                             |
| ERR1009 | 参数丢失       | 用户没有输入“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”参数。                           | 重新输入“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”参数，保证其唯一性和存在性。                           |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                         | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。 |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                    | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                      |
| ERR1004 | 参数值无效      | 用户输入的“IMSI”或“MSISDN”或“用户个数”或“IMSI文件名”或“MSISDN文件名”或“DP点”或“业务键”的参数值超出取值范围。 | 重新输入“IMSI”或“MSISDN”或“用户个数”或“IMSI文件名”或“MSISDN文件名”或“DP点”或“业务键”取值范围内的参数值。            |