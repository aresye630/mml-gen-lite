# 显示注册的服务实例信息（DSP SERVICEINSTINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于显示在CMF上注册的服务实例信息。

- 若要显示所有服务在CMF上注册的服务实例信息，“查询类型”请选择“ALL”。
- 若要显示指定服务在CMF上注册的服务实例信息，“查询类型”请选择“BYNAME”，并输入“服务名称”参数。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数描述                                                                                                                                                                                                       |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE        | 查询类型   | 可选必选说明：必选参数 参数含义：用于指定查询在CMF上注册的服务实例信息的方式。 取值范围： ALL(所有)BYNAME(通过服务名称) 默认值：无。 配置原则：无。  说明： 本参数类型为“ALL”时，仅支持查询FE、BE业务的服务实例，不支持查询平台业务的服务实例。                                                                   |
| SERVICENAME | 服务名称   | 可选必选说明：本参数在“查询类型”配置的类型为“BYNAME”时为必选参数。 参数含义：用于表示服务名称。服务名称可通过DSP SERVICENAME命令查询获取。 取值范围：长度为1~31的字符串。 默认值：无。 配置原则：无。  说明： 参数“查询类型”类型为“BYNAME”时，若查询结果返回为空，可能是本参数输入的服务名称不正确，可以通过DSP SERVICENAME命令查询获取正确的服务名称。 |

## 使用实例

1. 显示“查询类型”为“ALL”服务实例信息：

   ```
   DSP SERVICEINSTINFO: TYPE=ALL;
   ```

   服务地址为IPv4的环境：

   ```
   %%DSP SERVICEINSTINFO: TYPE=ALL;%%
   RETCODE = 0  操作成功

   操作结果如下：
   -------------
   服务名称                      服务实例ID            CSE 服务实例ID  进程ID                  服务地址
   UDRDbbroker                   18445160386127748531  4218291         pcf-all-pod20-0_3507_0  10.38.0.111:11118
   PcfSgmService                 18436555706913021372  4218300         pcf-all-pod20-0_3516_0  10.38.0.210:23834
   PcfDisCtrlService             18436450128026938806  4206006         pcf-all-pod20-1-3510_0  10.38.0.146:40449?sslEnabled=true
   PcfNrfClientService           18436344549140868528  4206000         pcf-all-pod20-1_3504_0  10.38.0.236:53905
   PcfDisCtr1Service             18436450128026951094  4218294         pcf-all-pod20-0_3510_0  10.38.0.119:40125?sslEnabled=true
   PcfNotificationTaskServiceGo  18436626028412546481  4206001         pcf-all-pod20-1_3505_0  10.38.0.110:40673
   (结果个数 = 6)

   ---    END
   ```

   服务地址为IPv6的环境：

   ```
   %%DSP SERVICEINSTINFO: TYPE=ALL;%%
   RETCODE = 0  操作成功

   操作结果如下：
   -------------
   服务名称                      服务实例ID            CSE服务实例ID  进程ID                                        服务地址
   PcfHttpAgentService           18436467724575112621  71368109       pcf-srvra-pod242-0__3501__1                   [fc00:1dd2::195]:23802
   PcfOfflineTaskExecService     18436538110499163579  71372219       pcf-addn-pod242-7db84bbf7f-r4fz7__3515__1     [fc00:1dd2::152]:23831
   PcfDisCtrlService             18436450128026934710  4201910        pcf-addp-pod242-5b6c87b458-9gm6d__3510__0     [fc00:1dd2::c2]:40789?sslEnabled=true
   PcfPolicyManagementService    18436414935132102068  71392692       pcf-addp-pod242-5b6c87b458-qvmwj__3508__1     [fc00:1dd2::e0]:23911, [3d0e:1dd2::e0]:23811
   PcfOfflineTaskCtrlService     18436520513950981562  4201914        pcf-addp-pod242-5b6c87b458-9gm6d__3514__0     [fc00:1dd2::c2]:23815
   PcfHttpLoadBalanceService     18436291759697866157  4238765        pcf-srvr1-pod242-7c448d7bdc-jjj9s__3501__0    [fc00:1dd2::1b0]:23860
   PcfDiamLoadBalanceService     18436309356178877870  4238766        pcf-srvr1-pod242-7c448d7bdc-jjj9s__3502__0    [fc00:1dd2::1b0]:23870
   PcfPolicyEngineService        18436326952794148271  138497455      pcf-srvs-pod242-8545dc95b8-j89sd__3503__2     [fc00:1dd2::172]:23822
   PcfPolicyManagementService    18436414935132020148  71310772       pcf-addp-pod242-5b6c87b458-9gm6d__3508__1     [fc00:1dd2::c2]:23911, [3d0e:1dd2::c2]:23811
   PcfPolicyEngineService        18436326952928292271  272641455      pcf-srvs-pod242-8545dc95b8-5gk7t__3503__4     [fc00:1dd2::b2]:23824
   (结果个数 = 10)

   ---    END
   ```
2. 显示“查询类型”为“BYNAME”，“服务名称”为“PcfDisCtrlService”的服务实例信息：

   ```
   DSP SERVICEINSTINFO: TYPE=BYNAME, SERVICENAME="PcfDisCtrlService";
   ```

   服务地址为IPv4的环境：

   ```
   %%DSP SERVICEINSTINFO: TYPE=BYNAME, SERVICENAME="PcfDisCtrlService";%%
   RETCODE = 0  操作成功

   操作结果如下：
   -------------
   服务名称           服务实例ID            CSE 服务实例ID  进程ID                  服务地址
   PcfDisCtrlService  18436450128026938806  4206006         pcf-all-pod20-1-3510_0  10.38.0.146:40449?sslEnabled=true
   PcfDisCtr1Service  18436450128026951094  4218294         pcf-all-pod20-0_3510_0  10.38.0.119:40125?sslEnabled=true
   (结果个数 = 2)

   ---    END
   ```

   服务地址为IPv6的环境：

   ```
   %%DSP SERVICEINSTINFO: TYPE=BYNAME, SERVICENAME="PcfDisCtrlService";%%
   RETCODE = 0  操作成功

   操作结果如下：
   -------------
   服务名称           服务实例ID            CSE服务实例ID  进程ID                                     服务地址
   PcfDisCtrlService  18436450128026934710  4201910        pcf-addp-pod242-5b6c87b458-9gm6d__3510__0  [fc00:1dd2::c2]:40789?sslEnabled=true
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

| 输出项名称      | 输出项解释                                                            |
|:-----------|:-----------------------------------------------------------------|
| 服务名称       | 参数含义：该参数用于表示服务名称。服务名称可通过DSP SERVICENAME命令查询获取。 取值范围：长度为1~31的字符串。 |
| 服务实例ID     | 参数含义：该参数用于表示返回服务的通信实例号。 取值范围：0~64                                |
| CSE 服务实例ID | 参数含义：该参数用于表示返回服务的实例号。 取值范围：0~64                                  |
| 进程ID       | 参数含义：该参数用于表示服务实例所在的进程ID。 取值范围：0~64                               |
| 服务地址       | 参数含义：该参数用于表示服务实例的地址。 取值范围：0~299                                  |