---
id: ''
name: 配置PGW HTTPS数字证书
ne_type: UEG
type: feature
description: 用户使用浏览器首次使用HTTPS认证方式登录PGW Web LMT或DMS WebUI之前需要加载HTTPS证书文件。业务发放系统和PGW服务端之间使用HTTPS协议进行通信时使用SOAP、MML或REST类型的HTTPS证书文件；客户端（PGW Web LMT或DMS WebUI）和PGW服务端之间使用HTTPS协议进行通信时使用WEBLMT类型的HTTPS证书文件。  * 安装USCDB网元时已不再默认加载华为证书文件，客户需要自行申请并部署商用证书文件。当仅用于系统调测时，如果客户无法申请到证书文件，请联系华为技术工程师获取。 * 长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置PGW HTTPS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户使用浏览器首次使用HTTPS认证方式登录PGW Web LMT或DMS WebUI之前需要加载HTTPS证书文件。业务发放系统和PGW服务端之间使用HTTPS协议进行通信时使用SOAP、MML或REST类型的HTTPS证书文件；客户端（PGW Web LMT或DMS WebUI）和PGW服务端之间使用HTTPS协议进行通信时使用WEBLMT类型的HTTPS证书文件。* 安装USCDB网元时已不再默认加载华为证书文件，客户需要自行申请并部署商用证书文件。当仅用于系统调测时，如果客户无法申请到证书文件，请联系华为技术工程师获取。* 长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。

## 必备事项
前提条件

客户已申请证书文件并已获取对应的证书密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_port_list:
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
          - PORT_FOR_REST
          - PORT_FOR_HTTP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lod_verif_list:
      type: items
      properties:
        VERIFID:
          name: '证书ID'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USTYPE:
          name: '用途类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFTYPE:
          name: '证书类型'
          type: string
          enum:
          - ROOTVERIF
          - CAVERIF
          - DEVVERIF
          - KEYFILE
          - CRLF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPKGNAME:
          name: '证书文件包名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VNAME:
          name: '证书文件名'
          type: string
          maxLength: 128
          required: true
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
    add_port_list_1:
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
          - PORT_FOR_REST
          - PORT_FOR_HTTP
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
    mod_insp_list_2:
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
    rst_module_list:
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
  examples:
    add_port_list:
    - PORTNO: ''
      PORTTYPE: ''
      PORTTYPENAME: ''
    lod_verif_list:
    - VERIFID: ''
      USTYPE: ''
      VERIFTYPE: ''
      VPKGNAME: ''
      VNAME: ''
    mod_insp_list:
    - INSPT: ''
      INSPN: ''
      INSPV: ''
    add_port_list_1:
    - PORTNO: ''
      PORTTYPE: ''
      PORTTYPENAME: ''
    mod_port_list:
    - PORTNO: ''
      PORTTYPE: ''
      PORTTYPENAME: ''
    mod_insp_list_1:
    - INSPT: ''
      INSPN: ''
      INSPV: ''
    mod_insp_list_2:
    - INSPT: ''
      INSPN: ''
      INSPV: ''
    rst_module_list:
    - MID: ''
      MT: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal界面。

### 2 进入“系统 > 文件传输”页面。

### 3 在左侧“文件传输”菜单中选择“CGPLite文件 > 网元文件”。

### 4 单击“添加文件”，选择需要上传的证书文件并上传。

### **图1** 上传证书文件

### 5 登录“USCDB MML命令”界面。

### 6 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为SOAP、MML或REST端口。

```jinja2
{%- for item in add_port_list -%}
    ADD PORT:
    {#- --- 必选参数 --- -#}
    PORTTYPE={{item.PORTTYPE}},
    PORTTYPENAME={{item.PORTTYPENAME}},
    PORTNO={{item.PORTNO}},
    ;
{%- endfor -%}
```

### 加载SOAP、MML或REST类型的证书时需要执行该操作。

### 如果是加载USCDB的默认端口的证书，则可跳过此步骤。端口相关信息可参考PGW端口配置管理中的“表1 端口类型和协议关系表”。

### “SUP-FE”仅为示例，此处请以实际的FE类型为准。

### 7 执行**LOD VERIF**命令分别加载CA证书、设备证书和密钥文件。

```jinja2
{%- for item in lod_verif_list -%}
    LOD VERIF:
    {#- --- 必选参数 --- -#}
    VERIFTYPE={{item.VERIFTYPE}},
    USTYPE={{item.USTYPE}},
    VNAME="{{item.VNAME}}",
    VERIFID={{item.VERIFID}},
    VPKGNAME="{{item.VPKGNAME}}",
    ;
{%- endfor -%}
```

### 8 根据加载证书的端口类型不同，需要做如下操作：

#### 8.1 加载SOAP类型的证书，需要执行**MOD INSP**命令设置如下软件参数。

```jinja2
{%- if is_scenario_soap_cert -%}
    {%- for item in mod_insp_list -%}
        MOD INSP:
        {#- --- 必选参数 --- -#}
        INSPN={{item.INSPN}},
        INSPV={{item.INSPV}},
        INSPT={{item.INSPT}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 8.1.1 “PROVRIGHTSWITCH（营帐权限开关）”设置为“1”。

##### 8.1.2 “TLSMODE（TLS工作模式）”设置为“3”。

##### 8.1.3 “HTTPSAUTHSWITCH（HTTPS鉴权开关）”为“0”

#### 8.2 加载MML类型的证书，需要执行**ADD PORT**/**MOD PORT**命令设置参数“端口子类型”为“PORT\_FOR\_MML” 且“是否使用HTTPS”为“YES”，执行**MOD INSP**命令设置“MMLTLSAUTHSWITCH（MML TLS鉴权开关）”为“0”。

```jinja2
{%- if is_scenario_mml_cert -%}
    {%- for item in add_port_list_1 -%}
        ADD PORT:
        {#- --- 必选参数 --- -#}
        PORTTYPE={{item.PORTTYPE}},
        PORTTYPENAME={{item.PORTTYPENAME}},
        PORTNO={{item.PORTNO}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_mml_cert -%}
    {%- for item in mod_port_list -%}
        MOD PORT:
        {#- --- 必选参数 --- -#}
        PORTTYPE={{item.PORTTYPE}},
        PORTTYPENAME={{item.PORTTYPENAME}},
        PORTNO={{item.PORTNO}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_mml_cert -%}
    {%- for item in mod_insp_list_1 -%}
        MOD INSP:
        {#- --- 必选参数 --- -#}
        INSPN={{item.INSPN}},
        INSPV={{item.INSPV}},
        INSPT={{item.INSPT}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.3 加载WEBLMT类型的证书，需要执行**MOD INSP**命令设置软件参数“WEBLMTHTTPSSWITCH（weblmt https控制开关）”为“1”。

```jinja2
{%- if is_scenario_weblmt_cert -%}
    {%- for item in mod_insp_list_2 -%}
        MOD INSP:
        {#- --- 必选参数 --- -#}
        INSPN={{item.INSPN}},
        INSPV={{item.INSPV}},
        INSPT={{item.INSPT}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 执行**RST MODULE**命令重启PGW进程使配置生效。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MT={{item.MT}},
    MID={{item.MID}},
    ;
{%- endfor -%}
```

### 如果加载的是WEBLMT类型的证书，需要重启所有PGW模块、所有DMA模块、网关类型为PGW的DPU模块和DMA类型的DPU模块。

