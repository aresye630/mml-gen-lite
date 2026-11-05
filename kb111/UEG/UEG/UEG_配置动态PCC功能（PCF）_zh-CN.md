---
id: ''
name: 配置动态PCC功能（PCF）
ne_type: UEG
type: feature
description: 园区UEG部署PCF/PCRF实体功能时，涉及到语音专载业务或LTE一键通功能，支持动态PCC。  动态PCC分为动态规则和预定义规则：  * 动态规则：PCRF/PCF下发该规则对应的业务流特征及业务的精细化管理动作。SMF仅需要开启动态PCC开关，UPF不需要特殊配置。PCF可以随时删除旧规则，安装新规则。 * 预定义规则：UPF/SMF/PCF上需定义相同的规则标识，UPF上定义该规则对应的业务流特征及业务的精细化管理动作。用户注册过程中，由PCF下发规则标识，PCF通过规则标识的方式激活SMF/UPF本地静态配置的规则来实现计费和策略的控制。PCF可以随时删除旧规则，安装新规则。  本页面以PTT业务使用的动态规则为例。一号通专网场景下，请参考Rx接口（使用Diameter协议）VoLTE策略控制、Rx接口（使用Diameter协议）VoNR策略控制、Rx接口（使用Diameter协议）EPS Fallback策略控制选择对应场景的章节进行PCF上的语音策略配置，本页面仅提供PCF上动态PCC规则配置的使用样例，一号通场景无需配置PTT业务，本页面仅供学习参考使用。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","PCC规则配置","配置动态PCC","配置动态PCC功能（PCF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
园区UEG部署PCF/PCRF实体功能时，涉及到语音专载业务或LTE一键通功能，支持动态PCC。动态PCC分为动态规则和预定义规则：* 动态规则：PCRF/PCF下发该规则对应的业务流特征及业务的精细化管理动作。SMF仅需要开启动态PCC开关，UPF不需要特殊配置。PCF可以随时删除旧规则，安装新规则。* 预定义规则：UPF/SMF/PCF上需定义相同的规则标识，UPF上定义该规则对应的业务流特征及业务的精细化管理动作。用户注册过程中，由PCF下发规则标识，PCF通过规则标识的方式激活SMF/UPF本地静态配置的规则来实现计费和策略的控制。PCF可以随时删除旧规则，安装新规则。本页面以PTT业务使用的动态规则为例。一号通专网场景下，请参考Rx接口（使用Diameter协议）VoLTE策略控制、Rx接口（使用Diameter协议）VoNR策略控制、Rx接口（使用Diameter协议）EPS Fallback策略控制选择对应场景的章节进行PCF上的语音策略配置，本页面仅提供PCF上动态PCC规则配置的使用样例，一号通场景无需配置PTT业务，本页面仅供学习参考使用。

## 必备事项
前提条件

* 请仔细阅读特性概述。
* 完成加载License（开站后通过OM Portal可一键开启所有License项，IOPS场景无需手动开启）。
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
    add_actiongroup_list:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_chargingaction_list:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OFFLINETYPE:
          name: '离线计费参数值类型'
          type: string
          required: false
          description: '使用Gx接口时，必须配置计费动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OFFLINEVALUE:
          name: 'Offline'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINETYPE:
          name: '在线计费参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINEVALUE:
          name: 'Online'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPTYPE:
          name: '费率组参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPVALUE:
          name: 'RatingGroup'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELTYPE:
          name: '计费报告级别参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELVALUE:
          name: 'ReportingLevel'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERTYPE:
          name: '业务标识参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERVALUE:
          name: 'ServiceIdentifier'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODTYPE:
          name: '计量方式参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODVALUE:
          name: 'MeteringMethod'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_qosaction_list:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPERATION:
          name: '操作类型'
          type: string
          required: false
          description: '“TYPE”取值为“Default Bearer QoS”时不需要规划该参数；“TYPE”取值为“Dynamic”需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: '使用量取舍'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '规则关联的条件组之间的关系。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEFLOWNAME:
          name: '业务流'
          type: string
          required: false
          description: '索引**ADD SERVICEFLOW**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        REINSTALL:
          name: '支持重复下发'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ruleactiongroup_list:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policy_list:
      type: items
      properties:
        POLICYNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '策略类型'
          type: string
          required: false
          description: '与PGW-C/SMF交互时，策略类型支持Gx Policy和N7 Policy。  PTT业务时，须采用“Gx Policy”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policyrule_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policytrigger_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list:
      type: items
      properties:
        SERVICENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICETYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: '激活方式'
          type: string
          required: false
          description: '用户通过Gx、N7接口发起的会话建立或更新时（如服务区改变、固网用户共享使用量）使用的业务激活方式。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越大，优先级越高。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QoS模式'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: '签约后才能使用'
          type: string
          required: false
          description: '仅当“激活方式”为“AF”时该参数配置才有效。  此处以用户不需要签约也可以使用这个业务为例。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROBILLDATE:
          name: '结帐日失效'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: '配额分配方式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: '是否设置共享模式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: '是否组业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: '是否是模板业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: '自动记录位置'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          required: false
          description: 'PCRF会将用户上线时携带的APN或DNN与用户签约业务中配置的APN进行全匹配，如果完全一致，则全匹配成功。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: '是否有基础业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: '是否计算动态实例有效期'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: '自定义重置类型'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        MASTER2MASTERSHARESERVICE:
          name: 'M2M共享业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
    add_servicepolicy_list:
      type: items
      properties:
        SERVICENAME:
          name: '业务名称'
          type: string
          required: false
          description: '索引**ADD SERVICE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_actiongroup_list_1:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_defaultbearerqos_list:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力开关参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDLVALUE:
          name: 'AMBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRULVALUE:
          name: 'AMBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_chargingaction_list_1:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OFFLINETYPE:
          name: '离线计费参数值类型'
          type: string
          required: false
          description: '使用Gx接口时，必须配置计费动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OFFLINEVALUE:
          name: 'Offline'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINETYPE:
          name: '在线计费参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINEVALUE:
          name: 'Online'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPTYPE:
          name: '费率组参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPVALUE:
          name: 'RatingGroup'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELTYPE:
          name: '计费报告级别参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELVALUE:
          name: 'ReportingLevel'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERTYPE:
          name: '业务标识参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERVALUE:
          name: 'ServiceIdentifier'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODTYPE:
          name: '计量方式参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODVALUE:
          name: 'MeteringMethod'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_qosaction_list_1:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_serviceflow_list:
      type: items
      properties:
        SERVICEFLOWNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        SERVICEFLOWNAME:
          name: '业务流名称'
          type: string
          required: false
          description: '索引**ADD SERVICEFLOW**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERDIRECTION:
          name: '流方向'
          type: string
          required: false
          description: 'Up：上行流。  Down：下行流。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTINATIONIPADDRESSMODE:
          name: '目的IP地址获取方式'
          type: string
          required: false
          description: '* Assigned Value：获取的值为业务流中配置的目的IP地址。 * UEIP：获取的值为用户上线时携带的目的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESTINATIONIPADDRESS:
          name: '目的IP地址'
          type: string
          required: false
          description: '业务流的目的IP地址及掩码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKOFDESTINATIONIPADDRESS:
          name: '目的IP地址掩码/前缀长度'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINDESTINATIONPORT1:
          name: '最小目的端口1'
          type: string
          required: false
          description: '端口为0时，表示不限制端口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXDESTINATIONPORT1:
          name: '最大目的端口1'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINDESTINATIONPORT2:
          name: '最小目的端口2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXDESTINATIONPORT2:
          name: '最大目的端口2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SOURCEIPADDRESSMODE:
          name: '源IP地址获取方式'
          type: string
          required: false
          description: '* Assigned Value：获取的值为业务流中配置的源IP地址。 * UEIP：获取的值为用户上线时携带的源IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SOURCEIPADDRESS:
          name: '源IP地址'
          type: string
          required: false
          description: '业务流的源IP地址及掩码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKOFSOURCEIPADDRESS:
          name: '源IP地址掩码/前缀长度'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINSOURCEPORT1:
          name: '最小源端口1'
          type: string
          required: false
          description: '端口为0时，表示不限制端口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXSOURCEPORT1:
          name: '最大源端口1'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINSOURCEPORT2:
          name: '最小源端口2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXSOURCEPORT2:
          name: '最大源端口2'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: '使用量取舍'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '规则关联的条件组之间的关系。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATION:
          name: '操作类型'
          type: string
          required: false
          description: '“TYPE”取值为“Default Bearer QoS”时不需要规划该参数；“TYPE”取值为“Dynamic”需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICEFLOWNAME:
          name: '业务流'
          type: string
          required: false
          description: '索引**ADD SERVICEFLOW**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        REINSTALL:
          name: '支持重复下发'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ruleactiongroup_list_1:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policy_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '策略类型'
          type: string
          required: false
          description: '与PGW-C/SMF交互时，策略类型支持Gx Policy和N7 Policy。  PTT业务时，须采用“Gx Policy”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policyrule_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policytrigger_list_1:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list_1:
      type: items
      properties:
        SERVICENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICETYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: '激活方式'
          type: string
          required: false
          description: '用户通过Gx、N7接口发起的会话建立或更新时（如服务区改变、固网用户共享使用量）使用的业务激活方式。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越大，优先级越高。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QoS模式'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: '签约后才能使用'
          type: string
          required: false
          description: '仅当“激活方式”为“AF”时该参数配置才有效。  此处以用户不需要签约也可以使用这个业务为例。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROBILLDATE:
          name: '结帐日失效'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: '配额分配方式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: '是否设置共享模式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: '是否组业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: '是否是模板业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: '自动记录位置'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          required: false
          description: 'PCRF会将用户上线时携带的APN或DNN与用户签约业务中配置的APN进行全匹配，如果完全一致，则全匹配成功。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: '是否有基础业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: '是否计算动态实例有效期'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: '自定义重置类型'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        MASTER2MASTERSHARESERVICE:
          name: 'M2M共享业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
    add_servicepolicy_list_1:
      type: items
      properties:
        SERVICENAME:
          name: '业务名称'
          type: string
          required: false
          description: '索引**ADD SERVICE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_rule_list_3:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越小优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: '使用量取舍'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '规则关联的条件组之间的关系。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        REINSTALL:
          name: '支持重复下发'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATION:
          name: '操作类型'
          type: string
          required: false
          description: '“TYPE”取值为“Default Bearer QoS”时不需要规划该参数；“TYPE”取值为“Dynamic”需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICEFLOWNAME:
          name: '业务流'
          type: string
          required: false
          description: '索引**ADD SERVICEFLOW**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_conditiongroup_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '同一个条件组下，多个条件之间的关系。AND表示需要同时满足，OR表示满足其一即可。  条件组下只有一个条件时，AND和OR效果相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。  C\_Reservation\_*x*：*x*取值范围0-15，此处仅给出0和1为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: '对象属性'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATOR:
          name: '操作符'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: '右值类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: '右值'
          type: string
          required: false
          description: '根据需要判断的条件进行设置。  C\_Reservation\_*x*：*x*取值1时，右值为One；*x*取值2时，右值为Two；以此类推。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_actiongroup_list_3:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_defaultbearerqos_list_1:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力开关参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDLVALUE:
          name: 'AMBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRULVALUE:
          name: 'AMBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_qosaction_list_2:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gateaction_list:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWSTATUSTYPE:
          name: '门控状态参数值类型'
          type: string
          required: false
          description: '设置门控状态。  取值范围：Enable Uplink、Enable Downlink、Enabled、Disabled，分别对应：允许上行，允许下行，允许，阻塞。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWSTATUSVALUE:
          name: 'FlowStatus'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_chargingaction_list_2:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OFFLINETYPE:
          name: '离线计费参数值类型'
          type: string
          required: false
          description: '使用Gx接口时，必须配置计费动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OFFLINEVALUE:
          name: 'Offline'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINETYPE:
          name: '在线计费参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ONLINEVALUE:
          name: 'Online'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODTYPE:
          name: '计量方式参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        METERINGMETHODVALUE:
          name: 'MeteringMethod'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPTYPE:
          name: '费率组参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATINGGROUPVALUE:
          name: 'RatingGroup'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELTYPE:
          name: '计费报告级别参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPORTINGLEVELVALUE:
          name: 'ReportingLevel'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERTYPE:
          name: '业务标识参数值类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SERVICEIDENTIFIERVALUE:
          name: 'ServiceIdentifier'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_conditiongroup_list_1:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '同一个条件组下，多个条件之间的关系。AND表示需要同时满足，OR表示满足其一即可。  条件组下只有一个条件时，AND和OR效果相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list_1:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。  C\_Reservation\_*x*：*x*取值范围0-15，此处仅给出0和1为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: '对象属性'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATOR:
          name: '操作符'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: '右值类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: '右值'
          type: string
          required: false
          description: '根据需要判断的条件进行设置。  C\_Reservation\_*x*：*x*取值1时，右值为One；*x*取值2时，右值为Two；以此类推。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_actiongroup_list_5:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_defaultbearerqos_list_2:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力开关参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDLVALUE:
          name: 'AMBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRULVALUE:
          name: 'AMBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_qosaction_list_3:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gateaction_list_1:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWSTATUSTYPE:
          name: '门控状态参数值类型'
          type: string
          required: false
          description: '设置门控状态。  取值范围：Enable Uplink、Enable Downlink、Enabled、Disabled，分别对应：允许上行，允许下行，允许，阻塞。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWSTATUSVALUE:
          name: 'FlowStatus'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_actiongroup_list_7:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosaction_list_4:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gateaction_list_2:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWSTATUSTYPE:
          name: '门控状态参数值类型'
          type: string
          required: false
          description: '设置门控状态。  取值范围：Enable Uplink、Enable Downlink、Enabled、Disabled，分别对应：允许上行，允许下行，允许，阻塞。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWSTATUSVALUE:
          name: 'FlowStatus'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_conditiongroup_list_2:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '同一个条件组下，多个条件之间的关系。AND表示需要同时满足，OR表示满足其一即可。  条件组下只有一个条件时，AND和OR效果相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list_2:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。  C\_Reservation\_*x*：*x*取值范围0-15，此处仅给出0和1为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: '对象属性'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATOR:
          name: '操作符'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: '右值类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: '右值'
          type: string
          required: false
          description: '根据需要判断的条件进行设置。  C\_Reservation\_*x*：*x*取值1时，右值为One；*x*取值2时，右值为Two；以此类推。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_conditiongroup_list_3:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '同一个条件组下，多个条件之间的关系。AND表示需要同时满足，OR表示满足其一即可。  条件组下只有一个条件时，AND和OR效果相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list_3:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。  C\_Reservation\_*x*：*x*取值范围0-15，此处仅给出0和1为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: '对象属性'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATOR:
          name: '操作符'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: '右值类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: '右值'
          type: string
          required: false
          description: '根据需要判断的条件进行设置。  C\_Reservation\_*x*：*x*取值1时，右值为One；*x*取值2时，右值为Two；以此类推。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_actiongroup_list_8:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosaction_list_5:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gateaction_list_3:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWSTATUSTYPE:
          name: '门控状态参数值类型'
          type: string
          required: false
          description: '设置门控状态。  取值范围：Enable Uplink、Enable Downlink、Enabled、Disabled，分别对应：允许上行，允许下行，允许，阻塞。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWSTATUSVALUE:
          name: 'FlowStatus'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_conditiongroup_list_4:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELATION:
          name: '关系'
          type: string
          required: false
          description: '同一个条件组下，多个条件之间的关系。AND表示需要同时满足，OR表示满足其一即可。  条件组下只有一个条件时，AND和OR效果相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USETIMEZONE:
          name: 'USETIMEZONE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list_19:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。  C\_Reservation\_*x*：*x*取值范围0-15，此处仅给出0和1为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: '对象属性'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPERATOR:
          name: '操作符'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: '右值类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: '右值'
          type: string
          required: false
          description: '根据需要判断的条件进行设置。  C\_Reservation\_*x*：*x*取值1时，右值为One；*x*取值2时，右值为Two；以此类推。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_actiongroup_list_9:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosaction_list_6:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYTYPE:
          name: 'ARP抢占能力参数值类型'
          type: string
          required: false
          description: '设置ARP抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAPABILITYVALUE:
          name: 'PreemptionCapability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYTYPE:
          name: 'ARP被抢占开关参数值类型'
          type: string
          required: false
          description: '设置ARP被抢占能力开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVULNERABILITYVALUE:
          name: 'PreemptionVulnerability'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPLEVELTYPE:
          name: 'ARP抢占优先级参数值类型'
          type: string
          required: false
          description: '设置ARP抢占优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPLEVELVALUE:
          name: 'ARPLevel'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRULTYPE:
          name: '承诺上行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRULVALUE:
          name: 'GBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GBRDLTYPE:
          name: '承诺下行带宽参数值类型'
          type: string
          required: false
          description: '设置GBR下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDLVALUE:
          name: 'GBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRDLTYPE:
          name: '最大下行带宽参数值类型'
          type: string
          required: false
          description: '设置最大下行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDLVALUE:
          name: 'MBRDL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MBRULTYPE:
          name: '最大上行带宽参数值类型'
          type: string
          required: false
          description: '设置最大上行带宽。单位：Kbit/s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRULVALUE:
          name: 'MBRUL'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCITYPE:
          name: 'QoS等级标识参数值类型'
          type: string
          required: false
          description: '设置QoS等级标识（QCI）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCIVALUE:
          name: 'QCI'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gateaction_list_4:
      type: items
      properties:
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        FLOWSTATUSTYPE:
          name: '门控状态参数值类型'
          type: string
          required: false
          description: '设置门控状态。  取值范围：Enable Uplink、Enable Downlink、Enabled、Disabled，分别对应：允许上行，允许下行，允许，阻塞。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWSTATUSVALUE:
          name: 'FlowStatus'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ruleconditiongroup_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleactiongroup_list_3:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleconditiongroup_list_2:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleactiongroup_list_5:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleconditiongroup_list_4:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleactiongroup_list_8:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleconditiongroup_list_6:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: '条件组名称'
          type: string
          required: false
          description: '索引**ADD CONDITIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_ruleactiongroup_list_9:
      type: items
      properties:
        RULENAME:
          name: '名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ACTIONGROUPNAME:
          name: '动作组名称'
          type: string
          required: false
          description: '索引**ADD ACTIONGROUP**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policy_list_2:
      type: items
      properties:
        POLICYNAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '策略类型'
          type: string
          required: false
          description: '与PGW-C/SMF交互时，策略类型支持Gx Policy和N7 Policy。  PTT业务时，须采用“Gx Policy”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_policyrule_list_3:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '索引**ADD RULE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_policytrigger_list_2:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '名称'
          type: string
          required: false
          description: '存在多条时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICETYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: '激活方式'
          type: string
          required: false
          description: '用户通过Gx、N7接口发起的会话建立或更新时（如服务区改变、固网用户共享使用量）使用的业务激活方式。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRECEDENCE:
          name: '优先级'
          type: string
          required: false
          description: '数字越大，优先级越高。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QoS模式'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: '签约后才能使用'
          type: string
          required: false
          description: '仅当“激活方式”为“AF”时该参数配置才有效。  此处以用户不需要签约也可以使用这个业务为例。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROBILLDATE:
          name: '结帐日失效'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: '配额分配方式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: '是否设置共享模式'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: '是否组业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: '是否是模板业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: '自动记录位置'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APN匹配类型'
          type: string
          required: false
          description: 'PCRF会将用户上线时携带的APN或DNN与用户签约业务中配置的APN进行全匹配，如果完全一致，则全匹配成功。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: '是否有基础业务'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: '是否计算动态实例有效期'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: '自定义重置类型'
          type: string
          required: false
          description: '-'
          data_source: '默认值'
          pattern: ''
          default: ''
    add_servicepolicy_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '业务名称'
          type: string
          required: false
          description: '索引**ADD SERVICE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略'
          type: string
          required: false
          description: '索引**ADD POLICY**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_applicationservicemapping_list:
      type: items
      properties:
        APPID:
          name: '应用标识'
          type: string
          required: false
          description: '必须与对接的AF上定义的应用标识一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '业务'
          type: string
          required: false
          description: '索引**ADD SERVICE**定义的名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        SERVICECLASS:
          name: '业务等级'
          type: string
          required: false
          description: '必须与对接的AF上定义的业务等级一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
  examples:
    mod_pcfinsp_list:
    - INSPN: VRM_MAXBEARNUMPERIPCAN
      INSPV: 10
    add_actiongroup_list:
    - ACTIONGROUPNAME: 34211_0101_AG03
    add_chargingaction_list:
    - ACTIONGROUPNAME: 34211_0101_AG03
      OFFLINETYPE: Value
      OFFLINEVALUE: EnableOffline
      ONLINETYPE: Value
      ONLINEVALUE: DisableOnline
      RATINGGROUPTYPE: Value
      RATINGGROUPVALUE: '77'
      REPORTINGLEVELTYPE: Value
      REPORTINGLEVELVALUE: Service Identifier Level
      SERVICEIDENTIFIERTYPE: Value
      SERVICEIDENTIFIERVALUE: '77'
      METERINGMETHODTYPE: Value
      METERINGMETHODVALUE: Volume
    add_qosaction_list:
    - ACTIONGROUPNAME: 34211_0101_AG03
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Enabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      ARPLEVELTYPE: Value
      ARPLEVELVALUE: '3'
      GBRULTYPE: Object Attribute
      GBRULVALUE: IPSession.BearerRequestedGBRUL
      GBRDLTYPE: Object Attribute
      GBRDLVALUE: IPSession.BearerRequestedGBRDL
      MBRDLTYPE: Object Attribute
      MBRDLVALUE: IPSession.BearerRequestedMBRDL
      MBRULTYPE: Object Attribute
      MBRULVALUE: IPSession.BearerRequestedMBRUL
      QCITYPE: Object Attribute
      QCIVALUE: IPSession.BearerRequestedQCI
    add_rule_list:
    - RULENAME: 34211_0101_R03
      OPERATION: Change Rule
      TYPE: Dynamic
      PRECEDENCE: '2'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
      SERVICEFLOWNAME: 34211_0101_SF01
      REINSTALL: No
    add_ruleactiongroup_list:
    - RULENAME: 34211_0101_R03
      ACTIONGROUPNAME: 34211_0101_AG03
    add_policy_list:
    - POLICYNAME: 34211_0101_P02
      TYPE: Gx Policy
    add_policyrule_list:
    - POLICYNAME: 34211_0101_P02
      RULENAME: 34211_0101_R03
    add_policytrigger_list:
    - POLICYNAME: 34211_0101_P02
      TRIGGERNAME: ResourceModificationRequest
    add_service_list:
    - SERVICENAME: 34211_0101_S02
      SERVICETYPE: BASIC_SERVICE
      ACTIVATEDBY: UE_INITIATED_RESOURCE
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list:
    - SERVICENAME: 34211_0101_S02
      POLICYNAME: 34211_0101_P02
    add_actiongroup_list_1:
    - ACTIONGROUPNAME: 34211_0101_AG01
    add_defaultbearerqos_list:
    - ACTIONGROUPNAME: 34211_0101_AG01
      QCITYPE: Value
      QCIVALUE: '5'
      ARPLEVELTYPE: Value
      ARPLEVELVALUE: '1'
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Enabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      AMBRDLTYPE: Value
      AMBRDLVALUE: '10240'
      AMBRULTYPE: Value
      AMBRULVALUE: '10240'
    add_chargingaction_list_1:
    - ACTIONGROUPNAME: 34211_0101_AG02
      OFFLINETYPE: Value
      OFFLINEVALUE: EnableOffline
      ONLINETYPE: Value
      ONLINEVALUE: DisableOnline
      RATINGGROUPTYPE: Value
      RATINGGROUPVALUE: '99'
      REPORTINGLEVELTYPE: Value
      REPORTINGLEVELVALUE: Service Identifier Level
      SERVICEIDENTIFIERTYPE: Value
      SERVICEIDENTIFIERVALUE: '99'
      METERINGMETHODTYPE: Value
      METERINGMETHODVALUE: Volume
    add_qosaction_list_1:
    - ACTIONGROUPNAME: 34211_0101_AG02
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Enabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      ARPLEVELTYPE: Value
      ARPLEVELVALUE: '1'
      GBRULTYPE: Value
      GBRULVALUE: '10000'
      GBRDLTYPE: Value
      GBRDLVALUE: '10000'
      MBRDLTYPE: Value
      MBRDLVALUE: '10000'
      MBRULTYPE: Value
      MBRULVALUE: '10000'
      QCITYPE: Value
      QCIVALUE: '5'
    add_serviceflow_list:
    - SERVICEFLOWNAME: 34211_0101_SF01
    add_flowfilter_list:
    - SERVICEFLOWNAME: 34211_0101_SF01
      FLOWFILTERNAME: 34211_0101_FF01
      FILTERDIRECTION: Up
      DESTINATIONIPADDRESSMODE: Assigned Value
      DESTINATIONIPADDRESS: '0'
      MASKOFDESTINATIONIPADDRESS: 0.0.0.0
      MINDESTINATIONPORT1: '0'
      MAXDESTINATIONPORT1: '0'
      MINDESTINATIONPORT2: '0'
      MAXDESTINATIONPORT2: '0'
      SOURCEIPADDRESSMODE: Assigned Value
      SOURCEIPADDRESS: '0'
      MASKOFSOURCEIPADDRESS: 0.0.0.0
      MINSOURCEPORT1: '0'
      MAXSOURCEPORT1: '0'
      MINSOURCEPORT2: '0'
      MAXSOURCEPORT2: '0'
      PROTOCOL: Any IP Protocol
    add_rule_list_1:
    - RULENAME: 34211_0101_R01
      TYPE: Default Bearer QoS
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
      OPERATION: Install Rule
      SERVICEFLOWNAME: 34211_0101_SF01
      REINSTALL: No
    add_ruleactiongroup_list_1:
    - RULENAME: 34211_0101_R01
      ACTIONGROUPNAME: 34211_0101_AG01
    add_policy_list_1:
    - POLICYNAME: 34211_0101_P01
      TYPE: Gx Policy
    add_policyrule_list_1:
    - POLICYNAME: 34211_0101_P01
      RULENAME: 34211_0101_R01
    add_policytrigger_list_1:
    - POLICYNAME: 34211_0101_P01
      TRIGGERNAME: IPCANSessionEstablish
    add_service_list_1:
    - SERVICENAME: 34211_0101_S01
      SERVICETYPE: BASIC_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list_1:
    - SERVICENAME: 34211_0101_S01
      POLICYNAME: 34211_0101_P01
    add_rule_list_3:
    - RULENAME: R_IMS
      TYPE: Default Bearer QoS
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
      REINSTALL: No
      OPERATION: Install Rule
      SERVICEFLOWNAME: 34211_0101_SF01
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: APN_For_Data
      RELATION: AND
      USETIMEZONE: No
    add_condition_list:
    - CONDITIONGROUPNAME: APN_For_Data
      CONDITIONNAME: APN_NOT_IMS
      OBJECTATTRIBUTE: IPSession.CalledStationID
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: elte.com
    add_actiongroup_list_3:
    - ACTIONGROUPNAME: AG_IMS_Default
    add_defaultbearerqos_list_1:
    - ACTIONGROUPNAME: AG_IMS_Default
      QCITYPE: Value
      QCIVALUE: '9'
      ARPLEVELTYPE: Object Attribute
      ARPLEVELVALUE: IPSession.ARPLevel
      PREEMPTIONCAPABILITYTYPE: Object Attribute
      PREEMPTIONCAPABILITYVALUE: IPSession.PreemptionCapability
      PREEMPTIONVULNERABILITYTYPE: Object Attribute
      PREEMPTIONVULNERABILITYVALUE: IPSession.PreemptionVulnerability
      AMBRDLTYPE: Object Attribute
      AMBRDLVALUE: ApplicationSession.MaxRequestBandwidthDL
      AMBRULTYPE: Object Attribute
      AMBRULVALUE: ApplicationSession.MaxRequestBandwidthUL
    add_qosaction_list_2:
    - ACTIONGROUPNAME: AG_IMS_Default_1
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Disabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      ARPLEVELTYPE: Object Attribute
      ARPLEVELVALUE: IPSession.ARPLevel
      GBRULTYPE: Object Attribute
      GBRULVALUE: IPSession.BearerRequestedGBRUL
      GBRDLTYPE: Object Attribute
      GBRDLVALUE: IPSession.BearerRequestedGBRDL
      MBRDLTYPE: Object Attribute
      MBRDLVALUE: IPSession.BearerRequestedMBRDL
      MBRULTYPE: Object Attribute
      MBRULVALUE: IPSession.BearerRequestedMBRUL
      QCITYPE: Value
      QCIVALUE: '9'
    add_gateaction_list:
    - ACTIONGROUPNAME: AG_IMS_Default_1
      FLOWSTATUSTYPE: Value
      FLOWSTATUSVALUE: Enabled
    add_chargingaction_list_2:
    - ACTIONGROUPNAME: AG_IMS_Default_1
      OFFLINETYPE: Value
      OFFLINEVALUE: EnableOffline
      ONLINETYPE: Value
      ONLINEVALUE: DisableOnline
      METERINGMETHODTYPE: Value
      METERINGMETHODVALUE: Volume
      RATINGGROUPTYPE: Value
      RATINGGROUPVALUE: '9'
      REPORTINGLEVELTYPE: Value
      REPORTINGLEVELVALUE: Rating Group Level
      SERVICEIDENTIFIERTYPE: Value
      SERVICEIDENTIFIERVALUE: '99'
    add_conditiongroup_list_1:
    - CONDITIONGROUPNAME: qci9_cg
      RELATION: AND
      USETIMEZONE: No
    add_condition_list_1:
    - CONDITIONGROUPNAME: qci9_cg
      CONDITIONNAME: qci9_cg
      OBJECTATTRIBUTE: IPSession.RATType
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: EUTRAN
    add_actiongroup_list_5:
    - ACTIONGROUPNAME: QCI9_ag
    add_defaultbearerqos_list_2:
    - ACTIONGROUPNAME: QCI9_ag_2
      QCITYPE: Value
      QCIVALUE: '9'
      ARPLEVELTYPE: Value
      ARPLEVELVALUE: '1'
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Disabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      AMBRDLTYPE: Value
      AMBRDLVALUE: '1000000'
      AMBRULTYPE: Value
      AMBRULVALUE: '1000000'
    add_qosaction_list_3:
    - ACTIONGROUPNAME: QCI9_ag
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Disabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      ARPLEVELTYPE: Value
      ARPLEVELVALUE: '1'
      GBRULTYPE: Value
      GBRULVALUE: '1000000'
      GBRDLTYPE: Value
      GBRDLVALUE: '1000000'
      MBRDLTYPE: Value
      MBRDLVALUE: '1000000'
      MBRULTYPE: Value
      MBRULVALUE: '1000000'
      QCITYPE: Value
      QCIVALUE: '9'
    add_gateaction_list_1:
    - ACTIONGROUPNAME: QCI9_ag
      FLOWSTATUSTYPE: Value
      FLOWSTATUSVALUE: Enabled
    add_actiongroup_list_7:
    - ACTIONGROUPNAME: Def_Dyn_AG
    add_qosaction_list_4:
    - ACTIONGROUPNAME: Def_Dyn_AG
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Disabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Enabled
      ARPLEVELTYPE: Object Attribute
      ARPLEVELVALUE: IPSession.ARPLevel
      GBRULTYPE: Object Attribute
      GBRULVALUE: IPSession.BearerRequestedMBRUL
      GBRDLTYPE: Object Attribute
      GBRDLVALUE: IPSession.BearerRequestedGBRDL
      MBRDLTYPE: Object Attribute
      MBRDLVALUE: IPSession.BearerRequestedMBRDL
      MBRULTYPE: Object Attribute
      MBRULVALUE: IPSession.BearerRequestedMBRUL
      QCITYPE: Object Attribute
      QCIVALUE: IPSession.BearerRequestedQCI
    add_gateaction_list_2:
    - ACTIONGROUPNAME: Def_Dyn_AG
      FLOWSTATUSTYPE: Value
      FLOWSTATUSVALUE: Enabled
    add_conditiongroup_list_2:
    - CONDITIONGROUPNAME: C_Volte_Audio
      RELATION: AND
      USETIMEZONE: No
    add_condition_list_2:
    - CONDITIONGROUPNAME: C_Volte_Audio
      CONDITIONNAME: C_Volte_Audio
      OBJECTATTRIBUTE: ApplicationSession.MediaType
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: Audio
    add_conditiongroup_list_3:
    - CONDITIONGROUPNAME: C_Reservation_0
      RELATION: OR
      USETIMEZONE: No
    add_condition_list_3:
    - CONDITIONGROUPNAME: C_Reservation_0
      CONDITIONNAME: C_Reservation_2
      OBJECTATTRIBUTE: ApplicationSession.ReservationPriority
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: Two
    add_actiongroup_list_8:
    - ACTIONGROUPNAME: AG_Volte_Audio
    add_qosaction_list_5:
    - ACTIONGROUPNAME: AG_Volte_Audio
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Enabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Disabled
      ARPLEVELTYPE: Object Attribute
      ARPLEVELVALUE: IPSession.ARPLevel
      GBRULTYPE: Object Attribute
      GBRULVALUE: ApplicationSession.MinRequestBandwidthUL
      GBRDLTYPE: Object Attribute
      GBRDLVALUE: ApplicationSession.MinRequestBandwidthDL
      MBRDLTYPE: Object Attribute
      MBRDLVALUE: ApplicationSession.MaxRequestBandwidthDL
      MBRULTYPE: Object Attribute
      MBRULVALUE: ApplicationSession.MaxRequestBandwidthUL
      QCITYPE: Value
      QCIVALUE: '65'
    add_gateaction_list_3:
    - ACTIONGROUPNAME: AG_Volte_Audio
      FLOWSTATUSTYPE: Value
      FLOWSTATUSVALUE: Enabled
    add_conditiongroup_list_4:
    - CONDITIONGROUPNAME: C_Volte_Video
      RELATION: AND
      USETIMEZONE: No
    add_condition_list_19:
    - CONDITIONGROUPNAME: C_Volte_Video
      CONDITIONNAME: C_Volte_Video
      OBJECTATTRIBUTE: ApplicationSession.MediaType
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: Video
    add_actiongroup_list_9:
    - ACTIONGROUPNAME: AG_Volte_Video
    add_qosaction_list_6:
    - ACTIONGROUPNAME: AG_Volte_Video
      PREEMPTIONCAPABILITYTYPE: Value
      PREEMPTIONCAPABILITYVALUE: Enabled
      PREEMPTIONVULNERABILITYTYPE: Value
      PREEMPTIONVULNERABILITYVALUE: Disabled
      ARPLEVELTYPE: Object Attribute
      ARPLEVELVALUE: IPSession.ARPLevel
      GBRULTYPE: Object Attribute
      GBRULVALUE: ApplicationSession.MinRequestBandwidthUL
      GBRDLTYPE: Object Attribute
      GBRDLVALUE: ApplicationSession.MinRequestBandwidthDL
      MBRDLTYPE: Object Attribute
      MBRDLVALUE: ApplicationSession.MaxRequestBandwidthDL
      MBRULTYPE: Object Attribute
      MBRULVALUE: ApplicationSession.MaxRequestBandwidthUL
      QCITYPE: Value
      QCIVALUE: '4'
    add_gateaction_list_4:
    - ACTIONGROUPNAME: AG_Volte_Video
      FLOWSTATUSTYPE: Value
      FLOWSTATUSVALUE: Enabled
    add_ruleconditiongroup_list:
    - RULENAME: R_IMS
      CONDITIONGROUPNAME: APN_For_Data
    add_ruleactiongroup_list_3:
    - RULENAME: R_IMS
      ACTIONGROUPNAME: AG_IMS_Default
    add_ruleconditiongroup_list_2:
    - RULENAME: qci9_rule
      CONDITIONGROUPNAME: qci9_cg
    add_ruleactiongroup_list_5:
    - RULENAME: ' qci9_rule'
      ACTIONGROUPNAME: QCI9_ag
    add_ruleconditiongroup_list_4:
    - RULENAME: R_Volte_Audio
      CONDITIONGROUPNAME: C_Volte_Audio
    add_ruleactiongroup_list_8:
    - RULENAME: R_Volte_Audio
      ACTIONGROUPNAME: AG_Volte_Audio
    add_ruleconditiongroup_list_6:
    - RULENAME: R_Volte_Video
      CONDITIONGROUPNAME: C_Volte_Video
    add_ruleactiongroup_list_9:
    - RULENAME: R_Volte_Video
      ACTIONGROUPNAME: AG_Volte_Video
    add_policy_list_2:
    - POLICYNAME: P_IMS
      TYPE: Gx Policy
    add_policyrule_list_3:
    - POLICYNAME: P_IMS
      RULENAME: R_IMS
    add_policytrigger_list_2:
    - POLICYNAME: P_IMS
      TRIGGERNAME: IPCANSessionEstablish
    add_service_list_2:
    - SERVICENAME: S_IMS_Signaling
      SERVICETYPE: VALUE_ADDED_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: No
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
    add_servicepolicy_list_2:
    - SERVICENAME: S_IMS_Signaling
      POLICYNAME: P_IMS
    add_applicationservicemapping_list:
    - APPID: eApp
      SERVICENAME: S_Volte
      SERVICECLASS: '1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置每个IP-CAN的最大承载数。

### 此处以每个IP-CAN的最大承载数设置成10为例。在“MML命令行-UEG”窗口下，执行如下脚本：

```jinja2
{%- for item in mod_pcfinsp_list -%}
    MOD PCFINSP:
    {#- --- 必选参数 --- -#}
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

### 2 配置全局策略。

#### 2.1 通过UPCF WEBUI配置时，请参考GWFD-025301 Gx接口(使用Diameter协议)策略控制特性配置。

#### 2.2 通过CLI命令配置时，请参考如下脚本。可参考登录UPCF WebUI界面与CLI导入导入CLI脚本。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chargingaction_list的变量区（command: ADD CHARGINGACTION） -#}
<!-- MISSING_MACRO: command=ADD CHARGINGACTION list_name=add_chargingaction_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_1的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_defaultbearerqos_list的变量区（command: ADD DEFAULTBEARERQOS） -#}
<!-- MISSING_MACRO: command=ADD DEFAULTBEARERQOS list_name=add_defaultbearerqos_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chargingaction_list_1的变量区（command: ADD CHARGINGACTION） -#}
<!-- MISSING_MACRO: command=ADD CHARGINGACTION list_name=add_chargingaction_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_1的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_serviceflow_list的变量区（command: ADD SERVICEFLOW） -#}
<!-- MISSING_MACRO: command=ADD SERVICEFLOW list_name=add_serviceflow_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_1的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list_1的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list_1的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list_1的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list_1的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list_1的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list_1 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list_1的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list_1 step_id=2.2 -->
```

### 3 配置PTT业务策略。

#### 3.1 通过UPCF WEBUI配置时，请参考GWFD-025301 Gx接口(使用Diameter协议)策略控制特性配置。

#### 3.2 通过CLI命令配置时，请参考如下脚本。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_3的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_3的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_defaultbearerqos_list_1的变量区（command: ADD DEFAULTBEARERQOS） -#}
<!-- MISSING_MACRO: command=ADD DEFAULTBEARERQOS list_name=add_defaultbearerqos_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_2的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_gateaction_list的变量区（command: ADD GATEACTION） -#}
<!-- MISSING_MACRO: command=ADD GATEACTION list_name=add_gateaction_list step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chargingaction_list_2的变量区（command: ADD CHARGINGACTION） -#}
<!-- MISSING_MACRO: command=ADD CHARGINGACTION list_name=add_chargingaction_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list_1的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_1的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_5的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_5 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_defaultbearerqos_list_2的变量区（command: ADD DEFAULTBEARERQOS） -#}
<!-- MISSING_MACRO: command=ADD DEFAULTBEARERQOS list_name=add_defaultbearerqos_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_3的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_gateaction_list_1的变量区（command: ADD GATEACTION） -#}
<!-- MISSING_MACRO: command=ADD GATEACTION list_name=add_gateaction_list_1 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_7的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_7 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_4的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_4 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_gateaction_list_2的变量区（command: ADD GATEACTION） -#}
<!-- MISSING_MACRO: command=ADD GATEACTION list_name=add_gateaction_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list_2的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_2的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list_3的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_3的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_8的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_8 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_5的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_5 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_gateaction_list_3的变量区（command: ADD GATEACTION） -#}
<!-- MISSING_MACRO: command=ADD GATEACTION list_name=add_gateaction_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list_4的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list_4 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list_19的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list_19 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_actiongroup_list_9的变量区（command: ADD ACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD ACTIONGROUP list_name=add_actiongroup_list_9 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_qosaction_list_6的变量区（command: ADD QOSACTION） -#}
<!-- MISSING_MACRO: command=ADD QOSACTION list_name=add_qosaction_list_6 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_gateaction_list_4的变量区（command: ADD GATEACTION） -#}
<!-- MISSING_MACRO: command=ADD GATEACTION list_name=add_gateaction_list_4 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list_3的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list_2的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list_5的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list_5 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list_4的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list_4 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list_8的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list_8 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list_6的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list_6 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleactiongroup_list_9的变量区（command: ADD RULEACTIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULEACTIONGROUP list_name=add_ruleactiongroup_list_9 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list_2的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list_3的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list_3 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list_2的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list_2的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list_2的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list_2 step_id=3.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_applicationservicemapping_list的变量区（command: ADD APPLICATIONSERVICEMAPPING） -#}
<!-- MISSING_MACRO: command=ADD APPLICATIONSERVICEMAPPING list_name=add_applicationservicemapping_list step_id=3.2 -->
```

