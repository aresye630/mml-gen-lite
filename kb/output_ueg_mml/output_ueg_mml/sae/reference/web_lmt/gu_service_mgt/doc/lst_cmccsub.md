# 查询CMCC用户静态数据(LST CMCCSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于从内存库查询CMCC用户的静态数据，主要包括用户签约的各种业务信息以及用户是否加锁等信息。

- 若需要查询单个CMCC用户的静态数据，请输入参数“IMSI”或“MSISDN”。
- 若需要查询连续多个CMCC用户的静态数据，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”。
- 若需要查询不连续的多个CMCC用户的静态数据，请输入参数“IMSI文件名”或“MSISDN文件名”。

**说明** 

- 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
- 在从运营商网络获取数据前，必须要获得运营商的授权。
- 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。
- 当**SET MAPCONF**命令中的“是否支持LST CMCCSUB命令返回的报文中显示IMEI参数”参数取值为“FALSE”时，该命令的查询结果不会显示“IMEI”参数。
- 当**SET MAPSERV**命令中的“用户信息显示模式”参数取值为“ANONYMOUS”时，该命令的查询结果会屏蔽“IMSI” 、“MSISDN” 、 “前转号码”、“IMEI”信息。

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

1. 查询“IMSI”号码为“460000009123456”的用户的静态数据，且不返回详细信息：

   ```
   LST CMCCSUB: IMSI="460000009123456", DETAIL=FALSE;
   ```

   ```
   %%LST CMCCSUB: IMSI="460000009123456", DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 15
                             IMSI = 460000009123456
                             ISDN = 460000009123456
                             IMEI = 123456789123456
                              NAM = BOTH
                         CATEGORY = COMMON
   Basic Service
   TSCODE:
                       Emergency Call (TS12)

   DefaultCall
                      DefaultCall = Telephony (TS11)

   RR Data
                         RROption = ALL_PLMNS

   PS Data
                    CHARGE_GLOBAL = NONE
                           CNTXID = 1
                    PSAPNQOSTPLID = 103

   EPS Data
                    CHARGE_GLOBAL = NONE
                    DEFAULTCNTXID = 1
                           CNTXID = 2
                   EPSAPNQOSTPLID = 102

                           CNTXID = 1
                   EPSAPNQOSTPLID = 101

                          

   Total count = 18

   There is together 1 report

   ---    END
   ```
2. 查询“MSISDN”为“460000009012389”的用户的静态数据，且返回详细信息：

   ```
   LST CMCCSUB: ISDN="460000009012389", DETAIL=TRUE;
   ```

   ```
   %%LST CMCCSUB: ISDN="460000009012389", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 15
                             IMSI = 460000009012389
                             ISDN = 460000009012389
                             IMEI = 123456789123456
                              NAM = BOTH
                         CATEGORY = COMMON
   LOCK
                               IC = FALSE
                               OC = FALSE
                         GPRSLOCK = FALSE
                          EPSLOCK = FALSE
                      NON3GPPLOCK = FALSE

   SABLOCK
                               IC = FALSE
                               OC = FALSE

   Basic Service
   TSCODE:
                       Emergency Call (TS12)

   DefaultCall
                      DefaultCall = Telephony (TS11)

   ODB Data
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
                           ODBPOS = NOBPOS

   RR Data
                         RROption = ALL_PLMNS

   SS Data
   CFU
                              CFU = NOTPROV
   CFB
                              CFB = NOTPROV
   CFNRY
                            CFNRY = NOTPROV
   CFNRC
                            CFNRC = NOTPROV
   CFD
                              CFD = NOTPROV
   BAOC
                             BAOC = NOTPROV
   BOIC
                             BOIC = NOTPROV
   BOICEXHC
                         BOICEXHC = NOTPROV
   BORO
                             BORO = NOTPROV
   BAIC
                             BAIC = NOTPROV
   BICROAM
                          BICROAM = NOTPROV
   CW
                               CW = NOTPROV
   PLMNSS
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
   OTHER SS
                            CBCOU = SUBSCRIBER
                             CLIP = NOTPROV
                             CLIR = NOTPROV
                             COLP = NOTPROV
                             COLR = NOTPROV
                             HOLD = NOTPROV
                             MPTY = NOTPROV
                            EMLPP = NOTPROV
                        EMLPP_COU = SUBSCRIBER

   ARD
                              ARD = PROV                   
                     NRNOTALLOWED = TRUE 
                  NR5GSNOTALLOWED = TRUE

   CN Restriction
                    EPCNOTALLOWED = TRUE
                    NGCNOTALLOWED = TRUE

   Other Service Data
                             CARP = NOTPROV
   PS Data
                    CHARGE_GLOBAL = NONE
                           CNTXID = 1
                    PSAPNQOSTPLID = 103

   EPS Data
                    CHARGE_GLOBAL = NONE
                        AMBRMAXUL = 4294967111                     
                        AMBRMAXDL = 4294967111 
                   AMBRMAXUL_UNIT = kbps                 
                   AMBRMAXDL_UNIT = kbps 
                    DEFAULTCNTXID = 1
                         SUPWBPTW = TRUE
                            WBPTW = 1
                         SUPNBPTW = TRUE
                            NBPTW = 1
                           CNTXID = 1
                   EPSAPNQOSTPLID = 101

                           CNTXID = 2
                   EPSAPNQOSTPLID = 102

   5GS Data
                           AMBRUP = 10000
                           UPUNIT = bps
                           AMBRDW = 10000
                           DWUNIT = bps
                      FORBIDTPLID = 10
                     SERAREATPLID = 10
                        RFSPINDEX = 1
                         AUTHTYPE = 5G-AKA
                    SMSSUBSCRIBED = TRUE
                            MTSMS = FALSE
                          MTSMSBA = FALSE
                          MTSMSBR = FALSE
                            MOSMS = FALSE
                          MOSMSBA = FALSE
                          MOSMSBR = FALSE
                  SUPSUBSREGTIMER = TRUE
                     SUBSREGTIMER = 2233
                      MICOALLOWED = FALSE
                              MPS = FALSE
                              MCS = FALSE
                      DLBUFFERIND = NOT_REQUESTED
                         DLBUFFER = 0
                        INGROUPID = 5-460003-01
                         SHAREDID = 46001-shared5

   CSLocationData
                           VlrNum = 86183411
                           MscNum = 86183411
               MsPurgedForNonGprs = FALSE

   PSLocationData
                       SGSNNUMBER = 86183421
                     PURGEDONSGSN = FALSE

   EPSLocationData
                          MMEHOST = cmccsub.huawei.com
                         MMEREALM = huawei.com
                      PURGEDONMME = FALSE

                           PLMNID = 46002
                          CAGONLY = FALSE
                            CAGID = abcdef22
                            CAGID = abcdef23
   						
   		        PLMNID = 46003
                          CAGONLY = FALSE
                            CAGID = abcdef32
                            CAGID = abcdef33

   Total count = 126

   There is together 1 report

   ---    END
   ```
3. 查询第一个MSISDN号码为“13310911001”的连续3个用户的静态数据，且返回详细信息：

   ```
   LST CMCCSUB: ISDN="13310911001", RECORDCOUNT=3, DETAIL=TRUE;
   ```

   ```
   %%LST CMCCSUB: ISDN="13310911001", RECORDCOUNT=3, DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：11. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
4. 查询“MSISDN文件名”为“lstsub.txt”的用户的静态数据，且返回详细信息：

   ```
   LST CMCCSUB: ISDNFILE="lstsub.txt", DETAIL=TRUE;
   ```

   ```
   %%LST CMCCSUB: ISDNFILE="lstsub.txt", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435468. 使用CHK BATSTAT指令可查看此批操作的执行情况

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

| 输出项名称              | 输出项解释                                              |
|:-------------------|:---------------------------------------------------|
| IMEI               | 国际移动设备标识。                                          |
| MsPurgedForNonGprs | CS域用户是否被purge。                                     |
| PURGEDONSGSN       | PS域用户是否被purge。                                     |
| PURGEDONMME        | EPS域用户是否被purge。                                    |
| 批操作ID              | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息，并保存查询结果。 |
| SUPSUBSREGTIMER    | 是否支持5G周期注册定时器签约。                                   |
| INGROUPID          | 用于返回移动网络内部设备之间通信时互相传递的组ID。                         |
| SHAREDID           | 用于返回为内部组创建的共享数据的ID。                                |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                             | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |