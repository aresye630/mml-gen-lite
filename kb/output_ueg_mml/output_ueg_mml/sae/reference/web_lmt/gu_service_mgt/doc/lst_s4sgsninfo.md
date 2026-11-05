# 查询S4SGSN地址信息(LST S4SGSNINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的S4SGSN地址信息：

- 若需要查询单个用户的S4SGSN地址信息，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户的S4SGSN地址信息，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户的S4SGSN地址信息，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                 |
|:------------|:----------|:-------------------------------------|
| IMSI        | IMSI      | 用于指定系统按照哪个IMSI号来查询用户的S4SGSN地址信息。     |
| ISDN        | MSISDN    | 用于指定系统按照哪个MSISDN号来查询用户的S4SGSN地址信息。   |
| RECORDCOUNT | 用户个数      | 用于指定系统查询多少个连续用户的S4SGSN地址信息。          |
| IMSIFILE    | IMSI文件名   | 用于指定系统按照哪个IMSI文件名来查询用户的S4SGSN地址信息。   |
| ISDNFILE    | MSISDN文件名 | 用于指定系统按照哪个MSISDN文件名来查询用户的S4SGSN地址信息。 |

## 使用实例

1. 查询“IMSI”号码为“460456304005011”用户的S4SGSN地址信息：

```
LST S4SGSNINFO: IMSI="460456304005011";
```

```
%%LST S4SGSNINFO: IMSI="460456304005011";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460456304005011
                          ISDN = 86456304005011
                    S4SGSNHOST = <NULL>
                   S4SGSNREALM = <NULL>
                       SGSNNUM = <NULL>
                  LOCATIONTIME = 1412161227

Total count = 6

There is together 1 report

---    END
```

2. 查询第一个“IMSI”号码为“460456304005011”的连续3个用户的S4SGSN地址信息：

```
LST S4SGSNINFO: IMSI="460456304005011", RECORDCOUNT=3;
```

```
%%LST S4SGSNINFO: IMSI="460456304005011", RECORDCOUNT=3;%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：2. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

3. 查询“MSISDN文件名”为“S4SGSNinfo.txt”用户的S4SGSN地址信息：

```
LST S4SGSNINFO: ISDNFILE="S4SGSNinfo.txt";
```

```
%%LST S4SGSNINFO: ISDNFILE="S4SGSNinfo.txt";%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：4. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，请参见**MOD S4SGSNINFO**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 输入的界面参数不在取值范围内。                                                                                    | 参考MOD S4SGSNINFO命令的参数说明，重新输入取值范围内的参数值。                                                                                  |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |
| ERR3001 | 用户未开户      | 用户输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                    | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明该用户已销户，不需要再执行命令，否则重新输入正确的IMSI号码或MSISDN号码。                                               |