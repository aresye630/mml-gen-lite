# 停止导出任务(STP EXPTASK)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于停止一个导出任务。

## 注意事项

该命令仅支持操作管理员执行。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                           |
|:-------|:-------|:---------------------------------------------------------------|
| TASKID | 任务ID   | 用于指示待停止导出任务的任务ID。操作员可以使用DSP EXPTASK命令查询获得。 取值范围：1～65535 默认值：无。 |

## 使用实例

1. 停止“任务ID”为“1”的导出任务。

   ```
   STP EXPTASK: TASKID=1;
   ```
2. 停止周期性导出任务。
   1. 执行**DSP EXPTASK**命令，查询周期性导出任务状态的“关联ID”。

      ```
      DSP EXPTASK:;
      ```

      ```
      %%DSP EXPTASK:;%%
      RETCODE = 0 操作成功

      <TASK ID>   <Service type>   <Status>         <Task type>      <Export file number>   <Successfully exported number>   <Failed exported number>   <Cycle unit>     <Cycle value>    <Correlation ID>   <Export time>        <Start time>         <Upload time>        <Finish time>        <MML CMD>
      268         USCDB            NOTSTART         CYCLE            0                      0                                0                          HOUR             1                266                2017-04-21 21:26:22                                                                 /*HWHandle=5*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=CYCLE, CYCLEUNIT=HOUR, CYCLEVALUE=1;
      271         USCDB            NOTSTART         CYCLE            0                      0                                0                          DAY              1                269                2017-04-22 20:28:01                                                                 /*HWHandle=17*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=CYCLE, CYCLEUNIT=DAY, CYCLEVALUE=1;
      273         USCDB            NOTSTART         CYCLE            0                      0                                0                          WEEK             1                272                2017-04-21 20:29:37                                                                 /*HWHandle=25*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=CYCLE, CYCLEUNIT=WEEK, CYCLEVALUE=1;
      276         SUP-FE           NOTSTART         CYCLE            0                      0                                0                          MONTH            1                274                2017-05-21 20:29:53                                                                 /*HWHandle=29*/ADD EXPTASK: FETYPE="SUP-FE", TPLNAME="DataExp_Test", TASKTYPE=CYCLE, CYCLEUNIT=MONTH, CYCLEVALUE=1;
      279         SUP-FE           NOTSTART         CYCLE            0                      0                                0                          WEEK             1                277                2017-04-28 20:31:18                                                                 /*HWHandle=40*/ADD EXPTASK: FETYPE="SUP-FE", TPLNAME="DataExp_Test", TASKTYPE=CYCLE, CYCLEUNIT=WEEK, CYCLEVALUE=1;
      294         USCDB            NOTSTART         ONCE             0                      0                                0                          NULL             0                0                  2017-04-25 08:11:45                                                                 /*HWHandle=12*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=ONCE, TIME=2017&04&25&08&11&45;
      295         USCDB            NOTSTART         ONCE             0                      0                                0                          NULL             0                0                  2017-05-25 08:11:45                                                                 /*HWHandle=25*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=ONCE, TIME=2017&05&25&08&11&45;
      296         USCDB            NOTSTART         ONCE             0                      0                                0                          NULL             0                0                  2017-05-25 08:11:45                                                                 /*HWHandle=26*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=ONCE, TIME=2017&05&25&08&11&45;
      297         USCDB            NOTSTART         ONCE             0                      0                                0                          NULL             0                0                  2017-05-25 08:11:45                                                                 /*HWHandle=27*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=ONCE, TIME=2017&05&25&08&11&45;
      298         USCDB            NOTSTART         ONCE             0                      0                                0                          NULL             0                0                  2017-05-25 08:11:45                                                                 /*HWHandle=28*/ADD EXPTASK: FETYPE="USCDB", TPLNAME="DataExp_USCDB_11001", TASKTYPE=ONCE, TIME=2017&05&25&08&11&45;

      Total count = 10

      There is together 1 report

      ---    END
      ```
   2. 执行**STP EXPTASK**命令，“任务ID”设置为a中查询到的“关联ID”，停止该任务ID的导出任务。

      ```
      STP EXPTASK: TASKID=266;
      ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释      | 原因分析                 | 处理建议                                             |
|------:|:-----------|:---------------------|:-------------------------------------------------|
|  5077 | 任务不存在。     | 指定的“任务ID”对应的任务不存在。   | 请先执行DSP EXPTASK命令查询所有的导出任务及状态，确认待停止任务的ID后再执行本命令。 |
|  5078 | 该任务已经停止运行。 | 待停止的导出任务已经处于停止运行状态了。 | -                                                |