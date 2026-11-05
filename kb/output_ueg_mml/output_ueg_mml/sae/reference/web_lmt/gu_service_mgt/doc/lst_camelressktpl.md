# 查询CAMEL限制业务键模板(LST CAMELRESSKTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询CAMEL限制业务键模板的配置信息：

- 若需要查询某个HLR上全部CAMEL限制业务键模板的概要配置信息，请只输入“HLR序列号”。
- 若需要查询某个CAMEL限制业务键模板的详细配置信息，请输入“HLR序列号”和“模板ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                             |
|:-------|:-------|:-------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询CAMEL限制业务键模板信息。               |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询CAMEL限制业务键模板信息；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询“HLR序列号”为“1”的全部CAMEL限制业务键模板信息。命令如下：

   ```
   LST CAMELRESSKTPL: HLRSN=1;
   ```

   ```
   %%LST CAMELRESSKTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                  TPLID        TPLNAME
                  0            tplname0
                  1            tplname1
                  2            tplname2
                  65534        <NULL>

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”、“模板ID”为“1”的CAMEL限制业务键模板信息。命令如下：

   ```
   LST CAMELRESSKTPL: HLRSN=1, TPLID=1;
   ```

   ```
   %%LST CAMELRESSKTPL: HLRSN=1, TPLID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 1
                          TPLNAME = tplname1
                           SKTYPE = OCSI
                               SK = 1

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD CAMELRESSKTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                     | 处理建议                                                                                  |
|:--------|:--------|:-----------------------------------------|:--------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”和“模板ID”参数对应的CAMEL限制业务键模板数据记录不存在。 | 输入的“HLR序列号”和“模板ID”参数对应的CAMEL限制业务键模板数据记录不存在，请确认是否需要增加该模板，如果需要请执行ADD CAMELRESSKTPL命令增加。 |