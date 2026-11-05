# 查询全局数据状态(DSP GDATAREFRESH)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询某个CCU或ACF模块的全局数据状态。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                         |
|:-------|:-------|:-----------------------------------------------------------------------------|
| MID    | 模块号    | 用于请求系统显示指定CCU或ACF模块的全局数据状态。模块号必须先通过ADD MODULE命令配置才能在此处引用。 取值范围：1～1023 默认值：无。 |

## 使用实例

查询全局数据状态，“模块号”参数为“30”。

```
DSP GDATAREFRESH: MID=30;
```

```
%%DSP GDATAREFRESH: MID=30;%%
RETCODE = 0  操作成功

查询结果如下
------------
 表名称                          数据加载源  数据加载结果  数据加载时间         数据刷新源  数据刷新结果  数据刷新时间         强制刷新标记

 W_G_APN_TPL                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_AMF_DATA                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_BCALIAS_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_BWADDRESS_DATA              0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_BWFTN_DATA                  0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CALLEDNUM_ANALYSIS          0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CSIR_LIST                   0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CAMELROAM_LIST              0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CAMELROAM_TPL               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CAMELINTER_LIST             0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_CAMELINTER_TPL              0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_DOMESTICAREA_DATA           0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_DCSI_DATA                   0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_DCSI_TPL                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_FORBIDFWD_NUM               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_FTNTRANS_DATA               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_FTN_NCS_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_FM_COR_DATA                 0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_GLOBALDATA_STATUSINFO       0           成功          2024-08-16 21:20:52  0           成功          2024-08-17 08:21:55  否          
 W_G_GLOBAL_DATA                 0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_GPRSCSI_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_GPRSCSI_TPL                 0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_GPRS_DATA                   0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_GPRS_TPL                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_HLRRR_DF_LIST               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_HLRRR_LIST                  0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_HLR_ATTR                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_IMSICODE_DATA               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_INTAREA_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_INTRA_OFFICE                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_ISDNCODE_DATA               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_K4_DATA                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_LCSGMLC_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_LCSMOLR_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_LCSPRIVACY_DATA             0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_LCS_TPL                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_MCSI_TPL                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_MTSMSCSI_TPL                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_MTSMSCSI_DATA               0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_NCC_DATA                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OCSI_DATA                   0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OCSI_TPL                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OFA_DATA                    0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OFA_TPL                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OP_DATA                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OPTGPRS_TPL                 0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_OPTGPRS_DATA                0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_QOS_TPL                     0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_RRTPL_DATA                  0           成功          2024-08-16 21:20:52  NULL        NULL          NULL                 NULL        
 W_G_RRTPL_CC_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RRTPL_NDC_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSNTYPE_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SMSCSI_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SKTYPE_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SMSCSI_TPL                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SSCSI_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SERVICE_ENTITY_LIST         0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSN_TPL                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSN_LIST                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SERVICE_LIST                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SERVICE_PRN_LIST            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_TCSI_DATA                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_TCSI_TPL                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_UCSI_DATA                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_UCSI_TPL                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_UNSUPP_ODB_OPTIONS          0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_USER_CHANGED_MSISDN         0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_USSD_DATA                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VBS_GROUPID_DATA            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VBS_GROUPID_TPL             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VGCS_GROUPID_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VGCS_GROUPID_TPL            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLR_TPL                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLR_LIST                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLRTYPE_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VTCSI_DATA                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VTCSI_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OKSC_TPL                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ERRRULE_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ADSUADDR_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_EIN_CFG_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SHORTNUM_MAP_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CSITPL_PREFIX_DATA          0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CAMEL_CAPABILITY_TPL        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_NONPORT_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SMSROUTE_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_IMSIRTINFO                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SERRESTRICT_TPL             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SERRESTRICT_LIST            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SCPTPL_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SCPTPL_CAMELPHS_DATA        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SCPTPL_PLMN_DATA            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RSI_TPL                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RSI_LIST                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ODBSS_RANGE                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_USSDSTRING                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_FRAUD_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PLMN_DATA                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PLMNVSNO_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PLMNIMSI_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SHORTCODE_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_K2_DATA                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_K7INDEX_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VERIFY_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_TAI_DATA                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_TAIZCLIST_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PRIVATEKEY_DATA             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VPLMN_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VPLMNTPL_MCC_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VPLMNTPL_MNC_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_APNQOSTPLINFO               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_DIAMNODE_TPL                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_DIAMNODE_LIST               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ISDNRTINFO                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_IP_SM_GW_ROUTE              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MGCF_IMRN_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_LUCSI_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_LUCSI_DATA                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PEER_ENTITY_TYPE            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CSG_TPL                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CSG_DATA                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PSAPNQOS_TPL                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_FM_AUTHRANGE_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRINFO_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRPREFIX_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRGROUP_DATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_APNOI_TPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SCPTPL_VLR_DATA             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_REDUNDANCY_DETECT           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OCMNVLR                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OCMNISDN                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SKALLOW_TPL                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SKALLOW_LIST                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MAPADDRRES_TPL              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MAPADDRRES_DATA             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_DIAMSERVICE_ENTITY_LIST     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_DIAMSERVICE_LIST            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SMFWDPLAT_LIST              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_EPSAPNQOS_TPL               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_EPSUSER_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OSNNUM_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_LTEAUTO_FORBID_PREFIX_DATA  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_APNREST_TPL                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_IMSIADD_LIST                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_APNREST_DATA                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CALLING_CAMEL               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_NUMBER_COUNTRYCODE_DATA     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRINFO_DATA_TPL            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRGROUP_DATA_TPL           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ETCSIREST_TPL               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ETCSIREST_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_QOSREP_LIST                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_QOSREP_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ETCSI_CONVER_TPL            0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ETCSI_CONVER_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_NTUCSI_TPL                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_NTUCSI_TPL_DATA             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CAMELRESSK_TPL              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CAMELRESSK_SK_TYPE          0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CAMELRESSK_SK_DATA          0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ISDN_GT_TPL                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ISDN_GT_LIST                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RESFTN_DATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_ANUMBLST                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLRAREA_TPL                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLRAREA_LIST                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSNAREA_TPL                0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSNAREA_LIST               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VLRROAMRESTRICT_LIST        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SGSNROAMRESTRICT_LIST       0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MIGRATION_FNRCFG_TPL        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MIGRATION_FNRCFG_DATA       0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_VERIFY_EXT_DATA             0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_DEFEPSQOSREP_DATA           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_EPSQOSREP_LIST              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_EPSQOSREP_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RKCFG_DATA                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_MKCFG_DATA                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_WKCFG_DATA                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CCEPS                       0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_GLOBALDIAMRR_LIST           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_GLOBALVPLMN_MCC_DATA        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_GLOBALVPLMN_MNC_DATA        0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_PSAPNEPS                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SOAPFORMAT                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_OPRPLMNID_DATA              0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_LTEAUTO_FORBID_IMEI_PREFIX  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_SPRTINFO                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CSIREPTPL                   0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_CSIREPTPL_VLRTPL_DATA       0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_RDUCHECK_INFO               0           成功          2024-08-16 21:20:53  0           成功          2024-08-16 21:21:14  否          
 W_G_R8TRACEDATA                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_IMS_TRACEDATA               0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 W_G_REPDATA_SYNC_RULE           0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLK4DATA                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLAMFDATA                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLOPDATA                     0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLCHRGTPL                    0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLAKAINFOTPL                 0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLVNTPL                      0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLVNTPLADDR                  0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLNATPL                      0           成功          2024-08-16 21:20:53  NULL        NULL          NULL                 NULL        
 H_TBLNATPLADDR                  0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLOCSITPL                    0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLOCSITDPTPL                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLTCSITPL                    0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLTCSITDPTPL                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLWPUINFO                    0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLSIFCTPLINFO                0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLSYSTEMPARA                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_CF_FTN_SIP_POSTFIX            0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_REPDATABLKLIST                0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLIMPIRTINFO                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLIMPURTINFO                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLASID                       0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 H_TBLK2DATA                     0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_GLOBAL_DATA                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_FORBIDAREA_TPL              0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        

仍有后续报告输出
---    END

+++    UDM/*MEID:402 MENAME:UDM402*/        2024-08-17 08:21:56
O&M    #2292
%%DSP GDATAREFRESH: MID=30;%%
RETCODE = 0  操作成功

查询结果如下
------------
 表名称                       数据加载源  数据加载结果  数据加载时间         数据刷新源  数据刷新结果  数据刷新时间         强制刷新标记

 N_G_SERVICEAREA_TPL          0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_DNNQOS_TPL               0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_IWFIMSIINFO              0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_CAMPUS_CONFIG            0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_EE_ANYUE_DATA            0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 W_G_ANUMBLST_PREFIX          0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 W_G_SQN_INFO                 0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_NEF_ROAM_PLMN_DATA       0           成功          2024-08-16 21:20:54  NULL        NULL          NULL                 NULL        
 N_G_DNN_REP_RULE_TPL         0           成功          2024-08-16 21:20:54  0           成功          2024-08-17 01:49:26  是          
 N_G_GK2_DATA                 0           成功          2024-08-16 21:20:54  0           成功          2024-08-17 03:20:26  是          
 N_G_DEF_KEY                  0           成功          2024-08-16 21:20:54  0           成功          2024-08-17 03:20:26  是 
 W_G_AUCFORMAT                0           成功          2024-08-16 21:20:54  0           成功          2024-08-17 03:20:26  是 
 W_G_AUCERROCODE              0           成功          2024-08-16 21:20:54  0           成功          2024-08-17 03:20:26  是
 W_G_IMSDETTACHCSMME_DATA     0           成功          2024-10-28 21:51:44  0           成功          2024-10-29 04:41:37  否          
 W_G_IMSDETTACHCSVPLMN_DATA   0           成功          2024-10-28 21:51:44  0           成功          2024-10-29 04:41:37  否          
 W_G_TESTUSERLISTBYIMSI_DATA  0           成功          2024-10-28 21:51:44  0           成功          2024-10-29 04:41:37  否          
 W_G_TESTUSERLISTBYIMPI_DATA  0           成功          2024-10-28 21:51:44  0           成功          2024-10-29 06:34:01  否          

(结果个数 = 235)

共有2个报告
---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表1所示。

| 输出项名称   | 输出项解释                                                                |
|:--------|:---------------------------------------------------------------------|
| 表名称     | 用于返回加载表的表名。                                                          |
| 数据加载源   | 用于返回最近一次加载全局数据的数据源：0：表示从DS加载。1～1023：表示从该CCU或ACF模块号对应的CCU或ACF模块加载。    |
| 数据加载结果  | 用于返回最近一次加载全局数据的结果：成功失败                                               |
| 数据加载时间  | 用于返回最近一次加载全局数据的时间。                                                   |
| 数据刷新源   | 用于返回最近一次刷新全局数据状态表的数据源：0：表示从DS刷新。1～1023：表示从该CCU或ACF模块号对应的CCU或ACF模块刷新。 |
| 数据刷新结果  | 用于返回最近一次刷新全局数据状态表的结果：成功失败                                            |
| 数据刷新时间  | 用于返回最近一次刷新全局数据状态表的时间。                                                |
| 强制刷新标记  | 用于返回是否设置了强制刷新标记：是否                                                   |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释      | 原因分析                       | 处理建议                                                                     |
|------:|:-----------|:---------------------------|:-------------------------------------------------------------------------|
|   113 | 指定模块非CCU模块 | 输入的“模块号”参数不是CCU或ACF模块的模块号。 | 根据实际情况，重新输入“模块号”参数的取值，确保其是CCU或ACF模块的模块号。CCU或ACF模块的模块号可以通过LST MODULE命令查询。 |