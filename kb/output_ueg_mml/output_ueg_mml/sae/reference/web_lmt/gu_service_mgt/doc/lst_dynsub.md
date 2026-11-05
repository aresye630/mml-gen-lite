# 查询用户动态数据(LST DYNSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于从内存库查询用户的动态数据，主要包括各类业务的状态，例如，GSM业务、GPRS业务、EPS业务、ODB业务、短消息业务、VLR不支持的业务和LCS业务的状态。

- 若需要查询单个用户的动态数据，请输入参数“IMSI”或“MSISDN”。
- 若需要查询连续多个用户的动态数据，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”。
- 若需要查询不连续的多个用户的动态数据，请输入参数“IMSI文件名”或“MSISDN文件名”。

**说明** 

- 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
- 在从运营商网络获取数据前，必须要获得运营商的授权。
- 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。
- 该命令输出报文中的“ACCESSNETID”输出项只显示ASCII码中的可见字符（0x20～0x7E），如果遇到非可见字符，则只显示非可见字符前面的可见字符部分。

## 参数说明

| 参数标识                 | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                       |
|:---------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI                 | IMSI            | 用于标识要查询哪个IMSI号码对应的动态数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                      |
| ISDN                 | MSISDN          | 用于标识要查询哪个MSISDN号码对应的动态数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                    |
| CONTENT              | 内容              | 用于标识查询用户的哪一类动态数据，若不输入，表示查询用户的所有动态数据。 取值范围：ALL：查询所有动态数据。 GSM：查询与GSM有关的动态数据。 GPRS：查询与GPRS有关的动态数据。 SM：查询与短消息有关的动态数据。 ODB：查询与ODB有关的动态数据。 UNSP：查询与VLR不支持的业务有关的动态数据。 LCS：查询与LCS有关的动态数据。 ALLSM：查询所有与短消息有关的动态数据。 EPS：查询与EPS有关的动态数据。 AMF：查询与AMF相关的动态数据。 SMF：查询与SMF有关的动态数据。ACK：查询与ACK有关的动态数据。 默认值：无。 |
| RECORDCOUNT          | 用户个数            | 用于标识查询动态数据的用户数目。 当需要查询连续号码的多个用户的动态数据时配置。配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的动态数据。 取值范围：1～10000 默认值：无。 说明：该参数是对连续号码的多个用户进行动态数据查询，当只有一个用户时，该参数不必配置。当一次查询的用户个数很多时，对系统性能无影响，但查询的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。                                                                            |
| IMSIFILE             | IMSI文件名         | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的待查询动态数据的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstdynsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                                                                            |
| ISDNFILE             | MSISDN文件名       | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的待查询动态数据的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstdynsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                                                                      |
| EPSFEATURELISTDETAIL | 是否显示详细的EPS域支持特性 | 用于标识是否显示详细的EPS域支持特性，即是否显示MME-FeatureList、S4SGSN-FeatureList、MME-FeatureList2和S4SGSN-FeatureList2的详细信息。 取值范围： TRUE：显示FeatureList值及详细的支持特性。FALSE：仅显示FeatureList值。 默认值：FALSE。                                                                                                                 |

## 使用实例

1. 查询“IMSI”号码为“460000009123456”的用户的所有动态数据，且不显示详细的EPS域支持特性：

   ```
   LST DYNSUB: IMSI="460000009123456";
   ```

   ```
   %%LST DYNSUB: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                             IMSI = 460000009123456
                             ISDN = 8613912345678

   "Dynamic Status Information For GSM"
               MsPurgedForNonGprs = FALSE
                       VLRInHplmn = TRUE
                 VLRInHomeCountry = TRUE
                        VLRInArea = FALSE
                   RequireCheckSS = FALSE
       RoamingRestrictInMscDueToUnsupportedFeature
                                  = FALSE
       MscOrVlrAreaRoamingRestrict
                                  = FALSE
       ODBarredForUnsupportedCamel
                                  = FALSE
             SupportedCamelPhase1 = FALSE
             SupportedCamelPhase2 = FALSE
             SupportedCamelPhase3 = FALSE
             SupportedCamelPhase4 = FALSE
                  SRIMsrnCfActive = TRUE
              ZoneCodeStatusAtMsc = zoneCodesSupported
             longGroupIDSupported = FALSE
                basicISTSupported = FALSE
              istCommandSupported = FALSE
      SuperChargerSupportedForGsm = FALSE
                   ECATEGORYAtMsc = FALSE
                           LSFLAG = FALSE
            camelInduceBarringSMS = FALSE
                     RoamBaocTs11 = FALSE
                    MTRFSupported = FALSE
                   CS-MSISDN-LESS = FALSE
                        CSRATTYPE = GERAN&UTRAN
                      CsUplStatus = Normal
                 longFTNSupported = TRUE
               BaocForVlrRestrict = FALSE

   "Dynamic Status Information For GPRS"
                      SgsnInHplmn = TRUE
                  MsPurgedForGprs = FALSE
                SgsnInHomeCountry = TRUE
                       SgsnInArea = FALSE
       RoamingRestrictInSgsnDueToUnsupportedFeature
                                  = FALSE
          SgsnAreaRoamingRestrict = FALSE
       ODBarredForUnsupportedCamelForGprs
                                  = FALSE
                   PS-MSISDN-LESS = FALSE
                        PSRATTYPE = GERAN&UTRAN
                      PsUplStatus = Normal
             SupportedCamelPhase3 = FALSE
             SupportedCamelPhase4 = FALSE
             ZoneCodeStatusAtSgsn = zoneCodesSupported
     SuperChargerSupportedForGprs = FALSE

   "Dynamic Status Information For MME"
                          MMEHOST = saehss1.huawei.com
                         MMEREALM = huawei.com
                          RATTYPE = UTRAN
                            VPLMN = 460456
                      PURGEDONMME = FALSE
          MME-UpdateLocation-Time = 2015-10-31 17:12:24
                  MME-FeatureList = 0x00000000
                 MME-FeatureList2 = 0x00000000
               LastIDRorDSRFailed = FALSE
   Single-Registration-Indication = FALSE
   Skip-Subscriber-Data-Indicator = FALSE
   GPRS-Subscription-Data-Indicator
                                  = FALSE
              Node-Type-Indicator = Combined
         Initial-Attach-Indicator = FALSE
       PS-LCS-Not-Supported-By-UE = FALSE
                             IMEI = 123456789012340
                           IMEISV = 01
     IMS-VO-PS-Sessions-Supported = UNKNOWN
              UE-SRVCC-Capability = UE-SRVCC-NOT-SUPPORTED
                         ISDYNNSA = 0

   "Dynamic Status Information For S4SGSN"
                         SGSNHOST = saehss1.huawei.com
                        SGSNREALM = huawei.com
                            VPLMN = 460456
                     PURGEDONSGSN = FALSE
                     AREARESTRICT = FALSE
       S4SGSN-UpdateLocation-Time = 2015-10-31 17:12:24
               S4SGSN-FeatureList = 0xFFFFFFFF
              S4SGSN-FeatureList2 = 0xFFFFFFFF
               LastIDRorDSRFailed = FALSE
   Skip-Subscriber-Data-Indicator = FALSE
   GPRS-Subscription-Data-Indicator
                                  = FALSE
              Node-Type-Indicator = Combined
         Initial-Attach-Indicator = TRUE
       PS-LCS-Not-Supported-By-UE = FALSE
                             IMEI = 123456789012340
                           IMEISV = 01
     IMS-VO-PS-Sessions-Supported = UNKNOWN
              UE-SRVCC-Capability = UE-SRVCC-NOT-SUPPORTED

   "Dynamic Status Information For Non-3GPP"
                              VNI = 45.460.com
                        REGSTATUS = NOT_REGISTERED
                      ACCESSNETID = 05WLAN
                TGPPAAASERVERNAME = saehss3.huawei.com
               TGPPAAASERVERREALM = huawei.com
                        TGPP2MEID = FFFFFFFFFFFFFFFF
                           IMEISV = 01
                   NON3GPPRATTYPE = HRPD

   "Short Message Dynamic Data for GSM"
                             MCEF = FALSE
                             MNRF = FALSE
                             MNRR = No Reason for Non-GPRS

   "Short Message Dynamic Data for GPRS"
                             MCEF = FALSE
                             MNRG = FALSE
                             MNRR = No Reason
       SupportedShortMessageMT-PP = TRUE
       SupportedShortMessageMO-PP = TRUE

   "ODB Supported Features For GSM"
                   BarredSSAccess = TRUE
       BarredOutgoingEntertainmentCall
                                  = TRUE
       BarredOutgoingInformationCall
                                  = TRUE
       BarredOutgoingInternationalCallExHC
                                  = TRUE
       BarredOutgoingInternationalCall
                                  = TRUE
            BarredAllOutgoingCall = TRUE
                     BarredAllECT = TRUE
              BarredChargeableECT = TRUE
           BarredInternationalECT = TRUE
              BarredInterzonalECT = TRUE
                       BarredDECT = TRUE
                       BarredMECT = TRUE

   "ODB Supported Features For GPRS"
            BarredAllOutgoingCall = TRUE
       BarredOutgoingInternationalCall
                                  = TRUE
       BarredOutgoingInternationalCallExHC
                                  = TRUE
       Barring of Packet Oriented Services
                                  = TRUE

   "Supported LCS"
       MSC Supported LCS Capability Set1
                                  = FALSE
       MSC Supported LCS Capability Set2
                                  = FALSE
       SGSN Supported LCS Capability Set2
                                  = FALSE

   "Featured Service Supported Features"
                              ALS = FALSE
                             VVDN = FALSE

   "Resend Information"
                           CS_ISD = FALSE
                           CS_DSD = FALSE
                           CS_CLR = FALSE
                           PS_ISD = FALSE
                           PS_DSD = FALSE
                           PS_CLR = FALSE
                          S6a_IDR = FALSE
                          S6a_CLR = FALSE
                          S6d_IDR = FALSE
                          S6d_CLR = FALSE
                             UDCD = FALSE

   "Dynamic Status Information For AMF"
                             IMEI = 012345678980201
                       AMF_DYN_ID = 1
                    AMFINSTANCEID = 11112222-1111-2222-3333-111122223333
                SUPPORTEDFEATURES = 0000000000000000
                        PURGEFLAG = FALSE
                          IMSVOPS = UNKNOWN
                 DEREGCALLBACKURI = http://127.105.70.6:8089/nudm_uecm/callback/v1/
                                    ueId/registrations/amf-3gpp-access/08828018120d
                                    086712090164001302100000f1
                          REGTIME = 2019-01-30 03:58:39
                              MCC = 045
                              MNC = 012
                            AMFID = FFFFFF
                         URRP_AMF = REACHABLE
                          RATTYPE = EUTRA
                    VGMLCIPV4ADDR = 10.189.171.60
                    VGMLCIPV6ADDR = fe80:910a:2222:5498:8475:1111:3900:2020
                        VGMLCFQDN = Huawei.com

   "Dynamic Status Information For SMSF"
                   SMSFINSTANCEID = 1
               SUPPORTEDFEATURES  = 0000000000000001
                         PLMNID   = 111111
                     SMSFNUMBER   = 1
                       SMSFNAME   = 1
                      SMSFREALM   = 1
                        REGTIME   = 2020-05-17 12:17:16
                         MNRFSMSF = FALSE
                         MNRRSMSF = No reason
   "IP USSD"
                    IP_USSD_AS_GT = 8613966666

   Total count = 156

   There is together 1 report

   ---    END
   ```
2. 查询“IMSI”号码为“460000009123456”的用户的所有动态数据，且显示详细的EPS域支持特性：

   ```
   LST DYNSUB: IMSI="460000009123456", EPSFEATURELISTDETAIL=TRUE;
   ```

   ```
   %%LST DYNSUB: IMSI="460000009123456", EPSFEATURELISTDETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                             IMSI = 460000009123456
                             ISDN = 8613912345678

   "Dynamic Status Information For GSM"
               MsPurgedForNonGprs = FALSE
                       VLRInHplmn = TRUE
                 VLRInHomeCountry = TRUE
                        VLRInArea = FALSE
                   RequireCheckSS = FALSE
       RoamingRestrictInMscDueToUnsupportedFeature
                                  = FALSE
       MscOrVlrAreaRoamingRestrict
                                  = FALSE
       ODBarredForUnsupportedCamel
                                  = FALSE
             SupportedCamelPhase1 = FALSE
             SupportedCamelPhase2 = FALSE
             SupportedCamelPhase3 = FALSE
             SupportedCamelPhase4 = FALSE
                  SRIMsrnCfActive = TRUE
              ZoneCodeStatusAtMsc = zoneCodesSupported
             longGroupIDSupported = FALSE
                basicISTSupported = FALSE
              istCommandSupported = FALSE
      SuperChargerSupportedForGsm = FALSE
                   ECATEGORYAtMsc = FALSE
                           LSFLAG = FALSE
            camelInduceBarringSMS = FALSE
                     RoamBaocTs11 = FALSE
                    MTRFSupported = FALSE
                   CS-MSISDN-LESS = FALSE
                        CSRATTYPE = GERAN&UTRAN
                      CsUplStatus = Normal
                 longFTNSupported = TRUE
               BaocForVlrRestrict = FALSE

   "Dynamic Status Information For GPRS"
                      SgsnInHplmn = TRUE
                  MsPurgedForGprs = FALSE
                SgsnInHomeCountry = TRUE
                       SgsnInArea = FALSE
       RoamingRestrictInSgsnDueToUnsupportedFeature
                                  = FALSE
          SgsnAreaRoamingRestrict = FALSE
       ODBarredForUnsupportedCamelForGprs
                                  = FALSE
                   PS-MSISDN-LESS = FALSE
                        PSRATTYPE = GERAN&UTRAN
                      PsUplStatus = Normal
             SupportedCamelPhase3 = FALSE
             SupportedCamelPhase4 = FALSE
             ZoneCodeStatusAtSgsn = zoneCodesSupported
     SuperChargerSupportedForGprs = FALSE

   "Dynamic Status Information For MME"
                          MMEHOST = saehss1.huawei.com
                         MMEREALM = huawei.com
                          RATTYPE = UTRAN
                            VPLMN = 460456
                      PURGEDONMME = FALSE
          MME-UpdateLocation-Time = 2015-10-31 17:12:24
                  MME-FeatureList = 0x00000000
                 MME-FeatureList2 = 0x00000000
               LastIDRorDSRFailed = FALSE
   Single-Registration-Indication = FALSE
   Skip-Subscriber-Data-Indicator = FALSE
   GPRS-Subscription-Data-Indicator
                                  = FALSE
              Node-Type-Indicator = Combined
         Initial-Attach-Indicator = FALSE
       PS-LCS-Not-Supported-By-UE = FALSE
                             IMEI = 123456789012340
                           IMEISV = 01
     IMS-VO-PS-Sessions-Supported = UNKNOWN
              UE-SRVCC-Capability = UE-SRVCC-NOT-SUPPORTED
                         ISDYNNSA = 0

   "MME-FeatureList-DetailInfo"
                      ODB-all-APN = TRUE
                    ODB-HPLMN-APN = TRUE
                    ODB-VPLMN-APN = TRUE
                       ODB-all-OG = TRUE
          ODB-all-InternationalOG = TRUE
   ODB-all-InternationalOGNotToHPLMN-Country
                                  = TRUE
             ODB-all-InterzonalOG = TRUE
   ODB-all-InterzonalOGNotToHPLMN-Country
                                  = TRUE
   ODB-all-InterzonalOGAndInternationalOGNotToHPLMN-Country
                                  = TRUE
                           RegSub = TRUE
                            Trace = TRUE
                LCS-all-PrivExcep = TRUE
                    LCS-Universal = TRUE
           LCS-CallSessionRelated = TRUE
         LCS-CallSessionUnrelated = TRUE
                 LCS-PLMNOperator = TRUE
                  LCS-ServiceType = TRUE
                  LCS-all-MOLR-SS = TRUE
            LCS-BasicSelfLocation = TRUE
       LCS-AutonomousSelfLocation = TRUE
         LCS-TransferToThirdParty = TRUE
                         SM-MO-PP = TRUE
            Barring-OutgoingCalls = TRUE
                             BAOC = TRUE
                             BOIC = TRUE
                         BOICExHC = TRUE
     UE-Reachability-Notification = TRUE
             T-ADS Data Retrieval = TRUE
   State/Location-Information-Retrieval
                                  = TRUE
                    Partial Purge = TRUE
                Additional MSISDN = TRUE

   "MME-FeatureList2-DetailInfo"
               P-CSCF Restoration = TRUE
          Dedicated Core Networks = TRUE
             Non-IP PDN Type APNs = TRUE
              NR as Secondary RAT = TRUE

   "Dynamic Status Information For S4SGSN"
                         SGSNHOST = saehss1.huawei.com
                        SGSNREALM = huawei.com
                            VPLMN = 460456
                     PURGEDONSGSN = FALSE
                     AREARESTRICT = FALSE
       S4SGSN-UpdateLocation-Time = 2015-10-31 17:12:24
               S4SGSN-FeatureList = 0xFFFFFFFF
              S4SGSN-FeatureList2 = 0xFFFFFFFF
               LastIDRorDSRFailed = FALSE
   Skip-Subscriber-Data-Indicator = FALSE
   GPRS-Subscription-Data-Indicator
                                  = FALSE
              Node-Type-Indicator = Combined
         Initial-Attach-Indicator = TRUE
       PS-LCS-Not-Supported-By-UE = FALSE
                             IMEI = 123456789012340
                           IMEISV = 01
     IMS-VO-PS-Sessions-Supported = UNKNOWN
              UE-SRVCC-Capability = UE-SRVCC-NOT-SUPPORTED

   "Dynamic Status Information For Non-3GPP"
                              VNI = 45.460.com
                        REGSTATUS = NOT_REGISTERED
                      ACCESSNETID = 05WLAN
                TGPPAAASERVERNAME = saehss3.huawei.com
               TGPPAAASERVERREALM = huawei.com
                        TGPP2MEID = FFFFFFFFFFFFFFFF
                           IMEISV = 01
                   NON3GPPRATTYPE = HRPD

   "S4SGSN-FeatureList-DetailInfo"
                      ODB-all-APN = TRUE
                    ODB-HPLMN-APN = TRUE
                    ODB-VPLMN-APN = TRUE
                       ODB-all-OG = TRUE
          ODB-all-InternationalOG = TRUE
   ODB-all-InternationalOGNotToHPLMN-Country
                                  = TRUE
             ODB-all-InterzonalOG = TRUE
   ODB-all-InterzonalOGNotToHPLMN-Country
                                  = TRUE
   ODB-all-InterzonalOGAndInternationalOGNotToHPLMN-Country
                                  = TRUE
                           RegSub = TRUE
                            Trace = TRUE
                LCS-all-PrivExcep = TRUE
                    LCS-Universal = TRUE
           LCS-CallSessionRelated = TRUE
         LCS-CallSessionUnrelated = TRUE
                 LCS-PLMNOperator = TRUE
                  LCS-ServiceType = TRUE
                  LCS-all-MOLR-SS = TRUE
            LCS-BasicSelfLocation = TRUE
       LCS-AutonomousSelfLocation = TRUE
         LCS-TransferToThirdParty = TRUE
                         SM-MO-PP = TRUE
            Barring-OutgoingCalls = TRUE
                             BAOC = TRUE
                             BOIC = TRUE
                         BOICExHC = TRUE
     UE-Reachability-Notification = TRUE
             T-ADS Data Retrieval = TRUE
   State/Location-Information-Retrieval
                                  = TRUE
                    Partial Purge = TRUE
        Local Time Zone Retrieval = TRUE
                Additional MSISDN = TRUE

   "S4SGSN-FeatureList2-DetailInfo"
                       SMS in MME = TRUE
                      SMS in SGSN = TRUE
            Dia-LCS-all-PrivExcep = TRUE
                Dia-LCS-Universal = TRUE
       Dia-LCS-CallSessionRelated = TRUE
     Dia-LCS-CallSessionUnrelated = TRUE
             Dia-LCS-PLMNOperator = TRUE
              Dia-LCS-ServiceType = TRUE
              Dia-LCS-all-MOLR-SS = TRUE
        Dia-LCS-BasicSelfLocation = TRUE
   Dia-LCS-AutonomousSelfLocation = TRUE
     Dia-LCS-TransferToThirdParty = TRUE
                      Gdd-in-SGSN = TRUE
       Optimized-LCS-Proc-Support = TRUE
            SGSN CAMEL Capability = TRUE
                 ProSe Capability = TRUE
               P-CSCF Restoration = TRUE
                        Reset-IDs = TRUE
            Communication-pattern = TRUE

   "Short Message Dynamic Data for GSM"
                             MCEF = FALSE
                             MNRF = FALSE
                             MNRR = No Reason for Non-GPRS

   "Short Message Dynamic Data for GPRS"
                             MCEF = FALSE
                             MNRG = FALSE
                             MNRR = No Reason
       SupportedShortMessageMT-PP = TRUE
       SupportedShortMessageMO-PP = TRUE

   "Short Message Dynamic Data for IP"
                             MCEF = FALSE
                             UNRI = FALSE
                             UNRR = No Reason
                         URRP-MME = REACHABLE
                        URRP-SGSN = REACHABLE

   "ODB Supported Features For GSM"
                   BarredSSAccess = TRUE
       BarredOutgoingEntertainmentCall
                                  = TRUE
       BarredOutgoingInformationCall
                                  = TRUE
       BarredOutgoingInternationalCallExHC
                                  = TRUE
       BarredOutgoingInternationalCall
                                  = TRUE
            BarredAllOutgoingCall = TRUE
                     BarredAllECT = TRUE
              BarredChargeableECT = TRUE
           BarredInternationalECT = TRUE
              BarredInterzonalECT = TRUE
                       BarredDECT = TRUE
                       BarredMECT = TRUE

   "ODB Supported Features For GPRS"
            BarredAllOutgoingCall = TRUE
       BarredOutgoingInternationalCall
                                  = TRUE
       BarredOutgoingInternationalCallExHC
                                  = TRUE
       Barring of Packet Oriented Services
                                  = TRUE

   "Supported LCS"
       MSC Supported LCS Capability Set1
                                  = FALSE
       MSC Supported LCS Capability Set2
                                  = FALSE
       SGSN Supported LCS Capability Set2
                                  = FALSE

   "Featured Service Supported Features"
                              ALS = FALSE
                             VVDN = FALSE

   "Resend Information"
                           CS_ISD = FALSE
                           CS_DSD = FALSE
                           CS_CLR = FALSE
                           PS_ISD = FALSE
                           PS_DSD = FALSE
                           PS_CLR = FALSE
                          S6a_IDR = FALSE
                          S6a_CLR = FALSE
                          S6d_IDR = FALSE
                          S6d_CLR = FALSE
                             UDCD = FALSE

   "Dynamic Status Information For AMF"
                             IMEI = 012345678980201
                       AMF_DYN_ID = 1
                    AMFINSTANCEID = 11112222-1111-2222-3333-111122223333
                SUPPORTEDFEATURES = 0000000000000000
                        PURGEFLAG = FALSE
                          IMSVOPS = UNKNOWN
                 DEREGCALLBACKURI = http://127.105.70.6:8089/nudm_uecm/callback/v1/
                                    ueId/registrations/amf-3gpp-access/08828018120d
                                    086712090164001302100000f1
                          REGTIME = 2019-01-30 03:58:39
                              MCC = 045
                              MNC = 012
                            AMFID = FFFFFF
                         URRP_AMF = REACHABLE
                          RATTYPE = EUTRA
                    VGMLCIPV4ADDR = 10.189.171.60
                    VGMLCIPV6ADDR = fe80:910a:2222:5498:8475:1111:3900:2020
                        VGMLCFQDN = Huawei.com

   "Dynamic Status Information For SMSF"
                   SMSFINSTANCEID = 1
               SUPPORTEDFEATURES  = 0000000000000001
                         PLMNID   = 111111
                     SMSFNUMBER   = 1
                       SMSFNAME   = 1
                      SMSFREALM   = 1
                        REGTIME   = 2020-05-17 12:17:16
                         MNRFSMSF = FALSE
                         MNRRSMSF = No reason
   "IP USSD"
                    IP_USSD_AS_GT = 8613966666

   Total count = 212

   There is together 1 report

   ---    END
   ```
3. 查询第一个MSISDN号码为“13310911001”的连续3个用户的与GSM有关的动态数据：

   ```
   LST DYNSUB: ISDN="13310911001", RECORDCOUNT=3, CONTENT=GSM;
   ```

   ```
   %%LST DYNSUB: ISDN="13310911001", RECORDCOUNT=3, CONTENT=GSM;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：13. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
4. 查询“MSISDN文件名”为“lstdynsub.txt”的用户的所有动态数据：

   ```
   LST DYNSUB: ISDNFILE="lstdynsub.txt", CONTENT=ALL;
   ```

   ```
   %%LST DYNSUB: ISDNFILE="lstdynsub.txt", CONTENT=ALL;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435470. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD SUB**

、

**MOD AMDATA**

、

**MOD NGSRRS、ADD SNSSAI和**

**ADD SMDATA**

命令的参数说明。表1列出的是未包含在

**ADD SUB**

、

**MOD AMDATA**

、

**MOD NGSRRS、ADD SNSSAI和**

**ADD SMDATA**

命令参数说明中的输出项。

| 输出项名称                                                                 | 输出项解释                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MsPurgedForNonGprs                                                    | CS域用户是否被purge                                                                                                                                                                                                                                                                                                                                                             |
| VLRInHplmn                                                            | 用户是否在本网的VLR漫游                                                                                                                                                                                                                                                                                                                                                             |
| VLRInHomeCountry                                                      | 用户是否在本网所在的国家的VLR漫游                                                                                                                                                                                                                                                                                                                                                        |
| VLRInArea                                                             | 用户是否在本地的VLR漫游                                                                                                                                                                                                                                                                                                                                                             |
| RequireCheckSS                                                        | 位置更新时是否发起checkSS流程                                                                                                                                                                                                                                                                                                                                                        |
| RoamingRestrictInMscDueToUnsupportedFeature                           | 是否由于MSC/VLR不支持某些业务导致漫游受限                                                                                                                                                                                                                                                                                                                                                  |
| MscOrVlrAreaRoamingRestrict                                           | 用户是否在CS域漫游受限                                                                                                                                                                                                                                                                                                                                                              |
| ODBarredForUnsupportedCamel                                           | 是否由于MSC/VLR不支持某些版本的CAMEL导致ODB闭锁                                                                                                                                                                                                                                                                                                                                           |
| SupportedCamelPhase1                                                  | MSC/VLR是否支持CAMEL Phase 1                                                                                                                                                                                                                                                                                                                                                  |
| SupportedCamelPhase2                                                  | MSC/VLR是否支持CAMEL Phase 2                                                                                                                                                                                                                                                                                                                                                  |
| SupportedCamelPhase3                                                  | MSC/VLR是否支持CAMEL Phase 3                                                                                                                                                                                                                                                                                                                                                  |
| SupportedCamelPhase4                                                  | MSC/VLR是否支持CAMEL Phase 4                                                                                                                                                                                                                                                                                                                                                  |
| SRIMsrnCfActive                                                       | PLMNSS业务是否激活                                                                                                                                                                                                                                                                                                                                                              |
| ZoneCodeStatusAtMsc                                                   | MSC/VLR是否支持区域漫游业务                                                                                                                                                                                                                                                                                                                                                         |
| longGroupIDSupported                                                  | MSC/VLR是否支持长组ID                                                                                                                                                                                                                                                                                                                                                           |
| basicISTSupported                                                     | MSC/VLR是否支持基本的IST业务                                                                                                                                                                                                                                                                                                                                                       |
| istCommandSupported                                                   | MSC/VLR是否支持强制下发方式的IST业务                                                                                                                                                                                                                                                                                                                                                   |
| SuperChargerSupportedForGsm                                           | MSC/VLR是否支持Super-Charger业务                                                                                                                                                                                                                                                                                                                                                |
| ECATEGORYAtMsc                                                        | MSC/VLR是否支持增强用户类别业务                                                                                                                                                                                                                                                                                                                                                       |
| LSFLAG                                                                | 用户是否正在进行位置更新                                                                                                                                                                                                                                                                                                                                                              |
| camelInduceBarringSMS                                                 | CAMEL业务导致的短消息闭锁                                                                                                                                                                                                                                                                                                                                                           |
| CS-MSISDN-LESS                                                        | 用于表示用户在CS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                          |
| CSRATTYPE                                                             | 用于表示用户在CS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA和E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                        |
| CsUplStatus                                                           | 表示用户的CS域位置更新的状态。 “Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向VLR下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置CsUplStatus的值。场景一：位置更新中创建的全网跟踪超时。场景二：HLR收到VLR发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景三：VLR对HLR发来的ISD消息响应超时。场景四：HLR收到VLR发来的其他错误响应。 场景一和场景二，设置CsUplStatus为Exception。场景三和四，设置CsUplStatus为TimeOut。 |
| longFTNSupported                                                      | 用于表示VLR是否支持长前转号码，当VLR不支持长前转号码时不显示。                                                                                                                                                                                                                                                                                                                                        |
| BaocForVlrRestrict                                                    | 是否限制除短消息以外的所有出呼业务                                                                                                                                                                                                                                                                                                                                                         |
| SgsnInHplmn                                                           | 用户是否在本网的SGSN漫游                                                                                                                                                                                                                                                                                                                                                            |
| MsPurgedForGprs                                                       | PS域用户是否被purge                                                                                                                                                                                                                                                                                                                                                             |
| SgsnInHomeCountry                                                     | 用户是否在本网所在的国家的SGSN漫游                                                                                                                                                                                                                                                                                                                                                       |
| SgsnInArea                                                            | 用户是否在本地的SGSN漫游                                                                                                                                                                                                                                                                                                                                                            |
| RoamingRestrictInSgsnDueToUnsupportedFeature                          | 是否由于SGSN不支持某些业务导致漫游受限                                                                                                                                                                                                                                                                                                                                                     |
| SgsnAreaRoamingRestrict                                               | 用户是否在PS域漫游受限                                                                                                                                                                                                                                                                                                                                                              |
| ODBarredForUnsupportedCamelForGprs                                    | 是否由于SGSN不支持某些版本的CAMEL导致ODB闭锁                                                                                                                                                                                                                                                                                                                                              |
| PS-MSISDN-LESS                                                        | 用于表示用户在PS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                          |
| PSRATTYPE                                                             | 用于表示用户在PS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA和E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                        |
| PsUplStatus                                                           | 表示用户的PS域位置更新的状态。 “Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向SGSN下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置PsUplStatus的值。场景一：HLR收到SGSN发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景二：SGSN对HLR发来的ISD消息响应超时。场景三：HLR收到SGSN发来的其他错误响应。 场景一，设置PsUplStatus为Exception。场景二和场景三，设置PsUplStatus为TimeOut。                  |
| MME-FeatureList                                                       | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                  |
| MME-FeatureList2                                                      | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                 |
| S4SGSN-FeatureList                                                    | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                               |
| S4SGSN-FeatureList2                                                   | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                              |
| SuperChargerSupportedForGprs                                          | SGSN是否支持Super-Charger业务                                                                                                                                                                                                                                                                                                                                                   |
| ZoneCodeStatusAtSgsn                                                  | SGSN是否支持区域漫游业务                                                                                                                                                                                                                                                                                                                                                            |
| MCEF                                                                  | 内存溢出标志（Memory Capacity Exceed Flag）                                                                                                                                                                                                                                                                                                                                       |
| MNRF                                                                  | 移动台不可及标志（Mobile Station Not Reachable Flag）                                                                                                                                                                                                                                                                                                                               |
| MNRR                                                                  | 移动台不可及原因（Moblie Station Not Reachable Reason）                                                                                                                                                                                                                                                                                                                             |
| MNRG                                                                  | 移动台GPRS不可及标志（Moblie Station Not Reachable For GPRS Flag）                                                                                                                                                                                                                                                                                                                  |
| SupportedShortMessageMT-PP                                            | SGSN是否支持短消息终结业务                                                                                                                                                                                                                                                                                                                                                           |
| SupportedShortMessageMO-PP                                            | SGSN是否支持短消息始发业务                                                                                                                                                                                                                                                                                                                                                           |
| BarredSSAccess                                                        | MSC是否支持闭锁SS（supplementary service）业务                                                                                                                                                                                                                                                                                                                                      |
| BarredOutgoingEntertainmentCall                                       | MSC是否支持闭锁高费率娱乐台                                                                                                                                                                                                                                                                                                                                                           |
| BarredOutgoingInformationCall                                         | MSC是否支持闭锁高费率信息台                                                                                                                                                                                                                                                                                                                                                           |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GSM)  | MSC是否支持闭锁除归属国家外的国际出呼叫                                                                                                                                                                                                                                                                                                                                                     |
| BarredOutgoingInternationalCall (ODB Supported Features For GSM)      | MSC是否支持闭锁国际出呼叫                                                                                                                                                                                                                                                                                                                                                            |
| BarredAllOutgoingCall (ODB Supported Features For GSM)                | MSC是否支持闭锁所有出呼叫                                                                                                                                                                                                                                                                                                                                                            |
| BarredAllECT                                                          | MSC是否支持闭锁所有ECT业务                                                                                                                                                                                                                                                                                                                                                          |
| BarredChargeableECT                                                   | MSC是否支持闭锁Chargeable ECT业务                                                                                                                                                                                                                                                                                                                                                 |
| BarredInternationalECT                                                | MSC是否支持闭锁International ECT业务                                                                                                                                                                                                                                                                                                                                              |
| BarredInterzonalECT                                                   | MSC是否支持闭锁Interzonal ECT业务                                                                                                                                                                                                                                                                                                                                                 |
| BarredDECT                                                            | MSC是否支持闭锁DECT业务                                                                                                                                                                                                                                                                                                                                                           |
| BarredMECT                                                            | MSC是否支持闭锁MECT业务                                                                                                                                                                                                                                                                                                                                                           |
| BarredAllOutgoingCall (ODB Supported Features For GPRS)               | SGSN是否支持闭锁所有出呼叫                                                                                                                                                                                                                                                                                                                                                           |
| BarredOutgoingInternationalCall (ODB Supported Features For GPRS)     | SGSN是否支持闭锁国际出呼叫                                                                                                                                                                                                                                                                                                                                                           |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GPRS) | SGSN是否支持闭锁除归属国家外的国际出呼叫                                                                                                                                                                                                                                                                                                                                                    |
| Barring of Packet Oriented Services                                   | SGSN是否支持闭锁分组业务                                                                                                                                                                                                                                                                                                                                                            |
| MSC Supported LCS Capability Set1                                     | MSC对LCS业务Capability Set1的支持能力                                                                                                                                                                                                                                                                                                                                             |
| MSC Supported LCS Capability Set2                                     | MSC对LCS业务Capability Set2的支持能力                                                                                                                                                                                                                                                                                                                                             |
| SGSN Supported LCS Capability Set2                                    | SGSN对LCS业务Capability Set2的支持能力                                                                                                                                                                                                                                                                                                                                            |
| CS_ISD                                                                | 表示CS域的插入用户数据用户消息是否被重发                                                                                                                                                                                                                                                                                                                                                     |
| CS_DSD                                                                | 表示CS域的删除用户数据消息是否被重发                                                                                                                                                                                                                                                                                                                                                       |
| CS_CLR                                                                | 表示CS域的cancel消息是否被重发                                                                                                                                                                                                                                                                                                                                                       |
| PS_ISD                                                                | 表示PS域的插入用户数据消息是否被重发                                                                                                                                                                                                                                                                                                                                                       |
| PS_DSD                                                                | 表示PS域的删除用户数据消息是否被重发                                                                                                                                                                                                                                                                                                                                                       |
| PS_CLR                                                                | 表示PS域的cancel消息是否被重发                                                                                                                                                                                                                                                                                                                                                       |
| S6a_IDR                                                               | 表示S6a接口的下发用户数据消息是否被重发                                                                                                                                                                                                                                                                                                                                                     |
| S6a_CLR                                                               | 表示S6a接口的cancel消息是否被重发                                                                                                                                                                                                                                                                                                                                                     |
| S6d_IDR                                                               | 表示S6d接口的下发用户数据消息是否被重发                                                                                                                                                                                                                                                                                                                                                     |
| S6d_CLR                                                               | 表示S6d接口的cancel消息是否被重发                                                                                                                                                                                                                                                                                                                                                     |
| UDCD                                                                  | 表示MAP的ADD通知消息是否被重发                                                                                                                                                                                                                                                                                                                                                        |
| DataRef                                                               | 用于返回Sh接口上AS向HSS请求订阅的用户数据类型。当前版本仅实现了返回“UERSVCCCAP”，即UE-SRVCC-Capability数据。                                                                                                                                                                                                                                                                                                 |
| AS_Host_Name                                                          | 用于返回AS的主机名。                                                                                                                                                                                                                                                                                                                                                               |
| AS_Realm_Name                                                         | 用于返回AS所在的域名。                                                                                                                                                                                                                                                                                                                                                              |
| Server-Assignment-Time                                                | 用于返回SWx接口位置更新成功的时间戳。                                                                                                                                                                                                                                                                                                                                                      |
| ACCESSNETID                                                           | 用于返回接入网标识，是用户设备接入网络的唯一标识符。                                                                                                                                                                                                                                                                                                                                                |
| NON3GPPRATTYPE                                                        | 用于返回用户终端的Non-3GPP无线网络接入类型。 WLANCDMA2000_1XHRPDUMBEHRPD                                                                                                                                                                                                                                                                                                                    |
| RATTYPE                                                               | 用于返回用户终端接入网络的无线接入技术类型。 Dynamic Status Information For MMEUTRANGERANGANHSPA_EVOLUTIONEUTRANEUTRAN-NB-IoT Dynamic Status Information For AMFNREUTRAWLANVIRTUALNR_REDCAP                                                                                                                                                                                                     |
| 批操作ID                                                                 | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息，并保存查询结果。                                                                                                                                                                                                                                                                                                                        |
| P-CSCF Restoration                                                    | MME/SGSN是否支持P-CSCF恢复流程。                                                                                                                                                                                                                                                                                                                                                   |
| Dedicated Core Networks                                               | MME/SGSN是否支持专用核心网。                                                                                                                                                                                                                                                                                                                                                        |
| Non-IP PDN Type APNs                                                  | MME/SGSN是否支持无IP PDN类型的APN。                                                                                                                                                                                                                                                                                                                                                |
| NR as Secondary RAT                                                   | MME/SGSN是否支持NR作为辅助RAT。                                                                                                                                                                                                                                                                                                                                                    |
| AMF_DYN_ID                                                            | 用于返回AMF的动态ID。                                                                                                                                                                                                                                                                                                                                                             |
| AMFINSTANCEID                                                         | 用于返回用户在NRF注册时的AMF标识。                                                                                                                                                                                                                                                                                                                                                      |
| SUPPORTEDFEATURES                                                     | 用于返回AMF的特性支持能力。 取值范围：16进制字符串，bit0为最右边字符的最低bit位。每个bit位表示一个特性支持能力。                                                                                                                                                                                                                                                                                                          |
| PURGEFLAG                                                             | 用于返回AMF在UDM中是否被去注册。 取值范围：TRUE：已经被去注册 FALSE：未被去注册                                                                                                                                                                                                                                                                                                                          |
| IMSVOPS                                                               | 用于返回AMF是否支持IMS VoPS能力。 取值范围： NOT SUPPORT：不支持 SUPPORT：支持 UNKNOWN：未知状态                                                                                                                                                                                                                                                                                                      |
| DEREGCALLBACKURI                                                      | 用于返回UDM给AMF发送去注册时，消息中的URI取值。                                                                                                                                                                                                                                                                                                                                              |
| REGTIME                                                               | 用于返回用户最近一次注册时间。                                                                                                                                                                                                                                                                                                                                                           |
| MCC                                                                   | 用于标识移动国家码。                                                                                                                                                                                                                                                                                                                                                                |
| MNC                                                                   | 用于标识移动网络码。                                                                                                                                                                                                                                                                                                                                                                |
| AMFID                                                                 | 用于返回AMF的标识。                                                                                                                                                                                                                                                                                                                                                               |
| URRP_AMF                                                              | 用于返回UE在AMF上的可达性状态。 取值范围：UNREACHABLE：不可达 REACHABLE：可达 REGULATORY_ONLY：仅用于管理策略优先级服务。                                                                                                                                                                                                                                                                                        |
| ISDYNNSA                                                              | 用户是否为NSA动态用户。 取值范围： 0：4G注册状态1：5G NSA注册状态                                                                                                                                                                                                                                                                                                                                  |
| APNENHANCEFLAG                                                        | 用户是否启用APN下发增强特性。 FALSE：未启用APN下发增强特性。TRUE：启用APN下发增强特性。                                                                                                                                                                                                                                                                                                                     |
| IP USSD                                                               | 用于返回动态IP-USSD-AS地址。当参数“内容”取值为“ALL”或“EPS”时显示。                                                                                                                                                                                                                                                                                                                              |
| VGMLCIPV4ADDR                                                         | 表示VGMLC的IPv4地址。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                       |
| VGMLCIPV6ADDR                                                         | 表示VGMLC的IPv6地址。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                       |
| VGMLCFQDN                                                             | 表示VGMLC IPv6地址的FQDN。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                  |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                             | 处理建议                                                                                                                    |
|:--------|:-----------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                 | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                           | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                            | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |