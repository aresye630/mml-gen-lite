# 查询EPS QoS模板(LST EPSQOSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询EPS QoS模板数据信息：

- 若需要查询全部EPS QoS模板数据信息，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个EPS QoS模板数据的详细信息，请输入“HLR序列号”和“QoS模板ID”。

## 注意事项

- 如果没有指定TPLID，显示所有的EPS QoS模板ID和相关数据。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                      |
|:-------|:--------|:----------------------------------------------------------|
| HLRSN  | HLR序列号  | 用于指示系统按照哪个HLR序列号来查询EPS QoS模板数据。                           |
| TPLID  | QoS模板ID | 用于指示系统按照哪个QoS模板ID来查询EPS QoS模板数据；若不输入，则表示查询所有的EPS QoS模板数据。 |

## 使用实例

1. 查询“HLR序列号”为1的所有EPS QoS模板信息。命令如下：

   ```
   LST EPSQOSTPL: HLRSN=1;
   ```

   如果操作成功，返回的结果可能如下：

   ```
   %%LST EPSQOSTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  10           EPS-QoS
                  11           EPS-QoS-11
                  100          EPS

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为1，“QoS模板ID”为10的EPS QoS模板信息。命令如下：

   ```
   LST EPSQOSTPL: HLRSN=1, TPLID=10;
   ```

   如果操作成功，返回的结果可能如下：

   ```
   %%LST EPSQOSTPL: HLRSN=1, TPLID=10;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            TPLID = 10
                          TPLNAME = EPS-QoS
                       QOSCLASUID = 5
                           EXTQCI = 130
                         PRILEVEL = 1
                    PREEMPTIONCAP = ENABLE
                    PREEMPTIONVUL = ENABLE
                   AMBRMAXREQBWUL = 4294967295
                   AMBRMAXREQBWDL = 4294967295
                         AMBRNRUL = 10000
                         AMBRNRDL = 20000

   Total count = 11

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD EPSQOSTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                             | 处理建议                                                                                                                               |
|:--------|:--------|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因如下：需要查询的虚拟HLR中未添加模板。“HLR序列号”和“QoS模板ID”参数对应的EPS QoS模板数据记录不存在。 | 根据可能原因可按如下方法操作：如果需要增加模板，可以通过ADD EPSQOSTPL命令为该虚拟HLR增加模板。确保满足“HLR序列号”和“QoS模板ID”参数对应的EPS模板数据记录已存在。已存在的EPS模板数据记录可以通过LST EPSQOSTPL命令查询。 |