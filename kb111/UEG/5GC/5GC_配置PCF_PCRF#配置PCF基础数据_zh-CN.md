---
id: ''
name: 配置PCF基础数据
ne_type: UEG
type: feature
description: 开局时，配置PCF基础数据。  PCF/PCRF从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：  * FE（Front End）网元也称为PCF/PCRF网元，实现PCF/PCRF功能实体的功能，包括协议处理、业务处理以及数据管理。 * BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。    PCF/PCRF部署在园区网络时，用户数据的增加、删除和更新通过业务发放系统或在PGW本地（在PGW Web LMT上执行MML批操作文件）进行业务发放。在一个UDR（USCDB）上进行开户，该UDR（USCDB）会将用户数据自动备份到另一个UDR（USCDB）。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置PCF/PCRF","配置PCF基础数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置PCF/PCRF","配置PCF基础数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置PCF/PCRF","配置PCF基础数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置PCF基础数据。PCF/PCRF从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：* FE（Front End）网元也称为PCF/PCRF网元，实现PCF/PCRF功能实体的功能，包括协议处理、业务处理以及数据管理。* BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。  PCF/PCRF部署在园区网络时，用户数据的增加、删除和更新通过业务发放系统或在PGW本地（在PGW Web LMT上执行MML批操作文件）进行业务发放。在一个UDR（USCDB）上进行开户，该UDR（USCDB）会将用户数据自动备份到另一个UDR（USCDB）。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_fesn_list:
      type: items
      properties:
        SN:
          name: 'FE序号'
          type: integer
          minimum:
          - 0
          - 255
          maximum:
          - 20
          - 255
          required: true
          description: '容灾的2个FE的SN必须相同。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_pcrf_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DN:
          name: '本地域名'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '由运营商提供。'
          data_source: '整网规划'
          pattern: ''
          default: ''
        HN:
          name: '本地主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '由运营商提供。'
          data_source: '整网规划'
          pattern: ''
          default: ''
    set_dbslocation_list:
      type: items
      properties:
        LOCID:
          name: 'Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '如已完成园区UDM配置，则不需要规划该数据。   * 双DC场景，两个PCF的Location标识必须不同。如DC1用13，DC2用15。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CNFM:
          name: '是否确认修改'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '取值为YES时，不管当前是否已设置“Location标识”，此次都会强制设置成功。'
          data_source: '本端规划'
          pattern: ''
          default: NO
    add_dbsserviceno_list:
      type: items
      properties:
        SERVICENO:
          name: '服务模块号'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '如已完成园区UDM配置，则不需要规划该数据。   1. 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。 2. 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PODNAME:
          name: 'POD名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '-'
          data_source: '通过OM Portal获取'
          pattern: ''
          default: ''
    add_dbsserviceno_list_2:
      type: items
      properties:
        SERVICENO:
          name: '服务模块号'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '如已完成园区UDM配置，则不需要规划该数据。   1. 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。 2. 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PODNAME:
          name: 'POD名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '-'
          data_source: '通过OM Portal获取'
          pattern: ''
          default: ''
    add_dbsipaddr_list:
      type: items
      properties:
        DBSIPINDEX:
          name: 'Dbbroker IP索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '网元内存在多条记录时，该参数不能重复。同时部署园区UDM时，该参数必须与UDM的参数值不同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '与USCDB互通的业务IP地址及VPN实例。  VPN名称采用**ADD L3VPNINST**定义的VPN实例名称。  双DC场景，两个DC的业务IP地址不能重复，如DC1用样例值，DC2用10.201.200.22等。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IP1VPNNAME:
          name: 'IP地址1的VPN名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '本地Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '本地Location IPV4子网掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IP2VPNNAME:
          name: 'IP地址2的VPN名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '本地Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '本地Location IPV4子网掩码2'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_hlbdevaddr_list:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '本端服务化接口IP，用于和SMF/AMF互通。   * 双DC场景，两个DC的服务化接口IP地址不能重复，如DC1用样例值，DC2用10.201.200.47等。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IP:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPSFUNC:
          name: 'HTTPS功能'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '* AMF、SMF与PCF均由同一个UEG设备实现，可不开启HTTPS。 * HTTP端口号默认为8080，HTTPS端口号默认为443。'
          data_source: '与对端协商'
          pattern: ''
          default: ON
    add_dlbvpn_list:
      type: items
      properties:
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_dlbdevaddr_list:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '本端Diameter IP，用于和PCEF互通。   * 双DC场景，两个DC的Diameter IP地址不能重复，如DC1用样例值，DC2用10.201.200.87等。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IP:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pmsvpn_list:
      type: items
      properties:
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: 'VPN名称采用**ADD L3VPNINST**定义的VPN实例名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_pmsdevaddr_list:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '本端IP，用于登录PMS Portal，即配置策略数据。   * 双DC场景，两个DC的服务化接口IP地址不能重复，如DC1用样例值，DC2用10.201.200.47等。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IP:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_dlbvpn_list_2:
      type: items
      properties:
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'VPN名称采用**ADD L3VPNINST**定义的VPN实例名称。  如网设规划为VRF\_PS\_Signal，则请将VRF\_SBI替换成VRF\_PS\_Signal。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_dlbdevaddr_list_2:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '本端Diameter IP，用于和AF互通。   * 双DC场景，两个DC的Diameter IP地址不能重复，如DC1用样例值，DC2用172.21.100.102等。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IP:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_sdrtrans_list:
      type: items
      properties:
        FLATTYPE:
          name: '通信平面类型'
          type: string
          enum:
          - BASE
          - FABRIC
          required: true
          description: '指定对应的网络平面，此处固定配置为FABRIC。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TRANSABILITY:
          name: '传输能力类型'
          type: string
          enum:
          - RELIABILITY
          - SECURITY
          required: true
          description: '标识SDR传输能力类型，此处固定配置为RELIABILITY。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OPT:
          name: '选项开关'
          type: string
          enum:
          - DISABLEALL
          - ENABLEALL
          - NOTSET
          required: true
          description: '标识SDR传输能力的选项开关，此处固定配置为DISABLEALL。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    mod_pcfinsp_list:
      type: items
      properties:
        INSPN:
          name: '软参名'
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
          description: '当新建局点时，需要手动将该软参取值修改为“1”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        INSPV:
          name: '软参值'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_fesn_list:
    - SN: 0
    add_pcrf_list:
    - PCRFID: 1
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcrf01.ucn.3gppnetwork.org'
    - PCRFID: 1
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcrf02.ucn.3gppnetwork.org'
    set_dbslocation_list:
    - LOCID: 13
      CNFM: YES
    - LOCID: 15
      CNFM: YES
    add_dbsserviceno_list:
    - SERVICENO: 301
      PODNAME: 'dbb-all-pod13-0'
    add_dbsserviceno_list_2:
    - SERVICENO: 301
      PODNAME: 'dbb-all-pod13-0'
    add_dbsipaddr_list:
    - DBSIPINDEX: 1
      IPVER: IPV4
      IP1VPNNAME: 'VRF_DATA'
      IPV4IP1: '10.200.200.22'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_DATA'
      IPV4IP2: '10.200.200.23'
      IPV4MASK2: '255.255.255.255'
    - DBSIPINDEX: 1
      IPVER: IPV4
      IP1VPNNAME: 'VRF_DATA'
      IPV4IP1: '10.201.200.22'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_DATA'
      IPV4IP2: '10.201.200.23'
      IPV4MASK2: '255.255.255.255'
    add_hlbdevaddr_list:
    - DEVAID: 2
      VPNNAME: 'VRF_SBI'
      IPVER: IPV4
      IP: '10.200.200.47'
      HTTPSFUNC: OFF
    - DEVAID: 2
      VPNNAME: 'VRF_SBI'
      IPVER: IPV4
      IP: '10.201.200.47'
      HTTPSFUNC: OFF
    add_dlbvpn_list:
    - VPNINDEX: 6
      VPNNAME: '_public_'
    - VPNINDEX: 6
      VPNNAME: '_public_'
    add_dlbdevaddr_list:
    - DEVAID: 6
      VPNINDEX: 6
      IPVER: IPV4
      IP: '10.200.200.87'
    - DEVAID: 6
      VPNINDEX: 6
      IPVER: IPV4
      IP: '10.201.200.87'
    add_pmsvpn_list:
    - VPNINDEX: 3
      VPNNAME: 'VRF_OM'
    - VPNINDEX: 3
      VPNNAME: 'VRF_OM'
    add_pmsdevaddr_list:
    - DEVAID: 3
      VPNINDEX: 3
      IPVER: IPV4
      IP: '10.200.200.99'
    - DEVAID: 3
      VPNINDEX: 3
      IPVER: IPV4
      IP: '10.201.200.99'
    add_dlbvpn_list_2:
    - VPNINDEX: 4
      VPNNAME: 'VRF_AF'
    - VPNINDEX: 4
      VPNNAME: 'VRF_AF'
    add_dlbdevaddr_list_2:
    - DEVAID: 4
      VPNINDEX: 4
      IPVER: IPV4
      IP: '10.200.200.67'
    - DEVAID: 4
      VPNINDEX: 4
      IPVER: IPV4
      IP: '10.201.200.67'
    set_sdrtrans_list:
    - FLATTYPE: FABRIC
      TRANSABILITY: RELIABILITY
      OPT: DISABLEALL
    mod_pcfinsp_list:
    - INSPN: VRM_N15COMPATIBILITYSWITCH
      INSPV: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 设置FE序号。

```jinja2
{%- for item in set_fesn_list -%}
    SET FESN:
    {#- --- 必选参数 --- -#}
    SN={{item.SN}},
    ;
{%- endfor -%}
```

### 3 增加PCRF实体。

#### 3.1 //DC1：

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    PCRFID={{item.PCRFID}},
    DN="{{item.DN}}",
    HN="{{item.HN}}",
    ;
{%- endfor -%}
```

### 执行本命令后，需要在CSP界面执行**RST POD**命令，重启HLB、DLB、PES和DUS服务。具体重启操作请参考**ADD PCRF**联机帮助。

### 刀片式服务器2U不需要部署DUS服务，故不需要重启DUS服务。

### 执行完重启命令后，可以通过**DSP POD**查询服务是否已经恢复。

### 4 配置dbbroker信息，用于微服务和USCDB对接。如采用中心UDM或园区UDM未完成基础数据配置，请执行本步骤；否则请跳转到5。

#### 4.1 检查Location标识是否与规划一致。

#### 执行**LST LOCATION**命令和**LST DBSLOCATION**命令，检查“Location标识”参数值是否相等，且与规划一致。

#### 主用局PCF/PCRF、主用局USCDB、容灾局PCF/PCRF、容灾局USCDB的Location标识各不相同。

#### 一致，请执行4.c。

#### * **LST DBSLOCATION**命令查询结果为空，请执行4.b。

#### 其他查询结果，请联系华为技术支持工程师处理。

#### 4.2 设置DBS Location标识。

##### 4.2.1 //DC1：

```jinja2
{%- for item in set_dbslocation_list -%}
    SET DBSLOCATION:
    {#- --- 必选参数 --- -#}
    LOCID={{item.LOCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.CNFM is not none -%}
        CNFM={{item.CNFM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 设置本端服务ID。

#### 参数“PODNAME”，通过以下操作获取：

##### 4.3.1 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。

##### 4.3.2 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。

##### 4.3.3 **虚机容器**：

```jinja2
{%- if is_scenario_vm_container -%}
    {%- for item in add_dbsserviceno_list -%}
        ADD DBSSERVICENO:
        {#- --- 必选参数 --- -#}
        SERVICENO={{item.SERVICENO}},
        PODNAME="{{item.PODNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.4 **裸机容器**：

```jinja2
{%- if is_scenario_baremetal_container -%}
    {%- for item in add_dbsserviceno_list_2 -%}
        ADD DBSSERVICENO:
        {#- --- 必选参数 --- -#}
        SERVICENO={{item.SERVICENO}},
        PODNAME="{{item.PODNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置网元IP，用于FE与对端BE进行对接。

##### 4.4.1 //DC1：

```jinja2
{%- for item in add_dbsipaddr_list -%}
    ADD DBSIPADDR:
    {#- --- 必选参数 --- -#}
    DBSIPINDEX={{item.DBSIPINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4/IPV6 时必选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        IP1VPNNAME="{{item.IP1VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4MASK1 is not none -%}
            IPV4MASK1="{{item.IPV4MASK1}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4/IPV6 时可选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        {%- if item.IP2VPNNAME is not none -%}
            IP2VPNNAME="{{item.IP2VPNNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置HTTP IP，用于和AMF/SMF/PGW-C通信。

#### 5.1 //DC1：

```jinja2
{%- for item in add_hlbdevaddr_list -%}
    ADD HLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNNAME="{{item.VPNNAME}}",
    IPVER={{item.IPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPSFUNC is not none -%}
        HTTPSFUNC={{item.HTTPSFUNC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置Diameter信令IP，用于和PCEF通信。部署PTT业务时需要配置，其他场景请跳过本步骤。

#### 6.1 //DC1：

```jinja2
{%- for item in add_dlbvpn_list -%}
    ADD DLBVPN:
    {#- --- 必选参数 --- -#}
    VPNINDEX={{item.VPNINDEX}},
    VPNNAME="{{item.VPNNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dlbdevaddr_list -%}
    ADD DLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNINDEX={{item.VPNINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置PMS IP，用于配置策略数据。

#### 7.1 //DC1：

```jinja2
{%- for item in add_pmsvpn_list -%}
    ADD PMSVPN:
    {#- --- 必选参数 --- -#}
    VPNINDEX={{item.VPNINDEX}},
    VPNNAME="{{item.VPNNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pmsdevaddr_list -%}
    ADD PMSDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNINDEX={{item.VPNINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 完成PMS IP配置后，需要安装PMS证书，请参考配置PMS数字证书进行操作。完成操作后，需要进一步参考UPCF WebUI进行浏览器和安全配置。至此，PMS相关配置均已完成，待按顺序完成PCF与USCDB对接数据后，PMS Web UI（UPCF Web UI）功能可以正常使用。

### 8 配置Diameter信令IP，用于和AF（基于Diameter协议）通信。

#### 8.1 //DC1：

```jinja2
{%- for item in add_dlbvpn_list_2 -%}
    ADD DLBVPN:
    {#- --- 必选参数 --- -#}
    VPNINDEX={{item.VPNINDEX}},
    VPNNAME="{{item.VPNNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dlbdevaddr_list_2 -%}
    ADD DLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNINDEX={{item.VPNINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 设置SDR的可靠性传输功能。

```jinja2
{%- for item in set_sdrtrans_list -%}
    SET SDRTRANS:
    {#- --- 必选参数 --- -#}
    FLATTYPE={{item.FLATTYPE}},
    TRANSABILITY={{item.TRANSABILITY}},
    OPT={{item.OPT}},
    ;
{%- endfor -%}
```

### 10 开启N15接口兼容开关和修改业务token数量。

```jinja2
{%- for item in mod_pcfinsp_list -%}
    MOD PCFINSP:
    {#- --- 必选参数 --- -#}
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    ;
{%- endfor -%}
```

