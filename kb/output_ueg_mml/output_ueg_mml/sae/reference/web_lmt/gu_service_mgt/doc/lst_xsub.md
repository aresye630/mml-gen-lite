# 查询XML格式的用户信息(LST XSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于SOAP接口从内存库查询用户的静态数据和动态数据，主要包括用户签约的各种业务信息。

**说明** 

- 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
- 在从运营商网络获取数据前，必须要获得运营商的授权。
- 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

“IMSI”和“MSISDN”是条件可选参数，必须有且只能有一个参数出现。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                       |
|:-------|:-------|:-----------------------------------------------------------|
| IMSI   | IMSI   | 用于标识要查询哪个IMSI号码对应的静态和动态数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| ISDN   | MSISDN | 用于标识要查询哪个MSISDN号码对应的静态和动态数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |

## 使用实例

查询“IMSI”号码为“460000009012345”的用户签约的各种业务信息。

```
LST XSUB: IMSI="460000009012345";
```

```
%%LST XSUB: IMSI="460000009012345";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                         HLRSN = 1
                          IMSI = 460000009012345
                      CardType = USIM
                           NAM = BOTH
                      CATEGORY = COMMON
                          SMDP = MSC
                     XSUB_ISDN = 111111111111111
                     INDICATOR = MASTER
           XSUB_DEFAULTCALL_TS = TS11
                     DSCODE_TS = TS11
                                 TS12
                           ARD = PROV
               NR5GSNOTALLOWED = TRUE
                 EPCNOTALLOWED = TRUE
                 NGCNOTALLOWED = TRUE
                     CfSerCode = CFU
                           CFU = NOTPROV
                     CfSerCode = CFB
                           CFB = NOTPROV
                     CfSerCode = CFNRY
                         CFNRY = NOTPROV
                     CfSerCode = CFNRC
                         CFNRC = NOTPROV
                     CfSerCode = CFD
                           CFD = NOTPROV
                         CBCOU = SUBSCRIBER
                     CbSerCode = BAOC
                          BAOC = NOTPROV
                     CbSerCode = BOIC
                          BOIC = NOTPROV
                     CbSerCode = BOICEXHC
                      BOICEXHC = NOTPROV
                     CbSerCode = BORO
                          BORO = NOTPROV
                     CbSerCode = BAIC
                          BAIC = NOTPROV
                     CbSerCode = BICROAM
                       BICROAM = NOTPROV
                          CLIP = NOTPROV
                          CLIR = NOTPROV
                          COLP = NOTPROV
                          COLR = NOTPROV
                            CW = NOTPROV
                          HOLD = NOTPROV
                          MPTY = NOTPROV
                          CNAP = NOTPROV
                         EMLPP = NOTPROV
                     EMLPP_COU = SUBSCRIBER
                           CUG = NOTPROV
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
                           ECT = NOTPROV
                            MC = NOTPROV
                          AOCI = NOTPROV
                          AOCC = NOTPROV
                        CCBS_A = NOTPROV
                        CCBS_B = PROV
                         ODBOC = NOBOC
                         ODBIC = NOBIC
                       ODBROAM = NOBAR
                       ODBINFO = FALSE
                       ODBENTE = FALSE
                         ODBSS = FALSE
                        ODBECT = NOBECT
                       ODBDECT = FALSE
                       ODBMECT = FALSE
                        ODBPOS = NOBPOS
                    ODBPOSTYPE = BOTH
                        ODBRCF = NOBRCF
                        ODBPB1 = FALSE
                        ODBPB2 = FALSE
                        ODBPB3 = FALSE
                        ODBPB4 = FALSE
                   ODBENTEROAM = FALSE
                   ODBINFOROAM = FALSE
                BROLOCDOMEGPRS = FALSE
          BROCROSSDOMESTICGPRS = FALSE
               BROLOCINTERGPRS = FALSE
             BROCROSSINTERGPRS = FALSE
                        TIFCSI = NOTPROV
                          SKEY = 0
                        GSM_IC = FALSE
                        GSM_OC = FALSE
                      GPRSLOCK = FALSE
                       EPSLOCK = FALSE
                   Non3GPPLOCK = FALSE
                      CSUPLLCK = FALSE
                      PSUPLLCK = FALSE
                    SABLOCK_IC = FALSE
                    SABLOCK_OC = FALSE
                      RROption = ALL_PLMNS
                         RZONE = 0
                 CHARGE_GLOBAL = NONE
                        CNTXID = 3
                       PDPTYPE = IPV4IPV6
                        ADDIND = DYNAMIC ADDRESS
                       ADD2IND = STATIC ADDRESS
                    PDPADDIPV4 = 192.168.52.12
                         VPLMN = TRUE
                     STDCHARGE = 1234
                    APNOITPLID = 2
                   GPRSPDPTYPE = IPV4IPV6
                    GPRSADDIND = DYNAMIC ADDRESS
                GPRSPDPADDIPV4 = 192.168.52.12
                   GPRSADD2IND = STATIC ADDRESS
                        RELCLS = ACKALLPRODT
                      DELAYCLS = DELAY1
                        PRECLS = HIGH
                       PEAKTHR = 16000 OCT
                       MEANTHR = 5000 OCT
                           APN = APN
                     GPRSVPLMN = TRUE
                 GPRSSTDCHARGE = 1234
                GPRSAPNOITPLID = 2
                           VBS = NOTPROV
                          VGCS = NOTPROV
                     AMBRUL-UE = 123456
                     AMBRDL-UE = 123456
                           EGR = NOTPROV
                   LTEAUTOPROV = FALSE
                           MPS = FALSE
                        ICSIND = FALSE
                        ANCHOR = FALSE
                      TAUTIMER = 0
                    RELAY_NODE = FALSE
                     EPSODBPOS = NOBPOS
                   RAUTAUTIMER = 10
                   ACTIVETIMER = 10
               EUTRANEDRXCYCLE = 10
                NBIOTEDRXCYCLE = 10
                       NSAFLAG = TRUE 
                   NSAAUTOPROV = TRUE
                         WBPTW = 1
                         NBPTW = 1
                    CNTXID_EPS = 1
                  APNTPLID_EPS = 100
                DEFAULTAPN_EPS = TRUE
               WILDCARDAPN_EPS = FALSE
                   EPSQOSTPLID = 100
                   PDPTYPE_EPS = IPV4IPV6
                    ADDIND_EPS = DYNAMIC ADDRESS
                   ADD2IND_EPS = DYNAMIC ADDRESS
              VPLMNALLOWED_EPS = FALSE
                    CHARGE_EPS = NORMAL
                    CNTXID_EPS = 2
                  APNTPLID_EPS = 200
                DEFAULTAPN_EPS = TRUE
               WILDCARDAPN_EPS = FALSE
                   EPSQOSTPLID = 100
                   PDPTYPE_EPS = IPV4IPV6
                    ADDIND_EPS = DYNAMIC ADDRESS
                   ADD2IND_EPS = DYNAMIC ADDRESS
              VPLMNALLOWED_EPS = FALSE
                    CHARGE_EPS = NORMAL
              NONIPAPNFLAG_EPS = TRUE
                    ZCLOCKPROV = FALSE
                       MOSMSBR = FALSE
         NSSAIINCLUSIONALLOWED = TRUE
                          CARP = NOTPROV
                    ACR_STATUS = NOTPROV
                           ALS = NOTPROV
                           CPP = NOTPROV
                           DIC = NOTPROV
                          ELCS = NOTPROV
                        FMInit = NOTPROV
                  FMSupervisor = NOTPROV
                      FMRemote = NOTPROV
                           IST = NOTPROV
                       NIRPROV = FALSE
                    ODBPREMSMS = FALSE
                   ODBADULTSMS = FALSE
                         SMSCF = NOTPROV
                          UUS1 = NOTPROV
                          UUS2 = NOTPROV
                          UUS3 = NOTPROV
                          VVDN = NOTPROV
                           ICI = FALSE
                           DND = TRUE
                          VMCC = TRUE
                 ANCHORTCSI_ID = 111
                  USERCATEGORY = NORMAL
                   IMEILCKPROV = FALSE
                     M2MNOTIFY = NOTPROV
            MsPurgedForNonGprs = FALSE
                    VLRInHplmn = TRUE
              VLRInHomeCountry = TRUE
                     VLRInArea = FALSE
                RequireCheckSS = FALSE
RoamingRestrictInMscDueToUnsupportedFeature
                               = FALSE
   MscOrVlrAreaRoamingRestrict = FALSE
   ODBarredForUnsupportedCamel = FALSE
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
            BaocForVlrRestrict = FALSE
                    MCEFforGSM = FALSE
                          MNRF = FALSE
                    MNRRforGSM = No Reason for Non-GPRS
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
     SupportedCamelPhase3_SGSN = FALSE
     SupportedCamelPhase4_SGSN = FALSE
  SuperChargerSupportedForGprs = networkNode_AreaRestricted
          ZoneCodeStatusAtSgsn = zoneCodesSupported
                   MCEFforGPRS = FALSE
                          MNRG = FALSE
                   MNRRforGPRS = No Reason
     SupportedShortMessageMTPP = TRUE
     SupportedShortMessageMOPP = TRUE
                       MMEHOST = saehss1.huawei.com
                      MMEREALM = huawei.com
                     M-RATTYPE = UTRAN
                           VNI = 45.460.com
                     REGSTATUS = NOT_REGISTERED
             TGPPAAASERVERNAME = saehss3.huawei.com
            TGPPAAASERVERREALM = huawei.com
                    AAA-IMEISV = 01
              NON_3GPP_RATTYPE = HRPD
IMS-VO-PS-Sessions-Supported_MME
                               = UNKNOWN
       UE-SRVCC-Capability_MME = UE-SRVCC-NOT-SUPPORTED
                      ISDYNNSA = 1
                  PURGEDONSGSN = FALSE
                S-AREARESTRICT = FALSE
                 IP_USSD_AS_GT = 8613966666
                BarredSSAccess = TRUE
BarredOutgoingEntertainmentCall
                               = TRUE
 BarredOutgoingInformationCall = TRUE
SupGSMODB-BarredOutgoingInternationalCallExHC
                               = TRUE
SupGSMODB-BarredOutgoingInternationalCall
                               = TRUE
SupGSMODB-BarredAllOutgoingCall
                               = TRUE
                  BarredAllECT = TRUE
           BarredChargeableECT = TRUE
        BarredInternationalECT = TRUE
           BarredInterzonalECT = TRUE
                    BarredDECT = TRUE
                    BarredMECT = TRUE
SupGPRSODB-BarredAllOutgoingCall
                               = TRUE
SupGPRSODB-BarredOutgoingInternationalCall
                               = TRUE
SupGPRSODB-BarredOutgoingInternationalCallExHC
                               = TRUE
BarringofPacketOrientedServices
                               = TRUE
 MSCSupportedLCSCapabilitySet1 = FALSE
 MSCSupportedLCSCapabilitySet2 = FALSE
SGSNSupportedLCSCapabilitySet2 = FALSE
                       ALS_DYN = FALSE
                      VVDN_DYN = FALSE
                          BS20 = BS20
                          BS22 = BS22

Total count = 272

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

**MOD NGSRRS**

、

**ADD SNSSAI**

和

**ADD SMDATA**

命令的参数说明。表1列出的是未包含在

**ADD SUB**

、

**MOD LCK**

、

**MOD AMDATA**

、

**MOD NGSRRS**

、

**ADD SNSSAI**

和

**ADD SMDATA**

命令的参数说明中的输出项。

| 输出项名称                                                                 | 输出项解释                                                                                                                                                                                                                                                                                                                                                                    |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUB_AGE                                                               | 用户的年龄指数（在Super-Charger业务中使用）。                                                                                                                                                                                                                                                                                                                                            |
| SPN                                                                   | 用于返回用户是否签约SPN（Single Personal Number）业务。 PROV：用户签约SPN业务。 NOTPROV：用户没有签约SPN业务。                                                                                                                                                                                                                                                                                            |
| TPLID                                                                 | 用于返回用户签约的通过SPN业务对应的OFA模板ID。                                                                                                                                                                                                                                                                                                                                              |
| FTN                                                                   | 用于返回用户签约的SPN前转号码。                                                                                                                                                                                                                                                                                                                                                        |
| STATUS                                                                | 用于返回用户的呼叫前转状态。 PROV：签约。 REG：登记。 ACT：激活。 QUIESCENT：静止。                                                                                                                                                                                                                                                                                                                    |
| PERMANENTIND                                                          | 用于返回用户接入的APN是否是永久APN。 TRUE：永久APN。FALSE：非永久APN。                                                                                                                                                                                                                                                                                                                           |
| BaocForVlrRestrict                                                    | 是否限制除短消息以外的所有出呼业务。                                                                                                                                                                                                                                                                                                                                                       |
| MsPurgedForNonGprs                                                    | CS域用户是否被purge。                                                                                                                                                                                                                                                                                                                                                           |
| VLRInHplmn                                                            | 用户是否在本网的VLR漫游。                                                                                                                                                                                                                                                                                                                                                           |
| VLRInHomeCountry                                                      | 用户是否在本网所在的国家的VLR漫游。                                                                                                                                                                                                                                                                                                                                                      |
| VLRInArea                                                             | 用户是否在本地的VLR漫游。                                                                                                                                                                                                                                                                                                                                                           |
| RequireCheckSS                                                        | 位置更新时是否发起checkSS流程。                                                                                                                                                                                                                                                                                                                                                      |
| RoamingRestrictInMscDueToUnsupportedFeature                           | 是否由于MSC/VLR不支持某些业务导致漫游受限。                                                                                                                                                                                                                                                                                                                                                |
| MscOrVlrAreaRoamingRestrict                                           | 用户是否在CS域漫游受限。                                                                                                                                                                                                                                                                                                                                                            |
| ODBarredForUnsupportedCamel                                           | 是否由于MSC/VLR不支持某些版本的CAMEL导致ODB闭锁。                                                                                                                                                                                                                                                                                                                                         |
| SupportedCamelPhase1                                                  | MSC/VLR是否支持CAMEL Phase 1。                                                                                                                                                                                                                                                                                                                                                |
| SupportedCamelPhase2                                                  | MSC/VLR是否支持CAMEL Phase 2。                                                                                                                                                                                                                                                                                                                                                |
| SupportedCamelPhase3                                                  | MSC/VLR是否支持CAMEL Phase 3。                                                                                                                                                                                                                                                                                                                                                |
| SupportedCamelPhase4                                                  | MSC/VLR是否支持CAMEL Phase 4。                                                                                                                                                                                                                                                                                                                                                |
| SRIMsrnCfActive                                                       | PLMNSS业务是否激活。                                                                                                                                                                                                                                                                                                                                                            |
| ZoneCodeStatusAtMsc                                                   | MSC/VLR是否支持区域漫游业务。                                                                                                                                                                                                                                                                                                                                                       |
| longGroupIDSupported                                                  | MSC/VLR是否支持长组ID。                                                                                                                                                                                                                                                                                                                                                         |
| basicISTSupported                                                     | MSC/VLR是否支持基本的IST业务。                                                                                                                                                                                                                                                                                                                                                     |
| istCommandSupported                                                   | MSC/VLR是否支持强制下发方式的IST业务。                                                                                                                                                                                                                                                                                                                                                 |
| SuperChargerSupportedForGsm                                           | MSC/VLR是否支持Super-Charger业务。                                                                                                                                                                                                                                                                                                                                              |
| ECATEGORYAtMsc                                                        | MSC/VLR是否支持增强用户类别业务。                                                                                                                                                                                                                                                                                                                                                     |
| LSFLAG                                                                | 用户是否正在进行位置更新。                                                                                                                                                                                                                                                                                                                                                            |
| camelInduceBarringSMS                                                 | CAMEL业务导致的短消息闭锁。                                                                                                                                                                                                                                                                                                                                                         |
| CS-MSISDN-LESS                                                        | 用于表示用户在CS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                         |
| CSRATTYPE                                                             | 用于表示用户在CS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA和E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                       |
| CsUplStatus                                                           | 表示用户的CS域位置更新的状态。“Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向VLR下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置CsUplStatus的值。场景一：位置更新中创建的全网跟踪超时。场景二：HLR收到VLR发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景三：VLR对HLR发来的ISD消息响应超时。场景四：HLR收到VLR发来的其他错误响应。 场景一和场景二，设置CsUplStatus为Exception。场景三和四，设置CsUplStatus为TimeOut。 |
| longFTNSupported                                                      | 用于表示VLR是否支持长前转号码，当VLR不支持长前转号码时不显示。                                                                                                                                                                                                                                                                                                                                       |
| BaocForVlrRestrict                                                    | 是否限制除短消息以外的所有出呼业务。                                                                                                                                                                                                                                                                                                                                                       |
| SgsnInHplmn                                                           | 用户是否在本网的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                          |
| MsPurgedForGprs                                                       | PS域用户是否被purge。                                                                                                                                                                                                                                                                                                                                                           |
| SgsnInHomeCountry                                                     | 用户是否在本网所在的国家的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                     |
| SgsnInArea                                                            | 用户是否在本地的SGSN漫游。                                                                                                                                                                                                                                                                                                                                                          |
| RoamingRestrictInSgsnDueToUnsupportedFeature                          | 是否由于SGSN不支持某些业务导致漫游受限。                                                                                                                                                                                                                                                                                                                                                   |
| SgsnAreaRoamingRestrict                                               | 用户是否在PS域漫游受限。                                                                                                                                                                                                                                                                                                                                                            |
| ODBarredForUnsupportedCamelForGprs                                    | 是否由于SGSN不支持某些版本的CAMEL导致ODB闭锁。                                                                                                                                                                                                                                                                                                                                            |
| PS-MSISDN-LESS                                                        | 用于表示用户在PS域是否支持M2M MSISDN-less属性。                                                                                                                                                                                                                                                                                                                                         |
| PSRATTYPE                                                             | 用于表示用户在PS域的无线接入类型。 说明：该返回值只有当RAT记录有效（即为UTRAN、GERAN、GAN、I-HSPA和E-UTRAN这几个无线接入类型中的一个或多个）且ARD增强特性开关打开（即SET MAPCONF命令中的“是否支持ARD增强处理”参数取值为“TRUE”）时才会显示。                                                                                                                                                                                                                       |
| PsUplStatus                                                           | 表示用户的PS域位置更新的状态。“Normal”表示位置更新正常。“TimeOut”表示位置更新超时。“Exception”表示位置更新异常。 说明：当用户发起位置更新流程后，HSS更新完用户动态数据之后，向SGSN下发ISD消息，如果SET MAPCONF命令中的“是否记录UPL状态”参数取值为“TRUE”且发生以下场景时，需要设置PsUplStatus的值。场景一：HLR收到SGSN发来的PABORT、NOTICE、CLOSE、UABORT或用户未定义的异常消息。场景二：SGSN对HLR发来的ISD消息响应超时。场景三：HLR收到SGSN发来的其他错误响应。 场景一，设置PsUplStatus为Exception。场景二和场景三，设置PsUplStatus为TimeOut。                  |
| MME-FeatureList                                                       | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                 |
| MME-FeatureList2                                                      | 表示用户的MME特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                                |
| S4SGSN-FeatureList                                                    | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                              |
| S4SGSN-FeatureList2                                                   | 表示用户的S4SGSN特性支持能力，取值中各比特位对应特性请参见FeatureList2与各比特位之间的对应关系。 比特位取值为1，表示支持该特性能力。                                                                                                                                                                                                                                                                                             |
| SuperChargerSupportedForGprs                                          | SGSN是否支持Super-Charger业务。                                                                                                                                                                                                                                                                                                                                                 |
| ZoneCodeStatusAtSgsn                                                  | SGSN是否支持区域漫游业务。                                                                                                                                                                                                                                                                                                                                                          |
| MCEF                                                                  | 内存溢出标志（Memory Capacity Exceed Flag）。                                                                                                                                                                                                                                                                                                                                     |
| MNRF                                                                  | 移动台不可及标志（Mobile Station Not Reachable Flag）。                                                                                                                                                                                                                                                                                                                             |
| MNRR                                                                  | 移动台不可及原因（Moblie Station Not Reachable Reason）。                                                                                                                                                                                                                                                                                                                           |
| MNRG                                                                  | 移动台GPRS不可及标志（Moblie Station Not Reachable For GPRS Flag）。                                                                                                                                                                                                                                                                                                                |
| SupportedShortMessageMT-PP                                            | SGSN是否支持短消息终结业务。                                                                                                                                                                                                                                                                                                                                                         |
| SupportedShortMessageMO-PP                                            | SGSN是否支持短消息始发业务。                                                                                                                                                                                                                                                                                                                                                         |
| BarredSSAccess                                                        | MSC是否支持闭锁SS（supplementary service）业务。                                                                                                                                                                                                                                                                                                                                    |
| BarredOutgoingEntertainmentCall                                       | MSC是否支持闭锁高费率娱乐台。                                                                                                                                                                                                                                                                                                                                                         |
| BarredOutgoingInformationCall                                         | MSC是否支持闭锁高费率信息台。                                                                                                                                                                                                                                                                                                                                                         |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GSM)  | MSC是否支持闭锁除归属国家外的国际出呼叫。                                                                                                                                                                                                                                                                                                                                                   |
| BarredOutgoingInternationalCall (ODB Supported Features For GSM)      | MSC是否支持闭锁国际出呼叫。                                                                                                                                                                                                                                                                                                                                                          |
| BarredAllOutgoingCall (ODB Supported Features For GSM)                | MSC是否支持闭锁所有出呼叫。                                                                                                                                                                                                                                                                                                                                                          |
| BarredAllECT                                                          | MSC是否支持闭锁所有ECT业务。                                                                                                                                                                                                                                                                                                                                                        |
| BarredChargeableECT                                                   | MSC是否支持闭锁Chargeable ECT业务。                                                                                                                                                                                                                                                                                                                                               |
| BarredInternationalECT                                                | MSC是否支持闭锁International ECT业务。                                                                                                                                                                                                                                                                                                                                            |
| BarredInterzonalECT                                                   | MSC是否支持闭锁Interzonal ECT业务。                                                                                                                                                                                                                                                                                                                                               |
| BarredDECT                                                            | MSC是否支持闭锁DECT业务。                                                                                                                                                                                                                                                                                                                                                         |
| BarredMECT                                                            | MSC是否支持闭锁MECT业务。                                                                                                                                                                                                                                                                                                                                                         |
| BarredAllOutgoingCall (ODB Supported Features For GPRS)               | SGSN是否支持闭锁所有出呼叫。                                                                                                                                                                                                                                                                                                                                                         |
| BarredOutgoingInternationalCall (ODB Supported Features For GPRS)     | SGSN是否支持闭锁国际出呼叫。                                                                                                                                                                                                                                                                                                                                                         |
| BarredOutgoingInternationalCallExHC (ODB Supported Features For GPRS) | SGSN是否支持闭锁除归属国家外的国际出呼叫。                                                                                                                                                                                                                                                                                                                                                  |
| Barring of Packet Oriented Services                                   | SGSN是否支持闭锁分组业务。                                                                                                                                                                                                                                                                                                                                                          |
| MSC Supported LCS Capability Set1                                     | MSC对LCS业务Capability Set1的支持能力。                                                                                                                                                                                                                                                                                                                                           |
| MSC Supported LCS Capability Set2                                     | MSC对LCS业务Capability Set2的支持能力。                                                                                                                                                                                                                                                                                                                                           |
| SGSN Supported LCS Capability Set2                                    | SGSN对LCS业务Capability Set2的支持能力。                                                                                                                                                                                                                                                                                                                                          |
| CS_ISD                                                                | 表示CS域的插入用户数据用户消息是否被重发。                                                                                                                                                                                                                                                                                                                                                   |
| CS_DSD                                                                | 表示CS域的删除用户数据消息是否被重发。                                                                                                                                                                                                                                                                                                                                                     |
| CS_CLR                                                                | 表示CS域的cancel消息是否被重发。                                                                                                                                                                                                                                                                                                                                                     |
| PS_ISD                                                                | 表示PS域的插入用户数据消息是否被重发。                                                                                                                                                                                                                                                                                                                                                     |
| PS_DSD                                                                | 表示PS域的删除用户数据消息是否被重发。                                                                                                                                                                                                                                                                                                                                                     |
| PS_CLR                                                                | 表示PS域的cancel消息是否被重发。                                                                                                                                                                                                                                                                                                                                                     |
| S6a_IDR                                                               | 表示S6a接口的下发用户数据消息是否被重发。                                                                                                                                                                                                                                                                                                                                                   |
| S6a_CLR                                                               | 表示S6a接口的cancel消息是否被重发。                                                                                                                                                                                                                                                                                                                                                   |
| S6d_IDR                                                               | 表示S6d接口的下发用户数据消息是否被重发。                                                                                                                                                                                                                                                                                                                                                   |
| S6d_CLR                                                               | 表示S6d接口的cancel消息是否被重发。                                                                                                                                                                                                                                                                                                                                                   |
| UDCD                                                                  | 表示MAP的ADD通知消息是否被重发。                                                                                                                                                                                                                                                                                                                                                      |
| DataRef                                                               | 用于返回Sh接口上AS向HSS请求订阅的用户数据类型。当前版本仅实现了返回“UERSVCCCAP”，即UE-SRVCC-Capability数据。                                                                                                                                                                                                                                                                                                |
| AS_Host_Name                                                          | 用于返回AS的主机名。                                                                                                                                                                                                                                                                                                                                                              |
| AS_Realm_Name                                                         | 用于返回AS所在的域名。                                                                                                                                                                                                                                                                                                                                                             |
| MBRSYNC                                                               | 成员用户是否允许补充业务同步。                                                                                                                                                                                                                                                                                                                                                          |
| DENY_USSD                                                             | 成员用户USSD操作权限。                                                                                                                                                                                                                                                                                                                                                            |
| RELAY_NODE                                                            | 设置用户是否为中继节点。                                                                                                                                                                                                                                                                                                                                                             |
| USERATTRIBUTE                                                         | 仅当用户是MSISDN-Less用户且参数“DETAIL”取值为“TRUE”时该参数显示。用于标识用户为MSISDN-Less用户。                                                                                                                                                                                                                                                                                                       |
| CS_ROAMPERTPL_ID                                                      | 用于返回用户签约的CS域优选漫游模板ID。                                                                                                                                                                                                                                                                                                                                                    |
| PS_ROAMPERTPL_ID                                                      | 用于返回用户签约的PS域优选漫游模板ID。                                                                                                                                                                                                                                                                                                                                                    |
| Server-Assignment-Time                                                | 用于返回SWx接口位置更新成功的时间戳。                                                                                                                                                                                                                                                                                                                                                     |
| NON3GPPRATTYPE                                                        | 用于返回用户终端的Non-3GPP无线网络接入类型。 WLANCDMA2000_1XHRPDUMBEHRPD                                                                                                                                                                                                                                                                                                                   |
| M-RATTYPE                                                             | 用于返回用户终端通过S6a接口接入网络的无线接入技术类型。 UTRANGERANGANHSPA_EVOLUTIONEUTRANEUTRAN-NB-IoT                                                                                                                                                                                                                                                                                             |
| NONIPAPNFLAG                                                          | 是否是Non-IP PDN类型的APN。                                                                                                                                                                                                                                                                                                                                                     |
| P-CSCF Restoration                                                    | MME/SGSN是否支持P-CSCF恢复流程。                                                                                                                                                                                                                                                                                                                                                  |
| Dedicated Core Networks                                               | MME/SGSN是否支持专用核心网。                                                                                                                                                                                                                                                                                                                                                       |
| Non-IP PDN Type APNs                                                  | MME/SGSN是否支持无IP PDN类型的APN。                                                                                                                                                                                                                                                                                                                                               |
| NR as Secondary RAT                                                   | MME/SGSN是否支持NR作为辅助RAT。                                                                                                                                                                                                                                                                                                                                                   |
| AMF_DYN_ID                                                            | 用于返回AMF的动态ID。                                                                                                                                                                                                                                                                                                                                                            |
| AMFINSTANCEID                                                         | 用于返回用户在NRF注册时的AMF标识。                                                                                                                                                                                                                                                                                                                                                     |
| SUPPORTEDFEATURES                                                     | 用于返回AMF的特性支持能力。 取值范围：16进制字符串，bit0为最右边字符的最低bit位。每个bit位表示一个特性支持能力。                                                                                                                                                                                                                                                                                                         |
| PURGEFLAG                                                             | 用于返回AMF在UDM中是否被去注册。 取值范围：TRUE：已经被去注册。 FALSE：未被去注册。                                                                                                                                                                                                                                                                                                                       |
| IMSVOPS                                                               | 用于返回AMF是否支持IMS VoPS能力。 取值范围： NOT SUPPORT：不支持。 SUPPORT：支持。 UNKNOWN：未知状态。                                                                                                                                                                                                                                                                                                  |
| DEREGCALLBACKURI                                                      | 用于返回UDM给AMF发送去注册时，消息中的URI取值。                                                                                                                                                                                                                                                                                                                                             |
| REGTIME                                                               | 用于返回用户最近一次注册时间。                                                                                                                                                                                                                                                                                                                                                          |
| MCC                                                                   | 用于标识移动国家码。                                                                                                                                                                                                                                                                                                                                                               |
| MNC                                                                   | 用于标识移动网络码。                                                                                                                                                                                                                                                                                                                                                               |
| AMFID                                                                 | 用于返回AMF的标识。                                                                                                                                                                                                                                                                                                                                                              |
| URRP_AMF                                                              | 用于返回UE在AMF上的可达性状态。 取值范围：UNREACHABLE：不可达。 REACHABLE：可达。 REGULATORY_ONLY：仅用于管理策略优先级服务。                                                                                                                                                                                                                                                                                     |
| RATTYPE                                                               | 用于返回用户终端接入5G网络的无线接入技术类型。 NREUTRAWLANVIRTUALNR_REDCAP                                                                                                                                                                                                                                                                                                                     |
| ISDYNNSA                                                              | 用户是否为NSA动态用户。 取值范围： 0：4G注册状态。1：5G NSA注册状态。                                                                                                                                                                                                                                                                                                                               |
| APNENHANCEFLAG                                                        | 用户是否启用APN下发增强特性。 FALSE：未启用APN下发增强特性。TRUE：启用APN下发增强特性。                                                                                                                                                                                                                                                                                                                    |
| IP USSD                                                               | 用于返回动态IP-USSD-AS地址。                                                                                                                                                                                                                                                                                                                                                      |
| NSAAUTOPROV                                                           | 用户是否为NSA自动开户用户，该参数仅在用户触发NSA自动开户流程后才会显示。 取值范围： FALSE：非NSA自动开户用户。TRUE：已发送通知消息并收到成功响应的NSA自动开户用户。AUTOTONSA_NN：已发送通知消息未收到成功响应的NSA自动开户用户。                                                                                                                                                                                                                                      |
| BSXX/TSXX                                                             | 用于显示当前用户的自定义承载能力，通过LST ISDNBCALIAS命令可以查询改用户自定义承载能力的详细信息。                                                                                                                                                                                                                                                                                                                 |