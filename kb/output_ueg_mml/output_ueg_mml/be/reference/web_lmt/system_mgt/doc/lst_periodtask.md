# 查询周期性任务（LST PERIODTASK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已经添加的周期性任务。

- 若要查询所有已经添加的周期性任务，请不要输入任何参数。
- 若要查询某个周期性任务的详细信息，请输入“任务ID”或“FE类型”或这两个参数的组合。

## 注意事项

- 该命令仅支持通过PGW Web LMT接入。
- 该命令仅支持超级管理员、ADMINISTRATOR级别的操作员和CUSTOM级别的操作员执行。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                 |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| TASKID | 任务ID   | 可选必选说明：可选参数。 参数含义：用于指定周期性任务的任务ID，若不输入，则表示查询所有任务ID的周期性任务。 取值范围：1～512。 默认值：无。 配置原则：无。                                                                  |
| FETYPE | FE类型   | 可选必选说明：可选参数。 参数含义：用于指定查询哪个FE类型的周期性任务，若不输入，则表示查询所有FE类型的周期性任务。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：此参数在USCDB下唯一，通过“MML命令行 - USCDB”的LOD FEPLUG命令加载FE插件后在此引用。 |

## 使用实例

- 查询所有已经添加的周期性任务。

  ```
  LST PERIODTASK:;
  ```

  ```
  %%LST PERIODTASK:;%%
  RETCODE = 0 操作成功

  <Task ID>   <FE type>   <MML command>                                                                                            <Task type>   <Cycle unit>   <Cycle value>   <Start time>          <Task description>
  1           SUP-FE      EXC OML: FETYPE="USCDB", OBJNAME="PGW_PERIODTASK_SUMMARY", OML="select * from PGW_PERIODTASK_SUMMARY";   CYCLE         HOUR           1               2024-05-15 15:10:54   
  2           USCDB       EXC OML: FETYPE="USCDB", OBJNAME="PGW_PERIODTASK_SUMMARY", OML="select * from PGW_PERIODTASK_SUMMARY";   ONCE          NULL           0               2024-05-15 15:11:38   
  3           SUP-FE      STR CMPDB: FETYPE="SUP-FE", FDBTYPE=CUR, TABLENAME="SUID_DATA", FIELDNAME="SUID", KEYTYPE="SUID";        CYCLE         DAY            2               2024-05-15 15:12:03   
  8           USCDB       STR CMPDB: FETYPE="SUP-FE", FDBTYPE=CUR, TABLENAME="SUID_DATA", FIELDNAME="SUID", KEYTYPE="SUID";        ONCE          NULL           0               2024-05-15 14:42:42   

  Total count = 4

  There is together 1 report

  ---    END
  ```
- 查询“任务ID”为“1”的周期性任务。

  ```
  LST PERIODTASK: TASKID=1;
  ```

  ```
  %%LST PERIODTASK: TASKID=1;%%
  RETCODE = 0 操作成功

  <Task ID>   <FE type>   <MML command>                                                                                            <Task type>   <Cycle unit>   <Cycle value>   <Start time>          <Task description>
  1           SUP-FE      EXC OML: FETYPE="USCDB", OBJNAME="PGW_PERIODTASK_SUMMARY", OML="select * from PGW_PERIODTASK_SUMMARY";   CYCLE         HOUR           1               2024-05-15 15:10:54    

  Total count = 1

  There is together 1 report

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1的参数说明。

| 输出项名称            | 输出项解释                 |
|:-----------------|:----------------------|
| Task ID          | 用于返回周期性任务的任务ID。       |
| FE type          | 用于返回周期性任务的FE类型。       |
| MML command      | 用于返回添加周期性任务时指定的MML命令。 |
| Task type        | 用于返回周期性任务的任务类型。       |
| Cycle unit       | 用于返回周期性任务执行的周期单位。     |
| Cycle value      | 用于返回周期性任务执行的周期值。      |
| Start time       | 用于返回周期性任务执行的开始时间。     |
| Task description | 用于返回周期性任务的任务描述。       |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释            | 原因分析                          | 处理建议                                              |
|------:|:-----------------|:------------------------------|:--------------------------------------------------|
|  1004 | 无效的参数值。          | 输入的参数值不在其取值范围内或者输入的参数值不符合要求。  | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                  |
|  5072 | 该命令只能通过WebLMT接入。 | 通过Web LMT之外的方式访问PGW，执行此命令。    | 请通过Web LMT访问PGW执行该命令。                             |
|  5079 | 指定的业务类型不存在或未加载。  | 选择的“FE类型”参数指定的FE插件不存在或未加载。    | 在“USCDB MML命令”上执行LOD FEPLUG命令加载FE插件包后再执行本命令进行添加。  |
|  1006 | 没有权限执行此命令。       | 当前操作员没有操作权限。                  | 请使用超级管理员、ADMINISTRATOR级别的操作员或CUSTOM级别的操作员账号执行本命令。 |
|  5286 | 任务不存在。           | 系统不存在对应“任务ID”或对应“FE类型”的周期性任务。 | 执行本命令前，请确保待查询的周期性任务已添加。                           |