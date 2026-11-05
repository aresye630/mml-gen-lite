# 测试NF和NRF上的网元信息是否一致（TST NFPROFILECHECK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NEF、NWDAF、SCF**

该命令用来手动触发NF本地配置的NFProfile信息和NRF上存储的该NF的NFProfile信息校验，如果两者不一致NF会自动触发一次注册，保证NRF上存储的NFProfile信息和本地配置的保持一致。

## 注意事项

- NF也可以通过SET NFNRFMGMTPARA中的TPROFILECHK参数实现周期性的自动校验。
- 如果同一类号段数存在多组参数不一致，只会输出其中一组的配置侧数据信息。
- 对于部分枚举类型信息将以数字显示，各数字对于关系如下：
- NfStatus:
- 0: "NFStatusINVALID"。
- 1: "NFStatusREGISTERED"。
- 2: "NFStatusSUSPENDED"。
- 3: "NFStatusUNDISCOVERABLE"。
- 4: "NFStatusMAX"。
- AccessType:
- 0: "AccessTypeINVALID"。
- 1: "AccessType3GPP\_ACCESS"。
- 2: "AccessTypeNON\_3GPP\_ACCESS"。
- 3: "AccessTypeMAX"。
- NotificationType:
- 0: "NotificationTypeINVALID"。
- 1: "NotificationTypeN1\_MESSAGES"。
- 2: "NotificationTypeN2\_INFORMATION"。
- 3: "NotificationTypeLOCATION\_NOTIFICATION"。
- 4: "NotificationTypeDATA\_REMOVAL\_NOTIFICATION"。
- 5: "NotificationTypeDATA\_CHANGE\_NOTIFICATION"。
- 6: "NotificationTypeMAX"。
- N1MessageClass:
- 0: "N1MessageClassINVALID"。
- 1: "N1MessageClass5GMM"。
- 2: "N1MessageClassSM"。
- 3: "N1MessageClassLPP"。
- 4: "N1MessageClassSMS"。
- 5: "N1MessageClassUPDP"。
- 6: "N1MessageClassMAX"。
- N2InformationClass。
- 0: "N2InformationClassINVALID"。
- 1: "N2InformationClassSM"。
- 2: "N2InformationClassNRPPa"。
- 3: "N2InformationClassPWS"。
- 4: "N2InformationClassPWSBCAL"。
- 5: "N2InformationClassPWSRF"。
- 6: "N2InformationClassRAN"。
- 7: "N2InformationClassMAX"。
- ServiceName:
- 1: "Nrf\_NFManagement"。
- 2: "Nnrf\_NFDiscovery"。
- 3: "Nudm\_SubscriberDataManagement"。
- 4: "Nudm\_UEContextManagement"。
- 5: "Nudm\_UEAuthentication"。
- 6: "Nudm\_EventExposure"。
- 7: "Nudm\_ParameterProvision"。
- 8: "Namf\_Communication"。
- 9: "Namf\_EventExposure"。
- 10: "Namf\_MT"。
- 11: "Namf\_Location"。
- 12: "Nsmf\_PDUSession"。
- 13: "Nsmf\_EventExposure"。
- 14: "Nausf\_UEAuthentication"。
- 15: "Nausf\_SoRProtection"。
- 16: "Nausf\_UPUProtection"。
- 17: "Nnef\_PFDManagement"。
- 18: "Npcf\_AMPolicyControl"。
- 19: "Npcf\_SMPolicyControl"。
- 20: "Npcf\_PolicyAuthorization"。
- 21: "Npcf\_BDTPolicyControl"。
- 22: "Npcf\_EventExposure"。
- 23: "Npcf\_UEPolicyControl"。
- 24: "Nsmsf\_SMService"。
- 25: "Nnssf\_NSSelection"。
- 26: "Nnssf\_NSSAIAvailability"。
- 27: "Nudr\_DataRepository"。
- 28: "Nlmf\_Location"。
- 29: "N5g-eir\_EquipmentIdentityCheck"。
- 30: "Nbsf\_Management"。
- 31: "Nchf\_SpendingLimitControl"。
- 32: "Nchf\_Converged\_Charging"。
- 33: "Nnwdaf\_EventsSubscription"。
- 34: "Nnwdaf\_AnalyticsInfo"。
- 35: "Ncustom\_ocs\_SpendingLimitControl"。
- 36: "Ncustom\_ocs\_ConvergedCharging"。
- 37: "Ngmlc\_Location"。
- 38: "Nnef\_3gppAsSessionWithQos"。
- 39: "Nnef\_3gppMonEvent"。
- NfType:
- 1: "Nrf"。
- 2: "Udm"。
- 3: "Amf"。
- 4: "Smf"。
- 5: "Ausf"。
- 6: "Pcf"。
- 7: "Udr"。
- 8: "Upf"。
- 9: "Bsf"。
- 10: "Chf"。
- 11:"Nef"。
- 12:"Nwdaf"。
- NfServiceStatus:
- 1: "NFServiceStatusREGISTERED"。
- 2: "NFServiceStatusSUSPENDED"。
- 3: "NFServiceStatusUNDISCOVERABLE"。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称         | 参数说明                                                                                                                                                                    |
|:-------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCEID | 网元实例标识       | 可选必选说明：必选参数  参数含义：该参数用于指定NF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度是36。  默认值：无  配置原则：  NFINSTANCEID值可通过LST NFUUID获得。                                                           |
| DATACHKREGSW | 数据校验不一致重注册开关 | 可选必选说明：可选参数  参数含义：该参数用于控制数据校验不一致后NF是否发起重注册。  开关值为OFF时，数据校验不一致的NF不会向NRF发起重注册； 开关值为ON时，数据校验不一致的NF会向NRF发起重注册。  数据来源：本端规划 取值范围： “ON（ON）”：功能打开“OFF（OFF）”：功能关闭  默认值：无  配置原则：无 |

## 使用实例

手动触发NFINSTANCEID为“639deb4b-b625-4fe8-bb64-d79c4d5a4aaa”的NF本地配置的NFProfile数据和NRF上存储的此NF的NFProfile数据一致性校验。

```
TST NFPROFILECHECK: NFINSTANCEID="639deb4b-b625-4fe8-bb64-d79c4d5a4aaa", DATACHKREGSW=ON;
```