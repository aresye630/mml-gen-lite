---
id: ''
name: 配置IMS AKA鉴权(IMS-HSS与SAE-HSS/HLR融合部署场景)
ne_type: UEG
type: feature
description: 该任务指导操作人员配置IMS-HSS与SAE-HSS/HLR融合部署场景下的IMS AKA（Authentication and Key Agreement）鉴权业务。  举例的数据将实现如下功能：开户模型为1个IMPI（IP Multimedia Private Identity）、1个IMPU（IP Multimedia PUblic Identity），并增加IMPI和IMSI（International Mobile Subscriber Identity）的关联关系，为IMPI配置了SIM/USIM卡鉴权数据，用户携带IMS AKA鉴权模式到IMS域进行注册，如果配置IMS AKA鉴权数据正确，则用户在IMS网络上注册成功。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置IMS AKA鉴权(IMS-HSS与SAE-HSS/HLR融合部署场景)"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置IMS AKA鉴权(IMS-HSS与SAE-HSS/HLR融合部署场景)"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","HSS&UDM配置","配置IMS AKA鉴权(IMS-HSS与SAE-HSS/HLR融合部署场景)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置IMS-HSS与SAE-HSS/HLR融合部署场景下的IMS AKA（Authentication and Key Agreement）鉴权业务。举例的数据将实现如下功能：开户模型为1个IMPI（IP Multimedia Private Identity）、1个IMPU（IP Multimedia PUblic Identity），并增加IMPI和IMSI（International Mobile Subscriber Identity）的关联关系，为IMPI配置了SIM/USIM卡鉴权数据，用户携带IMS AKA鉴权模式到IMS域进行注册，如果配置IMS AKA鉴权数据正确，则用户在IMS网络上注册成功。

## 必备事项
前提条件

前提条件

* 操作人员具有OM Portal管理员权限。
* 操作人员具有PGW Web LMT客户端业务发放权限。
* 用户IMSI已在SAE-HSS/HLR上开户并签约AKA（Authentication and Key Agreement）鉴权特性。
* IMS-HSS和SAE-HSS/HLR之间的链路已经配置完成，具体可参见配置Diameter信令数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_sreg_list:
      type: items
      properties:
        NA:
          name: 'NA'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_himsi_list:
      type: items
      properties:
        IMPI:
          name: 'IMPI'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        ISDN:
          name: 'ISDN'
          type: string
          required: false
          description: '统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    set_heaa_list:
      type: items
      properties:
        IMPI:
          name: 'IMPI'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
        EAAFLAG:
          name: 'EAAFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hsub_list:
      type: items
      properties:
        SUBID:
          name: 'SUBID'
          type: string
          required: false
          description: '在IMS中，一个IMS签约用户唯一对应一个SUBID。'
          data_source: ''
          pattern: ''
          default: ''
        IMPI:
          name: 'IMPI'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
    set_hvncflag_list:
      type: items
      properties:
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
        VNCFLAG:
          name: 'VNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_hregauth_list:
      type: items
      properties:
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '无。'
          data_source: ''
          pattern: ''
          default: ''
        REGAUTH:
          name: 'REGAUTH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSPV:
          name: '软件参数值'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_sreg_list:
    - NA: Y
    add_himsi_list:
    - IMPI: user@huawei.com
      IMSI: '460001234567890'
      ISDN: '8613988888888'
    set_heaa_list:
    - IMPI: user@huawei.com
      EAAFLAG: TRUE
    add_hsub_list:
    - SUBID: subinfo
      IMPI: user@huawei.com
      IMPU: sip:user@huawei.com
    set_hvncflag_list:
    - IMPU: sip:user@huawei.com
      VNCFLAG: FALSE
    set_hregauth_list:
    - IMPU: sip:user@huawei.com
      REGAUTH: TRUE
    mod_insp_list:
    - INSPT: IMS-HSS
      INSPN: EARLY_AKA_MODE
      INSPV: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“IMS-HSS业务管理”窗口。

### 在HSS上进行操作之前需要确保表1中所列CSC上的参数按表中样例配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_sreg_list的变量区（command: MOD SREG） -#}
<!-- MISSING_MACRO: command=MOD SREG list_name=mod_sreg_list step_id=1 -->
```

### 2 执行**ADD HIMSI**命令增加IMSI、IMPI、ISDN三者的关联关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_himsi_list的变量区（command: ADD HIMSI） -#}
<!-- MISSING_MACRO: command=ADD HIMSI list_name=add_himsi_list step_id=2 -->
```

### 3 执行**SET HEAA**命令为指定的IMPI设置Early AKA鉴权模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_heaa_list的变量区（command: SET HEAA） -#}
<!-- MISSING_MACRO: command=SET HEAA list_name=set_heaa_list step_id=3 -->
```

### 4 执行**ADD HSUB**命令开户，增加一个IMPI和一个IMPU。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_hsub_list的变量区（command: ADD HSUB） -#}
<!-- MISSING_MACRO: command=ADD HSUB list_name=add_hsub_list step_id=4 -->
```

### 5 设置IMPU的IMS漫游权限检查标志。执行**SET HVNCFLAG**命令，设置IMPU的IMS漫游权限检查标志为“FALSE”，不进行漫游检查。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hvncflag_list的变量区（command: SET HVNCFLAG） -#}
<!-- MISSING_MACRO: command=SET HVNCFLAG list_name=set_hvncflag_list step_id=5 -->
```

### 如果要进行漫游检查需要把漫游权限检查标志设置为“TRUE”，漫游限制配置详细请参见配置IMS漫游限制。

### 6 执行**SET HREGAUTH**命令，设置IMPU的注册权限为“TRUE”，允许注册。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hregauth_list的变量区（command: SET HREGAUTH） -#}
<!-- MISSING_MACRO: command=SET HREGAUTH list_name=set_hregauth_list step_id=6 -->
```

### 7 登录“UEG MML命令”界面。

### 8 执行**MOD INSP**命令设置Early AKA鉴权处理方式。

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

