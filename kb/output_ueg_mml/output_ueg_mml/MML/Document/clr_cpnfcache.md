# 清除NF缓存（CLR CPNFCACHE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

本命令会清除本端从NRF中获得的远端NF信息缓存数据，可能会导致业务呼损。

**适用NF：AMF、SMF、NRF、NSSF、NCG、NEF、SMSF、NWDAF、SCF**

该命令用于清除本端从NRF中获得的远端NF信息缓存数据。如果缓存数据存在异常，或者希望在缓存老化时间到达之前清除缓存，可以执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 清除缓存信息后，后续NF进行服务发现就需要发查询请求给NRF，可能会导致短时间内向NRF的服务发现请求增多。
- 该命令参数均为可选，若不提供任何输入参数，则会清除全部缓存，建议就实际情况选择输入参数。
- 当参数“仅缓存更新”开启时，不会直接删除缓存，而是按照一定的速率，向NRF主动服务发现来更新缓存。
- 如果在短时间内连续两次执行此命令且参数“仅缓存更新”都开启时，先执行的命令还没有将所有NF的缓存全部更新完成的场景下，后执行优先级更高的“CLR\_CACHE\_ALL”会打断前面“CLR\_CACHE\_NFTYPE”的命令。其它场景则会直接丢弃后执行的此命令。
- 如果“仅缓存更新”功能正在执行过程中，再次下发此命令且参数“仅缓存更新”关闭时，“仅缓存更新”功能会中止。
- 指定NF InstanceID清缓存时推荐对主备NF InstanceID同时执行清缓存，否则会导致无法按照配置的NF优先级选择目标NF。
- 如果“仅缓存更新”功能关闭，且软参DWORD205 BIT31开启，执行“CLR\_CACHE\_ALL”会清除所有订阅记录并触发去订阅流程。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLRCACHETYPE    | 缓存清除策略    | 可选必选说明：可选参数  参数含义：该参数用于指定缓存清除的策略。  数据来源：本端规划 取值范围： “CLR_CACHE_ALL（CLR_CACHE_ALL）”：清除缓存中所有的NF信息。“CLR_CACHE_NFTYPE（CLR_CACHE_NFTYPE）”：根据NF类型清除缓存中的NF信息。“CLR_CACHE_NFID（CLR_CACHE_NFID）”：根据指定的NF实例标识清除缓存中的单个NF信息。  默认值：CLR_CACHE_ALL  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| NFTYPE          | NF类型      | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_NFTYPE"时为条件必选参数。  参数含义：该参数用于指定采用NF类型来清除缓存时，具体的NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF  默认值：无  配置原则：无 |
| NFID            | NF实例标识    | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_NFID"时为条件必选参数。  参数含义：该参数用于指定采用NF实例标识来清除缓存时，具体的NF实例标识。  数据来源：本端规划  取值范围：字符串类型，输入长度是36。  默认值：无  配置原则：  该参数为通过DSP CPNFCACHE命令指定对应的NF类型以及Cache Type为E_REMOTE_ONLY查询得到的NF实例标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CACHEUPDATEONLY | 仅缓存更新     | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_ALL"、"CLR_CACHE_NFTYPE"、"CLR_CACHE_NFID"时为条件可选参数。  参数含义：如果功能开启，不直接删除本地缓存，而是将缓存里指定的NF记录（记录的范围根据参数缓存清除策略来定），按照一定的速率，向NRF主动服务发现来更新缓存。如果功能关闭，支持删除本地缓存。  数据来源：本端规划 取值范围： “OFF（OFF）”：功能关闭“ON（ON）”：功能开启  默认值：ON  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| UPDATESPEED     | 缓存更新速度(秒) | 可选必选说明：该参数在"CACHEUPDATEONLY"配置为"ON"时为条件可选参数。  参数含义：该参数用于指定当次缓存更新的速度，即每隔N秒去NRF服务发现一个NF。  数据来源：本端规划  取值范围：整数类型，取值范围是0~255。当取值为0时，会按照默认值10秒每个的速率去NRF服务发现。  默认值：10  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PODID           | POD地址     | 可选必选说明：可选参数  参数含义：该参数用于指定POD的地址。如需按指定POD进行清除缓存，输入此参数即可。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。来源于DSP CPNFCACHE的输出报文的参数“Pod地址”或命令DSP POD的输出报文中的参数“Pod名称”。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## 使用实例

- 运营商A需要清除从NRF中获得的远端NF信息缓存数据：

  ```
  CLR CPNFCACHE:;
  ```
- 运营商A需要清除所有从NRF中获得的所有远端AMF信息缓存数据：

  ```
  CLR CPNFCACHE:CLRCACHETYPE=CLR_CACHE_NFTYPE,NFTYPE=NfAMF;
  ```
- 运营商A需要清除从NRF中获得的远端网元（NF实例标识为a6a61c6f-0d3a-4221-b1da-424eda3ccf67）信息缓存数据：

  ```
  CLR CPNFCACHE:CLRCACHETYPE=CLR_CACHE_NFID,NFID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67";
  ```
- 运营商A需要清除所有向NRF的订阅记录和从NRF中获得的远端网元缓存记录（需先通过LST COMMONSOFTPARAOFBIT确保软参DWORD205 BIT31开启）：

  ```
  CLR CPNFCACHE:CLRCACHETYPE=CLR_CACHE_ALL;
  ```