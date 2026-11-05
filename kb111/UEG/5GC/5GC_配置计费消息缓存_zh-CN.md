---
id: ''
name: 配置计费消息缓存
ne_type: UEG
type: feature
description: 应急接入场景下，为避免用户体验变差，可以采用不做配额管理的计费方式，允许用户接入继续使用业务，并缓存计费信息。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","配置业务数据（UEG）","计费功能配置","部署应急SMF","配置计费消息缓存"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
应急接入场景下，为避免用户体验变差，可以采用不做配额管理的计费方式，允许用户接入继续使用业务，并缓存计费信息。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          data_source: '本端规划'
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
          description: '当CHF不可用，SMF允许用户继续使用业务，不再进行配额管理和配额上报。  固定配置，开启计费消息缓存的前提条件。'
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
        CNVCHGRECOVER:
          name: '融合计费自动恢复功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置CHF故障恢复后重建计费会话功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '融合计费自动恢复间隔 (分钟)'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pduscact_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '融合计费模板名称，配置融合计费模板已经配置。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REPLAYRATE:
          name: '融合计费消息回放的速率(个/秒)'
          type: integer
          minimum: 10
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_stgtrigger_list:
      type: items
      properties:
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: '融合计费消息缓存期间的trigger，全局配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: ''
          data_source: '本端规划'
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
    set_stgalarmctrl_list:
      type: items
      properties:
        ALMTHD:
          name: '告警产生门限(KB)'
          type: integer
          minimum: 0
          maximum: 1048576
          required: false
          description: '配置告警产生门限。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MONITORTIME:
          name: '告警监控时长(分)'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '配置告警监控时长。'
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
          description: '控制单个会话的N4计费消息缓存池满时（20条消息），是否扩展消息缓存池规格到40条消息，最多支持100个会话进行扩展。如果该会话已缓存的N4计费消息中存在丢中间消息时，该会话不可以扩展。'
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
      CNVCHGRECOVER: ENABLE
      RECOVERINTERVAL: 5
    mod_pduscact_list:
    - CCTMPLTNAME: 'cct-test'
      CODETYPE: VALUE
      STATUSCODE: 502
      SCACT: FAILOVER
    set_n40msgstg_list:
    - STGSWITCH: ENABLE
      REPLAYINTERVAL: 30
      REPLAYRATE: 500
    set_stgtrigger_list:
    - VOLUMELIMIT: IMMEDIATE
      PDUVOLUMELIMIT: 500
    set_cnvrgdchgpara_list:
    - CHGDATAREFGEN: SMF
    set_stgalarmctrl_list:
    - ALMTHD: 5120
      MONITORTIME: 60
    set_n4chgmsgctrl_list:
    - MSGCACHEEPDSW: ENABLE
      CACHEFULLACT: CONTINUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置当CHF故障，SMF放通业务，不进行配额管理和配额上报；配置当CHF故障恢复后重建计费会话功能。

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
    {%- if item.CNVCHGRECOVER is not none -%}
        CNVCHGRECOVER={{item.CNVCHGRECOVER}},
    {%- endif -%}
    {%- if item.RECOVERINTERVAL is not none -%}
        RECOVERINTERVAL={{item.RECOVERINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置当SMF收到异常返回码时的动作。

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
    ;
{%- endfor -%}
```

### 4 配置计费消息缓存期间的trigger。

```jinja2
{%- for item in set_stgtrigger_list -%}
    SET STGTRIGGER:
    {#- --- 可选参数 --- -#}
    {%- if item.VOLUMELIMIT is not none -%}
        VOLUMELIMIT={{item.VOLUMELIMIT}},
    {%- endif -%}
    {%- if item.PDUVOLUMELIMIT is not none -%}
        PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
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
    ;
{%- endfor -%}
```

### 6 配置融合计费话单缓存告警上报的控制参数。

### ****SET STGALARMCTRL****

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

#### 6.1 + **SET STGALARMCTRL**命令的“ALMTHD”参数控制SMF上报**“ALM-81025 话单缓存”**告警的缓存文件占用空间阈值。缓存文件超过该阈值时，上报告警；缓存文件全部被回放后，清除告警。

#### 6.2 + **SET STGALARMCTRL**命令的“MONITORTIME”参数控制告警监控时长，当SMF检查到缓存文件存在且不超过占用空间阈值时，超过告警监控时长后，SMF上报**“ALM-81025 话单缓存”**告警。建议该参数配置为**SET N40MSGSTG**命令配置的融合计费消息回放的最小间隔的2倍以上。

### 如果“MONITORTIME”参数配置为0，则告警监控时长受软参**DWORD507**控制，该软参用于控制扫描硬盘上缓存文件的周期。

### 7 配置N4接口计费消息相关控制参数。当阈值配置过小，比如流量阈值较低，会导致N4接口频繁上报阈值到，当CHF性能不足响应较慢时，会导致N4接口上报消息堆积，超过最大可缓存的消息规格，用户被去活。该命令主要用于配置SMF在突发和持续高带宽下载场景，用户不被去活。

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

