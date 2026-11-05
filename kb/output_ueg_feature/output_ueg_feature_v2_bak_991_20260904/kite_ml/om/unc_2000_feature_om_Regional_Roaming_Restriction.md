# 激活区域漫游限制特性（适用于SGSN/MME）

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。

区域漫游限制是指UEG可以控制某一类用户可以接入的位置区域，或者控制某一区域不同类别用户的接入策略。

**说明** 

适用于SGSN、MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-020911 区域漫游限制特性概述（适用于MME/HSS）。
- 已完成加载License，对应的License项为“82206572 LKV2RRR02 区域漫游限制”。

数据

| 类别                                                 | 参数名称                      | 取值样例                    | 获取方法   | 说明                        |
|:---------------------------------------------------|:--------------------------|:------------------------|:-------|:--------------------------|
| ADD ZC                                             | 区域码（ZC）                   | 0x1234                  | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 标识类型（IDTYPE）              | LA                      | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 移动国家码（MCC）                | 123                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 移动网号（MNC）                 | 03                      | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 位置区域码（LAC）                | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 路由区域码（RAC）                | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 服务区域码（SAC）                | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 跟踪区域码（TAC）                | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 区域名称（ZCN）                 | china-mobile-001        | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 位置区域码范围（LACRANGE）         | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 路由区域码范围（RACRANGE）         | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 跟踪区域码范围（TACRANGE）         | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZC                                             | 服务区域码范围（SACRANGE）         | 0x1                     | 全网规划   | ZC配置参数                    |
| ADD ZCCONVERT                                      | 用户范围（SUBRANGE）            | 外网用户                    | 全网规划   | ZC配置参数                    |
| ADD ZCCONVERT                                      | 转换策略（CONVERTPLCY）         | 签约则采用指定ZC               | 全网规划   | ZC配置参数                    |
| ADD ZCCONVERT                                      | 区域码（ZC）                   | 0x1235                  | 全网规划   | ZC配置参数                    |
| ADD AREAGP ADD AREAGPMEM                           | 区域群标识（AREAID）             | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 标识类型（IDTYPE）              | TA                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 移动国家码（MCC）                | 123                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 移动网号（MNC）                 | 03                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 路由区域码（RAC）                | 0x1                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 跟踪区域码（TAC）                | 0x4201                  | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD AREAGP ADD AREAGPMEM                           | 位置区域码（LAC）                | 0x1                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 区域范围（AREA）                | AG                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 区域群标识（AREAID）             | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 用户范围（SUBRANGE）            | SPECIAL_IMSI_RANGE      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 移动国家码（MCC）                | 123                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 移动网号（MNC）                 | 03                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 跟踪区域码（TAC）                | 0x4201                  | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 跟踪区域码范围（TACRANGE）         | 0x1                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | IMSI前缀（IMSIPRE）           | 1230301                 | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 控制类型（CTRLTYPE）            | REJECT                  | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 原因值（CAUSE）                | EPS_SERVICE_NOT_ALLOWED | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 用户群标识（SUBID）              | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 起始IMSI（BEGIMSI）           | 123                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 终止IMSI（ENDIMSI）           | 456                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBACCAREALST ADD IUACCAREALST ADD S1ACCAREALST | 自定义原因值（SDCAUSE）           | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 拒绝特征用户接入（SPECSUB）         | NO                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 拒绝特征RFSP用户接入（SUBRFSP）     | NO                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 拒绝特征RFSP索引（REJRFSPIDX）    | 1                       | 本端规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 拒绝CSFB用户接入（SUBCSFB）       | NO                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | SRVCC能力（SRVCCCAP）         | YES                     | 本端规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 匹配STN-SR（CHKSTNSR）        | NO                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | eNodeB指示方式（ENBIND）        | NO                      | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1ACCAREALST                                   | 指示特征RFSP（ENBRFSPIDX）      | 1                       | 本端规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SUBGP ADD SUBGPMEM                             | 用户群标识（SUBID）              | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SUBGP ADD SUBGPMEM                             | IMSI前缀（IMSIPRE）           | 1230301                 | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD MSISDNSUBGPMEM                                 | 用户群标识（SUBID）              | 1                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD MSISDNSUBGPMEM                                 | MSISDN前缀（MSISDNPRE）       | 123456                  | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD IMEILIB                                        | IMEITAC（设备型号核准号码）设备型号核准号码 | 12345678                | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD IMEILIB                                        | UETYPE（终端类型）              | BLACKBERRY              | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1IMEICFG                                      | SUBRANGE（ 用户范围）           | ALL_USER                | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD S1IMEICFG                                      | GETIMEIPLC（IMEI获取策略）      | IMEISV                  | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SPECRFSPVALUE                                  | 特征RFSP索引（RFSPIDX）         | 0                       | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SPECRFSPVALUE                                  | 特征RFSP索引类型（TYPE）          | ACC_REJECT              | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SPECRFSPVALUE                                  | 起始RFSP（BEGRFSP）           | 250                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD SPECRFSPVALUE                                  | 终止RFSP（ENDRFSP）           | 255                     | 全网规划   | 以位置区域为对象，控制该区域不同用户的接入策略   |
| ADD GBSUBRRLST ADD IUSUBRRLST ADD S1SUBRRLST       | 用户范围（SUBRANGE）            | IMSI_RANGE              | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD GBSUBRRLST ADD IUSUBRRLST ADD S1SUBRRLST       | 起始IMSI（BEGIMSI）           | 123003000000000         | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD GBSUBRRLST ADD IUSUBRRLST ADD S1SUBRRLST       | 终止IMSI（ENDIMSI）           | 123003666000000         | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD GBSUBRRLST ADD IUSUBRRLST ADD S1SUBRRLST       | 区域群标识（LARAGPID）           | 1                       | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD GBSUBRRLST ADD IUSUBRRLST ADD S1SUBRRLST       | 区域限制模式（ARMODE）            | BLACKLST                | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGP                                         | 区域群标识（LARAGPID）           | 1                       | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGP                                         | 区域群名称（LARAGPN）            | Shanghai                | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 区域群标识（LARAGPID）           | 1                       | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 标识类型（IDTYPE）              | RA                      | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 移动国家码（MCC）                | 456                     | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 移动网号（MNC）                 | 12                      | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 位置区域码（LAC）                | 0x1401                  | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 路由区域码（RAC）                | 0x11                    | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD LARAGPMEM                                      | 路由区域码范围（RACRANGE）         | 0x20                    | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGP                                           | 跟踪区群组标识（TAGPID）           | 1                       | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGP                                           | 跟踪区群组名称（TANAME）           | Shanghai                | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGPMEM                                        | 跟踪区群组标识（TAGPID）           | 1                       | 本端规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGPMEM                                        | 移动国家码（MCC）                | 456                     | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGPMEM                                        | 移动网号（MNC）                 | 12                      | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGPMEM                                        | 跟踪区域码（TAC）                | 0x4201                  | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |
| ADD TAGPMEM                                        | 跟踪区域码范围（TACRANGE）         | 0x4210                  | 全网规划   | 以某一类用户为对象，控制该类用户可以接入的位置区域 |

## 操作流程

激活区域漫游限制操作流程如图1所示。

**图1** 激活区域漫游限制操作流程

**说明** 

图1中，方法3.1和方法3.2不可以同时选择使用。

**针对特征用户进行接入控制配置流程**

**说明** 

针对特征用户进行接入控制属于方法3.1，其中针对签约特征RFSP用户的接入控制仅适用于运营商在HSS上为特定类型的用户签约了特定的RFSP的场景。此处对该配置流程单独进行说明。

1. 所有本网用户全部支持基于特征用户进行接入限制。
2. 外网用户中特定IMSI前缀的用户（数量较少）支持基于特征用户进行接入限制。
3. 其它外网用户都不支持基于特征用户进行接入限制。

1和2对应已知特定IMSI前缀的用户，支持基于特征RFSP控制；3对应其余非特定IMSI前缀的用户，不支持基于特征RFSP控制。

为了方便用户配置，特性实现时，针对支持基于特征用户控制的所有本网用户，增加了用户范围取值HOME\_USER，避免了配置多条特定IMSI前缀完成本网用户范围配置的场景。数量较少的支持基于特征用户进行接入限制的外网用户，可以用特定IMSI前缀实现配置。同时，其它外网用户也增加了用户范围取值FOREIGN\_USER，避免了配置多条其余IMSI前缀完成其它外网用户范围配置的场景。

**图2** 根据特征RFSP值进行接入控制配置流程

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 开启本特性的功能控制开关。

   **SET LICENSESWITCH**

   **说明** 

   根据用户签约ZC信息进行漫游限制不受该License控制。
3. 根据需要选择合适的漫游策略。

   **说明** 

   - 可以根据不同的需求配置多种策略进行漫游限制。如果配置多种策略，则在用户接入时，需要所有策略都允许用户接入，该用户才能接入网络。否则，该用户不允许接入。
   - 此种场景下TAU流程的Downlink NAS Transport消息是否携带Handover Restriction List信元，需要判断MME对接的所有eNodeB是否都支持此信元。如果都支持，可以将**SET S1CMPT**命令中的“HRL”设置为“YES”，此时TAU流程中的Downlink NAS Transport消息才会携带Handover Restriction List信元。否则，“HRL”需要设置为“NO”，避免对不支持此信元的eNodeB产生影响，此时TAU流程中的Downlink NAS Transport消息不会携带Handover Restriction List信元。

   - **方法1.1: 通过用户的签约ZC列表进行接入限制。**

     **说明** 

     该功能需要HLR/HSS支持并配置了用户的签约ZC信息。

     1. 打开根据用户ZC信息进行漫游限制的功能开关。

        **SET MMFUNC**
     2. 增加区域码记录。

        **ADD ZC**
     3. （可选）配置区域码转换策略。当运营商需要忽略来自其它区域或其它运营商的签约ZC时，执行该步骤。

        **ADD ZCCONVERT**
     4. （可选）配置用户不允许接入某区域时，UEG下发拒绝接入消息中携带的原因值。

        - 2G/3G用户携带的原因值通过软参“BYTE\_EX64 控制ZC接入限制下发的拒绝原因值”进行控制（缺省携带的原因值为#12 Location area not allowed）：

          **SET SOFTPARA**
        - 4G用户携带的原因值通过软参“BYTE\_EX209 控制下发给4G区域限制用户拒绝消息中携带的原因值”进行控制（缺省携带的原因值为#15 No suitable cells in tracking area）：

          **SET SOFTPARA**
   - **方法1.2: 通过UEG配置的ZC列表进行接入限制。**

     1. 打开根据用户ZC信息进行漫游限制的功能开关。

        **SET MMFUNC**
     2. 定义某一类用户可以接入的区域信息（区域码和区域码对应的位置区域）。

        **ADD ZC**
     3. 配置该类用户和3.b定义的区域码绑定。

        **ADD ZCCONVERT**
     4. （可选）配置用户不允许接入某区域时，UEG下发拒绝接入消息中携带的原因值。

        - 2G/3G用户携带的原因值通过软参“BYTE\_EX64 控制ZC接入限制下发的拒绝原因值”进行控制（缺省携带的原因值为#12 Location area not allowed）：

          **SET SOFTPARA**
        - 4G用户携带的原因值通过软参“BYTE\_EX209 控制下发给4G区域限制用户拒绝消息中携带的原因值”进行控制（缺省携带的原因值为#15 No suitable cells in tracking area）：

          **SET SOFTPARA**
   - **方法2: 配置以某一类用户为对象，控制该类用户可以接入的位置区域**

     1. 配置区域群记录，同一个区域群中的成员具有相同的接入控制策略。

        - 配置位置区域群记录。

          1. 配置位置区域群标识和名称。

             **ADD LARAGP**
          2. 配置区域群的群成员。

             **ADD LARAGPMEM**
        - 配置跟踪区域群记录。

          1. 配置区域群标识和名称。

             **ADD TAGP**
          2. 配置区域群的群成员。

             **ADD TAGPMEM**
     2. 配置对指定用户范围内用户的区域漫游限制策略。
        - Gb模式下

          **ADD GBSUBRRLST**
        - Iu模式下

          **ADD IUSUBRRLST**
        - S1模式下

          **ADD S1SUBRRLST**
   - **方法3.1: 配置某区域群的用户接入策略。**

     **说明** 

     在进行策略配置时，该方式不能和“方法3.2: 配置某一特定区域的用户接入策略”同时选择，只能选择其中一种进行配置。

     1. **可选：**配置网络侧的IMEI获取策略为获取IMEI或获取IMEISV。

        如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

        **ADD S1IMEICFG**
     2. 将多个区域划分为一个区域群。

        - 配置区域群标识和名称。

          **ADD AREAGP**
        - 配置加入区域群的区域信息。

          **ADD AREAGPMEM**
     3. **可选：**配置IMEI TAC与终端类型的映射关系。

        如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

        **ADD IMEILIB**
     4. **可选：**将不同IMSI前缀的用户划分为一个用户群。

        如果需要对多个不同IMSI前缀的用户均采用相同的控制策略，则可以通过此步骤将不同IMSI前缀的用户配置为一个用户群。

        - 配置用户群标识和名称。

          **ADD SUBGP**
        - 配置加入用户群的IMSI前缀。

          **ADD SUBGPMEM**
     5. 配置区域群内不同用户的控制策略。
        - Gb模式下，配置区域群下特定IMSI范围或指定用户群用户的控制策略。

          **ADD GBACCAREALST**

          **说明** 

          此处以配置区域群下指定用户群用户的控制策略为例。
        - Iu模式下，配置区域群下特定IMSI范围或指定用户群用户的控制策略。

          **ADD IUACCAREALST**

          **说明** 

          此处以配置区域群下特定IMSI范围用户的控制策略为例。
        - S1模式下，配置区域群下特定IMSI范围、指定终端类型或指定用户群用户进行接入控制。

          **ADD S1ACCAREALST**

          **说明** 

          此处以配置区域群下指定终端类型用户的控制策略为例。
   - **针对特征用户的接入控制**

     **说明** 

     - 在进行策略配置时，该方式不能和“方法3.2: 配置某一特定区域的用户接入策略”同时选择，只能选择其中一种进行配置。
     - 此种场景下TAU流程的Downlink NAS Transport消息中的特征SPID信元是R10协议新增的，需要判断eNodeB是否都支持此信元，如果支持，将**SET S1CMPT**命令中的“SPID”设置为“YES”，此时TAU流程中的Downlink NAS Transport消息才会携带特征RFSP。否则，“SPID”需要设置为“NO”，避免对不支持此信元的eNodeB产生影响，此时TAU流程中的Downlink NAS Transport消息不会携带特征RFSP。
     - 针对特征用户进行接入控制的策略不支持根据MSISDN配置接入策略。

     1. 配置特定限制区域群。
        - 增加特定限制区域群。

          **ADD AREAGP**
        - 增加特定限制区域群成员。

          **说明** 

          所有特定限制区域需要配置在一个区域群“AREAID”中。

          **ADD AREAGPMEM**
     2. 设置特征RFSP取值范围以便于控制用户接入。

        **ADD SPECRFSPVALUE**
     3. 设置特征用户的接入控制策略。
        - 配置所有本网用户限制策略，以实现用户诉求第一种场景。

          **ADD S1ACCAREALST**
        - 配置外网用户中特定IMSI前缀用户限制策略，可配置多条，以实现用户诉求第二种场景。

          **ADD S1ACCAREALST**
        - 配置其它外网用户限制策略，以实现用户诉求第三种场景。

          **ADD S1ACCAREALST**
     4. **可选：**在HSS需要根据IMEI识别特征用户的场景下，配置用户获取IMEI策略。
        - 查询用户获取IMEI策略是否配置。

          **LST S1IMEICFG**
        - **可选：**如果之前没有配置获取IMEI策略，需要执行此步骤。

          **MOD S1IMEICFG**
     5. 为防止用户在移动或切换时接入特定限制区域，系统下发给UE的TA List中过滤禁止UE接入的TA，且系统向eNodeB发送禁止用户接入的TA列表。

        **SET MMFUNC**
   - **方法3.2: 配置某一特定区域的用户接入策略**

     **说明** 

     在进行策略配置时，该方式不能和“方法3.1: 配置某区域群的用户接入策略”和“基于特征RFSP值场景下的区域漫游限制”同时选择，只能选择其中一种进行配置。

     1. **可选：**配置网络侧的IMEI获取策略为获取IMEI或获取IMEISV。

        如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

        **ADD S1IMEICFG**
     2. **可选：**配置IMEI TAC与终端类型的映射关系。

        如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

        **ADD IMEILIB**
     3. **可选：**将不同IMSI前缀的用户划分为一个用户群。

        如果需要对多个不同IMSI前缀的用户均采用相同的控制策略，则可以通过此步骤将不同IMSI前缀的用户配置为一个用户群。

        - 配置用户群标识和名称。

          **ADD SUBGP**
        - 查询IMSI用户群成员。

          **LST SUBGPMEM**

          **说明** 

          系统采用最长匹配原则查询对用户的接入限制策略。例如IMSI为1234567890的用户接入时，若系统中同时存在以下3条记录，那该用户只会匹配到SUBID=3对应的接入限制策略。因此在添加IMSI前缀用户群成员前需要先查询当前范围的用户是否已存在配置记录，避免对该用户的部分接入限制策略不生效。

          - ADD SUBGPMEM: SUBID=1, IMSIPRE="123456";
          - ADD SUBGPMEM: SUBID=2, IMSIPRE="1234567";
          - ADD SUBGPMEM: SUBID=3, IMSIPRE="12345678";
        - **可选：**

          配置加入用户群的IMSI前缀。

          **ADD SUBGPMEM**
     4. **可选：**将不同MSISDN前缀的用户划分为一个用户群。

        如果需要对多个不同MSISDN前缀的用户均采用相同的控制策略，则可以通过此步骤将不同MSISDN前缀的用户配置为一个用户群。

        - 配置用户群标识和名称。

          **ADD SUBGP**
        - 查询MSISDN用户群成员。

          **LST MSISDNSUBGPMEM**

          **说明** 

          系统采用最长匹配原则查询对用户的接入限制策略。例如MSISDN为1234567890的用户接入时，若系统中同时存在以下3条记录，那该用户只会匹配到SUBID=3对应的接入限制策略。因此在添加MSISDN前缀用户群成员前需要先查询当前范围的用户是否已存在配置记录，避免对该用户的部分接入限制策略不生效。

          - ADD MSISDNSUBGPMEM: SUBID=1, MSISDNPRE="123456";
          - ADD MSISDNSUBGPMEM: SUBID=2, MSISDNPRE="1234567";
          - ADD MSISDNSUBGPMEM: SUBID=3, MSISDNPRE="12345678";
        - **可选：**

          配置加入用户群的MSISDN前缀。

          **ADD MSISDNSUBGPMEM**

          **说明** 

          - 对于同一用户如果系统中同时存在基于IMSI前缀和基于MSISDN前缀的接入限制策略，用户接入时，系统将按照基于IMSI前缀对应的策略对其进行接入限制。
          - 在Inter Handover和Inter Relocation流程中，新侧MME无法从老侧MME获取到MSISDN，因此在这两个流程中新侧MME无法根据MSISDN判断是否允许用户接入该区域，直到后续通过TAU/RAU流程获取到用户签约数据后才能对用户进行接入控制。
     5. 配置特定区域内不同用户的控制策略。
        - Gb模式下，配置特定区域下特定IMSI范围或指定用户群用户的控制策略。

          **ADD GBACCAREALST**

          **说明** 

          此处特定区域的区域范围以指定路由区为例，并以配置指定用户群用户的控制策略为例。
        - Iu模式下，配置特定区域下特定IMSI范围或指定用户群用户的控制策略。

          **ADD IUACCAREALST**

          **说明** 

          此处特定区域的区域范围以指定路由区为例，并以配置特定IMSI范围用户的控制策略为例。
        - S1模式下，配置特定区域下特定IMSI范围、指定终端类型或指定用户群用户进行接入控制。

          **ADD S1ACCAREALST**

          **说明** 

          此处特定区域的区域范围以指定跟踪区为例，并以配置指定终端类型用户的控制策略为例。

## 任务示例

任务描述

配置各类区域漫游限制策略。

脚本

//开启区域漫游限制功能开关。

```
SET LICENSESWITCH: LICITEM="LKV2RRR02", SWITCH=ENABLE;
```

- **任务1**

  //配置根据签约ZC进行漫游限制，限制签约ZC为0x1234的用户仅能在位置区域码为1的区域接入，区域名称为china-mobile-001。同时，针对来自其它运营商（运营商标识为128）的外网用户，忽略其签约ZC，不进行ZC接入限制。

  ```
  SET MMFUNC: ZC=YES;
  ADD ZC: ZC="0x1234", IDTYPE=LA, MCC="123", MNC="03", LAC="0x1", ZCN="china-mobile-001";
  ADD MNO: MNOID=128;
  ADD ZCCONVERT: SUBRANGE=FOREIGN_USER, NOID=128, CONVERTPLCY=IGNORE_SUB_ZC;
  ```
- **任务2**

  //在网络中存在大量不同用户群需要接入不同区域，且不同用户群需接入区域交叠的场景下，以某一类用户为对象，配置该类用户可以接入的区域。

  //打开ZC开关。

  ```
  SET MMFUNC: ZC=YES;
  ```

  //配置IMSI前缀为1230301的用户只能在跟踪区0x4201~0x4209中接入，其它区域均拒绝接入。

  ```
  ADD ZC: ZC="0x2000", IDTYPE=TA, MCC="123", MNC="03", TAC="0x4201", TACRANGE="0x4209";
  ADD ZCCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230301", CONVERTPLCY=OVERWRITE_DIRECTLY, ZC="0x2000";
  ```

  //配置IMSI前缀为1230304的用户只能在跟踪区0x4201~0x4205、0x4215~0x4225中接入，其它区域均拒绝接入。

  ```
  ADD ZC: ZC="0x4000", IDTYPE=TA, MCC="123", MNC="03", TAC="0x4201", TACRANGE="0x4205";
  ADD ZC: ZC="0x4000", IDTYPE=TA, MCC="123", MNC="03", TAC="0x4215", TACRANGE="0x4225";
  ADD ZCCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230304", CONVERTPLCY=OVERWRITE_DIRECTLY, ZC="0x4000";
  ```

  //配置IMSI前缀为1230302的用户只能在跟踪区0x4210~0x4219中接入，其它区域均拒绝接入。

  ```
  ADD ZC: ZC="0x3000", IDTYPE=TA, MCC="123", MNC="03", TAC="0x4203", TACRANGE="0x4204";
  ADD ZCCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230302", CONVERTPLCY=OVERWRITE_DIRECTLY, ZC="0x3000";
  ```
- **任务3**

  //配置一个区域群，该区域群包含的区域群成员如下：移动国家代码为123，移动网号为03，跟踪区"0x7603"到"0x7614"。该区域群允许本网所有用户、特定IMSI前缀的外网用户接入，不允许其它外网用户、特定特征RFSP值（CS voice preferred）用户接入。**该方式不能和任务4的配置方式同时存在。**

  //配置区域群1。

  ```
  ADD AREAGP: AREAID=1, AREAN="L800";
  ADD AREAGPMEM: AREAID=1, IDTYPE=TA, MCC="123", MNC="03", TAC="0x7603", TACRANGE="0x7614";
  ```

  //设置特征RFSP取值范围以便于控制用户接入。

  ```
  ADD SPECRFSPVALUE: RFSPIDX=0, TYPE=ACC_REJECT, BEGRFSP=250, ENDRFSP=255;
  ```

  //配置允许本网所有用户接入区域群1。

  ```
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=HOME_USER, NOID=0, CTRLTYPE=ALLOW, SUBRFSP=YES, REJCAUSE=NO_SUITABLE_CELLS_IN_TA;
  ```

  //配置允许特定IMSI前缀的外网用户接入区域群1。

  ```
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="12303", CTRLTYPE=ALLOW, SUBRFSP=YES, REJCAUSE=NO_SUITABLE_CELLS_IN_TA;
  ```

  //配置不允许其它外网用户接入区域群1。

  ```
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=FOREIGN_USER, NOID=0, CTRLTYPE=REJECT, CAUSE=NO_SUITABLE_CELLS_IN_TA;
  ```

  //配置不允许特定特征RFSP值（CSFB Only）用户接入区域群1。

  ```
  MOD S1IMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEISV;
  SET MMFUNC: TALIST=LOCAL_CFG-1, FORBIDTA=LOCAL_CFG-1;
  ```
- **任务4**

  //为不同的指定区域配置用户的接入策略。**该方式不能和任务3的配置方式同时存在。**

  //1.E-UTRAN中配置根据IMSI号段进行漫游限制，IMSI前缀为1230301的用户，除在跟踪区"0x4201"和"0x4205"中拒绝接入外，其它区域均可以接入。

  ```
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4201", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4205", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ```

  //2.E-UTRAN中配置根据IMSI号段进行漫游限制，跟踪区"0x4201"和"0x4205"只允许IMSI前缀为1230301的用户接入。

  ```
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4201", SUBRANGE=ALL_USER, CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4201", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=ALLOW;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4205", SUBRANGE=ALL_USER, CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4205", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=ALLOW;
  ```

  //3.E-UTRAN中配置根据IMSI号段进行漫游限制，跟踪区"0x4201"和"0x4205"除IMSI前缀为1230301的用户外都可以接入。

  ```
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4201", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4205", SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="1230301", CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;
  ```

  //4.E-UTRAN中配置根据终端类型进行漫游限制，跟踪区"0x4201"和"0x4205"拒绝某一终端类型的用户接入。

  ```
  MOD S1IMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEISV;
  ADD IMEILIB: IMEITAC="12345678", UETYPE=BLACKBERRY;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4201", SUBRANGE=UE_TYPE, CTRLTYPE=REJECT, CAUSE=NO_SUITABLE_CELLS_IN_TA, UETYPE=BLACKBERRY;
  ADD S1ACCAREALST: AREA=TA, MCC="123", MNC="03", TAC="0x4205", SUBRANGE=UE_TYPE, CTRLTYPE=REJECT, CAUSE=NO_SUITABLE_CELLS_IN_TA, UETYPE=BLACKBERRY;
  ```
- **任务5**

  //假设有2家运营商A、B，运营商A希望禁止运营商B的指定IMSI号段为123003000000000~123003666000000内的2G用户以及IMSI号段为123004000000000~123004666000000内的3G用户在位置区"0x1401"下的路由区域"0x11"~"0x20"以及"0x31"~"0x40"中接入，允许其在其余的区域内接入，移动国家代码为456，移动网号为12。

  //配置区域群记录，同一个区域群中的成员具有相同的接入控制策略。

  ```
  ADD LARAGP: LARAGPID=1, LARAGPN="shanghai";
  ADD LARAGPMEM: LARAGPID=1, IDTYPE=RA, MCC="456", MNC="12", LAC="0x1401", RAC="0x11", RACRANGE="0x20";
  ADD LARAGPMEM: LARAGPID=1, IDTYPE=RA, MCC="456", MNC="12", LAC="0x1401", RAC="0x31", RACRANGE="0x40";
  ```

  //配置禁止指定IMSI号段为123003000000000~123003666000000内的2G用户在路由区域"0x11"~"0x20"以及"0x31"~"0x40"中接入，允许其在其余的区域内接入。

  ```
  ADD GBSUBRRLST: SUBRANGE=IMSI_RANGE, BEGIMSI="123003000000000", ENDIMSI="123003666000000", LARAGPID=1, ARMODE=BLACKLST;
  ```

  //配置禁止指定IMSI号段为123004000000000~123004666000000内的3G用户在路由区域"0x11"~"0x20"以及"0x31"~"0x40"中接入，允许其在其余的区域内接入。

  ```
  ADD IUSUBRRLST: SUBRANGE=IMSI_RANGE, BEGIMSI="123004000000000", ENDIMSI="123004666000000", LARAGPID=1, ARMODE=BLACKLST;
  ```
- **任务6**

  //假设在TAC为“0x0011”到“0x0020”的区域仅存在LTE信号，不存在GSM/UMTS信号，运营商希望拒绝本网用户中的CS voice preferred用户和RFSP值为251~255的用户在此区域接入，同时将接入限制策略指示给eNodeB。

  //增加特定限制区域群及群成员。

  ```
  ADD AREAGP: AREAID=1, AREAN="shanghai";
  ADD AREAGPMEM: AREAID=1, IDTYPE=TA, MCC="456", MNC="12", TAC="0x0011", TACRANGE="0x0020";
  ```

  //配置特征RFSP取值范围，控制特征用户接入。

  ```
  ADD SPECRFSPVALUE: RFSPIDX=1, TYPE=ACC_REJECT, BEGRFSP=251, ENDRFSP=255;
  ADD SPECRFSPVALUE: RFSPIDX=2, TYPE=ENODEB_IND, BEGRFSP=251, ENDRFSP=255;
  ```

  //配置针对CS voice preferred属性用户的接入控制策略。

  ```
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=HOME_USER, NOID=0, CTRLTYPE=ALLOW, SPECSUB=YES, SUBRFSP=YES, REJRFSPIDX=1, SUBCSFB=YES, REJCAUSE=NO_SUITABLE_CELLS_IN_TA, ENBIND=RFSP_ID, ENBRFSPIDX=2;
  ```

  //在HSS需要根据IMEI识别特征用户的场景下，配置用户获取IMEI策略。

  ```
  MOD S1IMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEI;
  ```

  //为防止用户在移动或切换时接入特定限制区域，系统下发给UE的TA List中过滤禁止UE接入的TA，且系统向eNodeB发送禁止用户接入的TA列表。

  ```
  SET MMFUNC: TALIST=LOCAL_CFG, FORBIDTA=LOCAL_CFG;
  ```
- **任务7**

  //TAC为“0x0011”到“0x0020”的区域只允许MSISDN前缀为12345678和12340001的用户接入。

  //增加特定限制区域群及群成员。

  ```
  ADD AREAGP: AREAID=1, AREAN="shanghai";
  ADD AREAGPMEM: AREAID=1, IDTYPE=TA, MCC="456", MNC="12", TAC="0x0011", TACRANGE="0x0020";
  ```

  //增加用户群。

  ```
  ADD SUBGP: SUBID=1;
  ```

  //增加MSISDN用户群成员。

  ```
  ADD MSISDNSUBGPMEM: SUBID=1, MSISDNPRE="12345678";
  ADD MSISDNSUBGPMEM: SUBID=1, MSISDNPRE="12340001";
  ```

  //配置针对MSISDN前缀为12345678和12340001的用户的接入控制策略。

  ```
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=ALL_USER, CTRLTYPE=REJECT, CAUSE=NO_SUITABLE_CELLS_IN_TA, ENBIND=NO;
  ADD S1ACCAREALST: AREA=AG, AREAID=1, SUBRANGE=USER_GROUP, SUBID=1, CTRLTYPE=ALLOW, SPECSUB=NO, ENBIND=NO;
  ```