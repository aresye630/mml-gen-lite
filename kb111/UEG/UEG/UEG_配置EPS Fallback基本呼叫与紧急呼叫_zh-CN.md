---
id: ''
name: 配置EPS Fallback基本呼叫与紧急呼叫
ne_type: UEG
type: feature
description: UPCF支持EPS Fallback方案，用于部署IMS应用，为基本呼叫业务提供保障的带宽，确保用户享用优质语音和高清视频。还可以为紧急呼叫业务提供可靠的质量保证，保证用户在各种紧急的情况下，能够顺利拨打紧急呼叫号码。当用户使用语音呼叫业务时，针对业务是否为紧急呼叫，享有不同的资源分配优先级，并实行不同的计费策略，在5G网络无线环境较差时，可以通过EPS Fallback方案，将5G紧急呼叫业务回落到4G VoLTE紧急呼叫。  本章节以EPS Fallback基本呼叫与紧急呼叫合一部署场景进行介绍。  5G呼叫业务回落到4G网络后，策略接口采用N7或Gx上报会话请求消息，由对端设备的配置决定，本流程介绍以N7接口为例。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","PCRF&PCF配置","Rx接口（使用Diameter协议）EPS Fallback策略控制","配置EPS Fallback基本呼叫与紧急呼叫"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPCF支持EPS Fallback方案，用于部署IMS应用，为基本呼叫业务提供保障的带宽，确保用户享用优质语音和高清视频。还可以为紧急呼叫业务提供可靠的质量保证，保证用户在各种紧急的情况下，能够顺利拨打紧急呼叫号码。当用户使用语音呼叫业务时，针对业务是否为紧急呼叫，享有不同的资源分配优先级，并实行不同的计费策略，在5G网络无线环境较差时，可以通过EPS Fallback方案，将5G紧急呼叫业务回落到4G VoLTE紧急呼叫。本章节以EPS Fallback基本呼叫与紧急呼叫合一部署场景进行介绍。5G呼叫业务回落到4G网络后，策略接口采用N7或Gx上报会话请求消息，由对端设备的配置决定，本流程介绍以N7接口为例。

## 必备事项
前提条件

* 操作员已了解GWFD-025904 Rx接口（使用Diameter协议）EPS Fallback策略控制特性概述。
* 已完成配置UPCF与AF（基于Diameter协议）的对接数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_pcfinsp_list:
      type: items
      properties:
        INSPN:
          name: '参数名'
          type: string
          enum:
          - VRM_MAXIPCANSESNUMPERSPU
          - VRM_MAXAFSESNUMPERSPU
          - VRM_MAXSUBNUMPERSPU
          - VRM_UPGRADE
          - VRM_MAXRATBEARIDPERSES
          - VRM_SRVNUMPERUSR
          - VRM_MAXPAFNUM
          - VRM_MAXPCEFNUM
          - VRM_MAXRADIUSSRVNUM
          - VRM_MAXCONNECTIONPERPAF
          - VRM_MAXCONNECTIONPERPCEF
          - VRM_MAXLINKRADIUSSRV
          - VRM_SUBSRCIPTIONIDTYPE
          - VRM_GLBREFLASHINTERVAL
          - VRM_NOTIFYMSGMAXRECORDPERSUB
          - VRM_NOTIFYMSGMAXDAYPERSUB
          - VRM_REVALIDATIONTIMEMETHOD
          - VRM_NOSUBSCRIPTIONERRORCODE
          - VRM_NOTIFYMSGMAXWAITEDRECORDS
          - VRM_PRINTLOCALLOG
          - VRM_USRREVALIHRANGE
          - VRM_ONLINECHECK
          - VRM_TIMEZONEENHANCE
          - VRM_GXIMEIFORMAT
          - VRM_NOTIFYMSGMAXRECORDPERDSU
          - VRM_CLEARALLDYNCREATEDUSER
          - VRM_PEELDOMAINSWITCH
          - VRM_NOTIFYRCVER
          - VRM_FIRSTDAYOFWEEK
          - VRM_UPDATESPRSUBACTIVE
          - VRM_SUBCTRLRESULT
          - VRM_SPRSUBMAXOFFLINEDAYS
          - VRM_CHECKSUBSCRIBEDSERVICE
          - VRM_SUBACTCTRL
          - VRM_SESSIONCHECKINTERVAL
          - VRM_CHKSUBSRVSYTYPE
          - VRM_RARSENDSPEED
          - VRM_DIAREDIRECTSWITCH
          - VRM_PERIODVALUE
          - VRM_PROTECTTIMER
          - VRM_SENDUSERNUM
          - VRM_POLICYCASESENSITIVE
          - VRM_SESSIONRESTORATION
          - VRM_RXRPMAPRELATION
          - VRM_NOTIFYUSAGEUNITCONVERT
          - VRM_TIMEACCUMODE
          - VRM_SYSWITCH
          - VRM_PLMNMATCHPRIORITY
          - VRM_RESETNOTIFYRPT
          - VRM_REPORTINGLEVEL
          - VRM_RATINGGROUP
          - VRM_SERVICEIDENTIFIER
          - VRM_DFTCHARGINGPARA
          - VRM_LOGPRINTPERIOD
          - VRM_MAXBBERFNUM
          - VRM_MAXCONNECTIONPERBBERF
          - VRM_SPNOTIFYDOMAIN
          - VRM_EXSPRNOTIFICATION
          - VRM_SESSIONBACKUPSWITCH
          - VRM_DIAMHBINTERVAL
          - VRM_DIAMHBTIMES
          - VRM_EDRACCESSFORMATE
          - VRM_IPCANTERMSWITCH
          - VRM_DELBEAROPTION
          - VRM_LDAPREVBUFFERSIZE
          - VRM_NOTIFYOPTIMIZE
          - VRM_RESULTCODESWITCH
          - VRM_FMTIPADDR
          - VRM_GROUPDIAREDIRECTSWITCH
          - VRM_RMVSUBWITHOUTRAR
          - VRM_GRPMBRUSAGECACHE1
          - VRM_GRPMBRUSAGECACHE2
          - VRM_DYNRULEFORMAT
          - VRM_IPV6HASHLENGTH
          - VRM_DURATIONMKMATCH
          - VRM_SNRRECSPEED
          - VRM_DIAMTIMETHRD
          - VRM_LDAPTIMETHRD
          - VRM_RELGXBYRAATIMEOUT
          - VRM_SETHOMESRVZONE
          - VRM_MAXTDFNUM
          - VRM_TDFCCRUSPD
          - VRM_TDFCCRTSPD
          - VRM_PROCHEARTBEATTIMEOUT
          - VRM_MAXAUXILIARYAREA
          - VRM_AADIAREDIRECTSWITCH
          - VRM_DIAMFAILOVERSWITCH
          - VRM_DYNSMSMSISDN
          - VRM_SUBGRPCREATESUB
          - VRM_QUOTACROSSSERVICE
          - VRM_SYSUBIDTYPE
          - VRM_DEACTIVESERVICETIMER
          - VRM_QUOTALOGSWITCH
          - VRM_SIMPLEPOLICYSTATISTIC
          - VRM_GXTRIGGERCMP
          - VRM_QOSNEGOTIATIONSWITCH
          - VRM_IPFLOWANYCVT
          - VRM_SUBLISTNORULE
          - VRM_NTFOVERDUEMODE
          - VRM_DESTPEERMODE
          - VRM_SYNDATASWITCH
          - VRM_SYNDATAINTERVAL
          - VRM_TAIECGIMATCHMODE
          - VRM_SYCARRYSUBID
          - VRM_SYRESENDTIMES
          - VRM_DYNQUOTATIMEZONE
          - VRM_FIRSTGXSESSIONATTR
          - VRM_SESSIONIDHASHMODE
          - VRM_PEERFCDURATION
          - VRM_AFPOLICYRECALCULATE
          - VRM_SGWRESTORETIME
          - VRM_QUOTAUSEPRIORITY
          - VRM_SESSIONIDSWITCH
          - VRM_REPORTUSAGE
          - VRM_IMEIQUERYSERVICE
          - VRM_MCITRIGGERUDR
          - VRM_RXMAXUL
          - VRM_RXMAXDL
          - VRM_SYSESSIONCONTROLATTRIBUTE
          - VRM_SYSESSIONCONTROLVALUE
          - VRM_AUTORECUSRLOC
          - VRM_LINKDSPMODE
          - VRM_RXSTAINCAUTHAPPID
          - VRM_MAXAREANUM
          - VRM_GXSESSIONONLYVOLTE
          - VRM_LDAPDBTIMEOUT
          - VRM_OFFSETTIME
          - VRM_APNSENSITIVE
          - VRM_DYNGROUPNUMBERPERUSER
          - VRM_SYSESSIONBACKUP
          - VRM_NOTIFYATTRRESTRICTION
          - VRM_UNKNOWNRULEPROC
          - VRM_FORCEUPGRADEQOS
          - VRM_RMVGRPMEMBERACT
          - VRM_SYNUSRDATASPEED
          - VRM_SYCHARGINGCHARSWITCH
          - VRM_LICDSPMODE
          - VRM_GRPMBRPARENTSTATUSFLAG
          - VRM_TERMSESSNOTIFICATIONFLAG
          - VRM_DCIPRIORITY
          - VRM_SERVICEINFOSTATUSMODE
          - VRM_RXARPMAPPINGMODE
          - VRM_NOTIFYATTRENUMVALUEMODE
          - VRM_GLBSESDATAREFRESH
          - VRM_MAXPOCSCPNUM
          - VRM_SPUAUTOSWITCHOVER
          - VRM_PRAIDCODECMODE
          - VRM_DFTROAMINGSTATUS
          - VRM_MCIPROCMODE
          - VRM_VMSTORAGEFAULTRMSWITCH
          - VRM_PREBINDFORSESSIONBACKUP
          - VRM_SHARESYQUOTAMODE
          - VRM_MEMCHECKALARMSWITCH
          - VRM_QUOTASTATUSSTATISTIC
          - VRM_SUBIDCHOOSESWITCH
          - VRM_MCCMNCROAMREGION
          - VRM_TERMFIRSTSESSIONSWITCH
          - VRM_RECORDMEMSWITCH
          - VRM_Q922ERRMSGSWITCH
          - VRM_MEMFREERECORDSTKSWITCH
          - VRM_MEMFREERECORDSTKPOLICY
          - VRM_MSGFREERECORDSTKSWITCH
          - VRM_MSGFREERECORDSTKPOLICY
          - VRM_MEMALLOCFAILEDHOOKSWITCH
          - VRM_LOADINGALLAREADATA
          - VRM_MAXMSGTEMPLATENUM
          - VRM_PCEFHOSTTOGROUP
          - VRM_LINKBASEAPN
          - VRM_CBOVERRUNALMTH
          - VRM_CBRECOVERYALMTH
          - VRM_VOLTESESSINDEPENDENT
          - VRM_MEWORKROLE
          - VRM_RESETFORALLOCMEMFAILED
          - VRM_RESETFORALLOCMSGFAILED
          - VRM_ENABLEVOLTEAPNGXFLOWCTRL
          - VRM_CBWATCHTIME
          - VRM_DIAMMSGRELAYSWITCH
          - VRM_SYNTIMER
          - VRM_DEVAUDITACCELERATION
          - VRM_PENDINGTRANSACTIONNUM
          - VRM_VOLTEQRYSPR
          - VRM_TRIGGERRESTRICTTYPE
          - BLC_UPMUSERREQ
          - BLC_BEARUPDATE
          - BLC_WAITBEARTERM
          - BLC_ZONETYPE
          - BLC_SECPDPQOSCONTROL
          - RM_RATINGVOLRNDUNIT
          - RM_USGVOLRNDUNIT
          - RM_USGVOLRNDTHRESH
          - RM_RUSGVOLRNDUNIT
          - RM_RUSGVOLRNDTHRESH
          - RM_PLMNANDSGSNALM
          - RM_ALMCLRPERIOD
          - BLC_NOTIFYSENDINTERVAL
          - VRM_OCSCHARGEFLAGFORPRE
          - VRM_OCSCHARGEFLAGFORPOS
          - VRM_OCSCHARGEFLAGFOROTHER
          - BLC_DELSSINVALIDINTERVAL
          - BLC_DELSSINTERVAL
          - BLC_DELSSNUM
          - VRM_CHECKAPNIP
          - VRM_QCIUPGRADE
          - VRM_UNDERCONTROLTHRESHOLD
          - VRM_NORMALVALUE
          - UPM_SUBCTRL
          - UPM_ACCRARTIMEOUT
          - UPM_TIMERPLYCNTREQ
          - VRM_KPIMONITORINGSWITCH
          - VRM_TDFPOLICYMODE
          - VRM_RXBEARWITH5002
          - LIC_PREALMTH
          - VRM_QRYSPRPRIORITY
          - VRM_SDUROUTECONFILICTRAR
          - VRM_DBTIMERVALIDPERIOD
          - VRM_FORCERECOVERYSESSION
          - ALC_WAITAFTERM
          - VRM_RARWITHTRIGGER
          - VRM_RELEASERXTRIGGER
          - VRM_MAXIPCANNUMPERUSR
          - VRM_RETENTION_NOTIFYLOG
          - VRM_RETENTION_MNTLOG
          - VRM_RETENTION_EXPORT
          - VRM_MAXSESSBACKUPNUMPERSUB
          - VRM_SAVESYORGSTATUS
          - VRM_SNRSUPPORTSUBID
          - VRM_AUDITFAILEDCODE
          - VRM_ADJUSTSERVICEMODE
          - VRM_SYORIGINSTATEID
          - VRM_NOTRARWITHSAMEINSTALLRULE
          - VRM_CALCPRIBYSRVNAME
          - VRM_PENDINGTIME2LOCALTIME
          - VRM_MAXPCEFRADIUSNUM
          - VRM_RTPDRNOFLOW
          - VRM_SYDRASLRITIMEOUTSTRCTRL
          - VRM_GXREDIRECTACTION
          - VRM_GXRULEDEDUP
          - VRM_MCITOPGWSPEED
          - VRM_NRIPV6HASHLENGTH
          - VRM_SDCHARGINGCHARSWITCH
          - VRM_OFFLINESRVSWITCH
          - VRM_OFFLINEREDOLOG
          - VRM_VOLTESESSIONNOTUPDATE
          - VRM_BSFONLYVOLTE
          - VRM_BSFRESENDTIMES
          - VRM_BSFTIMEOUT
          - VRM_CHRGIDFMT
          - VRM_LONGTERMNTYRECORDPERSUB
          - VRM_GXQRYCHARINGSYSMODE
          - VRM_RECREATERULENOTIFICATION
          - VRM_PACKETFILTER
          - VRM_SNRWITHOUTHOSTMODE
          - VRM_SYCOUNTERTRANSMODE
          - VRM_MAXCONDITIONNUM
          - VRM_MAXQUOTANUM
          - VRM_RMVSYSRVBYRESULTCODE
          - VRM_VIRTUALSUBIDSWITCH
          - VRM_VOLTEPDPQRYSY
          - VRM_PACKETERRRATETYPE
          - VRM_IPDOMAINSENSITIVE
          - VRM_NRCOMBINEPRIORITYMODE
          - VRM_N15COMPATIBILITYSWITCH
          - VRM_HASHAUDITSWITCH
          - VRM_RECUSRLOCBASERAT
          - VRM_MULTIPCEFQRYDB
          - VRM_DEVAUDITSTARTTIME
          - VRM_MCIDELOLDSES
          - VRM_MCIDELOLDSESSPEED
          - VRM_CHECKSUBSRV
          - VRM_MASTERSLAVENOTIFYENHANCE
          - VRM_NEPEERSTATUS
          - VRM_NONOVERLOADERRORCODESW
          - VRM_AMFRESELECTSWITCH
          - VRM_REDIRECTSWITCH
          - VRM_POLICYASSOCIATESWITCH
          - VRM_DIAMDIRECTPATH
          - VRM_SMFALMWITHIPPORT
          - VRM_REGWITHINSTANCENAME
          - VRM_VIRTUALQUOTAREPORTUSAGE
          - VRM_SPONSORDYNRULEFORMAT
          - VRM_SRVTOKENNUM
          - VRM_UPDSMFSTA
          - VRM_N7CHGNORULESWITCH
          - VRM_QUOTAOBJNOTEXISTCALCMODE
          - VRM_SDRRELIABTRANSSWITCH
          - VRM_CALCULBYNR
          - VRM_GXSESSIONCHARGE
          - VRM_RARSPEEDDOWNCPU
          - VRM_RARSPEEDUPCPU
          - VRM_SUBSCRIBERGROUPMATCHMODE
          - VRM_SCANSTARTTIME
          - VRM_DISTRIQUERYMAXRECORD
          - VRM_GLBPARTITIONLOADINGSWITCH
          - VRM_COMPARECCRIUQOS
          - VRM_AUTORECUSRLOCEX
          - VRM_AVGCHILDPERPARENT
          - VRM_AVGPARENTPERCHILD
          - VRM_SELECTNTSMETHOD
          - VRM_QUOTADEDUCTMODE
          - VRM_MAXBEARNUMPERIPCAN
          - VRM_SDSESSIONBACKUP
          - VRM_SERVICEZONEAREAMATCHTYPE
          - VRM_USRLOCATION_VALUE
          - VRM_RULESUFFIXLENAPPMODE
          - VRM_TAIMATCHINGMODE
          - VRM_N7PCCNOCHGANINFOSW
          - VRM_N5SESSIONBACKUP
          - VRM_PROFILEUPDATEBASERULEPRI
          - VRM_AFSELBINDCFG
          - VRM_ROUTEQUERYRETRYTIMES
          - VRM_ROUTEQUERYRETRYINTERVAL
          - VRM_NOTIFYBEFOREEXPIRE
          - VRM_N36INTERFACESW
          - VRM_N36SUBSCRIPTIONSW
          - VRM_PCFLIPSELECTMODE
          - VRM_PESSRVDISCTIMER
          - VRM_EXATTR1DEFAULTVALUE
          - VRM_HTTPCLIENTREDIRECTTIMES
          - VRM_N23SWITCH
          - VRM_DIAMGETAPPID
          - VRM_N23SESSIONBACKUP
          - VRM_GLBDATAIDMAPSWITCH
          - VRM_PEERNFDEFAULTPRIORITY
          - VRM_N23SESADTMSGSPEED
          - VRM_IPDOMAINSRCFORGX
          - VRM_N15VIRTUALSUBIDSWITCH
          - VRM_SESSIONCOMPRESSTYPE
          - VRM_UPDAMFSTA
          - VRM_N23TIMEOUT
          - VRM_MAXAMSAUNUMPERSPU
          - VRM_N24AMSWITCH
          - VRM_N24AMTIMEOUT
          - VRM_CALLRXFIRSTSW
          - VRM_BACKFILLSESRULE
          - VRM_N7NWDAFLINKDOWNSW
          - VRM_N7POLICYCHGN23SW
          - VRM_RSTSYQUOTASW
          - VRM_HTTPLOCFILLMODE
          - VRM_DRALINKSTAMPUPTMODE
          - VRM_TRACECACHECHKSW
          - VRM_N15AREACODESW
          - VRM_USELASTPLMNIFNOTMATCHED
          - VRM_AUTORESETSWITCH4FSM
          - VRM_N23HDPCFIDMODE
          - VRM_CALCREDPRIBYNAME
          - VRM_STATEXTERNALRESTORATION
          - VRM_BSFBINDINGUPDATESW
          - VRM_SBICALLBACKVALUE
          - VRM_NGPOLICYCASESENSITIVE
          - VRM_N15QRYCHARINGSYSMODE
          - VRM_AFUPDATEUMMODE
          - VRM_HSRCTRLSW
          - VRM_CALCMEDRULEPRIBYNAME
          - VRM_DATAVIRTUALSUBIDSWITCH
          - VRM_INTRANETSESSEFFMODE
          - VRM_N28PENDINGTIME2LOCAL
          - VRM_MIDNIGHTGLBREFRESHSWITCH
          - VRM_SCANFROZENUSER
          - VRM_N1NOTIFYTIMER
          - VRM_MAXNWDAFSESNUMPERSPU
          - VRM_PCEFPARAMATCHMODE
          - VRM_N5VIRTUALMEDIA
          - VRM_SYQTAINSTMODE
          - VRM_N7UPDATECAFCRXMODE
          - VRM_N7ACTN23POLICYMODE
          - VRM_N23BAKCOMPATIBILITYSW
          - VRM_N7MAXDYNRULENUM
          - VRM_N7FAILRCPROCMETHOD
          - VRM_DELAYSTATAUTOENABLEDSW
          - VRM_AUTHSRVENCODEMODE
          - VRM_SUBLOCNUM
          - VRM_HPCFDELIVERLOCCHSW
          - VRM_N15RMVSPCMCCFROMGPSI
          - VRM_MODULERSTPROTECTTIME
          - VRM_N15DYNMATCHMODE
          - VRM_NESTATUSREFRESHCYCLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSPV:
          name: '参数值'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNID:
          name: 'APN标识'
          type: integer
          minimum: 0
          maximum: 319
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNTYPE:
          name: 'APN类型'
          type: string
          enum:
          - Revalidation-APN
          - Multi-PCEF-APN
          - Emergency-APN
          - VoLTE-APN
          - Force-Sy-APN
          - Statistics-APN
          - Ignore-SPR-APN
          - Realm-Replace-APN
          - Bypass-IP-APN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Revalidation-APN
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          enum:
          - FullMatching
          - LongestPrefixMatching
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FullMatching
    add_apn_list_1:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNID:
          name: 'APN标识'
          type: integer
          minimum: 0
          maximum: 319
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNTYPE:
          name: 'APN类型'
          type: string
          enum:
          - Revalidation-APN
          - Multi-PCEF-APN
          - Emergency-APN
          - VoLTE-APN
          - Force-Sy-APN
          - Statistics-APN
          - Ignore-SPR-APN
          - Realm-Replace-APN
          - Bypass-IP-APN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Revalidation-APN
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          enum:
          - FullMatching
          - LongestPrefixMatching
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FullMatching
  examples:
    mod_pcfinsp_list:
    - INSPN: UPM_SUBCTRL
      INSPV: 1
    add_apn_list:
    - PCRFID: 1
      APNID: 1
      APNNAME: 'ims'
      APNTYPE: VoLTE-APN
      APNMATCHTYPE: FullMatching
    add_apn_list_1:
    - PCRFID: 1
      APNID: 2
      APNNAME: 'SOS'
      APNTYPE: VoLTE-APN
      APNMATCHTYPE: FullMatching
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

#### 1.1 执行**MOD PCFINSP**命令，设置参数UPM\_SUBCTRL为“1”，即宽松签约模式。

```jinja2
{%- for item in mod_pcfinsp_list -%}
    MOD PCFINSP:
    {#- --- 必选参数 --- -#}
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

#### 1.2 执行ADD APN命令，添加“VoLTE-APN”类型的APN。

#### 该命令用来防止数据业务的规则下发给IMS。命令举例如下：

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    PCRFID={{item.PCRFID}},
    APNID={{item.APNID}},
    APNNAME="{{item.APNNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APNTYPE is not none -%}
        APNTYPE={{item.APNTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：APNTYPE=Emergency-APN/VoLTE-APN/Revalidation-APN/Force-Sy-APN/Ignore-SPR-APN/Realm-Replace-APN 时可选 --- -#}
    {%- if item.APNTYPE in ['Emergency-APN', 'VoLTE-APN', 'Revalidation-APN', 'Force-Sy-APN', 'Ignore-SPR-APN', 'Realm-Replace-APN'] -%}
        {%- if item.APNMATCHTYPE is not none -%}
            APNMATCHTYPE={{item.APNMATCHTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 执行ADD APN命令，添加“VoLTE-APN”和“Emergency-APN”类型的APN。

#### 流控场景下需要保证紧急呼叫，用于配置EPS FallBack紧急呼叫APN。命令举例如下：

```jinja2
{%- for item in add_apn_list_1 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    PCRFID={{item.PCRFID}},
    APNID={{item.APNID}},
    APNNAME="{{item.APNNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APNTYPE is not none -%}
        APNTYPE={{item.APNTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：APNTYPE=Emergency-APN/VoLTE-APN/Revalidation-APN/Force-Sy-APN/Ignore-SPR-APN/Realm-Replace-APN 时可选 --- -#}
    {%- if item.APNTYPE in ['Emergency-APN', 'VoLTE-APN', 'Revalidation-APN', 'Force-Sy-APN', 'Ignore-SPR-APN', 'Realm-Replace-APN'] -%}
        {%- if item.APNMATCHTYPE is not none -%}
            APNMATCHTYPE={{item.APNMATCHTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### “APNNAME”的取值需要以运营商实际规划的APN名称为准。

### 2 登录UPCF Web UI界面。

### 3 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置5个条件组，用于分别判断不同的媒体类型（语音呼叫或视频呼叫）、媒体流的使用方式、是否紧急呼叫。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Emergency\_EPSFB |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | C\_Emergency\_EPSFB |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：IsEmergencySession |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Yes  说明：  表示此会话为紧急呼叫。 |

### | 条件组2 | 基本信息 | 名称 | CG\_Audio\_EPSFB |

### |  |  | 关系 | AND |

### |  | 条件1 | 名称 | C\_NotEmergency\_EPSFB |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：IsEmergencySession |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | No  说明：  表示此会话为非紧急呼叫。 |

### |  | 条件2 | 名称 | C\_Audio\_EPSFB |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：MediaType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Audio  说明：  表示媒体类型为语音呼叫。 |

### | 条件组3 | 基本信息 | 名称 | CG\_Video\_EPSFB |

### |  |  | 关系 | AND |

### |  | 条件1 | 名称 | C\_NotEmergency\_EPSFB |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：IsEmergencySession |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | No  说明：  表示此会话为非紧急呼叫。 |

### |  | 条件2 | 名称 | C\_Video\_EPSFB |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：MediaType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Video  说明：  表示媒体类型为视频呼叫。 |

### | 条件组4 | 基本信息 | 名称 | CG\_FlowUsage\_NoEq\_RTCP |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | cond\_FlowUsage\_NoEq\_RTCP |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：FlowUsage |

### |  |  | 操作符 | Not Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | RTCP |

### | 条件组5 | 基本信息 | 名称 | CG\_FlowUsage\_Eq\_RTCP |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | cond\_FlowUsage\_Eq\_RTCP |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：FlowUsage |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | RTCP |

### 4 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 此场景需配置5G动作：Ambr、Arp、DefaultQosInformation、SessionRuleAction、BasicInfoAction、FlowDescription、FlowInformation、QoSData、TrafficControlData、DynamicPccRule和DynamicPccRuleIMS，相关应用场景如下：

### Ambr：用于设置会话类型的上下行带宽。

### Arp：当需要配置“类型”为“QoSData”和“DefaultQosInformation”的动作组时必须配置此动作。

### DefaultQosInformation：用于设置会话类型的QoS信息。

### SessionRuleAction：需要配置会话类型规则，需要配置此动作。

### BasicInfoAction：用于设置QoS流的方式为IMS信令。

### FlowDescription：当需要下发流方向时需配置此动作。

### FlowInformation：当需要下发流信息时需配置此动作。

### QoSData：当需要进行带宽控制时均需配置此动作，若不配置则表示不限制QoS。

### TrafficControlData：当需要做门限控制时，配置此动作。在下发流描述时，如果不配默认为放通该流，当需要限制流时，此动作必须配置。此场景根据AF请求的Flow-Status，下发门限策略。

### DynamicPccRule：需要配置动态类的业务规则，需要配置此动作。

### DynamicPccRuleIMS：EPS Fallback场景使用AF携带的流信息时需要配置此动作。

### 请增加如下5G动作组和动作：

### 动作组AG\_IMSDef\_ambr和AG\_EmerDef\_ambr：动作类型为Ambr

### 动作组AG\_IMSDef\_Arp、AG\_EmerDef\_Arp、AG1\_Audio\_ARPRTP、AG1\_Audio\_ARPRTCP、AG2\_Video\_ARPRTP、AG2\_Video\_ARPRTCP、AG3\_Emergency\_ARPRTP和AG3\_Emergency\_ARPRTCP：动作类型为Arp

### 动作组AG\_IMSDef\_def和AG\_EmerDef\_def：动作类型为DefaultQosInformation

### 动作组AG\_IMSDef\_SessRule和AG\_EmerDef\_SessRule：动作类型为SessionRuleAction

### 动作组AG\_IMSDef\_BasicRule和AG\_EmerDef\_BasicRule：动作类型为BasicInfoAction

### 动作组AG\_IMSDef\_FlowD和AG\_EmerDef\_FlowD：动作类型为FlowDescription

### 动作组AG\_IMSDef\_Finfo和AG\_EmerDef\_Finfo：动作类型为FlowInformation

### 动作组AG\_IMSDef\_QoSData、AG\_EmerDef\_QoS、AG1\_Audio\_QoSRTP、AG1\_Audio\_QoSRTCP、AG2\_Video\_QoSRTP、AG2\_Video\_QOSRTCP、AG3\_Emergency\_QoSRTP和AG3\_Emergency\_QOSRTCP：动作类型为QoSData

### 动作组AG\_IMSDef\_TrafficCtrl、AG\_EmerDef\_TrafficCtrl、AG1\_Audio\_tcRTP、AG1\_Audio\_tcRTCP、AG2\_Video\_tcRTP、AG2\_Video\_tcRTCP、AG3\_Emergency\_tcRTP和AG3\_Emergency\_tcRTCP：动作类型为TrafficControlData

### 动作组AG\_IMSDef\_PccRule和AG\_EmerDef\_PccRule：动作类型为DynamicPccRule

### 动作组AG1\_AudioRTP\_PccRule、AG1\_AudioRTCP\_PccRule、AG2\_VideoRTP\_PccRule、AG2\_VideoRTCP\_PccRule、AG3\_EmergencyRTP\_PccRule和AG3\_EmergencyRTCP\_PccRule：动作类型为DynamicPccRuleIMS

### 动作组的数据规划如表3所示，详细参数说明请参见5G动作组参数表。

### **表3** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_IMSDef\_ambr |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | downlink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组2 | 基本信息 | 名称 | AG\_IMSDef\_Arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：2 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组3 | 基本信息 | 名称 | AG\_IMSDef\_def |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：5 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_Arp  说明：  已在5G动作组中定义。 |

### | 5G动作组4 | 基本信息 | 名称 | AG\_IMSDef\_SessRule |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG\_IMSDef\_SessRule |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_ambr  说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_def  说明：  已在5G动作组中定义。 |

### | 5G动作组5 | 基本信息 | 名称 | AG\_IMSDef\_FlowD |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组6 | 基本信息 | 名称 | AG\_IMSDef\_Finfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_FlowD  说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组7 | 基本信息 | 名称 | AG\_IMSDef\_TrafficCtrl |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG\_IMSDef\_TrafficCtrl |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组8 | 基本信息 | 名称 | AG\_IMSDef\_QoSData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_IMSDef\_QoSData |

### |  |  | 5qi | * 类型：Value * 值：5 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组9 | 基本信息 | 名称 | AG\_IMSDef\_PccRule |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_IMSDef\_PccRule |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_Finfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_QoSData 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_IMSDef\_TrafficCtrl 说明：  已在5G动作组中定义。 |

### | 5G动作组10 | 基本信息 | 名称 | AG\_IMSDef\_BasicRule |

### |  |  | 类型 | BasicInfoAction |

### |  | 属性 | qosFlowUsage | * 类型：Value * 值：IMS\_SIG |

### | 5G动作组11 | 基本信息 | 名称 | AG\_EmerDef\_ambr |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | downlink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组12 | 基本信息 | 名称 | AG\_EmerDef\_Arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组13 | 基本信息 | 名称 | AG\_EmerDef\_def |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：5 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_Arp  说明：  已在5G动作组中定义。 |

### | 5G动作组14 | 基本信息 | 名称 | AG\_EmerDef\_SessRule |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG\_EmerDef\_SessRule |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_ambr  说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_def  说明：  已在5G动作组中定义。 |

### | 5G动作组15 | 基本信息 | 名称 | AG\_EmerDef\_FlowD |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组16 | 基本信息 | 名称 | AG\_EmerDef\_Finfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_FlowD  说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组17 | 基本信息 | 名称 | AG\_EmerDef\_TrafficCtrl |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG\_EmerDef\_TrafficCtrl |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组18 | 基本信息 | 名称 | AG\_EmerDef\_QoS |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_EmerDef\_QoS |

### |  |  | 5qi | * 类型：Value * 值：5 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组19 | 基本信息 | 名称 | AG\_EmerDef\_PccRule |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_EmerDef\_PccRule |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_Finfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_QoS 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_EmerDef\_TrafficCtrl 说明：  已在5G动作组中定义。 |

### | 5G动作组20 | 基本信息 | 名称 | AG\_EmerDef\_BasicRule |

### |  |  | 类型 | BasicInfoAction |

### |  | 属性 | qosFlowUsage | * 类型：Value * 值：IMS\_SIG |

### | 5G动作组21 | 基本信息 | 名称 | AG1\_Audio\_ARPRTCP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：6 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组22 | 基本信息 | 名称 | AG1\_Audio\_tcRTCP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG1\_Audio\_tcRTCP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组23 | 基本信息 | 名称 | AG1\_Audio\_QoSRTCP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG1\_Audio\_QoSRTCP |

### |  |  | 5qi | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG1\_Audio\_ARPRTCP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组24 | 基本信息 | 名称 | AG1\_AudioRTCP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG1\_AudioRTCP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：4 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG1\_Audio\_QoSRTCP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG1\_Audio\_tcRTCP 说明：  已在5G动作组中定义。 |

### | 5G动作组25 | 基本信息 | 名称 | AG1\_Audio\_ARPRTP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：6 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组26 | 基本信息 | 名称 | AG1\_Audio\_tcRTP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG1\_Audio\_tcRTP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组27 | 基本信息 | 名称 | AG1\_Audio\_QoSRTP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG1\_Audio\_QoSRTP |

### |  |  | 5qi | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG1\_Audio\_ARPRTP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组28 | 基本信息 | 名称 | AG1\_AudioRTP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG1\_AudioRTP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：0 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG1\_Audio\_QoSRTP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG1\_Audio\_tcRTP 说明：  已在5G动作组中定义。 |

### | 5G动作组29 | 基本信息 | 名称 | AG2\_Video\_ARPRTCP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：7 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组30 | 基本信息 | 名称 | AG2\_Video\_tcRTCP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG2\_Video\_tcRTCP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组31 | 基本信息 | 名称 | AG2\_Video\_QOSRTCP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG2\_Video\_QOSRTCP |

### |  |  | 5qi | * 类型：Value * 值：2 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG2\_Video\_ARPRTCP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组32 | 基本信息 | 名称 | AG2\_VideoRTCP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG2\_VideoRTCP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG2\_Video\_QOSRTCP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG2\_Video\_tcRTCP 说明：  已在5G动作组中定义。 |

### | 5G动作组33 | 基本信息 | 名称 | AG2\_Video\_ARPRTP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：7 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组34 | 基本信息 | 名称 | AG2\_Video\_tcRTP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG2\_Video\_tcRTP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组35 | 基本信息 | 名称 | AG2\_Video\_QoSRTP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG2\_Video\_QoSRTP |

### |  |  | 5qi | * 类型：Value * 值：2 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG2\_Video\_ARPRTP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组36 | 基本信息 | 名称 | AG2\_VideoRTP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG2\_VideoRTP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG2\_Video\_QoSRTP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG2\_Video\_tcRTP 说明：  已在5G动作组中定义。 |

### | 5G动作组37 | 基本信息 | 名称 | AG3\_Emergency\_ARPRTCP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组38 | 基本信息 | 名称 | AG3\_Emergency\_tcRTCP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG3\_Emergency\_tcRTCP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组39 | 基本信息 | 名称 | AG3\_Emergency\_QOSRTCP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG3\_Emergency\_QOSRTCP |

### |  |  | 5qi | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_ARPRTCP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组40 | 基本信息 | 名称 | AG3\_EmergencyRTCP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG3\_EmergencyRTCP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_QOSRTCP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_tcRTCP 说明：  已在5G动作组中定义。 |

### | 5G动作组41 | 基本信息 | 名称 | AG3\_Emergency\_ARPRTP |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组42 | 基本信息 | 名称 | AG3\_Emergency\_tcRTP |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG3\_Emergency\_tcRTP |

### |  |  | flowStatus | * 类型：Object Attribute * 值：ApplicationSession.FlowStatus |

### | 5G动作组43 | 基本信息 | 名称 | AG3\_Emergency\_QoSRTP |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG3\_Emergency\_QoSRTP |

### |  |  | 5qi | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_ARPRTP 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### |  |  | gbrUl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthUL |

### |  |  | gbrDl | * 类型：Object Attribute * 值：ApplicationSession.MaxRequestBandwidthDL |

### | 5G动作组44 | 基本信息 | 名称 | AG3\_EmergencyRTP\_PccRule |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG3\_EmergencyRTP\_PccRule |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_QoSRTP 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG3\_Emergency\_tcRTP 说明：  已在5G动作组中定义。 |

### 5 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### EPS Fallback场景下，规则的“类型”需要配置为“5G Smf Pcc Rule for IMS”。

### 当Rx接口携带多个QoS请求能力不同的流信息时，因不同的流QoS能力不同，则需配置不同的条件组和refQosData动作被不同的“类型”为“5G Smf Pcc Rule for IMS”的规则关联。

### 规则的数据规划如表4所示，详细参数说明请参见规则参数表。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | IMSDef\_Sess\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 5G动作组 | 5G动作组 | AG\_IMSDef\_SessRule  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | IMSDef\_Pcc\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 5G动作组 | 5G动作组 | AG\_IMSDef\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | IMSDef\_Basic\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Basic Rule |

### |  | 5G动作组 | 5G动作组 | AG\_IMSDef\_BasicRule  说明：  已在5G动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | EmerDef\_Sess\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 5G动作组 | 5G动作组 | AG\_EmerDef\_SessRule  说明：  已在5G动作组中定义。 |

### | 规则5 | 基本信息 | 名称 | EmerDef\_Pcc\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 5G动作组 | 5G动作组 | AG\_EmerDef\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则6 | 基本信息 | 名称 | EmerDef\_Basic\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Basic Rule |

### |  | 5G动作组 | 5G动作组 | AG\_EmerDef\_BasicRule  说明：  已在5G动作组中定义。 |

### | 规则7 | 基本信息 | 名称 | EPSFB\_AudioRTP\_Rule1 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | * CG\_Audio\_EPSFB * CG\_FlowUsage\_NoEq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG1\_AudioRTP\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则8 | 基本信息 | 名称 | EPSFB\_AudioRTCP\_Rule1 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | * CG\_Audio\_EPSFB * CG\_FlowUsage\_Eq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG1\_AudioRTCP\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则9 | 基本信息 | 名称 | EPSFB\_VideoRTP\_Rule2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | * CG\_Video\_EPSFB * CG\_FlowUsage\_NoEq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG2\_VideoRTP\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则10 | 基本信息 | 名称 | EPSFB\_VideoRTCP\_Rule2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件 | * CG\_Video\_EPSFB * CG\_FlowUsage\_Eq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG2\_VideoRTCP\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则11 | 基本信息 | 名称 | EPSFB\_EmergencyRTP\_Rule3 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | * CG\_Emergency\_EPSFB * CG\_FlowUsage\_NoEq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG3\_EmergencyRTP\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则12 | 基本信息 | 名称 | EPSFB\_EmergencyRTCP\_Rule3 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | * CG\_Emergency\_EPSFB * CG\_FlowUsage\_Eq\_RTCP 说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG3\_EmergencyRTCP\_PccRule  说明：  已在5G动作组中定义。 |

### 6 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 请增加如下策略：

### IMSDef\_Policy：用户从IMS APN上线时被调用的策略，触发器为IPCAN\_EST。

### EmerDef\_Policy：用户从紧急呼叫APN上线时被调用的策略，触发器为IPCAN\_EST。

### EPSFB\_Dedicate\_Policy：UPCF接收到EPS Fallback应用会话请求时触发的策略，触发器为AFSessionAuthorization。

### 策略的数据规划如表5所示，详细参数说明请参见策略参数表。

### **表5** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略1 | 基本信息 | 名称 | IMSDef\_Policy |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * IMSDef\_Sess\_Rule * IMSDef\_Pcc\_Rule * IMSDef\_Basic\_Rule 说明：  已在规则中定义。 |

### | 策略2 | 基本信息 | 名称 | EmerDef\_Policy |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * EmerDef\_Sess\_Rule * EmerDef\_Pcc\_Rule * EmerDef\_Basic\_Rule 说明：  已在规则中定义。 |

### | 策略3 | 基本信息 | 名称 | EPSFB\_Dedicate\_Policy |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | AFSessionAuthorization |

### |  | 规则 | 名称 | * EPSFB\_AudioRTP\_Rule1 * EPSFB\_AudioRTCP\_Rule1 * EPSFB\_VideoRTP\_Rule2 * EPSFB\_VideoRTCP\_Rule2 * EPSFB\_EmergencyRTP\_Rule3 * EPSFB\_EmergencyRTCP\_Rule3 说明：  已在规则中定义。 |

### 7 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 请增加如下业务：

### IMSDef\_Service：由PCEF激活的业务，用于创建IMS信令默认QoS Flow。此业务被动态用户组签约，故参数“签约后才能使用”必须配置为“是”。

### EmerDef\_Service：由PCEF激活的业务，用于创建IMS信令默认QoS Flow。此业务被动态用户组签约，故参数“签约后才能使用”必须配置为“是”。

### EPSFB\_Dedicate\_Service：由AF激活的EPS Fallback应用业务，如语音、视频、紧急呼叫等。因为此业务不需要用户签约，故参数“签约后才能使用”必须配置为“否”。

### 业务的数据规划如表6 所示，详细参数说明请参见业务参数表。

### **表6** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务1 | 基本信息 | 名称 | IMSDef\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | APN | ims  说明：  需要与1中**ADD APN**命令的参数“APN名称”取值保持一致。 |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | IMSDef\_Policy  说明：  已在策略中定义。 |

### | 业务2 | 基本信息 | 名称 | EmerDef\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | APN | SOS  说明：  需要与1中**ADD APN**命令的参数“APN名称”取值保持一致。 |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | EmerDef\_Policy  说明：  已在策略中定义。 |

### | 业务3 | 基本信息 | 名称 | EPSFB\_Dedicate\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | AF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 否  说明：  若业务激活方式为AF，但用户没有订购该业务，则需要将业务的参数“签约后才能使用”设置为“否”。 |

### |  | 策略 | 名称 | EPSFB\_Dedicate\_Policy  说明：  已在策略中定义。 |

### 8 配置应用业务映射。

### 导航入口为“业务管理 > 业务 > 应用业务映射”。

### 配置AF激活的EPS Fallback业务时，必须配置应用业务映射。其中，“应用标识”必须和AF侧协商一致；“业务”为7中已定义的EPS Fallback呼叫业务。

### 应用业务映射的数据规划如表7所示，详细参数说明请参见应用业务映射参数表。

### **表7** 应用业务映射

### | 类别 | 参数 | 取值样例 |

### | --- | --- | --- |

### | 应用业务映射 | 应用标识 | EPSFB\_Dedicate\_App  说明：  和AF中定义的应用标识协商一致。 |

### |  | 业务 | EPSFB\_Dedicate\_Service  说明：  已在业务中定义的由AF激活的业务（EPS Fallback呼叫业务）。 |

### 9 配置用户组。

### 导航入口为“用户管理 > 用户 > 用户组”。

### 需要配置如下2个动态用户组：

### SG\_IMS\_Def：匹配条件为APN=ims，关联7中已定义的业务“IMSDef\_Service”。

### Emergency\_Sub\_Group：匹配条件为APN=SOS，关联7中已定义的业务“EmerDef\_Service”。

### 动态用户组的数据规划如表8所示，详细参数说明请参见动态用户组参数表。

### **表8** 动态用户组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 用户组1 | 基本信息 | 名称 | SG\_IMS\_Def |

### |  |  | 类型 | 动态 |

### |  |  | 优先级 | 1 |

### |  |  | APN | ims  说明：  需要与1中**ADD APN**命令的参数“APN名称”取值保持一致。 |

### |  |  | 应用类型 | 缺省方式  说明：  表示该动态用户组订购的业务是专门用于IMS基本呼叫。 |

### |  | 业务 | 名称 | IMSDef\_Service  说明：  已在业务中定义。 |

### | 用户组2 | 基本信息 | 名称 | Emergency\_Sub\_Group |

### |  |  | 类型 | 动态 |

### |  |  | 优先级 | 0 |

### |  |  | APN | SOS  说明：  需要与1中**ADD APN**命令的参数“APN名称”取值保持一致。 |

### |  |  | 应用类型 | 紧急呼叫  说明：  表示该动态用户组订购的业务是专门用于紧急呼叫。 |

### |  | 业务 | 名称 | EmerDef\_Service  说明：  已在业务中定义。 |

