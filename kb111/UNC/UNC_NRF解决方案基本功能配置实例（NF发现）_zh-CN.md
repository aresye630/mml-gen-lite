---
id: ''
name: NRF解决方案基本功能配置实例（NF发现）
ne_type: UNC
type: feature
description: NRF支持NF/NFS服务发现功能，当NF需要某些特定服务时，向NRF请求发现可用服务，NRF基于已注册的NF/NFS进行筛选，将可用NF/NFS发送给NF。NRF支持基于不同选择条件进行特定NF的选择，有助于不同组网方式下的NF选择。目前NRF主要支持：  * AMF基于多维属性策略选择SMF、PCF、SMSF。 * SMF基于多维属性策略选择UDM、PCF。  * SMF基于SUPI或GPSI选择CHF系统直接支持，无需配置。 * 当被选择的NF或NF服务注册了多个IP时，AMF随机选择其中一个IP进行业务，当此IP故障时，AMF再随机选择其他IP；当故障的IP恢复正常后，此IP地址继续作为备选IP进入后续随机选择的范围。 * NF服务发现过程中，NF对查询发现结果列表有缓存功能，NF服务发现缓存时长可以自定义配置。配置方法请参考《UNC产品文档》“网络部署 > 初始配置与调测”。 * NF注册到NRF时，如果注册信息中没有携带IP地址，只有FQDN，NF间交互时需要使用DNS查询获取对端NF的IP地址，DNS查询需要配置。配置方法请参考《UNC产品文档》“网络部署 > 初始配置与调测”。 * 当AMF同时配置了多种选择策略时，NRF会同时基于所有选择条件选择符合的SMF；如果没有同时满足多种选择策略的SMF时，NRF返回空代表没有符合的SMF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","5G独立部署","NRF单层非容灾组网","NRF解决方案基本功能配置实例（NF发现）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
NRF支持NF/NFS服务发现功能，当NF需要某些特定服务时，向NRF请求发现可用服务，NRF基于已注册的NF/NFS进行筛选，将可用NF/NFS发送给NF。NRF支持基于不同选择条件进行特定NF的选择，有助于不同组网方式下的NF选择。目前NRF主要支持：* AMF基于多维属性策略选择SMF、PCF、SMSF。* SMF基于多维属性策略选择UDM、PCF。* SMF基于SUPI或GPSI选择CHF系统直接支持，无需配置。* 当被选择的NF或NF服务注册了多个IP时，AMF随机选择其中一个IP进行业务，当此IP故障时，AMF再随机选择其他IP；当故障的IP恢复正常后，此IP地址继续作为备选IP进入后续随机选择的范围。* NF服务发现过程中，NF对查询发现结果列表有缓存功能，NF服务发现缓存时长可以自定义配置。配置方法请参考《UNC产品文档》“网络部署 > 初始配置与调测”。* NF注册到NRF时，如果注册信息中没有携带IP地址，只有FQDN，NF间交互时需要使用DNS查询获取对端NF的IP地址，DNS查询需要配置。配置方法请参考《UNC产品文档》“网络部署 > 初始配置与调测”。* 当AMF同时配置了多种选择策略时，NRF会同时基于所有选择条件选择符合的SMF；如果没有同时满足多种选择策略的SMF时，NRF返回空代表没有符合的SMF。

## 必备事项
前提条件

前提条件

完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EPSIWKCOND:
          name: '融合SMF/PGW-C选择条件'
          type: string
          required: false
          description: '支持选择融合PGW-C功能的SMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_3:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfselplcy_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAISW:
          name: '是否使用TAI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '支持基于UE位置选择SMF，使用UE当前所驻留的TAI作为目标SMF的选择条件。'
          data_source: '全网规划'
          pattern: ''
          default: NO
        ISMFSW:
          name: '是否支持I-SMF选择'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_4:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_5:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfloc_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '请求方NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: '目标NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: '* “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。 * “PREFERRED\_LOCALITY（优选位置）”：将位置信息作为最高优先级选择目标NF。'
          data_source: '全网规划'
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '在"LOCTYPE"配置为"PREFERRED\_LOCALITY"时，选择特定DC2的NF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_6:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_7:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfloc_list_1:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '请求方NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: '目标NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: '* “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。 * “PREFERRED\_LOCALITY（优选位置）”：将位置信息作为最高优先级选择目标NF。'
          data_source: '全网规划'
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list:
      type: items
      properties:
        LOCSELECT:
          name: 'Locality优选的匹配策略'
          type: string
          enum:
          - LOCSELECT_INVALID
          - LOCSELECT_REGION
          - LOCSELECT_DATACENTER
          - LOCSELECT_SOURCEPOOL
          required: false
          description: '在"LOCTYPE"配置为"LOCALITY"时，选择同区域同数据中心的NF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_8:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_9:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - USER_GROUP
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GPSISW:
          name: '是否使用GPSI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '使用GPSI作为PCF选择条件。  AMF默认根据用户的SUPI发现和选择目标PCF，只有在运营商仅使用GPSI号段发现PCF的时候才需要配置此参数。'
          data_source: '全网规划'
          pattern: ''
          default: NO
        CTRLMODE:
          name: '控制模式'
          type: string
          enum:
          - WHITELIST
          - BLACKLIST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_10:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_11:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smsfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_RANGE
          - MSISDN_RANGE
          required: true
          description: 'AMF基于SUPI号段选择SMSF。  SUPISW和GPSISW只能开启一个，具体开启情况根据运营商规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPISW:
          name: '是否使用SUPI'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GPSISW:
          name: '是否使用GPSI'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDIMSI:
          name: '结束IMSI'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDMSISDN:
          name: '结束MSISDN'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTIMSI:
          name: '起始IMSI'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTMSISDN:
          name: '起始MSISDN'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_12:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_13:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfselplcy_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNFMT:
          name: 'DNN格式'
          type: string
          enum:
          - DEFAULT
          - NI
          - NIANDOI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        RETRYSW:
          name: '是否重选SMF'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_amfdnnplcy_list:
      type: items
      properties:
        DNNNI:
          name: 'DNN网络标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '表示切片URLLC（2）的业务类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '标识AMF在选择目标SMF时携带Serving Scope信息，实现在指定DNN与切片条件下根据特定Serving Scope选择目标SMF。'
          data_source: '全网规划'
          pattern: ''
          default: NO
        SERVINGSCOPE:
          name: '服务范围'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAISW:
          name: '是否使用TAI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: NO
        NEXTSSP:
          name: '下一个ServingScope映射类型'
          type: string
          enum:
          - VOID
          - TAISSP
          - RGNSSP
          - PRVSSP
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: VOID
    set_licenseswitch_list_14:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_15:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfseludm_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GPSISW:
          name: '是否使用GPSI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: 'SMF默认根据用户的SUPI发现和选择目标UDM，只有在运营商仅使用GPSI号段发现UDM的时候才需要配置此参数。'
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_licenseswitch_list_16:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_17:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfloc_list_2:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '请求方NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: '目标NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: '* “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。 * “PREFERRED\_LOCALITY（优选位置）”：将位置信息作为最高优先级选择目标NF。'
          data_source: '全网规划'
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '在"LOCTYPE"配置为"PREFERRED\_LOCALITY"时，选择特定DC2的NF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_18:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_19:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfloc_list_3:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '请求方NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: '目标NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: '* “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。 * “PREFERRED\_LOCALITY（优选位置）”：将位置信息作为最高优先级选择目标NF。'
          data_source: '全网规划'
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list_1:
      type: items
      properties:
        LOCSELECT:
          name: 'Locality优选的匹配策略'
          type: string
          enum:
          - LOCSELECT_INVALID
          - LOCSELECT_REGION
          - LOCSELECT_DATACENTER
          - LOCSELECT_SOURCEPOOL
          required: false
          description: '在"LOCTYPE"配置为"LOCALITY"时，选择同区域的NF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_20:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_21:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '已经通过**ADD APN**命令配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCFSELECTMODE:
          name: '选择PCF方式'
          type: string
          required: false
          description: 'SMF选择PCF的方式有如下几种，客户根据需要选择使用：   * DNN：根据DNN选择PCF。 * IMSI：根据IMSI选择PCF。 * GPSI：根据GPSI选择PCF。 * SNSSAIS：根据S-NSSAIs选择PCF。 * PLMN：根据PLMN选择PCF。 * NFLOC：根据优选区域选择PCF。 * SERVINGSCOPE：根据ServingScope选择PCF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_22:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_23:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '已经通过**ADD APN**命令配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCFSELECTMODE:
          name: '选择PCF方式'
          type: string
          required: false
          description: 'SMF选择PCF的方式有如下几种，客户根据需要选择使用：   * DNN：根据DNN选择PCF。 * IMSI：根据IMSI选择PCF。 * GPSI：根据GPSI选择PCF。 * SNSSAIS：根据S-NSSAIs选择PCF。 * PLMN：根据PLMN选择PCF。 * NFLOC：根据优选区域选择PCF。 * SERVINGSCOPE：根据ServingScope选择PCF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_smfselplcy_list:
    - SUBRANGE: HOME_USER
      EPSIWKCOND: UE_SUBSCRIPTION_DATA-1
      IMSIPRE: ''
      LOCDISCOPTSW: ''
      SSSW: ''
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_smfselplcy_list_1:
    - SUBRANGE: HOME_USER
      TAISW: YES
      ISMFSW: NO
      IMSIPRE: ''
      LOCDISCOPTSW: ''
      SSSW: ''
    set_licenseswitch_list_4:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_5:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_nfloc_list:
    - NFTYPE: NfAMF
      TGTNFTYPE: SMF
      LOCTYPE: PREFERRED_LOCALITY
      PREFERLOC: 'DC2'
      DESC: 'prefer the SMFs of DC2'
    set_licenseswitch_list_6:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_7:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_nfloc_list_1:
    - NFTYPE: NfAMF
      TGTNFTYPE: SMF
      LOCTYPE: LOCALITY
      PREFERLOC: ''
    set_nfdiscplcy_list:
    - LOCSELECT: LOCSELECT_DATACENTER
    set_licenseswitch_list_8:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_9:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_pcfselplcy_list:
    - SUBRANGE: HOME_USER
      GPSISW: YES
      CTRLMODE: ''
      IMSIPRE: ''
      SSSW: ''
      USRGRPID: ''
    set_licenseswitch_list_10:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_11:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_smsfselplcy_list:
    - SUBRANGE: HOME_USER
      SUPISW: ON
      GPSISW: OFF
      ENDIMSI: ''
      ENDMSISDN: ''
      STARTIMSI: ''
      STARTMSISDN: ''
    set_licenseswitch_list_12:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_13:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    add_smfselplcy_list_2:
    - SUBRANGE: HOME_USER
      DNNFMT: NI
      RETRYSW: YES
      IMSIPRE: ''
      LOCDISCOPTSW: ''
      SSSW: ''
    add_amfdnnplcy_list:
    - DNNNI: 'dnn2'
      SST: 1
      SD: '000001'
      SSSW: YES
      SERVINGSCOPE: 'shanghai'
      TAISW: NO
      NEXTSSP: VOID
    set_licenseswitch_list_14:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_15:
    - LICITEM: 'LKV2NFDSM01'
      SWITCH: ENABLE
    add_smfseludm_list:
    - SUBRANGE: HOME_USER
      GPSISW: YES
    set_licenseswitch_list_16:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_17:
    - LICITEM: 'LKV2NFDSM01'
      SWITCH: ENABLE
    add_nfloc_list_2:
    - NFTYPE: NfSMF
      TGTNFTYPE: UDM
      LOCTYPE: PREFERRED_LOCALITY
      PREFERLOC: 'DC2'
      DESC: 'prefer the UDMs of DC2'
    set_licenseswitch_list_18:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_19:
    - LICITEM: 'LKV2NFDSM01'
      SWITCH: ENABLE
    add_nfloc_list_3:
    - NFTYPE: NfSMF
      TGTNFTYPE: UDM
      LOCTYPE: LOCALITY
      PREFERLOC: ''
    set_nfdiscplcy_list_1:
    - LOCSELECT: LOCSELECT_REGION
    set_licenseswitch_list_20:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_21:
    - LICITEM: 'LKV2NFDSM01'
      SWITCH: ENABLE
    set_apnpccfunc_list:
    - APN: 'huawei'
      PCFSELECTMODE: DNN-1
    set_licenseswitch_list_22:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    set_licenseswitch_list_23:
    - LICITEM: 'LKV2NFDSM01'
      SWITCH: ENABLE
    set_apnpccfunc_list_1:
    - APN: 'huawei'
      PCFSELECTMODE: IMSI-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置AMF灵活选择其他NF

#### 1.1 **任务场景1**

#### AMF为本网用户选择融合PGW-C功能的SMF。

#### **配置脚本1**

##### 1.1.1 NRF侧配置

###### 1.1.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.1.2 AMF侧配置

###### 1.1.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.1.2.2 //AMF为本网用户选择融合PGW-C功能的SMF。

```jinja2
{%- for item in add_smfselplcy_list -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.EPSIWKCOND is not none -%}
        EPSIWKCOND={{item.EPSIWKCOND}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.LOCDISCOPTSW is not none -%}
            LOCDISCOPTSW={{item.LOCDISCOPTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 **任务场景2**

#### AMF为本网用户基于用户TAI位置选择SMF。

#### **配置脚本2**

##### 1.2.1 NRF侧配置

###### 1.2.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.2.2 AMF侧配置

###### 1.2.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_3 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.2.2.2 //AMF为本网用户基于用户TAI位置选择SMF。

```jinja2
{%- for item in add_smfselplcy_list_1 -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISMFSW is not none -%}
        ISMFSW={{item.ISMFSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ISMFSW=NO 时可选 --- -#}
    {%- if item.ISMFSW == 'NO' -%}
        {%- if item.TAISW is not none -%}
            TAISW={{item.TAISW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.LOCDISCOPTSW is not none -%}
            LOCDISCOPTSW={{item.LOCDISCOPTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 **任务场景3**

#### 由于网络调整，运营商期望AMF为新建的PDU Session选择位于“DC2”数据中心内的SMF。

#### **配置脚本3**

##### 1.3.1 NRF侧配置

###### 1.3.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_4 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.3.2 AMF侧配置

###### 1.3.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_5 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.3.2.2 //AMF选择特定DC2位置的SMF。

```jinja2
{%- for item in add_nfloc_list -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 **任务场景4**

#### AMF选择同区域同数据中心的SMF。

#### **配置脚本4**

##### 1.4.1 NRF侧配置

###### 1.4.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_6 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.4.2 AMF侧配置

###### 1.4.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_7 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.4.2.2 //AMF选择同区域同数据中心的SMF。

```jinja2
{%- for item in add_nfloc_list_1 -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCSELECT is not none -%}
        LOCSELECT={{item.LOCSELECT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 **任务场景5**

#### AMF通过GPSI为本网用户选择发现PCF。

#### **配置脚本5**

##### 1.5.1 NRF侧配置

###### 1.5.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_8 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.5.2 AMF侧配置

###### 1.5.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_9 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.5.2.2 //AMF通过GPSI为本网用户选择PCF。

```jinja2
{%- for item in add_pcfselplcy_list -%}
    ADD PCFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GPSISW is not none -%}
        GPSISW={{item.GPSISW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=USER_GROUP/IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE in ['USER_GROUP', 'IMSI_PREFIX'] -%}
        CTRLMODE={{item.CTRLMODE}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
    {%- if item.SUBRANGE == 'USER_GROUP' -%}
        USRGRPID={{item.USRGRPID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=USER_GROUP/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['USER_GROUP', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 **任务场景6**

#### AMF通过SUPI为本网用户选择发现SMSF。

#### **配置脚本6**

##### 1.6.1 NRF侧配置

###### 1.6.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_10 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.6.2 AMF侧配置

###### 1.6.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_11 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.6.2.2 //AMF通过SUPI为本网用户选择SMSF。

```jinja2
{%- for item in add_smsfselplcy_list -%}
    ADD SMSFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SUPISW is not none -%}
        SUPISW={{item.SUPISW}},
    {%- endif -%}
    {%- if item.GPSISW is not none -%}
        GPSISW={{item.GPSISW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        STARTIMSI="{{item.STARTIMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=MSISDN_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_RANGE' -%}
        STARTMSISDN="{{item.STARTMSISDN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI_RANGE 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
        {%- if item.ENDIMSI is not none -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=MSISDN_RANGE 时可选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_RANGE' -%}
        {%- if item.ENDMSISDN is not none -%}
            ENDMSISDN="{{item.ENDMSISDN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 **任务场景7**

#### 运营商网络中，DNN2的2个数据网络分别接入部署到北京和上海SMF上，在南方的用户期望根据Serving Scope选择就近的上海SMF接入。

#### **配置脚本7**

##### 1.7.1 NRF侧配置

###### 1.7.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_12 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.7.2 AMF侧配置

###### 1.7.2.1 //打开NF发现的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_13 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 1.7.2.2 //AMF根据用户所在省份查询就近的SMF。

```jinja2
{%- for item in add_smfselplcy_list_2 -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DNNFMT is not none -%}
        DNNFMT={{item.DNNFMT}},
    {%- endif -%}
    {%- if item.RETRYSW is not none -%}
        RETRYSW={{item.RETRYSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.LOCDISCOPTSW is not none -%}
            LOCDISCOPTSW={{item.LOCDISCOPTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
        {%- if item.SSSW is not none -%}
            SSSW={{item.SSSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_amfdnnplcy_list -%}
    ADD AMFDNNPLCY:
    {#- --- 必选参数 --- -#}
    DNNNI="{{item.DNNNI}}",
    SST={{item.SST}},
    SD="{{item.SD}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSSW is not none -%}
        SSSW={{item.SSSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SSSW=YES 时必选 --- -#}
    {%- if item.SSSW == 'YES' -%}
        SERVINGSCOPE="{{item.SERVINGSCOPE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SSSW=YES 时可选 --- -#}
    {%- if item.SSSW == 'YES' -%}
        {%- if item.TAISW is not none -%}
            TAISW={{item.TAISW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TAISW=NO 时可选 --- -#}
    {%- if item.TAISW == 'NO' -%}
        {%- if item.NEXTSSP is not none -%}
            NEXTSSP={{item.NEXTSSP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置SMF侧灵活选择其他NF

#### 2.1 **任务场景8**

#### SMF通过GPSI为本网用户选择发现UDM。

#### **配置脚本8**

##### 2.1.1 NRF侧配置

###### 2.1.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_14 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 2.1.2 SMF侧配置

###### 2.1.2.1 //打开NF发现的License配置开关，适用于SMF。

```jinja2
{%- for item in set_licenseswitch_list_15 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.1.2.2 //SMF通过GPSI为本网用户选择发现UDM。

```jinja2
{%- for item in add_smfseludm_list -%}
    ADD SMFSELUDM:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GPSISW is not none -%}
        GPSISW={{item.GPSISW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 **任务场景9**

#### 由于网络调整，运营商期望SMF选择位于“DC2”数据中心内的UDM进行业务交互。

#### **配置脚本9**

##### 2.2.1 NRF侧配置

###### 2.2.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_16 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 2.2.2 SMF侧配置

###### 2.2.2.1 //打开NF发现的License配置开关，适用于SMF。

```jinja2
{%- for item in set_licenseswitch_list_17 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.2.2.2 //由于网络调整，运营商期望SMF选择位于“DC2”数据中心内的UDM进行业务交互。

```jinja2
{%- for item in add_nfloc_list_2 -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 **任务场景10**

#### SMF选择同区域的UDM进行业务。

#### **配置脚本10**

##### 2.3.1 NRF侧配置

###### 2.3.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_18 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 2.3.2 SMF侧配置

###### 2.3.2.1 //打开NF发现的License配置开关，适用于SMF。

```jinja2
{%- for item in set_licenseswitch_list_19 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.3.2.2 //SMF选择同区域的UDM。

```jinja2
{%- for item in add_nfloc_list_3 -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nfdiscplcy_list_1 -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCSELECT is not none -%}
        LOCSELECT={{item.LOCSELECT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 **任务场景11**

#### SMF为指定APN（huawei）用户基于DNN选择PCF。

#### **配置脚本11**

##### 2.4.1 NRF侧配置

###### 2.4.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_20 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 2.4.2 SMF侧配置

###### 2.4.2.1 //打开NF发现的License配置开关，适用于SMF。

```jinja2
{%- for item in set_licenseswitch_list_21 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.4.2.2 //SMF为指定APN用户基于DNN选择PCF。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCFSELECTMODE is not none -%}
        PCFSELECTMODE={{item.PCFSELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 **任务场景12**

#### SMF为指定APN（huawei）用户基于IMSI选择PCF。

#### **配置脚本12**

##### 2.5.1 NRF侧配置

###### 2.5.1.1 //打开NF发现的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_22 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 2.5.2 SMF侧配置

###### 2.5.2.1 //打开NF发现的License配置开关，适用于SMF。

```jinja2
{%- for item in set_licenseswitch_list_23 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.5.2.2 //SMF为指定APN用户基于IMSI选择PCF。

```jinja2
{%- for item in set_apnpccfunc_list_1 -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCFSELECTMODE is not none -%}
        PCFSELECTMODE={{item.PCFSELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

