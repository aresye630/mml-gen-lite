# 设置容器资源阈值（SET CNTRESTHD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置容器的资源告警上报、清除阈值，CPU突变检测阈值和检测间隔，容器网络亚健康资源检测。

## 注意事项

- 告警阈值会持久化写入到Gauss数据库中，各容器阈值更新会有一定的延迟，可通过**DSP CNTRESSTAT**命令查看。
- 本命令若按照“容器类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“容器类型”的配置。

- 该命令系统初始值参数设置如下：

| 参数名称           | 初始值   |
|:---------------|:------|
| 网络亚健康告警开关      | on    |
| 单链路丢包率阈值(%)    | 2.0   |
| 网络亚健康告警上报阈值(%) | 70    |
| 网络亚健康告警清除阈值(%) | 30    |
| 网络亚健康响应阈值(ms)  | 200   |

## 参数说明

| 参数标识                            | 参数名称           | 参数说明                                                                                                                                                                                                                                                                       |
|:--------------------------------|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SETCNTTHD_RES_NAME              | 资源名称           | 可选必选说明：必选参数。 参数含义：用于指示系统当前设置的资源名称。 取值范围： cpu(CPU)memory(内存)net(网络)disk(磁盘) 默认值：无。 配置原则：无。                                                                                                                                                                                  |
| SETCNTTHD_RES_CPU               | CPU阈值类型        | 可选必选说明：该参数在“资源名称”取值为“cpu(CPU)”时为必选参数。 参数含义：用于指示系统当前设置的CPU阈值类型。 取值范围： cpu_usage(cpu告警阈值)cpu_change(cpu突变阈值) 默认值：无。 配置原则：无。                                                                                                                                                  |
| SETCNTTHD_RES_DISK              | DISK阈值类型       | 可选必选说明：该参数在“资源名称”取值为“disk(磁盘)”时为必选参数。 参数含义：用于指示系统当前设置的disk阈值类型。 取值范围： disk_usage(disk告警阈值)inode_usage(inode告警阈值) 默认值：无。 配置原则：无。                                                                                                                                            |
| SETCNTTHD_MEID                  | 网元ID           | 可选必选说明：该参数在“资源名称”取值为“memory(内存)”时为必选参数，在“CPU阈值类型”取值为“cpu_usage(cpu告警阈值)”时为必选参数；或在“资源名称”取值为“disk(磁盘)”且在“DISK阈值类型”取值为“disk_usage(disk告警阈值)”或“inode_usage(inode告警阈值)”时为必选参数。 参数含义：当前需要设置告警阈值的网元ID，即应用ID。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                |
| SETCNTTHD_GENERATE_SWITCH       | 开关             | 可选必选说明：该参数在“CPU阈值类型”取值为“cpu_change(cpu突变阈值)”时为必选参数。 参数含义：CPU突变检测是否开启。 取值范围： on(ON)off(OFF) 默认值：无。 配置原则：无。                                                                                                                                                                  |
| SETCNTTHD_GENERATE_TH           | 阈值(%)          | 可选必选说明：该参数在“开关”取值为“on(ON)”时为必选参数。 参数含义：当前需要设置的CPU检测阈值，单位为百分比。 取值范围：整数类型，取值范围3~100。 默认值：无。 配置原则：无。                                                                                                                                                                          |
| SETCNTTHD_GENERATE_INTERVAL     | CPU突变检测间隔(s)   | 可选必选说明：该参数在“开关”取值为“on(ON)”时为必选参数。 参数含义：当前需要设置的CPU突变检测时间间隔，单位为秒。 取值范围：整数类型，取值范围3~60。 默认值：无。 配置原则：无。                                                                                                                                                                         |
| SETCNTTHD_ALARM_GENERATE_TH     | 告警上报阈值(%)      | 可选必选说明：该参数在“资源名称”取值为“memory(内存)”时为必选参数，在“资源名称”取值为“cpu(CPU)”且在"CPU阈值类型"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在“资源名称”取值为“disk(磁盘)”且在“DISK阈值类型”取值为“disk_usage(disk告警阈值)”或“inode_usage(inode告警阈值)”时为必选参数。 参数含义：用于指示系统当前设置的告警上报阈值。 取值范围：整数类型，取值范围 2~100。 默认值： 无。 配置原则：告警上报阈值应大于告警清除阈值。 |
| SETCNTTHD_ALARM_CLEAR_TH        | 告警清除阈值(%)      | 可选必选说明：该参数在“资源名称”取值为“memory(内存)”时为必选参数，在“资源名称”取值为“cpu(CPU)”且在"CPU阈值类型"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在“资源名称”取值为“disk(磁盘)”且在“DISK阈值类型”取值为“disk_usage(disk告警阈值)”或“inode_usage(inode告警阈值)”时为必选参数。 参数含义：用于指示系统当前设置的告警清除阈值。 取值范围：整数类型，取值范围 1~99。 默认值： 无。 配置原则：告警清除阈值应小于告警上报阈值。  |
| SETCNTTHD_ALARM_TYPE            | 阈值设置类型         | 可选必选说明：该参数在“资源名称”取值为“memory(内存)”时为必选参数，在“资源名称”取值为“cpu(CPU)”且在"CPU阈值类型"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在“资源名称”取值为“disk(磁盘)”且在“DISK阈值类型”取值为“disk_usage(disk告警阈值)”或“inode_usage(inode告警阈值)”时为必选参数。 参数含义：用于指示系统当前设置的阈值类型。 取值范围： byME(网元级)byContainerType(容器类型) 默认值：无。 配置原则：无。   |
| SETCNTTHD_CNT_TYPE              | 容器类型           | 可选必选说明：该参数在“阈值设置类型”取值为“byContainerType(容器类型)”时为必选参数。 参数含义：用于指示系统按照容器类型设置告警阈值。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP CNTINFO命令查询容器类型。                                                                                                                              |
| SETCNTTHD_NETSUBHEALTH          | 网络亚健康资源检测      | 可选必选说明：该参数在“资源名称”取值为“net(网络)”时为必选参数。 参数含义：用于指示当前设置的网络亚健康类型。 取值范围：netsubhealth(网络亚健康) 默认值：无。 配置原则：无。                                                                                                                                                                        |
| SETCNTTHD_GENERATE_NET_SWITCH   | 网络亚健康告警开关      | 可选必选说明：该参数在“网络亚健康资源检测”取值为“netsubhealth(网络亚健康)”时为必选参数。 参数含义：用于指示网络亚健康告警是否上报。 取值范围： on(ON)off(OFF) 默认值：无。 配置原则：无。                                                                                                                                                            |
| SETCNTTHD_PACKET_LOST_NET_TH    | 单链路丢包率阈值(%)    | 可选必选说明：该参数在“网络亚健康告警开关”取值为“on(ON)”时为必选参数。 参数含义：用于指示每条链路的丢包阈值。 取值范围：字符串类型，取值范围 0~99。 默认值：无。 配置原则：无。                                                                                                                                                                          |
| SETCNTTHD_ALARM_GENERATE_NET_TH | 网络亚健康告警上报阈值(%) | 可选必选说明：该参数在“网络亚健康告警开关”取值为“on(ON)”时为必选参数。 参数含义：用于指示网络亚健康告警上报的阈值。 取值范围：整数类型，取值范围 1~100。 默认值：无。 配置原则：告警清除阈值应小于告警上报阈值。                                                                                                                                                         |
| SETCNTTHD_ALARM_CLEAR_NET_TH    | 网络亚健康告警清除阈值(%) | 可选必选说明：该参数在“网络亚健康告警开关”取值为“on(ON)”时为必选参数。 参数含义：用于指示网络亚健康告警清除的阈值。 取值范围：整数类型，取值范围 0~99。 默认值：无。 配置原则：告警清除阈值应小于告警上报阈值。                                                                                                                                                          |
| SETCNTTHD_NETSUBHEALTH_RESP_TH  | 网络亚健康响应阈值(ms)  | 可选必选说明：该参数在“网络亚健康告警开关”取值为“on(ON)”时为必选参数。 参数含义：用于指示网络亚健康响应的阈值。 取值范围：整数类型，取值范围 5~20000。 默认值：无。 配置原则：无。                                                                                                                                                                       |

## 使用实例

1. 按照网元设置容器告警上报、清除阈值。

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=memory, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=80, SETCNTTHD_ALARM_CLEAR_TH=65, SETCNTTHD_ALARM_TYPE=byME;%% 
   RETCODE = 0  操作成功    
   操作结果  =  SUCCESS 
   (结果个数 = 1)  
   ---    END
   ```

2. 按照容器类型设置容器告警上报、清除阈值。

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=memory, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=80, SETCNTTHD_ALARM_CLEAR_TH=65, SETCNTTHD_ALARM_TYPE=byContainerType, SETCNTTHD_CNT_TYPE="cspopsagent-software";%% 
   RETCODE = 0  执行成功    
   操作结果  =  SUCCESS 
   (结果个数 = 1)  
   ---    END
   ```

3. 设置CPU检测阈值。

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=cpu, SETCNTTHD_RES_CPU=cpu_change, SETCNTTHD_GENERATE_SWITCH=on, SETCNTTHD_GENERATE_TH=60, SETCNTTHD_GENERATE_INTERVAL=18;%% 
   RETCODE = 0  操作成功    
   操作结果  =  SUCCESS 
   (结果个数 = 1)  
   ---    END
   ```

4. 设置容器网络检测阈值。

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=net, SETCNTTHD_NETSUBHEALTH=netsubhealth, SETCNTTHD_GENERATE_NET_SWITCH=on, SETCNTTHD_PACKET_LOST_NET_TH="1.0", SETCNTTHD_ALARM_GENERATE_NET_TH=19, SETCNTTHD_ALARM_CLEAR_NET_TH=9, SETCNTTHD_NETSUBHEALTH_RESP_TH=333;%%
   RETCODE = 0  操作成功
   操作结果  =  SUCCESS
   (结果个数 = 1)
   ---    END
   ```

5. 按网元ID设置磁盘分区使用量disk\_usage上报告警和清除告警的阈值

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=disk, SETCNTTHD_RES_DISK=disk_usage, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=90, SETCNTTHD_ALARM_CLEAR_TH=85, SETCNTTHD_ALARM_TYPE=byME;%% 
   RETCODE = 0  操作成功    
   操作结果  =  SUCCESS 
   (结果个数 = 1)  
   ---    END
   ```
6. 按容器类型设置磁盘inode的使用量inode\_usage上报告警和清除告警的阈值

   ```
   %%SET CNTRESTHD: SETCNTTHD_RES_NAME=disk, SETCNTTHD_RES_DISK=inode_usage, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=90, SETCNTTHD_ALARM_CLEAR_TH=85, SETCNTTHD_ALARM_TYPE=byContainerType, SETCNTTHD_CNT_TYPE="fileserver-software";%% 
   RETCODE = 0  操作成功    
   操作结果  =  SUCCESS 
   (结果个数 = 1)  
   ---    END
   ```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1 输出项说明所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 操作结果    | 阈值是否设置成功。 |

|    错误码 | 消息解释                   | 原因分析                  | 处理建议           |
|-------:|:-----------------------|:----------------------|:---------------|
|  20010 | gauss服务状态不正确           | Gauss服务故障或网络异常。       | 重试或联系华为技术支持处理。 |
|  20020 | 该网元不存在                 | 输入了不存在的网元ID。          | 修改对应字段后重试。     |
|  20021 | 告警阈值不合法，恢复阈值应小于告警阈值    | 告警清除阈值应小于告警上报阈值。      | 修改对应字段后重试。     |
|  20022 | 无法修改该服务的告警阈值           | 未查询到该服务在线信息或者不支持此项设置。 | 修改对应字段后重试。     |
| 102200 | 此场景不支持                 | 当前场景不支持此命令。           | 无。             |
|  20023 | 单链路丢包率阈值超过范围(0.0~99.0) | 丢包阈值设置超过限制。           | 修改对应字段后重试。     |