# 查询指定用户的运行信息（DSP USERRUNINFOSTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示当前进行用户收集运行信息的所有用户，或者查询指定用户的运行信息。

用于查询指定用户的运行信息，输出用户使用静态规则时各种rule信息的匹配次数统计、该rule下的流量统计。或者使用动态规则时的flow信息，各种rule信息的匹配次数统计、该rule下的流量统计，用户业务car/shaping的信息，用户当前使用的五元组信息，用户访问业务的协议信息。或者输出动态和预定义ADC规则匹配次数统计。Rule group information统计项只对PCC用户生效。User profile and Common-Policy统计项只针对非PCC用户生效。

#### 注意事项

- 执行该命令前，必须先执行命令ADD USERRUNINFO配置指定用户。
- 同一用户类型下有多个会话时，只显示第一个会话的运行信息。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                      |
|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERTYPE | 用户类型   | 可选必选说明：必选参数 参数含义：该参数用于指定用户类型。 数据来源：本端规划 取值范围：枚举类型。 IMSI：表示用户的IMSI号。MSISDN：表示用户的MSISDN号。 默认值：无 配置原则：无                                                                                                                                                                                                                                      |
| IMSI     | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。 参数含义：表示用户的IMSI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无 |
| MSISDN   | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。 参数含义：表示用户的MSISDN号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。 默认值：无 配置原则：无                                                                                       |
| INFOTYPE | 信息类型   | 可选必选说明：可选参数 参数含义：信息类型。 数据来源：本端规划 取值范围：枚举类型。 RULE：表示需要查询的规则。CAR_SHAPING：表示该用户的car-shaping信息。FLOW：表示该用户的flow-info信息。PROTOCOL：表示该用户的协议信息。只有做过协议识别，才可以显示协议信息。 默认值：无 配置原则：无                                                                                                                                                                    |
| RULETYPE | 规则类型   | 可选必选说明：条件必选参数 前提条件：该参数在“INFOTYPE”配置为“RULE”时为必选参数。 参数含义：表示需要查询的规则类别。未指定时表示查询用户的所有规则。 数据来源：本端规划 取值范围：枚举类型。 BWM：查询bwm rule。STATIC：查询静态规则。DYNC：查询动态规则。 默认值：无 配置原则：无                                                                                                                                                                           |

#### 使用实例

- 显示当前用户的bwm-rule详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=RULE,RULETYPE=BWM;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ---------------
  Result = 
  BwmRule of pdp/bearer[1]
  --------------- 
  No Matchs UpRevPkts UpRevByts DownRevPkts DownRevByts Name 
  1  58     100       2569      80          1894        bwm-rule1
  (结果个数 = 1)
  ```
- 显示当前用户的static-rule详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=RULE,RULETYPE=STATIC;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result = 
  Rule of pdp/bearer[0] 
  -------------------- 
  No. Status Type  Priority Matchs UpRevPkts UpRevByts DownRevPkts DownRevByts ActTime RuleType Name 
  1   Active Local 65       1      3         491       3           1408        0       pcc       rule1

  Current Used Quintuple Information
  ------------------------
  No. SrcIP         DstIP         SrcPort DstPort l4Protocol L7Protocol L7AppProtocol PayloadProtocol FilterName RuleName 
  1   10.114.114.4  192.168.64.13 49162   3761    tcp        17         19            0               mft_filter mft_rule0 
  (结果个数 = 1)
  ```
- 显示当前用户的dync-rule详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=RULE,RULETYPE=DYNC;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result  =  
  PDR information
  ---------------
           PDR ID = 1
         Priority = 4294967295
             Type = Predefine PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 2
         Priority = 4294967295
             Type = Predefine PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 3
         Priority = 1030
             Type = Dynamic PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 4
         Priority = 1030
             Type = Dynamic PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps
  PDR information
  (结果个数 = 1)
  ```
- 显示当前用户的car-shaping详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=CAR_SHAPING;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result = 

  pdp/bearer base info:
  ------------------------
  CAR information of pdp/bearer[1]
  ---------------------------
  No Cir  Cbs       Pir   Pbs       DrpPkts DrpByts BwmRulename 
  1  8590 393216000 17180 786432000 0       0 
  2  8590 393216000 17180 786432000 0       0 

  Shaping information of pdp/bearer[1]
  ---------------------------
  No Cir Cbs QueDepth DrpPkts DrpByts BwmRulename 

  Info: No matching Shaping info is found. 

  (结果个数 = 1)
  ```
- 显示当前用户的flow-info详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=FLOW;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result = 

  pdp/bearer base info:
  ------------------------
  Flow info in Dynamic-Rule information of pdp/bearer[1]
  --------------------
  No SrcIP/mask     DstIP/mask     SrcPort DstPort Protocol Dir  RuleName
  1  any            192.168.1.31/32 0       0       0        UP   rule1
  2  192.168.1.31/32 any            0       0       0        DOWN rule1
  (结果个数 = 1)
  ```
- 显示当前用户的protocol-info详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551",INFOTYPE=PROTOCOL;
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result = 
  Protocol-info of pdp/bearer[1]
  ---------------
  No.  SubProtocol                     Pkts       Bytes      
  1    http                            13         5512       
  total                                           5512 
  (结果个数 = 1)
  ```
- 显示当前用户的详细信息：

  ```
  DSP USERRUNINFOSTATE:USERTYPE=IMSI,IMSI="460011223344551";
  ```

  ```
  RETCODE = 0 操作成功.

  承载信息
  ------------------------
  Result  =  
  Info: No matching result is found.  

  Info: No matching PROTOCOL info is found. 

  Traffic information of  user[1]
  -------------------------------------
  UpRevPkts  UpRevByts   UpSndPkts   UpSndByts  DnRevPkts   DnRevByts   DnSndPkts   DnSndByts  UpRevPps    UpSndPps    DnRevPps    DnSndPps    
  0          0           0           0          0           0           0           0          0           0           0           0           

  Group CAR information of user[1]
  -------------------------------------
  No  Cir         Cbs         Pir         Pbs         DrpPkts     DrpByts     BwmRulename                      

  Info: No matching CAR info is found.  

  CAR information of user[1]
  -------------------------------------
  No  Cir         Cbs         Pir         Pbs         DrpPkts     DrpByts     BwmRulename                      

  Info: No matching CAR info is found.  

  Shaping information of user[1]
  -------------------------------------
  No  Cir         Cbs         QueDepth    DrpPkts     DrpByts     BwmRulename                      

  Info: No matching Shaping info is found.  

  PDR information
  ---------------
           PDR ID = 1
         Priority = 4294967295
             Type = Predefine PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 2
         Priority = 4294967295
             Type = Predefine PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 3
         Priority = 1030
             Type = Dynamic PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps

           PDR ID = 4
         Priority = 1030
             Type = Dynamic PDR
           Matchs = 0
           UpPkts = 0
           UpByts = 0
           DnPkts = 0
           DnByts = 0
           QER ID = 1
              Qci = 0
              Arp = 0
        GbrUpLink = 256000kbps
        GbrDwLink = 128000kbps
   Real GbrUpLink = 150000kbps
   Real GbrDwLink = 128000kbps
        MbrUpLink = 1024000kbps
        MbrDwLink = 1024000kbps
   Real MbrUpLink = 150000kbps
   Real MbrDwLink = 150000kbps
  PDR information
  ---------------
  SDF Filter info in PDR information
  ----------------------------------
  No     SDF FILTER ID SrcIP/mask         DstIP/mask         SrcPort     DstPort     Protocol Dir  PDR ID
  1      4294967295    any                any                0           0           0        1    1     
  2      4294967295    any                any                0           0           0        1    2     
  3      4294967295    any                any                0           0           0        1    3     
  4      4294967295    any                any                0           0           0        1    4

  (结果个数 = 1)
  ```

#### 输出结果说明

| 输出项名称       | 输出项解释                        |
|:------------|:-----------------------------|
| No          | 标识第几个用户上下文。                  |
| Matchs      | 匹配到该rule的次数。                 |
| UpRevPkts   | 上行入口包数统计。                    |
| UpRevByts   | 上行入口字节数统计。                   |
| UpSndPkts   | 上行出口包数统计。                    |
| UpSndByts   | 上行出口字节数统计。                   |
| DownRevPkts | 下行入口包数统计。                    |
| DownRevByts | 下行入口字节数统计。                   |
| DnSndPkts   | 下行出口包数统计。                    |
| DnSndByts   | 下行出口字节数统计。                   |
| Name        | 规则的名称。                       |
| RuleName    | 规则的名称。                       |
| BwmRulename | bwm-rule名字。                  |
| Status      | 规则的状态，包括Deactive和Active两种状态。 |
| RuleType    | 规则的类型。                       |
| Priority    | 规则的优先级。                      |
| ActTime     | 用户下发静态rule的时间。               |
| UpCir       | 上行承诺信息速率。                    |
| DownCir     | 上行承诺信息速率。                    |
| UpPir       | 上行峰值信息速率。                    |
| SrcIP       | 源地址/掩码。                      |
| DstIP       | 目的地址/掩码。                     |
| SrcPort     | 源端口。                         |
| DstPort     | 目的端口。                        |
| Protocol    | 协议号。                         |