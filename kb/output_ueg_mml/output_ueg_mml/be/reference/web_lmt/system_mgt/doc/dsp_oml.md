# 查询内存数据库任务（DSP OML）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询当前正在执行的内存数据库的任务结果。

## 注意事项

- 该命令仅支持通过PGW Web LMT接入。
- 该命令仅支持超级管理员、ADMINISTRATOR级别的操作员和CUSTOM级别的操作员执行。

## 参数说明

无。

## 使用实例

1. 当操作内存数据库任务中未配置“过滤条件文件”参数或“过滤条件文件”未配置属性RuleName时，查询正在执行的内存数据库的任务信息。

   ```
   DSP OML:;
   ```

   ```
   %%DSP OML:;%%
   RETCODE = 0 操作成功

   <FETYPE>    <OBJNAME>        <STATUS>         <STARTTIME>          <ENDTIME>            <TOTAL>          <SUCCESS>        <MML CMD>
   SUP-FE      SUID_DATA        COMPLETED        2020-03-06 06:35:34  2020-03-06 06:35:36  1                1                /*HWHandle=6*/EXC OML: FETYPE="SUP-FE", OBJNAME="SUID_DATA", OML="update AUC1_DATA set INT16_1 /e 9";

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 当操作内存数据库任务中配置了“过滤条件文件”参数并且“过滤条件文件”有配置属性RuleName时，查询正在执行的内存数据库的任务信息。

   ```
   DSP OML:;
   ```

   ```
   %%DSP OML:;%%
   RETCODE = 0 操作成功

   <FETYPE>    <OBJNAME>     <RULENAME>   <STATUS>         <STARTTIME>          <ENDTIME>            <TOTAL>          <SUCCESS>        <MML CMD>
   SUP-FE      SUID_DATA     rule1        RUNNING          2024-07-15 17:20:31                       100              100              /*HWHandle=65542*/EXC OML: FETYPE="SUP-FE", OBJNAME="SUID_DATA", FILTERFILE="default_excoml_filterfile.xml";
   SUP-FE      SUID_DATA     rule10       RUNNING          2024-07-15 17:20:31                       100              100              /*HWHandle=65542*/EXC OML: FETYPE="SUP-FE", OBJNAME="SUID_DATA", FILTERFILE="default_excoml_filterfile.xml";

   Total count = 2

   There is together 1 report
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1的参数说明。

| 输出项名称     | 输出结果解释                                                                                                                                          |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| FETYPE    | 用于返回操作数据对应的FE类型。                                                                                                                                |
| OBJNAME   | 用于返回对象树的名称。                                                                                                                                     |
| RULENAME  | 用于返回内存数据库任务的过滤规则，由EXC OML命令中“过滤条件文件”参数的属性RuleName指定。                                                                                            |
| STATUS    | 用于返回内存数据库任务的执行状态。 取值说明：RUNNING：运行。COMPLETED：完成。ABNORMAL：异常终止，对应过程中DMA重启等异常场景。ABORTED：手工终止，执行STP OML命令终止任务。PREPROCESSING：准备阶段，对应用户列表查询DSU CID场景。 |
| STARTTIME | 用于返回任务开始的时间点。                                                                                                                                   |
| ENDTIME   | 用于返回任务结束的时间点。 若任务未结束，则不显示。                                                                                                                      |
| TOTAL     | 用于返回已执行符合条件的个数。                                                                                                                                 |
| SUCCESS   | 用于返回任务已成功执行个数。                                                                                                                                  |
| MML CMD   | 用于返回启动任务的MML命令。                                                                                                                                 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                                           | 原因分析                                                | 处理建议                                              |
|------:|:------------------------------------------------|:----------------------------------------------------|:--------------------------------------------------|
|  5178 | 没有历史任务信息。                                       | PGW模块当前为初始化状态，未执行EXC OML命令操作。                       | 待有EXC OML命令执行完后，再重新执行本命令查询。                       |
|  5179 | 只有超级管理员、ADMINISTRATOR级别的操作员和CUSTOM级别的操作员可执行该命令。 | 当前执行命令的操作员不是超级管理员、ADMINISTRATOR级别的操作员或CUSTOM级别的操作员。 | 请使用超级管理员、ADMINISTRATOR级别的操作员或CUSTOM级别的操作员账号执行本命令。 |
|  5072 | 该命令只能通过WebLMT接入。                                | 不是通过PGW Web LMT来执行该命令。                              | 请通过PGW Web LMT执行本命令。                              |