# 增加基于NFType设置NRF的各类功能开关（ADD NRFNFTYPEFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

开关设置将会导致以下影响:

- DISCFILTERSW开关关闭可能导致服务发现返回实际不可用的网元。
- DISCFILTERFWDSW、DISCROAFILFWDSW开关打开可能导致服务发现结果信息缺失。

**适用NF：NRF**

该命令用于增加基于NFType设置NRF的各类功能开关。

## 注意事项

- 该命令执行后立即生效。

- 客户端类型和服务端类型不能同时配置为NULL。
- 多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。
- 例如：
- 配置1 AMF（客户端）发现UDM（服务端）按照新要求。
- 配置2 AMF（客户端）发现其他网元按照新要求。
- 配置3 UDM（服务端）被其他网元发现，按照老要求。
- AMF发现UDM时按新要求返回，以配置1优先。

- 最多可输入1000条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| REQUESTNFTYPE   | TARGETNFTYPE   | DISCFILTERSW   | DISCNOPROFILESW   | DISCFILTERFWDSW   | DISCROAFILFWDSW   |
|:----------------|:---------------|:---------------|:------------------|:------------------|:------------------|
| NEF             | BSF            | DEFAULT        | FUNC_OFF          | FUNC_OFF          | DEFAULT           |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                             | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REQUESTNFTYPE   | 客户端NF类型                          | 可选必选说明：必选参数  参数含义：该参数用于表示客户端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| TARGETNFTYPE    | 服务端NF类型                          | 可选必选说明：必选参数  参数含义：该参数用于表示服务端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| DISCFILTERSW    | 服务发现结果过滤开关                       | 可选必选说明：可选参数  参数含义：该参数用于表示NRF在服务发现返回结果中是否携带SUSPENDED状态的实例，开关设置为FUNC_ON时，表示不携带SUSPENDED状态，开关设置为FUNC_OFF时，携带。开关设置为DEFAULT，使用SET NRFFUNCSW中服务发现结果过滤开关（DISCFILTERSW）的开关配置记录。  数据来源：本端规划 取值范围： DEFAULT（继承默认策略）FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无  配置原则：  ADD NRFNFTYPEFUNC中对服务发现结果过滤开关（DISCFILTERSW）的配置优先级高于SET NRFFUNCSW中的配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DISCNOPROFILESW | 服务发现结果是否携带NoProfileMatchReason开关 | 可选必选说明：该参数在"DISCFILTERSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数用于表示NF向NRF发起服务发现，满足发现条件的NF都为SUSPENDED状态且被过滤掉时是否携带NoProfileMatchReason。开关设置为FUNC_ON时，服务发现结果携带NoProfileMatchReason；开关设置为FUNC_OFF时，服务发现结果不携带NoProfileMatchReason。  数据来源：本端规划 取值范围： FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无  配置原则：  ADD NRFNFTYPEFUNC中对服务发现结果是否携带NoProfileMatchReason开关（DISCNOPROFILESW）的配置优先级高于SET NRFFUNCSW中的配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DISCFILTERFWDSW | 跨NRF服务发现结果精确匹配开关                 | 可选必选说明：可选参数  参数含义：该参数用于表示NRF在跨NRF的服务发现返回结果中是否只携带匹配上的信元信息，这些信元主要包括supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元。开关设置为FUNC_ON时，表示NFINFO中只携带匹配的信元信息；开关设置为FUNC_OFF时，携带NFINFO中所有信元信息。开关设置为DEFAULT，是否只携带匹配上的信元信息受SET NRFFUNCSW中跨NRF服务发现结果精确匹配开关（DISCFILTERFWDSW）的控制。  数据来源：本端规划 取值范围： DEFAULT（继承默认策略）FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无  配置原则：  当服务端NF类型为SMF时，跨NRF服务发现结果精确匹配不受该开关控制，由软参DWORD31 BIT10控制。  ADD NRFNFTYPEFUNC中跨NRF服务发现结果精确匹配开关（DISCFILTERFWDSW）的配置优先级高于SET NRFFUNCSW中的配置。                                                                                                                                                                                                                                                                                                                                                                  |
| DISCROAFILFWDSW | 漫游场景下精确匹配开关                      | 可选必选说明：可选参数  参数含义：该参数用于表示漫游场景下NRF在跨NRF的服务发现或通知结果中是否携带精简后的信元信息，这些信元主要包括supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元。开关设置为FUNC_ON时，表示服务发现结果中NFINFO只携带匹配的信元信息，通知结果中只携带这些信元的第一个值。开关设置为FUNC_OFF时，服务发现或通知结果携带NFINFO中所有信元信息。开关设置为default时，漫游场景下服务发现或通知结果中NFINFO是否信息精简，受ADD NRFPLMNHOMEPLY、SET NRFHOMEPLY中的INFOHIDEPLY信息精简策略中NFINFO（nfinfo）策略控制。 若不配置ADD NRFPLMNHOMEPLY和SET NRFHOMEPLY归属地策略时，需要根据ADD NRFNFTYPEFUNC和SET NRFFUNCSW中DISCFILTERFWDSW参数配置确定发现结果是否精确匹配返回。  数据来源：本端规划 取值范围： DEFAULT（继承默认策略）FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无  配置原则：  当服务端NF类型为SMF时，漫游场景下NRF是否返回精确匹配不受该开关控制，由软参DWORD31 BIT10控制。  漫游场景下精确匹配开关（DISCROAFILFWDSW）的优先级高于跨NRF服务发现结果精确匹配开关（DISCFILTERFWDSW）。                                                                                                                                                                           |

## 使用实例

运营商通过此命令增加基于NFType设置NRF的各类功能：设置客户端NF类型为AMF；服务端NF类型为UDM；开启服务发现结果过滤开关；开启服务发现结果是否携带NoProfileMatchReason开关；开启跨NRF服务发现结果精确匹配开关；开启漫游场景下精确匹配开关。

```
ADD NRFNFTYPEFUNC: REQUESTNFTYPE=AMF, TARGETNFTYPE=UDM, DISCFILTERSW=FUNC_ON, DISCNOPROFILESW=FUNC_ON, DISCFILTERFWDSW=FUNC_ON, DISCROAFILFWDSW=FUNC_ON;
```