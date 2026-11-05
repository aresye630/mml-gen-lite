# 显示承载上下文相关的调试信息(DSP SMDBGINFO)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询和承载上下文相关的一些调试信息。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME    | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定SPU资源单元名称。该参数可以通过DSP RU命令查询。 取值范围：0~63位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MSTATE    | 主备状态   | 可选必选说明：可选参数 参数含义：该参数用于指定节点的主备状态。 取值范围：“MASTER(主用状态)”“SLAVE(备用状态)” 默认值：“MASTER(主用状态)”                                                                                                                                                                                                                                                                                                                                                                                                     |
| PROCNO    | 进程号    | 可选必选说明：必选参数 参数含义：该参数用于指定进程的序号。 取值范围：0～20 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| QRYTP     | 查询类型   | 可选必选说明：可选参数 参数含义：该参数用于指定查询的类型。 取值范围：0～4294967294 默认值：无  说明： 0表示查看部分消息的收发次数。1表示主/从进程（主-从状态必须设为主状态或者从状态）的PDP上下文数。100表示统计GTPU_SM_CREAT_RSP消息的各原因值次数。101表示统计GTPU_SM_UPDATE_RSP消息的各原因值次数。102表示统计GTPU_SM_DELETE_RSP消息的各原因值次数。103表示统计GTPU_SM_DATA_ERR_IND消息的各原因值次数。106表示统计系统收到的PGW/SGW故障消息以及记录故障信息清除时间和第一条故障信息产生的时间。110表示统计DNS查询失败和成功次数。120表示统计内部消息MM_SM_CTRL_REL_SM_REQ的各原因值次数。130表示查询内部消息SDB_SM_DEACTIVE_REQ的各原因值次数。140表示将异常统计点输出到LMT和系统日志。150表示查询哪些异常统计点开启了打印调试信息至系统日志的功能。                   |
| DBGTP     | 调试类型   | 可选必选说明：可选参数 参数含义：该参数用于指定调试的类型。 取值范围：0～4294967294 默认值：无  说明： 0表示将消息统计次数清零。10表示将异常统计点清零。如果第一个字符串（First String Value）携带了特定原因值，则将该特定原因值的异常统计点清零。 如果第一个字符串（First String Value）为空，则将全部的异常统计点清零。20表示关闭打印调试信息至系统日志的功能。如果第一个字符串（First String Value）携带了特定原因值，则不将该原因值的调试信息输出到系统日志。 如果第一个字符串（First String Value）为空，则关闭所有异常统计点的调试信息。21表示打开打印调试信息至系统日志的功能。如果第一个字符串（First String Value）携带了特定原因值，则将该原因值的调试信息输出到系统日志。 如果第一个字符串（First String Value）为空，则输出所有异常统计点的调试信息至系统日志。106表示清零PGW/SGW故障消息计数以及故障信息清除时间。 |
| VARINDEX  | 变量索引   | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：0～4294967294 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VARVALUE1 | 第一个变量值 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：0～4294967294 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VARVALUE2 | 第二个变量值 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：0～4294967294 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VARVALUE3 | 第三个变量值 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：0～4294967294 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VARVALUE4 | 第四个变量值 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：0～4294967294 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| STRVALUE1 | 第一个字符串 | 可选必选说明：可选参数 参数含义：输入字符串参数。 取值范围：1～127位字符串 默认值：无  说明： 结合调试类型为10、20、21功能一起使用。                                                                                                                                                                                                                                                                                                                                                                                                               |
| STRVALUE2 | 第二个字符串 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：1～127位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| STRVALUE3 | 第三个字符串 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：1～127位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| STRVALUE4 | 第四个字符串 | 可选必选说明：可选参数 参数含义：暂未使用。 取值范围：1～127位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |

#### 使用实例

1. 当Query Type为0时，显示部分消息的收发次数：

   DSP SMDBGINFO: RUNAME="USN\_SP\_RU\_0066", PROCNO=0, QRYTP=0;

   ```
   %%DSP SMDBGINFO: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=0;%%
   RETCODE = 0  操作成功。

   操作结果如下
   -------------------------
    消息                                    消息数量

    E_GTPC_SM_UPDATE_PDP_CONTEXT_RSP_TIMEOUT  4         
    PSM_ACTIVATE_PDP_CONTEXT_REQ_3G           8         
    PSM_ACTIVATE_PDP_CONTEXT_ACC_3G           4         
    PSM_ACTIVATE_PDP_CONTEXT_REJ_3G           1         
    GMT_CREATE_PDP_CONTEXT_REQ_V1             8         
    GMT_CREATE_PDP_CONTEXT_RSP _V1            5         
    GMT_UPDATE_PDP_CONTEXT_REQ_V1             4         
    GMT_DELETE_PDP_CONTEXT_REQ_V1             5         
    GMT_UPDATE_PDP_CONTEXT_REQ_V1_SM_SEND     4         
    GMT_DELETE_PDP_CONTEXT_REQ_V1_SM_SEND     5         
    SM_GTPU_CREATE_IND                        8         
    GTPU_SM_CREATE_RSP                        8         
    SM_GTPU_UPDATE_IND                        12        
    GTPU_SM_UPDATE_RSP                        12        
    SM_GTPU_DELETE_IND                        8         
    GTPU_SM_DELETE_RSP                        8         
    GTPU_SM_CREATE_RSP_SUCCESS                8         
    GTPU_SM_UPDATE_RSP_SUCCESS                12        
    GTPU_SM_DELETE_RSP_SUCCESS                8         
    SNSM_DEACTIVATE_IND                       4         
    SNSM_DEACTIVATE_RES                       4         
    SNSM_MODIFY_IND                           4         
    SNSM_MODIFY_RES                           4         
    MM_SM_CTRL_GET_CONTEXT_REQ                4         
    SM_MM_CTRL_GET_CONTEXT_RSP                4         
    MM_SM_CTRL_REDIRECT_BEARER_START_REQ      4         
    SM_MM_CTRL_REDIRECT_BEARER_START_RSP      4         
    MM_SM_CTRL_REDIRECT_BEARER_CMP_REQ        4         
    SM_MM_CTRL_REDIRECT_BEARER_CMP_RSP        4         
    MM_SM_CTRL_NEW_ADDR_REQ                   4         
    SM_MM_CTRL_NEW_ADDR_RSP                   4         
    MM_SM_CTRL_REL_CONN_NOTIFY                4         
    MM_SM_CTRL_REL_SM_REQ                     3         
    SM_MM_CTRL_REL_SM_RSP                     3         
    SM_MM_CTRL_LAST_ACTIVE                    8         
    USPU_UICP_RAB_ASS_REQ                     5         
    UICP_USPU_RAB_ASS_RSP                     4         
    USPU_UICP_SRNS_CONTEXT_REQ                4         
    UICP_USPU_SRNS_CONTEXT_RSP                4         
    E_SPU_DNS_REQUEST_MSG                     8         
    E_DNS_SPU_RESPONSE_MSG                    8         
    E_DNS_SPU_RESPONSE_MSG_SUCCESS            8         
    GTPC_SPU_VERSION_ERROR                    12        
   (结果个数 = 43)
   ```
2. 当Query Type为140时，将异常统计点输出到LMT和系统日志：

   DSP SMDBGINFO: RUNAME="USN\_SP\_RU\_0066", PROCNO=0, QRYTP=140;

   ```
   %%DSP SMDBGINFO: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=140;%%
   RETCODE = 0  操作成功。

   操作结果如下
   -------------------------
    消息                              消息数量

    E_SM_ERRSTAT_DEFAULT              14654     
    E_SM_ERRSTAT_ENTER                47049     
    E_SM_ERRSTAT_TIMEOUT              4         
    E_SM_ERRSTAT_CONFLICT             6         
    E_SM_ERRSTAT_GET_PDPCB_PTR_FAIL   90        
    E_SM_ERRSTAT_GET_USERCB_PTR_FAIL  25        
    E_SmLicense_limited_function      12        
    E_Sm_DT_License_Limited           8         
   (结果个数 = 8)
   ```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 消息      | 查询消息名称。 |
| 消息数量    | 查询消息数量。 |