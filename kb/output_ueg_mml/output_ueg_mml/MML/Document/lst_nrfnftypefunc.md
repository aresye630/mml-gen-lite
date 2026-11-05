# 查询基于NFType设置NRF的各类功能开关（LST NRFNFTYPEFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询基于NFType设置NRF的各类功能开关。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:--------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REQUESTNFTYPE | 客户端NF类型 | 可选必选说明：可选参数  参数含义：该参数用于表示客户端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| TARGETNFTYPE  | 服务端NF类型 | 可选必选说明：可选参数  参数含义：该参数用于表示服务端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |

## 使用实例

运营商通过此命令查询基于NFType设置NRF的各类功能：

```
LST NRFNFTYPEFUNC:;
%%LST NRFNFTYPEFUNC:;%%
RETCODE = 0  执行成功

结果如下
--------
客户端NF类型  服务端NF类型  服务发现结果过滤开关  服务发现结果是否携带NoProfileMatchReason开关  跨NRF服务发现结果精确匹配开关  漫游场景下精确匹配开关
AMF           UDM           打开                  打开                                          打开                           打开
SMF           UDM           打开                  打开                                          打开                           打开
(结果个数 = 2)
2.LST NRFNFTYPEFUNC:;
%%LST NRFNFTYPEFUNC:;%%
RETCODE = 0  执行成功

结果如下
--------
                                客户端NF类型  =  AMF
                                服务端NF类型  =  UDM
                        服务发现结果过滤开关  =  打开
服务发现结果是否携带NoProfileMatchReason开关  =  打开
               跨NRF服务发现结果精确匹配开关  =  打开
                      漫游场景下精确匹配开关  =  打开
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                            | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 客户端NF类型                          | 该参数用于表示客户端NF类型。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 服务端NF类型                          | 该参数用于表示服务端NF类型。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 服务发现结果过滤开关                       | 该参数用于表示NRF在服务发现返回结果中是否携带SUSPENDED状态的实例，开关设置为FUNC_ON时，表示不携带SUSPENDED状态，开关设置为FUNC_OFF时，携带。开关设置为DEFAULT，使用SET NRFFUNCSW中服务发现结果过滤开关（DISCFILTERSW）的开关配置记录。                                                                                                                                                                                                                                                                            |
| 服务发现结果是否携带NoProfileMatchReason开关 | 该参数用于表示NF向NRF发起服务发现，满足发现条件的NF都为SUSPENDED状态且被过滤掉时是否携带NoProfileMatchReason。开关设置为FUNC_ON时，服务发现结果携带NoProfileMatchReason；开关设置为FUNC_OFF时，服务发现结果不携带NoProfileMatchReason。                                                                                                                                                                                                                                                                |
| 跨NRF服务发现结果精确匹配开关                 | 该参数用于表示NRF在跨NRF的服务发现返回结果中是否只携带匹配上的信元信息，这些信元主要包括supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元。开关设置为FUNC_ON时，表示NFINFO中只携带匹配的信元信息；开关设置为FUNC_OFF时，携带NFINFO中所有信元信息。开关设置为DEFAULT，是否只携带匹配上的信元信息受SET NRFFUNCSW中跨NRF服务发现结果精确匹配开关（DISCFILTERFWDSW）的控制。                                                                                                                                                                                               |
| 漫游场景下精确匹配开关                      | 该参数用于表示漫游场景下NRF在跨NRF的服务发现或通知结果中是否携带精简后的信元信息，这些信元主要包括supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元。开关设置为FUNC_ON时，表示服务发现结果中NFINFO只携带匹配的信元信息，通知结果中只携带这些信元的第一个值。开关设置为FUNC_OFF时，服务发现或通知结果携带NFINFO中所有信元信息。开关设置为default时，漫游场景下服务发现或通知结果中NFINFO是否信息精简，受ADD NRFPLMNHOMEPLY、SET NRFHOMEPLY中的INFOHIDEPLY信息精简策略中NFINFO（nfinfo）策略控制。 若不配置ADD NRFPLMNHOMEPLY和SET NRFHOMEPLY归属地策略时，需要根据ADD NRFNFTYPEFUNC和SET NRFFUNCSW中DISCFILTERFWDSW参数配置确定发现结果是否精确匹配返回。 |