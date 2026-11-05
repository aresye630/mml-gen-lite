# 微服务软件调测（STR MSSFTD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

**执行本命令会影响业务，需要慎重使用。必须在华为技术支持人员的指导下操作。**

本命令为异步任务，命令结果“操作成功”只代表命令下发到模块成功，不代表命令在模块中的执行结果成功。

本命令为专家维护命令，用于向服务发送软件调试命令。

## 注意事项

不同的模块有不同的命令码，不同的命令码也有不同的参数，如果命令码和参数输入不准确，不会出现错误提示，具体可参考使用实例。

## 参数说明

| 参数标识                | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                   |
|:--------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSSFTD_KEY_TYPE     | 标识类型   | 可选必选参数说明：必选参数。 参数含义：用于区别用进程或进程类型方式下发命令。 取值范围： “byProcess(进程)”：用于使用进程方式下发命令。“byProcessType(进程类型)”：用于使用进程类型方式下发命令。 默认值：byProcess(进程)。 配置原则：无。                                                                                                                                                                                                                                                            |
| MSSFTD_PROCESS_KEY  | 进程标识   | 可选必选说明：该参数在“标识类型”配置为“byProcess(进程)”时为条件必选参数。 参数含义：用于唯一标识指定的服务进程。 取值范围：字符串类型，输入长度范围为7~512。 默认值：无。 配置原则：操作员可以使用DSP PROCINFO命令查询。                                                                                                                                                                                                                                                                         |
| MSSFTD_MEID         | 网元ID   | 可选必选参数说明：该参数在“标识类型”配置为“byProcessType(进程类型)”时为条件必选参数。 参数含义：用于下发至对应网元ID的服务。 取值范围：0～65535。 默认值：无。 配置原则：操作员可以使用DSP PROCINFO命令查询。                                                                                                                                                                                                                                                                           |
| MSSFTD_PROCESS_TYPE | 进程类型   | 可选必选参数说明：该参数在“标识类型”配置为“byProcessType(进程类型)”时为条件必选参数。 参数含义：用于下发至对应进程类型的服务。 取值范围：字符串类型，输入长度范围为2~256。 默认值：无。 配置原则：操作员可以使用DSP PROCINFO命令查询。                                                                                                                                                                                                                                                                |
| MSSFTD_MODULE_ID    | 模块ID   | 可选必选说明：必选参数。 参数含义：用于标识微服务软件调试命令下发的目的模块号。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                         |
| MSSFTD_CMD          | 命令码    | 可选必选说明：必选参数。 参数含义：用于标识微服务软件调试命令下发到模块的命令码。 取值范围：整数类型，取值范围1~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                        |
| MSSFTD_PARAMETER1   | 参数1    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数1。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则： 模块ID为201，命令码为11时，参数1为SNMP心跳检测开关，取值为0表示开启，其它取值表示关闭。当模块ID（MSSFTD_MODULE_ID）为101，命令码（MSSFTD_CMD）为1的时候，功能为设置HAService管理实例心跳超时时间，该参数为设置超时时间的大小，可设置的参数取值范围为7~60秒。当模块ID（MSSFTD MODULE ID）为2，命令码（MSSFTD CMD）为2的时候，功能为打开CSP C微服务内存泄漏检测开关，该参数为内存泄漏检测超时时间，单位为分钟，超过此时间会自动关闭，如果不填或者填0默认为10分钟。此命令不支持重复开启，会导致失败，可以通过开关状态变更规避，具体原因可查看日志错误码。 |
| MSSFTD_PARAMETER2   | 参数2    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数2。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER3   | 参数3    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数3。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER4   | 参数4    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数4。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER5   | 参数5    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数5。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER6   | 参数6    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数6。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER7   | 参数7    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数7。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER8   | 参数8    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数8。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER9   | 参数9    | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数9。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                           |
| MSSFTD_PARAMETER10  | 参数10   | 可选必选说明：可选参数。 参数含义：用于标识微服务软件调试命令下发的参数10。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                          |

## 使用实例

- 生成C服务的黑匣子或生成Go服务的pprof或生成Java服务的黑匣子。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="12_CSPCCommonServiceDemo_172.16.0.1_40045", MSSFTD_MODULE_ID=1, MSSFTD_CMD=4;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="ccommon", MSSFTD_MODULE_ID=1, MSSFTD_CMD=4;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-获取OS/JVM信息。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=1;%% 
  RETCODE = 0  操作成功  

  ---    END

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=1;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

- Java服务JVM调试命令-获取类加载信息。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=2, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=2, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-设置类加载详情开关。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=2, MSSFTD_PARAMETER1=2, MSSFTD_PARAMETER2=1;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=2, MSSFTD_PARAMETER1=2, MSSFTD_PARAMETER2=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-dump栈。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=3, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=3, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-检查是否存在死锁。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=3, MSSFTD_PARAMETER1=2;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=3, MSSFTD_PARAMETER1=2;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-查询内存分配情况。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=4, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=4, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- Java服务JVM调试命令-dump堆。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CMDProxy_172.16.0.1_40045", MSSFTD_MODULE_ID=100, MSSFTD_CMD=4, MSSFTD_PARAMETER1=2;%%
  RETCODE = 0  操作成功

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CMDProxy", MSSFTD_MODULE_ID=100, MSSFTD_CMD=4, MSSFTD_PARAMETER1=2;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- C、Go、Java服务发起手动全量订阅推送。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CSPHAService_172.16.0.1_40045", MSSFTD_MODULE_ID=2, MSSFTD_CMD=1;%% 
  RETCODE = 0  操作成功 

  ---    END 

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_OpsAgent_172.16.0.1_40045", MSSFTD_MODULE_ID=2, MSSFTD_CMD=1;%% 
  RETCODE = 0  操作成功

  ---    END

  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_ModuleKeeper_172.16.0.1_40045", MSSFTD_MODULE_ID=2, MSSFTD_CMD=1;%%
   RETCODE = 0  操作成功

  ---    END
  ```

- 设置HAService管理实例心跳超时时间（心跳超时时长即参数MSSFTD\_PARAMETER1的取值范围为7~60秒）。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="HAService", MSSFTD_MODULE_ID=101, MSSFTD_CMD=1, MSSFTD_PARAMETER1=50;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- HAService关闭动态修改心跳超时时长。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="HAService", MSSFTD_MODULE_ID=101, MSSFTD_CMD=2;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 边缘普通域场景OpsAgent打开本地配置开关。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CSPOpsAgent", MSSFTD_MODULE_ID=3, MSSFTD_CMD=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 边缘普通域场景OpsAgent关闭本地配置开关。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CSPOpsAgent", MSSFTD_MODULE_ID=3, MSSFTD_CMD=2;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 生成Go服务的pprof时支持设置cpu采集时长。参数1用于设置时长，未填写或填为0时默认为7，时长最大为600最小为7，单位为秒，超过此范围MML执行报错。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CSPAgentManager", MSSFTD_MODULE_ID=1, MSSFTD_CMD=4, MSSFTD_PARAMETER1=20;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

- 生成Go服务的pprof时支持设置是否清理反射信息的缓存。参数2用于设置是否清理，默认0不清理，1：清理，2不清理，大于2时MML执行报错。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CSPAgentManager", MSSFTD_MODULE_ID=1, MSSFTD_CMD=4, MSSFTD_PARAMETER2=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 配置C服务Dopra资源异常时是否上报告警的开关。“参数1”用于配置异常类型，当前共有7种类型，分别为内存破坏(1)、内存重复释放(4)、消息包破坏(8)、消息包泄露(16)、消息单元过载(32)、消息包重复释放(64)、消息包申请失败(128)，可以对单一的类型配置开关，也可对多种类型配置开关，配置多种类型时对应类型的取值进行或运算即可（例如要同时配置内存重复释放和消息包破坏的开关，“参数1”传入12）；“参数2”用于控制开关状态，默认0代表关闭，1：开启。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=10, MSSFTD_PROCESS_TYPE="cclient", MSSFTD_MODULE_ID=1, MSSFTD_CMD=5, MSSFTD_PARAMETER1=12, MSSFTD_PARAMETER2=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 告警“发生时间”转换开关，开启后告警“发生时间”修改为实际“发生时间”+“闪断周期”。其中“参数1”表示是否开启告警“发生时间”转换，“1”表示开启，“0”表示关闭。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="FMService", MSSFTD_MODULE_ID=100, MSSFTD_CMD=601, MSSFTD_PARAMETER1=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="FMService", MSSFTD_MODULE_ID=100, MSSFTD_CMD=601, MSSFTD_PARAMETER1=0;%%
  RETCODE = 0  操作成功 

  ---    END
  ```

- CSP C微服务打开内存泄漏检测开关。“参数1”用于表示内存泄漏检测超时时间，单位为分钟，超过该时间检测功能会关闭，如果不填或者填0默认为10分钟。此命令不支持重复开启，会导致失败，可以通过开关状态变更规避，具体原因可查看日志错误码。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CSPHAService_172.16.0.1_40045", MSSFTD_MODULE_ID=2, MSSFTD_CMD=2, MSSFTD_PARAMETER1=50;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

- CSP C微服务关闭内存泄漏检测开关，关闭之后会生成dump文件，针对生成的dump文件会解析生成parse文件，此命令不支持重复关闭，会导致失败，可以通过开关状态变更规避，具体原因可查看日志错误码。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CSPHAService_172.16.0.1_40045", MSSFTD_MODULE_ID=2, MSSFTD_CMD=3;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

核查节点资源是否一致，执行后会对节点的CPU和内存资源与VNFD配置规格进行核查，如果核查不一致则上报ALM-135632虚机资源核查不一致告警。其中

“进程类型”

需要填写NRSMaster主实例进程类型。

```
%%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="0_CSPNRSMaster_xxx.xxx.xxx.xxx_40001", MSSFTD_MODULE_ID=401, MSSFTD_CMD=1;%% 
RETCODE = 0  操作成功  
---    END
```

| VNFD配置参数   | 参数描述     |
|:-----------|:---------|
| num_cpus   | CPU规格配置项 |
| mem_size   | 内存规格配置项  |

**说明** 

获取NRSMaster主实例信息：

选择“应用配置 > 服务治理 ”，搜索框中输入“NRSMaster”，点击查询，在列表中展开NRSMaster实例，查看属性列json字符串中HaStatus字段值是否为“Active”，如果是则表示当前实例为NRSMaster主实例。

- 设置IDRService功能逃生开关。要求以“进程类型”的方式下发。“参数1”表示要设置开关的网元ID。“参数2”表示要设置的开关状态，0：关闭，1：开启。“参数3”表示逃生开关控制的范围，取值只能选择1：采集模块，3：检测模块，4：诊断模块，5：恢复模块。当开关状态设置为关时，系统会把“参数3”设置的模块及之后的业务全部停止。当开关状态设置为开时，系统恢复原状态，此时“参数3”不生效。该命令只能用来设置适配了故障诊断恢复能力的网元开关，即“参数1”只能填写适配了故障诊断恢复能力的网元ID，否则会下发失败。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="CSPIDRService", MSSFTD_MODULE_ID=5, MSSFTD_CMD=1, MSSFTD_PARAMETER1=319, MSSFTD_PARAMETER2=1, MSSFTD_PARAMETER3=1;%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 开启InferMindFramework显存泄漏检测开关，“参数1”用于表示显存泄漏检测超时时间，单位为秒，超过该时间检测功能会关闭，如果不填或者填0默认为1分钟。“参数2”用于表示单个采样文件的大小上限，单位为M，如果不填或者填0默认为2M。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="10_ccommon_172.18.0.61_40042", MSSFTD_MODULE_ID=501, MSSFTD_CMD=1, MSSFTD_PARAMETER1=10, MSSFTD_PARAMETER2=20;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```

- 关闭InferMindFramework显存泄漏检测开关，关闭之后会生成采样文件，针对生成的采样文件会生成解析文件。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcess, MSSFTD_PROCESS_KEY="10_ccommon_172.18.0.61_40042", MSSFTD_MODULE_ID=501, MSSFTD_CMD=2;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```

- 模块ID为201，命令码为11时，参数1为SNMP心跳检测开关，0表示开启，其它表示关闭。

  ```
  %%STR MSSFTD: MSSFTD_KEY_TYPE=byProcessType, MSSFTD_MEID=0, MSSFTD_PROCESS_TYPE="SNMP", MSSFTD_MODULE_ID=201, MSSFTD_CMD=11, MSSFTD_PARAMETER1=1;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。

命令执行异常，请联系华为技术支持处理。输出结果说明如表2所示。

|   错误码 | 消息解释   | 原因分析           | 处理建议        |
|------:|:-------|:---------------|:------------|
| 20023 | 操作失败。  | 执行微服务软件调试命令失败。 | 联系华为技术支持处理。 |