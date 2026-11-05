# 查询备份恢复状态(DSP DB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护命令，用于请求系统显示批量备份/恢复的状态。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                       |
|:------------|:-------|:---------------------------------------------------------------------------|
| SERVICETYPE | 业务类型   | 用于请求系统显示哪种业务类型的备份/恢复状态信息；若不输入，则表示所有的业务类型。                                  |
| LOCINFO     | 位置信息   | 用于请求系统显示哪种位置信息的备份/恢复状态信息；若不输入，则表示查询本局内存数据的备份/恢复状态。                         |
| LOCID       | 位置标识   | 仅当本命令中的“位置信息”参数选择为“Remote”时该参数有效，用于请求系统显示哪个远端局点的备份/恢复状态信息；若不输入，则表示所有的远端局点。 |

## 使用实例

1. 查询所有批量备份/恢复的状态：

   ```
   DSP DB:;
   ```

   ```
   %%DSP DB:;%%
   RETCODE = 0 操作成功

   <Location ID> <Service type> <Type>       <Cluster ID> <Cluster type> <Module ID> <State>        <Start Time>          <End Time>            <Total Num> <Success Num>
   5             USCDB          BKP COMMAND  1            DRU            1060        TASK FINISH    2020-09-18 08:09:45   2020-09-18 08:09:47   NULL        NULL
   5             USCDB          BKP COMMAND  1            DRU            1061        TASK FINISH    2020-09-18 08:09:45   2020-09-18 08:09:48   NULL        NULL
   5             SUP-FE         RCV COMMAND  1073         DRU            1073        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   3           2
   5             SUP-FE         RCV COMMAND  1073         DRU            1074        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1077         DRU            1077        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1077         DRU            1078        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1081         DRU            1081        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1081         DRU            1082        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1097         DSU            1097        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1097         DSU            1098        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1101         DSU            1101        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   2           2
   5             SUP-FE         RCV COMMAND  1101         DSU            1102        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0

   Total count = 12

   There is together 1 report

   --- END
   ```
2. 查询“业务类型”为“SUP-FE”的状态：

   ```
   DSP DB: SERVICETYPE="SUP-FE";
   ```

   ```
   %%DSP DB:;%%
   RETCODE = 0 操作成功

   <Location ID> <Service type> <Type>       <Cluster ID> <Cluster type> <Module ID> <State>        <Start Time>          <End Time>            <Total Num> <Success Num>
   5             SUP-FE         RCV COMMAND  1073         DRU            1073        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   3           2
   5             SUP-FE         RCV COMMAND  1073         DRU            1074        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1077         DRU            1077        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1077         DRU            1078        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1081         DRU            1081        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1081         DRU            1082        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1097         DSU            1097        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1097         DSU            1098        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0
   5             SUP-FE         RCV COMMAND  1101         DSU            1101        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   2           2
   5             SUP-FE         RCV COMMAND  1101         DSU            1102        TASK FINISH    2020-09-18 08:09:14   2020-09-18 08:09:14   0           0

   Total count = 10

   There is together 1 report

   --- END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各输出项含义请参见表1。

| 输出项名称        | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location ID  | 用于表示备份/恢复局点的位置标识，即Location标识。                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Service type | 用于表示节点的业务类型。                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Type         | 用于表示当前备份/恢复类型： TIMER：定时备份。 BKP COMMAND：BKP DB命令备份。 RCV COMMAND：RCV DB命令恢复。                                                                                                                                                                                                                                                                                                                                                                                 |
| Cluster ID   | 用于表示节点所在Cluster的标识。                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Cluster type | 用于表示节点所在Cluster的类型： DRU(DRU) DSU(DSU)                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Module ID    | 用于表示DRU/DSU的模块号。                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| State        | 用于表示节点是当前的任务状态： NOBACKUP：无备份任务 BACKUPING：节点备份中 BACKUP FINISH：节点备份完成 BACKUP FAIL：节点备份失败 SENDING TO DPU：发送给DPU中 SEND TO DPU FINISH：发送给DPU完成 SEND TO DPU FAIL：发送给DPU失败 UPLOADING TO THIRD PARTY SPACE：上传第三方服务器中 UPLOAD TO THIRD PARTY SPACE FINISH：上传第三方服务器完成 UPLOAD TO THIRD PARTY SPACE FAIL：传第三方服务器失败 TASK FINISH：任务完成 TASK ABNORMAL：任务异常 TASK TIMEOUT：任务超时 RECOVERING：节点恢复中RECOVERY FINISH：节点恢复完成RECOVERY FAIL：节点恢复失败RECOVERY ABORT：节点恢复中被执行STP RCVDB停止任务 |
| Start Time   | 用于表示最近一次任务起始时间，如果没有开始，则用NULL表示。                                                                                                                                                                                                                                                                                                                                                                                                                            |
| End Time     | 用于表示最近一次任务结束时间，如果没有结束或者超时，则用NULL表示。                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Total Num    | 当“Type”取值为“RCV COMMAND”时，该参数有效。否则用NULL表示。 对于全局DRU模块：用于表示指定待恢复的用户总数。对于DSU模块：用于表示指定实际查询成功的待恢复的用户总数。 说明：DSU模块实际获取“Total Num”之和等于全局DRU模块实际获取的“Success Num”。                                                                                                                                                                                                                                                                                                    |
| Success Num  | 当“Type”取值为“RCV COMMAND”时，该参数有效。否则用NULL表示。 对于全局DRU模块：用于表示实际查询成功的用户总数。对于DSU模块：用于表示实际恢复成功的用户总数。                                                                                                                                                                                                                                                                                                                                                               |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                           | 原因分析                                           | 处理建议                                                                                                                                          |
|------:|:--------------------------------|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
|  5079 | 指定的业务类型不存在或未加载。                 | 输入的“业务类型”参数指定的业务类型不存在或未加载。                     | 在“USCDB MML命令”界面执行LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即“业务类型”。 若“业务类型”加载成功，请在执行该命令时输入正确的服务类型名称。 若“业务类型”加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。 |
|  5115 | 部分模块状态异常，命令无法执行。                | 输入的“业务类型”参数对应业务类型的DMA模块异常。                     | 执行命令前请确保输入的“业务类型”参数对应业务类型的DMA模块正常。模块状态可以通过DSP MODULE命令查询。                                                                                     |
|  5116 | 存在操作失败模块。                       | 命令下发到DMA\DRU\DSU模块时，部分和全部模块操作失败。               | 请联系华为技术支持处理。                                                                                                                                  |
|  5117 | 参数取值无效：当前未对接属于容灾关系的USCDB类型远端局点。 | 输入的“位置信息”参数为“Remote”时，未配置对接属于容灾关系的USCDB类型远端局点。 | 输入的“位置信息”参数为“Remote”时，请确保已配置对接属于容灾关系的USCDB类型远端局点。已配置对接属于容灾关系的USCDB类型远端局点可以通过LST RLOCATION命令查询。                                                |
|  5118 | 参数取值无效：LOCID指定的局点未配置。           | 输入的“位置标识”参数对应的局点未配置。                           | 请确保“位置标识”参数对应的局点已配置。已配置对接的远端局点可以通过LST RLOCATION命令查询。                                                                                          |