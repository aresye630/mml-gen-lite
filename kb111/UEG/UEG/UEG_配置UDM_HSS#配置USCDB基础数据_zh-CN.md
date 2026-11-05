---
id: ''
name: 配置USCDB基础数据
ne_type: UEG
type: feature
description: 开局时，配置USCDB基础数据。  UDM从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：  * FE（Front End）网元也称为UDM/HSS网元，实现UDM/HSS功能实体的功能，包括协议处理、业务处理以及数据管理。 * BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。    UDM/HSS部署在园区网络时，园区UDM/HSS支持开户，用户数据的增加、删除和更新通过业务发放系统或在PGW本地（在PGW Web LMT上执行MML批操作文件）进行业务发放。在一个UDR（USCDB）上进行开户，该UDR（USCDB）会将用户数据自动备份到另一个UDR（USCDB）。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置UDM/HSS","配置USCDB基础数据"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST MODULE')
- getParameterValue('LST LOCATION')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置USCDB基础数据。UDM从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：* FE（Front End）网元也称为UDM/HSS网元，实现UDM/HSS功能实体的功能，包括协议处理、业务处理以及数据管理。* BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。  UDM/HSS部署在园区网络时，园区UDM/HSS支持开户，用户数据的增加、删除和更新通过业务发放系统或在PGW本地（在PGW Web LMT上执行MML批操作文件）进行业务发放。在一个UDR（USCDB）上进行开户，该UDR（USCDB）会将用户数据自动备份到另一个UDR（USCDB）。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    str_instenv_list:
      type: items
      properties:
        ENVTYPE:
          name: '安装环境类型'
          type: string
          enum:
          - LocalDisk
          - FESQL
          - SINGLEDB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_module_list:
      type: items
      properties:
        MID:
          name: '模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        SERVICETYPE:
          name: '业务类型'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VMNAME1:
          name: '主用Pod名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VMNAME2:
          name: '备用Pod名称'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名称'
          type: string
          maxLength: 32
          required: false
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
          description: '用于指定业务IP类型。   * DSG类型用于和UDM/HSS对接。 * PGW类型用于业务发放及访问PGW Web LMT。IP1用于连接业务发放系统，IP2用于连接PGW Web LMT。 * DMA类型IP必须配置，否则DPU模块异常。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '业务IP地址。  双DC场景，两个DC的业务IP地址不能重复，如DC1用样例值，DC2用10.201.200.32等。'
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
        SERVICETYPE:
          name: '业务类型'
          type: string
          maxLength: 128
          required: false
          description: '用于定义待增加模块的业务类型，即对应的插件包类型。当“SRVIPTYPE”设置为“DSG”时，业务类型配置为HSS9860。'
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
    act_feplug_list:
      type: items
      properties:
        FETYPENAME:
          name: 'FE类型名称'
          type: string
          maxLength: 128
          required: true
          description: '用于启用FE插件。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    str_initdata_list:
      type: items
      properties:
        SERVICETYPE:
          name: '业务类型'
          type: string
          maxLength: 128
          required: true
          description: '分别对USCDB及HSS9860进行内存数据库初始化。'
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
    mod_port_list:
      type: items
      properties:
        PORTNO:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPE:
          name: '端口类型'
          type: string
          enum:
          - PORT_FOR_WEBLMT
          - PORT_FOR_PROV
          - PORT_FOR_DMSWEB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPENAME:
          name: '端口子类型'
          type: string
          enum:
          - PORT_FOR_CLIENT
          - PORT_FOR_LMT_MML
          - PORT_FOR_SOAP
          - PORT_FOR_MML
          - PORT_FOR_REDIRECT
          - PORT_FOR_DMSWEB
          - PORT_FOR_REST
          - PORT_FOR_HTTP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISABLEPORT:
          name: '是否屏蔽本端口'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTBUSSTYPE:
          name: '端口业务类型'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_mdutype_list:
      type: items
      properties:
        MEID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '模块类型'
          type: string
          maxLength: 200
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HAST:
          name: '主备状态'
          type: string
          enum:
          - STANDBY
          - ACTIVE
          - ALL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
  examples:
    str_instenv_list:
    - ENVTYPE: LocalDisk
    add_module_list:
    - MID: 3
      MT: DPU
      SERVICETYPE: 'USCDB'
      VMNAME1: 'usdid3aservice14-0'
      VMNAME2: 'usdid3bservice14-0'
      MNAME: 'DPU3'
    add_srvipaddr_list:
    - SRVINDEX: 1
      SRVIPTYPE: DSG
      IPVER: IPV4
      IP1VPNNAME: 'VRF_DATA'
      IPV4IP1: '10.200.200.32'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_DATA'
      IPV4IP2: '10.200.200.33'
      IPV4MASK2: '255.255.255.255'
      SERVICETYPE: 'HSS9860'
      DPUMID: 3
    - SRVINDEX: 1
      SRVIPTYPE: DSG
      IPVER: IPV4
      IP1VPNNAME: 'VRF_DATA'
      IPV4IP1: '10.201.200.32'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_DATA'
      IPV4IP2: '10.201.200.33'
      IPV4MASK2: '255.255.255.255'
      SERVICETYPE: 'HSS9860'
      DPUMID: 3
    act_feplug_list:
    - FETYPENAME: 'HSS9860'
    str_initdata_list:
    - SERVICETYPE: 'USCDB'
    mod_insp_list:
    - INSPT: PGW
      INSPN: GRANTIPSWITCH
      INSPV: 0
    mod_port_list:
    - PORTNO: 7776
      PORTTYPE: PORT_FOR_PROV
      PORTTYPENAME: PORT_FOR_MML
      DISABLEPORT: NO
      PORTBUSSTYPE: 'USCDB'
    rst_mdutype_list:
    - MEID: 14
      DESC: 'pgw'
      HAST: ALL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 虚机容器场景下，设置物理数据库的安装环境类型为“LocalDisk”。裸机容器不需要执行该步骤。

```jinja2
{%- for item in str_instenv_list -%}
    STR INSTENV:
    {#- --- 必选参数 --- -#}
    ENVTYPE={{item.ENVTYPE}},
    ;
{%- endfor -%}
```

### 3 执行**LST MODULE**命令查询DPU模块号。

### 查看是否存在模块类型为DPU，业务类型为USCDB的模块：

### 存在=>5

### 不存在=>4。

### 4 执行**ADD MODULE**命令添加DPU模块。

### 参数“VMNAME1”与参数“VMNAME2”通过**LST PODINFO**命令查询，采用应用类型为USDID3的Pod名称。

### “MID”不能与已存在的模块号重复。

```jinja2
{%- set LST_MODULE=getParameterValue('LST MODULE') -%}
{%- if LST_MODULE=='' -%}
    {%- for item in add_module_list -%}
        ADD MODULE:
        {#- --- 必选参数 --- -#}
        MID={{item.MID}},
        MT={{item.MT}},
        VMNAME1="{{item.VMNAME1}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MNAME is not none -%}
            MNAME="{{item.MNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MT=DPU/DSG 时必选 --- -#}
        {%- if item.MT in ['DPU', 'DSG'] -%}
            SERVICETYPE="{{item.SERVICETYPE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MT=DPU/NDF/PGW 时可选 --- -#}
        {%- if item.MT in ['DPU', 'NDF', 'PGW'] -%}
            {%- if item.VMNAME2 is not none -%}
                VMNAME2="{{item.VMNAME2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
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
    {#- --- 条件必选：IPVER=IPV4/IPV6 时必选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        IP1VPNNAME="{{item.IP1VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件必选：SRVIPTYPE=DSG 时必选 --- -#}
    {%- if item.SRVIPTYPE == 'DSG' -%}
        SERVICETYPE="{{item.SERVICETYPE}}",
    {%- endif -%}
    {#- --- 条件必选：SRVIPTYPE=PGW/DMA 时必选 --- -#}
    {%- if item.SRVIPTYPE in ['PGW', 'DMA'] -%}
        DPUMID={{item.DPUMID}},
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

### 6 检查Location标识是否与规划一致。

### 执行**LST LOCATION**命令，检查“LOCID”参数值是否与规划一致。

### 主用局UDM/HSS、主用局USCDB、容灾局UDM/HSS、容灾局USCDB的Location标识各不相同。

### 一致，请执行7。

### 不一致，请联系华为技术支持工程师处理。

#### 6.1 //DC1：

#### RETCODE = 0  操作成功

#### 操作结果如下

#### ------------

#### Location标识  =  14

#### 网元类型  =  USCDB

#### (结果个数 = 1)

#### ---    END

#### 6.2 RETCODE = 0  操作成功

#### 操作结果如下

#### ------------

#### Location标识  =  16

#### 网元类型  =  USCDB

#### (结果个数 = 1)

#### ---    END

### 7 激活插件包。

```jinja2
{%- set LST_LOCATION=getParameterValue('LST LOCATION') -%}
{%- if LST_LOCATION -%}
    {%- for item in act_feplug_list -%}
        ACT FEPLUG:
        {#- --- 必选参数 --- -#}
        FETYPENAME="{{item.FETYPENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 执行7后，至少等待10s，然后再执行8。

### 8 初始化数据库。

### 执行如下命令，会清除内存数据库数据，请在华为技术支持人员指导下使用。

```jinja2
{%- for item in str_initdata_list -%}
    STR INITDATA:
    {#- --- 必选参数 --- -#}
    SERVICETYPE="{{item.SERVICETYPE}}",
    ;
{%- endfor -%}
```

### 9 设置软参“IP限制开关”。请根据局点规划设置。

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

### 10 修改PGW业务消息侦听端口。如不修改，则使用默认端口。

```jinja2
{%- for item in mod_port_list -%}
    MOD PORT:
    {#- --- 必选参数 --- -#}
    PORTNO={{item.PORTNO}},
    PORTTYPE={{item.PORTTYPE}},
    PORTTYPENAME={{item.PORTTYPENAME}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时必选 --- -#}
    {%- if item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
        PORTBUSSTYPE="{{item.PORTBUSSTYPE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PORTTYPENAME=PORT_FOR_LMT_MML/PORT_FOR_CLIENT 时可选 --- -#}
    {%- if item.PORTTYPENAME in ['PORT_FOR_LMT_MML', 'PORT_FOR_CLIENT'] -%}
        {%- if item.DISABLEPORT is not none -%}
            DISABLEPORT={{item.DISABLEPORT}},
        {%- endif -%}
    {#- --- 条件可选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时可选 --- -#}
    {%- elif item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
        {%- if item.DISABLEPORT is not none -%}
            DISABLEPORT={{item.DISABLEPORT}},
        {%- endif -%}
    {#- --- 条件可选：PORTTYPENAME=PORT_FOR_DMSWEB 时可选 --- -#}
    {%- elif item.PORTTYPENAME == 'PORT_FOR_DMSWEB' -%}
        {%- if item.DISABLEPORT is not none -%}
            DISABLEPORT={{item.DISABLEPORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 登录“CSP MML命令”界面。

### 12 执行**RST MDUTYPE**命令重启PGW模块。

```jinja2
{%- for item in rst_mdutype_list -%}
    RST MDUTYPE:
    {#- --- 必选参数 --- -#}
    MEID={{item.MEID}},
    DESC="{{item.DESC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HAST is not none -%}
        HAST={{item.HAST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 重启PGW模块的操作需要在登录PGW Web LMT之前进行，否则PGW Web LMT界面的Service Management MML导航树显示为空。登录PGW Web LMT的详细操作，请参见登录与退出PGW Web LMT。

