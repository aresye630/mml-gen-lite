# 显示内部审计报告（DSP INATEX）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统内部设置的审计任务，包含设备内审计任务信息、服务内哈希审计信息和License审计信息。

## 注意事项

- 当天的审计任务完成后，若服务故障重启，则重新执行**DSP INATEX**查询时，返回的审计结果为初始状态结果。
- 若执行**DSP INATEX**查询得到审计任务已结束，报文中有审计数据为“NULL”的记录，则可能该服务在审计过程中出现过故障。请检查告警，查看CSP网元下是否存在“ALM-100001 进程故障告警”，如果存在，请参考告警进行处理；如果不存在，说明该服务当前无审计任务。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                       |
|:-----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESULTTYPE | 结果类型   | 用于请求系统按照哪种结果类型显示内部审计任务信息。 取值范围：CURRENT(当前审计任务信息)：查看当前审计任务。HISTORY(查看历史审计任务)：查看历史审计任务。 默认值：无。                                                               |
| ATTYPE     | 审计类型   | 用于标识审计类型。 取值范围：OTMODULE(设备内审计)：用于PES和DUS之间路由校验、PES内部PID之间相同接口类型会话的审计、HASH审计。HASH(哈希审计)：用于PES服务内哈希表的审计。LICENSE(LICENSE审计)：用于LICENSE审计。 默认值：OTMODULE(设备内审计)。 |

## 使用实例

1. 查询PES服务重启后，初始状态下的设备内审计任务信息。“结果类型”为“CURRENT(当前审计任务信息)”，“审计类型”为“OTMODULE(设备内审计)”。

   ```
   DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=OTMODULE;
   ```

   ```
   %%DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=OTMODULE;%%
   RETCODE = 0  操作成功

   结果如下
   ------------------------
   实例号		 审计任务状态  审计启动时间	 审计结束时间	 数据类型   总数          已审计数        已修复数

   4210095          NULL          NULL              NULL            USER       0             0               0                
   4210095          NULL          NULL              NULL            IP         0             0               0                
   4210095          NULL          NULL              NULL            SESSION    0             0               0                
   4218287          NULL          NULL              NULL            USER       0             0               0                
   4218287          NULL          NULL              NULL            IP         0             0               0                
   4218287          NULL          NULL              NULL            SESSION    0             0               0                
   (结果个数 = 6)

   ---    END
   ```
2. 查询系统当前哈希审计任务信息。“结果类型”为“CURRENT(当前审计任务信息)”，“审计类型”为“HASH(哈希审计)”。

   ```
   DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=HASH;
   ```

   ```
   %%DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=HASH;%%
   RETCODE = 0  操作成功

   结果如下
   ------------------------
   实例号		 审计任务状态  审计启动时间	 审计结束时间	 数据类型        总数          已审计数        已修复数

   4210095          NULL          NULL              NULL            DIAMSESSHASH    0             0               0                
   4210095          NULL          NULL              NULL            BLCSCBHASH      0             0               0                
   4210095          NULL          NULL              NULL            UPMUSERCBHASH   0             0               0                
   4210095          NULL          NULL              NULL            ALCSCBHASH      0             0               0                
   4210095          NULL          NULL              NULL            SMFSESSCBHASH   0             0               0                
   4210095          NULL          NULL              NULL            NGCHFHASH       0             0               0                
   4210095          NULL          NULL              NULL            NGAMSESSCBHASH  0             0               0                
   4210095          NULL          NULL              NULL            NGAMSUPIHASH    0             0               0                
   4210095          NULL          NULL              NULL            NGUESESSCBHASH  0             0               0                
   4210095          NULL          NULL              NULL            NGUESUPIHASH    0             0               0                
   4210095          NULL          NULL              NULL            NGAFSESSCBHASH  0             0               0                
   4210095          NULL          NULL              NULL            NGBINDHASH      0             0               0                
   4210095          NULL          NULL              NULL            MSISDNCBHASH    0             0               0                
   4218287          NULL          NULL              NULL            DIAMSESSHASH    0             0               0                
   4218287          NULL          NULL              NULL            BLCSCBHASH      0             0               0                
   4218287          NULL          NULL              NULL            UPMUSERCBHASH   0             0               0                
   4218287          NULL          NULL              NULL            ALCSCBHASH      0             0               0                
   4218287          NULL          NULL              NULL            SMFSESSCBHASH   0             0               0                
   4218287          NULL          NULL              NULL            NGCHFHASH       0             0               0                
   4218287          NULL          NULL              NULL            NGAMSESSCBHASH  0             0               0                
   4218287          NULL          NULL              NULL            NGAMSUPIHASH    0             0               0                
   4218287          NULL          NULL              NULL            NGUESESSCBHASH  0             0               0                
   4218287          NULL          NULL              NULL            NGUESUPIHASH    0             0               0                
   4218287          NULL          NULL              NULL            NGAFSESSCBHASH  0             0               0                
   4218287          NULL          NULL              NULL            NGBINDHASH      0             0               0                
   4218287          NULL          NULL              NULL            MSISDNCBHASH    0             0               0                
   (结果个数 = 26)

   ---    END
   ```
3. 查询系统当前的license审计结果。“结果类型”为“CURRENT(当前审计任务信息)”，“审计类型”为“LICENSE(LICENSE审计)”。

   ```
   DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=LICENSE;
   ```

   ```
   %%DSP INATEX: RESULTTYPE=CURRENT, ATTYPE=LICENSE;%%
   RETCODE = 0  操作成功

   结果如下
   ------------------------
   实例号		 审计任务状态  审计启动时间	 审计结束时间	 数据类型            总数          已审计数        已修复数  

   4210095          NULL          NULL              NULL            GXLICENSE           0             0               0                
   4210095          NULL          NULL              NULL            SDLICENSE           0             0               0                
   4210095          NULL          NULL              NULL            FOURTHGENLICENSE    0             0               0                
   4210095          NULL          NULL              NULL            RXLICENSE           0             0               0                
   4210095          NULL          NULL              NULL            REGRXLICENSE        0             0               0                
   4210095          NULL          NULL              NULL            SYLICENSE           0             0               0                
   4210095          NULL          NULL              NULL            EMBBLICENSE         0             0               0                
   4210095          NULL          NULL              NULL            RXVONRLICENSE       0             0               0                
   4210095          NULL          NULL              NULL            RXEPSFBLICENSE      0             0               0                
   4210095          NULL          NULL              NULL            RXVOLTELICENSE      0             0               0                
   4210095          NULL          NULL              NULL            N7LICENSE           0             0               0                
   4210095          NULL          NULL              NULL            N75GLICENSE         0             0               0                
   4210095          NULL          NULL              NULL            N74GLICENSE         0             0               0                
   4210095          NULL          NULL              NULL            N15AMPOLICYLICENSE  0             0               0                
   4210095          NULL          NULL              NULL            VONRDEFAULTLICENSE  0             0               0                
   4210095          NULL          NULL              NULL            SALICENSE           0             0               0                
   4210095          NULL          NULL              NULL            N28LICENSE          0             0               0                
   4210095          NULL          NULL              NULL            N5DATALICENSE       0             0               0                
   4210095          NULL          NULL              NULL            AMUELOGOLICENSE     0             0               0                
   4210095          NULL          NULL              NULL            AMRFSPLICENSE       0             0               0                
   4210095          NULL          NULL              NULL            N23LICENSE          0             0               0                
   4210095          NULL          NULL              NULL            RXWIFILICENSE       0             0               0                
   4210095          NULL          NULL              NULL            FWALICENSE          0             0               0                
   4218287          NULL          NULL              NULL            GXLICENSE           0             0               0                
   4218287          NULL          NULL              NULL            SDLICENSE           0             0               0                
   4218287          NULL          NULL              NULL            FOURTHGENLICENSE    0             0               0                
   4218287          NULL          NULL              NULL            RXLICENSE           0             0               0                
   4218287          NULL          NULL              NULL            REGRXLICENSE        0             0               0                
   4218287          NULL          NULL              NULL            SYLICENSE           0             0               0                
   4218287          NULL          NULL              NULL            EMBBLICENSE         0             0               0                
   4218287          NULL          NULL              NULL            RXVONRLICENSE       0             0               0                
   4218287          NULL          NULL              NULL            RXEPSFBLICENSE      0             0               0                
   4218287          NULL          NULL              NULL            RXVOLTELICENSE      0             0               0                
   4218287          NULL          NULL              NULL            N7LICENSE           0             0               0                
   4218287          NULL          NULL              NULL            N75GLICENSE         0             0               0                
   4218287          NULL          NULL              NULL            N74GLICENSE         0             0               0                
   4218287          NULL          NULL              NULL            N15AMPOLICYLICENSE  0             0               0                
   4218287          NULL          NULL              NULL            VONRDEFAULTLICENSE  0             0               0                
   4218287          NULL          NULL              NULL            SALICENSE           0             0               0                
   4218287          NULL          NULL              NULL            N28LICENSE          0             0               0                
   4218287          NULL          NULL              NULL            N5DATALICENSE       0             0               0                
   4218287          NULL          NULL              NULL            AMUELOGOLICENSE     0             0               0                
   4218287          NULL          NULL              NULL            AMRFSPLICENSE       0             0               0                
   4218287          NULL          NULL              NULL            N23LICENSE          0             0               0                
   4218287          NULL          NULL              NULL            RXWIFILICENSE       0             0               0                
   4218287          NULL          NULL              NULL            FWALICENSE          0             0               0                
   (结果个数 = 46)

   ---    END
   ```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                              |
|:--------|:-----------------------------------------------------------------------------------|
| 实例号     | 用于标识PES服务实例号。                                                                      |
| 审计任务状态  | 用于标识审计任务状态。 取值说明： NULL：服务状态异常，无审计任务信息。完成：审计任务完成。中断：审计任务中断。正在审计：审计正在执行。准备审计：准备启动审计。 |
| 审计启动时间  | 用于标识审计任务的启动时间。                                                                     |
| 审计结束时间  | 用于标识审计任务的结束时间。                                                                     |
| 数据类型    | 用于标识审计任务的数据类型。                                                                     |
| 总数      | 用于标识各项数据的总量。                                                                       |
| 已审计数    | 用于标识各项数据审计的总量。                                                                     |
| 已修复数    | 用于标识各项数据审计修复的总量。                                                                   |