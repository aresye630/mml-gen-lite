# 强制停止校验(STP VRYNRFDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成业务呼损或系统严重过载甚至崩溃，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于在校验NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据以及校验NRFClient内存数据和NRF数据的过程中强制停止校验。

**说明** 

校验NRFClient内存数据或NRFClient SDK内存数据支持校验NRF信息、网元实例信息、网元服务信息、网元PLMN信息、网元S-Nssai信息、网元号段信息、网元信息和网元公共信息。

校验方式如下：

- 执行**VRY NRFDATA**命令手动校验。
- 由PeriodicVerificationSwitch(周期校验开关)与PeriodicVerificationNRFData(与NRF远端周期校验开关)软参控制的每天上午07时17分自动校验。

该命令使用场景如下：

- 在校验单个MML命令的过程中，支持校验的相关命令数据无法变更，若必须执行对应的命令，可执行该命令强制停止校验，执行对应的命令后，再次执行**VRY NRFDATA**进行校验。相关命令为：
  - **ADD UDMNRFINFO**、**MOD UDMNRFINFO**、**RMV UDMNRFINFO**
  - **ADD UDMNFSRV**、**MOD UDMNFSRV**、**RMV UDMNFSRV**
  - **ADD UDMNFINFO**、**MOD UDMNFINFO**、**RMV UDMNFINFO**
  - **ADD UDMNFSERVICE**、**MOD UDMNFSERVICE**、**RMV UDMNFSERVICE**
  - **ADD UDMNFPLMN**、**RMV UDMNFPLMN**
  - **ADD UDMNFSNSSAI**、**RMV UDMNFSNSSAI**
  - **ADD UDMNFRANGEINFO**、**RMV UDMNFRANGEINFO**
  - **ADD UDMNFCOMINFO**、**MOD UDMNFCOMINFO**、**RMV UDMNFCOMINFO**
- 由于异常情况导致系统负载较高，可执行该命令强制停止校验。

## 注意事项

执行该命令强制停止校验，会导致NRFClient内存数据或NRFClient SDK内存数据和CSP内存数据不一致、NRFClient内存数据和NRF数据不一致，导致大量业务失败。

## 参数说明

无。

## 使用实例

在校验NRFClient内存数据或NRFClient SDK内存数据的过程中，可强制停止校验。

```
STP VRYNRFDATA:;
```

```
%%STP VRYNRFDATA: CONFIRM=Y;%%
RETCODE = 0 操作成功

操作结果如下:
------------
微服务类型  微服务实例ID          校验类型  结果   
NRFClient   11806846920942295203  OMDATA    没有需要停止的校验任务 
NRFClient   11806846920942296215  NRFDATA   没有需要停止的校验任务 
AUSF        11807914104351228697  OMDATA    停止成功 
UdmSub      11808573897227241271  OMDATA    停止成功 
UdmSub      11808573897227129751  OMDATA    停止成功 
AUSF        11807914104351116205  OMDATA    停止成功 

(结果个数 = 6)

--- END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息，各参数含义请参见

**VRY NRFDATA**

命令的参数说明，表1列出的是未包含在

**VRY NRFDATA**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                            |
|:--------|:-------------------------------------------------|
| 结果      | 用于返回停止校验的停止结果： 没有需要停止的校验任务停止成功数据正在修复中，无法停止，请稍后再试 |