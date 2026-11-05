# 查询QoS模板(LST QOSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询QoS模板数据。

- 若需要查询全部的QoS模板数据，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某条QoS模板数据，请同时输入“HLR序列号”和“模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                              |
|:-------|:-------|:------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 标识QoS模板数据记录的关键字段之一，用于指定在哪个HLR上删除QoS模板数据记录，操作员可以使用LST HLRSN命令查询获得。 |
| TPLID  | 模板ID   | 用于标识系统需要按照哪个模板ID来查询QoS模板数据；若不输入，则表示所有的模板ID。                       |

## 使用实例

1. 查询“HLR序列号”为1的所有QoS模板信息。命令如下：

   `LST QOSTPL: HLRSN=1;`

   ```
   %%LST QOSTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  10           QoS
                  11           QoS-11
                  100          11

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为1，“模板ID”为10的QoS模板信息。命令如下：

   `LST QOSTPL: HLRSN=1, TPLID=10;`

   ```
   %%LST QOSTPL: HLRSN=1, TPLID=10;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 10
                          TPLNAME = QoS
                           RELCLS = ACKALLPRODT
                         DELAYCLS = DELAY1
                           PRECLS = HIGH
                          PEAKTHR = 1000 OCT
                          MEANTHR = 100 OCT
                         PRILEVEL = 0
                    PREEMPTIONCAP = ENABLE
                    PREEMPTIONVUL = ENABLE

   Total count = 11

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD QOSTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析            | 处理建议                                                         |
|:--------|:--------|:----------------|:-------------------------------------------------------------|
| ERR3003 | 模板未定义   | 输入的“模板ID”参数未定义。 | 根据实际情况，重新输入“模板ID”参数的取值，确保其存在。已存在的“模板ID”参数可以通过LST QOSTPL命令查询。 |