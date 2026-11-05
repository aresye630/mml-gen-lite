# 查询自动批操作文件名称(LST BATFILENAME)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询自动批操作文件名称的配置信息。

- 若需要查询系统中所有自动批操作文件名称的配置信息，请不要输入“批操作文件名前缀”参数。
- 若需要查询系统中某条自动批操作文件名称的配置信息，请输入“批操作文件名前缀”参数。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称     | 参数说明                                                       |
|:----------|:---------|:-----------------------------------------------------------|
| BATPREFIX | 批操作文件名前缀 | 用于指示系统需要按照哪个批操作文件名前缀来查询批操作文件名前缀数据；若不输入，则表示查询所有的批操作文件名前缀数据。 |

## 使用实例

1. 查询系统中所有批操作文件名前缀数据记录，不输入参数：

   ```
   LST BATFILENAME:;
   ```

   ```
   %%LST BATFILENAME:;%%
   RETCODE = 0 SUCCESS0001:操作成功

   BATPREFIX     RSTPREFIX     RSTSUCCPREFIX     RSTERRPREFIX     RSTDETAILPREFIX
   bat1          rst1          succ1             err1             detail1
   bat2          rst2          succ2             err2             detail2
   bat3          rst3          succ3             err3             detail3

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询系统中“批操作文件名前缀”为“bat1”的批操作文件名数据记录：

   ```
   LST BATFILENAME: BATPREFIX="bat1";
   ```

   ```
   %%LST BATFILENAME: BATPREFIX="bat1";%%
   RETCODE = 0 SUCCESS0001:操作成功

                        BATPREFIX = bat1
                        RSTPREFIX = rst1
                    RSTSUCCPREFIX = succ1
                     RSTERRPREFIX = err1
                  RSTDETAILPREFIX = detail1

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 消息解释   | 原因分析           | 处理建议                               |
|:--------|:-------|:---------------|:-----------------------------------|
| ERR3007 | 记录不存在  | “批操作文件名前缀”未定义。 | 根据实际情况，重新输入已定义的“批操作文件名前缀”再执行此命令查询。 |