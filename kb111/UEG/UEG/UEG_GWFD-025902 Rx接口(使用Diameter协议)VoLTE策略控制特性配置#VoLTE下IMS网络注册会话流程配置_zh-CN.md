---
id: GWFD-025902
name: VoLTE下IMS网络注册会话流程配置
ne_type: UEG
type: feature
description: IMS网络注册是VoLTE用户使用IMS网络提供业务的前提，UPCF支持用户在IMS网络的注册会话流程。 IMS网络注册会话流程仅用于VoLTE组网下的AF（即P-CSCF）容灾场景，当VoLTE用户发起IMS网络的注册会话时，AF通过Rx接口向UPCF发起AAR消息。UPCF根据AF上报的媒体流信息（包含AF地址）、本地配置的业务策略和用户签约信息进行策略判断，将生成的规则和AF地址通过RAR消息下发给PCEF。PCEF获知用户选择的AF地址，当该AF故障时，PCEF将通知用户向其他AF重新发起IMS网络注册请求。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF语音基本功能","GWFD-025902 Rx接口(使用Diameter协议)VoLTE策略控制","GWFD-025902 Rx接口(使用Diameter协议)VoLTE策略控制特性配置","VoLTE下IMS网络注册会话流程配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IMS网络注册是VoLTE用户使用IMS网络提供业务的前提，UPCF支持用户在IMS网络的注册会话流程。IMS网络注册会话流程仅用于VoLTE组网下的AF（即P-CSCF）容灾场景，当VoLTE用户发起IMS网络的注册会话时，AF通过Rx接口向UPCF发起AAR消息。UPCF根据AF上报的媒体流信息（包含AF地址）、本地配置的业务策略和用户签约信息进行策略判断，将生成的规则和AF地址通过RAR消息下发给PCEF。PCEF获知用户选择的AF地址，当该AF故障时，PCEF将通知用户向其他AF重新发起IMS网络注册请求。

## 必备事项
前提条件

* 操作员已了解GWFD-025902 Rx接口(使用Diameter协议)VoLTE策略控制特性概述。
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
  examples:
    mod_pcfinsp_list:
    - INSPN: UPM_SUBCTRL
      INSPV: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置Rx特性的相关软参。

#### 1.1 在OM Portal界面选择“应用管理 > MML”，进入Web MML配置界面。

#### 1.2 选择UEG网元执行**MOD PCFINSP**命令，设置参数“UPM\_SUBCTRL”为“1”，即宽松签约模式。

```jinja2
{%- for item in mod_pcfinsp_list -%}
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

### 需要配置一个用于判断媒体部件编号的条件组。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组 | 基本信息 | 名称 | CG\_Default\_Signalling |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Signalling\_Condition\_Default |

### |  |  | 对象属性 | * 对象：ApplicationSession * 属性：MediaComponentNumber |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | 0 |

### 4 配置动作组。

### 导航入口为“策略管理 > 策略 > 动作组”。

### 此场景需配置动作：ChargingAction，相关应用场景如下：

### ChargingAction：当需要做计费策略控制时，配置此动作（若对端为华为GGSN或者华为PDN-GW，此动作必须配置）。其中属性“RatingGroup”的取值需与在线/离线计费系统（如OCS）协商一致。

### 动作组的数据规划如表3所示，详细参数说明请参见动作组参数表。

### **表3** 动作组

### | 类别 | 参数 |  |  | 取值样例 |

### | --- | --- | --- | --- | --- |

### | 动作组 | 基本信息 | 名称 |  | AG\_Default\_Signalling |

### |  | 动作 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | Offline | * 值类型：Value * 值：EnableOffline |

### |  |  |  | Online | * 值类型：Value * 值：DisableOnline |

### |  |  |  | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：5 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

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

### | 规则 | 基本信息 | 名称 | Default\_Signalling\_Rule |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Default\_Signalling  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG\_Default\_Signalling |

### 7 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 请增加Default\_Signalling\_Policy策略：用户IMS网络注册，UPCF接收到VoLTE应用会话请求时触发的策略，触发器为AFSessionAuthorization。

### 策略的数据规划如表6所示，详细参数说明请参见策略参数表。

### **表6** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Default\_Signalling\_Policy |

### |  |  | 策略类型 | Gx Policy |

### |  | 触发器 | 名称 | AFSessionAuthorization |

### |  | 规则 | 名称 | Default\_Signalling\_Rule  说明：  已在规则中定义。 |

### 8 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 请增加Default\_Signalling\_Service业务：由AF激活的IMS用户注册业务，用于VoLTE容灾场景下，用户注册流程时透传AF侧的地址给PCEF。因为此业务不需要用户签约，故参数“签约后才能使用”必须配置为“否”。

### 业务的数据规划如表7所示，详细参数说明请参见业务参数表。

### **表7** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Default\_Signalling\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | AF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 否  说明：  若业务激活方式为AF，但用户没有订购该业务，则需要将业务的参数“签约后才能使用”设置为“否”。 |

### |  | 策略 | 名称 | Default\_Signalling\_Policy  说明：  已在策略中定义。 |

### 9 配置应用业务映射。

### 导航入口为“业务管理 > 业务 > 应用业务映射”。

### 配置AF激活的IMS用户注册业务时，必须配置应用业务映射。其中，“应用标识”必须和AF侧协商一致；“业务”为8中已定义的VoLTE业务。

### 应用业务映射的数据规划如表8所示，详细参数说明请参见应用业务映射参数表。

### **表8** 应用业务映射

### | 类别 | 参数 | 取值样例 |

### | --- | --- | --- |

### | 应用业务映射 | 应用标识 | IMS\_Signalling  说明：  和AF中定义的应用标识协商一致。 |

### |  | 业务 | Default\_Signalling\_Service  说明：  已在业务中定义的由AF激活的业务（IMS用户注册业务）。 |

### **脚本**

### CLI脚本

