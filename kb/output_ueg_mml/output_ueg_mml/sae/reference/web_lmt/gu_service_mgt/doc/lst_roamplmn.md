# 查询运营商的PLMN标识(LST ROAMPLMN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询运营商ID、运营商名称和PLMN标识的对应关系：

- 若需要查询全部运营商ID和运营商名称，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个运营商网络配置的所有PLMN标识信息，请输入“HLR序列号”和“运营商ID”或“HLR序列号”和“运营商名称”，其他参数不输入。
- 若需要查询某个PLMN标识所属的运营商信息，请输入“HLR序列号”和“PLMN标识”，其他参数不输入。

## 注意事项

“运营商ID”、“运营商名称”和“PLMN标识”三个参数同时只能输入一个。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                        |
|:--------|:-------|:--------------------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询运营商和PLMN标识的对应关系，该参数必须选择。 |
| OPRID   | 运营商ID  | 用于指示系统按照哪个运营商ID来查询运营商和PLMN标识的对应关系。          |
| OPRNAME | 运营商名称  | 用于指示系统按照哪个运营商名称来查询运营商和PLMN标识的对应关系。          |
| PLMNID  | PLMN标识 | 用于指示系统按照哪个PLMN标识来查询运营商和PLMN标识的对应关系。         |

## 使用实例

1. 查询“HLRSN”为“1”的所有运营商ID和名称信息：

   ```
   LST ROAMPLMN: HLRSN=1;
   ```

   ```
   %%LST ROAMPLMN: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "OPRID"   "OPRNAME"
           025       nan001
           029       shan003

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLRSN”为“1”、“运营商ID”为“25”的所有PLMN标识信息：

   ```
   LST ROAMPLMN: HLRSN=1, OPRID=25;
   ```

   ```
   %%LST ROAMPLMN: HLRSN=1, OPRID=25;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            OPRID = 025
                          OPRNAME = nan001
                           PLMNID = 787878

   Total count = 4

   There is together 1 report

   ---    END
   ```
3. 查询“HLRSN”为“1”、“PLMN标识”为“898989”的运营商信息：

   ```
   LST ROAMPLMN: HLRSN=1, PLMNID="898989";
   ```

   ```
   %%LST ROAMPLMN: HLRSN=1, PLMNID="898989";%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            OPRID = 029
                          OPRNAME = shan003
                           PLMNID = 898989

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET ROAMPLMN**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                                            | 处理建议                                                             |
|:--------|:----------|:------------------------------------------------|:-----------------------------------------------------------------|
| ERR3097 | HLR序列号未定义 | 参数“HLR序列号”输入错误，实际输入的参数“HLR序列号”未定义。              | 根据实际情况，重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。 |
| ERR1010 | 参数冲突      | 同时输入了“运营商ID”、“运营商名称”、“PLMN标识”三个参数中的任意两个或三个全部输入。 | 根据实际情况，重新输入参数，确保满足“运营商ID”、“运营商名称”、“PLMN标识”三个参数同时只能输入其中一个。        |