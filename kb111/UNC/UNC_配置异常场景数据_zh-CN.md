---
id: ''
name: 配置异常场景数据
ne_type: UNC
type: feature
description: GGSN/PGW-C与PCRF交互时，常见的异常场景如下：  * 基于号段选择PCRF分组失败    特定号段的用户激活时选择不到号段绑定的PCRF分组。该种情况通常是由于GGSN/PGW-C上未基于号段绑定PCRF分组。 * 等待PCRF响应超时    GGSN/PGW-C向PCRF发送CCR-I/U/T消息后，在Tx timer超时前，没有收到CCA响应消息。该种情况下可能是PCRF由于拥塞导致CCA回复失败，或者PCRF应用层故障导致无法正常回复CCA。DRA场景下还有可能是DRA的原因导致CCA消息丢失。 * Gx接口链路故障    GGSN/PGW-C和PCRF/DRA之间无法建立连接，包括传输层TCP链路或者Diameter链路，导致网元间无法正常交互。该种情况下可能是物理链路故障，也可能是对端PCRF/DRA的链路层故障导致Diameter心跳消息DWR/DWA无法正常维护。 * CCA消息中携带异常返回码    PCRF给GGSN/PGW-C回复的CCA-I/U/T响应消息中，如果Result-Code AVP或Experimental-Result-Code AVP携带了DIAMETER\_SUCCESS(2001)和DIAMETER\_LIMITED\_SUCCESS(2002)以外的异常返回码，比如3XXX，4XXX，5XXX，表明业务层存在问题，可根据返回码的标准定义排查异常。 * CCA-I消息中下发的PCC规则全部安装失败    按照协议要求，PCC用户成功激活的必要条件是必须安装有效的PCC规则。该场景中，PCRF成功响应CCA-I消息，也下发了PCC规则，但是PCC规则因未通过有效性检查而全部安装失败，例如PCRF下发的预定义规则未在网关上配置等。该种情况下通常是由于PCRF侧签约错误导致，此时GGSN/PGW-C会将该用户去活。 * CCA-I消息中未下发PCC规则    该场景中，PCRF成功响应CCA-I消息，但未下发PCC规则。该种情况下通常是由于用户开户但未签约业务导致。 * Gx failover    详细内容请参见Gx Failover功能。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109101 PCC基本功能","PCC基本功能（2G/3G/4G，基于Gx接口）","激活PCC基本功能","配置异常场景数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/PGW-C与PCRF交互时，常见的异常场景如下：* 基于号段选择PCRF分组失败  特定号段的用户激活时选择不到号段绑定的PCRF分组。该种情况通常是由于GGSN/PGW-C上未基于号段绑定PCRF分组。* 等待PCRF响应超时  GGSN/PGW-C向PCRF发送CCR-I/U/T消息后，在Tx timer超时前，没有收到CCA响应消息。该种情况下可能是PCRF由于拥塞导致CCA回复失败，或者PCRF应用层故障导致无法正常回复CCA。DRA场景下还有可能是DRA的原因导致CCA消息丢失。* Gx接口链路故障  GGSN/PGW-C和PCRF/DRA之间无法建立连接，包括传输层TCP链路或者Diameter链路，导致网元间无法正常交互。该种情况下可能是物理链路故障，也可能是对端PCRF/DRA的链路层故障导致Diameter心跳消息DWR/DWA无法正常维护。* CCA消息中携带异常返回码  PCRF给GGSN/PGW-C回复的CCA-I/U/T响应消息中，如果Result-Code AVP或Experimental-Result-Code AVP携带了DIAMETER\_SUCCESS(2001)和DIAMETER\_LIMITED\_SUCCESS(2002)以外的异常返回码，比如3XXX，4XXX，5XXX，表明业务层存在问题，可根据返回码的标准定义排查异常。* CCA-I消息中下发的PCC规则全部安装失败  按照协议要求，PCC用户成功激活的必要条件是必须安装有效的PCC规则。该场景中，PCRF成功响应CCA-I消息，也下发了PCC规则，但是PCC规则因未通过有效性检查而全部安装失败，例如PCRF下发的预定义规则未在网关上配置等。该种情况下通常是由于PCRF侧签约错误导致，此时GGSN/PGW-C会将该用户去活。* CCA-I消息中未下发PCC规则  该场景中，PCRF成功响应CCA-I消息，但未下发PCC规则。该种情况下通常是由于用户开户但未签约业务导致。* Gx failover  详细内容请参见Gx Failover功能。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成配置与PCRF对接数据。
* 完成配置动态PCC功能。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_pccfailaction_list:
      type: items
      properties:
        SELPEERFAILACT:
          name: '选择PCRF/PCF失败动作'
          type: string
          enum:
          - DEFAULT
          - FORBIDDEN
          - ROLLBACK
          required: false
          description: '配置激活过程中根据号段匹配选择PCRF/PCF-Group和realm失败情况下系统执行的动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - ROLLBACK
          required: false
          description: '配置激活过程中Gx链路故障、流控丢消息或响应超时情况下系统执行的动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELPEERLOCPCC:
          name: '选择PCRF/PCF失败回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SELPEERRDSPCC:
          name: '选择PCRF/PCF失败回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_pcctimer_list:
      type: items
      properties: {}
    add_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELPEERFAILACT:
          name: '选择PCF/PCRF失败动作'
          type: string
          enum:
          - DEFAULT
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        INITIALFAILACT:
          name: 'Initial流程故障处理动作'
          type: string
          enum:
          - FORBIDDEN
          - INHERIT
          - ROLLBACK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        INITFAILRDSPCC:
          name: 'Initial流程故障回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - INHERIT
          - ROLLBACK
          - TERMINATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        INITFAILLOCPCC:
          name: 'Initial流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        SELPEERLOCPCC:
          name: '选择PCF/PCRF失败回滚为Local PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
        SELPEERRDSPCC:
          name: '选择PCF/PCRF失败回滚为RADIUS PCC用户类型'
          type: string
          enum:
          - LOCAL_PCC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL_PCC
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN下的故障处理动作。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_resultcodectrl_list:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - INTFTYPE_GX
          - INTFTYPE_N7
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '配置UNC收到异常返回码后执行何种操作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GXRESULTCODEVAL:
          name: 'Gx返回码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITACTION:
          name: 'Intial流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - INHERIT
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPDATEACTION:
          name: 'Update流程处理动作'
          type: string
          enum:
          - CONTINUE
          - FAILOVER
          - INHERIT
          - INHERIT_PCC
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TERMINACTION:
          name: 'Terminate流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INITHOLDTMSW:
          name: 'Initial流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        N7RESULTCODEVAL:
          name: 'N7返回码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REACTREQ:
          name: '重新激活请求'
          type: string
          enum:
          - DEFAULT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        UPDHOLDTMSW:
          name: 'Update流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_resultcodectrl_list_1:
      type: items
      properties:
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - INTFTYPE_GX
          - INTFTYPE_N7
          required: true
          description: ''
          data_source: '对端协商'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '配置UNC收到异常返回码后执行何种操作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GXRESULTCODEVAL:
          name: 'Gx返回码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DIRECTINITACT:
          name: '直连对端Initial流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - FAILOVERALL
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INVALID
        DIRECTUPDACT:
          name: '直连对端Update流程处理动作'
          type: string
          enum:
          - CONTINUE
          - FAILOVER
          - FAILOVERALL
          - INHERIT_PCC
          - INVALID
          - LOCALPCC
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INVALID
        DIRECTTERMINACT:
          name: '直连对端Terminate流程处理动作'
          type: string
          enum:
          - DEFAULT
          - FAILOVER
          - FAILOVERALL
          - INVALID
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INVALID
        DIRECTINITHTSW:
          name: '直连对端Initial流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DIRECTREACTREQ:
          name: '直连对端重激活请求'
          type: string
          enum:
          - DEFAULT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        DIRECTUPDHTSW:
          name: '直连对端Update流程回滚后使能Holding-Time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        N7RESULTCODEVAL:
          name: 'N7返回码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pcctimer_list_1:
      type: items
      properties: {}
    set_fhbypass_list:
      type: items
      properties: {}
  examples:
    set_pccfailaction_list:
    - SELPEERFAILACT: DEFAULT
      INITIALFAILACT: ROLLBACK
      INITFAILLOCPCC: LOCAL_PCC
      INITFAILRDSPCC: LOCAL_PCC
      UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: LOCAL_PCC
      SELPEERLOCPCC: LOCAL_PCC
      SELPEERRDSPCC: LOCAL_PCC
    set_pcctimer_list:
    - {}
    add_pcctemplate_list:
    - PCCTEMPNAME: 'templatetest'
      SELPEERFAILACT: DEFAULT
      INITIALFAILACT: ROLLBACK
      INITFAILRDSPCC: LOCAL_PCC
      UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: LOCAL_PCC
      INITFAILLOCPCC: LOCAL_PCC
      SELPEERLOCPCC: LOCAL_PCC
      SELPEERRDSPCC: LOCAL_PCC
    set_apnpccfunc_list:
    - APN: 'apn-test'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
      PCCTEMPLATE: 'templatetest'
    add_resultcodectrl_list:
    - PCCTEMPLATE: 'templatetest'
      INTFTYPE: INTFTYPE_GX
      VENDORID: 0
      GXRESULTCODEVAL: '3xxx'
      INITACTION: FAILOVER
      UPDATEACTION: FAILOVER
      TERMINACTION: FAILOVER
      INITHOLDTMSW: DISABLE
      N7RESULTCODEVAL: ''
      REACTREQ: DEFAULT
      UPDHOLDTMSW: DISABLE
    add_resultcodectrl_list_1:
    - PCCTEMPLATE: 'templatetest'
      INTFTYPE: INTFTYPE_GX
      VENDORID: 0
      GXRESULTCODEVAL: '3xxx'
      DIRECTINITACT: FAILOVER
      DIRECTUPDACT: FAILOVER
      DIRECTTERMINACT: FAILOVER
      DIRECTINITHTSW: DISABLE
      DIRECTREACTREQ: DEFAULT
      DIRECTUPDHTSW: DISABLE
      N7RESULTCODEVAL: ''
    set_pcctimer_list_1:
    - {}
    set_fhbypass_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于号段选择PCRF分组失败/等待PCRF响应超时/Gx接口链路故障。

#### 1.1 如果基于全局控制GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，请执行步骤 2～步骤 3。

#### 1.2 如果基于APN控制GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，请执行步骤 2～步骤 5。

#### 1.3 进入“MML命令行-UNC”窗口。

#### 1.4 配置GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，缺省使用默认值。

```jinja2
{%- for item in set_pccfailaction_list -%}
    SET PCCFAILACTION:
    {#- --- 可选参数 --- -#}
    {%- if item.SELPEERFAILACT is not none -%}
        SELPEERFAILACT={{item.SELPEERFAILACT}},
    {%- endif -%}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERLOCPCC is not none -%}
            SELPEERLOCPCC={{item.SELPEERLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERRDSPCC is not none -%}
            SELPEERRDSPCC={{item.SELPEERRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 **可选：**配置PCC用户回滚后的在线保持时长，缺省使用默认值。

```jinja2
{%- if is_optional_pcc_user_rollback_hold_duration -%}
    SET PCCTIMER:
    ;
{%- endif -%}
```

#### 1.6 配置PCC Template中GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式以及PCC用户回滚后的在线保持时长。若不配置，GGSN/PGW-C默认继承全局配置。

```jinja2
{%- for item in add_pcctemplate_list -%}
    ADD PCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    PCCTEMPNAME="{{item.PCCTEMPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SELPEERFAILACT is not none -%}
        SELPEERFAILACT={{item.SELPEERFAILACT}},
    {%- endif -%}
    {%- if item.INITIALFAILACT is not none -%}
        INITIALFAILACT={{item.INITIALFAILACT}},
    {%- endif -%}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILRDSPCC is not none -%}
            INITFAILRDSPCC={{item.INITFAILRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INITIALFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.INITIALFAILACT == 'ROLLBACK' -%}
        {%- if item.INITFAILLOCPCC is not none -%}
            INITFAILLOCPCC={{item.INITFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERLOCPCC is not none -%}
            SELPEERLOCPCC={{item.SELPEERLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SELPEERFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.SELPEERFAILACT == 'ROLLBACK' -%}
        {%- if item.SELPEERRDSPCC is not none -%}
            SELPEERRDSPCC={{item.SELPEERRDSPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 当基于APN粒度设置GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式，需要将PCCTEMPLATE绑定到APN下。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    {%- if item.PCCTEMPLATE is not none -%}
        PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 CCA消息中携带异常返回码。

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 根据运营商规划配置GGSN/PGW-C收到各种结果码后执行何种操作。若不配置，GGSN/PGW-C使用系统默认处理方式。

```jinja2
{%- for item in add_resultcodectrl_list -%}
    ADD RESULTCODECTRL:
    {#- --- 必选参数 --- -#}
    PCCTEMPLATE="{{item.PCCTEMPLATE}}",
    INTFTYPE={{item.INTFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.INITACTION is not none -%}
        INITACTION={{item.INITACTION}},
    {%- endif -%}
    {%- if item.UPDATEACTION is not none -%}
        UPDATEACTION={{item.UPDATEACTION}},
    {%- endif -%}
    {%- if item.TERMINACTION is not none -%}
        TERMINACTION={{item.TERMINACTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        VENDORID={{item.VENDORID}},
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
        GXRESULTCODEVAL="{{item.GXRESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件必选：INTFTYPE=INTFTYPE_N7 时必选 --- -#}
    {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
        N7RESULTCODEVAL="{{item.N7RESULTCODEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INITACTION=LOCALPCC 时可选 --- -#}
    {%- if item.INITACTION == 'LOCALPCC' -%}
        {%- if item.INITHOLDTMSW is not none -%}
            INITHOLDTMSW={{item.INITHOLDTMSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEACTION=TERMINATE 时可选 --- -#}
    {%- if item.UPDATEACTION == 'TERMINATE' -%}
        {%- if item.REACTREQ is not none -%}
            REACTREQ={{item.REACTREQ}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPDATEACTION=LOCALPCC/INHERIT_PCC 时可选 --- -#}
    {%- if item.UPDATEACTION in ['LOCALPCC', 'INHERIT_PCC'] -%}
        {%- if item.UPDHOLDTMSW is not none -%}
            UPDHOLDTMSW={{item.UPDHOLDTMSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 **可选：**配置GGSN/PGW-C收到直连对端返回码后执行何种操作。

```jinja2
{%- if is_optional_direct_peer_return_code_action -%}
    {%- for item in add_resultcodectrl_list_1 -%}
        ADD RESULTCODECTRL:
        {#- --- 必选参数 --- -#}
        PCCTEMPLATE="{{item.PCCTEMPLATE}}",
        INTFTYPE={{item.INTFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DIRECTINITACT is not none -%}
            DIRECTINITACT={{item.DIRECTINITACT}},
        {%- endif -%}
        {%- if item.DIRECTUPDACT is not none -%}
            DIRECTUPDACT={{item.DIRECTUPDACT}},
        {%- endif -%}
        {%- if item.DIRECTTERMINACT is not none -%}
            DIRECTTERMINACT={{item.DIRECTTERMINACT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
        {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
            VENDORID={{item.VENDORID}},
        {%- endif -%}
        {#- --- 条件必选：INTFTYPE=INTFTYPE_GX 时必选 --- -#}
        {%- if item.INTFTYPE == 'INTFTYPE_GX' -%}
            GXRESULTCODEVAL="{{item.GXRESULTCODEVAL}}",
        {%- endif -%}
        {#- --- 条件必选：INTFTYPE=INTFTYPE_N7 时必选 --- -#}
        {%- if item.INTFTYPE == 'INTFTYPE_N7' -%}
            N7RESULTCODEVAL="{{item.N7RESULTCODEVAL}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DIRECTINITACT=LOCALPCC 时可选 --- -#}
        {%- if item.DIRECTINITACT == 'LOCALPCC' -%}
            {%- if item.DIRECTINITHTSW is not none -%}
                DIRECTINITHTSW={{item.DIRECTINITHTSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DIRECTUPDACT=TERMINATE 时可选 --- -#}
        {%- if item.DIRECTUPDACT == 'TERMINATE' -%}
            {%- if item.DIRECTREACTREQ is not none -%}
                DIRECTREACTREQ={{item.DIRECTREACTREQ}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DIRECTUPDACT=INHERIT_PCC/LOCALPCC 时可选 --- -#}
        {%- if item.DIRECTUPDACT in ['INHERIT_PCC', 'LOCALPCC'] -%}
            {%- if item.DIRECTUPDHTSW is not none -%}
                DIRECTUPDHTSW={{item.DIRECTUPDHTSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 **可选：**如果设置GGSN/PGW-C收到直连对端返回码后执行FAILOVERALL动作，可配置FAILOVERALL的持续时长，缺省使用默认值。

```jinja2
{%- if is_optional_failoverall_duration -%}
    SET PCCTIMER:
    ;
{%- endif -%}
```

#### GGSN/PGW-C根据指定返回码对所有用户执行failover动作后，已在线和新激活的用户使用备PCRF进行交互。当Failover All-sessions定时器到达后，如果主PCRF可用，新激活用户将使用主PCRF进行交互，已在线用户仍使用备PCRF进行交互，否则均使用备PCRF进行交互。

### 3 进入“MML命令行-UNC”窗口。故障场景紧急处理：配置等待PCRF响应超时、Gx接口链路故障、CCA消息中携带异常返回码时的一键放通功能。

```jinja2
SET FHBYPASS:
;
```

#### 3.1 本命令优先级高于**SET PCCFAILACTION**和**ADD RESULTCODECTRL**。

#### 3.2 由于配置**SET FHBYPASS**将影响用户的控制策略，只有在取得了客户的书面认可后方可使用。

#### 3.3 GGSN/PGW-C支持如下方式配置故障恢复后的处理。方式1针对全部放通用户，可能存在恢复不及时的情况，推荐使用方式2。

##### 3.3.1 - 方式1：通过**SET FHBYPASS** “HOLDINGTIME”控制对放通用户的后续处理。

##### 3.3.2 - 方式2：通过**DSP CPPDPCHGINFO**查询被放通用户的归属信息。

