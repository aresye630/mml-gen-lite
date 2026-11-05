# 查询园区配置(LST CAMPUSCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询园区配置数据信息：

- 若要查询全部园区配置数据信息，请不要输入任何参数。
- 若要查询某个园区配置数据信息，请输入“园区名称”参数。

## 注意事项

该命令仅在特定局点使用，其他局点不需要配置。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                      |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------|
| CAMPUSNAME | 园区名称   | 可选必选说明：可选参数 参数含义：用于指示系统按照哪一个园区名称来查询园区配置数据信息；若不输入，则表示所有的园区名称。 取值范围：长度不超过16位的字符串，只允许输入数字、字母和下划线。 默认值：无。 配置原则：“园区名称”区分大小写字母。 |

## 使用实例

1. 查询全部园区配置数据信息：

   ```
   LST CAMPUSCFG:;
   ```

   ```
   %%LST CAMPUSCFG:;%%
   RETCODE = 0 SUCCESS0001:操作成功

   CAMPUSNAME       FILTERNAME      K4SNO       OPSNO    EXPDATATYPE    FEATURETYPE
   campus1          filter1         1           NULL     5G             REDCAP
   campus2          filter2         1           NULL     5G             REDCAP  
   campus3          filter3         1           NULL     4G&5G          NULL
   campus4          filter4         1           NULL     4G&5G          NULL

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询某个园区配置数据信息，“园区名称”为“campus1”：

   ```
   LST CAMPUSCFG: CAMPUSNAME="campus1";
   ```

   ```
   %%LST CAMPUSCFG: CAMPUSNAME="campus1";%%
   RETCODE = 0 SUCCESS0001:操作成功

   CAMPUSNAME       FILTERNAME      K4SNO       OPSNO    EXPDATATYPE    FEATURETYPE
   campus1          filter1         1           NULL     5G             REDCAP

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD CAMPUSCFG**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                   | 处理建议                                           |
|:--------|:--------|:-----------------------|:-----------------------------------------------|
| ERR3007 | 记录不存在。  | 输入的“园区名称”对应记录在数据库中不存在。 | 根据实际情况，重新输入参数，确保通过本命令查询，“园区名称”参数对应的配置数据记录是存在的。 |