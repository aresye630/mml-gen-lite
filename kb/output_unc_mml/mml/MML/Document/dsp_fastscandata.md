# 显示快速扫描任务信息（DSP FASTSCANDATA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示快速扫描任务信息。

## 注意事项

最多输出100个DS的快速扫描任务详细信息，最后一行输出所有DS的汇总记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                       |
|:----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TASKTYPE  | 扫描任务类型 | 可选必选说明：必选参数  参数含义：该参数用于指定扫描任务类型。  数据来源：本端规划 取值范围： UPF_DEACTIVE（UPF去活扫描任务）SBC_FAULT（SBC故障扫描任务）UPF_CHECK（UPF核查扫描任务）  默认值：无  配置原则：无                                                                                                                                                                           |
| CONDITION | 查询条件   | 可选必选说明：可选参数  参数含义：该参数用于表示扫描任务数据查询条件。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：  不输入CONDITION时，查询指定TASKTYPE的所有任务信息。TASKTYPE为UPF_DEACTIVE或UPF_CHECK时，需要查询特定UPF实例的任务信息时，CONDITION填写UPF实例ID，UPF实例ID不区分大小写。TASKTYPE为SBC_FAULT时，需要查询特定UPF实例关联特定PCSCF地址的任务信息时，CONDITION填写UPF实例ID+PCSCFIP，UPF实例ID不区分大小写。 |

## 使用实例

- 查询系统中TASKTYPE=UPF\_DEACTIVE的快速扫描任务信息：

  ```
  %%DSP FASTSCANDATA: TASKTYPE=UPF_DEACTIVE;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件     Token编号   扫描任务数据个数

  UPF去活扫描任务   NULL         9           10
  UPF去活扫描任务   NULL         5           10
  UPF去活扫描任务   NULL         2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE=UPF\_DEACTIVE，CONDITION=“upf\_instance\_1”（对应UPF实例ID为“upf\_instance\_1”）的快速扫描任务信息：

  ```
  %%DSP FASTSCANDATA: TASKTYPE=UPF_DEACTIVE, CONDITION="upf_instance_1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件         Token编号   扫描任务数据个数

  UPF去活扫描任务   upf_instance_1   9           10
  UPF去活扫描任务   upf_instance_1   5           10
  UPF去活扫描任务   upf_instance_1   2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE为SBC\_FAULT的快速扫描任务信息：

  ```
  %%DSP FASTSCANDATA: TASKTYPE=SBC_FAULT;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件     Token编号   扫描任务数据个数

  SBC故障扫描任务   NULL         9           10
  SBC故障扫描任务   NULL         5           10
  SBC故障扫描任务   NULL         2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE为SBC\_FAULT，CONDITION为"upf\_instance\_1+1.2.3.4"（对应UPF实例ID为"upf\_instance\_1"，PCSCFID为"1.2.3.4"）的快速扫描任务信息：

  ```
  %%DSP FASTSCANDATA: TASKTYPE=SBC_FAULT, CONDITION="upf_instance_1+1.2.3.4";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件                 Token编号   扫描任务数据个数

  SBC故障扫描任务   upf_instance_1+1.2.3.4   9           10
  SBC故障扫描任务   upf_instance_1+1.2.3.4   5           10
  SBC故障扫描任务   upf_instance_1+1.2.3.4   2           20
  (结果个数 = 3)

  ---    END
  ```

## 输出结果说明

| 输出项名称    | 输出项解释                                                                                |
|:---------|:-------------------------------------------------------------------------------------|
| 扫描任务类型   | 该参数用于指定扫描任务类型。 取值说明： UPF_DEACTIVE（UPF去活扫描任务）SBC_FAULT（SBC故障扫描任务）UPF_CHECK（UPF核查扫描任务） |
| 查询条件     | 该参数用于表示扫描任务数据查询条件。                                                                   |
| Token编号  | 该参数用于标识Token的编号。最后一行输出的Token参数含义为汇总所得的Token数量。                                       |
| 扫描任务数据个数 | 该参数用于标识扫描任务数据个数，例如会话数等。                                                              |