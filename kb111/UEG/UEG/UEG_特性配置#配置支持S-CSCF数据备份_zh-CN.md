---
id: GWFD-025804
name: 配置支持S-CSCF数据备份
ne_type: UEG
type: feature
description: 该任务指导操作人员配置支持S-CSCF数据备份。  举例的数据将实现如下功能：在HSS上打开软参“CSCFDISASRSWITCH”支持S-CSCF容灾，并为对端S-CSCF配置了CSCF的容灾特性。在注册过程中，HSS会更新用户信息并保存S-CSCF发送过来的容灾数据；会话过程中，由于S-CSCF的重启或者故障HSS会支持下发S-CSCF容灾数据。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-025800 UDM语音基本功能","GWFD-025804 支持CSCF数据备份功能","支持S-CSCF数据备份功能","特性配置","配置支持S-CSCF数据备份"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置支持S-CSCF数据备份。举例的数据将实现如下功能：在HSS上打开软参“CSCFDISASRSWITCH”支持S-CSCF容灾，并为对端S-CSCF配置了CSCF的容灾特性。在注册过程中，HSS会更新用户信息并保存S-CSCF发送过来的容灾数据；会话过程中，由于S-CSCF的重启或者故障HSS会支持下发S-CSCF容灾数据。

## 必备事项
前提条件

前提条件

* 操作人员具有OM Portal权限。
* 操作人员具有PGW Web LMT客户端业务发放权限。
* 已完成软件安装和初始配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_insp_list:
      type: items
      properties:
        INSPT:
          name: '软件参数类型'
          type: string
          enum:
          - PCDR
          - LOG
          - HSS9860
          - IMS-HSS
          - ENS
          - GLOBALDATA
          - RELIABILITY
          - SRVCTRL
          - AAA
          - AGING
          - UIMCOMMON
          - GBA
          required: true
          description: '指定软参的类型。'
          data_source: ''
          pattern: ''
          default: ''
        INSPN:
          name: '软件参数名称'
          type: string
          enum:
          - PDCSMODULECONFIG
          - CALLPCDRSWITCH
          - TIMESTAMPPERIOD
          - CALLSYNPERIOD
          - NOCALLPCDRSWITCH
          - PCDRRESERVE
          - MSMODE
          - MSCOMPRESS
          - MSCLEARTIME
          - MSBUFREMAIN
          - LOGFLAG
          - LOGCONTROL
          - DBGLOGL0
          - DBGLOGL1
          - DBGLOGL2
          - DBGLOGL3
          - DBGLOGL4
          - RUNLOGL0
          - RUNLOGL1
          - RUNLOGL2
          - RUNLOGL3
          - RUNLOGL4
          - LOGFLOWCONTROL
          - HDFLOWCTRLSWITCH
          - MAXUDTDATALEN
          - CDRCRCSWITCH
          - CDRPOOLSWITCH
          - TOTALMSGNUM
          - AUCMSGNUM
          - SMSMSGNUM
          - EMAILMSGNUM
          - CDRMSGNUM
          - FEUPGRADESTATUS
          - MESSAGEFLOWCTRL
          - TRANSTCAPVERSION
          - BSGMSGDISTRIBUTE
          - LICINFODSPCTRL
          - IMSCMCTRACE
          - SH_ENTITY_FUNCTION
          - VOLTE_DATA_SYN_SWITCH
          - VOLTE_HSS_SYN_DATA_IN_MULTMODE
          - VOLTE_NOT_ISD_SWITCH
          - FORBIDCRCERR
          - SUPPORT_FAILOVER
          - TFLAG_IN_FAILOVER
          - TCAPVERSION
          - TCAPVERSIONSWITCH
          - SUPP_STANDARD_LOCVLRNUM_FORMAT
          - DIAM_SCTP_GET_MSG_BY_TIMER
          - HOST_REALM_REMAIN_UNCHANGED
          - REDUNDANCY_FE_DETECT
          - CPU_OVER_LOAD_THRESHOLD
          - MODULE_RST_WHEN_ALLOC_MEM_FAIL
          - IMS_DELIVER_MSG_MODE
          - PWD_COMP_SWITCH
          - VoLTE_ENHANCED_FEATURE_SWITCH
          - VOLTE_DATA_SYN_ODB_SWITCH
          - XMLFORMATCTRL
          - NETOPRTIMER
          - SHPULLTIMER
          - SHPULLTIMES
          - RESENDTIMES
          - STORESCSCF
          - WAITRSPFORNOTIFY
          - IgnoreSupportedFeatures
          - ENCRYPTSQNWITHAK
          - THIRDPARTYNOTIFYCONTROL
          - THIRDPARTYLDAPCONTROL
          - IGNORE_MULTIPLE_REGISTERATION
          - SIDVALIDPERIOD
          - AUTHFLAG
          - HSFMEMOVERTHRESHOLD
          - SAR_STORE_CHANGED_INFO
          - SNR_PNR_DEL_INVALID_INFO
          - DOWNLOADRLI
          - SLFPROXYSWITCH
          - AUTHPRIORITY
          - CHECKIMPI
          - RSIMAXLEN
          - MAPNODETYPE
          - WORKMODE
          - HCFMEMORYCAPABILITY
          - STMSWITCH
          - PSTDDSTRATEGY
          - MONPERIOD
          - HRMRSTIMES
          - CBMSWITCH
          - CBDECTECTTIME
          - CHECKFTNISINTER
          - EARLY_AKA_MODE
          - EARLY_AKA_NODE
          - IMS_UPG_CMP
          - HssErrUserRejudge
          - CSCFDISASRSWITCH
          - OVERLAP
          - SlfMatchControl
          - ESN_FORMAT
          - CAVEAKASwitch
          - SELACTIVEBE
          - IMSOneNumberWithCS
          - SUPPORT_3GPP_R8_WIMPU
          - MULTIPLE_MATCH_WILDCARDEDIMPU
          - SUPPORT_SH_EXPIRYTIME
          - SUPPORT_ALIASIND
          - EXTPRIORSWITCH
          - SESSIONPRIORITYLEVEL
          - THIRDPARTYNOTIFYIMPUCONTROL
          - AUTH_HA1_USE_NULL_USERNAME
          - LRF_GET_USER_LOC_MODE
          - SCHEMACHKREPOSITORYDATA
          - SHCFDINUSER
          - SH_REJECT_BARREDUSER
          - ATICONTAINREQEDINFOTYPE
          - ENSNPREQTIMEOUT
          - LIR_CHK_INVALID_SCSCFNAME
          - QUEUEMSGMAXLENGTH
          - GDATAVERIFY
          - GDATAVRFPERIOD
          - GDATAAUTORESUME
          - PRINTGLOBDATA
          - GLOBALDATASYNCTIME
          - GLOBDATASERIAL
          - LICDATAVRFPERIOD
          - GLOBDATADEALYTIMEBE
          - GLOBDATADEALYTIMECCU
          - WHOLESITESWITCH
          - BEFAULTDELAY
          - BERECOVERDELAY
          - WHOLESITEAUTORECOVER
          - NOTIFYSIGNSTATTOBE
          - SIGNALFAULTDELAY
          - SIGNALRECOVERDELAY
          - SUPP_DOWNTIME_FUNC
          - DOWNTIME_THRESHOLD
          - SENDUABORT
          - VOLTE_DATA_SYN_CAMEL_SWITCH
          - VOLTE_DATA_SYN_RBT_SWITCH
          - VOLTE_DATA_SYN_PLMNSS
          - VOLTE_DATA_SYN_EXTENSION_SWITCH
          - USERCACHEVALIDPERIOD
          - PAUTCPLINKHBCYCLE
          - PAUTCPLINKHBFAULTTIMES
          - PREUSER
          - LICENSEMODE
          - GIACCTTIMER
          - DIAMHDFLOWCTRLSWITCH
          - VOLTE_SYN_DATA_STORE_SWITCH
          - SWX_MAPNODETYPE
          - EXPMMLSWITCH
          - GLOBAL_DATA_RETRY_NUM
          - GLOBAL_DATA_RETRY_TIME
          - GLOBAL_DATA_TABLE_RETRY_NUM
          - DSPLICONTROL
          - NOT_CHECK_AAA_HOST
          - VOLTE_SYN_CW_BSG_SWITCH
          - N_DEL_IPSMGW
          - RECTIFY_MODEL_CXSH_FLAG
          - TRACE_AUTH_ANONYMIZATION
          - SERVICE_CONTROL_FUNCTION
          - SCF_CS_SAI
          - SCF_PS_SAI
          - SCF_S6AS6D_AIR
          - SCF_SWX_MAR
          - SCF_CXDX_MAR
          - SCF_ZH_MAR
          - VOLTE_SH_DATA_SYN_FORMAT
          - CS_UPL_SERIAL_SWITCH
          - EPS_ULR_SERIAL_SWITCH
          - FE_SND_BE_MODE
          - SET_NET_DETECT_ALARM_SWITCH
          - VOLTE_DATA_SYN_LRBT_SWITCH
          - VOLTE_DATA_SYN_LRBT_ECATEGORY
          - VOLTE_DATA_SYN_LRBT_PLMNSS
          - USSD_STAT_CONTROL
          - USSD_TRACE_ANONYMIZATION
          - RECORD_MEM_INFO_SWITCH
          - Q922_CRC_VRY_SWITCH
          - MEM_REFREE_CALLSTK_REC_SWITCH
          - MEM_REFREE_CALLSTK_REC_POLICY
          - MSG_REFREE_CALLSTK_REC_SWITCH
          - MSG_REFREE_CALLSTK_REC_POLICY
          - MEM_DESTROY_TEST_SWITCH
          - MEM_ABNORMAL_CHECK_SWITCH
          - IDP_CALLEDPARTNUMBER_ODDEVEN
          - PASSWORD_CHECK_SWITCH
          - MAXERRORTIME
          - UNLOCKTIME
          - VOLTE_SYN_CHK_SERREST_SWITCH
          - DIAM_SCTP_GET_MSG_MAX_TIME
          - VOLTE_DATA_SYN_PLMNSS_SWITCH
          - WHOLESITESWITCH_FE
          - REMOTE_FE_TIMEOUT
          - VOLTE_DATA_SYN_MMTELSERVICES_SWITCH
          - USSD_STAT_ADJUST_SWITCH
          - USSD_ABORT_STAT_FUNCTION
          - NFV_EVOLUTION_SWITCH
          - REDUNDANCYCHECK
          - REDUNDANCYCHECKTIMER
          - QUERYDBMODE
          - MAP_MSG_COUNT_MODE
          - VOLTE_WITHOUT_SERVICEDATA
          - IMS_MHOST_MODE
          - DCIMEMCACHESWITCH
          - GETDCIDATAMODE
          - ONELOGICAL_DYNLIC_VFY_MODE
          - QUINTUPLETNUMCTR
          - RETENTION_LOG
          - ENCODEFAILEDAVP
          - MEM_HANG_TIME_SET
          - MODULE_RST_RUNTIME
          - MODULE_RST_CPURATE
          - MAP_MSG_VALIDITY_CHECK_SWITCH
          - USER_STAT_MODE
          - SRIFORSM_SUPPRESS_HASH
          - IP_RECONSTRUCTION_SCENARIO
          - ENHANCED_IMS_LINK_QUERY_SWITCH
          - MEMORY_GUARD_SWITCH
          - CCUMSGMODE
          - DIAM_FORWORD_OPTI
          - HA_HEARTBEAT_TIMES
          - HA_HEARTBEAT_INTERVAL
          - ENHANCED_MSG_VALIDITY_CHECK_SWITCH
          - DIAM_FORWORD_WITH_FIX_SESSIONID
          - DYNLIC_MODE_ON_HYBRID_NETWORKS
          - EVO_AUTO_PROVISIONING_NOTIFY_MODE
          - EVO_AUTO_IMSI_CHANGE_NOTIFY_MODE
          - BECONNECTMODE
          - UDA_AGEOFLOCATION_INFO
          - TRACECTRL
          - DEV_TRACE_CTRL
          - SUPPORT_LINK_DOWN_PING
          - TRACEAUTOLOCK
          - SRVINNER_TRANSMISSION_ENCRYPT_SUPPORT
          - PLYCHECKSWITCH
          - UPGPHASE
          - SRVINNER_INNERMSG_SWITCH
          - MAP_DIAM_IP_SHARE_SWITCH
          - SUPPORT_VOLTE_LIC_STAT_MODE
          - PS_UPL_SERIAL_SWITCH
          - UDRMSGSTATMODE
          - DOPRA2SDRSWITCH
          - DRUBYPASSSWITCH
          - LIC_STAT_MODE
          - SCF_SCA_STU
          - MAP_MSG_LOOP_CHECK
          - LICENSE_BROADCAST_TIMER
          - TRACEFORMAT
          - PULL_IMSI_WITH_MSISDN
          - TCAP_START_ALARM_TIMES
          - TCAP_STOP_ALARM_TIMES
          - DIAM_START_ALARM_TIMES
          - DIAM_STOP_ALARM_TIMES
          - REPLYMSG
          - CHECKODB
          - FORCEUPL
          - CHECKNAI
          - IWLANCUI
          - IWLAN3GPPIMSI
          - STRRSPNOUSERNAME
          - ODBPOSCHECK
          - PEERTIMEOUT
          - RSPTIMEOUT
          - RETRYTIMES
          - NOTIFICATIONFAIL
          - CALLINGIDAUTH
          - MCCMNCWHITELIST
          - CHKROMAUSER
          - CHKAPN
          - ATTACHEDPERIODCHK
          - ODBINFO
          - USERNAME
          - VOWIFIMAP
          - STASESSIONNUM
          - S6BSESSIONNUM
          - S6BRAR
          - APIDPARSE
          - APIDNOMATCHREJECT
          - SWMSESSIONNUM
          - CHKPOLICY
          - DYNSWITCH
          - APNFMT
          - PAU_UDP_SERVER_PORT
          - IPAUTORECYCLE
          - IPPREALARM
          - IPALARM
          - IPPREALARMCLEAR
          - IPALARMCLEAR
          - PROXYRESPMOD
          - SUPPORTACSWITCH
          - CUISWITCH
          - SUPPORT_OPENSSL_RC4
          - NOACCTINTERVAL
          - RADIUSAVPCHECK
          - WISPRMAP
          - STOPCLEAN
          - STRRSPNOUSER
          - NOUSERNAME
          - NOSESSIONTIMEOUT
          - OCSRATINGGRP
          - NOOCSOCTTIME
          - OCSCGI
          - GENOCSCHARGINGID
          - OCSSERVERID
          - OCSQOS
          - OCSDEFAPNCC
          - IPALLOCCHKNSAPI
          - OLDSESSIONDM
          - PROXYSESSIONNUM
          - ONLYAPNVSA
          - RTRNEWSERVER
          - MOBILEUSERID
          - IPALLOCATION
          - IMSILEADINGADAPT
          - SNDIPPOOLTOMT
          - EXTAVPOVERWA
          - CONCEALIMSI
          - GENREALMFORMAT
          - IPQUERYNUM
          - IPPOOLCACHENUM
          - IPPOOLALLOCFAILNUM
          - NOSESSIGNOREACCTSTOP
          - STRKEEPUSERDATA
          - MNIDGENMODE
          - LOCALROAMCTRL
          - NOUEIPREJECTROAM
          - NOMATCHREJECTROAM
          - MULTIAPNIP
          - IMSIDECRYPTENABLE
          - DEFAULTIMSIVERIFID
          - SUPPORTREDIRECT
          - WCDMATIMEOUT
          - BROARDBANDTIMEOUT
          - WCDMAOFFSET
          - BROARDBANDOFFSET
          - IWLANOFFSET
          - CONTAIN_VNI
          - PPARTA_NOTCONTAIN_USERNAME
          - RADIUSPROXYFAILTIMES
          - PROXYRETRYPOLICY
          - PROXY_ALL_FAIL_CHK_PERIOD
          - IMSI_ENC_PROPORTION
          - AAA_IWLAN_BHCA
          - AAA_VOWIFI_BHCA
          - IMEI_CHK
          - DIAMSIMTOAKA
          - FORCEREGIST
          - IMSI_ENC_ALM_REPORT_PERIOD
          - FORCE_DEREG
          - SUPP_EMCALL
          - UPDATE_EMPGWADDR
          - EMCALL_SWMSENDCONF
          - VOWIFI5GSIWKSUPP
          - SESSIONAGINGFLAG
          - USERAGINGFLAG
          - N3GPPAGINGFLAG
          - GBAAGINGFLAG
          - N3GPPOLDTIME
          - GBAOLDTIME
          - OLDSTARTTIMEHOUR
          - OLDSTARTTIMEMIN
          - IMEIOLDTIME
          - IMEIAGINGFLAG
          - MSGAUTHDYNAUTH
          - SUPPORTIPV6
          - DIAMWITHOUTAVP
          - DIAMIGNOREAVP
          - DEACTIVESESSIONTIME
          - CHKAPPTYPESWITCH
          - QUERYMOD
          - NEEXPMMLANDPLA
          - LICDSPMODE
          - SCTPPLDID
          - END_TO_END_MODE
          - IPAUTOCOLOR
          - APWAITBSF
          - APCACHETM
          - CHKUSERID
          - IMPUPROXYMODE
          - BTIDEXPIREDTIMES
          - BTIDINVALIDCODE
          - INTERZNIF
          - IGNOREGUSS
          - OPAQUEERRPROCMODE
          - GENXAIDWITHMSISDN
          - BIAERRRSP503
          - HTTPLNKTYPE
          - HTTPRETRAN
          - RETRANWAITTIME
          - ATSNORSPNUM
          - ATSCHKPERIOD
          - AUTH_HDR_SPACE
          - SUPP_TOHOME
          - TRCCREATETHD
          - LIC_STAT_FOR_PM
          - TRCTASKCHECK
          - NETOPRTIMEROPT
          - NETOPRRSTOPT
          - AGING_SPEED_PER_ACF
          - AP_AUTH_ALG_TYPE
          - BSF_RSP_SERVER_CFG
          - BSF_AUTH_ALG_TYPE
          - LIC_STAT_USAGE_DSP_POLICY
          - UDMNETYPE
          required: true
          description: '此软参表示是否支持CSCF容灾。'
          data_source: ''
          pattern: ''
          default: ''
        INSPV:
          name: '软件参数值'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: '取值为“1”表示HSS支持S-CSCF网络容灾。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmle_list:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: '该参数用于标识本端实体的名称。  运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        LOCTYPE:
          name: '本端设备类型'
          type: string
          enum:
          - IMS-HSS
          - IMS-SLF
          - SAE-HSS
          - UEIR
          - LRF
          - IWF
          - IWF-EIR
          - AAA
          - BSF
          - AP
          required: true
          description: '该参数用于标识本端实体的类型。固定取值为“IMS-HSS(IMS-HSS)”。'
          data_source: ''
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: true
          description: '该参数用于标识本端实体的域名。  运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: true
          description: '该参数用于标识本端实体的主机名。  运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmpe_list:
      type: items
      properties:
        EN:
          name: 'S-CSCF名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          enum:
          - OTHER
          - AS
          - S-CSCF
          - I-CSCF
          - GGSN
          - SAE
          - BSF
          - IMS-HSS
          - E-CSCF
          - P-GW
          - ePDG
          - HSGW
          - Non-3GPP
          - AP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OTHER
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: true
          description: '统一规划。HSS与对端S-CSCF协商的参数之一，该名称必须唯一。'
          data_source: ''
          pattern: ''
          default: ''
    set_dmpecap_list:
      type: items
      properties:
        PEERNAME:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: '统一规划。该参数取值需要和**ADD DMPE**命令中的“实体名称”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        OPTYPE:
          name: '操作类型'
          type: string
          enum:
          - ADD
          - MOD
          required: false
          description: '固定取值。'
          data_source: ''
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          enum:
          - OTHER
          - AS
          - S-CSCF
          - I-CSCF
          - GGSN
          - SAE
          - BSF
          - IMS-HSS
          - E-CSCF
          - P-GW
          - ePDG
          - HSGW
          - Non-3GPP
          - AP
          required: true
          description: '统一规划。该参数取值需要和**ADD DMPE**命令中的“Diameter对端实体类型”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        CSCFFEATURELIST:
          name: 'Cx特性列表'
          type: string
          required: false
          description: '定义S-CSCF支持的“特性列表”。对应的参数值置为“1”，表示允许，置为“0”，表示禁止。  * SharedIFC(共享IFC)：表示支持共享IFC特性。 * CscfDisaster(CSCF容灾)：表示支持CSCF容灾特性。 * AliasInd(别名ID)：表示支持别名ID特性。'
          data_source: ''
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: false
          description: '统一规划。该参数取值需要和**ADD DMPE**命令中的“主机名”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: '统一规划。该参数取值需要和**ADD DMPE**命令中的“域名”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmlks_list:
      type: items
      properties:
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        LOCALNAM:
          name: 'Diameter本端实体名称'
          type: string
          maxLength: 127
          required: true
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        PEERNAM:
          name: 'Diameter对端实体名称'
          type: string
          maxLength: 127
          required: true
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        LNKMOD:
          name: '链路选择模式'
          type: string
          enum:
          - SESSIONIDBASED
          - POLLING
          - AORS
          - ACTIVE
          - ACTIVEWITHPRI
          - POLLINGWITHPRI
          required: true
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmlnk_list:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_hsystempara_list:
      type: items
      properties:
        SCSCF_BACKUP_DATA_SIZE:
          name: 'SCSCF容灾数据存储最大长度'
          type: string
          required: false
          description: '用于标识S-CSCF容灾数据存储最大长度。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_insp_list:
    - INSPT: IMS-HSS
      INSPN: CSCFDISASRSWITCH
      INSPV: 1
    add_dmle_list:
    - EN: 'HSS_0'
      LOCTYPE: SAE-HSS
      DN: 'huawei.com'
      HN: 'as.huawei.com'
    add_dmpe_list:
    - EN: 'scscf'
      PEERTYPE: OTHER
      HN: 'scscf.huawei.com'
    set_dmpecap_list:
    - PEERNAME: 'HSS_0'
      OPTYPE: ADD
      PEERTYPE: S-CSCF
      CSCFFEATURELIST: SharedIFC-1&CscfDisaster-1
      HN: 'scscf.huawei.com'
      DN: 'huawei.com'
    add_dmlks_list:
    - LINKSNAM: 'hss-scscf'
      LOCALNAM: 'HSS_0'
      PEERNAM: 'SCSCF'
      LNKMOD: POLLING
    add_dmlnk_list:
    - LNKNAME: 'LINK_SCSCF'
      LINKSNAM: 'HSS-SCSCF'
      HSFMID: 202
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSF211'
      PIPVER: IPV4
      PIPV4: '10.1.182.2'
      PPT: 4200
    set_hsystempara_list:
    - SCSCF_BACKUP_DATA_SIZE: 8K
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 **MOD INSP**是软参修改命令，误操作会对整个系统的正常运行造成严重影响，请谨慎操作。

### 执行**MOD INSP**命令修改容灾配置的软参信息，设置HSS支持S-CSCF数据备份的功能。

```jinja2
{%- for item in mod_insp_list -%}
    MOD INSP:
    {#- --- 必选参数 --- -#}
    INSPT={{item.INSPT}},
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

### 3 执行**ADD DMLE**命令增加一条Diameter本端实体记录

```jinja2
{%- for item in add_dmle_list -%}
    ADD DMLE:
    {#- --- 必选参数 --- -#}
    EN="{{item.EN}}",
    LOCTYPE={{item.LOCTYPE}},
    DN="{{item.DN}}",
    HN="{{item.HN}}",
    ;
{%- endfor -%}
```

### 4 执行**ADD DMPE**命令增加备用S-CSCF的设备记录，

```jinja2
{%- for item in add_dmpe_list -%}
    ADD DMPE:
    {#- --- 必选参数 --- -#}
    EN="{{item.EN}}",
    HN="{{item.HN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERTYPE is not none -%}
        PEERTYPE={{item.PEERTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 执行**SET DMPECAP**命令增加特性列表设置记录，“Cx特性列表”参数要选择“CscfDisaster(CSCF容灾)”。

```jinja2
{%- for item in set_dmpecap_list -%}
    SET DMPECAP:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    PEERTYPE={{item.PEERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.OPTYPE is not none -%}
        OPTYPE={{item.OPTYPE}},
    {%- endif -%}
    {%- if item.HN is not none -%}
        HN="{{item.HN}}",
    {%- endif -%}
    {%- if item.DN is not none -%}
        DN="{{item.DN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERTYPE=S-CSCF/I-CSCF 时必选 --- -#}
    {%- if item.PEERTYPE in ['S-CSCF', 'I-CSCF'] -%}
        CSCFFEATURELIST={{item.CSCFFEATURELIST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 执行**ADD DMLKS**命令增加备用S-CSCF的链路集记录。

```jinja2
{%- for item in add_dmlks_list -%}
    ADD DMLKS:
    {#- --- 必选参数 --- -#}
    LINKSNAM="{{item.LINKSNAM}}",
    LOCALNAM="{{item.LOCALNAM}}",
    PEERNAM="{{item.PEERNAM}}",
    LNKMOD={{item.LNKMOD}},
    ;
{%- endfor -%}
```

### 7 执行**ADD DMLNK**命令增加备用S-CSCF的链路记录。

```jinja2
{%- for item in add_dmlnk_list -%}
    ADD DMLNK:
    {#- --- 必选参数 --- -#}
    LNKNAME="{{item.LNKNAME}}",
    LINKSNAM="{{item.LINKSNAM}}",
    PTYPE={{item.PTYPE}},
    WMODE={{item.WMODE}},
    IPNAM1="{{item.IPNAM1}}",
    PIPVER={{item.PIPVER}},
    PPT={{item.PPT}},
    {#- --- 可选参数 --- -#}
    {%- if item.HSFMID is not none -%}
        HSFMID={{item.HSFMID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
    {%- if item.PIPVER == 'IPV4' -%}
        PIPV4="{{item.PIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 登录“IMS-HSS业务管理”窗口。

### 9 执行**SET HSYSTEMPARA**命令配置S-CSCF容灾数据存储最大长度。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=9 -->
```

