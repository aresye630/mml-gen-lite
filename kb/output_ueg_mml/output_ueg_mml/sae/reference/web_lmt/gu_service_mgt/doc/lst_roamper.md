# 查询国家分组和运营商信息(LST ROAMPER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询国家分组和运营商信息：

- 若需要查询全部国家分组信息，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个国家分组的所有运营商信息，请输入“HLR序列号”和“分组ID”，其他参数不输入。
- 若需要查询某个运营商及其归属的分组信息，请输入“HLR序列号”和“运营商ID”或“HLR序列号”和“运营商名称”，其他参数不输入。

## 注意事项

“分组ID”、“运营商名称”和“运营商ID”三个参数同时只能输入其中一个。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                            |
|:--------|:-------|:--------------------------------------------------------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询国家分组和运营商信息，该参数必须选择。                                          |
| GRPID   | 分组ID   | 用于指示系统按照哪个分组ID来查询国家分组和运营商信息。                                                    |
| OPRID   | 运营商ID  | 用于标识查询国家分组和运营商信息的运营商ID。该参数必须先由SET ROAMPREFIX命令定义，然后才能在此处引用。 取值范围：1～65535 默认值：无。 |
| OPRNAME | 运营商名称  | 用于标识查询国家分组和运营商信息的运营商名称。 取值范围：1～60位由字母、数字和特殊字符组成的字符串。 默认值：无。                     |

## 使用实例

1. 查询全部国家分组信息，“HLRSN”为“1”：

   ```
   LST ROAMPER: HLRSN=1;
   ```

   ```
   %%LST ROAMPER: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  GRPID        GRPNAME
                  1            Group1
                  2            Group2
                  3            Group3

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询某个国家分组的所有运营商信息，“HLRSN”为“1”，“分组ID”为“1”：

   ```
   LST ROAMPER: HLRSN=1, GRPID=1;
   ```

   ```
   %%LST ROAMPER: HLRSN=1, GRPID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            GRPID = 1
                          GRPNAME = Group1
                               CC = 86
                        REJECTNUM = 3
                         OPR1NAME = Peking1
                    OPR1CSROAMPRO = 30
                    OPR1PSROAMPRO = 30
                         OPR2NAME = Peking2
                    OPR2CSROAMPRO = 30
                    OPR2PSROAMPRO = 30
                         OPR3NAME = Peking3
                    OPR3CSROAMPRO = 40
                    OPR3PSROAMPRO = 40

   Total count = 14

   There is together 1 report

   ---    END
   ```
3. 查询某个运营商及其归属的分组信息，“HLRSN”为“1”，“运营商名称”为“Peking1”：

   ```
   LST ROAMPER: HLRSN=1, OPRNAME="Peking1";
   ```

   ```
   %%LST ROAMPER: HLRSN=1, OPRNAME="Peking1";%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            GRPID = 1
                          GRPNAME = Group1
                               CC = 86
                        REJECTNUM = 3
                         OPR1NAME = Peking1
                    OPR1CSROAMPRO = 30
                    OPR1PSROAMPRO = 30

   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET ROAMPER**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                                          | 处理建议                                                             |
|:--------|:----------|:----------------------------------------------|:-----------------------------------------------------------------|
| ERR3097 | HLR序列号未定义 | 参数“HLR序列号”输入错误，实际输入的参数“HLR序列号”未定义。            | 根据实际情况，重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。 |
| ERR1010 | 参数冲突      | 同时输入了“分组ID”、“运营商名称”和“运营商ID”三个参数中的任意两个或三个全部输入。 | 根据实际情况，重新输入参数，确保满足“分组ID”、“运营商名称”和“运营商ID”三个参数同时只能输入其中一个。          |