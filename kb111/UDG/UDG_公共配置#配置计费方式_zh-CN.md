---
id: ''
name: 配置计费方式
ne_type: UDG
type: feature
description: 本指导用于描述UNC同时支持离线计费和在线计费的操作过程。  **GGSN-C/PGW-C/SMF**  对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。  GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。  根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。  **SGW-C**  对于SGW-C，计费方式要通过本地进行配置。SGW-C本地配置计费开关有三种粒度：IMSI/MSISDN号段组、APN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET SGWCHARGECFG**是控制SGW-C本地配置的计费开关是否有效的总开关，当总开关使能了离线计费，其他开关的配置才能生效。默认情况下，漫游用户和拜访用户使能离线计费，本地用户不使能离线计费。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","公共配置","配置计费方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导用于描述UNC同时支持离线计费和在线计费的操作过程。**GGSN-C/PGW-C/SMF**对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。**SGW-C**对于SGW-C，计费方式要通过本地进行配置。SGW-C本地配置计费开关有三种粒度：IMSI/MSISDN号段组、APN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET SGWCHARGECFG**是控制SGW-C本地配置的计费开关是否有效的总开关，当总开关使能了离线计费，其他开关的配置才能生效。默认情况下，漫游用户和拜访用户使能离线计费，本地用户不使能离线计费。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chargectrl_list:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均开启在线计费和离线计费，不开启融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chargectrl_list_1:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均开启在线计费和离线计费，不开启融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '（可选）基于用户模板配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于用户模板配置计费方式。  说明：  * “ONLINESW”和“OFFLINESW”配置“INHERIT”，表示计费方式继承基于DNN的配置。 * 本示例配置User Profile为up-test的用户在线计费开关和离线计费开关继承上一级配置，不开启融合计费。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chargectrl_list_2:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均开启在线计费和离线计费，不开启融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '（可选）基于DNN配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于DNN配置计费方式。  说明：  * “ONLINESW”和“OFFLINESW”配置“INHERIT”，表示计费方式继承基于计费属性的配置。 * 本示例配置APN为apn-test的用户在线计费开关、离线计费开关均继承上一级配置，融合计费开关关闭。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chargectrl_list_3:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均开启在线计费和离线计费，不开启融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chargemethod_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          required: false
          description: '（可选）基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于计费属性配置计费方式。  说明：  本示例配置计费属性为0x0400的用户在线计费开关、离线计费开关和融合计费开关均使能，融合计费开关不使能。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASK:
          name: '计费属性掩码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '计费属性优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINE:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINE:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGED:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchargecfg_list:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          required: false
          description: '基于用户的漫游属性配置SGW-C的计费开关。  说明：  本示例配置本地用户不使能离线计费 ，漫游和拜访用户使能离线计费。 一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchargecfg_list_1:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          required: false
          description: '基于用户的漫游属性配置SGW-C的计费开关。  说明：  本示例配置本地用户不使能离线计费 ，漫游和拜访用户使能离线计费。 一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchgmeth_list:
      type: items
      properties:
        CHARGECHAR:
          name: '计费属性'
          type: string
          required: false
          description: '（可选）基于用户的计费属性配置SGW-C的计费开关。  说明：  本示例配置计费属性为0x0800的用户使能离线计费。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHARGECHARVALUE:
          name: '计费属性值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCMASK:
          name: '计费属性掩码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: '计费属性优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: '是否离线计费'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchargecfg_list_2:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          required: false
          description: '基于用户的漫游属性配置SGW-C的计费开关。  说明：  本示例配置本地用户不使能离线计费 ，漫游和拜访用户使能离线计费。 一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwapnchgmeth_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '（可选）基于APN配置SGW-C的计费开关。  说明：  本示例配置APN为apn-test的用户离线开关继承上一级配置。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINE:
          name: 'APN离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchargecfg_list_3:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          required: false
          description: '基于用户的漫游属性配置SGW-C的计费开关。  说明：  本示例配置本地用户不使能离线计费 ，漫游和拜访用户使能离线计费。 一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访用户离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sgwseggchgmeth_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号段组名称'
          type: string
          required: false
          description: '（可选）基于用户的IMSI/MSISDN号段组配置SGW-C的计费开关。  说明：  本示例配置在号段组segment1中的用户使能离线计费 。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'IMSI/MSISDN号段组优先级'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: 'IMSI/MSISDN号段组离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_chargectrl_list:
    - HOMECONVERGED: DISABLE
      HOMEONLINE: ENABLE
      HOMEOFFLINE: ENABLE
      VISITONLINE: ENABLE
      VISITOFFLINE: ENABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: ENABLE
      ROAMOFFLINE: ENABLE
      ROAMCONVERGED: DISABLE
    set_chargectrl_list_1:
    - HOMECONVERGED: DISABLE
      HOMEONLINE: ENABLE
      HOMEOFFLINE: ENABLE
      VISITONLINE: ENABLE
      VISITOFFLINE: ENABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: ENABLE
      ROAMOFFLINE: ENABLE
      ROAMCONVERGED: DISABLE
    set_usrprofcharge_list:
    - USRPROFNAME: up-test
      ONLINESW: INHERIT
      OFFLINESW: INHERIT
      CONVERGEDSW: DISABLE
    set_chargectrl_list_2:
    - HOMECONVERGED: DISABLE
      HOMEONLINE: ENABLE
      HOMEOFFLINE: ENABLE
      VISITONLINE: ENABLE
      VISITOFFLINE: ENABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: ENABLE
      ROAMOFFLINE: ENABLE
      ROAMCONVERGED: DISABLE
    set_apnchargectrl_list:
    - APN: apn-test
      ONLINESW: INHERIT
      OFFLINESW: INHERIT
      CONVERGEDSW: DISABLE
    set_chargectrl_list_3:
    - HOMECONVERGED: DISABLE
      HOMEONLINE: ENABLE
      HOMEOFFLINE: ENABLE
      VISITONLINE: ENABLE
      VISITOFFLINE: ENABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: ENABLE
      ROAMOFFLINE: ENABLE
      ROAMCONVERGED: DISABLE
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0400'
      MASK: '0xFFFF'
      PRIORITY: '1'
      ONLINE: ENABLE
      OFFLINE: ENABLE
      CONVERGED: DISABLE
    set_sgwchargecfg_list:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
    set_sgwchargecfg_list_1:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
    set_sgwchgmeth_list:
    - CHARGECHAR: SPECIFIC_VALUE
      CHARGECHARVALUE: '0x0800'
      CCMASK: '0xFFFF'
      CCPRIORITY: '1'
      OFFLINEFLAG: ENABLE
    set_sgwchargecfg_list_2:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
    set_sgwapnchgmeth_list:
    - APN: apn-test
      OFFLINE: INHERIT
    set_sgwchargecfg_list_3:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
    add_sgwseggchgmeth_list:
    - SEGGROUPNAME: segment1
      PRIORITY: '1'
      OFFLINEFLAG: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chargectrl_list的变量区（command: SET CHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET CHARGECTRL list_name=set_chargectrl_list step_id=1 -->
```

### **SET CHARGECTRL**根据用户漫游属性设置计费方式，**ADD CHARGEMETHOD**根据计费属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对计费属性是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。

### 2 **可选：**基于User Profile配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chargectrl_list_1的变量区（command: SET CHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET CHARGECTRL list_name=set_chargectrl_list_1 step_id=2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_usrprofcharge_list的变量区（command: SET USRPROFCHARGE） -#}
<!-- MISSING_MACRO: command=SET USRPROFCHARGE list_name=set_usrprofcharge_list step_id=2 -->
```

### 3 **可选：**基于DNN配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chargectrl_list_2的变量区（command: SET CHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET CHARGECTRL list_name=set_chargectrl_list_2 step_id=3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3 -->
```

### 4 **可选：**基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chargectrl_list_3的变量区（command: SET CHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET CHARGECTRL list_name=set_chargectrl_list_3 step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chargemethod_list的变量区（command: ADD CHARGEMETHOD） -#}
<!-- MISSING_MACRO: command=ADD CHARGEMETHOD list_name=add_chargemethod_list step_id=4 -->
```

### 5 配置基于用户的漫游属性配置SGW-C的计费开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwchargecfg_list的变量区（command: SET SGWCHARGECFG） -#}
<!-- MISSING_MACRO: command=SET SGWCHARGECFG list_name=set_sgwchargecfg_list step_id=5 -->
```

### 6 **可选：**基于用户的计费属性配置SGW-C的计费开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwchargecfg_list_1的变量区（command: SET SGWCHARGECFG） -#}
<!-- MISSING_MACRO: command=SET SGWCHARGECFG list_name=set_sgwchargecfg_list_1 step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwchgmeth_list的变量区（command: SET SGWCHGMETH） -#}
<!-- MISSING_MACRO: command=SET SGWCHGMETH list_name=set_sgwchgmeth_list step_id=6 -->
```

### 7 **可选：**基于APN配置SGW-C的计费开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwchargecfg_list_2的变量区（command: SET SGWCHARGECFG） -#}
<!-- MISSING_MACRO: command=SET SGWCHARGECFG list_name=set_sgwchargecfg_list_2 step_id=7 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwapnchgmeth_list的变量区（command: SET SGWAPNCHGMETH） -#}
<!-- MISSING_MACRO: command=SET SGWAPNCHGMETH list_name=set_sgwapnchgmeth_list step_id=7 -->
```

### 8 **可选：**基于用户的IMSI/MSISDN号段组配置SGW-C的计费开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_sgwchargecfg_list_3的变量区（command: SET SGWCHARGECFG） -#}
<!-- MISSING_MACRO: command=SET SGWCHARGECFG list_name=set_sgwchargecfg_list_3 step_id=8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_sgwseggchgmeth_list的变量区（command: ADD SGWSEGGCHGMETH） -#}
<!-- MISSING_MACRO: command=ADD SGWSEGGCHGMETH list_name=add_sgwseggchgmeth_list step_id=8 -->
```

