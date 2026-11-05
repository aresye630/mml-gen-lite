---
id: ''
name: 配置计费消息缓存（融合计费）
ne_type: UNC
type: feature
description: 本指导描述融合计费场景计费消息缓存功能的相关配置过程。  融合计费场景中，当主备NCG/CHF(OCS)均故障时，为避免用户体验变差，UNC(GGSN/PGW-C/SMF)可以采用不做配额管理的计费方式，允许用户继续使用业务，并缓存计费信息；随着NCG/CHF(OCS)的恢复，UNC(GGSN/PGW-C/SMF)可以将缓存的计费信息回放到对应的NCG/CHF(OCS)。  此功能为定制能力，要求对端NCG/CHF(OCS)为华为公司NCG。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","SMF配置","配置计费消息缓存（融合计费）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述融合计费场景计费消息缓存功能的相关配置过程。融合计费场景中，当主备NCG/CHF(OCS)均故障时，为避免用户体验变差，UNC(GGSN/PGW-C/SMF)可以采用不做配额管理的计费方式，允许用户继续使用业务，并缓存计费信息；随着NCG/CHF(OCS)的恢复，UNC(GGSN/PGW-C/SMF)可以将缓存的计费信息回放到对应的NCG/CHF(OCS)。此功能为定制能力，要求对端NCG/CHF(OCS)为华为公司NCG。

## 必备事项
前提条件

前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
* 已完成融合计费模板创建。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_failhandling_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '融合计费模板名称，配置融合计费模板已经配置。'
          data_source: '从已有配置中获取'
          pattern: ''
          default: ''
        FHACTION:
          name: 'FH处理动作'
          type: string
          enum:
          - TERMINATE
          - CONTINUE
          - RETRY_AND_TERM
          required: false
          description: '当NCG/CHF(OCS)不可用，UNC(GGSN/PGW-C/SMF)允许用户继续使用业务，不再进行配额管理和配额上报。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长(秒)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: '配置Tx定时器时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDCONTTERM:
          name: 'Update消息触发业务放通结束计费会话开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置ChargingDataUpdate消息触发的计费缓存场景，UNC(GGSN/PGW-C/SMF)发送ChargingDataRelease消息结束计费会话。'
          data_source: ''
          pattern: ''
          default: ''
        CNVCHGRECOVER:
          name: '融合计费自动恢复功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置NCG/CHF(OCS)故障恢复后重建计费会话功能。'
          data_source: ''
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '融合计费自动恢复间隔 (分钟)'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_pduscact_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '融合计费模板名称，配置融合计费模板已经配置。'
          data_source: '从已有配置中获取'
          pattern: ''
          default: ''
        CODETYPE:
          name: '返回码类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: integer
          minimum:
          - 300
          - 65535
          maximum:
          - 999
          - 65535
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        SCACT:
          name: '处理动作'
          type: string
          enum:
          - FAILOVER
          - CONTINUE
          - TERM_WITH_REL
          - TERM_NO_REL
          - BLOCK
          - REDIRECT
          required: true
          description: 'SCACT需配置为FAILOVER或CONTINUE，开启计费消息缓存的前提条件。'
          data_source: ''
          pattern: ''
          default: ''
        BLKTIMER:
          name: '阻塞处理时间间隔'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPV01CAUSE:
          name: '原因值GtpV0-1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPV2CAUSE:
          name: '原因值GtpV2'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIP:
          name: '重定向IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDVIRTIPV6:
          name: '重定向IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REACTREQ:
          name: '重新激活请求'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_n40msgstg_list:
      type: items
      properties:
        STGSWITCH:
          name: '融合计费消息缓存开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '固定配置，开启计费消息缓存功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        REPLAYINTERVAL:
          name: '融合计费消息回放的最小间隔(分钟)'
          type: integer
          minimum: 5
          maximum: 1440
          required: false
          description: '配置缓存消息回放的时间间隔。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REPLAYRATE:
          name: '融合计费消息回放的速率(个/秒)'
          type: integer
          minimum: 10
          maximum: 10000
          required: false
          description: '配置缓存消息回放的速率。'
          data_source: ''
          pattern: ''
          default: ''
        ENCRYPT:
          name: '加密开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STGTXTIMER:
          name: '缓存Tx定时器时长(秒)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_stgtrigger_list:
      type: items
      properties:
        TIMELIMIT:
          name: '时间阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: '融合计费消息缓存期间的trigger，全局配置。  说明：  TIMELIMIT参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，时间阈值trigger的处理方式。  PDUTIMELIMIT参数：配置PDU级别触发生成缓存消息的时长阈值。  VOLUMELIMIT参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，流量阈值trigger的处理方式。  PDUVOLUMELIMIT参数：配置PDU级别触发生成缓存消息的流量阈值。  RATCHG参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，RAT更新trigger的处理方式。  SRVNDCHG参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，服务节点更新trigger的处理方式。  QOSCHG参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，QoS更新trigger的处理方式。  ULCHG参数：配置主备NCG/CHF(OCS)均故障后用户业务放通期间，用户位置更新trigger的处理方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATCHG:
          name: 'RAT更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULCHG:
          name: '用户位置更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cnvrgdchgpara_list:
      type: items
      properties:
        CHGDATAREFGEN:
          name: 'ChargingDataRef生成方式'
          type: string
          enum:
          - CHF
          - SMF
          required: false
          description: '指定由SMF生成ChargingDataRef。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHGDATAREFFMT:
          name: 'ChargingDataRef格式'
          type: string
          enum:
          - CHGDATAREF_FMT_DEFAULT
          - CHGDATAREF_FMT_CUSTOM1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGDATAREFUSE:
          name: 'ChargingDataRef使用方式'
          type: string
          enum:
          - SMF
          - CHF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cdrstoragectrl_list:
      type: items
      properties:
        CDREXPIREDAY:
          name: '话单缓存超期天数'
          type: integer
          minimum: 0
          maximum: 6
          required: false
          description: '配置缓存话单文件的超期时长，超期后缓存话单不再回放。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDREXPIREWEEK:
          name: '话单缓存超期周数'
          type: integer
          minimum: 0
          maximum: 52
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_stgalarmctrl_list:
      type: items
      properties:
        ALMTHD:
          name: '告警产生门限'
          type: integer
          minimum: 0
          maximum: 1048576
          required: false
          description: '配置**“ALM-81025 话单缓存”**告警产生门限。缓存话单文件占用空间大小超过该阈值时，上报告警；缓存话单被回放后，清除告警。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MONITORTIME:
          name: '告警监控时长'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '配置**“ALM-81025 话单缓存”**告警监控时长。  说明：  参考融合计费缓存消息回放的最小间隔（通过**SET N40MSGSTG**命令的“REPLAYINTERVAL”参数设置）进行配置，本参数建议配置为回放间隔的2倍以上。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_n4chgmsgctrl_list:
      type: items
      properties:
        MSGCACHEEPDSW:
          name: '消息缓存池扩展开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制单个会话的N4计费消息缓存池满时（20条消息），是否扩展消息缓存池规格到40条消息，最多支持100个会话进行扩展。如果该会话已缓存的N4计费消息由于部分消息被丢弃而不连续时，不可以针对该会话进行扩展。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CACHEFULLACT:
          name: '缓存池满的动作'
          type: string
          enum:
          - CONTINUE
          - TERMINATE
          required: false
          description: '控制单个会话的N4计费消息缓存池满时动作。允许业务继续进行，不再进行配额管理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_failhandling_list:
    - CCTMPLTNAME: 'cct-test'
      FHACTION: CONTINUE
      TXTIMER: 5
      UPDCONTTERM: ENABLE
      CNVCHGRECOVER: ENABLE
      RECOVERINTERVAL: 5
    mod_pduscact_list:
    - CCTMPLTNAME: 'cct-test'
      CODETYPE: VALUE
      STATUSCODE: 502
      SCACT: FAILOVER
      BLKTIMER: ''
      GTPV01CAUSE: ''
      GTPV2CAUSE: ''
      RDVIRTIP: ''
      RDVIRTIPV6: ''
      REACTREQ: ''
    set_n40msgstg_list:
    - STGSWITCH: ENABLE
      REPLAYINTERVAL: 30
      REPLAYRATE: 500
      ENCRYPT: ''
      STGTXTIMER: ''
    set_stgtrigger_list:
    - TIMELIMIT: IMMEDIATE
      PDUTIMELIMIT: 30
      VOLUMELIMIT: IMMEDIATE
      PDUVOLUMELIMIT: 500
      RATCHG: IMMEDIATE
      SRVNDCHG: IMMEDIATE
      QOSCHG: DEFERRED
      ULCHG: DEFERRED
    set_cnvrgdchgpara_list:
    - CHGDATAREFGEN: SMF
      CHGDATAREFFMT: ''
      CHGDATAREFUSE: ''
    set_cdrstoragectrl_list:
    - CDREXPIREDAY: 2
      CDREXPIREWEEK: 4
    set_stgalarmctrl_list:
    - ALMTHD: 5120
      MONITORTIME: 60
    set_n4chgmsgctrl_list:
    - MSGCACHEEPDSW: ENABLE
      CACHEFULLACT: CONTINUE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置当NCG/CHF(OCS)故障，UNC(GGSN/PGW-C/SMF)放通业务，不进行配额管理和配额上报；配置当NCG/CHF(OCS)故障恢复后重建计费会话功能。

### 如果在配置（可选）配置异常返回码动作时已经配置了如下内容，则此步骤可以跳过：

### 当NCG/CHF(OCS)故障，UNC(GGSN/PGW-C/SMF)放通业务；当NCG/CHF(OCS)故障恢复后重建计费会话功能：**SET FAILHANDLING**命令的“FHACTION”参数为“CONTINUE”，“UPDCONTTERM”参数值为“ENABLE”，“CNVCHGRECOVER”参数值为“ENABLE”。

### UNC(GGSN/PGW-C/SMF)收到NCG/CHF(OCS)的PDU级异常返回码时的动作为failover或者continue：**MOD PDUSCACT**命令的“SCACT”参数值为“FAILOVER”或者“CONTINUE”。

```jinja2
{%- for item in set_failhandling_list -%}
    SET FAILHANDLING:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FHACTION is not none -%}
        FHACTION={{item.FHACTION}},
    {%- endif -%}
    {%- if item.TXTIMER is not none -%}
        TXTIMER={{item.TXTIMER}},
    {%- endif -%}
    {%- if item.UPDCONTTERM is not none -%}
        UPDCONTTERM={{item.UPDCONTTERM}},
    {%- endif -%}
    {%- if item.CNVCHGRECOVER is not none -%}
        CNVCHGRECOVER={{item.CNVCHGRECOVER}},
    {%- endif -%}
    {%- if item.RECOVERINTERVAL is not none -%}
        RECOVERINTERVAL={{item.RECOVERINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置当UNC(GGSN/PGW-C/SMF)收到NCG/CHF(OCS)的PDU级异常返回码时的动作。

### 如果在配置（可选）配置异常返回码动作时已经配置了如下内容，则此步骤可以跳过：

### 当NCG/CHF(OCS)故障，UNC(GGSN/PGW-C/SMF)放通业务；当NCG/CHF(OCS)故障恢复后重建计费会话功能：**SET FAILHANDLING**命令的“FHACTION”参数为“CONTINUE”，“UPDCONTTERM”参数值为“ENABLE”，“CNVCHGRECOVER”参数值为“ENABLE”。

### UNC(GGSN/PGW-C/SMF)收到NCG/CHF(OCS)的PDU级异常返回码时的动作为failover或者continue：**MOD PDUSCACT**命令的“SCACT”参数值为“FAILOVER”或者“CONTINUE”。

```jinja2
{%- for item in mod_pduscact_list -%}
    MOD PDUSCACT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    CODETYPE={{item.CODETYPE}},
    SCACT={{item.SCACT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CODETYPE=VALUE 时必选 --- -#}
    {%- if item.CODETYPE == 'VALUE' -%}
        STATUSCODE={{item.STATUSCODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SCACT=REDIRECT/BLOCK 时可选 --- -#}
    {%- if item.SCACT in ['REDIRECT', 'BLOCK'] -%}
        {%- if item.BLKTIMER is not none -%}
            BLKTIMER={{item.BLKTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.GTPV01CAUSE is not none -%}
            GTPV01CAUSE={{item.GTPV01CAUSE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.GTPV2CAUSE is not none -%}
            GTPV2CAUSE={{item.GTPV2CAUSE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=REDIRECT 时可选 --- -#}
    {%- if item.SCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIP is not none -%}
            RDVIRTIP="{{item.RDVIRTIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=REDIRECT 时可选 --- -#}
    {%- if item.SCACT == 'REDIRECT' -%}
        {%- if item.RDVIRTIPV6 is not none -%}
            RDVIRTIPV6="{{item.RDVIRTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCACT=TERM_WITH_REL/TERM_NO_REL 时可选 --- -#}
    {%- if item.SCACT in ['TERM_WITH_REL', 'TERM_NO_REL'] -%}
        {%- if item.REACTREQ is not none -%}
            REACTREQ={{item.REACTREQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置计费消息缓存功能。

```jinja2
{%- for item in set_n40msgstg_list -%}
    SET N40MSGSTG:
    {#- --- 必选参数 --- -#}
    STGSWITCH={{item.STGSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：STGSWITCH=ENABLE 时可选 --- -#}
    {%- if item.STGSWITCH == 'ENABLE' -%}
        {%- if item.REPLAYINTERVAL is not none -%}
            REPLAYINTERVAL={{item.REPLAYINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STGSWITCH=ENABLE 时可选 --- -#}
    {%- if item.STGSWITCH == 'ENABLE' -%}
        {%- if item.REPLAYRATE is not none -%}
            REPLAYRATE={{item.REPLAYRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STGSWITCH=ENABLE 时可选 --- -#}
    {%- if item.STGSWITCH == 'ENABLE' -%}
        {%- if item.ENCRYPT is not none -%}
            ENCRYPT={{item.ENCRYPT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：STGSWITCH=ENABLE 时可选 --- -#}
    {%- if item.STGSWITCH == 'ENABLE' -%}
        {%- if item.STGTXTIMER is not none -%}
            STGTXTIMER={{item.STGTXTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置计费消息缓存期间的trigger。

```jinja2
{%- for item in set_stgtrigger_list -%}
    SET STGTRIGGER:
    {#- --- 可选参数 --- -#}
    {%- if item.TIMELIMIT is not none -%}
        TIMELIMIT={{item.TIMELIMIT}},
    {%- endif -%}
    {%- if item.PDUTIMELIMIT is not none -%}
        PDUTIMELIMIT={{item.PDUTIMELIMIT}},
    {%- endif -%}
    {%- if item.VOLUMELIMIT is not none -%}
        VOLUMELIMIT={{item.VOLUMELIMIT}},
    {%- endif -%}
    {%- if item.PDUVOLUMELIMIT is not none -%}
        PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
    {%- endif -%}
    {%- if item.RATCHG is not none -%}
        RATCHG={{item.RATCHG}},
    {%- endif -%}
    {%- if item.SRVNDCHG is not none -%}
        SRVNDCHG={{item.SRVNDCHG}},
    {%- endif -%}
    {%- if item.ULCHG is not none -%}
        ULCHG={{item.ULCHG}},
    {%- endif -%}
    {%- if item.QOSCHG is not none -%}
        QOSCHG={{item.QOSCHG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置由SMF生成ChargingDataRef。

```jinja2
{%- for item in set_cnvrgdchgpara_list -%}
    SET CNVRGDCHGPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CHGDATAREFGEN is not none -%}
        CHGDATAREFGEN={{item.CHGDATAREFGEN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CHGDATAREFGEN=SMF 时可选 --- -#}
    {%- if item.CHGDATAREFGEN == 'SMF' -%}
        {%- if item.CHGDATAREFFMT is not none -%}
            CHGDATAREFFMT={{item.CHGDATAREFFMT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHGDATAREFGEN=SMF 时可选 --- -#}
    {%- if item.CHGDATAREFGEN == 'SMF' -%}
        {%- if item.CHGDATAREFUSE is not none -%}
            CHGDATAREFUSE={{item.CHGDATAREFUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置缓存话单文件的超期时长。

```jinja2
{%- for item in set_cdrstoragectrl_list -%}
    SET CDRSTORAGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.CDREXPIREDAY is not none -%}
        CDREXPIREDAY={{item.CDREXPIREDAY}},
    {%- endif -%}
    {%- if item.CDREXPIREWEEK is not none -%}
        CDREXPIREWEEK={{item.CDREXPIREWEEK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置融合计费**“ALM-81025 话单缓存”**告警上报的控制参数。

```jinja2
{%- for item in set_stgalarmctrl_list -%}
    SET STGALARMCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.ALMTHD is not none -%}
        ALMTHD={{item.ALMTHD}},
    {%- endif -%}
    {%- if item.MONITORTIME is not none -%}
        MONITORTIME={{item.MONITORTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### **SET STGALARMCTRL**命令的“ALMTHD”参数控制UNC(GGSN/PGW-C/SMF)上报**“ALM-81025 话单缓存”**告警的缓存话单文件占用空间阈值。缓存话单文件超过该阈值时，上报告警；缓存话单全部被回放后，清除告警。

### **SET STGALARMCTRL**命令的“MONITORTIME”参数控制告警监控时长，当UNC(GGSN/PGW-C/SMF)检查到缓存话单文件存在且不超过占用空间阈值时，超过告警监控时长后，UNC(GGSN/PGW-C/SMF)上报**“ALM-81025 话单缓存”**告警。建议该参数配置为**SET N40MSGSTG**命令配置的“REPLAYINTERVAL”的2倍以上。

### 如果“MONITORTIME”参数配置为0，则告警监控时长受软参**DWORD507**控制，该软参用于控制扫描硬盘上缓存话单文件的周期。

### 8 配置N4接口计费消息相关控制参数。当阈值配置过小，比如流量阈值较低，会导致UPF在N4接口频繁上报计费消息，当NCG/CHF(OCS)性能不足响应较慢时，会导致UNC(GGSN/PGW-C/SMF)的N4接口上报消息堆积，超过最大可缓存的消息规格，会话被去激活。

```jinja2
{%- for item in set_n4chgmsgctrl_list -%}
    SET N4CHGMSGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.MSGCACHEEPDSW is not none -%}
        MSGCACHEEPDSW={{item.MSGCACHEEPDSW}},
    {%- endif -%}
    {%- if item.CACHEFULLACT is not none -%}
        CACHEFULLACT={{item.CACHEFULLACT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

