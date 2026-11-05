# 查询IMSI和ISDN绑定关系(LST IMSIISDN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户签约的辅IMSI和辅ISDN的绑定关系：

- 若需要查询单个用户签约的辅IMSI和辅ISDN的绑定关系，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户签约的辅IMSI和辅ISDN的绑定关系，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户签约的辅IMSI和辅ISDN的绑定关系，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                 |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于指示系统按照哪个IMSI号来查询用户签约的辅IMSI和辅ISDN的绑定关系。                                                                                                                                             |
| ISDN        | MSISDN    | 用于指示系统按照哪个MSISDN号来查询用户签约的辅IMSI和辅ISDN的绑定关系。                                                                                                                                           |
| RECORDCOUNT | 用户个数      | 用于标识查询用户签约的辅IMSI和辅ISDN的绑定关系的用户数目。 取值范围：1～10000 默认值：无。                                                                                                                                |
| IMSIFILE    | IMSI文件名   | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstimsiisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSI文件格式。 取值范围：1～16位由数字、字母或特殊字符等组成的字符串。 默认值：无。         |
| ISDNFILE    | MSISDN文件名 | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstimsiisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见MSISDN文件格式。 取值范围：1～16位由数字、字母或特殊字符等组成的字符串。 默认值：无。 |

## 使用实例

1. 查询“IMSI”号码为“45000000”的用户的辅IMSI和辅ISDN的绑定关系信息：

```
LST IMSIISDN: IMSI="45000000";
```

```
%%LST IMSIISDN: IMSI="45000000";%%
RETCODE = 0 SUCCESS0001:操作成功

         IMSI  =  45000000
         ISDN  =  2014521

"Auxilary IMSI"  "Band MSISDN"
45000001         2013522
45000002         2013523

Total count = 4

There is together 1 report

---    END
```

2. 查询第一个“MSISDN”号码为“2014521”的连续3个用户的辅IMSI和辅ISDN的绑定关系信息：

```
LST IMSIISDN: ISDN="2014521", RECORDCOUNT=3;
```

```
%%LST IMSIISDN: ISDN="2014521", RECORDCOUNT=3;%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：4. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

3. 查询“MSISDN文件名”为“lstimsiisdn.txt”的用户的辅IMSI和辅ISDN的绑定关系：

```
LST IMSIISDN: ISDNFILE="lstimsiisdn.txt";
```

```
%%LST IMSIISDN: ISDNFILE="lstimsiisdn.txt";%%
RETCODE = 0 SUCCESS0001:操作成功 批操作ID：5. 使用CHK BATSTAT指令可查看此批操作的执行情况

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD IMSIISDN**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                        | 处理建议                                                 |
|:--------|:--------|:------------------------------------------------------------|:-----------------------------------------------------|
| ERR1004 | 参数值不可用  | 用户输入的“IMSI”或“MSISDN”或“用户个数”或“IMSI文件名”或“MSISDN文件名”参数不在取值范围内。 | 重新输入取值范围内的“IMSI”或“MSISDN”或“IMSI文件名”或“MSISDN文件名”的参数值。 |
| ERR3001 | 用户未开户   | 用户输入的“IMSI”或“MSISDN”参数未定义。                                  | 重新输入已定义的“IMSI”或“MSISDN”参数。                           |
| ERR1005 | 文件未找到   | 用户输入的“IMSI文件名”或“MSISDN文件名”参数对应的文件不存在。                       | 重新输入已存在的文件对应的“IMSI文件名”或“MSISDN文件名”参数。                |
| ERR3247 | 用户类型不匹配 | 用户没有签约平等卡类型多imsi业务。                                         | 可使用MOD MIMSI命令修改用户签约类型后执行此查询命令。                      |