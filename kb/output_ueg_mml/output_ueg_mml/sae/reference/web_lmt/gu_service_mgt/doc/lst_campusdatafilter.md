# 查询园区数据过滤条件(LST CAMPUSDATAFILTER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询园区用户数据导出的过滤条件。

- 若需要查询过滤条件名称和过滤条件类型相同的所有记录，请输入“过滤条件名称”和“过滤条件类型”。
- 若需要查询过滤条件类型相同的所有记录，请只输入“过滤条件类型”。

## 注意事项

该命令仅在特定局点使用，其他局点不需要配置。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                     |
|:-----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| FILTERNAME | 过滤条件名称 | 可选必选说明：可选参数 参数含义：用于指示系统按照“过滤条件名称”来查询用户数据导出的过滤条件信息。 取值范围：长度不超过64位的字符串，只允许输入数字和字母。 默认值：无。 配置原则：无。                                                          |
| FILTERTYPE | 过滤条件类型 | 可选必选说明：必选参数 参数含义：用于指示系统按照“过滤条件类型”来查询用户数据导出的过滤条件信息。 取值范围： IMSIPRE：IMSI前缀过滤条件类型。MSISDNPRE：MSISDN前缀过滤条件类型。DNN：DNN过滤条件类型。SNSSAI：SNSSAI过滤条件类型。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有用户数据导出的过滤条件。

   ```
   LST CAMPUSDATAFILTER: FILTERTYPE=IMSIPRE;
   ```

   ```
   %%LST CAMPUSDATAFILTER: FILTERTYPE=IMSIPRE;%%
   RETCODE = 0 SUCCESS0001:操作成功

   FILTERNAME     FILTERTYPE            FILTERVALUE
   FILTERNAME1    IMSIPRE               963589125423

   Total count = 1  

   There is together 1 report  

   ---    END
   ```
2. 查询过滤条件名称和过滤条件类型相同的所有记录，“过滤条件名称”为“FILTERNAME2”，“过滤条件类型”为“DNN”。

   ```
   LST CAMPUSDATAFILTER: FILTERNAME="FILTERNAME2", FILTERTYPE=DNN;
   ```

   ```
   %%LST CAMPUSDATAFILTER: FILTERNAME="FILTERNAME2", FILTERTYPE=DNN;%%
   RETCODE = 0 SUCCESS0001:操作成功

   FILTERNAME             FILTERTYPE            FILTERVALUE
   FILTERNAME2            DNN                   1-Y143D5

   Total count = 1  

   There is together 1 report  

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD CAMPUSDATAFILTER**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如所表1示。

| 错误码     | 消息解释   | 原因分析                         | 处理建议                                   |
|:--------|:-------|:-----------------------------|:---------------------------------------|
| ERR3007 | 记录不存在。 | 查询的“过滤条件名称”或者“过滤条件类型”的记录不存在。 | 请先通过ADD CAMPUSDATAFILTER添加相关信息后再执行此命令。 |