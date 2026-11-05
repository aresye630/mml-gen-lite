# 查询用户静态数据(LST SUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于从内存库查询用户的静态数据，主要包括用户签约的各种业务信息以及用户是否加锁等信息。

- 若需要查询单个用户的静态数据，请输入参数“IMSI”或“MSISDN”。
- 若需要查询连续多个用户的静态数据，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”。
- 若需要查询不连续的多个用户的静态数据，请输入参数“IMSI文件名”或“MSISDN文件名”。

**说明** 

- 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
- 在从运营商网络获取数据前，必须要获得运营商的授权。
- 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。
- 执行该命令的结果中不显示呼叫等待业务的激活状态，若需要查询，请通过**LST CWAIT**命令进行查询。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                            |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于标识要查询哪个IMSI号码对应的静态数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                           |
| ISDN        | MSISDN    | 用于标识要查询哪个MSISDN号码对应的静态数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                         |
| RECORDCOUNT | 用户个数      | 用于标识查询静态数据的用户数目。 当需要查询连续号码的多个用户的静态数据时配置。配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的静态数据。 取值范围：1～10000 默认值：无。 说明：该参数是对连续号码的多个用户进行静态数据查询，当只有一个用户时，该参数不必配置。当一次查询的用户个数很多时，对系统性能无影响，但查询的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的待查询静态数据的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                    |
| ISDNFILE    | MSISDN文件名 | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的待查询静态数据的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                              |
| DETAIL      | 是否返回详细信息  | 用于标识查询后返回的报文中是否显示用户的详细信息。 取值范围： TRUE：显示用户详细信息，包括用户所有签约、未签约的业务数据。 FALSE：显示用户精简信息，包括用户已经签约的业务数据。 默认值：FALSE。                                                                                                       |

## 使用实例

1. 查询“IMSI”为“460000009123456”的用户的静态数据，且不返回详细信息：

   ```
   LST SUB: IMSI="460000009123456", DETAIL=FALSE;
   ```

   ```
   %%LST SUB: IMSI="460000009123456", DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                             IMSI = 460000009123456
                             ISDN = 460000009012389
                             ISDN = 460000009012399
                         CardType = SIM
                              NAM = BOTH
                         CATEGORY = COMMON
   "SABLOCK"

   "Basic Service"
                       Emergency Call (TS12)
                      DefaultCall = Telephony (TS11)

   "SS Data"
                       CCBSTARGET = PROV
   "GPRS Data"
                           CNTXID = 2
                              APN = APN1
                             SMDP = MSC
                         RROption = ALL_PLMNS

   "SMS INAP Service"
                             SKEY = 0
   "MAP Address Restriction Service"
                  MAPADDRRESTPLID = 1
   "Preferred Roaming Service"
                 CS_ROAMPERTPL_ID = 1
                 PS_ROAMPERTPL_ID = 2

   Total count = 18

   There is together 1 report

   ---    END
   ```
2. 查询“IMSI”为“460000009123456”的用户的静态数据，且返回详细信息：

   ```
   LST SUB: IMSI="460000009123456", DETAIL=TRUE;
   ```

   ```
   %%LST SUB: IMSI="460000009123456", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                             IMSI = 460000009123456
                             ISDN = 460000009123456
                    ICS-Indicator = FALSE
                 ANCHOR-Indicator = FALSE
                      UEUSAGETYPE = 241
                         CardType = SIM
                              NAM = BOTH
                         CATEGORY = COMMON
                          SUB_AGE = 0
                     USERCATEGORY = NORMAL
                       ZCLOCKPROV = FALSE
                              ICI = FALSE
   "LOCK"
                               IC = FALSE
                               OC = FALSE

                         GPRSLOCK = FALSE

                          EPSLOCK = FALSE

                      NON3GPPLOCK = FALSE

                         CSUPLLCK = FALSE

                         PSUPLLCK = FALSE

                          NGSLOCK = FALSE

   "SABLOCK"
                               IC = FALSE
                               OC = FALSE

   "Basic Service"
                       Emergency Call (TS12)
                      DefaultCall = Telephony (TS11)

   "ODB Data"
                            ODBSS = FALSE
                            ODBOC = NOBOC
                            ODBIC = NOBIC
                           ODBPB1 = FALSE
                           ODBPB2 = FALSE
                           ODBPB3 = FALSE
                           ODBPB4 = FALSE
                          ODBENTE = FALSE
                          ODBINFO = FALSE
                          ODBROAM = NOBAR
                           ODBRCF = NOBRCF
                           ODBECT = NOBECT
                          ODBDECT = FALSE
                          ODBMECT = FALSE
                           ODBPOS = NOBPOS
                       ODBPOSTYPE = BOTH
                      ODBENTEROAM = FALSE
                      ODBINFOROAM = FALSE

   "SS Data"
                              CFU = NOTPROV
                              CFB = NOTPROV
                            CFNRY = NOTPROV
                            CFNRC = NOTPROV
                              CFD = NOTPROV
                             BAOC = NOTPROV
                             BOIC = NOTPROV
                         BOICEXHC = NOTPROV
                             BORO = NOTPROV
                             BAIC = NOTPROV
                          BICROAM = NOTPROV
                            CBCOU = SUBSCRIBER
                             CLIP = NOTPROV
                             CLIR = NOTPROV
                             COLP = NOTPROV
                             COLR = NOTPROV
                              ECT = NOTPROV
                               CW = NOTPROV
                             HOLD = NOTPROV
                             MPTY = NOTPROV
                               MC = NOTPROV
                             AOCI = NOTPROV
                             AOCC = NOTPROV
                              CUG = NOTPROV
                             UUS1 = NOTPROV
                             UUS2 = NOTPROV
                             UUS3 = NOTPROV
                            SMSCF = NOTPROV
                plmn-specificSS-1 = NOTPROV
                plmn-specificSS-2 = NOTPROV
                plmn-specificSS-3 = NOTPROV
                plmn-specificSS-4 = NOTPROV
                plmn-specificSS-5 = NOTPROV
                plmn-specificSS-6 = NOTPROV
                plmn-specificSS-7 = NOTPROV
                plmn-specificSS-8 = NOTPROV
                plmn-specificSS-9 = NOTPROV
                plmn-specificSS-A = NOTPROV
                plmn-specificSS-B = NOTPROV
                plmn-specificSS-C = NOTPROV
                plmn-specificSS-D = NOTPROV
                plmn-specificSS-E = NOTPROV
                plmn-specificSS-F = NOTPROV
               allplmn-specificSS = NOTPROV
                             CNAP = NOTPROV
                             CCBS = NOTPROV
                       CCBSTARGET = PROV
                       ODBPREMSMS = FALSE
                      ODBADULTSMS = FALSE
                              SPN = PROV
                            TPLID = 1
                              FTN = 86139000
                           STATUS = PROV | REG | ACT
                             VMCC = TRUE
   "TIF-CSI"
                           TIFCSI = NOTPROV
                             SMDP = MSC
                              ALS = NOTPROV
                             VVDN = NOTPROV
                              ARD = PROV
                  UTRANNOTALLOWED = TRUE
                  GERANNOTALLOWED = TRUE
                  NR5GSNOTALLOWED = TRUE
                             CARP = NOTPROV
                         RROption = ALL_PLMNS
                            RZONE = 0
                              VBS = NOTPROV
                             VGCS = NOTPROV
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER
                           FMInit = NOTPROV
                     FMSupervisor = NOTPROV
                         FMRemote = NOTPROV
                              IST = NOTPROV
                              DIC = NOTPROV
                          NIRPROV = FALSE
                              CPP = NOTPROV
                             ELCS = NOTPROV
   "EPS Data"
                    CHARGE_GLOBAL = NONE
                        AMBRMAXUL = 4294967295
                        AMBRMAXDL = 4294967295
                              EGR = NOTPROV
                      NON3GPPSUPP = FALSE
                      LTEAUTOPROV = FALSE
                              MPS = FALSE
                           ICSIND = FALSE
                           ANCHOR = FALSE
                         TAUTIMER = 0
                       RELAY_NODE = FALSE
                        EPSODBPOS = NOBPOS
                         AMBRNRUL = 10000
                         AMBRNRDL = 10005 
                          NSAFLAG = TRUE
                      NSAAUTOPROV = TRUE
                             SMDP = MSC
                              ALS = NOTPROV
                             VVDN = NOTPROV
                              ARD = PROV
                             CARP = NOTPROV
                         RROption = ALL_PLMNS
                            RZONE = 0
                              VBS = NOTPROV
                             VGCS = NOTPROV
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER
                           FMInit = NOTPROV
                     FMSupervisor = NOTPROV
                         FMRemote = NOTPROV
                              IST = NOTPROV
                              DIC = NOTPROV
                          NIRPROV = FALSE
                              CPP = NOTPROV
                             ELCS = NOTPROV
                            WBPTW = 1
                            NBPTW = 1

   "PS PDP Data"   
                    CHARGE_GLOBAL = NONE
   "EPS PDN Data"
                    CHARGE_GLOBAL = NONE
                    DEFAULTCNTXID = 2
                           CNTXID = 1
                   EPSAPNQOSTPLID = 100

                           CNTXID = 2
                   EPSAPNQOSTPLID = 200

                             SMDP = MSC
                              ALS = NOTPROV
                             VVDN = NOTPROV
                              ARD = NOTPROV
                             CARP = NOTPROV
                         RROption = ALL_PLMNS
                            RZONE = 0
                              VBS = NOTPROV
                             VGCS = NOTPROV
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER
                           FMInit = NOTPROV
                     FMSupervisor = NOTPROV
                         FMRemote = NOTPROV
                              IST = NOTPROV
                              DIC = NOTPROV
                          NIRPROV = FALSE
                              CPP = NOTPROV
                             ELCS = NOTPROV

   "Dynamic Status Information For MME"
                          MMEHOST = saehss1.huawei.com
                         MMEREALM = huawei.com
                          RATTYPE = UTRAN
                      PURGEDONMME = FALSE
                  MME-FeatureList = 0x00000000
                 MME-FeatureList2 = 0x00000000
               LastIDRorDSRFailed = FALSE
   Single-Registration-Indication = FALSE
   Skip-Subscriber-Data-Indicator = FALSE
   GPRS-Subscription-Data-Indicator
                                  = FALSE
              Node-Type-Indicator = Single
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
       S4SGSN-UpdateLocation-Time = 2015-11-04 17:09:22
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

   "Dynamic Status Information For IMS"
                UE-Register-AtIMS = FALSE
                             SMDP = MSC
                              ALS = NOTPROV
                             VVDN = NOTPROV
                              ARD = NOTPROV
                             CARP = NOTPROV
                         RROption = ALL_PLMNS
                            RZONE = 0
                              VBS = NOTPROV
                             VGCS = NOTPROV
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER
                           FMInit = NOTPROV
                     FMSupervisor = NOTPROV
                         FMRemote = NOTPROV
                              IST = NOTPROV
                              DIC = NOTPROV
                          NIRPROV = FALSE
                              CPP = NOTPROV
                             ELCS = NOTPROV

   "Dynamic Status Information For Non-3GPP"
                              VNI = 45.460.com
                        REGSTATUS = NOT_REGISTERED
                TGPPAAASERVERNAME = saehss3.huawei.com
               TGPPAAASERVERREALM = huawei.com
                           IMEISV = 01
                   NON3GPPRATTYPE = HRPD

   "Dynamic Status Information For GSM"
               BaocForVlrRestrict = FALSE
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
                   CS-MSISDN-LESS = FALSE
                      CsUplStatus = Normal
                 longFTNSupported = TRUE
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
                      PsUplStatus = Normal
             SupportedCamelPhase3 = FALSE
             SupportedCamelPhase4 = FALSE
     SuperChargerSupportedForGprs = networkNode_AreaRestricted
             ZoneCodeStatusAtSgsn = zoneCodesSupported
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

   "SMS INAP Service"
                             SKEY = 0
   "M2M"
                      IMEILCKPROV = FALSE
                        M2MNOTIFY = NOTPROV
                     LTE_M2M_FLAG = TRUE
   "Preferred Roaming Service"
                 CS_ROAMPERTPL_ID = 1
                 PS_ROAMPERTPL_ID = 2
   "DND Service"
                              DND = TRUE
   "ANCHORTCSI"
                       ANCHORTCSI = 0
   "CN Restriction"
                    EPCNOTALLOWED = TRUE
                    NGCNOTALLOWED = FALSE
   "5GS Data"
                           AMBRUP = 11111111
                           UPUNIT = bps
                           AMBRDW = 111111111
                           DWUNIT = bps
                      RATRESTRICT = WLAN | VIRTUAL
                        RFSPINDEX = 255
                     SUBSREGTIMER = 11111
                              MPS = TRUE
                              MCS = FALSE
                       ACTIVETIME = 11111
                      DLBUFFERIND = REQUESTED
                         DLBUFFER = 1
                         AUTHTYPE = 5G-AKA
                    SMSSUBSCRIBED = TRUE
                            MTSMS = FALSE
                          MTSMSBA = FALSE
                          MTSMSBR = FALSE
                            MOSMS = FALSE
                          MOSMSBA = FALSE
                          MOSMSBR = FALSE
            NSSAIINCLUSIONALLOWED = TRUE
                      MICOALLOWED = FALSE
                           SNSSAI = 1-123abc
                        DEFSNSSAI = TRUE
                              DNN = cmwap
                          DEFAULT = TRUE
                      DNNQOSTPLID = 101
   "Group Data"
                        INGROUPID = 5-460003-01
                         SHAREDID = 46001-shared5
   "Dynamic Status Information For AMF"
                             IMEI = 012345678980201
                       AMF_DYN_ID = 1
                    AMFINSTANCEID = 11112222-1111-2222-3333-111122223333
                SUPPORTEDFEATURES = 00000000002D3A23
                        PURGEFLAG = FALSE
                          IMSVOPS = UNKOWN
                 DEREGCALLBACKURI = http://192.168.48.136:8020/namf-uecm/v1/imsi-4600012009001/registrations/amf-3gpp-access
                          REGTIME = 2019-09-09 11:26:54
                            AMFID = 111122
                         URRP_AMF = REACHABLE
                          RATTYPE = EUTRA
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
   "Prn GSM Bearer Replace Data" 
                             BS20 = BS20
                             BS22 = BS22

   Total count = 358

   There is together 1 report

   ---    END
   ```
3. 查询第一个“MSISDN”号码为“13310911001”的连续3个用户的静态数据，且返回详细信息：

   ```
   LST SUB: ISDN="13310911001", RECORDCOUNT=3, DETAIL=TRUE;
   ```

   ```
   %%LST SUB: ISDN="13310911001", RECORDCOUNT=3, DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：11. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
4. 查询“MSISDN文件名”为“lstsub.txt”的用户的静态数据，且返回详细信息：

   ```
   LST SUB: ISDNFILE="lstsub.txt", DETAIL=TRUE;
   ```

   ```
   %%LST SUB: ISDNFILE="lstsub.txt", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435468. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD SUB**

、

**MOD LCK**

、

**MOD AMDATA**

、

**MOD NGSRRS、ADD SNSSAI**

和

**ADD SMDATA**

命令的参数说明。表1列出的是未包含在

**ADD SUB**

、

**MOD LCK**

、

**MOD AMDATA**

、

**MOD NGSRRS、ADD SNSSAI**

和

**ADD SMDATA**

命令参数说明中的输出项。

| 输出项名称                                                                 | 输出项解释                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUB_AGE                                                               | 用户的年龄指数（在Super-Charger业务中使用）。                                                                                                                                                                                                                                                                                                                                             |
| SPN                                                                   | 用于返回用户是否签约SPN（Single Personal Number）业务。 PROV：用户签约SPN业务。NOTPROV：用户没有签约SPN业务。                                                                                                                                                                                                                                                                                              |
| TPLID                                                                 | 用于返回用户签约的通过SPN业务对应的OFA模板ID。                                                                                                                                                                                                                                                                                                                                               |
| FTN                                                                   | 用于返回用户签约的SPN前转号码。                                                                                                                                                                                                                                                                                                                                                         |
| STATUS                                                                | 用于返回用户的呼叫前转状态。 PROV：签约。REG：登记。ACT：激活。QUIESCENT：静止。                                                                                                                                                                                                                                                                                                                        |
| PERMANENTIND                                                          | 用于返回用户接入的APN是否是永久APN。 TRUE：永久APN。FALSE：非永久APN。                                                                                                                                                                                                                                                                                                                            |
| BaocForVlrRestrict                                                    | 是否限制除短消息以外的所有出呼业务。                                                                                                                                                                                                                                                                                                                                                        |
| MsPurgedForNonGprs                                                    | CS域用户是否被purge。                                                                                                                                                                                                                                                                                                                                                            |
| VLRInHplmn                                                            | 用户是否在本网的VLR漫游。                                                                                                                                                                                                                                                                                                                                                            |
| VLRInHomeCountry                                                      | 用户是否在本网所在的国家的VLR漫游。                                                                                                                                                                                                                                                                                                                                                       |
| VLRInArea                                                             | 用户是否在本地的VLR漫游。                                                                                                                                                                                                                                                                                                                                                            |
| RequireCheckSS                                                        | 位置更新时是否发起checkSS流程。                                                                                                                                                                                                                                                                                                                                                       |
| RoamingRestrictInMscDueToUnsupportedFeature                           | 是否由于MSC/VLR不支持某些业务导致漫游受限。                                                                                                                                                                                                                                                                                                                                                 |
| MscOrVlrAreaRoamingRestrict                                           | 用户是否在CS域漫游受限。                                                                                                                                                                                                                                                                                                                                                             |
| ODBarredForUnsupportedCamel                                           | 是否由于MSC/VLR不支持某些版本的CAMEL导致ODB闭锁。                                                                                                                                                                                                                                                                                                                                          |
| SupportedCamelPhase1                                                  | MSC/VLR是否支持CAMEL Phase 1。                                                                                                                                                                                                                                                                                                                                                 |
| SupportedCamelPhase2                                                  | MSC/VLR是否支持CAMEL Phase 2。                                                                                                                                                                                                                                                                                                                                                 |
| SupportedCamelPhase3                                                  | MSC/VLR是否支持CAMEL Phase 3。                                                                                                                                                                                                                                                                                                                                                 |
| SupportedCamelPhase4                                                  | MSC/VLR是否支持CAMEL Phase 4。                                                                                                                                                                                                                                                                                                                                                 |
| SRIMsrnCfActive                                                       | PLMNSS业务是否激活。                                                                                                                                                                                                                                                                                                                                                             |
| ZoneCodeStatusAtMsc                                                   | MSC/VLR是否支持区域漫游业务。                                                                                                                                                                                                                                                                                                                                                        |
| longGroupIDSupported                                                  | MSC/VLR是否支持长组ID。                                                                                                                                                                                                                                                                                                                                                          |
| basicISTSupported                                                     | MSC/VLR是否支持基本的IST业务。                                                                                                                                                                                                                                                                                                                                                      |
| istCommandSupported                                                   | MSC/VLR是否支持强制下发方式的IST业务。                                                                                                                                                                                                                                                                                                                                                  |
| SuperChargerSupportedForGsm                                           | MSC/VLR是否支持Super-Charger业务。                                                                                                                                                                                                                                                                                                                                               |
| ECATEGORYAtMsc                                                        | MSC/VLR是否支持增强用户类别业务。                                                                                                                                                                                                                                                                                                                                                      |
| CS-MSISDN-LESS                                                        | 用于表示用户在CS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                          |
| CSRATTYPE                                                             | 用于表示用户在CS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA或E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                        |
| CsUplStatus                                                           | 表示用户的CS域位置更新的状态。 “Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向VLR下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置CsUplStatus的值。场景一：位置更新中创建的全网跟踪超时。场景二：HLR收到VLR发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景三：VLR对HLR发来的ISD消息响应超时。场景四：HLR收到VLR发来的其他错误响应。 场景一和场景二，设置CsUplStatus为Exception。场景三和四，设置CsUplStatus为TimeOut。 |
| longFTNSupported                                                      | 用于表示VLR是否支持长前转号码，当VLR不支持长前转号码时不显示。                                                                                                                                                                                                                                                                                                                                        |
| SgsnInHplmn                                                           | 用户是否在本网的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                           |
| MsPurgedForGprs                                                       | PS域用户是否被purge。                                                                                                                                                                                                                                                                                                                                                            |
| SgsnInHomeCountry                                                     | 用户是否在本网所在的国家的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                      |
| SgsnInArea                                                            | 用户是否在本地的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                           |
| RoamingRestrictInSgsnDueToUnsupportedFeature                          | 是否由于SGSN不支持某些业务导致漫游受限。                                                                                                                                                                                                                                                                                                                                                    |
| SgsnAreaRoamingRestrict                                               | 用户是否在PS域漫游受限。                                                                                                                                                                                                                                                                                                                                                             |
| ODBarredForUnsupportedCamelForGprs                                    | 是否由于SGSN不支持某些版本的CAMEL导致ODB闭锁。                                                                                                                                                                                                                                                                                                                                             |
| PS-MSISDN-LESS                                                        | 用于表示用户在PS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                          |
| PSRATTYPE                                                             | 用于表示用户在PS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA或E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                        |
| PsUplStatus                                                           | 表示用户的PS域位置更新的状态。 “Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向SGSN下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置PsUplStatus的值。场景一：HLR收到SGSN发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景二：SGSN对HLR发来的ISD消息响应超时。场景三：HLR收到SGSN发来的其他错误响应。 场景一，设置PsUplStatus为Exception。场景二和场景三，设置PsUplStatus为TimeOut。                  |
| MME-FeatureList                                                       | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                  |
| MME-FeatureList2                                                      | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                 |
| S4SGSN-FeatureList                                                    | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                               |
| S4SGSN-FeatureList2                                                   | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                              |
| SuperChargerSupportedForGprs                                          | SGSN是否支持Super-Charger业务。                                                                                                                                                                                                                                                                                                                                                  |
| ZoneCodeStatusAtSgsn                                                  | SGSN是否支持区域漫游业务。                                                                                                                                                                                                                                                                                                                                                           |
| MCEF                                                                  | 内存溢出标志（Memory Capacity Exceed Flag）。                                                                                                                                                                                                                                                                                                                                      |
| MNRF                                                                  | 移动台不可及标志（Mobile Station Not Reachable Flag）。                                                                                                                                                                                                                                                                                                                              |
| MNRR                                                                  | 移动台不可及原因（Moblie Station Not Reachable Reason）。                                                                                                                                                                                                                                                                                                                            |
| MNRG                                                                  | 移动台GPRS不可及标志（Moblie Station Not Reachable For GPRS Flag）。                                                                                                                                                                                                                                                                                                                 |
| SupportedShortMessageMT-PP                                            | SGSN是否支持短消息终结业务。                                                                                                                                                                                                                                                                                                                                                          |
| SupportedShortMessageMO-PP                                            | SGSN是否支持短消息始发业务。                                                                                                                                                                                                                                                                                                                                                          |
| BarredSSAccess                                                        | MSC是否支持闭锁SS（supplementary service）业务。                                                                                                                                                                                                                                                                                                                                     |
| BarredOutgoingEntertainmentCall                                       | MSC是否支持闭锁高费率娱乐台。                                                                                                                                                                                                                                                                                                                                                          |
| BarredOutgoingInformationCall                                         | MSC是否支持闭锁高费率信息台。                                                                                                                                                                                                                                                                                                                                                          |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GSM)  | MSC是否支持闭锁除归属国家外的国际出呼叫。                                                                                                                                                                                                                                                                                                                                                    |
| BarredOutgoingInternationalCall (ODB Supported Features For GSM)      | MSC是否支持闭锁国际出呼叫。                                                                                                                                                                                                                                                                                                                                                           |
| BarredAllOutgoingCall (ODB Supported Features For GSM)                | MSC是否支持闭锁所有出呼叫。                                                                                                                                                                                                                                                                                                                                                           |
| BarredAllECT                                                          | MSC是否支持闭锁所有ECT业务。                                                                                                                                                                                                                                                                                                                                                         |
| BarredChargeableECT                                                   | MSC是否支持闭锁Chargeable ECT业务。                                                                                                                                                                                                                                                                                                                                                |
| BarredInternationalECT                                                | MSC是否支持闭锁International ECT业务。                                                                                                                                                                                                                                                                                                                                             |
| BarredInterzonalECT                                                   | MSC是否支持闭锁Interzonal ECT业务。                                                                                                                                                                                                                                                                                                                                                |
| BarredDECT                                                            | MSC是否支持闭锁DECT业务。                                                                                                                                                                                                                                                                                                                                                          |
| BarredMECT                                                            | MSC是否支持闭锁MECT业务。                                                                                                                                                                                                                                                                                                                                                          |
| BarredAllOutgoingCall (ODB Supported Features For GPRS)               | SGSN是否支持闭锁所有出呼叫。                                                                                                                                                                                                                                                                                                                                                          |
| BarredOutgoingInternationalCall (ODB Supported Features For GPRS)     | SGSN是否支持闭锁国际出呼叫。                                                                                                                                                                                                                                                                                                                                                          |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GPRS) | SGSN是否支持闭锁除归属国家外的国际出呼叫。                                                                                                                                                                                                                                                                                                                                                   |
| Barring of Packet Oriented Services                                   | SGSN是否支持闭锁分组业务。                                                                                                                                                                                                                                                                                                                                                           |
| MSC Supported LCS Capability Set1                                     | MSC对LCS业务Capability Set1的支持能力。                                                                                                                                                                                                                                                                                                                                            |
| MSC Supported LCS Capability Set2                                     | MSC对LCS业务Capability Set2的支持能力。                                                                                                                                                                                                                                                                                                                                            |
| SGSN Supported LCS Capability Set2                                    | SGSN对LCS业务Capability Set2的支持能力。                                                                                                                                                                                                                                                                                                                                           |
| MBRSYNC                                                               | 成员用户是否允许补充业务同步。                                                                                                                                                                                                                                                                                                                                                           |
| DENY_USSD                                                             | 成员用户USSD操作权限。                                                                                                                                                                                                                                                                                                                                                             |
| 批操作ID                                                                 | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息，并保存查询结果。                                                                                                                                                                                                                                                                                                                        |
| RELAY_NODE                                                            | 设置用户是否为中继节点。                                                                                                                                                                                                                                                                                                                                                              |
| USERATTRIBUTE                                                         | 仅当用户是MSISDN-Less用户且参数“DETAIL”取值为“TRUE”时该参数显示。用于标识用户为MSISDN-Less用户。                                                                                                                                                                                                                                                                                                        |
| CS_ROAMPERTPL_ID                                                      | 用于返回用户签约的CS域优选漫游模板ID。                                                                                                                                                                                                                                                                                                                                                     |
| PS_ROAMPERTPL_ID                                                      | 用于返回用户签约的PS域优选漫游模板ID。                                                                                                                                                                                                                                                                                                                                                     |
| Server-Assignment-Time                                                | 用于返回SWx接口位置更新成功的时间戳。                                                                                                                                                                                                                                                                                                                                                      |
| NON3GPPRATTYPE                                                        | 用于返回用户终端的Non-3GPP无线网络接入类型。 WLANCDMA2000_1XHRPDUMBEHRPD                                                                                                                                                                                                                                                                                                                    |
| RATTYPE                                                               | 用于返回用户终端接入网络的无线接入技术类型。 Dynamic Status Information For MMEUTRANGERANGANHSPA_EVOLUTIONEUTRANEUTRAN-NB-IoT Dynamic Status Information For AMFNREUTRAWLANVIRTUALNR_REDCAP                                                                                                                                                                                                     |
| NONIPAPNFLAG                                                          | 是否是Non-IP PDN类型的APN。                                                                                                                                                                                                                                                                                                                                                      |
| ISDYNNSA                                                              | 用户是否为NSA动态用户。 取值范围： 0：4G注册状态。1：5G NSA注册状态。                                                                                                                                                                                                                                                                                                                                |
| APNENHANCEFLAG                                                        | 用户是否启用APN下发增强特性。FALSE：未启用APN下发增强特性。TRUE：启用APN下发增强特性。                                                                                                                                                                                                                                                                                                                      |
| INGROUPID                                                             | 用于返回移动网络内部设备之间通信时互相传递的组ID。                                                                                                                                                                                                                                                                                                                                                |
| SHAREDID                                                              | 用于返回为内部组创建的共享数据的ID。                                                                                                                                                                                                                                                                                                                                                       |
| IP USSD                                                               | 用于返回动态IP-USSD-AS地址。当参数“是否返回详细信息”取值为“TRUE”时显示。                                                                                                                                                                                                                                                                                                                             |
| NSAAUTOPROV                                                           | 用户是否为NSA自动开户用户，该参数仅在用户触发NSA自动开户流程后才会显示。 取值范围： FALSE：非NSA自动开户用户。TRUE：已发送通知消息并收到成功响应的NSA自动开户用户。AUTOTONSA_NN：已发送通知消息未收到成功响应的NSA自动开户用户。                                                                                                                                                                                                                                       |
| BSXX/TSXX                                                             | 用于显示当前用户的自定义承载能力，通过LST ISDNBCALIAS命令可以查询该用户自定义承载能力的详细信息。该参数仅在“是否返回详细信息”取值为“TRUE”时显示。                                                                                                                                                                                                                                                                                      |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释       | 原因分析                                                                                                                           | 处理建议                                                                                                                    |
|:--------|:------------|:-------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值      | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                                                       | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失        | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                                              | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到       | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                                               | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突        | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。                             | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户       | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                         | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法  | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                                          | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |
| ERR1150 | 操作员无权限管理该用户 | 当“PROVRIGHTSWITCH（营帐权限开关）”和“SERVICERIGHTSWITCH（业务权限开关）”为默认值，同时“NPSWITCH（NP 开关）”为“2”时，某虚拟HLRSN的操作员登录客户端后执行该命令对其它虚拟HLRSN的用户进行操作。 | 请联系华为技术支持处理。                                                                                                            |