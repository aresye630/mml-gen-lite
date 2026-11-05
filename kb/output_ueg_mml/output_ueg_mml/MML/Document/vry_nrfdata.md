# 校验内存数据(VRY NRFDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行过程中相关MML无法运行，执行不当会造成业务呼损或系统严重过载甚至崩溃，因此执行该命令前，需要与华为技术支持确认后才可以实施。

本命令用于手动校验NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据的一致性以及NRFClient内存数据和NRF数据的一致性。支持校验NRF信息、网元实例信息、网元服务信息、网元PLMN信息、网元S-Nssai信息、网元号段信息、网元信息和网元公共信息。

日常维护过程中，为了便于NRFClient数据或NRFClient SDK数据周期性检查或者进行问题定位，可执行该命令校验NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据是否一致，以及校验NRFClient内存数据和远端NRF数据是否一致。

**说明** 

- 系统除了支持通过该命令进行手动校验之外，还可以通过命令**MOD UDMSOFTPARA**控制以下两个软参来设置是否每天上午07时17分进行OMDATA定时校验。
  - 通过“PeriodicVerificationSwitch”软参设置以下数据的定时校验：
    - 校验NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据的一致性。
    - 校验UdmSubService内存数据和CSP内存数据的一致性。
    - 校验UdmAuthService内存数据和CSP内存数据的一致性。
  - 通过“PeriodicVerificationNRFData”软参设置NRFClient内存数据与远端NRF数据一致性的定时校验。

  在“OMDATA”校验完成后，会在随机等待0~600秒（手动校验无需等待）后，启动NRFClient内存数据和NRF数据的一致性校验。
- 校验NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据一致性的过程大约持续30s，持续时间与配置数据量有关，数据越多校验时间越长。

## 注意事项

- 在校验单个UDM MML命令的过程中，该命令数据无法变更，若运行对应的命令，则提示“360155 该MML数据正在校验中，请稍后再试”。相关命令为**：**
  - **ADD UDMNRFINFO**、**MOD UDMNRFINFO**、**RMV UDMNRFINFO**
  - **ADD UDMNFSRV**、**MOD UDMNFSRV**、**RMV UDMNFSRV**
  - **ADD UDMNFINFO** 、**MOD UDMNFINFO**、**RMV UDMNFINFO**
  - **ADD UDMNFSERVICE**、**MOD UDMNFSERVICE**、**RMV UDMNFSERVICE**
  - **ADD UDMNFPLMN**、**RMV UDMNFPLMN**
  - **ADD UDMNFSNSSAI**、**RMV UDMNFSNSSAI**
  - **ADD UDMNFRANGEINFO**、**RMV UDMNFRANGEINFO**
  - **ADD UDMNFCOMINFO**、**MOD UDMNFCOMINFO**、**RMV UDMNFCOMINFO**
- 若执行该命令时，NRFClient内存数据或NRFClient SDK内存数据校验正在进行中，则提示“360153 校验正在进行中，请稍后再试”，需等待校验结束后才可执行该命令。
- 若校验出现NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据不一致，会上报ALM-18607 NRFClient内存数据不一致告警，并以CSP数据为准，按照CSP的数据重新刷新内存数据，刷新结束后，ALM-18607 NRFClient内存数据不一致告警自动恢复。校验数据被成功修复后，如果涉及NF配置数据变更，需要重新向NRF发送更新数据。
- 若校验出现NRFClient内存数据和远端NRF数据不一致，会上报ALM-18612 NRFClient与NRF数据不一致告警，**ADD UDMNFSRV**配置的“UPDATEFLAG”为“TRUE”时，系统向NRF发送全量更新请求，并等待更新结果，NRF全量更新成功时，ALM-18612 NRFClient与NRF数据不一致告警自动恢复。
- 在“PeriodicVerificationNRFData(与NRF远端周期校验开关)”软参关闭，且“PeriodicPushData(周期性推送全量数据开关)”软参开启情况下，校验开始时NRFClient会推送全量数据到NRF，确保数据一致性。

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                          |
|:--------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE    | 校验类型    | 可选必选说明：必选参数 参数含义：用于标识校验NRFClient内存数据的校验类型。 取值范围： OMDATA(OMDATA)：校验NRFClient内存数据或NRFClient SDK内存数据和CSP的内存数据。NRFDATA(NRFDATA)：校验NRFClient内存数据与远端NRF数据ALL(所有)：校验NRFClient内存数据或NRFClient SDK内存数据和CSP的内存数据，以及NRFClient内存数据和NRF数据。 默认值：无 配置原则：同一时间只能启动一种校验，若该参数为“ALL(ALL)”，则UDM会先校验NRFClient内存数据或NRFClient SDK内存数据和CSP的内存数据，再校验NRFClient内存数据与NRF数据。 |
| MSTYPE  | 微服务类型   | 可选必选说明：条件可选参数 参数含义：用于标识校验NRFClient内存数据或NRFClient SDK内存数据的微服务类型。 取值范围： ALL(ALL)：校验NRFClient、UdmSub和AUSF微服务类型和CSP内存数据的一致性。NRFClient(NRFClient)：校验NRFClient微服务类型和CSP内存数据的一致性。UdmSub(UdmSub)：校验UdmSub微服务类型和CSP内存数据的一致性。AUSF(AUSF)：校验AUSF微服务类型和CSP内存数据的一致性。 默认值：ALL(ALL) 配置原则：仅当“校验类型”为“OMDATA(OMDATA)”时，该参数有效。                                    |
| MSINSID | 微服务实例ID | 可选必选说明：条件可选参数 参数含义：用于标识校验NRFClient内存数据或NRFClient SDK内存数据的微服务实例ID，通过执行命令DSP UDMSERVICE来查询微服务实例ID。在NRFClient、UdmSub和AUSF微服务类型的实例中，只有NRFClient的服务实例ID有主备之分。 取值范围：长度不超过63位的字符串。 默认值：无 配置原则：仅当“微服务类型”取值为“NRFClient(NRFClient)”、“UdmSub(UdmSub)”或者“AUSF(AUSF)”时，该参数有效。                                                                              |

## 使用实例

为了日常维护过程中，便于对NRFClient内存数据或NRFClient SDK内存数据和CSP的内存数据进行校验，设置“校验类型”为“OMDATA”，“微服务类型”为“ALL”。

```
VRY NRFDATA: TYPE=OMDATA, MSTYPE=ALL;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                | 原因分析                                                 | 处理建议                                               |
|-------:|:---------------------|:-----------------------------------------------------|:---------------------------------------------------|
| 360145 | 校验任务指定服务类型对应的实例ID不存在 | 指定的服务类型对应的“微服务实例ID”不存在。                              | 请使用命令DSP UDMSERVICE查询“微服务实例ID”并输入正确的实例ID。          |
| 360153 | 校验正在进行中，请稍后再试        | NRFClient内存数据或NRFClient SDK内存数据校验正在进行中，校验结束后才可执行该命令。 | 使用命令DSP VRYNRFDATA查询校验状态，确保“校验状态”为“校验已结束”，则可执行该命令。 |
| 360173 | 非主模块无法执行该命令          | 输入的“微服务实例ID”为“NRFClient(NRFClient)”的备实例ID。           | 请使用命令DSP UDMSERVICE查询NRFClient微服务主备实例ID并输入正确的实例ID。 |
| 360193 | NRF倒换中，无法启动校验        | 远端NRF正在倒换中，无法启动数据校验。                                 | 请使用命令DSP UDMNFSRV查询NRF倒换结果，确保NRF倒换结束，则可执行该命令。      |