# 查询USSD响应内容(LST USSDSTR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询USSD（Unstructured Supplementary Service Data）响应内容的配置信息。

请输入“HLR序列号”和“业务类型”查询相应USSD响应内容的配置信息。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                             |
|:--------|:-------|:---------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统需要按照哪个HLR序列号来查询USSD响应内容数据。 |
| SERVICE | 业务类型   | 用于指示系统需要按照哪个业务类型来查询USSD响应内容数据。   |

## 使用实例

1. 查询“HLR序列号”为“1”，“业务类型”为“MultiSIM”的USSD响应内容数据记录：

   ```
   LST USSDSTR: HLRSN=1, SERVICE=MultiSIM;
   ```

   ```
   %%LST USSDSTR: HLRSN=1, SERVICE=MultiSIM;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                          SERVICE = MultiSIM

                             SCEN = SuccActiveId
                          CONTENT = Success_Actived

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“2”，“业务类型”为“GROUP\_SECSIM\_DEA”的USSD响应内容数据记录：

   ```
   LST USSDSTR: HLRSN=2, SERVICE=GROUP_SECSIM_DEA;
   ```

   ```
   %%LST USSDSTR: HLRSN=2, SERVICE=GROUP_SECSIM_DEA;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 2
                          SERVICE = GROUP_SECSIM_DEA

                             SCEN = DeaByPrimaryOnly_S
                          CONTENT = 1234

   Total count = 4

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“3”，“业务类型”为“GROUP\_SECSIM\_ACT”的USSD响应内容数据记录：

   ```
   LST USSDSTR: HLRSN=3, SERVICE=GROUP_SECSIM_ACT;
   ```

   ```
   %%LST USSDSTR: HLRSN=3, SERVICE=GROUP_SECSIM_ACT;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 3
                          SERVICE = GROUP_SECSIM_ACT

                             SCEN = ActBySecondary_S
                          CONTENT = test

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD USSDSTR**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                          | 处理建议                                                         |
|:--------|:--------|:------------------------------|:-------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”与“业务类型”对应的数据在数据库中未添加。 | 根据实际情况，重新输入已定义的“HLR序列号”和“业务类型”，可通过LST HLRSN命令查询已定义的“HLR序列号”。 |