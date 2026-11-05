# 查询批操作(CHK BATSTAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

本命令用于查询批操作状态。

## 注意事项

- “BEGINTIME”和“ENDTIME”必须同时指定或同时不指定。
- 如果没有参数被指定，将显示所有批操作的信息。

## 参数说明

| 参数标识      | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                       |
|:----------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TASKID    | 批操作任务ID  | 批操作任务号 取值范围：1～4294967295。 缺省值：无 说明：如果DETAIL为TRUE，此参数必选。                                                                                                                                                                                                                                                                                                    |
| OPNAME    | 操作员名称    | 操作员的名称 取值范围：不超过32位的字符串，由数字和字母组成，且首字符必须为字母。 缺省值：无 说明：可选参数                                                                                                                                                                                                                                                                                                   |
| BEGINTIME | 起始时间     | 起始时间 取值范围：格式为"YYYY&MM&DD&HH&MM&SS"的字符串。 缺省值：无 说明：该参数与“批操作任务ID”不能同时存在。                                                                                                                                                                                                                                                                                      |
| ENDTIME   | 结束时间     | 结束时间 取值范围： 格式为： "YYYY&MM&DD&HH&MM&SS"的字符串。 缺省值：无 说明：该参数与“批操作任务ID”不能同时存在。                                                                                                                                                                                                                                                                                   |
| STATE     | 执行状态     | 要查询的批操作的状态。 取值范围： READY：准备RUNNING：运行COMPLETED：完成ABORTED：中止PENDING：等待 UPLDFAIL：上传文件失败，导入批操作结果文件从负载PGW上传到主备PGW失败。DWLDING：下载文件中，导入文件正在从主备PGW下载到负载PGW中。DWLDFAIL：下载文件失败，导入文件从主备PGW下载到负载PGW失败。CFGFAIL：执行导入批操作BAT IMP命令时，参数“配置文件名”对应文件内容不合法。 缺省值：无                                                                                                                |
| DETAIL    | 是否提供详细信息 | 是否返回批操作的详细信息。 取值范围：TRUE/FALSE 缺省值：无。 说明：可选参数                                                                                                                                                                                                                                                                                                               |
| SAVEAS    | 保存文件名    | 保存查询结果的文件名。 取值范围：1～20位字符串，可由字母、数字或字符组成，字符不能包含“>”、“/”、“?”、“\”、“:”、“*”、“"”、“<”、“|”、“,”、“;”、“=”和“'”。 默认值：无。 说明： 如果指定“保存文件名”，命令执行结果保存在文件内，不在WebUI显示命令执行结果。操作员可以通过WebUI的文件下载功能获取该文件。 如果不指定“保存文件名”，且显示的记录超过250条，则在WebUI的显示最后的250条记录信息。 如果不指定“保存文件名”，且显示的记录不超过250条，则在WebUI显示所有记录信息。 当“是否提供详细信息”参数为“FALSE”时该参数不能存在。如果输入“保存文件名”和“批操作任务ID”参数，需同时输入“是否提供详细信息”为“TRUE”。 |
| TASKTYPE  | 查询任务类型   | 用于指定查询进度的任务类型。 取值范围： IMP：导入批操作任务 BAT：普通批操作任务 默认值：无。                                                                                                                                                                                                                                                                                                        |

## 使用实例

1. 查询所有批操作任务，不输入任何参数。

   ```
   CHK BATSTAT:;
   ```

   ```
   %%CHK BATSTAT:;%%
   RETCODE = 0 Operation is successful

   TASK ID = 218103809
   TASK ID = 218103810
   TASK ID = 218103811
   TASK ID = 218103812
   TASK ID = 218103815
   TASK ID = 218103816
   TASK ID = 218103817
   TASK ID = 218103818
   TASK ID = 218103819
   TASK ID = 218103820
   TASK ID = 218103821
   TASK ID = 218103822
   TASK ID = 218103823
   TASK ID = 218103824
   TASK ID = 218103825
   TASK ID = 218103826
   TASK ID = 218103827
   TASK ID = 218103828
   TASK ID = 218103829
   TASK ID = 218103830
   TASK ID = 218103831
   TASK ID = 218103832
   TASK ID = 218103833
   TASK ID = 218103834
   TASK ID = 218103835
   TASK ID = 218103836
   TASK ID = 218103837
   TASK ID = 218103838
   TASK ID = 218103839
   TASK ID = 218103840
   TASK ID = 218103841
   TASK ID = 218103842
   TASK ID = 218103843
   TASK ID = 218103844
   TASK ID = 218103845
   TASK ID = 218103846
   TASK ID = 218103847
   TASK ID = 218103848
   TASK ID = 218103849

   Total count = 39

   There is together 1 report

   ---    END
   ```
2. 查询“批操作任务ID”为“218103809”的批操作任务状态，不保存查询结果。

   ```
   CHK BATSTAT: TASKID=218103809, DETAIL=FALSE;
   ```

   ```
   %%CHK BATSTAT: TASKID=218103809, DETAIL=FALSE;%%
   RETCODE = 0 Operation is successful

   <TASK ID>   <HLR INDEX>   <OPERATOR NAME>                   <START TIME>         <END TIME>           <STATUS>   <TOTAL>     <SUCCESS>   <FAILURE>   <PROGRESS>   <RESTTIME>   <DB SUCCEED BUT NETWORK FAIL>  <MML CMD>
   218103809   1             admin                             2021-12-14 18:13:16  2021-12-14 18:13:16  COMPLETED  1           1           0           100%         00:00:00     0                              /*HWHandle=514*/BAT IMP: FETYPE="HSS9860", FILE="ims_data.txt";

   Total count = 1

   There is together 1 report

   ---    END
   ```