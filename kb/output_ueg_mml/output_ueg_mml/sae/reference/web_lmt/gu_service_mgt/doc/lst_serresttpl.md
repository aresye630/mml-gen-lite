# 查询业务限制模板(LST SERRESTTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询业务限制模板中的配置信息：

- 若要查询全部的业务限制模板的数据信息，请输入“HLR序列号”参数。
- 若需要查询某个业务限制模板的详细信息，请输入全部参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                           |
|:-------|:-------|:-----------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询业务限制模板数据信息。                 |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询业务限制模板数据信息；若不输入，则表示查询所有的模板ID。 |

## 使用实例

1. 查询业务限制模板，“HLR序列号”为“1”。命令如下：

   ```
   LST SERRESTTPL: HLRSN=1;
   ```

   ```
   %%LST SERRESTTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  0            serrest002
                  1            serrest001

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询业务限制模板，“HLR序列号”为“1”，“模板ID”为“6”。命令如下：

   ```
   LST SERRESTTPL: HLRSN=1, TPLID=6;
   ```

   ```
   %%LST SERRESTTPL: HLRSN=1, TPLID=6;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 6
                          TPLNAME = <NULL>

                         SERCODE1 = SMS_CSI

                         SERCODE2 = PLMN_SS_5

                         SERCODE3 = COLP

                         SERCODE4 = CLIR

                         SERCODE5 = NSA

   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SERRESTTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                           | 处理建议                                                                            |
|:--------|:--------|:-------------------------------|:--------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”和“模板ID”参数对应的模板数据记录不存在。 | 根据实际情况，重新输入参数，确保“HLR序列号”和“模板ID”参数对应的模板数据记录已存在。已存在的模板数据记录可以通过LST SERRESTTPL命令查询。 |