---
id: ''
name: 配置UDM和USCDB对接配置
ne_type: UEG
type: feature
description: 开局时，配置UDM与USCDB的对接数据。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置UDM","配置UDM和USCDB对接配置"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST INSP')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置UDM与USCDB的对接数据。

## 必备事项
前提条件

已经完成UDM、USCDB的基础数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_groupswitch_list:
      type: items
      properties:
        GROUPNAME:
          name: '分组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPSWITCH:
          name: '开关'
          type: string
          enum:
          - OPEN
          - CLOSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rlocation_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '表示远端Location标识，可在UDM侧使用**LST DBSLOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载对应的网元插件包之后才能在此处进行设置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级值'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: 'UEG间FE和BE不交叉互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDUNFLAG:
          name: '是否容灾关系'
          type: string
          enum:
          - No
          - Yes
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rdsg_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端UDM网元中先定义，然后在本端网元通过**ADD RLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '**配置UDM基础数据**页面中，命令**ADD DBSSERVICENO**定义，对应参数“SERVICENO”的取值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载UDM插件后在此引用。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: 'USCDB与UDM中的DBS对接。'
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_ripaddr_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端UDM网元中先定义，然后在本端网元通过**ADD RLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端DPU模块号/远端IP的VPN索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端UDM网元由**ADD DBSIPADDR**先定义。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端UDM网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端UDM网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RDPUST:
          name: '远端IP地址业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载UDM插件后在此引用。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_notifycfg_list:
      type: items
      properties:
        FETYPE:
          name: '订阅通知的FE类型'
          type: string
          maxLength: 128
          required: true
          description: '固定配置为HSS9860。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        REMOTEID:
          name: '订阅通知对端的ID'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FEID:
          name: 'FE标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: '取值范围内不允许重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INFTYPE:
          name: '订阅通知的接口类型'
          type: string
          enum:
          - MCI
          - SOAP
          - FILE
          - THIRDPARTY
          required: true
          description: '在此场景下固定配置为“MCI”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SYNCHROSWITCH:
          name: '同步开关'
          type: string
          enum:
          - ASYNC
          - SYNC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONID:
          name: '订阅通知发送的Location标识'
          type: integer
          minimum: 0
          maximum: 512
          required: false
          description: '表示远端Location标识，可在UDM侧使用**LST DBSLOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
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
    set_dbsgrpswitch_list:
      type: items
      properties:
        GROUPNAME:
          name: '分组名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPSWITCH:
          name: '开关'
          type: string
          enum:
          - OPEN
          - CLOSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dbsrlocation_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '表示远端Location标识，可在USCDB侧使用**LST LOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          enum:
          - USCDB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: 'UEG间FE和BE不交叉互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsrdsg_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，然后在本端网元通过**ADD DBSRLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '可登录“USCDB MML命令”界面，执行“**LST MODULE: MT=DSG;**”查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'UDM（FE）与USCDB对接时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsripaddr_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，然后在本端网元通过**ADD DBSRLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端业务IP的索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端USCDB网元由**ADD SRVIPADDR**先定义（“SRVINDEX”参数值）。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
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
    act_ipdisp_list:
      type: items
      properties: {}
    act_dbsipdisp_list:
      type: items
      properties: {}
  examples:
    set_groupswitch_list:
    - GROUPNAME: 'UPCF'
      GROUPSWITCH: OPEN
    add_rlocation_list:
    - RLOCID: 13
      RMT: 'HSS9860'
      LP: 1
      REDUNFLAG: No
    add_rdsg_list:
    - RLOCID: 13
      RDSGMID: 301
      RDSGST: 'HSS9860'
      RDSGTYPE: DBS
    add_ripaddr_list:
    - RLOCID: 13
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.200.200.22'
      IPV4IP2: '10.200.200.23'
      RDPUST: 'HSS9860'
    add_notifycfg_list:
    - FETYPE: 'HSS9860'
      REMOTEID: 1
      FEID: 1
      INFTYPE: MCI
      SYNCHROSWITCH: ASYNC
      LOCATIONID: 13
      IPVER: ''
    mod_insp_list:
    - INSPT: FE
      INSPN: NOTIFYMAPPING
      INSPV: 1
      FETYPEN: 'HSS9860'
    set_dbsgrpswitch_list:
    - GROUPNAME: 'UPCF'
      GROUPSWITCH: OPEN
    add_dbsrlocation_list:
    - RLOCID: 14
      RMT: USCDB
      LP: 1
    add_dbsrdsg_list:
    - RLOCID: 14
      RDSGMID: 17
      RDSGST: 'HSS9860'
    add_dbsripaddr_list:
    - RLOCID: 14
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.200.200.32'
      IPV4IP2: '10.200.200.33'
    mod_insp_list_1:
    - INSPT: HSS9860
      INSPN: BECONNECTMODE
      INSPV: 1
    act_ipdisp_list:
    - {}
    act_dbsipdisp_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 设置分组开关。

```jinja2
{%- for item in set_groupswitch_list -%}
    SET GROUPSWITCH:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    GROUPSWITCH={{item.GROUPSWITCH}},
    ;
{%- endfor -%}
```

### 3 增加远端Location信息。

```jinja2
{%- for item in add_rlocation_list -%}
    ADD RLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT="{{item.RMT}}",
    LP={{item.LP}},
    REDUNFLAG={{item.REDUNFLAG}},
    ;
{%- endfor -%}
```

### 4 增加远端DBS。

### 参数“RDSGMID”通过在“UEG MML命令”下使用“LST DBSSERVICENO:;”查询。

```jinja2
{%- for item in add_rdsg_list -%}
    ADD RDSG:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RDSGMID={{item.RDSGMID}},
    RDSGST="{{item.RDSGST}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RDSGTYPE is not none -%}
        RDSGTYPE={{item.RDSGTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加远端网元IP地址。

```jinja2
{%- for item in add_ripaddr_list -%}
    ADD RIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    RDPUST="{{item.RDPUST}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加PGW订阅通知配置。操作员通过PGW修改全局数据或用户数据后，PGW负责通知FE相关的修改内容。

```jinja2
{%- for item in add_notifycfg_list -%}
    ADD NOTIFYCFG:
    {#- --- 必选参数 --- -#}
    FETYPE="{{item.FETYPE}}",
    FEID={{item.FEID}},
    INFTYPE={{item.INFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.REMOTEID is not none -%}
        REMOTEID={{item.REMOTEID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4/IPV6 时可选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI/THIRDPARTY 时可选 --- -#}
    {%- elif item.INFTYPE in ['MCI', 'THIRDPARTY'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI 时可选 --- -#}
    {%- if item.INFTYPE == 'MCI' -%}
        {%- if item.LOCATIONID is not none -%}
            LOCATIONID={{item.LOCATIONID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置软参。

#### 7.1 检查如下软参的参数值是否为“1”。

#### 是，请执行8。

#### 否，请执行7.b。

#### 7.2 将如下软参的参数值设置为“1”。

```jinja2
{%- set LST_INSP=getParameterValue('LST INSP') -%}
{%- if not LST_INSP -%}
    {%- for item in mod_insp_list -%}
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
{%- endif -%}
```

### 8 登录“UEG MML命令”界面。

### 9 设置DBS分组开关。

```jinja2
{%- for item in set_dbsgrpswitch_list -%}
    SET DBSGRPSWITCH:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    GROUPSWITCH={{item.GROUPSWITCH}},
    ;
{%- endfor -%}
```

### 10 增加远端Location信息。

```jinja2
{%- for item in add_dbsrlocation_list -%}
    ADD DBSRLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT={{item.RMT}},
    LP={{item.LP}},
    ;
{%- endfor -%}
```

### 11 增加远端DSG。

### 在“MML-USCDB”下使用“LST MODULE: MT=DSG;”查询参数“RDSGMID”的值，需要将查询出来的所有DSG模块号配置在此处。如下以查询到DSG模块号为17和18为例。

```jinja2
{%- for item in add_dbsrdsg_list -%}
    ADD DBSRDSG:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RDSGMID={{item.RDSGMID}},
    {#- --- 可选参数 --- -#}
    {%- if item.RDSGST is not none -%}
        RDSGST="{{item.RDSGST}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 增加远端网元IP地址。

```jinja2
{%- for item in add_dbsripaddr_list -%}
    ADD DBSRIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 配置软参。

#### 13.1 检查如下软参的参数值是否为“1”。

#### 是，请执行14。

#### 否，请执行13.b。

#### 13.2 将如下软参的参数值设置为“1”。

```jinja2
{%- if not LST_INSP -%}
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

### 14 登录“USCDB MML命令”界面。执行如下命令，激活IP链路。

```jinja2
{%- if LST_INSP=='1' -%}
    ACT IPDISP:
    ;
{%- endif -%}
```

### 15 登录“UEG MML命令”界面。执行如下命令，激活IP链路。

```jinja2
ACT DBSIPDISP:
;
```

