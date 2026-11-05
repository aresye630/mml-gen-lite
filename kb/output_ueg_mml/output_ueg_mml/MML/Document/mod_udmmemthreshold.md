# 修改UDM服务内存告警阈值(MOD UDMMEMTHRESHOLD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于修改UDM服务内存告警阈值。UDM在检测到服务内存占用达到阈值后需要上报“ALM-18901 微服务内存过载”告警，防止单个服务内存过大而导致整个系统复位。

## 注意事项

无。

## 参数说明

| 参数标识              | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:------------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST                | 服务类型   | 可选必选说明：必选参数 参数含义：用于标识服务类型。 取值范围：UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmSubServiceIWF(UdmSubServiceIWF)UdmAuthService(UdmAuthService)UdmAlbService(UdmAlbService)EnumService(EnumService) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                     |
| MEMTHRESHOLDVALUE | 内存阈值   | 可选必选说明：必选参数 参数含义：用于标识服务内存告警阈值。 取值范围：400～65535 默认值：无。 系统初始设置值：系统初始化时给每个服务预置一条数据，系统初始设置值如下所示。 当“服务类型”参数为“UdmTcpService(UdmTcpService)”：1024当“服务类型”参数为“UdmHttpService(UdmHttpService)”: 2048当“服务类型”参数为“UdmAppCtrlService(UdmAppCtrlService)”: 800当“服务类型”参数为“NRFClient(NRFClient)”: 2048当“服务类型”参数为“HttpDisCtrlService(HttpDisCtrlService)”: 900当“服务类型”参数为“UdmSubService(UdmSubService)”: 4608当“服务类型”参数为“UdmSubServiceIWF(UdmSubServiceIWF)”: 4608当“服务类型”参数为“UdmAuthService(UdmAuthService)”: 1536当“服务类型”参数为“UdmAlbService(UdmAlbService)”：2048当“服务类型”参数为“EnumService(EnumService)”：1536 配置原则：无。 |

## 使用实例

在维护场景中，修改UDM服务内存告警阈值，“服务类型”为“UdmTcpService(UdmTcpService)”，“内存阈值”为“2048”：

```
MOD UDMMEMTHRESHOLD: ST=UdmTcpService, MEMTHRESHOLDVALUE=2048;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。