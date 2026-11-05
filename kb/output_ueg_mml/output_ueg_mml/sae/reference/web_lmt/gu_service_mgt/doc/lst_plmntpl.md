# 查询PLMN区域漫游模板(LST PLMNTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询EPS用户的PLMN区域漫游模板的配置信息：

- 若需要查询某个HLR序列号下全部PLMN区域漫游模板的概要配置信息，请只输入“HLR序列号”。
- 若需要查询某个HLR序列号下某个PLMN区域漫游模板的详细配置信息，请输入“HLR序列号”和“模板ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                             |
|:-------|:-------|:-------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询PLMN区域漫游模板信息数据。               |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询PLMN区域漫游模板信息数据；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询PLMN区域漫游模板信息，“HLR序列号”为“1”：

   ```
   LST PLMNTPL: HLRSN=1;
   ```

   ```
   %%LST PLMNTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  1            TEST
                  2            huawei

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询PLMN区域漫游模板信息，“HLR序列号”为“1”，“模板ID”为“1”：

   ```
   LST PLMNTPL: HLRSN=1, TPLID=1;
   ```

   ```
   %%LST PLMNTPL: HLRSN=1, TPLID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                       TPLID = 1
                 DEFAULTRULE = PERMISSION
                     ERRCODE = ROAMNTALD
   DEF_SERRESTTPLID_NON_3GPP = 1
       DEF_SERRESTTPLID_3GPP = 1
                  CUSTOMRULE = PERMIT
   MCC_Code
                         MCC = 886
   Zone_Code
                         MNC = 443
                     ISLOCAL = TRUE
                        RULE = PERMISSION
       SERRESTTPLID_NON_3GPP = 1
           SERRESTTPLID_3GPP = 1

   Total count = 12

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD PLMNTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                     |
|:--------|:--------|:------------------------|:-----------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST PLMNTPL命令查询已定义的“模板ID”。 |