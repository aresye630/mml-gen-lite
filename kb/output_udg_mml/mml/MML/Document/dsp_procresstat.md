# 查询进程资源信息（DSP PROCRESSTAT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询进程的资源信息。

## 注意事项

无。

## 参数说明

| 参数标识                   | 参数名称   | 参数说明                                                                                                                                         |
|:-----------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| DSPPROCSTAT_MEID       | 网元ID   | 可选必选说明：必选参数。 参数含义：当前需要查询的网元ID，即应用ID。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                   |
| DSPPROCSTAT_RES_NAME   | 资源名称   | 可选必选说明：必选参数。 参数含义：用于指示系统当前查询的资源名称。 取值范围： cpu(CPU)memory(内存)thread(线程)fd(文件句柄) 默认值：无。 配置原则：当“资源名称”为“memory(内存)”时，该命令查询的内存信息不包含静态大页内存。         |
| DSPPROCSTAT_QUERY_TYPE | 查询类型   | 可选必选说明：可选参数。 参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。 取值范围： byProcessID(进程ID)byProcessType(进程类型)byContainerType(容器类型)byNode(节点名称) 默认值：无。 配置原则：无。     |
| DSPPROCSTAT_PROC_ID    | 进程ID   | 可选必选说明：该参数在“查询类型”取值为“byProcessID(进程ID)”时为必选参数。 参数含义：用于指示系统按照进程ID查询资源信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP PROCINFO命令查询进程ID。     |
| DSPPROCSTAT_PROC_TYPE  | 进程类型   | 可选必选说明：该参数在“查询类型”取值为“byProcessType(进程类型)”时为必选参数。 参数含义：用于指示系统按照进程类型查询资源信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP PROCINFO命令查询进程类型。   |
| DSPPROCSTAT_CNT_TYPE   | 容器类型   | 可选必选说明：该参数在“查询类型”取值为“byContainerType(容器类型)”时为必选参数。 参数含义：用于指示系统按照容器类型查询资源信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP PROCINFO命令查询容器类型。 |
| DSPPROCSTAT_NODE_NAME  | 节点名称   | 可选必选说明：该参数在“查询类型”取值为“byNode(节点名称)”时为必选参数。 参数含义：用于指示系统按照节点名称查询资源信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP PROCINFO命令查询节点名称。          |

## 使用实例

1. 根据资源名称查询所有进程的资源信息。

   ```
   %%DSP PROCRESSTAT: DSPPROCSTAT_MEID=0, DSPPROCSTAT_RES_NAME=cpu;%%
   RETCODE = 0  执行成功
   操作结果如下：
   --------------
   网元ID  进程类型      配额     使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  进程ID
   0       PatchMgr      200.00%  0.40%   0.20%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-phr75/containerType:patchmgr-software****
   0       CSPMTCenter   200.00%  0.00%   0.00%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-6ff5c59b6c-2qcqx/containerType:cspmtcenter****
   0       CSPNetConfGW  60.00%   0.20%   0.33%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspnetconfgw-5b74fbfdf9-6hhxf/containerType:cspnetconf****
   0       CSPMTCenter   60.00%   0.20%   0.34%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-6ff5c59b6c-6pfvn/containerType:cspmtcenter****
   0       CSPNetConfGW  150.00%  0.40%   0.27%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspnetconfgw-5b74fbfdf9-vtz9z/containerType:cspnetconf****
   0       PatchMgr      150.00%  0.40%   0.27%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-59kwj/containerType:patchmgr-softw****
   (结果个数 = 6)
   ---    END
   ```

2. 根据进程类型查询进程资源信息。

   ```
   %%DSP PROCRESSTAT: DSPPROCSTAT_MEID=0, DSPPROCSTAT_RES_NAME=cpu, DSPPROCSTAT_QUERY_TYPE=byProcessType, DSPPROCSTAT_PROC_TYPE="PatchMgr";%%
   RETCODE = 0  执行成功
   操作结果如下：
   --------------
   网元ID  进程类型       配额      使用量  使用率   告警开关  告警上报阈值(%)  告警清除阈值(%)  进程ID
   0       PatchMgr       200.00%   0.40%   0.20%    on        90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-phr75/containerType:patchmgr-software/process:****   
   0       PatchMgr       150.00%   0.40%   0.27%    on        90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-59kwj/containerType:patchmgr-software/process:****  
   (结果个数 = 2)
   ---    END
   ```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1 输出项说明所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

| 输出项名称     | 输出项解释                                        |
|:----------|:---------------------------------------------|
| 网元ID      | 进程所在网元ID，即应用ID。                              |
| 进程类型      | 进程名称。                                        |
| 配额        | 进程资源使用限额。                                    |
| 使用量       | 进程资源使用总量。                                    |
| 使用率       | 进程资源使用率。                                     |
| 告警开关      | 进程资源阈值告警开关。 on：表示超过阈值后上报告警。off：表示超过阈值后不上报告警。 |
| 告警上报阈值(%) | 进程资源上报告警阈值，显示方式为百分比。                         |
| 告警清除阈值(%) | 进程资源清除告警阈值，显示方式为百分比。                         |
| 进程ID      | 进程的唯一标识ID。                                   |

|   错误码 | 消息解释             | 原因分析                   | 处理建议           |
|------:|:-----------------|:-----------------------|:---------------|
| 20002 | 查询mk失败           | ModuleKeeper服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20005 | 查询OpsAgent失败     | OpsAgent服务故障或网络异常。     | 重试或联系华为技术支持处理。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。           | 修改查询条件后重试。     |