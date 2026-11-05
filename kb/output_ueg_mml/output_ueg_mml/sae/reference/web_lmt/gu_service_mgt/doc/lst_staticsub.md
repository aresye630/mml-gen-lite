# 查询用户静态数据(LST STATICSUB)

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

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                            |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于标识要查询哪个IMSI号码对应的静态数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                           |
| ISDN        | MSISDN    | 用于标识要查询哪个MSISDN号码对应的静态数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                         |
| RECORDCOUNT | 用户个数      | 用于标识查询静态数据的用户数目。 当需要查询连续号码的多个用户的静态数据时配置。配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的静态数据。 取值范围：1～10000 默认值：无。 说明：该参数是对连续号码的多个用户进行静态数据查询，当只有一个用户时，该参数不必配置。当一次查询的用户个数很多时，对系统性能无影响，但查询的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的待查询静态数据的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                    |
| ISDNFILE    | MSISDN文件名 | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的待查询静态数据的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                              |

## 使用实例

查询“IMSI”号码为“460456009002”的用户的静态数据：

```
LST STATICSUB: IMSI="460456009002";
```

```
%%LST STATICSUB: IMSI="460456009002";%%
RETCODE = 0 SUCCESS0001:操作成功

                         HLRSN = 84
                          IMSI = 460456009002
                          ISDN = 86456009002
                 ICS-Indicator = FALSE
              ANCHOR-Indicator = FALSE
                      CardType = USIM
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
"TIF-CSI"
                        TIFCSI = NOTPROV
"IM-O-CSI"
                         TPLID = 100
"EPS Data"
                 CHARGE_GLOBAL = NONE
                     AMBRMAXUL = 50000000
                     AMBRMAXDL = 50000000
                           EGR = NOTPROV
                   NON3GPPSUPP = FALSE
                   LTEAUTOPROV = FALSE
                           MPS = FALSE
                        ICSIND = FALSE
                        ANCHOR = FALSE
                      TAUTIMER = 0
                    RELAY_NODE = FALSE
                     EPSODBPOS = NOBPOS
                       NSAFLAG = TRUE
                   NSAAUTOPROV = TRUE
                         WBPTW = 1
                         NBPTW = 1                    
                        CNTXID = 1
                      APNTPLID = 71
                    DEFAULTAPN = TRUE
                   WILDCARDAPN = FALSE
                   EPSQOSTPLID = 101
                       PDPTYPE = IPV4
                        ADDIND = DYNAMIC ADDRESS
                  VPLMNALLOWED = TRUE
                        CHARGE = NORMAL

"5GS Data"
                        AMBRUP = 500
                        UPUNIT = bps
                        AMBRDW = 1000
                        DWUNIT = bps
                           MPS = FALSE
                           MCS = FALSE
                   DLBUFFERIND = NOT_REQUESTED
                      DLBUFFER = 0
                      AUTHTYPE = 5G-AKA
                   MICOALLOWED = FALSE
                 SMSSUBSCRIBED = FALSE
                         MTSMS = FALSE
                       MTSMSBA = FALSE
                       MTSMSBR = FALSE
                         MOSMS = FALSE
                       MOSMSBA = FALSE
                       MOSMSBR = FALSE
         NSSAIINCLUSIONALLOWED = TRUE
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

"SMS INAP Service"
                          SKEY = 0
"M2M"
                   IMEILCKPROV = FALSE
                     M2MNOTIFY = NOTPROV

Total count = 157

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD SUB**

、

**MOD AMDATA**

和

**MOD LCK**

命令的参数说明。表1列出的是未包含在

**ADD SUB**

、

**MOD AMDATA**

和

**MOD LCK**

命令参数说明中的输出项。

| 输出项名称        | 输出项解释                                                                                                                               |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------|
| PERMANENTIND | 用于返回用户接入的APN是否是永久APN。 TRUE：永久APN。FALSE：非永久APN。                                                                                      |
| NSAAUTOPROV  | 用户是否为NSA自动开户用户，该参数仅在用户触发NSA自动开户流程后才会显示。 取值范围： FALSE：非NSA自动开户用户。TRUE：已发送通知消息并收到成功响应的NSA自动开户用户。AUTOTONSA_NN：已发送通知消息未收到成功响应的NSA自动开户用户。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                             | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |