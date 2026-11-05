---
id: ''
name: 配置PGW与业务发放系统的对接数据
ne_type: UEG
type: feature
description: 用户数据的增加、删除和更新，可通过业务发放系统或PGW本地进行业务发放。  * 运营商规划通过业务发放系统对PGW中的用户数据进行管理操作的场景，请参考本页面进行配置。    同一个用户5秒内的配置数据需要通过同一个TCP链接发给相同的PGW模块处理。 * 运营商规划在PGW本地进行业务发放时，请根据配置USCDB基础数据中配置的PGW类型的IP登录PGW Web LMT进行操作。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置PGW与业务发放系统的对接数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置PGW与业务发放系统的对接数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置PGW与业务发放系统的对接数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置UDM/HSS","配置PGW与业务发放系统的对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户数据的增加、删除和更新，可通过业务发放系统或PGW本地进行业务发放。* 运营商规划通过业务发放系统对PGW中的用户数据进行管理操作的场景，请参考本页面进行配置。  同一个用户5秒内的配置数据需要通过同一个TCP链接发给相同的PGW模块处理。* 运营商规划在PGW本地进行业务发放时，请根据配置USCDB基础数据中配置的PGW类型的IP登录PGW Web LMT进行操作。

## 必备事项
前提条件

* UDM和业务发放系统均完成了软件安装和基础数据的配置。
* PGW与运营商的业务发放系统的物理连接正常。
* 已完成配置USCDB和USCDB对接数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_srvipaddr_list:
      type: items
      properties:
        SRVINDEX:
          name: '业务IP索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVIPTYPE:
          name: '业务IP类型'
          type: string
          enum:
          - DSG
          - PGW
          - DMA
          - PRV
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srvipaddr_list:
      type: items
      properties:
        SRVINDEX:
          name: '业务IP索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '用于指定业务IP地址对应的索引。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVIPTYPE:
          name: '业务IP类型'
          type: string
          enum:
          - DSG
          - PGW
          - DMA
          - PRV
          required: true
          description: 'PGW类型用于业务发放及访问PGW Web LMT。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DPUMID:
          name: 'DPU模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '业务IP地址。  双DC场景，两个DC的业务IP地址不能重复，如DC1用样例值，DC2用10.201.200.36等。  IP1用于连接业务发放系统，IP2用于连接PGW Web LMT。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IP1VPNNAME:
          name: 'IP地址1的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '用于指定“本地Location IPV4地址1”的VPN名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '本地Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '本地Location IPV4子网掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        IP2VPNNAME:
          name: 'IP地址2的VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '用于指定“本地Location IPV4地址2”的VPN名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '本地Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '本地Location IPV4子网掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
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
          - DBSRV
          - WDS
          - MULTIDRU
          - VERIFY
          - PGW
          - LDAP
          - STAT
          - FE
          - FUNCCFG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSPN:
          name: '软件参数名称'
          type: string
          enum:
          - MAXONECLIENTNUMS
          - FWDLOGINFOSWITCH
          - USCDBLOGFLAG
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
          - MSCLEARTIME
          - MSBUFREMAIN
          - SERVICEPORT
          - DRUIMDBS
          - DSUIMDBS
          - LDRSOURCE
          - TSYNCOPER
          - TQUERYOPER
          - TVERIFYOPER
          - TMULTINODEOPER
          - TREPRSPW
          - TVERIFYRSPW
          - TDSURSPW
          - TSYNCREPRSPW
          - TASYNCREPRSPW
          - TVERITYRSPW
          - FWDVFYSWT
          - REVVFYSWT
          - FWDRTVFYSWT
          - REVRTVFYSWT
          - TMFWDVFY
          - TMREVVFY
          - TMFWDRTVFY
          - TMREVRTVFY
          - PRDFWDVFY
          - PRDREVVFY
          - PRDFWDRTVFY
          - PRDREVRTVFY
          - GLOBALDATAREFRESHCYCLE
          - DRUFRWDVFYUNITNUM
          - DSUFRWDVFYUNITNUM
          - REVVFYUNITNUM
          - FWDRTVFYUNITNUM
          - REVRTVFYUNITNUM
          - HESRTBEATPERIOD
          - INNERHEARTBEATTIMEOUT
          - OUTERHEARTBEATTIMEOUT
          - CHECKPERIOD
          - THREADMONPERIOD
          - REPSPENDTIME
          - UPGRADESTATUS
          - TIMEBACKUPFLAG
          - BACKUPHOUR
          - BACKUPMINUTE
          - CBTABLESIZE
          - TIMEROFAllDRUWAIT
          - TIMEROFUSRVFY
          - TIMEROFEXCPTROUTEVFY
          - PERIODVFYONLYCHECK
          - REDUNDANCYSWITCH
          - NOCONSISTWARINGNUM
          - COUNTERLOGSWT
          - INTERREPSWITCH
          - LANGUAGE
          - PATCHSWITCH
          - SESWITCH
          - MAXWEBLMTNUMBER
          - MAXCLIENTNUMBER
          - PGWREJECTSWITCH
          - VERIFYCODEFLAG
          - BATSEQLEN
          - PGWRESERVE1
          - PGWBATSTEP
          - PGWDIRMONINTV
          - TLSMODE
          - SOAPVERSION
          - CONNWAITTIME
          - TRANSTIMEOUT
          - MAXCONNNUMPERIP
          - SOAPMAXRECVBUFFER
          - SOAPMAXSENDBUFFER
          - SESSIONTIMEOUT
          - HTTPSAUTHSWITCH
          - LDAPSWITCH
          - RLOADSWITCH
          - RLOADTIMEOUT
          - RLOADPACKETSIZE
          - RCHANNELLOADSW
          - REDUCFSWITCH
          - REDUTFSWITCH
          - REDURFSWITCH
          - REDUCFINTERVAL
          - REDURFINTERVAL
          - REDUALAINTERVAL
          - APPLICATIONTYPE
          - PGWOPLOGTYPE
          - PGWOPLOGCYC
          - USERDATAMEASUREFLAG
          - MEASUREHOUR
          - MEASUREMINUTE
          - STARTLICENSETIME
          - GRANTIPSWITCH
          - WEBLMTHTTPSSWITCH
          - PGWLOGMAXCOUNT
          - GDRUIMDBS
          - IUDMSWT
          - IUDMLSD
          - IUDMHOUR
          - IUDMMIN
          - WEBLMTTIMEOUT
          - USERTRANSSPEED
          - UIVFYSWT
          - PRDUIVFY
          - UIVFYUNITNUM
          - DMVFYSWT
          - PGWSNDDCIMSGMODE
          - LINGERTIME
          - NPSWITCH
          - MVNOSWITCH
          - PWDVERIFYSWITCH
          - CONBATMMLQUEUE
          - JRVFYPRD
          - JRVFYUNITNUM
          - REDUNAUTOTAKEOVER
          - TAKEOVERDELAY
          - LICINFODSPCTRL
          - DATANOTIFYMODE
          - DSNOTIFYTIMEOUT
          - DSNOTIFYRETRY
          - PRVBATRSTSAVEPATH
          - CMDDISCARDSWITCH
          - NOTIFYLINKSWAPSWITCH
          - VFYDATARECORDFLAG
          - NOTIFYHBTIMEWAIT
          - SESSIONIDALGSWITCH
          - RSPWITHOUTDESCSWITCH
          - SOAPENVSWITCH
          - MAXBATNUMBER
          - AUTORECOVERYFLAG
          - LENQUKVFYQUE
          - REDQUKVFYSPD
          - DYNUSERMEASURE
          - DYNMEASURESPEED
          - INNERQUKVFYSWT
          - LOCREPEVENT
          - LOGDISCARDCMDSWITCH
          - LOGORIGINALSOAPSWITCH
          - DRUINNERREPQUEUESIZE
          - DELSUBDATASWT
          - SCANSUBDATASPEED
          - SOAPPACKAGEMAXSIZE
          - STATBUFFRESULTSIZE
          - CLOUDADDSIDPOLICY
          - PROVRIGHTSWITCH
          - USERTRACEFLAG
          - PGWMMLSWITCH
          - WEBLMTFILERESTRICT
          - IMSRETINFOSWITCH
          - FORBIDCRCERR
          - PGWSERIALSWITCH
          - NOTIFYGETLOCATIONPOLICY
          - MAXCPUOVERLOADVALUE
          - SUPP_DOWNTIME_FUNC
          - DOWNTIME_THRESHOLD
          - LINKAGESWITCH
          - SERVICERIGHTSWITCH
          - EXTERNALACCESSSWITCH
          - VMSTORAGEFAULTRMSWITCH
          - MAXCMDNUMPERBAT
          - LOGTOOMU
          - EMIGRATIONPERIOD
          - SENDHBBYCLUSTER
          - NEEXPMMLANDPLA
          - LICDSPMODE
          - BYPASSDRUSWITCH
          - OUTERQUKVFYSWT
          - VFYCOVERRECORDSWT
          - PARALLELLOADNUM
          - SPLOCALEXC
          - BATSUSPENDSWITCH
          - SOCKETUNIQUE
          - FINDOPRFORHEADAUTH
          - PROVISIONBATRESULTFILESWITCH
          - AUTHWITHSRCIP
          - SPCFDIRRSTSWT
          - QUKVERIFYMODE
          - PGWLOGCOUNT
          - NOTIFYCONTROL
          - SENDHBMODE
          - SPCFOPLOGWRITEFILESWT
          - LDAPCONNTHDALMSWT
          - DRUOUTERREPQUEUESIZE
          - DSUINNERREPQUEUESIZE
          - DSUOUTERREPQUEUESIZE
          - SSHALGORITHMSWITCH
          - GDRUTHREADNUM
          - DRUTHREADNUM
          - DSUTHREADNUM
          - SAVLOGMAXCOUNT
          - PGWLOGORDER
          - ROUTEMIGMSGSIZE
          - LICCUSTOMIZEDSWITCH
          - EXPMSGQLENGTH
          - IMDBWORKMODE
          - OBJECTSERIALIZEFLAG
          - NUMBATPROCESSSWITCH
          - PGWSESSIONMAXNUM
          - PGWCONALMSWT
          - IMPORTSEQLEN
          - STATICMEASURESPEED
          - DSUUSRCNTUPDTHD
          - MCIRETURNIMMEDIATELY
          - AAMODESWITCH
          - TIMINGSUBSCRIPTIONUNITNUM
          - TIMINGSUBSCRIPTIONRESENDPERIOD
          - INCONSISTENTTHRESHOLD
          - EXPORTSPEED
          - SERVERLINGERTIME
          - GDATAEXPORTSPEED
          - RTMTNMODE
          - DELJUNKDATANUM
          - REMAINDATANUM
          - DRUDISPATCHMODE
          - DMAGLOBALREFRESHCYCLE
          - FLOWCTRLRSPSWITCH
          - MSGTIMEOUTTHRESHOLD
          - DRUREPRSPW
          - DRUSYNCREPRSPW
          - PCDRBTPWINSIZE
          - THIRDCFGCHECKSWITCH
          - RETENTION_BACKUP
          - RETENTION_LOG
          - RETENTION_EXPORT
          - Q922TASKDELAYTIME
          - CLUSTERBALANCESWITCH
          - PGWLOGTOREMOTE
          - MASTERLDRCOMPRESS
          - EMGRSTMODE
          - DELJUNKDATACYCLE
          - IGNOREPREFIXCHECK
          - BATWRITERESULTAPART
          - AUTOBATPARALLELNUM
          - BATCMDASYNCNOTIFY
          - EXCOMLQUERYSPEED
          - EXCOMLUPDATESPEED
          - CLOUDADAPTERSWITCH
          - NETWORKMODE
          - DCIFWDMODE
          - NOTIFYFLOWMSGCOUNT
          - LOCREPMULTHREADSWT
          - OBJECTCOMPRESSMODE
          - SOAPDECODESWITCH
          - SELFSPACEBACKUP
          - THIRDSPACEBACKUP
          - UPDOWNTASKNUM
          - TIMEOUTTHIRDBKLOAD
          - TIMEOUTSELFBKLOAD
          - DSULOADSHAREMODE
          - GROUTEVRFYSWT
          - BROADCASTQUERYSTEP
          - BROADCASTUPDATESTEP
          - SFTPUSERPWDVALID
          - BATCHROUTEUPDATEDELAYTIME
          - EXCEPTIONROUTEVERIFYSWITCH
          - BATCHREPLICATIONDELAYTIME
          - BATCHREPLICATIONMODE
          - TAKEOVERFORCLUSTER
          - EXPIRETIME
          - PROVBATCHDELORIFILE
          - MAPLOGTOVRP
          - FWDMMLERRCODESWT
          - PROVBATCHFOBTAINFILEMODE
          - WEBLMTSECURITYOPTIONSWITCH
          - USERTRANSBKPSWITCH
          - MAXTMOUTPROVFORWARD
          - COMMANDACCESSTYPECONTROL
          - NTFCFGOFREMOTEIDSWITCH
          - OPRPWDPBKDF2ALGSWITCH
          - SOAPERRORMSGTYPESWITCH
          - REDOARCHIVEDAYS
          - INCREDOSWITCH
          - DBPAGEVACUUMMODE
          - PSITEMSGSWITCH
          - DMAMODULECFGSWT
          - SSHKEXALGORITHMSWITCH
          - LOCATIONVERIFYMODE
          - BKPFILEVRFSWT
          - CERTALAINTERVAL
          - KVDCISYNCTOUDB
          - SFTPCLIENTSECURITYALGSW
          - RESTHTTPSAUTHSWITCH
          - BYPASSREVRTSYNSWITCH
          - LENQUKVFYQUEOFROUTE
          - HTTPPROVRIGHTSWITCH
          - PROVHTTPSAUTHSWITCH
          - USERTRANSRECOVERSPEED
          - COMFORMATOFEXPFILE
          - FILEUPLOADMODE
          - HETERJUDGESWITCH
          - USERDATAMIGEXCEPENHANCESW
          - STOPTRACECPUTHD
          - SCTPDELAYSYNFLOWCTRLSW
          - MSGPRIQUEUECOMBINESW
          - ROLLBACKSTATUS
          - GLBDATAPOLICY
          - LOCREPCHECKSWITCH
          - HLOADSWITCH
          - RPRESTORENUM
          - BROADCASTPOLICY
          - QFECTRSW
          - QBEPRESSPARA
          - KEYRESPROTECT
          - FEBEFLOWSW
          - PARTITIONFLOWSW
          - RCVUSERLISTNUM
          - RCVUSERSPEED
          - SYNFLOWPRESSPARA
          - MMLTLSAUTHSWITCH
          - LENQUKVFYQUEFORPARTITION
          - DTLSOVERSCTPSWT
          - NOTIFYMAPPING
          - MAXNODERECORDLIMIT
          - SSHSFTPSRVSEPARATION
          - ACTIVELOCELECTSWT
          - GRDSYNCMODE
          - MLOADBUFLEN
          - MLOADDELAYTIME
          - RLOADBUFLEN
          - RLOADDELAYTIME
          - FABRICPROTECTSW
          - FABRICPROTECTFLOWPRESSPARA
          - FABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPROTECTSW
          - SDRFABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPORTFLOWCTREND
          - ALLOWENDWITHFSWITCH
          - MIGRATEWATCHPERIOD
          - HRCPMSMGR
          - MAXBROADCASTNUM
          - MAXVRYNUMINPRIKEY
          - FILEBKPENCSWT
          - ALLOWCSVTYPESWITCH
          - ALARMFORFAILEDEXP
          - MAXSFTPIPNUM
          - PGWCLEARMMLSWITCH
          - WEBLMTCONNTIMEOUT
          - SFTPCLIENTHOSTKEYSWITCH
          - SSORIGHTSWITCH
          - EXCOMLSHIELDSWITCH
          - SPCFTIMERSTSWT
          - RETENTION_EMG_BACKUP
          - VERIFYCOMPATIBILITYSWT
          - MAXINDEXBROADCASTNUM
          - BRDCSTFLOWCTLDROPSWT
          - MIGRATECTRLSWT
          - REDUNDANCYSYNFLOWCTRLSW
          - SCTPRCVQUEUETHD
          - DSGLINKCFGCHKSWT
          - NONGLOBALROUTEMODESWT
          - SPECFICDSGSCTPSRVSWT
          - PARGLBDATAVFYSPD
          - BATCHQUERYLIMIT
          - BATCHMODIFYLIMIT
          - BATCHMODIFYFAILLOGRETENTION
          - BUSINESSUSERLOCKTIMEOUT
          - BUSINESSUSERLOCKSWITCH
          - DMSRIGHTSWITCH
          - MAXONEUSERWEBLMTNUMS
          - MAXPAGEQUERYUSERDATANUM
          - UNIONEXPSPEED
          - ALMSUPPRESSIONSWT
          - ACCFILETIMEOUT
          - FTPCLIENTSENDPACKETCOUNT
          - FTPCLIENTPACKETSIZE
          - FTPCLIENTFLOWCTRLSENDTASKDELAY
          - SFTPCLIENTPACKETSIZE
          - SFTPCLIENTFLOWCTRLSENDTASKDELAY
          - EXPLOGTASKTARMODE
          - PHYDBMAXMEMORYSIZE
          - OPRCMDGMGRSWT
          - LGIFAILEDERRSWITCH
          - GDATANOCONSISTNUM
          - USERDATANOCONSISTNUM
          - SECIDXDEFVALSTORESWT
          - RESTCONNWAITTIME
          - GLOBALDATANOTIFYSWITCH
          - DCIFORWARDINGSWT
          - FABRICPLANELOADBALANCESW
          - FABRICPLANEPRISETSW
          - SOAPRSPMSGMODE
          - MAXIMPNUMBER
          - VERIFYMERGESWT
          - LICFROZENBUFFERTIME
          - PHYDBMEMREPSWITCH
          - NOTIFYTOSRCFESWT
          - PSITEHEARTBEATSWITCH
          - PARTITIONFORWARDPOLICY
          - LOCUSERDIFFNUM
          - LOCGDATADIFFNUM
          - VERIFYPAUSETIME
          - CROSSREGIONMIGRATESPEED
          - CROSSREGIONRBKSPEED
          - DYNDATARBKSWITCH
          - USERTRANSSTATUS
          - MAXILEGALBATCHQUERYNUM
          - SECONDMSGBYPASSDRU
          - PARALLELLOADCTRL
          - LICRATEDISPSWITCH
          - GDATAMAXREQNUM
          - SOAPCONBATSWITCH
          - MULTINODEBRDCSTRTNUM
          - INNERMSGSENDPATH
          - RLOADAUTOBATCHSWT
          - MAXRLOADTASKNUMPERIPU
          - UPGRADECOMPATIBILITYSWT
          - MULTIRANGECHECKSWITCH
          - SOAPRPTCTRL
          - THREADMONITORSWT
          - RCVDBEXECSW
          - EXCOMLEXECSW
          - N36NOTIFYSW
          - IMDBINSUFFICIENTTHD
          - DUALPROVLOG
          - INTERNALFILETRANSMODE
          - REPIGNORESWT
          - PHYDBCERTSWITCH
          - SCTPFAULTMMLSWT
          - DMSCONNTIMEOUT
          - MODULENOAUTOASSIGNALGORI
          - PLANEBATCHESMAXNUM
          - VERIFYHASHALGORITHM
          - CMPDBEXECSW
          - CMPDBPARALLELNUM
          - CMPDBSPEED
          - LIGHTSCHEDULSWT
          - BPTHREADDETACHSWT
          - SIMPLEDCIREPCOMPRSWT
          - WEBLMTLOGSAVEDAYS
          - PROVLOCREPMULTHREADSWT
          - ENABLEROARTINDEX
          - ROUTECONFLICTVFYMODE
          - GLOBALROUTEGENMODE
          - LOGAUDITSW
          - OBJREBUILDFRAGTHD
          - EXCOMLUSERQUERYSTEP
          - PGWCHECKRESTOPNAME
          - BATPARALLELADAPTSW
          - PHYDBBACKUPTRANSINTV
          - VERIFYCODEDISTIMES
          - USERDATASYNCVSPSW
          - VERIFYENHANCEMODE
          - MAXRLOADTASKNUMPERDSG
          - CUSIMPFAILEDNUM
          - NEWSUBALLOCMODE
          - SOAPGRANTIPMODE
          - PGWSDRFABRICPROTECTSW
          - AUTOTAKEOVERFWDMODE
          - CDB_VRSP_R_RECONSTRUCTMODE
          - BATSEQMINLEN
          - USERTRANSQRYSPEED
          - DRUUPGDPLANEACCSS
          - VFYCYCPRD
          - MANMACHINERELGISWT
          - THIRDSYSTEMSSOMODE
          - COUNTMERGESWT
          - LSTLOGRPTMAXRECNUM
          - DSUIMDBBALTHD
          - EXPFILEENCSWT
          - EXPLOGFILEENCSWT
          - MEMLOGCTRLSWT
          - STBYPDAPRTSW
          - DYNUSERMEASUREGROUP
          - LICENSEDEVIATION
          - LICENSEINTERVAL
          - USERTRANSLOCKSWT
          - ROUTEDRUREDOARCHIVEDAYS
          - GBKCODECONVERSIONSWITCH
          - PGWSNDDCIMSGPRIORITY
          - FTPPASSIVEIPVFYSWT
          - SCTPHASHALGO
          - DCIRSPCOMPRESSMODE
          - IPUPROTECTSW
          - IPUPROTECTTHD
          - IPUPROTECTENDTHD
          - IPURSPBANDWIDTH
          - DCIRSPCMPSTARTTHD
          - DCIRSPCMPCLOSETHD
          - LOCREPCOMPATIBILITYSWT
          - FVMODTSRECORDMODE
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
    add_provisionip_list:
      type: items
      properties:
        ADDRID:
          name: 'IP地址索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '本局内唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRNAME:
          name: 'IP地址名称'
          type: string
          maxLength: 256
          required: false
          description: '本局内唯一。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'IPTYPE为BOSS/SOAP/REST时，此处规划的是业务发放系统的IP地址。  IPTYPE为WEBLMT时，此处是PGW Web LMT的IP地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - SOAP
          - BOSS
          - WEBLMT
          - REST
          - HTTP
          required: true
          description: '业务发放系统采用MML/SOAP/REST（Restful）接口管理用户数据时，设置为BOSS/SOAP/REST。  通过PGW Web LMT管理用户数据时，设置为WEBLMT。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: '支持配置IP段。此处以主机IP为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_insp_list_1:
      type: items
      properties:
        INSPT:
          name: '软件参数类型'
          type: string
          enum:
          - PCDR
          - LOG
          - DBSRV
          - WDS
          - MULTIDRU
          - VERIFY
          - PGW
          - LDAP
          - STAT
          - FE
          - FUNCCFG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSPN:
          name: '软件参数名称'
          type: string
          enum:
          - MAXONECLIENTNUMS
          - FWDLOGINFOSWITCH
          - USCDBLOGFLAG
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
          - MSCLEARTIME
          - MSBUFREMAIN
          - SERVICEPORT
          - DRUIMDBS
          - DSUIMDBS
          - LDRSOURCE
          - TSYNCOPER
          - TQUERYOPER
          - TVERIFYOPER
          - TMULTINODEOPER
          - TREPRSPW
          - TVERIFYRSPW
          - TDSURSPW
          - TSYNCREPRSPW
          - TASYNCREPRSPW
          - TVERITYRSPW
          - FWDVFYSWT
          - REVVFYSWT
          - FWDRTVFYSWT
          - REVRTVFYSWT
          - TMFWDVFY
          - TMREVVFY
          - TMFWDRTVFY
          - TMREVRTVFY
          - PRDFWDVFY
          - PRDREVVFY
          - PRDFWDRTVFY
          - PRDREVRTVFY
          - GLOBALDATAREFRESHCYCLE
          - DRUFRWDVFYUNITNUM
          - DSUFRWDVFYUNITNUM
          - REVVFYUNITNUM
          - FWDRTVFYUNITNUM
          - REVRTVFYUNITNUM
          - HESRTBEATPERIOD
          - INNERHEARTBEATTIMEOUT
          - OUTERHEARTBEATTIMEOUT
          - CHECKPERIOD
          - THREADMONPERIOD
          - REPSPENDTIME
          - UPGRADESTATUS
          - TIMEBACKUPFLAG
          - BACKUPHOUR
          - BACKUPMINUTE
          - CBTABLESIZE
          - TIMEROFAllDRUWAIT
          - TIMEROFUSRVFY
          - TIMEROFEXCPTROUTEVFY
          - PERIODVFYONLYCHECK
          - REDUNDANCYSWITCH
          - NOCONSISTWARINGNUM
          - COUNTERLOGSWT
          - INTERREPSWITCH
          - LANGUAGE
          - PATCHSWITCH
          - SESWITCH
          - MAXWEBLMTNUMBER
          - MAXCLIENTNUMBER
          - PGWREJECTSWITCH
          - VERIFYCODEFLAG
          - BATSEQLEN
          - PGWRESERVE1
          - PGWBATSTEP
          - PGWDIRMONINTV
          - TLSMODE
          - SOAPVERSION
          - CONNWAITTIME
          - TRANSTIMEOUT
          - MAXCONNNUMPERIP
          - SOAPMAXRECVBUFFER
          - SOAPMAXSENDBUFFER
          - SESSIONTIMEOUT
          - HTTPSAUTHSWITCH
          - LDAPSWITCH
          - RLOADSWITCH
          - RLOADTIMEOUT
          - RLOADPACKETSIZE
          - RCHANNELLOADSW
          - REDUCFSWITCH
          - REDUTFSWITCH
          - REDURFSWITCH
          - REDUCFINTERVAL
          - REDURFINTERVAL
          - REDUALAINTERVAL
          - APPLICATIONTYPE
          - PGWOPLOGTYPE
          - PGWOPLOGCYC
          - USERDATAMEASUREFLAG
          - MEASUREHOUR
          - MEASUREMINUTE
          - STARTLICENSETIME
          - GRANTIPSWITCH
          - WEBLMTHTTPSSWITCH
          - PGWLOGMAXCOUNT
          - GDRUIMDBS
          - IUDMSWT
          - IUDMLSD
          - IUDMHOUR
          - IUDMMIN
          - WEBLMTTIMEOUT
          - USERTRANSSPEED
          - UIVFYSWT
          - PRDUIVFY
          - UIVFYUNITNUM
          - DMVFYSWT
          - PGWSNDDCIMSGMODE
          - LINGERTIME
          - NPSWITCH
          - MVNOSWITCH
          - PWDVERIFYSWITCH
          - CONBATMMLQUEUE
          - JRVFYPRD
          - JRVFYUNITNUM
          - REDUNAUTOTAKEOVER
          - TAKEOVERDELAY
          - LICINFODSPCTRL
          - DATANOTIFYMODE
          - DSNOTIFYTIMEOUT
          - DSNOTIFYRETRY
          - PRVBATRSTSAVEPATH
          - CMDDISCARDSWITCH
          - NOTIFYLINKSWAPSWITCH
          - VFYDATARECORDFLAG
          - NOTIFYHBTIMEWAIT
          - SESSIONIDALGSWITCH
          - RSPWITHOUTDESCSWITCH
          - SOAPENVSWITCH
          - MAXBATNUMBER
          - AUTORECOVERYFLAG
          - LENQUKVFYQUE
          - REDQUKVFYSPD
          - DYNUSERMEASURE
          - DYNMEASURESPEED
          - INNERQUKVFYSWT
          - LOCREPEVENT
          - LOGDISCARDCMDSWITCH
          - LOGORIGINALSOAPSWITCH
          - DRUINNERREPQUEUESIZE
          - DELSUBDATASWT
          - SCANSUBDATASPEED
          - SOAPPACKAGEMAXSIZE
          - STATBUFFRESULTSIZE
          - CLOUDADDSIDPOLICY
          - PROVRIGHTSWITCH
          - USERTRACEFLAG
          - PGWMMLSWITCH
          - WEBLMTFILERESTRICT
          - IMSRETINFOSWITCH
          - FORBIDCRCERR
          - PGWSERIALSWITCH
          - NOTIFYGETLOCATIONPOLICY
          - MAXCPUOVERLOADVALUE
          - SUPP_DOWNTIME_FUNC
          - DOWNTIME_THRESHOLD
          - LINKAGESWITCH
          - SERVICERIGHTSWITCH
          - EXTERNALACCESSSWITCH
          - VMSTORAGEFAULTRMSWITCH
          - MAXCMDNUMPERBAT
          - LOGTOOMU
          - EMIGRATIONPERIOD
          - SENDHBBYCLUSTER
          - NEEXPMMLANDPLA
          - LICDSPMODE
          - BYPASSDRUSWITCH
          - OUTERQUKVFYSWT
          - VFYCOVERRECORDSWT
          - PARALLELLOADNUM
          - SPLOCALEXC
          - BATSUSPENDSWITCH
          - SOCKETUNIQUE
          - FINDOPRFORHEADAUTH
          - PROVISIONBATRESULTFILESWITCH
          - AUTHWITHSRCIP
          - SPCFDIRRSTSWT
          - QUKVERIFYMODE
          - PGWLOGCOUNT
          - NOTIFYCONTROL
          - SENDHBMODE
          - SPCFOPLOGWRITEFILESWT
          - LDAPCONNTHDALMSWT
          - DRUOUTERREPQUEUESIZE
          - DSUINNERREPQUEUESIZE
          - DSUOUTERREPQUEUESIZE
          - SSHALGORITHMSWITCH
          - GDRUTHREADNUM
          - DRUTHREADNUM
          - DSUTHREADNUM
          - SAVLOGMAXCOUNT
          - PGWLOGORDER
          - ROUTEMIGMSGSIZE
          - LICCUSTOMIZEDSWITCH
          - EXPMSGQLENGTH
          - IMDBWORKMODE
          - OBJECTSERIALIZEFLAG
          - NUMBATPROCESSSWITCH
          - PGWSESSIONMAXNUM
          - PGWCONALMSWT
          - IMPORTSEQLEN
          - STATICMEASURESPEED
          - DSUUSRCNTUPDTHD
          - MCIRETURNIMMEDIATELY
          - AAMODESWITCH
          - TIMINGSUBSCRIPTIONUNITNUM
          - TIMINGSUBSCRIPTIONRESENDPERIOD
          - INCONSISTENTTHRESHOLD
          - EXPORTSPEED
          - SERVERLINGERTIME
          - GDATAEXPORTSPEED
          - RTMTNMODE
          - DELJUNKDATANUM
          - REMAINDATANUM
          - DRUDISPATCHMODE
          - DMAGLOBALREFRESHCYCLE
          - FLOWCTRLRSPSWITCH
          - MSGTIMEOUTTHRESHOLD
          - DRUREPRSPW
          - DRUSYNCREPRSPW
          - PCDRBTPWINSIZE
          - THIRDCFGCHECKSWITCH
          - RETENTION_BACKUP
          - RETENTION_LOG
          - RETENTION_EXPORT
          - Q922TASKDELAYTIME
          - CLUSTERBALANCESWITCH
          - PGWLOGTOREMOTE
          - MASTERLDRCOMPRESS
          - EMGRSTMODE
          - DELJUNKDATACYCLE
          - IGNOREPREFIXCHECK
          - BATWRITERESULTAPART
          - AUTOBATPARALLELNUM
          - BATCMDASYNCNOTIFY
          - EXCOMLQUERYSPEED
          - EXCOMLUPDATESPEED
          - CLOUDADAPTERSWITCH
          - NETWORKMODE
          - DCIFWDMODE
          - NOTIFYFLOWMSGCOUNT
          - LOCREPMULTHREADSWT
          - OBJECTCOMPRESSMODE
          - SOAPDECODESWITCH
          - SELFSPACEBACKUP
          - THIRDSPACEBACKUP
          - UPDOWNTASKNUM
          - TIMEOUTTHIRDBKLOAD
          - TIMEOUTSELFBKLOAD
          - DSULOADSHAREMODE
          - GROUTEVRFYSWT
          - BROADCASTQUERYSTEP
          - BROADCASTUPDATESTEP
          - SFTPUSERPWDVALID
          - BATCHROUTEUPDATEDELAYTIME
          - EXCEPTIONROUTEVERIFYSWITCH
          - BATCHREPLICATIONDELAYTIME
          - BATCHREPLICATIONMODE
          - TAKEOVERFORCLUSTER
          - EXPIRETIME
          - PROVBATCHDELORIFILE
          - MAPLOGTOVRP
          - FWDMMLERRCODESWT
          - PROVBATCHFOBTAINFILEMODE
          - WEBLMTSECURITYOPTIONSWITCH
          - USERTRANSBKPSWITCH
          - MAXTMOUTPROVFORWARD
          - COMMANDACCESSTYPECONTROL
          - NTFCFGOFREMOTEIDSWITCH
          - OPRPWDPBKDF2ALGSWITCH
          - SOAPERRORMSGTYPESWITCH
          - REDOARCHIVEDAYS
          - INCREDOSWITCH
          - DBPAGEVACUUMMODE
          - PSITEMSGSWITCH
          - DMAMODULECFGSWT
          - SSHKEXALGORITHMSWITCH
          - LOCATIONVERIFYMODE
          - BKPFILEVRFSWT
          - CERTALAINTERVAL
          - KVDCISYNCTOUDB
          - SFTPCLIENTSECURITYALGSW
          - RESTHTTPSAUTHSWITCH
          - BYPASSREVRTSYNSWITCH
          - LENQUKVFYQUEOFROUTE
          - HTTPPROVRIGHTSWITCH
          - PROVHTTPSAUTHSWITCH
          - USERTRANSRECOVERSPEED
          - COMFORMATOFEXPFILE
          - FILEUPLOADMODE
          - HETERJUDGESWITCH
          - USERDATAMIGEXCEPENHANCESW
          - STOPTRACECPUTHD
          - SCTPDELAYSYNFLOWCTRLSW
          - MSGPRIQUEUECOMBINESW
          - ROLLBACKSTATUS
          - GLBDATAPOLICY
          - LOCREPCHECKSWITCH
          - HLOADSWITCH
          - RPRESTORENUM
          - BROADCASTPOLICY
          - QFECTRSW
          - QBEPRESSPARA
          - KEYRESPROTECT
          - FEBEFLOWSW
          - PARTITIONFLOWSW
          - RCVUSERLISTNUM
          - RCVUSERSPEED
          - SYNFLOWPRESSPARA
          - MMLTLSAUTHSWITCH
          - LENQUKVFYQUEFORPARTITION
          - DTLSOVERSCTPSWT
          - NOTIFYMAPPING
          - MAXNODERECORDLIMIT
          - SSHSFTPSRVSEPARATION
          - ACTIVELOCELECTSWT
          - GRDSYNCMODE
          - MLOADBUFLEN
          - MLOADDELAYTIME
          - RLOADBUFLEN
          - RLOADDELAYTIME
          - FABRICPROTECTSW
          - FABRICPROTECTFLOWPRESSPARA
          - FABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPROTECTSW
          - SDRFABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPORTFLOWCTREND
          - ALLOWENDWITHFSWITCH
          - MIGRATEWATCHPERIOD
          - HRCPMSMGR
          - MAXBROADCASTNUM
          - MAXVRYNUMINPRIKEY
          - FILEBKPENCSWT
          - ALLOWCSVTYPESWITCH
          - ALARMFORFAILEDEXP
          - MAXSFTPIPNUM
          - PGWCLEARMMLSWITCH
          - WEBLMTCONNTIMEOUT
          - SFTPCLIENTHOSTKEYSWITCH
          - SSORIGHTSWITCH
          - EXCOMLSHIELDSWITCH
          - SPCFTIMERSTSWT
          - RETENTION_EMG_BACKUP
          - VERIFYCOMPATIBILITYSWT
          - MAXINDEXBROADCASTNUM
          - BRDCSTFLOWCTLDROPSWT
          - MIGRATECTRLSWT
          - REDUNDANCYSYNFLOWCTRLSW
          - SCTPRCVQUEUETHD
          - DSGLINKCFGCHKSWT
          - NONGLOBALROUTEMODESWT
          - SPECFICDSGSCTPSRVSWT
          - PARGLBDATAVFYSPD
          - BATCHQUERYLIMIT
          - BATCHMODIFYLIMIT
          - BATCHMODIFYFAILLOGRETENTION
          - BUSINESSUSERLOCKTIMEOUT
          - BUSINESSUSERLOCKSWITCH
          - DMSRIGHTSWITCH
          - MAXONEUSERWEBLMTNUMS
          - MAXPAGEQUERYUSERDATANUM
          - UNIONEXPSPEED
          - ALMSUPPRESSIONSWT
          - ACCFILETIMEOUT
          - FTPCLIENTSENDPACKETCOUNT
          - FTPCLIENTPACKETSIZE
          - FTPCLIENTFLOWCTRLSENDTASKDELAY
          - SFTPCLIENTPACKETSIZE
          - SFTPCLIENTFLOWCTRLSENDTASKDELAY
          - EXPLOGTASKTARMODE
          - PHYDBMAXMEMORYSIZE
          - OPRCMDGMGRSWT
          - LGIFAILEDERRSWITCH
          - GDATANOCONSISTNUM
          - USERDATANOCONSISTNUM
          - SECIDXDEFVALSTORESWT
          - RESTCONNWAITTIME
          - GLOBALDATANOTIFYSWITCH
          - DCIFORWARDINGSWT
          - FABRICPLANELOADBALANCESW
          - FABRICPLANEPRISETSW
          - SOAPRSPMSGMODE
          - MAXIMPNUMBER
          - VERIFYMERGESWT
          - LICFROZENBUFFERTIME
          - PHYDBMEMREPSWITCH
          - NOTIFYTOSRCFESWT
          - PSITEHEARTBEATSWITCH
          - PARTITIONFORWARDPOLICY
          - LOCUSERDIFFNUM
          - LOCGDATADIFFNUM
          - VERIFYPAUSETIME
          - CROSSREGIONMIGRATESPEED
          - CROSSREGIONRBKSPEED
          - DYNDATARBKSWITCH
          - USERTRANSSTATUS
          - MAXILEGALBATCHQUERYNUM
          - SECONDMSGBYPASSDRU
          - PARALLELLOADCTRL
          - LICRATEDISPSWITCH
          - GDATAMAXREQNUM
          - SOAPCONBATSWITCH
          - MULTINODEBRDCSTRTNUM
          - INNERMSGSENDPATH
          - RLOADAUTOBATCHSWT
          - MAXRLOADTASKNUMPERIPU
          - UPGRADECOMPATIBILITYSWT
          - MULTIRANGECHECKSWITCH
          - SOAPRPTCTRL
          - THREADMONITORSWT
          - RCVDBEXECSW
          - EXCOMLEXECSW
          - N36NOTIFYSW
          - IMDBINSUFFICIENTTHD
          - DUALPROVLOG
          - INTERNALFILETRANSMODE
          - REPIGNORESWT
          - PHYDBCERTSWITCH
          - SCTPFAULTMMLSWT
          - DMSCONNTIMEOUT
          - MODULENOAUTOASSIGNALGORI
          - PLANEBATCHESMAXNUM
          - VERIFYHASHALGORITHM
          - CMPDBEXECSW
          - CMPDBPARALLELNUM
          - CMPDBSPEED
          - LIGHTSCHEDULSWT
          - BPTHREADDETACHSWT
          - SIMPLEDCIREPCOMPRSWT
          - WEBLMTLOGSAVEDAYS
          - PROVLOCREPMULTHREADSWT
          - ENABLEROARTINDEX
          - ROUTECONFLICTVFYMODE
          - GLOBALROUTEGENMODE
          - LOGAUDITSW
          - OBJREBUILDFRAGTHD
          - EXCOMLUSERQUERYSTEP
          - PGWCHECKRESTOPNAME
          - BATPARALLELADAPTSW
          - PHYDBBACKUPTRANSINTV
          - VERIFYCODEDISTIMES
          - USERDATASYNCVSPSW
          - VERIFYENHANCEMODE
          - MAXRLOADTASKNUMPERDSG
          - CUSIMPFAILEDNUM
          - NEWSUBALLOCMODE
          - SOAPGRANTIPMODE
          - PGWSDRFABRICPROTECTSW
          - AUTOTAKEOVERFWDMODE
          - CDB_VRSP_R_RECONSTRUCTMODE
          - BATSEQMINLEN
          - USERTRANSQRYSPEED
          - DRUUPGDPLANEACCSS
          - VFYCYCPRD
          - MANMACHINERELGISWT
          - THIRDSYSTEMSSOMODE
          - COUNTMERGESWT
          - LSTLOGRPTMAXRECNUM
          - DSUIMDBBALTHD
          - EXPFILEENCSWT
          - EXPLOGFILEENCSWT
          - MEMLOGCTRLSWT
          - STBYPDAPRTSW
          - DYNUSERMEASUREGROUP
          - LICENSEDEVIATION
          - LICENSEINTERVAL
          - USERTRANSLOCKSWT
          - ROUTEDRUREDOARCHIVEDAYS
          - GBKCODECONVERSIONSWITCH
          - PGWSNDDCIMSGPRIORITY
          - FTPPASSIVEIPVFYSWT
          - SCTPHASHALGO
          - DCIRSPCOMPRESSMODE
          - IPUPROTECTSW
          - IPUPROTECTTHD
          - IPUPROTECTENDTHD
          - IPURSPBANDWIDTH
          - DCIRSPCMPSTARTTHD
          - DCIRSPCMPCLOSETHD
          - LOCREPCOMPATIBILITYSWT
          - FVMODTSRECORDMODE
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
    mod_insp_list_3:
      type: items
      properties:
        INSPT:
          name: '软件参数类型'
          type: string
          enum:
          - PCDR
          - LOG
          - DBSRV
          - WDS
          - MULTIDRU
          - VERIFY
          - PGW
          - LDAP
          - STAT
          - FE
          - FUNCCFG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSPN:
          name: '软件参数名称'
          type: string
          enum:
          - MAXONECLIENTNUMS
          - FWDLOGINFOSWITCH
          - USCDBLOGFLAG
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
          - MSCLEARTIME
          - MSBUFREMAIN
          - SERVICEPORT
          - DRUIMDBS
          - DSUIMDBS
          - LDRSOURCE
          - TSYNCOPER
          - TQUERYOPER
          - TVERIFYOPER
          - TMULTINODEOPER
          - TREPRSPW
          - TVERIFYRSPW
          - TDSURSPW
          - TSYNCREPRSPW
          - TASYNCREPRSPW
          - TVERITYRSPW
          - FWDVFYSWT
          - REVVFYSWT
          - FWDRTVFYSWT
          - REVRTVFYSWT
          - TMFWDVFY
          - TMREVVFY
          - TMFWDRTVFY
          - TMREVRTVFY
          - PRDFWDVFY
          - PRDREVVFY
          - PRDFWDRTVFY
          - PRDREVRTVFY
          - GLOBALDATAREFRESHCYCLE
          - DRUFRWDVFYUNITNUM
          - DSUFRWDVFYUNITNUM
          - REVVFYUNITNUM
          - FWDRTVFYUNITNUM
          - REVRTVFYUNITNUM
          - HESRTBEATPERIOD
          - INNERHEARTBEATTIMEOUT
          - OUTERHEARTBEATTIMEOUT
          - CHECKPERIOD
          - THREADMONPERIOD
          - REPSPENDTIME
          - UPGRADESTATUS
          - TIMEBACKUPFLAG
          - BACKUPHOUR
          - BACKUPMINUTE
          - CBTABLESIZE
          - TIMEROFAllDRUWAIT
          - TIMEROFUSRVFY
          - TIMEROFEXCPTROUTEVFY
          - PERIODVFYONLYCHECK
          - REDUNDANCYSWITCH
          - NOCONSISTWARINGNUM
          - COUNTERLOGSWT
          - INTERREPSWITCH
          - LANGUAGE
          - PATCHSWITCH
          - SESWITCH
          - MAXWEBLMTNUMBER
          - MAXCLIENTNUMBER
          - PGWREJECTSWITCH
          - VERIFYCODEFLAG
          - BATSEQLEN
          - PGWRESERVE1
          - PGWBATSTEP
          - PGWDIRMONINTV
          - TLSMODE
          - SOAPVERSION
          - CONNWAITTIME
          - TRANSTIMEOUT
          - MAXCONNNUMPERIP
          - SOAPMAXRECVBUFFER
          - SOAPMAXSENDBUFFER
          - SESSIONTIMEOUT
          - HTTPSAUTHSWITCH
          - LDAPSWITCH
          - RLOADSWITCH
          - RLOADTIMEOUT
          - RLOADPACKETSIZE
          - RCHANNELLOADSW
          - REDUCFSWITCH
          - REDUTFSWITCH
          - REDURFSWITCH
          - REDUCFINTERVAL
          - REDURFINTERVAL
          - REDUALAINTERVAL
          - APPLICATIONTYPE
          - PGWOPLOGTYPE
          - PGWOPLOGCYC
          - USERDATAMEASUREFLAG
          - MEASUREHOUR
          - MEASUREMINUTE
          - STARTLICENSETIME
          - GRANTIPSWITCH
          - WEBLMTHTTPSSWITCH
          - PGWLOGMAXCOUNT
          - GDRUIMDBS
          - IUDMSWT
          - IUDMLSD
          - IUDMHOUR
          - IUDMMIN
          - WEBLMTTIMEOUT
          - USERTRANSSPEED
          - UIVFYSWT
          - PRDUIVFY
          - UIVFYUNITNUM
          - DMVFYSWT
          - PGWSNDDCIMSGMODE
          - LINGERTIME
          - NPSWITCH
          - MVNOSWITCH
          - PWDVERIFYSWITCH
          - CONBATMMLQUEUE
          - JRVFYPRD
          - JRVFYUNITNUM
          - REDUNAUTOTAKEOVER
          - TAKEOVERDELAY
          - LICINFODSPCTRL
          - DATANOTIFYMODE
          - DSNOTIFYTIMEOUT
          - DSNOTIFYRETRY
          - PRVBATRSTSAVEPATH
          - CMDDISCARDSWITCH
          - NOTIFYLINKSWAPSWITCH
          - VFYDATARECORDFLAG
          - NOTIFYHBTIMEWAIT
          - SESSIONIDALGSWITCH
          - RSPWITHOUTDESCSWITCH
          - SOAPENVSWITCH
          - MAXBATNUMBER
          - AUTORECOVERYFLAG
          - LENQUKVFYQUE
          - REDQUKVFYSPD
          - DYNUSERMEASURE
          - DYNMEASURESPEED
          - INNERQUKVFYSWT
          - LOCREPEVENT
          - LOGDISCARDCMDSWITCH
          - LOGORIGINALSOAPSWITCH
          - DRUINNERREPQUEUESIZE
          - DELSUBDATASWT
          - SCANSUBDATASPEED
          - SOAPPACKAGEMAXSIZE
          - STATBUFFRESULTSIZE
          - CLOUDADDSIDPOLICY
          - PROVRIGHTSWITCH
          - USERTRACEFLAG
          - PGWMMLSWITCH
          - WEBLMTFILERESTRICT
          - IMSRETINFOSWITCH
          - FORBIDCRCERR
          - PGWSERIALSWITCH
          - NOTIFYGETLOCATIONPOLICY
          - MAXCPUOVERLOADVALUE
          - SUPP_DOWNTIME_FUNC
          - DOWNTIME_THRESHOLD
          - LINKAGESWITCH
          - SERVICERIGHTSWITCH
          - EXTERNALACCESSSWITCH
          - VMSTORAGEFAULTRMSWITCH
          - MAXCMDNUMPERBAT
          - LOGTOOMU
          - EMIGRATIONPERIOD
          - SENDHBBYCLUSTER
          - NEEXPMMLANDPLA
          - LICDSPMODE
          - BYPASSDRUSWITCH
          - OUTERQUKVFYSWT
          - VFYCOVERRECORDSWT
          - PARALLELLOADNUM
          - SPLOCALEXC
          - BATSUSPENDSWITCH
          - SOCKETUNIQUE
          - FINDOPRFORHEADAUTH
          - PROVISIONBATRESULTFILESWITCH
          - AUTHWITHSRCIP
          - SPCFDIRRSTSWT
          - QUKVERIFYMODE
          - PGWLOGCOUNT
          - NOTIFYCONTROL
          - SENDHBMODE
          - SPCFOPLOGWRITEFILESWT
          - LDAPCONNTHDALMSWT
          - DRUOUTERREPQUEUESIZE
          - DSUINNERREPQUEUESIZE
          - DSUOUTERREPQUEUESIZE
          - SSHALGORITHMSWITCH
          - GDRUTHREADNUM
          - DRUTHREADNUM
          - DSUTHREADNUM
          - SAVLOGMAXCOUNT
          - PGWLOGORDER
          - ROUTEMIGMSGSIZE
          - LICCUSTOMIZEDSWITCH
          - EXPMSGQLENGTH
          - IMDBWORKMODE
          - OBJECTSERIALIZEFLAG
          - NUMBATPROCESSSWITCH
          - PGWSESSIONMAXNUM
          - PGWCONALMSWT
          - IMPORTSEQLEN
          - STATICMEASURESPEED
          - DSUUSRCNTUPDTHD
          - MCIRETURNIMMEDIATELY
          - AAMODESWITCH
          - TIMINGSUBSCRIPTIONUNITNUM
          - TIMINGSUBSCRIPTIONRESENDPERIOD
          - INCONSISTENTTHRESHOLD
          - EXPORTSPEED
          - SERVERLINGERTIME
          - GDATAEXPORTSPEED
          - RTMTNMODE
          - DELJUNKDATANUM
          - REMAINDATANUM
          - DRUDISPATCHMODE
          - DMAGLOBALREFRESHCYCLE
          - FLOWCTRLRSPSWITCH
          - MSGTIMEOUTTHRESHOLD
          - DRUREPRSPW
          - DRUSYNCREPRSPW
          - PCDRBTPWINSIZE
          - THIRDCFGCHECKSWITCH
          - RETENTION_BACKUP
          - RETENTION_LOG
          - RETENTION_EXPORT
          - Q922TASKDELAYTIME
          - CLUSTERBALANCESWITCH
          - PGWLOGTOREMOTE
          - MASTERLDRCOMPRESS
          - EMGRSTMODE
          - DELJUNKDATACYCLE
          - IGNOREPREFIXCHECK
          - BATWRITERESULTAPART
          - AUTOBATPARALLELNUM
          - BATCMDASYNCNOTIFY
          - EXCOMLQUERYSPEED
          - EXCOMLUPDATESPEED
          - CLOUDADAPTERSWITCH
          - NETWORKMODE
          - DCIFWDMODE
          - NOTIFYFLOWMSGCOUNT
          - LOCREPMULTHREADSWT
          - OBJECTCOMPRESSMODE
          - SOAPDECODESWITCH
          - SELFSPACEBACKUP
          - THIRDSPACEBACKUP
          - UPDOWNTASKNUM
          - TIMEOUTTHIRDBKLOAD
          - TIMEOUTSELFBKLOAD
          - DSULOADSHAREMODE
          - GROUTEVRFYSWT
          - BROADCASTQUERYSTEP
          - BROADCASTUPDATESTEP
          - SFTPUSERPWDVALID
          - BATCHROUTEUPDATEDELAYTIME
          - EXCEPTIONROUTEVERIFYSWITCH
          - BATCHREPLICATIONDELAYTIME
          - BATCHREPLICATIONMODE
          - TAKEOVERFORCLUSTER
          - EXPIRETIME
          - PROVBATCHDELORIFILE
          - MAPLOGTOVRP
          - FWDMMLERRCODESWT
          - PROVBATCHFOBTAINFILEMODE
          - WEBLMTSECURITYOPTIONSWITCH
          - USERTRANSBKPSWITCH
          - MAXTMOUTPROVFORWARD
          - COMMANDACCESSTYPECONTROL
          - NTFCFGOFREMOTEIDSWITCH
          - OPRPWDPBKDF2ALGSWITCH
          - SOAPERRORMSGTYPESWITCH
          - REDOARCHIVEDAYS
          - INCREDOSWITCH
          - DBPAGEVACUUMMODE
          - PSITEMSGSWITCH
          - DMAMODULECFGSWT
          - SSHKEXALGORITHMSWITCH
          - LOCATIONVERIFYMODE
          - BKPFILEVRFSWT
          - CERTALAINTERVAL
          - KVDCISYNCTOUDB
          - SFTPCLIENTSECURITYALGSW
          - RESTHTTPSAUTHSWITCH
          - BYPASSREVRTSYNSWITCH
          - LENQUKVFYQUEOFROUTE
          - HTTPPROVRIGHTSWITCH
          - PROVHTTPSAUTHSWITCH
          - USERTRANSRECOVERSPEED
          - COMFORMATOFEXPFILE
          - FILEUPLOADMODE
          - HETERJUDGESWITCH
          - USERDATAMIGEXCEPENHANCESW
          - STOPTRACECPUTHD
          - SCTPDELAYSYNFLOWCTRLSW
          - MSGPRIQUEUECOMBINESW
          - ROLLBACKSTATUS
          - GLBDATAPOLICY
          - LOCREPCHECKSWITCH
          - HLOADSWITCH
          - RPRESTORENUM
          - BROADCASTPOLICY
          - QFECTRSW
          - QBEPRESSPARA
          - KEYRESPROTECT
          - FEBEFLOWSW
          - PARTITIONFLOWSW
          - RCVUSERLISTNUM
          - RCVUSERSPEED
          - SYNFLOWPRESSPARA
          - MMLTLSAUTHSWITCH
          - LENQUKVFYQUEFORPARTITION
          - DTLSOVERSCTPSWT
          - NOTIFYMAPPING
          - MAXNODERECORDLIMIT
          - SSHSFTPSRVSEPARATION
          - ACTIVELOCELECTSWT
          - GRDSYNCMODE
          - MLOADBUFLEN
          - MLOADDELAYTIME
          - RLOADBUFLEN
          - RLOADDELAYTIME
          - FABRICPROTECTSW
          - FABRICPROTECTFLOWPRESSPARA
          - FABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPROTECTSW
          - SDRFABRICPORTFLOWCTRTHRESHOLD
          - SDRFABRICPORTFLOWCTREND
          - ALLOWENDWITHFSWITCH
          - MIGRATEWATCHPERIOD
          - HRCPMSMGR
          - MAXBROADCASTNUM
          - MAXVRYNUMINPRIKEY
          - FILEBKPENCSWT
          - ALLOWCSVTYPESWITCH
          - ALARMFORFAILEDEXP
          - MAXSFTPIPNUM
          - PGWCLEARMMLSWITCH
          - WEBLMTCONNTIMEOUT
          - SFTPCLIENTHOSTKEYSWITCH
          - SSORIGHTSWITCH
          - EXCOMLSHIELDSWITCH
          - SPCFTIMERSTSWT
          - RETENTION_EMG_BACKUP
          - VERIFYCOMPATIBILITYSWT
          - MAXINDEXBROADCASTNUM
          - BRDCSTFLOWCTLDROPSWT
          - MIGRATECTRLSWT
          - REDUNDANCYSYNFLOWCTRLSW
          - SCTPRCVQUEUETHD
          - DSGLINKCFGCHKSWT
          - NONGLOBALROUTEMODESWT
          - SPECFICDSGSCTPSRVSWT
          - PARGLBDATAVFYSPD
          - BATCHQUERYLIMIT
          - BATCHMODIFYLIMIT
          - BATCHMODIFYFAILLOGRETENTION
          - BUSINESSUSERLOCKTIMEOUT
          - BUSINESSUSERLOCKSWITCH
          - DMSRIGHTSWITCH
          - MAXONEUSERWEBLMTNUMS
          - MAXPAGEQUERYUSERDATANUM
          - UNIONEXPSPEED
          - ALMSUPPRESSIONSWT
          - ACCFILETIMEOUT
          - FTPCLIENTSENDPACKETCOUNT
          - FTPCLIENTPACKETSIZE
          - FTPCLIENTFLOWCTRLSENDTASKDELAY
          - SFTPCLIENTPACKETSIZE
          - SFTPCLIENTFLOWCTRLSENDTASKDELAY
          - EXPLOGTASKTARMODE
          - PHYDBMAXMEMORYSIZE
          - OPRCMDGMGRSWT
          - LGIFAILEDERRSWITCH
          - GDATANOCONSISTNUM
          - USERDATANOCONSISTNUM
          - SECIDXDEFVALSTORESWT
          - RESTCONNWAITTIME
          - GLOBALDATANOTIFYSWITCH
          - DCIFORWARDINGSWT
          - FABRICPLANELOADBALANCESW
          - FABRICPLANEPRISETSW
          - SOAPRSPMSGMODE
          - MAXIMPNUMBER
          - VERIFYMERGESWT
          - LICFROZENBUFFERTIME
          - PHYDBMEMREPSWITCH
          - NOTIFYTOSRCFESWT
          - PSITEHEARTBEATSWITCH
          - PARTITIONFORWARDPOLICY
          - LOCUSERDIFFNUM
          - LOCGDATADIFFNUM
          - VERIFYPAUSETIME
          - CROSSREGIONMIGRATESPEED
          - CROSSREGIONRBKSPEED
          - DYNDATARBKSWITCH
          - USERTRANSSTATUS
          - MAXILEGALBATCHQUERYNUM
          - SECONDMSGBYPASSDRU
          - PARALLELLOADCTRL
          - LICRATEDISPSWITCH
          - GDATAMAXREQNUM
          - SOAPCONBATSWITCH
          - MULTINODEBRDCSTRTNUM
          - INNERMSGSENDPATH
          - RLOADAUTOBATCHSWT
          - MAXRLOADTASKNUMPERIPU
          - UPGRADECOMPATIBILITYSWT
          - MULTIRANGECHECKSWITCH
          - SOAPRPTCTRL
          - THREADMONITORSWT
          - RCVDBEXECSW
          - EXCOMLEXECSW
          - N36NOTIFYSW
          - IMDBINSUFFICIENTTHD
          - DUALPROVLOG
          - INTERNALFILETRANSMODE
          - REPIGNORESWT
          - PHYDBCERTSWITCH
          - SCTPFAULTMMLSWT
          - DMSCONNTIMEOUT
          - MODULENOAUTOASSIGNALGORI
          - PLANEBATCHESMAXNUM
          - VERIFYHASHALGORITHM
          - CMPDBEXECSW
          - CMPDBPARALLELNUM
          - CMPDBSPEED
          - LIGHTSCHEDULSWT
          - BPTHREADDETACHSWT
          - SIMPLEDCIREPCOMPRSWT
          - WEBLMTLOGSAVEDAYS
          - PROVLOCREPMULTHREADSWT
          - ENABLEROARTINDEX
          - ROUTECONFLICTVFYMODE
          - GLOBALROUTEGENMODE
          - LOGAUDITSW
          - OBJREBUILDFRAGTHD
          - EXCOMLUSERQUERYSTEP
          - PGWCHECKRESTOPNAME
          - BATPARALLELADAPTSW
          - PHYDBBACKUPTRANSINTV
          - VERIFYCODEDISTIMES
          - USERDATASYNCVSPSW
          - VERIFYENHANCEMODE
          - MAXRLOADTASKNUMPERDSG
          - CUSIMPFAILEDNUM
          - NEWSUBALLOCMODE
          - SOAPGRANTIPMODE
          - PGWSDRFABRICPROTECTSW
          - AUTOTAKEOVERFWDMODE
          - CDB_VRSP_R_RECONSTRUCTMODE
          - BATSEQMINLEN
          - USERTRANSQRYSPEED
          - DRUUPGDPLANEACCSS
          - VFYCYCPRD
          - MANMACHINERELGISWT
          - THIRDSYSTEMSSOMODE
          - COUNTMERGESWT
          - LSTLOGRPTMAXRECNUM
          - DSUIMDBBALTHD
          - EXPFILEENCSWT
          - EXPLOGFILEENCSWT
          - MEMLOGCTRLSWT
          - STBYPDAPRTSW
          - DYNUSERMEASUREGROUP
          - LICENSEDEVIATION
          - LICENSEINTERVAL
          - USERTRANSLOCKSWT
          - ROUTEDRUREDOARCHIVEDAYS
          - GBKCODECONVERSIONSWITCH
          - PGWSNDDCIMSGPRIORITY
          - FTPPASSIVEIPVFYSWT
          - SCTPHASHALGO
          - DCIRSPCOMPRESSMODE
          - IPUPROTECTSW
          - IPUPROTECTTHD
          - IPUPROTECTENDTHD
          - IPURSPBANDWIDTH
          - DCIRSPCMPSTARTTHD
          - DCIRSPCMPCLOSETHD
          - LOCREPCOMPATIBILITYSWT
          - FVMODTSRECORDMODE
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
        FETYPEN:
          name: '网元类型'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_module_list:
      type: items
      properties:
        MID:
          name: '模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '在“MML-USCDB”下使用“LST MODULE: MT=PGW;”查询，获取所有的PGW模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MT:
          name: '模块类型'
          type: string
          enum:
          - DPU
          - NDF
          - DBG
          - DSG
          - DRU
          - DSU
          - PGW
          - DMA
          - CAG
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_opr_list:
      type: items
      properties:
        SYSHLRSN:
          name: '系统HLR序列号'
          type: string
          required: false
          description: '可登录“USCDB MML命令”界面，执行“**LST SYSNO:;**”查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OPNAME:
          name: '操作员名称'
          type: string
          required: false
          description: '操作员登录时的名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '操作员描述'
          type: string
          required: false
          description: '便于识别账号的作用即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          required: false
          description: '默认的密码字符集包含大写字母+小写字母+数字+特殊字符。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UG:
          name: '操作员级别'
          type: string
          required: false
          description: '用于指定操作员的级别。不同级别级别的权限详见MML。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STATUS:
          name: '操作员状态'
          type: string
          required: false
          description: '是否激活操作员，即是否允许操作员登录PGW系统。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ATP:
          name: '账号类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    rmv_srvipaddr_list:
    - SRVINDEX: 3
      SRVIPTYPE: PGW
    add_srvipaddr_list:
    - SRVINDEX: 3
      SRVIPTYPE: PGW
      DPUMID: 3
      IPVER: IPV4
      IP1VPNNAME: 'VRF_provisioning'
      IPV4IP1: '10.200.200.36'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_OM'
      IPV4IP2: '10.200.200.37'
      IPV4MASK2: '255.255.255.255'
    - SRVINDEX: 3
      SRVIPTYPE: PGW
      DPUMID: 3
      IPVER: IPV4
      IP1VPNNAME: 'VRF_provisioning'
      IPV4IP1: '10.201.200.36'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_OM'
      IPV4IP2: '10.201.200.37'
      IPV4MASK2: '255.255.255.255'
    mod_insp_list:
    - INSPT: PGW
      INSPN: GRANTIPSWITCH
      INSPV: 0
    add_provisionip_list:
    - ADDRID: 1
      ADDRNAME: 'PRVIP01'
      IPVER: IPV4
      IPV4ADDR: '10.10.100.20'
      IPTYPE: BOSS
      IPV4MASK: '255.255.255.255'
    - ADDRID: 1
      ADDRNAME: 'PRVIP01'
      IPVER: IPV4
      IPV4ADDR: '10.10.100.20'
      IPTYPE: BOSS
      IPV4MASK: '255.255.255.255'
    mod_insp_list_1:
    - INSPT: PGW
      INSPN: GRANTIPSWITCH
      INSPV: 1
    - INSPT: PGW
      INSPN: GRANTIPSWITCH
      INSPV: 1
    mod_insp_list_3:
    - INSPT: FE
      INSPN: PROVRIGHTSWITCH
      INSPV: 0
      FETYPEN: 'USCDB'
    rst_module_list:
    - MID: 7
      MT: PGW
    add_opr_list:
    - SYSHLRSN: '1'
      OPNAME: boospgwuser
      DESC: boos in pgw system
      PWD: '*****'
      CFM: '*****'
      UG: OPERATOR
      STATUS: ACTIVE
      ATP: MACHINE-TO-MACHINE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**LST SRVIPADDR**命令查询存在与业务发放系统对接的IP地址。

### 查看是否存在业务IP类型为PGW的IP地址：

#### 2.1 不存在=>5。

#### 2.2 存在PGW类型IP，但只有IP1，没有IP2时=>3。

#### 2.3 存在PGW类型IP，且是IP1和IP2两个IP时=>6。

### 3 确认业务发放系统和PGW Web LMT的IP是否属于同一网段。

#### 3.1 是=>6。

#### 3.2 否=>4。

### 4 业务发放系统和PGW Web LMT的IP属于不同网段时，删除PGW类型的业务IP地址，然后再执行5。

#### 4.1 //执行**RMV SRVIPADDR**命令删除PGW类型的业务IP地址。此处以需删除的PGW类型的IP地址索引是3为例。

```jinja2
{%- for item in rmv_srvipaddr_list -%}
    RMV SRVIPADDR:
    {#- --- 必选参数 --- -#}
    SRVINDEX={{item.SRVINDEX}},
    SRVIPTYPE={{item.SRVIPTYPE}},
    ;
{%- endfor -%}
```

### 5 增加业务IP地址，以参数“IPVER”值为“IPV4”为例。

#### 5.1 //DC1：

```jinja2
{%- for item in add_srvipaddr_list -%}
    ADD SRVIPADDR:
    {#- --- 必选参数 --- -#}
    SRVINDEX={{item.SRVINDEX}},
    SRVIPTYPE={{item.SRVIPTYPE}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SRVIPTYPE=PGW/DMA 时必选 --- -#}
    {%- if item.SRVIPTYPE in ['PGW', 'DMA'] -%}
        DPUMID={{item.DPUMID}},
    {%- endif -%}
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

### 6 配置PGW的IP限制功能。

#### 6.1 PGW不校验管理用户数据的源IP时，关闭IP限制开关。

```jinja2
{%- if is_scenario_no_source_ip_check -%}
    {%- for item in mod_insp_list -%}
        MOD INSP:
        {#- --- 必选参数 --- -#}
        INSPT={{item.INSPT}},
        INSPN={{item.INSPN}},
        INSPV={{item.INSPV}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 PGW校验管理用户数据的源IP时，增加允许的IP地址。设置后，只允许特定IP的客户端能登录PGW。

##### 6.2.1 //DC1：

```jinja2
{%- if is_scenario_source_ip_check -%}
    {%- for item in add_provisionip_list -%}
        ADD PROVISIONIP:
        {#- --- 必选参数 --- -#}
        ADDRID={{item.ADDRID}},
        IPVER={{item.IPVER}},
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADDRNAME is not none -%}
            ADDRNAME="{{item.ADDRNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            {%- if item.IPV4MASK is not none -%}
                IPV4MASK="{{item.IPV4MASK}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_source_ip_check -%}
    {%- for item in mod_insp_list_1 -%}
        MOD INSP:
        {#- --- 必选参数 --- -#}
        INSPT={{item.INSPT}},
        INSPN={{item.INSPN}},
        INSPV={{item.INSPV}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 设置软参“营帐权限开关”、“TLS工作模式”。请根据局点规划设置。

```jinja2
{%- for item in mod_insp_list_3 -%}
    MOD INSP:
    {#- --- 必选参数 --- -#}
    INSPT={{item.INSPT}},
    INSPN={{item.INSPN}},
    INSPV={{item.INSPV}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INSPN=DRUIMDBS/DSUIMDBS/RLOADSWITCH/RCHANNELLOADSW/RLOADTIMEOUT/RLOADPACKETSIZE/LDRSOURCE/REVVFYSWT/FWDRTVFYSWT/REVRTVFYSWT/FWDVFYSWT/PRDFWDVFY/PRDREVVFY/PRDFWDRTVFY/PRDREVRTVFY/DRUFRWDVFYUNITNUM/DSUFRWDVFYUNITNUM/REVVFYUNITNUM/FWDRTVFYUNITNUM/PERIODVFYONLYCHECK/REDUNDANCYSWITCH/NOCONSISTWARINGNUM/UPGRADESTATUS/TIMEBACKUPFLAG/BACKUPHOUR/BACKUPMINUTE/GDRUIMDBS/IUDMSWT/RESTHTTPSAUTHSWITCH/HTTPPROVRIGHTSWITCH/PROVHTTPSAUTHSWITCH/HTTPSAUTHSWITCH/TLSMODE/USERTRANSSPEED/UIVFYSWT/PRDUIVFY/UIVFYUNITNUM/DMVFYSWT/LDAPSWITCH/REVRTVFYUNITNUM/REDUNAUTOTAKEOVER/TAKEOVERDELAY/JRVFYPRD/JRVFYUNITNUM/LICINFODSPCTRL/DATANOTIFYMODE/VFYDATARECORDFLAG/AUTORECOVERYFLAG/LENQUKVFYQUE/REDQUKVFYSPD/DYNUSERMEASURE/DYNMEASURESPEED/INNERQUKVFYSWT/LOCREPEVENT/DRUINNERREPQUEUESIZE/DELSUBDATASWT/SCANSUBDATASPEED/STATBUFFRESULTSIZE/PROVRIGHTSWITCH/RSPWITHOUTDESCSWITCH/SOAPENVSWITCH/NOTIFYGETLOCATIONPOLICY/LINKAGESWITCH/SERVICERIGHTSWITCH/VMSTORAGEFAULTRMSWITCH/BYPASSDRUSWITCH/OUTERQUKVFYSWT/VFYCOVERRECORDSWT/EMIGRATIONPERIOD/SPCFDIRRSTSWT/QUKVERIFYMODE/SPCFOPLOGWRITEFILESWT/DRUOUTERREPQUEUESIZE/DSUINNERREPQUEUESIZE/DSUOUTERREPQUEUESIZE/GDRUTHREADNUM/DRUTHREADNUM/DSUTHREADNUM/ROUTEMIGMSGSIZE/LICCUSTOMIZEDSWITCH/EXPMSGQLENGTH/IMDBWORKMODE/OBJECTSERIALIZEFLAG/STATICMEASURESPEED/DSUUSRCNTUPDTHD/AAMODESWITCH/TIMINGSUBSCRIPTIONUNITNUM/TIMINGSUBSCRIPTIONRESENDPERIOD/INCONSISTENTTHRESHOLD/EXPORTSPEED/GDATAEXPORTSPEED/RTMTNMODE/DELJUNKDATANUM/REMAINDATANUM/DRUDISPATCHMODE/DRUREPRSPW/DRUSYNCREPRSPW/Q922TASKDELAYTIME/DMAGLOBALREFRESHCYCLE/FLOWCTRLRSPSWITCH/MSGTIMEOUTTHRESHOLD/CLUSTERBALANCESWITCH/MASTERLDRCOMPRESS/EMGRSTMODE/DELJUNKDATACYCLE/IGNOREPREFIXCHECK/EXCOMLQUERYSPEED/EXCOMLUPDATESPEED/NETWORKMODE/DCIFWDMODE/OBJECTCOMPRESSMODE/ALLOWENDWITHFSWITCH/SELFSPACEBACKUP/THIRDSPACEBACKUP/UPDOWNTASKNUM/TIMEOUTTHIRDBKLOAD/TIMEOUTSELFBKLOAD/GROUTEVRFYSWT/THIRDCFGCHECKSWITCH/BROADCASTQUERYSTEP/BROADCASTUPDATESTEP/DSULOADSHAREMODE/BATCHROUTEUPDATEDELAYTIME/EXCEPTIONROUTEVERIFYSWITCH/BATCHREPLICATIONDELAYTIME/BATCHREPLICATIONMODE/TAKEOVERFORCLUSTER/EXPIRETIME/CLOUDADDSIDPOLICY/MCIRETURNIMMEDIATELY/FWDMMLERRCODESWT/USERTRANSBKPSWITCH/REDOARCHIVEDAYS/INCREDOSWITCH/DBPAGEVACUUMMODE/PSITEMSGSWITCH/LOCATIONVERIFYMODE/BKPFILEVRFSWT/KVDCISYNCTOUDB/BYPASSREVRTSYNSWITCH/LENQUKVFYQUEOFROUTE/GLBDATAPOLICY/LOCREPCHECKSWITCH/HLOADSWITCH/RPRESTORENUM/BROADCASTPOLICY/QFECTRSW/QBEPRESSPARA/KEYRESPROTECT/FEBEFLOWSW/PARTITIONFLOWSW/RCVUSERLISTNUM/RCVUSERSPEED/SYNFLOWPRESSPARA/MMLTLSAUTHSWITCH/LENQUKVFYQUEFORPARTITION/DTLSOVERSCTPSWT/NOTIFYMAPPING/MAXNODERECORDLIMIT/ACTIVELOCELECTSWT/MLOADBUFLEN/MLOADDELAYTIME/RLOADBUFLEN/RLOADDELAYTIME/GRDSYNCMODE/USERTRANSRECOVERSPEED/FABRICPROTECTSW/FABRICPROTECTFLOWPRESSPARA/FABRICPORTFLOWCTRTHRESHOLD/SDRFABRICPROTECTSW/SDRFABRICPORTFLOWCTRTHRESHOLD/SDRFABRICPORTFLOWCTREND/MIGRATEWATCHPERIOD/MAXBROADCASTNUM/MAXVRYNUMINPRIKEY/BRDCSTFLOWCTLDROPSWT/MAXINDEXBROADCASTNUM/SCTPRCVQUEUETHD/REDUNDANCYSYNFLOWCTRLSW/VERIFYCOMPATIBILITYSWT/FILEBKPENCSWT/COMFORMATOFEXPFILE/FILEUPLOADMODE/HETERJUDGESWITCH/MIGRATECTRLSWT/USERDATAMIGEXCEPENHANCESW/SCTPDELAYSYNFLOWCTRLSW/MSGPRIQUEUECOMBINESW/DSGLINKCFGCHKSWT/NONGLOBALROUTEMODESWT/SPECFICDSGSCTPSRVSWT/PARGLBDATAVFYSPD/BATCHQUERYLIMIT/BATCHMODIFYLIMIT/BUSINESSUSERLOCKTIMEOUT/BUSINESSUSERLOCKSWITCH/EXCOMLSHIELDSWITCH/SPCFTIMERSTSWT/MAXPAGEQUERYUSERDATANUM/UNIONEXPSPEED/ALMSUPPRESSIONSWT/ACCFILETIMEOUT/GDATANOCONSISTNUM/USERDATANOCONSISTNUM/SECIDXDEFVALSTORESWT/GLOBALDATANOTIFYSWITCH/DCIFORWARDINGSWT/FABRICPLANELOADBALANCESW/FABRICPLANEPRISETSW/VERIFYMERGESWT/LICFROZENBUFFERTIME/PSITEHEARTBEATSWITCH/PARTITIONFORWARDPOLICY/LOCUSERDIFFNUM/LOCGDATADIFFNUM/VERIFYPAUSETIME/CROSSREGIONMIGRATESPEED/CROSSREGIONRBKSPEED/DYNDATARBKSWITCH/USERTRANSSTATUS/SECONDMSGBYPASSDRU/LICRATEDISPSWITCH/GDATAMAXREQNUM/SOAPCONBATSWITCH/MULTINODEBRDCSTRTNUM/RLOADAUTOBATCHSWT/MAXRLOADTASKNUMPERIPU/UPGRADECOMPATIBILITYSWT/MULTIRANGECHECKSWITCH/N36NOTIFYSW/IMDBINSUFFICIENTTHD/REPIGNORESWT/VERIFYHASHALGORITHM/CMPDBSPEED/LIGHTSCHEDULSWT/BPTHREADDETACHSWT/SIMPLEDCIREPCOMPRSWT/PROVLOCREPMULTHREADSWT/ENABLEROARTINDEX/ROUTECONFLICTVFYMODE/GLOBALROUTEGENMODE/OBJREBUILDFRAGTHD/EXCOMLUSERQUERYSTEP/USERDATASYNCVSPSW/AUTOTAKEOVERFWDMODE/CDB_VRSP_R_RECONSTRUCTMODE/USERTRANSQRYSPEED/VERIFYENHANCEMODE/DRUUPGDPLANEACCSS/MAXRLOADTASKNUMPERDSG/VFYCYCPRD/DSUIMDBBALTHD/COUNTMERGESWT/STBYPDAPRTSW/DYNUSERMEASUREGROUP/LICENSEDEVIATION/ROUTEDRUREDOARCHIVEDAYS/USERTRANSLOCKSWT/PGWSNDDCIMSGPRIORITY/SCTPHASHALGO/DCIRSPCOMPRESSMODE/IPUPROTECTSW/IPUPROTECTTHD/IPUPROTECTENDTHD/IPURSPBANDWIDTH/DCIRSPCMPSTARTTHD/DCIRSPCMPCLOSETHD/LOCREPCOMPATIBILITYSWT/FVMODTSRECORDMODE 时必选 --- -#}
    {%- if item.INSPN in ['DRUIMDBS', 'DSUIMDBS', 'RLOADSWITCH', 'RCHANNELLOADSW', 'RLOADTIMEOUT', 'RLOADPACKETSIZE', 'LDRSOURCE', 'REVVFYSWT', 'FWDRTVFYSWT', 'REVRTVFYSWT', 'FWDVFYSWT', 'PRDFWDVFY', 'PRDREVVFY', 'PRDFWDRTVFY', 'PRDREVRTVFY', 'DRUFRWDVFYUNITNUM', 'DSUFRWDVFYUNITNUM', 'REVVFYUNITNUM', 'FWDRTVFYUNITNUM', 'PERIODVFYONLYCHECK', 'REDUNDANCYSWITCH', 'NOCONSISTWARINGNUM', 'UPGRADESTATUS', 'TIMEBACKUPFLAG', 'BACKUPHOUR', 'BACKUPMINUTE', 'GDRUIMDBS', 'IUDMSWT', 'RESTHTTPSAUTHSWITCH', 'HTTPPROVRIGHTSWITCH', 'PROVHTTPSAUTHSWITCH', 'HTTPSAUTHSWITCH', 'TLSMODE', 'USERTRANSSPEED', 'UIVFYSWT', 'PRDUIVFY', 'UIVFYUNITNUM', 'DMVFYSWT', 'LDAPSWITCH', 'REVRTVFYUNITNUM', 'REDUNAUTOTAKEOVER', 'TAKEOVERDELAY', 'JRVFYPRD', 'JRVFYUNITNUM', 'LICINFODSPCTRL', 'DATANOTIFYMODE', 'VFYDATARECORDFLAG', 'AUTORECOVERYFLAG', 'LENQUKVFYQUE', 'REDQUKVFYSPD', 'DYNUSERMEASURE', 'DYNMEASURESPEED', 'INNERQUKVFYSWT', 'LOCREPEVENT', 'DRUINNERREPQUEUESIZE', 'DELSUBDATASWT', 'SCANSUBDATASPEED', 'STATBUFFRESULTSIZE', 'PROVRIGHTSWITCH', 'RSPWITHOUTDESCSWITCH', 'SOAPENVSWITCH', 'NOTIFYGETLOCATIONPOLICY', 'LINKAGESWITCH', 'SERVICERIGHTSWITCH', 'VMSTORAGEFAULTRMSWITCH', 'BYPASSDRUSWITCH', 'OUTERQUKVFYSWT', 'VFYCOVERRECORDSWT', 'EMIGRATIONPERIOD', 'SPCFDIRRSTSWT', 'QUKVERIFYMODE', 'SPCFOPLOGWRITEFILESWT', 'DRUOUTERREPQUEUESIZE', 'DSUINNERREPQUEUESIZE', 'DSUOUTERREPQUEUESIZE', 'GDRUTHREADNUM', 'DRUTHREADNUM', 'DSUTHREADNUM', 'ROUTEMIGMSGSIZE', 'LICCUSTOMIZEDSWITCH', 'EXPMSGQLENGTH', 'IMDBWORKMODE', 'OBJECTSERIALIZEFLAG', 'STATICMEASURESPEED', 'DSUUSRCNTUPDTHD', 'AAMODESWITCH', 'TIMINGSUBSCRIPTIONUNITNUM', 'TIMINGSUBSCRIPTIONRESENDPERIOD', 'INCONSISTENTTHRESHOLD', 'EXPORTSPEED', 'GDATAEXPORTSPEED', 'RTMTNMODE', 'DELJUNKDATANUM', 'REMAINDATANUM', 'DRUDISPATCHMODE', 'DRUREPRSPW', 'DRUSYNCREPRSPW', 'Q922TASKDELAYTIME', 'DMAGLOBALREFRESHCYCLE', 'FLOWCTRLRSPSWITCH', 'MSGTIMEOUTTHRESHOLD', 'CLUSTERBALANCESWITCH', 'MASTERLDRCOMPRESS', 'EMGRSTMODE', 'DELJUNKDATACYCLE', 'IGNOREPREFIXCHECK', 'EXCOMLQUERYSPEED', 'EXCOMLUPDATESPEED', 'NETWORKMODE', 'DCIFWDMODE', 'OBJECTCOMPRESSMODE', 'ALLOWENDWITHFSWITCH', 'SELFSPACEBACKUP', 'THIRDSPACEBACKUP', 'UPDOWNTASKNUM', 'TIMEOUTTHIRDBKLOAD', 'TIMEOUTSELFBKLOAD', 'GROUTEVRFYSWT', 'THIRDCFGCHECKSWITCH', 'BROADCASTQUERYSTEP', 'BROADCASTUPDATESTEP', 'DSULOADSHAREMODE', 'BATCHROUTEUPDATEDELAYTIME', 'EXCEPTIONROUTEVERIFYSWITCH', 'BATCHREPLICATIONDELAYTIME', 'BATCHREPLICATIONMODE', 'TAKEOVERFORCLUSTER', 'EXPIRETIME', 'CLOUDADDSIDPOLICY', 'MCIRETURNIMMEDIATELY', 'FWDMMLERRCODESWT', 'USERTRANSBKPSWITCH', 'REDOARCHIVEDAYS', 'INCREDOSWITCH', 'DBPAGEVACUUMMODE', 'PSITEMSGSWITCH', 'LOCATIONVERIFYMODE', 'BKPFILEVRFSWT', 'KVDCISYNCTOUDB', 'BYPASSREVRTSYNSWITCH', 'LENQUKVFYQUEOFROUTE', 'GLBDATAPOLICY', 'LOCREPCHECKSWITCH', 'HLOADSWITCH', 'RPRESTORENUM', 'BROADCASTPOLICY', 'QFECTRSW', 'QBEPRESSPARA', 'KEYRESPROTECT', 'FEBEFLOWSW', 'PARTITIONFLOWSW', 'RCVUSERLISTNUM', 'RCVUSERSPEED', 'SYNFLOWPRESSPARA', 'MMLTLSAUTHSWITCH', 'LENQUKVFYQUEFORPARTITION', 'DTLSOVERSCTPSWT', 'NOTIFYMAPPING', 'MAXNODERECORDLIMIT', 'ACTIVELOCELECTSWT', 'MLOADBUFLEN', 'MLOADDELAYTIME', 'RLOADBUFLEN', 'RLOADDELAYTIME', 'GRDSYNCMODE', 'USERTRANSRECOVERSPEED', 'FABRICPROTECTSW', 'FABRICPROTECTFLOWPRESSPARA', 'FABRICPORTFLOWCTRTHRESHOLD', 'SDRFABRICPROTECTSW', 'SDRFABRICPORTFLOWCTRTHRESHOLD', 'SDRFABRICPORTFLOWCTREND', 'MIGRATEWATCHPERIOD', 'MAXBROADCASTNUM', 'MAXVRYNUMINPRIKEY', 'BRDCSTFLOWCTLDROPSWT', 'MAXINDEXBROADCASTNUM', 'SCTPRCVQUEUETHD', 'REDUNDANCYSYNFLOWCTRLSW', 'VERIFYCOMPATIBILITYSWT', 'FILEBKPENCSWT', 'COMFORMATOFEXPFILE', 'FILEUPLOADMODE', 'HETERJUDGESWITCH', 'MIGRATECTRLSWT', 'USERDATAMIGEXCEPENHANCESW', 'SCTPDELAYSYNFLOWCTRLSW', 'MSGPRIQUEUECOMBINESW', 'DSGLINKCFGCHKSWT', 'NONGLOBALROUTEMODESWT', 'SPECFICDSGSCTPSRVSWT', 'PARGLBDATAVFYSPD', 'BATCHQUERYLIMIT', 'BATCHMODIFYLIMIT', 'BUSINESSUSERLOCKTIMEOUT', 'BUSINESSUSERLOCKSWITCH', 'EXCOMLSHIELDSWITCH', 'SPCFTIMERSTSWT', 'MAXPAGEQUERYUSERDATANUM', 'UNIONEXPSPEED', 'ALMSUPPRESSIONSWT', 'ACCFILETIMEOUT', 'GDATANOCONSISTNUM', 'USERDATANOCONSISTNUM', 'SECIDXDEFVALSTORESWT', 'GLOBALDATANOTIFYSWITCH', 'DCIFORWARDINGSWT', 'FABRICPLANELOADBALANCESW', 'FABRICPLANEPRISETSW', 'VERIFYMERGESWT', 'LICFROZENBUFFERTIME', 'PSITEHEARTBEATSWITCH', 'PARTITIONFORWARDPOLICY', 'LOCUSERDIFFNUM', 'LOCGDATADIFFNUM', 'VERIFYPAUSETIME', 'CROSSREGIONMIGRATESPEED', 'CROSSREGIONRBKSPEED', 'DYNDATARBKSWITCH', 'USERTRANSSTATUS', 'SECONDMSGBYPASSDRU', 'LICRATEDISPSWITCH', 'GDATAMAXREQNUM', 'SOAPCONBATSWITCH', 'MULTINODEBRDCSTRTNUM', 'RLOADAUTOBATCHSWT', 'MAXRLOADTASKNUMPERIPU', 'UPGRADECOMPATIBILITYSWT', 'MULTIRANGECHECKSWITCH', 'N36NOTIFYSW', 'IMDBINSUFFICIENTTHD', 'REPIGNORESWT', 'VERIFYHASHALGORITHM', 'CMPDBSPEED', 'LIGHTSCHEDULSWT', 'BPTHREADDETACHSWT', 'SIMPLEDCIREPCOMPRSWT', 'PROVLOCREPMULTHREADSWT', 'ENABLEROARTINDEX', 'ROUTECONFLICTVFYMODE', 'GLOBALROUTEGENMODE', 'OBJREBUILDFRAGTHD', 'EXCOMLUSERQUERYSTEP', 'USERDATASYNCVSPSW', 'AUTOTAKEOVERFWDMODE', 'CDB_VRSP_R_RECONSTRUCTMODE', 'USERTRANSQRYSPEED', 'VERIFYENHANCEMODE', 'DRUUPGDPLANEACCSS', 'MAXRLOADTASKNUMPERDSG', 'VFYCYCPRD', 'DSUIMDBBALTHD', 'COUNTMERGESWT', 'STBYPDAPRTSW', 'DYNUSERMEASUREGROUP', 'LICENSEDEVIATION', 'ROUTEDRUREDOARCHIVEDAYS', 'USERTRANSLOCKSWT', 'PGWSNDDCIMSGPRIORITY', 'SCTPHASHALGO', 'DCIRSPCOMPRESSMODE', 'IPUPROTECTSW', 'IPUPROTECTTHD', 'IPUPROTECTENDTHD', 'IPURSPBANDWIDTH', 'DCIRSPCMPSTARTTHD', 'DCIRSPCMPCLOSETHD', 'LOCREPCOMPATIBILITYSWT', 'FVMODTSRECORDMODE'] -%}
        FETYPEN="{{item.FETYPEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 重启PGW模块。

### 重启PGW模块的操作需要在登录PGW Web LMT之前进行，否则PGW Web LMT界面的Service Management MML导航树显示为空。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MID={{item.MID}},
    MT={{item.MT}},
    ;
{%- endfor -%}
```

### 9 登录PGW Web LMT MML命令界面。

### 详细操作请参见登录与退出PGW Web LMT。

### 10 增加BOSS账号，用于BOSS登录设备进行业务发放。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_opr_list的变量区（command: ADD OPR） -#}
<!-- MISSING_MACRO: command=ADD OPR list_name=add_opr_list step_id=10 -->
```

