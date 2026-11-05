# 显示跨分区用户迁移任务（DSP MIGRATION）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于显示跨分区用户迁移或回退任务的状态信息。

## 注意事项

重启PGW模块后，再执行该命令查询之前的迁移或回退任务，只显示一条总记录，无法显示具体模块的迁移或回退信息。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                   |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------|
| TASKID | 任务ID   | 可选必选说明：可选参数 参数含义：用于指定需要查询跨分区用户迁移或回退任务的任务ID。若不输入，则表示查询全部迁移或回退任务。 取值范围：1~4294967295。 默认值：无。 配置原则：无                                       |
| FETYPE | FE类型   | 可选必选说明：可选参数 参数含义：用于指定需要查询哪个FE类型的迁移或回退任务。若不输入，则表示查询全部FE类型对应的任务。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：该参数是联想参数，不能手动输入，必须选择加载后的插件类型，不包括USCDB类型。 |
| OPTYPE | 操作类型   | 可选必选说明：可选参数 参数含义：用于指定查询迁移任务还是回退任务的状态信息。若不输入，则表示查询全部操作类型的任务。 取值范围： MIGRATION：指定查询迁移任务状态信息。ROLLBACK：指定查询迁移回退任务状态信息。 默认值：无。 配置原则：无        |

## 使用实例

查询全部跨分区用户迁移或回退任务状态信息。

```
DSP MIGRATION:;
```

```
%%DSP MIGRATION:;%% 
RETCODE = 0 操作成功  

<Task ID>   <Service type>   <Cluster ID>  <Module ID>  <Operation type>  <Status>                   <Start time>         <End time>           <Number of successful subscribers>  <Number of failed subscribers>  <Number of subscribers with successful rollback>  <Number of subscribers with failed rollback>  <Number of non-existent subscribers>  <MML info> 
218         SUP-FE           NULL          NULL         Rollback          Completed                  2022-07-29 02:46:58  2022-07-29 02:47:00  0                                   10                              NULL                                              NULL                                          NULL                                  RBK MIGRATION: TASKID=217; 
219         SUP-FE           NULL          NULL         Rollback          Completed                  2022-07-29 04:09:55  2022-07-29 04:09:57  10                                  0                               NULL                                              NULL                                          NULL                                  RBK MIGRATION: TASKID=217; 
220         SUP-FE           NULL          NULL         Migration         Completed                  2022-07-29 06:35:06  2022-07-29 06:35:08  10                                  0                               0                                                 0                                             0                                     STR MIGRATION: FETYPE="SUP-FE", KEYTYPE="SUID", PARTITIONID=18, TRANSTYPE=USERNUM, USERNUM=10; 
221         SUP-FE           NULL          NULL         Rollback          Completed                  2022-07-29 06:35:38  2022-07-29 06:35:40  0                                   10                              NULL                                              NULL                                          NULL                                  RBK MIGRATION: TASKID=220; 

Total count = 4

There is together 1 report  

---    END
```

查询“任务ID”为“317”，“FE类型”为“SUP-FE”，“操作类型”为“ROLLBACK”任务的状态信息。

```
DSP MIGRATION: TASKID=317, FETYPE="SUP-FE", OPTYPE=ROLLBACK;
```

**说明** 

当查询特定“任务ID”时，该命令会返回每个“Module ID”迁移或迁移回退的用户数量，最后一行表示该“任务ID”一共迁移或迁移回退的用户数量。

```
%%DSP MIGRATION: TASKID=317, FETYPE="SUP-FE", OPTYPE=ROLLBACK;%% 
RETCODE = 0 操作成功

<Task ID>   <Service type>   <Cluster ID>  <Module ID>  <Operation type>  <Status>                   <Start time>         <End time>           <Number of successful subscribers>  <Number of failed subscribers>  <Number of subscribers with successful rollback>  <Number of subscribers with failed rollback>  <Number of non-existent subscribers>  <MML info> 
317         SUP-FE           1097          1097         Rollback          Completed                  2022-08-18 10:26:58  2022-08-18 10:27:00  10                                  0                               NULL                                              NULL                                          NULL                                  NULL 
317         SUP-FE           1097          1098         Rollback          Completed                  2022-08-18 10:26:58  2022-08-18 10:27:00  0                                   0                               NULL                                              NULL                                          NULL                                  NULL 
317         SUP-FE           1101          1101         Rollback          Completed                  2022-08-18 10:26:58  2022-08-18 10:27:00  0                                   0                               NULL                                              NULL                                          NULL                                  NULL 
317         SUP-FE           1101          1102         Rollback          Completed                  2022-08-18 10:26:58  2022-08-18 10:27:00  0                                   0                               NULL                                              NULL                                          NULL                                  NULL 
317         SUP-FE           NULL          NULL         Rollback          Completed                  2022-08-18 10:26:58  2022-08-18 10:27:00  10                                  0                               NULL                                              NULL                                          NULL                                  RBK MIGRATION: TASKID=315, ISFORCE=YES;

Total count = 5  

There is together 1 report  

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各输出项含义请参见表1。

| 输出项名称                                          | 输出项解释                                                                                                                                                |
|:-----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Task ID                                        | 用于返回迁移或回退任务的ID。                                                                                                                                      |
| Service type                                   | 用于返回用户数据迁移或回退任务的业务类型。                                                                                                                                |
| Cluster ID                                     | 用于返回迁出分区的Cluster ID。                                                                                                                                 |
| Module ID                                      | 用于返回迁出分区的Module ID。                                                                                                                                  |
| Operation type                                 | 用于返回用户数据迁移或回退任务的操作类型。 取值范围： MIGRATION：迁移。ROLLBACK：回退。                                                                                                |
| Status                                         | 用于返回用户数据迁移任务的状态。 取值范围： Running：任务正在执行中。Terminating：任务正在终止中。Terminated unexpectedly：任务异常终止。Terminated manually：执行STP MIGRATION停止的任务。Completed：任务执行结束。 |
| Start time                                     | 用于返回任务启动的时间。                                                                                                                                         |
| End time                                       | 用于返回任务结束的时间。                                                                                                                                         |
| Number of successful subscribers               | 用于返回迁移或回退任务操作成功的用户个数。                                                                                                                                |
| Number of failed subscribers                   | 用于返回迁移或回退任务操作失败的用户个数。                                                                                                                                |
| Number of subscribers with successful rollback | 用于返回迁移失败后回滚成功的用户个数。                                                                                                                                  |
| Number of subscribers with failed rollback     | 用于返回迁移失败后回滚失败的用户个数。                                                                                                                                  |
| Number of non-existent subscribers             | 用于返回用户列表迁移类型中不存在的用户个数。                                                                                                                               |
| MML info                                       | 用于返回跨分区用户迁移或迁移回退的MML命令信息。                                                                                                                            |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释            | 原因分析                              | 处理建议                                                                                                                                              |
|------:|:-----------------|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
|  1038 | 记录不存在。           | 指定“任务ID”参数时，该任务不存在或者满足条件的任务记录不存在。 | 执行DSP MIGRATION命令查询已存在的“任务ID”后，重新执行本命令查询，确保查询的任务在系统中存在或满足条件。                                                                                      |
|  5079 | 指定的业务类型不存在或未加载。  | 指定的“FE类型”不存在或者未加载。                | 在“USCDB MML命令”界面执行LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即本命令的“FE类型”。 若“FE类型”加载成功，请在执行该命令时输入正确的服务类型名称。 若“FE类型”加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。 |
|  5243 | USCDB应用类型不支持该操作。 | 跨分区迁移或回退不支持对USCDB应用类型进行操作。        | 迁移或回退不支持对USCDB应用类型进行操作。请选择其他业务类型。                                                                                                                 |