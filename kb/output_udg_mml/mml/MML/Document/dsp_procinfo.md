# 查询进程部署信息（DSP PROCINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统中的进程部署信息。

## 注意事项

无。

## 参数说明

| 参数标识                | 参数名称   | 参数说明                                                                                                                                        |
|:--------------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| PROCINFO_MEID       | 网元ID   | 可选必选说明：可选参数。 参数含义：当前需要查询的网元ID；若不输入，则表示查询所有。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                           |
| PROCINFO_QUERY_TYPE | 查询类型   | 可选必选说明：可选参数。 参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。 取值范围： byProcessType(进程类型)byContainerType(容器类型)byNode(节点名称) 默认值：无。 配置原则：无。                     |
| PROCINFO_PROC_TYPE  | 进程类型   | 可选必选说明：该参数在“查询类型”取值为“byProcessType(进程类型)”时为必选参数。 参数含义：用于指示按照进程类型查询部署信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：可通过DSP PROCINFO命令查询进程类型。   |
| PROCINFO_CNT_TYPE   | 容器类型   | 可选必选说明：该参数在“查询类型”取值为“byContainerType(容器类型)”时为必选参数。 参数含义：用于指示按照容器类型查询部署信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：可通过DSP PROCINFO命令查询容器类型。 |
| PROCINFO_NODE_NAME  | 节点名称   | 可选必选说明：该参数在“查询类型”取值为“byNode(节点名称)”时为必选参数。 参数含义：用于指示按照节点名称查询部署信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：可通过DSP PROCINFO命令查询节点名称。          |

## 使用实例

1. 根据进程类型查询进程部署信息。

   ```
   %%DSP PROCINFO: PROCINFO_MEID=0, PROCINFO_QUERY_TYPE=byProcessType, PROCINFO_PROC_TYPE="CSPNetConfGW";%%
   RETCODE = 0  执行成功
   操作结果如下：
   -------------- 
   网元ID  进程类型      节点名称         Pod名称                          容器类型                进程编号   进程标识                           进程ID   
   0       CSPNetConfGW  172.16.0.1       cspnetconfgw-857ccfd9c5-cqqt7    cspnetconfgw-software   110        0_CSPNetConfGW_192.168.0.1_40333   nodeName:172.16.0.1/podName:cspnetconfgw-857ccfd9****
   0       CSPNetConfGW  172.16.0.2       cspnetconfgw-857ccfd9c5-pmmsk    cspnetconfgw-software   109        0_CSPNetConfGW_192.168.0.2_40293   nodeName:172.16.0.2/podName:cspnetconfgw-857ccfd9**** 
   (结果个数 = 2)  
   ---    END
   ```
2. 根据容器类型查询进程部署信息。

   ```
   %%DSP PROCINFO: PROCINFO_MEID=0, PROCINFO_QUERY_TYPE=byContainerType, PROCINFO_CNT_TYPE="cspnetconfgw-software";%% 
   RETCODE = 0  执行成功 
   操作结果如下：
   -------------- 
   网元ID  进程类型      节点名称         Pod名称                          容器类型                进程编号   进程标识                           进程ID
   0       CSPNetConfGW  172.16.0.1       cspnetconfgw-857ccfd9c5-cqqt7    cspnetconfgw-software   110        0_CSPNetConfGW_192.168.0.1_40333   nodeName:172.16.0.1/podName:cspnetconfgw-857ccfd9****
   0       CSPNetConfGW  172.16.0.2       cspnetconfgw-857ccfd9c5-pmmsk    cspnetconfgw-software   109        0_CSPNetConfGW_192.168.0.2_40293   nodeName:172.16.0.2/podName:cspnetconfgw-857ccfd9****
   (结果个数 = 2)  
   ---    END
   ```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1 输出项说明所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

| 输出项名称   | 输出项解释                                  |
|:--------|:---------------------------------------|
| 网元ID    | 进程所在网元ID，即应用ID。                        |
| 进程类型    | 进程名称。                                  |
| 节点名称    | 进程所在的节点名称。                             |
| Pod名称   | 进程所在的Pod名称。                            |
| 容器类型    | 进程所在的容器类型。                             |
| 进程编号    | 进程的编号。                                 |
| 进程标识    | 由网元ID、进程类型、服务IP和服务transport端口号组装的进程标识。 |
| 进程ID    | 由节点名称、Pod名称、容器类型、进程类型和进程编号组装的进程ID。     |

|   错误码 | 消息解释             | 原因分析                   | 处理建议           |
|------:|:-----------------|:-----------------------|:---------------|
| 20002 | 查询mk失败           | ModuleKeeper服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。           | 修改查询条件后重试。     |