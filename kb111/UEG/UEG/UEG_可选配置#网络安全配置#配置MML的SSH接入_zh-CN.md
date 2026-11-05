---
id: ''
name: 配置MML的SSH接入
ne_type: UEG
type: feature
description: 当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置PGW MML的SSH接入安全策略。  传统的网络服务程序，如：FTP在网络上用明文传送口令和数据，这些口令和数据很容易被第三方非法截获并冒充真正的服务器进行收发数据。因此出于安全的考虑，需要在配置PGW MML的SSH接入安全策略。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置MML的SSH接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置PGW MML的SSH接入安全策略。传统的网络服务程序，如：FTP在网络上用明文传送口令和数据，这些口令和数据很容易被第三方非法截获并冒充真正的服务器进行收发数据。因此出于安全的考虑，需要在配置PGW MML的SSH接入安全策略。

## 必备事项
前提条件

向系统管理员获取OM Portal的帐号的密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_pgwsshuser_list:
      type: items
      properties:
        USERNAME:
          name: '用户名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWD:
          name: '新密码'
          type: string
          maxLength: 30
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          maxLength: 30
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: 'PGW服务端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '用户描述'
          type: string
          maxLength: 64
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
  examples:
    add_pgwsshuser_list:
    - USERNAME: '用户名'
      PWD: '新密码'
      CFM: '确认密码'
      PORT: PGW服务端口
      DESCRIPTION: '用户描述'
    mod_insp_list:
    - INSPT: PGW
      INSPN: PGWMMLSWITCH
      INSPV: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**ADD PGWSSHUSER**命令增加PGW SSH用户。

```jinja2
{%- for item in add_pgwsshuser_list -%}
    ADD PGWSSHUSER:
    {#- --- 必选参数 --- -#}
    USERNAME="{{item.USERNAME}}",
    PWD="{{item.PWD}}",
    CFM="{{item.CFM}}",
    PORT={{item.PORT}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### “PGW服务端口”可以通过**LST PORT**命令查询，使用“端口类型”为“PORT\_FOR\_PROV”，“端口子类型”为“PORT\_FOR\_MML”对应的端口作为“PGW服务端口”。

### 当SSH客户端完成SSH鉴权后，需要发送PGW的登录鉴权指令**LGI**鉴权成功，才能执行后续PGW命令。

### 3 执行**MOD INSP**命令将软参“PGWMMLSWITCH”修改“0”，禁止客户端通过MML接入PGW。

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

