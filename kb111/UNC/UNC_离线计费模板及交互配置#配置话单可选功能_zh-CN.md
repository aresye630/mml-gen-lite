---
id: ''
name: 配置话单可选功能
ne_type: UNC
type: feature
description: 本指导描述UNC上某些可选离线计费功能的配置过程。  UNC上的话单可选功能包含：  * CCFH后强制产生话单    在系统测试时，如果UNC上设置的话单产生条件未到，还不具备自动产生话单时，可采用命令强制产生话单。 * 最后活动时间（LastActivity）计费    基于时长的计费模式下，用户可能由于idle去激活而较长时间没有业务访问，如果按当前时长计费会有向用户多收费嫌疑。可通过在话单的扩展字段RecordExtensions中记录最后一个业务报文通过的时间，由此计算用户访问业务的实际时长且据此收费，可优化时长计费模式。 * 抑制零流量话单    为减少无效话单的数量，如果用户一段时间内未进行业务，即业务访问流量为零，则忽略本次产生话单的计费事件，不产生中间话单。 * 费率切换后强制生成话单    离线计费模板参数CDRTRIGMAXCHNG配置为ENABLE，参数CONDITIONCHANGE参数配置为1时，UNC处理费率切换时会对费率切换前的使用量产生一张话单后，如果费率切换后的用量不强制产生一张话单，会导致费率切换后大量用户时间阈值同时触发，产生大量话单，导致UNC CPU使用率大幅波动，同时对CG产生冲击。为避免此现象发生，建议配置费率切换后强制生成话单。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","离线计费配置","离线计费模板及交互配置","配置话单可选功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述UNC上某些可选离线计费功能的配置过程。UNC上的话单可选功能包含：* CCFH后强制产生话单  在系统测试时，如果UNC上设置的话单产生条件未到，还不具备自动产生话单时，可采用命令强制产生话单。* 最后活动时间（LastActivity）计费  基于时长的计费模式下，用户可能由于idle去激活而较长时间没有业务访问，如果按当前时长计费会有向用户多收费嫌疑。可通过在话单的扩展字段RecordExtensions中记录最后一个业务报文通过的时间，由此计算用户访问业务的实际时长且据此收费，可优化时长计费模式。* 抑制零流量话单  为减少无效话单的数量，如果用户一段时间内未进行业务，即业务访问流量为零，则忽略本次产生话单的计费事件，不产生中间话单。* 费率切换后强制生成话单  离线计费模板参数CDRTRIGMAXCHNG配置为ENABLE，参数CONDITIONCHANGE参数配置为1时，UNC处理费率切换时会对费率切换前的使用量产生一张话单后，如果费率切换后的用量不强制产生一张话单，会导致费率切换后大量用户时间阈值同时触发，产生大量话单，导致UNC CPU使用率大幅波动，同时对CG产生冲击。为避免此现象发生，建议配置费率切换后强制生成话单。

## 必备事项
前提条件

请仔细阅读Ga/Gy接口离线/在线计费。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ofccdrpara_list:
      type: items
      properties:
        CCFHCDRSW:
          name: 'CCFH强制产生话单开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。  说明：  此功能为定制功能，通过话单中的Charging Characteristics区分CCFH前后的话单。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCFHCDRCC:
          name: 'CCFH强制产生话单填充的Charging Characteristics值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSFCIFORMAT:
          name: 'OCS故障导致用户离线后产生的话单pSFreeFormatData格式'
          type: string
          enum:
          - ASCII
          - HEX
          required: false
          description: '配置用户转离线后，pSFreeFormatData字段在话单中的填写格式。  说明：  此功能为定制功能，仅在特定局点使用。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        R6EGCDRCCFHSW:
          name: 'R6 eGCRD支持CCFH强制生成话单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置CCFH发生时是否支持强制产生R6 eGCDR话单。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    mod_ofctemplate_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TQM:
          name: '时长配额机制'
          type: string
          enum:
          - CTP
          - OPERATOR_CTP
          - QCT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCTVALUE:
          name: 'QCT时长（秒）'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTIMEFORMAT:
          name: '话单时间格式'
          type: string
          enum:
          - LOCAL_TIME
          - UTC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BTIVALUE:
          name: 'BTI时长（秒）'
          type: integer
          minimum: 60
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ofccdrpara_list_1:
      type: items
      properties:
        LASTACTIVITYSW:
          name: 'Last Activity功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置使能Last Activity计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_zerochgskipsw_list:
      type: items
      properties:
        ZEROCHGSKIPSW:
          name: '零流量计费事件忽略总开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置使能抑制零流量话单产生。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SKIPCCFH:
          name: '忽略CCFH'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPFINALCDR:
          name: '忽略去激活话单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPFOCGENCDR:
          name: '忽略强制生成话单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPPLMNCHNG:
          name: '忽略Serving Node PLMN标识改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPPSFCI:
          name: '忽略PS-Furnish-Charging-Information改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPQOSCHNG:
          name: '忽略QoS改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPRATCHNG:
          name: '忽略RAT更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPSNCHNG:
          name: '忽略Serving Node地址改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPTARIFFCHNG:
          name: '忽略费率切换'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPTIMETHRESH:
          name: '忽略时间阈值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPTMZONECHNG:
          name: '忽略MS时区改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPULIBASEDCHG:
          name: '忽略基于位置的计费订阅和取消'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SKIPULICHNG:
          name: '忽略ULI改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ofccdrpara_list_2:
      type: items
      properties:
        CDRAFTERTCSW:
          name: '费率切换后强制产生话单开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当费率切换后的使用量不满足产生话单的条件时，是否对费率切换后的使用量强制产生一张话单。  说明：  **ADD OFCTEMPLATE**命令的参数“CDRTRIGMAXCHNG”配置为“ENABLE”且参数“CONDITIONCHANGE”参数配置为“1”时，该参数建议配置为ENABLE'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRAFTERTCCAUSE:
          name: '费率切换后强制产生话单的关闭原因'
          type: string
          enum:
          - MANAGEMENT_INTERVENTION
          - MAX_CHANGE_COND
          required: false
          description: '配置费率切换后的使用量强制产生的话单关闭原因值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_ofccdrpara_list:
    - CCFHCDRSW: ENABLE
      CCFHCDRCC: '0x1000'
      PSFCIFORMAT: HEX
      R6EGCDRCCFHSW: DISABLE
    mod_ofctemplate_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      TQM: QCT
      QCTVALUE: 0
      CDRTIMEFORMAT: UTC
      BTIVALUE: ''
    set_ofccdrpara_list_1:
    - LASTACTIVITYSW: ENABLE
    set_zerochgskipsw_list:
    - ZEROCHGSKIPSW: ENABLE
      SKIPCCFH: ''
      SKIPFINALCDR: ''
      SKIPFOCGENCDR: ''
      SKIPPLMNCHNG: ''
      SKIPPSFCI: ''
      SKIPQOSCHNG: ''
      SKIPRATCHNG: ''
      SKIPSNCHNG: ''
      SKIPTARIFFCHNG: ''
      SKIPTIMETHRESH: ''
      SKIPTMZONECHNG: ''
      SKIPULIBASEDCHG: ''
      SKIPULICHNG: ''
    set_ofccdrpara_list_2:
    - CDRAFTERTCSW: ENABLE
      CDRAFTERTCCAUSE: MANAGEMENT_INTERVENTION
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在线计费CCFH处理时是否强制产生话单，以及强制产生话单时话单中charging characteristic字段的取值、R6版本的eG-CDR是否支持CCFH处理。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CCFHCDRSW is not none -%}
        CCFHCDRSW={{item.CCFHCDRSW}},
    {%- endif -%}
    {%- if item.PSFCIFORMAT is not none -%}
        PSFCIFORMAT={{item.PSFCIFORMAT}},
    {%- endif -%}
    {%- if item.R6EGCDRCCFHSW is not none -%}
        R6EGCDRCCFHSW={{item.R6EGCDRCCFHSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCFHCDRSW=ENABLE 时可选 --- -#}
    {%- if item.CCFHCDRSW == 'ENABLE' -%}
        {%- if item.CCFHCDRCC is not none -%}
            CCFHCDRCC="{{item.CCFHCDRCC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置最后活动时间（LastActivity）计费。

#### 2.1 配置OFCTemplate使产生话单的时间格式为UTC时间。

```jinja2
{%- for item in mod_ofctemplate_list -%}
    MOD OFCTEMPLATE:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TQM is not none -%}
        TQM={{item.TQM}},
    {%- endif -%}
    {%- if item.CDRTIMEFORMAT is not none -%}
        CDRTIMEFORMAT={{item.CDRTIMEFORMAT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TQM=QCT 时必选 --- -#}
    {%- if item.TQM == 'QCT' -%}
        QCTVALUE={{item.QCTVALUE}},
    {%- endif -%}
    {#- --- 条件必选：TQM=CTP/OPERATOR_CTP 时必选 --- -#}
    {%- if item.TQM in ['CTP', 'OPERATOR_CTP'] -%}
        BTIVALUE={{item.BTIVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### LastActivity计费话单时间格式只支持UTC时间。

#### 2.2 配置使能离线计费使用LastActivity计费功能。

```jinja2
{%- for item in set_ofccdrpara_list_1 -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.LASTACTIVITYSW is not none -%}
        LASTACTIVITYSW={{item.LASTACTIVITYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置抑制零流量话单产生开关。

```jinja2
{%- for item in set_zerochgskipsw_list -%}
    SET ZEROCHGSKIPSW:
    {#- --- 必选参数 --- -#}
    ZEROCHGSKIPSW={{item.ZEROCHGSKIPSW}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPCCFH is not none -%}
            SKIPCCFH={{item.SKIPCCFH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPFINALCDR is not none -%}
            SKIPFINALCDR={{item.SKIPFINALCDR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPFOCGENCDR is not none -%}
            SKIPFOCGENCDR={{item.SKIPFOCGENCDR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPPLMNCHNG is not none -%}
            SKIPPLMNCHNG={{item.SKIPPLMNCHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPPSFCI is not none -%}
            SKIPPSFCI={{item.SKIPPSFCI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPQOSCHNG is not none -%}
            SKIPQOSCHNG={{item.SKIPQOSCHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPRATCHNG is not none -%}
            SKIPRATCHNG={{item.SKIPRATCHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPSNCHNG is not none -%}
            SKIPSNCHNG={{item.SKIPSNCHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPTARIFFCHNG is not none -%}
            SKIPTARIFFCHNG={{item.SKIPTARIFFCHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPTIMETHRESH is not none -%}
            SKIPTIMETHRESH={{item.SKIPTIMETHRESH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPTMZONECHNG is not none -%}
            SKIPTMZONECHNG={{item.SKIPTMZONECHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPULIBASEDCHG is not none -%}
            SKIPULIBASEDCHG={{item.SKIPULIBASEDCHG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ZEROCHGSKIPSW=ENABLE 时可选 --- -#}
    {%- if item.ZEROCHGSKIPSW == 'ENABLE' -%}
        {%- if item.SKIPULICHNG is not none -%}
            SKIPULICHNG={{item.SKIPULICHNG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 费率切换后强制生成话单。

```jinja2
{%- for item in set_ofccdrpara_list_2 -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CDRAFTERTCSW is not none -%}
        CDRAFTERTCSW={{item.CDRAFTERTCSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CDRAFTERTCSW=ENABLE 时可选 --- -#}
    {%- if item.CDRAFTERTCSW == 'ENABLE' -%}
        {%- if item.CDRAFTERTCCAUSE is not none -%}
            CDRAFTERTCCAUSE={{item.CDRAFTERTCCAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

