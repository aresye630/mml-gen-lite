# 查询NCC模板(LST NCCTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询NCC（Network Capability Configuration）模板信息数据：

- 若需要查询全部NCC模板的配置信息，请只输入“HLR序列号”。
- 若需要查询某个NCC模板的详细配置信息，请同时输入“HLR序列号”和“模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                            |
|:-------|:-------|:------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询NCC模板数据。                     |
| TPLID  | 模板ID   | 用于指示系统需要按照哪个模板ID来查询NCC模板信息；若不输入，则表示查询所有NCC模板ID。 |

## 使用实例

1. 查询“HLR序列号”为“1”的UDM上的NCC模板数据记录：

   ```
   LST NCCTPL: HLRSN=1;
   ```

   ```
   %%LST NCCTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  3            TEST3
                  4            TEST4
                  5            TEST5

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的UDM上的NCC模板数据记录。其中，“模板ID”为“2”：

   ```
   LST NCCTPL: HLRSN=1, TPLID=2;
   ```

   ```
   %%LST NCCTPL: HLRSN=1, TPLID=2;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 2
                          TPLNAME = <NULL>

   MAP Operation
                              UPL = MAPV3
                              RSD = MAPV3
                              SAI = MAPV3
                              ISD = MAPV3
                              DSD = MAPV3
                             CANL = MAPV3
                              PRN = MAPV3

   MAP Service
                             MPTY = SR
                         PLMNSS-1 = SR
                         PLMNSS-2 = SR
                         PLMNSS-3 = SR
                         PLMNSS-4 = SR
                         PLMNSS-5 = SR
                         PLMNSS-6 = SR
                         PLMNSS-7 = SR
                         PLMNSS-8 = SR
                         PLMNSS-9 = SR
                         PLMNSS-A = SR
                         PLMNSS-B = SR
                         PLMNSS-C = SR
                         PLMNSS-D = SR
                         PLMNSS-E = SR
                         PLMNSS-F = SR
                       LCSSERVICE = SR
                              ALS = NR
                          ARDSERV = SR
                         CARPSERV = SR
                          GROUPID = SR
                        ECATEGORY = SR
                         ZONECODE = SR
                       BAOCFRSERV = NR
                       SMSCSISERV = SR
                              ECT = SR
                            ODBPB = SR
                       CANLSIGNAL = NR
                          VLRBS30 = SR
                        MULTIIMSI = NR
                             TZSZ = NR
                              CFD = SR
                  ROUTINGCATEGORY = SR
                              ACR = SR
                          GPRSCSI = NR
                             ELCS = NR
                         OCSITS11 = NR
                             SSET = NR
                           NSMSIN = NR
                         COMNISDN = NR
                             OLCM = NR
                            EMLPP = SR
                          VLRBS20 = SR
                             BS2X = SR
                             BS3X = SR
                              OSK = SR
                             MSIM = NR
                       SSET_VPLMN = SR
                     CHARGINGAREA = NR
                       FRAUDLIMIT = NR
                             TS22 = SR
                            LUDP3 = NR
                            LUDP4 = NR
                            MISDN = NR
                          PDPTYPE = DualStack
                             MTRF = NOTAUTH
                          PNP_ISD = NR
                          PNP_SRI = NR
                      CANLWHENUPL = SR
                          BOROISD = SR
                            EOICK = NR
                             CAPL = NR
                          NETTYPE = VoLTE
                            MMINT = NR
                 LOCINFEPSWHENPSI = SR
              EXEXROUTINGCATEGORY = SR
                            APNOI = NR
                       LTECSFBADD = NR
                     SUPPM2MCISDN = NR
                      ARDENHANCED = SR
                              ICK = NR
                         PRN_MTRR = SR
                    PRN_PrePaging = SR
                        PRN_Retry = NR
                              CUG = SR
                              SPN = NR
                              STE = NR
                            COMAP = SR
                           EXTFIR = NR
                          VCFBFTN = 000000000000000
                        VCFNRYFTN = 000000000000000
                        VCFNRCFTN = 000000000000000
                         SUPPEARP = NR
                      PDPTYPE_EPS = DualStack
                       ARD_CANCEL = NR
                     ONECXNANCHOR = NR
                               CW = SR
                           RFSPID = NR
                    REATTACH_SUPP = NR
                        SUPPSTNSR = SR
                   PSI_FORLOCINFO = SuppWithCurLoc
                   IDR_FORLOCINFO = SuppWithCurLoc
                         TRANSFER = SX
                          LONGFTN = CapabilityInUPL
                     MIG_SRI_CVER = PHASE3
                    SELECTCOMISDN = SX
                CHKSGSNMSISDNLESS = Check
                MSIM_AUXCARD_ISDN = NR
                  NGRANNOTALLOWED = NR
                      UEUSAGETYPE = SR
                              PSM = SR
                      LONGMMENAME = SR
                    CNRESTRICTION = SR 
                   IW5GSINDICATOR = SR
                        SDREG_MME = SX
                           ICSIND = SR
                              NSA = NR
             T-ADS_DATA_RETRIEVAL = NR
           
   Total count = 118

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NCCTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                    |
|:--------|:--------|:------------------------|:----------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST NCCTPL命令查询已定义的“模板ID”。 |