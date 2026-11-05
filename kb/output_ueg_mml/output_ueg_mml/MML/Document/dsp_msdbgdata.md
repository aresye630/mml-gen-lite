# 查询调试信息(DSP MSDBGDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询调试信息。

- 若要查询“服务类型”为“HttpDisCtrlService(HttpDisCtrlService)” 或“UdmSubService(UdmSubService)”服务中本端实例与SCP/SEPP实例的关系信息，请输入“参数0”取值为“1”。
- 若要查询与指定“服务类型”相依赖的其他服务的关键信息，请输入“参数0”取值为“2”。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                              |
|:--------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST      | 服务类型   | 可选必选说明：必选参数 参数含义：用于指示系统查询哪个服务类型的调试信息。 取值范围： UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UdmAlbService(UdmAlbService)EnumService(EnumService) 默认值：无。 配置原则：无。 |
| MSINSID | 服务实例ID | 可选必选说明：必选参数 参数含义：用于指示系统按照服务实例ID来查询调试信息。 取值范围：长度不超过36位的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                         |
| PM0     | 参数0    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数0。 取值范围：0～1024 默认值：无。 配置原则：该参数取值为“1”时，表示查询“服务类型”取值为“HttpDisCtrlService(HttpDisCtrlService)” 或“UdmSubService(UdmSubService)”服务中本端实例与SCP/SEPP实例的关系信息。该参数取值为“2”时，表示查询与指定“服务类型”相依赖的其他服务的关键信息。                                                                                                       |
| PM1     | 参数1    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数1。 取值范围：0～1024 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                   |
| PM2     | 参数2    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数2。 取值范围：0～1024 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                   |
| PM3     | 参数3    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数3。 取值范围：0～1024 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                   |
| PM4     | 参数4    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数4。 取值范围：0～1024 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                   |
| PM5     | 参数5    | 可选必选说明：可选参数 参数含义：用于指定系统查询调试信息下发的参数5。 取值范围：0～1024 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                   |

## 使用实例

- 查询DCS、SUB（DCS SDK）内存中本端实例与SCP/SEPP实例的关系信息。

  ```
  DSP MSDBGDATA: ST=HttpDisCtrlService, MSINSID="11784646200630118209", PM0="1";
  ```

  ```
  DSP MSDBGDATA: ST=HttpDisCtrlService, MSINSID="11784646200630118209", PM0="1";
  RETCODE = 0  操作成功
  操作结果如下:
  -------------------------
  结果字符串

  Index: UDM-NFInstanceId: SCP-NFInstanceId: SEPP-NFInstanceId                                                          
  1: 11ffffff-11ff-1fff-ffff-ffffffffffff: 11111111-1111-1111-1111-111111111133: NULL                                  
  2: 11ffffff-11ff-1fff-ffff-ffffffffffff: 11111144-1111-1111-1111-111111111144: NULL       
  3: ffffffff-ffff-ffff-ffff-ffffffffffff: 11111111-1111-1111-1111-111111111111: 11111112-1112-1112-1112-111111111112
  (结果个数 = 4)

  ---    END
  ```
- 查询与指定“服务类型”相依赖的其他服务的关键信息。

  ```
  DSP MSDBGDATA: ST=UdmHttpService, MSINSID="18427528712221137851", PM0="2";
  ```

  ```
  %%DSP MSDBGDATA: ST=HttpDisCtrlService, MSINSID="18427546308635016124", PM0="2";%%
  RETCODE = 0  操作成功
  操作结果如下:
  -------------
  结果字符串                                                                                                                                                               
  Index: SrvName SrvInst SrvState SrvLabel                                                                                                                                 
  1 UdmHttpService 18427528712221113275 Ready {"ClientToken":"32000","LinkStatus":"AllReady","ProcessNO":"1","UdmHttpDead":"false","UdmTcpInstId":"18427581506026224571"}  
  2 UdmCcu 18427651887789530048 Ready {"ModuleNumber":"203","ProcessNO":"4","isControlCCU":"True"}                                                                         
  3 UdmAuthService 18427511115672992698 Ready {"ProcessNO":"0"}                                                                                                            
  (结果个数 = 4)
  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各输出项含义请参见表1的参数说明。

| 输出项名称                  | 输出结果解释                  |
|:-----------------------|:------------------------|
| 当“参数0”取值为“1”时，报文输出项说明。 | 当“参数0”取值为“1”时，报文输出项说明。  |
| Index                  | 本端实例与SCP/SEPP实例的关系信息的索引 |
| UDM-NFInstanceId       | 本端实例ID                  |
| SCP-NFInstanceId       | SCP实例ID                 |
| SEPP-NFInstanceId      | SEPP实例ID                |
| 当“参数0”取值为“2”时，报文输出项说明。 | 当“参数0”取值为“2”时，报文输出项说明。  |
| Index                  | 服务实例索引                  |
| SrvName                | 服务名称                    |
| SrvInst                | 服务实例ID                  |
| SrvState               | 服务状态                    |
| SrvLabel               | 服务标签                    |

命令执行异常，请联系华为技术支持处理。输出错误码说明如表1错误码列表所示。

|    错误码 | 错误码解释          | 原因分析               | 处理建议                                        |
|-------:|:---------------|:-------------------|:--------------------------------------------|
| 360144 | 调试任务参数错误。      | 参数输入有误，无此调试开关。     | 请通过DSP UDMSERVICE查询“服务类型”和“服务实例ID”，重新执行该命令。 |
| 360145 | 调试任务服务类型实例不存在。 | “服务实例ID”输入错误或者不存在。 | 请通过DSP UDMSERVICE查询“服务实例ID”，重新执行该命令。        |