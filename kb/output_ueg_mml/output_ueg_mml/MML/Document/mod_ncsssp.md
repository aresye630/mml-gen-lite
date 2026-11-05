# 修改NRF客户端服务系统软参(MOD NCSSSP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会导致系统异常，影响业务处理，需联系华为技术支持确认后再执行。

该命令为配置类命令，用于修改NCS系统软件参数的配置信息。

## 注意事项

- 在缺省的情况下，系统在初始化的时候已经预置了软参数据表中的全部数据。
- 操作员应使用默认值。如果操作员确实需要修改软件参数，请联系华为技术服务工程师处理，禁止随意修改。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPN    | 参数名    | 可选必选说明：必选参数 参数含义：标识软件参数名称，用于指定需要对哪一类软参数据记录的参数进行修改。 取值范围： VRM_NRFAUTOSWAPSWITCH(NRF自动倒换开关)VRM_NFDATAPRIORITY(网元数据优先级)VRM_ACCESSTOKENREQ(Token请求控制开关)VRM_REQTOKENBEFORE(提前重新申请Token时间)VRM_DISCOVERMSGSPEED(NF发现消息的发送速度)VRM_REVNRFMSGSPEED(接收NRF通知消息的速度)VRM_NRFMAPNFSERVICE(NRF注册时使用nfServiceList)VRM_NRFMERGENUMBERRANGE(NRF注册时进行号段合并)VRM_HTTPLINKDOWNPING(HTTP链路故障时发送Ping)VRM_NRFREGISTERSWITCH(NRF注册开关)VRM_NRFREGISTERINTERVAL(NRF注册时间间隔）VRM_NRFAUTOVRYSWITCH(NRF自动校验开关)VRM_MULTIPCFLOGICINSTSW(PCF多逻辑实例开关)VRM_ACCESSTOKENPLMNLISTSW(AccessToken授权消息支持requesterPlmnList开关)VRM_NWDAFTACMERGESW（NWDAF对端TAC合并开关） 详细信息请参考产品手册的“UPCF软件参数 > NCS系统软参”。 默认值：无。 配置原则：无。  说明： VRM_NFDATAPRIORITY(网元数据优先级)软参在该版本已经废弃。 |
| SPV    | 参数值    | 可选必选说明：必选参数 参数含义：标识软件参数的值，此处取值应在软件参数的取值范围内取值。 取值范围：0-2147483647。 详细信息请参考产品手册的“UPCF软件参数 > NCS系统软参”。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

当NCS切换到备用NRF后，主用NRF故障后恢复正常，NCS仍使用低优先级的NRF。检测到高优先级NRF恢复后，可以自动倒换该NRF。设置“参数名”为“VRM\_NRFAUTOSWAPSWITCH(NRF自动倒换开关)”，“参数值”软参设置为“1”。

```
MOD NCSSSP: SPN=VRM_NRFAUTOSWAPSWITCH, SPV=1;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                                          | 原因分析                                                                      | 处理建议                                                                                          |
|------:|:-----------------------------------------------|:--------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| 54524 | 参数取值无效：参数VRM_NRFAUTOSWAPSWITCH的取值范围是0或者1。      | 输入参数VRM_NRFAUTOSWAPSWITCH的取值不在取值范围内。                                      | 重新输入VRM_NRFAUTOSWAPSWITCH取值，并保证取值为0-1。                                                        |
| 53510 | 参数取值无效：参数VRM_ACCESSTOKENREQ的取值范围是0-3。          | 输入参数VRM_ACCESSTOKENREQ的取值不在取值范围内。                                         | 重新输入VRM_ACCESSTOKENREQ取值，并保证取值为0-3。                                                           |
| 54542 | 参数取值无效：参数VRM_REQTOKENBEFORE的取值范围是0-1800。       | 输入参数VRM_REQTOKENBEFORE的取值不在取值范围内。                                         | 重新输入VRM_REQTOKENBEFORE取值，并保证取值为0-1800。                                                        |
| 53731 | 参数取值无效：参数VRM_DISCOVERMSGSPEED的取值范围是0-500。      | 输入参数VRM_DISCOVERMSGSPEED的取值不在取值范围内。                                       | 重新输入VRM_DISCOVERMSGSPEED取值，并保证取值为0-500。                                                       |
| 53732 | 参数取值无效：参数VRM_REVNRFMSGSPEED的取值范围是0-500。        | 输入参数VRM_REVNRFMSGSPEED的取值不在取值范围内。                                         | 重新输入VRM_REVNRFMSGSPEED取值，并保证取值为0-500。                                                         |
| 53734 | 参数取值无效：参数VRM_NRFMAPNFSERVICE的取值范围是0或者1。        | 输入参数VRM_NRFMAPNFSERVICE的取值不在取值范围内。                                        | 重新输入VRM_NRFMAPNFSERVICE取值，并保证取值为0-1。                                                          |
| 53735 | 参数取值无效：参数VRM_NRFMERGENUMBERRANGE的取值范围是0或者1。    | 输入参数VRM_NRFMERGENUMBERRANGE的取值不在取值范围内。                                    | 重新输入VRM_NRFMERGENUMBERRANGE取值，并保证取值为0-1。                                                      |
| 53764 | 参数取值无效：参数VRM_HTTPLINKDOWNPING的取值范围是0或者1。       | 输入参数VRM_HTTPLINKDOWNPING的取值不在取值范围内。                                       | 重新输入VRM_HTTPLINKDOWNPING取值，并保证取值为0-1。                                                         |
| 53771 | 参数取值无效：参数VRM_NRFREGISTERSWITCH的取值范围是0或1。       | 输入参数VRM_NRFREGISTERSWITCH的取值不在取值范围内。                                      | 重新输入VRM_NRFREGISTERSWITCH取值，并保证取值为0-1。                                                        |
| 53772 | 参数取值无效：参数VRM_NRFREGISTERINTERVAL的取值范围是20-1800。 | 输入参数VRM_NRFREGISTERINTERVAL的取值不在取值范围内。                                    | 重新输入VRM_NRFREGISTERINTERVAL取值，并保证取值为20-1800。                                                  |
| 53776 | 参数取值无效：参数VRM_NRFAUTOVRYSWITCH的取值范围是0或者1。       | 输入参数VRM_NRFAUTOVRYSWITCH的取值不在取值范围内。                                       | 重新输入VRM_NRFAUTOVRYSWITCH取值，并保证取值为0-1。                                                         |
| 53822 | 参数取值无效：参数VRM_MULTIPCFLOGICINSTSW的取值范围是0或1。     | 输入参数VRM_MULTIPCFLOGICINSTSW的取值不在取值范围内。                                    | 重新输入VRM_MULTIPCFLOGICINSTSW取值，并保证取值为0或1。                                                      |
| 58217 | 当PCF网元配置多个逻辑实例时，不允许修改本软参值为0。                   | PCF网元已存在多个逻辑实例，不允许通过本命令修改VRM_MULTIPCFLOGICINSTSW软参值为0。                    | 执行LST NFSRV命令，查询系统中已经存在的网元实例信息。若查询结果全部是无效记录可执行RMV NFSRV命令进行删除操作后再重新执行本命令，若都是有效记录则无须处理。        |
| 58238 | 存在NRFGROUP为NULL字符串的NRFINFO时，不允许修改本软参值为1。       | 存在“NRF所属组信息”为NULL字符串的NRFINFO时，不允许通过本命令修改“VRM_MULTIPCFLOGICINSTSW”软参值为“1”。 | 执行LST NRFINFO命令查询全部的配置记录，若结果报文存在“NRF所属组信息”为NULL，则需要联系华为技术支持对现网NRFGROUP的名称进行改造，改造后再执行本命令修改该软参。 |
| 53838 | 参数取值无效：参数VRM_ACCESSTOKENPLMNLIST的取值范围是0或1。     | 输入参数VRM_ACCESSTOKENPLMNLIST的取值不在取值范围内。                                    | 重新输入VRM_ACCESSTOKENPLMNLIST取值，并保证取值为0或1。                                                      |
| 53902 | 参数取值无效：参数VRM_NWDAFTACMERGESW的取值范围是0或1。         | 输入参数VRM_NWDAFTACMERGESW的取值不在取值范围内。                                        | 重新输入VRM_NWDAFTACMERGESW取值，并保证取值为0或1。                                                          |