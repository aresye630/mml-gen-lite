# 查询导出日志任务(LST EXPLOGTASK)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询操作日志导出任务的配置数据。

- 若需要查询所有操作日志导出任务的配置数据，则不输入任何参数。
- 若需要查询某个操作日志导出任务的配置数据，请输入“任务ID”或“任务ID”与其他参数的组合。

## 注意事项

该命令仅支持操作管理员执行。

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                    |
|:---------------|:-------|:------------------------------------------------------------------------------------------------------------------------|
| EXPTASKID      | 任务ID   | 用于指示系统需要按照哪个任务ID来查询操作日志导出任务的配置数据，若不输入，则查询所有操作日志导出任务的配置数据。                                                               |
| SERVERNAME     | 服务器名称  | 用于指示系统需要按照哪个服务器名称来查询操作日志导出任务的配置数据，若不输入，则查询所有操作日志导出任务的配置数据。                                                              |
| TASKMODE       | 任务模式   | 用于指示系统需要按照哪个任务模式来查询操作日志导出任务的配置数据，若不输入，则查询所有操作日志导出任务的配置数据。                                                               |
| FETYPE         | FE类型   | 用于指示系统需要按照哪个FE类型来查询操作日志导出任务的配置数据，若不输入，则查询所有FE类型的操作日志导出任务的配置数据。 FE业务类型需要通过“USCDB MML命令”界面的LOD FEPLUG命令加载对应的FE插件包之后，在此引用。 |
| TASKTYPE       | 任务类型   | 用于指示系统需要按照哪个任务类型来查询操作日志导出任务的配置数据，若不输入，则查询所有操作日志导出任务的配置数据。                                                               |
| CYCLEUNIT      | 周期单位   | 用于指示系统需要按照哪个周期单位来查询操作日志导出任务的配置数据，若不输入，则查询所有周期单位的操作日志导出任务的配置数据。                                                          |
| AUDITCYCLEUNIT | 审计周期单位 | 用于指示系统需要按照哪个审计周期单位来查询审计日志导出任务的配置数据，若不输入，则查询所有审计周期单位的审计日志导出任务的配置数据。                                                      |
| EXPCYCLE       | 导出周期   | 用于指示系统需要按照哪个导出周期来查询操作日志导出任务的配置数据，若不输入，则查询所有导出周期的操作日志导出任务的配置数据。                                                          |

## 使用实例

1. 查询所有导出任务的配置数据。

   ```
   LST EXPLOGTASK:;
   ```

   ```
   %%LST EXPLOGTASK:;%%
   RETCODE = 0 操作成功
      
   <Export task ID>   <Server name>   <Task mode>   <FE type>   <Task type>   <Cycle unit>   <Audit cycle unit>   <Export cycle>   <Start time>          <Field>                                                                                                                                                                                                                                                                            <Filter>   <File name>   <Titles>
   201                A               AUDIT         NULL        ONCE          NULL           NULL                 0                2020-09-09 12:40:33   OPERATOR_NAME/OPERATION_TIME/MML_COMMAND/CMDRESULT/IP                                                                                                                                                                                                                                                       LogTime,SubUser,App,Sip,AppModule,OpType,OpText,Result
   210                A               COMMON        SUP-FE      ONCE          NULL           NULL                 0                2020-09-09 11:03:47   SERIAL_NO/cHLR_INDEX/cOPERATOR_NAME/cOPERATION_TIME/cMML_COMMAND/cCMDRESULT/cBATCH_TASK_ID/cCOMMAND_NO/cMSG_TYPE/cIMSI_NO/cMSISDN_NO/cERRORCODE/crawtohex(IP)/cPORT/cSUB_ID/cIMPI_NO/cIMPU_NO/cFE_TYPE/cPARTITION_ID/cOPERATION_STRTIME/cOPERATION_STRTIME_MS/cOPERATION_TIME_MS              A.txt

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询导出任务的配置数据，“任务ID”为“201”。

   ```
   LST EXPLOGTASK: EXPTASKID=201;
   ```

   ```
   %%LST EXPLOGTASK: EXPTASKID=201;%%
   RETCODE = 0 操作成功

                   Export task ID = 201
                      Server name = A
                        Task mode = AUDIT
                          FE type = NULL
                        Task type = ONCE
                       Cycle unit = NULL
                 Audit cycle unit = NULL
                     Export cycle = 0
                       Start time = 2020-09-09 12:40:33
                            Field = OPERATOR_NAME/OPERATION_TIME/MML_COMMAND/CMDRESULT/IP
                           Filter = NULL
                        File name = NULL
                           Titles = LogTime,SubUser,App,Sip,AppModule,OpType,OpText,Result

   Total count = 13

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD EXPLOGTASK**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释   | 原因分析                | 处理建议                                                |
|------:|:--------|:--------------------|:----------------------------------------------------|
|  1038 | 记录不存在。  | 输入的“任务ID”所对应的记录不存在。 | 执行本命令不输入任何参数，查询已存在的“任务ID”后，重新执行本命令查询，确保查询的任务在系统中存在。 |