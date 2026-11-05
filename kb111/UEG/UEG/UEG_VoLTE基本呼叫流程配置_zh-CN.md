---
id: ''
name: VoLTE基本呼叫流程配置
ne_type: UEG
type: feature
description: Rx接口是UPCF与AF（Application Function）之间的接口，部署VoLTE（Voice over LTE）应用，包括基本呼叫（语音/视频呼叫）和紧急呼叫等业务。UPCF支持部署该特性，为基本呼叫业务提供保障的带宽，确保用户享用优质语音和高清视频。例如，当IMS用户发起VoLTE基本呼叫时，AF（即IMS域的P-CSCF）通过Rx接口向UPCF发起资源预留请求，将会话相关的属性，如应用标识、媒体类型、媒体流状态、媒体流描述等上报给UPCF，UPCF根据AF上报的信息和本地配置的业务策略进行策略判断，将生成的QoS规则下发给PCEF（Policy and Charging Enforcement Function），由PCEF执行策略控制。  此场景中，数据应用和VoLTE基本会话采用独立的APN（Access Point Name）。当用户使用VoLTE基本呼叫业务时，针对不同业务类型（如语音、视频）给用户下发不同的带宽，并实行不同的计费策略。VoLTE基本呼叫业务的详细配置信息，请参见随VoLTE解决方案发布的《VoLTE产品文档》。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","PCRF&PCF配置","Rx接口（使用Diameter协议）VoLTE策略控制","VoLTE基本呼叫流程配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
Rx接口是UPCF与AF（Application Function）之间的接口，部署VoLTE（Voice over LTE）应用，包括基本呼叫（语音/视频呼叫）和紧急呼叫等业务。UPCF支持部署该特性，为基本呼叫业务提供保障的带宽，确保用户享用优质语音和高清视频。例如，当IMS用户发起VoLTE基本呼叫时，AF（即IMS域的P-CSCF）通过Rx接口向UPCF发起资源预留请求，将会话相关的属性，如应用标识、媒体类型、媒体流状态、媒体流描述等上报给UPCF，UPCF根据AF上报的信息和本地配置的业务策略进行策略判断，将生成的QoS规则下发给PCEF（Policy and Charging Enforcement Function），由PCEF执行策略控制。此场景中，数据应用和VoLTE基本会话采用独立的APN（Access Point Name）。当用户使用VoLTE基本呼叫业务时，针对不同业务类型（如语音、视频）给用户下发不同的带宽，并实行不同的计费策略。VoLTE基本呼叫业务的详细配置信息，请参见随VoLTE解决方案发布的《VoLTE产品文档》。

## 必备事项
前提条件

操作员已了解GWFD-025902 Rx接口(使用Diameter协议)VoLTE策略控制特性概述。
已完成配置UPCF与AF（基于Diameter协议）的对接数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    mod_pcfinsp_list_1:
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
  examples:
    add_apn_list:
    - PCRFID: 1
      APNID: 1
      APNNAME: 'ims'
      APNTYPE: VoLTE-APN
      APNMATCHTYPE: FullMatching
    mod_pcfinsp_list:
    - INSPN: VRM_RELGXBYRAATIMEOUT
      INSPV: 1
    mod_pcfinsp_list_1:
    - INSPN: UPM_SUBCTRL
      INSPV: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

#### 1.1 执行ADD APN命令，添加“VoLTE-APN”类型的APN。

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

#### 1.2 配置Rx特性的相关软参。

#### 执行**MOD PCFINSP**命令，设置参数“VRM\_RELGXBYRAATIMEOUT”为“1”，即Gx接口RAA消息超时时不释放APN为“IMS”的Gx承载会话。

```jinja2
{%- for item in mod_pcfinsp_list -%}
    MOD PCFINSP:
    {#- --- 必选参数 --- -#}
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

#### 1.3 执行**MOD PCFINSP**命令，设置参数“UPM\_SUBCTRL”为“1”，即宽松签约模式。

```jinja2
{%- for item in mod_pcfinsp_list_1 -%}
    MOD PCFINSP:
    {#- --- 必选参数 --- -#}
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

### 2 登录UPCF WebUI界面。

### 3 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置两个条件组，用于语音呼叫或视频呼叫不同的媒体类型。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Audio\_Normal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | IMS\_Condition\_Audio |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：MediaType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Audio  说明：  表示媒体类型为语音呼叫。 |

### | 条件组2 | 基本信息 | 名称 | CG\_Video\_Normal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | IMS\_Condition\_Video |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：MediaType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Video  说明：  表示媒体类型为视频呼叫。 |

### 4 配置动作组。

### 导航入口为“策略管理 > 策略 > 动作组”。

### 此场景需配置动作：DefaultBearerQoS、QoSAction、ChargingAction和GateAction，相关应用场景如下：

### DefaultBearerQoS：当需要建立默认承载时必须配置此动作。

### QoSAction：当需要进行带宽控制时均需配置此动作，若不配置则表示不限制Qos。

### ChargingAction：当需要做计费策略控制时，配置此动作（若对端为华为GGSN或者华为PDN-GW，此动作必须配置）。其中属性“RatingGroup”的取值需与在线/离线计费系统（如OCS）协商一致。

### GateAction：当需要做门限控制时，配置此动作。在下发流描述时，如果不配GateAction，默认为放通该流，当需要限制流时，此动作必须配置。此场景根据AF请求的Flow-Status，下发门限策略。

### 请增加如下动作组和动作：

### 动作组AG1\_Data\_APN：动作DefaultBearerQoS

### 动作组AG2\_Data\_APN：动作QoSAction和ChargingAction

### 动作组AG1\_IMS\_APN：动作DefaultBearerQoS

### 动作组AG2\_IMS\_APN：动作QoSAction和ChargingAction

### 动作组AG\_Audio\_Normal：动作QoSAction、GateAction和ChargingAction

### 动作组AG\_Video\_Normal：动作QoSAction、GateAction和ChargingAction

### 动作组的数据规划如表3所示，详细参数说明请参见动作组参数表。

### **表3** 动作组

### | 类别 | 参数 |  |  | 取值样例 |

### | --- | --- | --- | --- | --- |

### | 动作组1 | 基本信息 | 名称 |  | AG1\_Data\_APN |

### |  | 动作 | 动作 |  | DefaultBearerQoS |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 说明：  数据APN的默认承载，建议QCI配置为8。 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  |  |  | AMBRDL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | AMBRUL | * 值类型：Value * 值(kbit/s)：10000 |

### | 动作组2 | 基本信息 | 名称 |  | AG2\_Data\_APN |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 |

### |  |  |  | MBRUL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | MBRDL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  | 动作2 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | Offline | * 值类型：Value * 值：EnableOffline |

### |  |  |  | Online | * 值类型：Value * 值：DisableOnline |

### |  |  |  | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：1 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### | 动作组3 | 基本信息 | 名称 |  | AG1\_IMS\_APN |

### |  | 动作 | 动作 |  | DefaultBearerQoS |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：5 说明：  IMS APN的默认承载，建议QCI配置为5。 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  |  |  | AMBRDL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | AMBRUL | * 值类型：Value * 值(kbit/s)：10000 |

### | 动作组4 | 基本信息 | 名称 |  | AG2\_IMS\_APN |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：5 说明：  QCI配置与默认承载一致。 |

### |  |  |  | MBRUL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | MBRDL | * 值类型：Value * 值(kbit/s)：10000 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  | 动作2 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | Offline | * 值类型：Value * 值：EnableOffline |

### |  |  |  | Online | * 值类型：Value * 值：DisableOnline |

### |  |  |  | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：1 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### | 动作组5 | 基本信息 | 名称 |  | AG\_Audio\_Normal |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：1 说明：  语音呼叫时，建议QCI取值为1。 |

### |  |  |  | MBRUL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthUL 说明：  带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | MBRDL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthDL 说明：  带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | GBRUL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthUL 说明：  配置保障带宽，且带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | GBRDL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthDL 说明：  配置保障带宽，且带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：2 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  | 动作2 | 动作 |  | GateAction |

### |  |  | 动作元素 | FlowStatus | * 值类型：Object Attribute * 对象属性：ApplicationSession.FlowStatus 说明：  FlowStatus取值与AF侧请求的FlowStatus一致。 |

### |  | 动作3 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | Offline | * 值类型：Value * 值：EnableOffline |

### |  |  |  | Online | * 值类型：Value * 值：DisableOnline |

### |  |  |  | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：7 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### |  |  |  | ChargingCorrelationIndicator | * 值类型：Value * 值：Charging Identifier Required 说明：  表示PCEF需上报计费信息，UPCF将计费信息转发给AF。 |

### | 动作组6 | 基本信息 | 名称 |  | AG\_Video\_Normal |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：2 说明：  视频呼叫时，建议QCI取值为2。 |

### |  |  |  | MBRUL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthUL 说明：  带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | MBRDL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthDL 说明：  带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | GBRUL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthUL 说明：  配置保障带宽，且带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | GBRDL | * 值类型：Object Attribute * 对象属性：ApplicationSession.MaxRequestBandwidthDL 说明：  配置保障带宽，且带宽取值与AF侧请求的带宽一致。 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：2 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  | 动作2 | 动作 |  | GateAction |

### |  |  | 动作元素 | FlowStatus | * 值类型：Object Attribute * 值：ApplicationSession.FlowStatus 说明：  FlowStatus取值与AF侧请求的FlowStatus一致。 |

### |  | 动作3 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | Offline | * 值类型：Value * 值：EnableOffline |

### |  |  |  | Online | * 值类型：Value * 值：DisableOnline |

### |  |  |  | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：8 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### |  |  |  | ChargingCorrelationIndicator | * 值类型：Value * 值：Charging Identifier Required 说明：  表示PCEF需上报计费信息，UPCF将计费信息转发给AF。 |

### 5 配置业务流。

### 导航入口为“策略管理 > 策略 > 业务流”。

### 当对端为华为PDN-GW时，所有的动态规则都必须配置业务流。

### 若Rx请求消息携带流信息，则会以Rx请求携带的流为准。

### 业务流的数据规划如表4所示，详细参数说明请参见业务流参数表。

### **表4** 业务流

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务流 | 基本信息 | 名称 | Flow\_Filter |

### |  | 流过滤器1 | 名称 | up\_pass |

### |  |  | 流方向 | Up |

### |  |  | 协议 | Any IP Protocol |

### |  | 流过滤器2 | 名称 | down\_pass |

### |  |  | 流方向 | Down |

### |  |  | 协议 | Any IP Protocol |

### 6 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 除配置的动作DefaultBearerQoS，必须在规则“类型”为“Default Bearer QoS”时才有效外，其他情况AF业务下的规则“类型”建议都配置为“Dynamic”。

### 在多PCEF场景下，若业务中的“激活方式”为“AF”，则业务下的规则都必须配置“目的PEER”。

### 规则的数据规划如表5所示，详细参数说明请参见规则参数表。

### **表5** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Data\_APN\_Rule1 |

### |  |  | 类型 | Default Bearer QoS  说明：  默认承载QoS场景，规则类型必须为“Default Bearer QoS”。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | -  说明：  任何条件下，都下发此规则。 |

### |  | 动作组 | 动作组 | AG1\_Data\_APN  说明：  已在动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Data\_APN\_Rule2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时， “关系”可设置为任意值。 |

### |  |  | 条件组 | -  说明：  任何条件下，都下发此规则。 |

### |  | 动作组 | 动作组 | AG2\_Data\_APN  说明：  已在动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | IMS\_APN\_Rule1 |

### |  |  | 类型 | Default Bearer QoS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | -  说明：  任何条件下，都下发此规则。 |

### |  | 动作组 | 动作组 | AG1\_IMS\_APN  说明：  已在动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | IMS\_APN\_Rule2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | -  说明：  任何条件下，都下发此规则。 |

### |  | 动作组 | 动作组 | AG2\_IMS\_APN  说明：  已在动作组中定义。 |

### | 规则5 | 基本信息 | 名称 | IMS\_Audio\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Audio\_Normal  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG\_Audio\_Normal  说明：  已在动作组中定义。 |

### | 规则6 | 基本信息 | 名称 | IMS\_Video\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Video\_Normal  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG\_Video\_Normal  说明：  已在动作组中定义。 |

### | 规则7 | 基本信息 | 名称 | Dynamic\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  |  | 优先级 | 20  说明：  优先级需要设置为最低。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | -  说明：  任何条件下，都下发此规则。 |

### |  | 动作组 | 动作组 | AG2\_IMS\_APN  说明：  已在动作组中定义。 |

### 7 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 请增加如下策略：

### Data\_APN\_Policy：用户从数据APN上线时触发的策略，触发器为IPCANSessionEstablish。

### IMS\_APN\_Policy：用户从IMS APN上线时触发的策略，触发器为IPCANSessionEstablish。

### IMS\_VOLTE\_Policy：UPCF接收到VoLTE应用会话请求时触发的策略，触发器为AFSessionAuthorization。

### 策略的数据规划如表6所示，详细参数说明请参见策略参数表。

### **表6** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略1 | 基本信息 | 名称 | Data\_APN\_Policy |

### |  |  | 策略类型 | Gx Policy |

### |  | 触发器 | 名称 | IPCANSessionEstablish |

### |  | 规则 | 名称 | * Data\_APN\_Rule1 * Data\_APN\_Rule2 说明：  已在规则中定义。 |

### | 策略2 | 基本信息 | 名称 | IMS\_APN\_Policy |

### |  |  | 策略类型 | Gx Policy |

### |  | 触发器 | 名称 | IPCANSessionEstablish |

### |  | 规则 | 名称 | * IMS\_APN\_Rule1 * IMS\_APN\_Rule2 说明：  已在规则中定义。 |

### | 策略3 | 基本信息 | 名称 | IMS\_VOLTE\_Policy |

### |  |  | 策略类型 | Gx Policy |

### |  | 触发器 | 名称 | AFSessionAuthorization |

### |  | 规则 | 名称 | * IMS\_Audio\_Rule * IMS\_Video\_Rule * Dynamic\_Rule 说明：  已在规则中定义。 |

### 8 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 请增加如下业务：

### Data\_APN\_Service：由PCEF激活的业务，用于创建数据APN的默认承载。此业务被动态用户组签约，故参数“签约后才能使用”必须配置为“是”。

### IMS\_APN\_Service：由PCEF激活的业务，用于创建VoLTE基本呼叫APN的默认承载。此业务被动态用户组签约，故参数“签约后才能使用”必须配置为“是”，该业务必须配置“APN”。

### IMS\_VOLTE\_Service：由AF激活的VoLTE应用业务，如语音、视频等。因为此业务不需要用户签约，故参数“签约后才能使用”必须配置为“否”。

### 如果“业务”中“APN”参数未配置， VOLTE业务商用后，又在LMT客户端上配置了**ADD APN**，则会导致业务受损。

### 业务的数据规划如表6 所示，详细参数说明请参见业务参数表。

### **表7** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务1 | 基本信息 | 名称 | Data\_APN\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Data\_APN\_Policy  说明：  已在策略中定义。 |

### | 业务2 | 基本信息 | 名称 | IMS\_APN\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | APN | IMS |

### |  |  | APN匹配类型 | 全匹配 |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | IMS\_APN\_Policy  说明：  已在策略中定义。 |

### | 业务3 | 基本信息 | 名称 | IMS\_VOLTE\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | AF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 否  说明：  若业务激活方式为AF，但用户没有订购该业务，则需要将业务的参数“签约后才能使用”设置为“否”。 |

### |  | 策略 | 名称 | IMS\_VOLTE\_Policy  说明：  已在策略中定义。 |

### 9 配置应用业务映射。

### 导航入口为“业务管理 > 业务 > 应用业务映射”。

### 配置AF激活的VoLTE基本呼叫业务时，必须配置应用业务映射。其中，“应用标识”必须和AF侧协商一致；“业务”为8中已定义的VoLTE业务。

### 应用业务映射的数据规划如表8所示，详细参数说明请参见应用业务映射参数表。

### **表8** 应用业务映射

### | 类别 | 参数 | 取值样例 |

### | --- | --- | --- |

### | 应用业务映射 | 应用标识 | VOLTE\_audio\_video  说明：  和AF中定义的应用标识协商一致。 |

### |  | 业务 | IMS\_VOLTE\_Service  说明：  已在业务中定义的由AF激活的业务（IMS VOLTE业务）。 |

### 10 配置用户组。

### 导航入口为“用户管理 > 用户 > 用户组”。

### 请增加如下两个动态用户组：

### Data\_APN\_Sub\_Group：匹配条件为APN=Data\_APN，关联8中已定义的业务Data\_APN\_Service。

### IMS\_APN\_Sub\_Group：匹配条件为APN=IMS，关联8中已定义的业务IMS\_APN\_Service。

### 动态用户组的数据规划如表9所示，详细参数说明请参见用户组参数表。

### **表9** 动态用户组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 用户组1 | 基本信息 | 名称 | Data\_APN\_Sub\_Group |

### |  |  | 类型 | 动态 |

### |  |  | 优先级 | 10 |

### |  |  | APN | Data\_APN |

### |  |  | 应用类型 | 缺省方式 |

### |  | 业务 | 名称 | Data\_APN\_Service  说明：  已在业务中定义。 |

### | 用户组2 | 基本信息 | 名称 | IMS\_APN\_Sub\_Group |

### |  |  | 类型 | 动态 |

### |  |  | 优先级 | 11 |

### |  |  | APN | IMS |

### |  |  | 应用类型 | 缺省方式 |

### |  | 业务 | 名称 | IMS\_APN\_Service  说明：  已在业务中定义。 |

### **脚本**

### CLI脚本

