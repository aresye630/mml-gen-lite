# 查询MAP业务(LST MAPSERV)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询MAP业务参数的设置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询MAP业务参数的设置信息：

```
LST MAPSERV:;
```

```
%%LST MAPSERV:;%%
RETCODE = 0 SUCCESS0001:Operation is successful

                      CFNRTIME = 30
                MAXTIMECALLFWD = 1
                    DEFAULTARP = NORMAL
                      USSD_BAR = PLMN-SS-D
                    ALERTSCREP = 3
                  FWDAREALIMIT = NORESTRICTION
                NUMSTRUCTLIMIT = NORESTRICTION
                        MAPVER = GSMPHASE3
                      CMCCSUPP = PHASE1
                 PLMNSPECSSENE = OBJECT
                     VP_BSCODE = 0X17_BS20
               MAXTIMEFORPUSSD = 600
               MAXTIMEFORUSSDN = 360
               MAXTIMEFORUSSDR = 360
            TEMPTABLECLEARTIME = 1
                    SRISM-PSCB = NORESTRICTION
                       GPRSLCK = CancelLocation
               MAXTIMEOFRESEND = 1
 CANCELLOCATIONMAXTIMEOFRESEND = 1
                     STRUCTURE = UNSTRUCTURE
                   SPC_LEN_IND = 14 Bits
                     NUM_SCMSG = 10
            MAXUSSDSESSIONTIME = 0
                  PLMNSS_STATE = 000000|000000
        ERRCODEFORROAMRESTRICT = RoamingNotAllowed
     ERRCODEFORFIRSTUPDATEFAIL = SuccessDbFailNetAndResendOnce
         ODBOC_SWITCH_FOR_OCSI = ODBBAOCAndODBSS
DELETEORCANCELWHENCAMEL2RMVOCSI
                               = DELETESUBDATA
              RECVSMS_AF_ODBIC = RETURNCALLBARRING
                   CRBT_PLMNSS = 0
                CFNRYDELAYTIME = 0
                      CBPASSWD = EEEE
                      AUTHSTEP = 101
              AUTH_MILENAGE_C1 = 00000000000000000000000000000000
              AUTH_MILENAGE_C2 = 00000000000000000000000000000001
              AUTH_MILENAGE_C3 = 00000000000000000000000000000002
              AUTH_MILENAGE_C4 = 00000000000000000000000000000004
              AUTH_MILENAGE_C5 = 00000000000000000000000000000008
              AUTH_MILENAGE_R1 = 40
              AUTH_MILENAGE_R2 = 00
              AUTH_MILENAGE_R3 = 20
              AUTH_MILENAGE_R4 = 40
              AUTH_MILENAGE_R5 = 60
                 CUSTOMAUTH_C1 = 00000000000000000000000000000000
                 CUSTOMAUTH_C2 = 00000000000000000000000000000001
                 CUSTOMAUTH_C3 = 00000000000000000000000000000002
                 CUSTOMAUTH_C4 = 00000000000000000000000000000004
                 CUSTOMAUTH_C5 = 00000000000000000000000000000008
                 CUSTOMAUTH_R1 = 40
                 CUSTOMAUTH_R2 = 00
                 CUSTOMAUTH_R3 = 20
                 CUSTOMAUTH_R4 = 40
                 CUSTOMAUTH_R5 = 60
        PRN_IMSI_TO_MSISDN_IND = NORMAL
                   PUSSDOPTION = NONE
                   LENGTHOFNDC = 2
                   FMUSSDTIMES = 1
                   VGCSVBSCODE = DELETE_PLMNSS
                   GPRSMANAGER = NotSupportGPRSManager
                      SPECMSRN = 000000000000000
                   RESERVE_LOC = NONE
                      TRANSFER = UC_TRANSFER
                    PREFERROAM = NotSupport
                 RESTRICTTIMES = 1
ERRCODE_FOR_PREFERROAM_ALLOWED = SystemFailure
ERRCODE_FOR_PREFERROAM_RESTRICTED
                               = RoamingNotAllowed_PLMNNotAllowed
                     MRBT_TYPE = NO_SUPP_MRBT
                   MRBT_PLMNSS = PLMN-SS-DEF
                     CUGFORMAT = Original
              DSACCESSOVERTIME = 5
                     SCCP_TYPE = ALWAYS_1
                     UPL_TIMER = 0
               SRI_WAITERTIMER = 0
                     NTBT_TYPE = NRBT
               SEGMENT_CONTROL = SegmentControlOff
          SRI_RSP_SEGMENT_SIZE = 150
               AUTH_TRIPLETSET = 0
                       ARDAREA = DOMESTIC
                 MAXACTCCBSNUM = 5000
                   SMS_ROUTING = NotSupport
                    ACR_PLMNSS = NotSupport
           FILTERSMSRETURNCODE = UnexpectedDataValue
                UNFLOWUSSDCODE = FFFFFFFFFFFFFFFF
                GSMBCFORSRIRSP = IgnoreMode
                STRUCTURE_BS30 = DEFAULT
                  OLCM_CONTROL = 0
                  BWT_UPL_TIME = 0
                     ODBSSLOCK = NONE
                       DEF_COU = OPERATOR
                      RESETWPA = MODCBCOUANDMODBARPWD
                RELAY_MSG_TYPE = NO_RELAY
              RELAY_MSG_METHOD = AUC
                ODBPOS_REJ_ULR = NO_REJECT
            SRIFORSPECFOLLOWME = NOSUPP
                    ISDOSKMAP2 = DELETE_PLMNSS
              RETURNALLVECTORS = 0
            VECTORNUMNOSEGMENT = 0
           ERRCODEFORHPLMNROAM = 0
                   DSDECATMAP2 = DELETE_PLMNSS
                MAXCHANGEDISDN = 1000
             ALERTSC_DELAYTIME = 0
                  PERIOD_OFCFR = 0
                    PERIOD_AUC = 0
                       NUM_AUC = 50
                    PERIOD_UPL = 0
                       NUM_UPL = 50
                  PERIOD_REGCF = 0
                     NUM_REGCF = 20
            PERIOD_REG_INTERCF = 0
               NUM_REG_INTERCF = 10
                  VSGSN_ADDRES = 10.0.0.0
                  EGR_AUTHMODE = SELF
                   ANCHOR_TYPE = NOANCHOR
                    QUERY_TADS = REALTIME
                 MSIM_PA_VALUE = 1
                 MSIM_SA_VALUE = 0
                     ICSPLMNSS = NONE
              MAPVERFORALERTSC = MAPVERCFG
                    ADD_SER_GT = 000000000000000
                      CSSQNIND = 0
                      PSSQNIND = 1
                     LTESQNIND = 16
                     IMSSQNIND = 2
                     AAASQNIND = 17
                     BSFSQNIND = 3
                       UDCDSSN = 0
                  CAMELMANAGER = Template
             SPECUSSDCODE_TYPE = InFront
             UPPER_LIMIT_HLRSN = 0
                   GMLCADDRISD = GMLCADDRISD_FIVE
                   NAM_FOR_EPS = SGSN
           REPORTSM_CHECK_TIME = 0
              PURGE_CHECK_TIME = 0
          NOT_REACH_REASON_FLG = MSPURGED
                    SRISPECIAL = NONEPROCESS
                RESTORECONTROL = DontUpdate
          SENDPARAMETERCONTROL = NoneProcess
              MAXEXTBRDWLLIMIT = UNLIMITED
                 LTEAUTOSUBTPL = 65535
                       UEAPNOI = #
                      UEAPNOI2 = #
                    DEFAULTAPN = FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                     EPSQOSTPL = 65535
                     ARPHVALUE = 5
                     ARPMVALUE = 10
                    PNP_PLMNSS = 0
                 ERRCODEFORSAA = DIAMETER_ERROR_USER_NO_NON_3GPP_SUBSCRIPTON
      MULTISIM_USSD_MSISDN_IND = Individual_MSISDN
                SSET_WITH_OCSI = NOT_SUPPORT
                 INVALID_K2SNO = 0
           VOLTEAUTOOPTGPRSTPL = 0
            VOLTEAUTOAMBRMAXUL = 1
            VOLTEAUTOAMBRMAXDL = 1
                 VOLTEAUTORIID = 0
            VOLTEAUTOPLMNTPLID = 65535
            VOLTEAUTODIAMTPLID = 65535
               VOLTEAUTOTIMER1 = 5
               VOLTEAUTOTIMER2 = 5
                 TCPADDTIMEOUT = 0
                    LTEAUTOQCI = 5
              DEFAULT_NET_TYPE = NON_VoLTE
                 SRIRSPWITHBSC = Default
       REGFTN_FOR_GROUPSIMUSER = NOT_SUP_SAME_GRPSIM
             USSDOPERATIONTYPE = DonebyPrimary
                   AUTOPROVNUM = 1
                   AUTOPROVCYC = 5
             AUTOPROVNOTIFYNUM = 1
            AUTOPROVNOTIFYTIME = 28
                EPS_ODBPB_SUPP = ALL_NOT_ALLOWED
                     IDPMSGSSN = 0
               LENOFMSISDNPACK = 0
         CAMELROAMTPL_FOR_TCSI = TCSI_SUPPRESS
          APN_STORAGE_COMPRESS = NotSupport
 UNIDXED_APN_RECORDS_THRESHOLD = 0
         EPS_AUTH_PROTOCOL_VER = R11
               CANCELTYPEVALUE = subscriptionWithdraw
            FTN_NCS_MATCH_RULE = ALL_MATCH_FTN
      LTE_AUTOPROV_QUERY_TIMES = 5
                     SRI_ETCSI = ReturnAbsent
                     DEFAPNTPL = 65535
                  EOICKPROCESS = DEFAULT
                  LTENOTIFMODE = MODE1
                      OFI_MODE = DEFAULT
   CHECK_NON_3GPP_ACCESS_RIGHT = NOT_CHECK
                EPC_CHECK_IMEI = NotCheck
        EPC_UPL_FAILED_NO_IMEI = S6aS6d_Ignore_IMEI_Check
               M2M_NOTIFY_MODE = MODE1
                   PLMN_POLICY = S6a_S6d_SwxIdr
                    SMSCF_MODE = MODE1
               OCMN_SPECFU_PRE = 0
                 EPSODBCONTROL = ODBPOS
                RETRIEVE_EOCSI = ReturnError
                     ACTIVENUM = 1
                     ACTIVECYC = 5
              ULR_CLR_SGSN_NUM = ALL_CLEAR
                 AUTSAMFFTFLAG = RETRY_CONFIG_AMF
                   ADDWAITTIME = 0
        CONTROLOFQUINTUPLETNUM = 0
            CHECKLCSCAPABILITY = ALLCHECK
            PRIORITY_FOR_ETCSI = ETCSI
                      WSMCFLAG = NONE
            VOLTEERRCODEFORUDA = UNABLE_TO_COMPLY
              CONTROLPSODBROAM = ODBROAM
                LTENOTIF_HLRSN = NOT_CARRY
                   ADD_CC_TYPE = TYPE1
               ACR_EXTEND_PROC = ACR_ALONE
                 LOCINFOVLRNUM = FROMPSI
                   ETCSINOSEND = FALSE
                       ALSTYPE = ALSTYPE1
               RESEND_LIST_NUM = 20000
                 RESEND_PERIOD = 30
                   RESEND_RATE = 10
                  RESEND_TIMES = 48
               VOWIFI_AUTOPROV = NOT_SUPPORT
CAMEL_INDICATOR_SUPPRESS_ETCSI = NOT_SUPPRESS
          ENHANCE_UCSI_MANAGER = Template
    PUSSD_DESTREFERENCE_FORMAT = IMSI_WITH_PREFIX96
                SOAPREPORTSORT = NONE
                     SRIBWADDR = ReturnMsrn
       FIRST_ALERTSC_DELAYTIME = 0
               AUTOPROVWAITNUM = 500
                CFD_INTER_ROAM = LOCALCROSSINTER
UDR_PRN_TIMER_SUPPORT_PREPAGING
                               = 14
UDR_PRN_TIMER_NOT_SUPPORT_PREPAGING
                               = 6
                SH_RETURN_CSRN = NONE
     ERRCODE_FOR_VOLTEFORBIDSS = ILLEGAL_SS_OPERATION
  CHECK_BORO_CFU_CONFLICT_RULE = CHECK
         SRI_SENDEOCSI_CONTROL = SEND_EOCSI
         SRI_SENDEOICK_CONTROL = NOT_SEND_EOICK
              USSD_CODE_SCHEME = MODE1
                  AUTHCHECKNAM = NOT_CHECK_NAM
              NUMBERRIGHTCHECK = HLRSN_NUMBER
                    VSAREATYPE = VSAREA_NUMBER_TYPE
                 REATTACH_SUPP = NONE
               RETRIEVE_VLRNUM = ReturnErr
         BWT_UPL_REPORTSM_TIME = 0
                     CCBS_TYPE = PRIVATE
               CCBS_RETAIN_SUP = NONE
                CCBS_T11_TIMER = 20
                CCBS_T12_TIMER = 20
                 CCBS_T3_TIMER = 45
                 CCBS_T7_TIMER = 45
                 CCBS_T8_TIMER = 15
                 CCBS_T9_TIMER = 55
             HLRA_CCBS_MAX_NUM = 3
             HLRB_CCBS_MAX_NUM = 3
          CCBS_STATUS_REF_TIME = 60
          MAXIMSINUMOFMULTISIM = 9
             SUPPABNORMALCAMEL = RETURNERR
           DEFAPN_CONVERT_RULE = DELETE
  REG_FTN_ODB_VALID_IN_SERREST = NONE
               ATSI_RETURN_BSG = MODE1
  CHECK_CALLINGGT_SAME_DYNDATA = NOT_CHECK_CALLINGGT_SAME_DYNDATA
VOLTEAUTO_CHECK_IMS_VOICE_OVER_PS
                               = NOT_CHECK
          CHECK_SS_RESTRICT_CF = CHECK
               LFTN_ISD_UNSUPP = Prefix15
               LFTN_SRI_UNSUPP = Prefix15
              LFTN_ATSI_UNSUPP = Prefix15
          MIGRAE_SRI_ATI_TIMER = 0
            MIGRAE_SRI_ATI_SNI = 0
               SUPPTHOTBILLING = NOTSUPPORT
          RESERVE_ABNORMAL_LOC = BOTH
           SRI_PSI_WAITERTIMER = 0
VOLTE_MSIM_PARALLEL_QUERY_ENHANCE
                               = NOT_SUPPORT
                  PUSSD_VLRNUM = SUB_DYN_DATA
                    CF_ODBBAOC = FORBID
               EPSLCKOPTGPRSID = 65535
        UPL_UPDATE_CHK_FOR_DAP = CHK_VLR_UPLTIME_FOR_DAP
                UPL_UPDATE_CHK = NOT_CHK
            GPRSUPL_UPDATE_CHK = NOT_CHK
             CHECK_LOCK_FORLCS = CHECK
                 HORLCF_FORMAT = FIR
                   UPL_CDR_FMT = SOAP
            ULR_ROAM_REST_RULE = CLEAR
P_CSCF_RESTORE_WITH_EMPTY_SUBSCRIPTION
                               = NOTEMPTY
                  AUC_INTERVAL = 10
                  AUC_MAXTIMES = 4
   CATEGORY_MNP_CANCELLOCATION = 0
                     NGCSQNIND = 18
          PREFIX_ANCHOR_FORMAT = CC_PREFIX_ISDN
   FORBID_AUXILIARY_SM_CONTROL = ForbidAuxiliarySmControlOff
                RESEND_VERSION = PHASE1
                SHORTNUM_TRANS = NoRule
                  ADD_SOAP_FMT = DEFAULT
                       NPMSCID = 000000000000000
          USSD_RCV_END_PROCESS = RETURN_CONTINUE
                EPCRESTRICTION = NOT_RESTRICTION
                     DEFRTINFO = 0
          NRBT_ANCHOR_PRIORITY = NRBT_PRIORITY
        EPSLCKOPTGPRSID_FOR_4G = 65535
    ERRCAUSE_FOR_BROHPLMNCGPRS = 0
                  AES_MODE_SAE = CBC
               AES_IV_MODE_IMS = ENHANCED
  EXTERNAL_AUC_CALLING_GT_MODE = INTROFF
   EXTERNAL_AUC_CALLED_GT_MODE = IMSIRTINFO
      CMCC_SOAPDISPLAY_VERSION = V1
             SUBTREE_QUERY_OPT = SUPPORT_BROADCAST
                      DEFKEYID = 0
                 VSRR_CHK_MODE = MODE1
         ERRCAUSE_FOR_BROHPLMN = 0
          CS_UPL_TIMEOUT_TIMER = 20
          PS_UPL_TIMEOUT_TIMER = 20
     OPERATIONCODETAG_CHK_MODE = CHK_RETURN_REJECT
     LST_CMD_EXP_FILE_COMPRESS = 2048
                      CHRG_HND = CHRG_HND_MODE_CLEAR_GCC
               OP_ENCRYPT_MODE = ENHANCED
        VPLMNID_FOR_SWXIDR_LBO = MME/S4SGSN
              SBP_CHK_VMS_MODE = ALL_CF
           ODBPOSNONSUPDSDTIME = 0
         AUTOPROV_CONTENT_TYPE =  text/xml;
      AUTOPROV_CONTENT_SUBTYPE =  charset="utf-8"
       TRANS_SUB_REATTACH_SUPP = UPDATE_PROCEDURE
         RMV_SUB_REATTACH_SUPP = NONE
        SUB_SENSINFO_SHOW_MODE = NONANONYMOUS
    PSI_TIMER_SUPPORT_PREAGING = 20
PSI_TIMER_NOT_SUPPORT_PREAGING = 20
SRI_PRN_TIMER_SUPPORT_PREAGING = 20
SRI_PRN_TIMER_NOT_SUPPORT_PREAGING
                               = 20
    IDR_TIMER_SUPPORT_PREAGING = 14
IDR_TIMER_NOT_SUPPORT_PREAGING = 6
UDR_PSI_TIMER_SUPPORT_PREAGING = 14
UDR_PSI_TIMER_NOT_SUPPORT_PREAGING
                               = 6
    ERRCODE_FOR_PREFERROAM_EPC = ROAMNTALD
                    CBPWD_MODE = NORMAL
            DS_BROADCAST_TIMER = 5
                   LENGTHOFCGI = 7
            FORCEUPDATEDNPINFO = FORCE_UPDATE_BY_NPDATA_TIMESTAMP
  VOLTE_PARALLEL_QUERY_ENHANCE = NOT_SUPPORT
                   NSAAUTOPROV = FALSE
                   AMBRPROCESS = DEFAULT
       CMCC_SOAPDISPLAY_FORMAT = DEFAULT
            REPDATA_SYNC_SUPP = FALSE
             VOLTEREGSNDCANCEL = NotSupportSndCancel
         ERRCODEFORCHKRESTORE = UABORT
                  ISKEEPDYNAPN = KEEP_IMS_APN
   ERRCODEFORPSIMSNOTREACHABLE = NetworkDeterminedNotReachable
           CNRESTRICTIONFORAAA = 1
CHECK_IMSCACHE_REPOSITSEQ_IN_UDR_PUR
                               = FALSE 
               UDREPSINFOCHECK = CHECK
VOLTEDEREGISTERTOIDRSTNSRVALUE = 999999999999999
               EPCSXZWPLMNRRID = 1
               EPCSXZWDIAMRRID = 1
         UDR_PRN_ASNUMBER_CTRL = 0
               EPC_CHK_5GS_IWK = CHECK
          NR_REDCAP_TYPE_TO_AS = NR
                LTENSAAUTOPROV = NOT_SUPPORT
               NSAAUTOAMBRNRUL = 0
               NSAAUTOAMBRNRDL = 0
            ENHANCE_PURGE_TIME = 14400
               DETACHCSCTLFUNC = 0
                    SRISM-CSCB = NORESTRICTION
           PUSSDSENDCGIANDIMEI = RELAY
              LOCEMPTYUDALOGIC = 0
           ODBRCF_RULE_CONTORL = DEFAULT_RULE
                  DETACHIMSCTL = REREGISTER
               DETACHREGIONCTL = ALLOWPLMNLIST
              OPTGPRS_APNTPLID = 65535
          OPTGPRS_APN_SUB_CTRL = FALSE
               SS_SERVICE_CTRL = 3
          RSPWITHLOCINFO_PURGE = 0
"ISD"
                     PLMN-SS-1 = FALSE
                     PLMN-SS-2 = FALSE
                     PLMN-SS-3 = FALSE
                     PLMN-SS-4 = FALSE
                     PLMN-SS-5 = FALSE
                     PLMN-SS-6 = FALSE
                     PLMN-SS-7 = FALSE
                     PLMN-SS-8 = FALSE
                     PLMN-SS-9 = FALSE
                     PLMN-SS-A = FALSE
                     PLMN-SS-B = FALSE
                     PLMN-SS-C = FALSE
                     PLMN-SS-D = FALSE
                     PLMN-SS-E = FALSE
                     PLMN-SS-F = FALSE

"SRI_MSRN"
                     PLMN-SS-1 = FALSE
                     PLMN-SS-2 = FALSE
                     PLMN-SS-3 = FALSE
                     PLMN-SS-4 = FALSE
                     PLMN-SS-5 = FALSE
                     PLMN-SS-6 = FALSE
                     PLMN-SS-7 = FALSE
                     PLMN-SS-8 = FALSE
                     PLMN-SS-9 = FALSE
                     PLMN-SS-A = FALSE
                     PLMN-SS-B = FALSE
                     PLMN-SS-C = FALSE
                     PLMN-SS-D = FALSE
                     PLMN-SS-E = FALSE
                     PLMN-SS-F = FALSE
                    ALLPLMN-SS = FALSE

"SRI_MSRNCF"
                     PLMN-SS-1 = FALSE
                     PLMN-SS-2 = FALSE
                     PLMN-SS-3 = FALSE
                     PLMN-SS-4 = FALSE
                     PLMN-SS-5 = FALSE
                     PLMN-SS-6 = FALSE
                     PLMN-SS-7 = FALSE
                     PLMN-SS-8 = FALSE
                     PLMN-SS-9 = FALSE
                     PLMN-SS-A = FALSE
                     PLMN-SS-B = FALSE
                     PLMN-SS-C = FALSE
                     PLMN-SS-D = FALSE
                     PLMN-SS-E = FALSE
                     PLMN-SS-F = FALSE

"SRI"
                     PLMN-SS-1 = FALSE
                     PLMN-SS-2 = FALSE
                     PLMN-SS-3 = FALSE
                     PLMN-SS-4 = FALSE
                     PLMN-SS-5 = FALSE
                     PLMN-SS-6 = FALSE
                     PLMN-SS-7 = FALSE
                     PLMN-SS-8 = FALSE
                     PLMN-SS-9 = FALSE
                     PLMN-SS-A = FALSE
                     PLMN-SS-B = FALSE
                     PLMN-SS-C = FALSE
                     PLMN-SS-D = FALSE
                     PLMN-SS-E = FALSE
                     PLMN-SS-F = FALSE

"BS20TOBS2X"
                          BS21 = FALSE
                          BS22 = FALSE
                          BS23 = FALSE
                          BS24 = FALSE
                          BS25 = FALSE
                          BS26 = FALSE

"BS30TOBS3X"
                          BS31 = FALSE
                          BS32 = FALSE
                          BS33 = FALSE
                          BS34 = FALSE

"VIDEO_MRBT"
                     PLMN-SS-1 = FALSE
                     PLMN-SS-2 = FALSE
                     PLMN-SS-3 = FALSE
                     PLMN-SS-4 = FALSE
                     PLMN-SS-5 = FALSE
                     PLMN-SS-6 = FALSE
                     PLMN-SS-7 = FALSE
                     PLMN-SS-8 = FALSE
                     PLMN-SS-9 = FALSE
                     PLMN-SS-A = FALSE
                     PLMN-SS-B = FALSE
                     PLMN-SS-C = FALSE
                     PLMN-SS-D = FALSE
                     PLMN-SS-E = FALSE
                     PLMN-SS-F = FALSE
                    ALLPLMN-SS = FALSE

"SUPPRESSTSBS"
                          TS11 = FALSE
                          TS12 = FALSE
                          TS21 = FALSE
                          TS22 = FALSE
                          TS61 = FALSE
                          TS62 = FALSE
                          BS20 = FALSE
                          BS21 = FALSE
                          BS22 = FALSE
                          BS23 = FALSE
                          BS24 = FALSE
                          BS25 = FALSE
                          BS26 = FALSE
                          BS30 = FALSE
                          BS31 = FALSE
                          BS32 = FALSE
                          BS33 = FALSE
                          BS34 = FALSE
                          BS41 = FALSE
                          BS42 = FALSE
                          BS43 = FALSE
                          BS44 = FALSE
                          BS45 = FALSE
                          BS46 = FALSE
                          BS51 = FALSE
                          BS52 = FALSE
                          BS53 = FALSE
                          BS61 = FALSE
                          BS81 = FALSE

"RESEND_SWITCH"
                        CS_ISD = FALSE
                        CS_DSD = FALSE
                        CS_CLR = FALSE
                        PS_ISD = FALSE
                        PS_DSD = FALSE
                        PS_CLR = FALSE
                       S6a_IDR = FALSE
                       S6a_CLR = FALSE
                       S6d_IDR = FALSE
                       S6d_CLR = FALSE
                          UDCD = FALSE

"LSTSUBPARADISPLAY"
           HIDEODBENTEINFOROAM = FALSE
          HIDECSPS-MSISDN-LESS = FALSE
             HIDECSPSUPLSTATUS = FALSE

"ADDMMLSUPP"
                          IMSI = FALSE
                        MSISDN = FALSE
                           CSI = FALSE

"TDR"
           MAP_UPDATE_LOCATION = FALSE
      MAP_UPDATE_GPRS_LOCATION = FALSE
           MAP_CANCEL_LOCATION = FALSE
  MAP_SEND_AUTHENTICATION_INFO = FALSE
                       S6A_ULR = FALSE
                       S6A_CLR = FALSE
                       S6A_AIR = FALSE

"SINGLEUSERMOVERULE"
  IMSI_CHANGE_MOVE_NEWIMSI_PID = FALSE
      IMSI_CHANGE_MOVE_DISABLE = FALSE
   IMS_ADDNEWPI_MOVE_NEWPI_PID = FALSE
   IMS_ADDNEWPI_MOVE_OLDPI_PID = FALSE
       NSA_ADDSUB_MOVE_IMSIPID = FALSE
       NSA_ADDSUB_MOVE_ISDNPID = FALSE
       NSA_ADDSUB_MOVE_USERPID = FALSE
NSA_ADDSUB_MOVE_SRCPIDS2DESTPIDS
                               = FALSE
        SA_ADDSUB_MOVE_IMSIPID = FALSE
        SA_ADDSUB_MOVE_ISDNPID = FALSE
SA_ADDSUB_MOVE_SRCPIDS2DESTPIDS
                               = FALSE

Total count = 511

There is together 1 report

---    END
```

## 输出结果说明

请参见**SET MAPSERV**命令的参数说明。