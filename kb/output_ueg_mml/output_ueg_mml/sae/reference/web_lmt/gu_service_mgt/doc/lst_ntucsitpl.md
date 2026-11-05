# 查询NT-U-CSI模板(LST NTUCSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询NT-U-CSI模板的配置信息。

- 若需要查询某个虚拟HLR中所有NT-U-CSI模板的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个虚拟HLR中某条NT-U-CSI模板的详细配置信息，请同时输入“HLR序列号”和“NT-U-CSI模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称         | 参数说明                                                                                                       |
|:-------|:-------------|:-----------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号       | 用于标识系统需要按照哪个HLR序列号来查询NT-U-CSI模板数据，可以使用LST HLRSN命令查询获得。 默认值：无。                                              |
| TPLID  | NT-U-CSI模板ID | 用于标识系统需要按照哪个NT-U-CSI模板ID来查询NT-U-CSI模板数据；若不输入，则表示查询所有的NT-U-CSI模板ID。该参数必须先通过ADD NTUCSITPL命令配置才能在此处引用。 默认值：无。 |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR上的NT-U-CSI模板数据记录：

   ```
   LST NTUCSITPL: HLRSN=1;
   ```

   ```
   %%LST NTUCSITPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID          TPLNAME
                  1              NTUCSI1
                  123            NTUCSI123

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR上的NT-U-CSI模板数据记录。其中，“NT-U-CSI模板ID”为“123”：

   ```
   LST NTUCSITPL: HLRSN=1, TPLID=123;
   ```

   ```
   %%LST NTUCSITPL: HLRSN=1, TPLID=123;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 123
                          TPLNAME = NTUCSI123
                       UCSI_TPLID = 123
                       UCSI_TPLID = 124

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NTUCSITPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                     | 处理建议                                                                                              |
|:--------|:--------|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 输入的参数取值不在其取值范围内。                         | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                  |
| ERR3003 | 模板未定义   | 可能原因为如下之一：“HLR序列号”未定义。“NT-U-CSI模板ID”未定义。 | 确保满足以下两点：根据实际情况，重新输入“HLR序列号”，确保已通过ADD HLRSN命令定义。根据实际情况，重新输入“NT-U-CSI模板ID”，确保已通过ADD NTUCSITPL命令定义。 |