---
id: ''
name: 配置支持P-CSCF恢复机制
ne_type: UEG
type: feature
description: 该任务指导操作人员配置HSS支持P-CSCF恢复机制。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","HSS&UDM配置","配置支持P-CSCF恢复机制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置HSS支持P-CSCF恢复机制。

## 必备事项
前提条件

* 已完成基础数据配置。
* 操作人员具有数据配置权限。
* 操作人员具有PGW Web LMT客户端业务发放权限。
* 操作人员具有OM Portal权限。
* 操作人员已完全了解支持P-CSCF恢复机制功能。
* 已加载P-CSCF恢复机制业务的相关License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_hsystempara_list:
      type: items
      properties:
        P_CSCF_RESTORE_SUPP:
          name: '是否支持P-CSCF恢复机制'
          type: string
          required: false
          description: '用于标识HSS是否支持P-CSCF恢复机制。'
          data_source: ''
          pattern: ''
          default: ''
    set_mapconf_list:
      type: items
      properties:
        FORWARDING_SMS:
          name: '用户在IMS未注册但IP-SM-GW地址有效时是否转发SRI\_FOR\_SM消息给IP-SM-GW'
          type: string
          required: false
          description: '用于标识在短消息终结流程中，用户在IMS网络未注册，但IP-SM-GW地址有效时，HSS是否转发SRI\_FOR\_SM消息给IP-SM-GW。'
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
          description: '用于标识当IMS用户注销时，是否保留IP-SM-GW地址。  取值范围：  * 0：表示当IMS用户注销时，清除IP-SM-GW地址。 * 1：表示当IMS用户注销时，保留IP-SM-GW地址。  默认值：0'
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
    set_hsystempara_list:
    - P_CSCF_RESTORE_SUPP: TRUE
    set_mapconf_list:
    - FORWARDING_SMS: TRUE
    mod_insp_list:
    - INSPT: HSS9860
      INSPN: N_DEL_IPSMGW
      INSPV: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“IMS-HSS业务管理”窗口。

### 2 执行**SET HSYSTEMPARA**命令配置P-CSCF恢复机制。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=2 -->
```

### 3 登录“UDM业务管理”窗口。

### 4 执行**SET MAPCONF**配置在短消息终结流程中，用户在IMS网络未注册，但IP-SM-GW地址有效时，转发SRI\_FOR\_SM消息给IP-SM-GW。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapconf_list的变量区（command: SET MAPCONF） -#}
<!-- MISSING_MACRO: command=SET MAPCONF list_name=set_mapconf_list step_id=4 -->
```

### 5 登录“UEG MML命令”界面。

### 6 执行**MOD INSP**将软参“N\_DEL\_IPSMGW(IMS用户注销时是否保留IP-SM-GW地址)”配置为“1”。

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

