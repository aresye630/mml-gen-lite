# 查询APN限制模板(LST APNRESTTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询APN限制模板。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                           |
|:-------------|:-------|:-----------------------------------------------|
| HLRSN        | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询APN限制模板。                    |
| APNRESTTPLID | 模板ID   | 用于指示系统需要按照APN限制模板ID来查询；若不输入，则表示查询所有的APN限制模板列表。 |

## 使用实例

1. 要查询APN限制模板，“HLR序列号”为“1”，“模板ID”为“2”：

   ```
   LST APNRESTTPL: HLRSN=1, APNRESTTPLID=2;
   ```

   ```
   %%LST APNRESTTPL: HLRSN=1, APNRESTTPLID=2;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                     APNRESTTPLID = 2
                          TPLNAME = apn1
                              APN = def.com
                              APN = abc.com

   Total count = 5

   There is together 1 report

   ---    END
   ```
2. 要查询全部APN限制模板列表，“HLR序列号”为“1”：

   ```
   LST APNRESTTPL: HLRSN=1;
   ```

   ```
   %%LST APNRESTTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                  APNRESTTPLID   TPLNAME
                  2              apn1

   Total count = 1

   There is together 1 report

   ---    END
   ```