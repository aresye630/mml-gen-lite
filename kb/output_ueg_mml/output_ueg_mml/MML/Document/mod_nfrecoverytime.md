# 修改网元实例恢复时间(MOD NFRECOVERYTIME)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成全网设备过载、链路拥塞、CPU负荷过载等现象，因此执行该命令前，需要与华为技术支持确认后才可以实施。

当需要对端网元重新注册时，需要使用此命令修改网元实例恢复时间。

当执行**ADD UDMNFSRV**命令配置时，将会按照当前时间自动生成recoveryTime，recoveryTime参数值支持通过本命令修改。

该命令当前仅在物联网5G用户数据割接时使用，其业务原理如图1所示。

**图1** recoveryTime变更流程原理

详细流程如图2所示。

**图2** recoveryTime变更流程

1. 旧IWF/UDM向新UDM进行用户数据割接。
2. 旧IWF/UDM执行该命令修改网元实例恢复时间，命令执行完毕后系统自动向NRF发送Nnrf\_NFManagement\_NFUpdate Request消息，携带recoveryTime信息。
3. NRF向旧IWF/UDM返回Nnrf\_NFManagement\_NFUpdate Response响应消息。
4. NRF收到旧IWF/UDM发送的recoveryTime变更消息后，查看已订阅旧IWF/UDM状态的AMF/SMF POOL，并向AMF/SMF POOL发送Nnrf\_NFManagement\_NFStatusNotify Request消息，其中nfProfile信元中携带recoveryTime信息，知会AMF/SMF POOL旧IWF/UDM的recoveryTime变更。
5. AMF/SMF POOL向NRF返回Nnrf\_NFManagement\_NFStatusNotify Response响应消息。
6. AMF/SMF POOL同时扫描已经注册到旧IWF/UDM上的用户，如果用户号段未被割接到新UDM上，则AMF/SMF POOL针对这些用户号段向旧IWF/UDM重新发起注册，获取签约数据。
7. 如果用户号段已经被割接到新UDM上时，AMF/SMF POOL需要向NRF发送Nnrf\_NFDiscovery\_NFDiscover Request重新进行服务发现。
8. NRF向AMF/SMF POOL返回Nnrf\_NFDiscovery\_NFDiscover Response响应消息。
9. AMF/SMF POOL针对已经被割接到新UDM上的用户号段向新UDM发起注册，获取签约数据。

## 注意事项

- 本命令配置的“恢复时间”不能早于**ADD UDMNFSRV**命令添加时的系统时间。
- 该命令不允许进行批操作。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                     |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSNAME    | 网元实例名称 | 可选必选说明：必选参数 参数含义：用于标识待修改“恢复时间”的网元实例名称。 取值范围：长度不超过32位的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无 配置原则：该参数需要先由ADD UDMNFSRV命令定义后，然后才能在此处引用。                                        |
| RECOVERYTIME | 恢复时间   | 可选必选说明：必选参数 参数含义：用于标识某个网元实例修改后的恢复时间。 取值范围：YYYY&MM&DD&HH&MM&SS 默认值：无 配置原则： 该参数配置的时间中“年”“月”“日”“时”“分”“秒”使用“&”连接。通过LST UDMNFSRV命令查询“恢复时间”参数的取值，确保本命令配置的“恢复时间”不能早于查询出的“恢复时间”。 |

## 使用实例

修改“网元实例名称”为“udm-application-001”的“恢复时间”为“2018&12&30&23&20&50”：

```
MOD NFRECOVERYTIME: NFINSNAME="udm-application-001", RECOVERYTIME=2018&12&30&23&20&50;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释        | 原因分析                               | 处理建议                                                           |
|-------:|:-------------|:-----------------------------------|:---------------------------------------------------------------|
|    505 | 当前操作的配置数据不存在 | 待修改的“网元实例名称”不存在。                   | 通过LST UDMNFSRV命令查询已存在的“网元实例名称”后重新输入。                           |
| 360041 | 参数值不合法       | 输入的“恢复时间”早于ADD UDMNFSRV命令配置时的系统时间。 | 通过LST UDMNFSRV命令查询“恢复时间”参数的取值，重新执行本命令，确保配置的“恢复时间”晚于查询出的“恢复时间”。 |