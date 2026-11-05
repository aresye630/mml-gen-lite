# 查询MAP消息地址过滤模板(LST MAPADDRRESTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已添加的MAP消息地址过滤模板信息：

- 若需要查询某个HLR序列号下全部MAP消息地址过滤模板的概要配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个HLR序列号下某个MAP消息地址过滤模板的某个MAP操作流程的详细配置信息，请输入“HLR序列号”、“模板ID”和“MAP操作流程”参数。

## 注意事项

“模板ID”参数和“MAP操作流程”参数必须同时输入或不输入。

## 参数说明

| 参数标识         | 参数名称    | 参数说明                                                    |
|:-------------|:--------|:--------------------------------------------------------|
| HLRSN        | HLR序列号  | 用于指示系统查询哪个HLR序列号的MAP消息地址过滤模板信息数据。                       |
| TPLID        | 模板ID    | 用于指示系统按照哪个模板ID来查询MAP消息地址过滤模板信息数据；若不输入，则表示所有的模板ID。       |
| MAPPROCEDURE | MAP操作流程 | 用于指示系统按照哪个MAP操作流程来查询MAP消息地址过滤模板信息数据；若不输入，则表示所有的MAP操作流程。 |

## 使用实例

1. 查询“HLR序列号”为“1”的虚拟HLR下添加的全部MAP消息地址过滤模板信息，命令如下：

   ```
   LST MAPADDRRESTPL: HLRSN=1;
   ```

   ```
   %%LST MAPADDRRESTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  2            test
                  3            test01

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的虚拟HLR下“模板ID”为“2”的短信息取路由流程已添加的MAP消息地址过滤模板信息，命令如下：

   ```
   LST MAPADDRRESTPL: HLRSN=1, TPLID=2, MAPPROCEDURE=SRIFORSM;
   ```

   ```
   %%LST MAPADDRRESTPL: HLRSN=1, TPLID=2, MAPPROCEDURE=SRIFORSM;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 2
                          TPLNAME = test01
                             RULE = RESTRICT

                            ADDRPREFIX
                            861389955

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD MAPADDRRESTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                     | 处理建议                                                                           |
|:--------|:--------|:-----------------------------------------|:-------------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 查询某个模板的详细信息时，未输入“模板ID”或者“MAP操作流程”参数的参数值。 | 确认是否要查询某个模板的详细信息，若是请确保“HLR序列号”、“模板ID”和“MAP操作流程”三个参数均已输入参数值。                    |
| ERR3003 | 模板未定义   | “HLR序列号”或者“模板ID”参数未定义。                   | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过该命令查询已定义的“模板ID”。 |