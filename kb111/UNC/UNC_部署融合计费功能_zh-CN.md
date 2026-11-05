---
id: ''
name: 部署融合计费功能
ne_type: UNC
type: feature
description: 该任务用于指导操作人员完成5G融合计费所需的相关参数。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","NCG配置","部署融合计费功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于指导操作人员完成5G融合计费所需的相关参数。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ccpfot_list:
      type: items
      properties:
        FOTNM:
          name: 'Failover模板标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '在线计费CC处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FOENABLE:
          name: '是否支持Failover开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: TRUE
        RESPPLCY:
          name: 'NCG代应答时的配额类型选择'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'TIME-1&SUMVOLUME-1'
        UVDQ:
          name: '默认上行流量额度(KB)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 2560
        DVDQ:
          name: '默认下行流量额度(KB)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 2560
        EVTQ:
          name: '默认事件额度(次)'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        FH:
          name: 'FailureHandling枚举值'
          type: string
          enum:
          - TERMINATE
          - CONTINUE
          - RETRYANDTERM
          - ALWAYSCONTINUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CONTINUE
        TQ:
          name: '默认时长额度(s)'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
    add_ccpccact_list:
      type: items
      properties:
        CCTYPE:
          name: 'CC类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '离线计费CC处理动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CHGCHAR:
          name: '指定计费属性值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        CHGCHARMASK:
          name: '指定计费属性掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: '0xFFFF'
        FOTNM:
          name: 'Failover模板标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FWDOCSENABLE:
          name: '是否转发OCS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ccprcact_list:
      type: items
      properties:
        RCTYPE:
          name: 'RC类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          - TIMEOUT
          - LINKFAULT
          required: true
          description: '异常返回码处理动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CODETYPE:
          name: '指定异常返回码类型'
          type: integer
          minimum:
          - 300
          - 65535
          - 0
          maximum:
          - 999
          - 65535
          - 0
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FOTNM:
          name: 'Failover模板标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERUNAVAILABLE:
          name: '代表对端不可用'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_agffuncpara_list:
      type: items
      properties:
        OCSRETRYCNT:
          name: '计费消息重发次数'
          type: integer
          minimum: 0
          maximum: 1
          required: true
          description: '配置AGF的功能参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OCSDISCPLCY:
          name: 'OCS选择策略'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CDFIPKGPLCY:
          name: 'CDF I包抄送策略'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ccptimer_list:
      type: items
      properties:
        TID:
          name: '定时器标识'
          type: string
          enum:
          - CCTIMEOUT
          - UCITIMER
          - RECOVERINTERVAL
          - SYSLEVELRECOVERINTERVAL
          - ONLINECDFRSP
          - OFFLINECDFRSP
          - RECOVERTOPOREQ
          required: true
          description: 'OCS超时时长配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '定时器的时长'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ccptimer_list_1:
      type: items
      properties:
        TID:
          name: '定时器标识'
          type: string
          enum:
          - CCTIMEOUT
          - UCITIMER
          - RECOVERINTERVAL
          - SYSLEVELRECOVERINTERVAL
          - ONLINECDFRSP
          - OFFLINECDFRSP
          - RECOVERTOPOREQ
          required: true
          description: '尝试恢复OCS时长配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '定时器的时长'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ccpfot_list:
    - FOTNM: 'FR1'
      FOENABLE: TRUE
      RESPPLCY: TIME-0&SUMVOLUME-1
      UVDQ: 102400
      DVDQ: 102400
      EVTQ: 20
      FH: CONTINUE
      TQ: 1800
    add_ccpccact_list:
    - CCTYPE: VALUE
      CHGCHAR: '0x0400'
      CHGCHARMASK: '0xFFFF'
      FOTNM: 'FR1'
      FWDOCSENABLE: TRUE
    add_ccprcact_list:
    - RCTYPE: VALUE
      CODETYPE: 408
      FOTNM: 'FR1'
      PEERUNAVAILABLE: FALSE
    set_agffuncpara_list:
    - OCSRETRYCNT: 0
      OCSDISCPLCY: SUPI-0&GPSI-1
      CDFIPKGPLCY: TRUE
    set_ccptimer_list:
    - TID: CCTIMEOUT
      VALUE: 3
    set_ccptimer_list_1:
    - TID: RECOVERINTERVAL
      VALUE: 300
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置默认Failover模板。

```jinja2
{%- for item in add_ccpfot_list -%}
    ADD CCPFOT:
    {#- --- 必选参数 --- -#}
    FOTNM="{{item.FOTNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FOENABLE is not none -%}
        FOENABLE={{item.FOENABLE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.RESPPLCY is not none -%}
            RESPPLCY={{item.RESPPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.UVDQ is not none -%}
            UVDQ={{item.UVDQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.DVDQ is not none -%}
            DVDQ={{item.DVDQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.EVTQ is not none -%}
            EVTQ={{item.EVTQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.FH is not none -%}
            FH={{item.FH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FOENABLE=TRUE 时可选 --- -#}
    {%- if item.FOENABLE == 'TRUE' -%}
        {%- if item.TQ is not none -%}
            TQ={{item.TQ}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置基于CC值的处理模板

```jinja2
{%- for item in add_ccpccact_list -%}
    ADD CCPCCACT:
    {#- --- 必选参数 --- -#}
    CCTYPE={{item.CCTYPE}},
    FOTNM="{{item.FOTNM}}",
    FWDOCSENABLE={{item.FWDOCSENABLE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CCTYPE=VALUE 时必选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        CHGCHAR="{{item.CHGCHAR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.CHGCHARMASK is not none -%}
            CHGCHARMASK="{{item.CHGCHARMASK}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置基于异常返回码的处理模板

```jinja2
{%- for item in add_ccprcact_list -%}
    ADD CCPRCACT:
    {#- --- 必选参数 --- -#}
    RCTYPE={{item.RCTYPE}},
    FOTNM="{{item.FOTNM}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RCTYPE=VALUE 时必选 --- -#}
    {%- if item.RCTYPE == 'VALUE' -%}
        CODETYPE={{item.CODETYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RCTYPE=VALUE 时可选 --- -#}
    {%- if item.RCTYPE == 'VALUE' -%}
        {%- if item.PEERUNAVAILABLE is not none -%}
            PEERUNAVAILABLE={{item.PEERUNAVAILABLE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置AGF功能参数。此处配置create消息生成话单、NCG等待OCS计费响应超时后不重发响应超时的计费请求，根据GPSI选择OCS。

```jinja2
{%- for item in set_agffuncpara_list -%}
    SET AGFFUNCPARA:
    {#- --- 必选参数 --- -#}
    OCSRETRYCNT={{item.OCSRETRYCNT}},
    {#- --- 可选参数 --- -#}
    {%- if item.OCSDISCPLCY is not none -%}
        OCSDISCPLCY={{item.OCSDISCPLCY}},
    {%- endif -%}
    {%- if item.CDFIPKGPLCY is not none -%}
        CDFIPKGPLCY={{item.CDFIPKGPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 CHF(OCS)超时时长配置，默认值为3秒。

```jinja2
{%- for item in set_ccptimer_list -%}
    SET CCPTIMER:
    {#- --- 必选参数 --- -#}
    TID={{item.TID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VALUE is not none -%}
        VALUE={{item.VALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 主备CHF(OCS)故障后NCG再次尝试转发CHF(OCS)时长配置，默认值为5分钟。

```jinja2
{%- for item in set_ccptimer_list_1 -%}
    SET CCPTIMER:
    {#- --- 必选参数 --- -#}
    TID={{item.TID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VALUE is not none -%}
        VALUE={{item.VALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

