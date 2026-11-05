# 查询开户模板(LST SUBTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于查询开户模板。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                     |
|:-------|:-------|:-----------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。 |
| TPLID  | 模板ID   | 在模板ID列表框中选择模板的ID，模板ID的值域为0～65534。        |

## 使用实例

1. 查询“HLR序列号”为“1”的用户开户模板信息：

   ```
   LST SUBTPL: HLRSN=1;
   ```

   ```
   %%LST SUBTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLTYPE      TPLNAME
                  1            NORMAL       <NULL>
                  2            NORMAL       <NULL>
                  33           NORMAL       <NULL>
                  55           NORMAL       <NULL>
                  69           NORMAL       <NULL>

   Total count = 5

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”、“模板ID”为“6”的用户开户模板信息：

   ```
   LST SUBTPL: HLRSN=1, TPLID=6;
   ```

   ```
   %%LST SUBTPL: HLRSN=1, TPLID=6;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 6
                          TPLTYPE = NORMAL
                          TPLNAME = <NULL>
                         CARDTYPE = SIM
                              NAM = BOTH
                         CATEGORY = COMMON
                     USERCATEGORY = NORMAL
                       ZCLOCKPROV = FALSE
                              ICI = FALSE

   "Basic Service"
                       Emergency Call (TS12)
                      DEFAULTCALL = Telephony (TS11)

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
                          CFU NCS = FALSE
                          CFU COU = SUBSCRIBER
                              CFB = NOTPROV
                          CFB NFS = FALSE
                          CFB NCS = FALSE
                          CFB COU = SUBSCRIBER
                            CFNRY = NOTPROV
                        CFNRY NFS = FALSE
                        CFNRY NCS = FALSE
                        CFNRY COU = SUBSCRIBER
                            CFNRC = NOTPROV
                        CFNRC NCS = FALSE
                        CFNRC COU = SUBSCRIBER
                              CFD = NOTPROV
                      SUPINTERCFD = FALSE
                          CFD NFS = FALSE
                          CFD NCS = FALSE
                     CFD_SHORTNUM = FALSE
                         CFD TS1X = FALSE
                         CFD TS6X = FALSE
                         CFD BS2X = FALSE
                         CFD BS3X = FALSE
                       CFD NRTIME = 0
                             BAOC = NOTPROV
                           CB COU = SUBSCRIBER
                             BOIC = NOTPROV
                           CB COU = SUBSCRIBER
                         BOICEXHC = NOTPROV
                           CB COU = SUBSCRIBER
                             BORO = NOTPROV
                             BAIC = NOTPROV
                           CB COU = SUBSCRIBER
                          BICROAM = NOTPROV
                           CB COU = SUBSCRIBER
                             CLIP = NOTPROV
                     CLIPOVERRIDE = TRUE
                             CNAP = NOTPROV
                             CLIR = NOTPROV
                         CLIRMODE = PERMANENT
                             COLP = NOTPROV
                     COLPOVERRIDE = TRUE
                             COLR = NOTPROV
                              ECT = NOTPROV
                               CW = NOTPROV
                             HOLD = NOTPROV
                             MPTY = NOTPROV
                               MC = NOTPROV
                             AOCI = NOTPROV
                             AOCC = NOTPROV
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
                       ACR_STATUS = NOTPROV

   "TIF-CSI"
                          TIF-CSI = NOTPROV

                             SMDP = Deliver From MSC
                         NAEA_CIC = NOTPROV
                           NLRInd = NONE
                             VVDN = NOTPROV
                              ARD = PROV
                  UTRANNOTALLOWED = TRUE
                  GERANNOTALLOWED = TRUE
                  NR5GSNOTALLOWED = FALSE
                   WLANNOTALLOWED = FALSE
            CDMA2000_1XNOTALLOWED = FALSE
                   HRPDNOTALLOWED = FALSE
                    UMBNOTALLOWED = FALSE
                  EHRPDNOTALLOWED = FALSE
                             CARP = NOTPROV
                         RROption = ALL_PLMNS
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER
                              VBS = NOTPROV
                             VGCS = NOTPROV
                        ECATEGORY = NOTPROV
                              IST = NOTPROV
                              DIC = NOTPROV
                    ROUTECATEGORY = NOTPROV
                     CALLREDIRECT = NOTPROV
                            MERBT = NOTPROV
                EXEXROUTECATEGORY = NOTPROV
                          NIRPROV = FALSE
                            RZONE = 0
                             CCBS = NOTPROV
                       CCBSTARGET = PROV
                        SMSINPROV = FALSE
                             SKEY = 0
                             TAMM = FALSE
                              CPP = NOTPROV
                             ELCS = NOTPROV
                       ODBPREMSMS = FALSE
                      ODBADULTSMS = FALSE
                         STE_PROV = FALSE
                             VMCC = FALSE
   "EPS Data"
                        AMBRMAXUL = 200
                        AMBRMAXDL = 100
                           ICSIND = FALSE
                      NON3GPPSUPP = FALSE
                              MPS = FALSE
                           ANCHOR = FALSE
                         TAUTIMER = 0
                        EPSODBPOS = NOBPOS
                      RAUTAUTIMER = 0
                      ACTIVETIMER = 10
                  EUTRANEDRXCYCLE = 10
                   NBIOTEDRXCYCLE = 10
                          NSAFLAG = TRUE
                            WBPTW = 12
                            NBPTW = 12
   "M2M"
                      IMEILCKPROV = FALSE
                        M2MNOTIFY = NOTPROV
                     LTE_M2M_FLAG = FALSE
   "DND Service"
                              DND = FALSE
   "CN Restriction"                 
                    EPCNOTALLOWED = TRUE 
                    NGCNOTALLOWED = TRUE
   "NGS Data"          
                    NGCNODETPL_ID = 1
                     NGSUSERTPLID = 1

   Total count = 161

   There is together 1 report

   ---    END
   ```