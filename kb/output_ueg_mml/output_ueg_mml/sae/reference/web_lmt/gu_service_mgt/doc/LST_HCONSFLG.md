# 查询用户数据一致性标识(LST HCONSFLG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中查询用户数据一致性标识。

- 若需要查询指定“SUBID”用户的指定一致性标识，请输入“SUBID”。
- 若需要查询指定“IMPU”用户的所有IMPU一致性标识，请输入“IMPU”。
- 若需要同时查询用户的“SUBID”和该用户所有“IMPU”一致性标识，请输入“SUBID”或“IMPU”参数，并且“是否同时查询”参数设置为“TRUE”。

## 注意事项

“SUBID”和“IMPU”参数仅且只能输入一个。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                    |
|:---------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBID    | SUBID  | 用于指示系统需要按照哪个SUBID来查询用户的一致性标识。                                                                                                                           |
| IMPU     | IMPU   | 用于指示系统需要按照哪个IMPU来查询用户的一致性标识。                                                                                                                            |
| QUERYALL | 是否同时查询 | 用于指示系统是否同时查询“SUBID”或“IMPU”输入参数下的所有一致性标识。 取值范围： TRUE：同时显示“SUBID”和所有IMPU下一致性标识。FALSE：按“SUBID”查询时，查询指定“SUBID”用户的一致性标识。按“IMPU”查询时，查询对应用户所有IMPU一致性标识。 默认值：无。 |

## 使用实例

1. 查询指定SUBID的一致性标识，“SUBID”为“+862970119992@domain50.huawei.com”：

   ```
   LST HCONSFLG: SUBID="+862970119992@domain50.huawei.com";
   ```

   ```
   %%LST HCONSFLG: SUBID="+862970119992@domain50.huawei.com";%%
   RETCODE = 0 SUCCESS0001:操作成功

   SUBID                                                                                                                           CONSFLG
   +862970119992@domain50.huawei.com                                                                                               0

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询指定IMPU的一致性标识，“IMPU”为“sip:+862970119992@domain50.huawei.com”：

   ```
   LST HCONSFLG: IMPU="sip:+862970119992@domain50.huawei.com";
   ```

   ```
   %%LST HCONSFLG: IMPU="sip:+862970119992@domain50.huawei.com";%%
   RETCODE = 0 SUCCESS0001:操作成功

   IMPU                                                     PU-CONSFLG
   sip:+862970119995@domain50.huawei.com                    0
   sip:+862970119994@domain50.huawei.com                    0
   sip:+862970119993@domain50.huawei.com                    0
   sip:+862970119992@domain50.huawei.com                    1

   Total count = 4

   There is together 1 report

   ---    END
   ```
3. 查询SUBID和IMPU的一致性标识签约情况，“IMPU”为“sip:+862970119992@domain50.huawei.com”，“是否同时查询”选择“TRUE”：

   ```
   LST HCONSFLG: IMPU="sip:+862970119992@domain50.huawei.com", QUERYALL=TRUE;
   ```

   ```
   %%LST HCONSFLG: IMPU="sip:+862970119992@domain50.huawei.com", QUERYALL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

   SUBID                                          IMPU                                             CONSFLG             PU-CONSFLG
   +862970119992@domain50.huawei.com              sip:+862970119995@domain50.huawei.com            0                   0
   +862970119992@domain50.huawei.com              sip:+862970119994@domain50.huawei.com            0                   0
   +862970119992@domain50.huawei.com              sip:+862970119993@domain50.huawei.com            0                   0
   +862970119992@domain50.huawei.com              sip:+862970119992@domain50.huawei.com            0                   1

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**SET HCONSFLG**

命令的参数说明。表1列出的是未在

**SET HCONSFLG**

命令参数说明中说明取值对应关系的输出项。

| 输出项名称      | 输出项解释                                                                               |
|:-----------|:------------------------------------------------------------------------------------|
| CONSFLG    | 用于返回指定SUBID用户的一致性标识。 0：即FALSE，指该用户不需要保持CS与IMS业务数据一致性。1：即TRUE，指该用户需要保持CS与IMS业务数据一致性。 |
| PU-CONSFLG | 用于返回指定IMPU用户的一致性标识。 0：即FALSE，指该用户不需要保持CS与IMS业务数据一致性。1：即TRUE，指该用户需要保持CS与IMS业务数据一致性。  |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|       错误码 | 错误码解释          | 原因分析                  | 处理建议                                                      |
|----------:|:---------------|:----------------------|:----------------------------------------------------------|
| 900001009 | 参数冲突           | “SUBID”和“IMPU”参数同时输入。 | 根据实际情况，重新输入参数，确保“SUBID”和“IMPU”参数仅且只能出现一个。                 |
| 900003051 | 请求消息中的SubId不存在 | 输入的参数“SUBID”不存在。      | 根据实际情况，重新输入参数，确保参数“SUBID”已经存在。可通过LST HSUB命令查询获得。          |
| 900003060 | 请求消息中的IMPU不存在  | 输入的参数“IMPU”不存在。       | 根据实际情况，重新输入参数，确保“IMPU”在IMS网络中已开户。可通过LST HSUB命令查询已存在的IMPU。 |
|      1001 | 无效的命令          | 输入的命令名称不正确。           | 请核对输入命令名称的正确性，并重新输入正确的命令。                                 |
| 900001004 | 无效的参数名         | 输入的参数标识不正确。           | 根据实际情况，重新输入提示错误的参数标识，确保参数标识正确。                            |
| 900001007 | 无效的参数值         | 输入的参数取值不在其取值范围内。      | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                          |
| 900001010 | 参数重复           | 输入命令中的同一参数重复出现。       | 根据实际情况，重新输入命令，确保命令中每一个参数只出现一次。                            |