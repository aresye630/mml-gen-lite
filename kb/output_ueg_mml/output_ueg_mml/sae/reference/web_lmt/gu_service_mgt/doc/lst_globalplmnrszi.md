# 查询全局PLMN区域漫游限制(LST GLOBALPLMNRSZI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询全局PLMN区域漫游限制数据信息：

- 若需要查询全局PLMN区域缺省漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“DEFRULE”。
- 若需要查询所有全局PLMN区域漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“ALL”。
- 若需要查询指定PLMN区域对应的漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“ONE”，并且输入指定的“移动国家码”和“移动网络码”参数。

## 注意事项

- 当“操作类型”参数为“DEFRULE”或“ALL”时，不能输入“移动国家码”或“移动网络码”参数的值。
- 当“操作类型”参数为“ONE”时，必须输入“移动国家码”和“移动网络码”参数的值。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                  |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询用户的漫游限制数据信息，该参数必须输入。                                                                                               |
| OPTYPE | 操作类型   | 用于指示系统按照哪种操作类型来查询用户的漫游限制数据信息，该参数必须输入。 取值范围：DEFRULE：查询全局PLMN区域缺省漫游限制数据信息。 ALL：查询所有全局PLMN区域漫游限制数据信息。 ONE：查询指定的PLMN区域对应的漫游限制数据信息。 默认值：无。 |
| MCC    | 移动国家码  | 仅当本命令中的“操作类型”参数为“ONE”时该参数有效。用于指示系统按照哪个移动国家码来查询全局PLMN区域漫游限制数据信息。                                                                       |
| MNC    | 移动网络码  | 仅当本命令中的“操作类型”参数为“ONE”时该参数有效。用于指示系统按照哪个移动网络码来查询全局PLMN区域漫游限制数据信息。                                                                       |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR中用户的全局PLMN区域缺省漫游限制数据信息：

   ```
   LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=DEFRULE;
   ```

   ```
   %%LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=DEFRULE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                      DEFAULTRULE = PERMISSION
                   DEFAULTERRCODE = ROAMNTALD

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR中用户的所有全局PLMN区域漫游限制数据信息：

   ```
   LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=ALL;
   ```

   ```
   %%LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=ALL;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "MCC"   "MNC"   "RULE"         "ERRCODE"
         460     111     PERMISSION     ROAMNTALD
         460     112     PERMISSION     ROAMNTALD

   Total count = 2

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”的HLR中指定PLMN区域的漫游限制数据信息，“移动国家码”为“460”，“移动网络码”为“111”：

   ```
   LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=ONE, MCC="460", MNC="111";
   ```

   ```
   %%LST GLOBALPLMNRSZI: HLRSN=1, OPTYPE=ONE, MCC="460", MNC="111";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "MCC"   "MNC"   "RULE"         "ERRCODE"
         460     111     PERMISSION     ROAMNTALD

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                               | 处理建议                                                                |
|:--------|:--------|:---------------------------------------------------|:--------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 当“操作类型”参数为“ONE”时，没有输入“移动国家码”或“移动网络码”参数的值或两者都没有输入。  | 根据实际情况，重新输入参数。确保当“操作类型”参数为“ONE”时，必须输入“移动国家码”和“移动网络码”参数的值。           |
| ERR1010 | 参数冲突    | 当“操作类型”参数为“DEFRULE”或“ALL”时，输入了“移动国家码”或“移动网络码”参数的值。 | 根据实际情况，重新输入参数。确保当“操作类型”参数为“DEFRULE”或“ALL”时，不能输入“移动国家码”或“移动网络码”参数的值。 |