---
id: GWFD-023801
name: 激活端到端用户跟踪（5G）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活端到端用户跟踪的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","网络OM增强","GWFD-023801 端到端用户跟踪","激活端到端用户跟踪(MME/SGW-C/PGW-C/AMF/SMF)","激活端到端用户跟踪（5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活端到端用户跟踪的操作过程。

## 必备事项
前提条件

* 请仔细阅读4G网络端到端跟踪特性概述和5G网络端到端跟踪特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_fwsoftparabits_list:
      type: items
      properties:
        DWORDNUM:
          name: 'DWORD参数索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARATYPE:
          name: '数据类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
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
    set_ngmmfunc_list:
      type: items
      properties:
        E2ESW:
          name: '全网跟踪开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '在本开关打开的情况下，AMF会从UDM获取全网跟踪的指示，并将获取到的全网跟踪的指示分发给SMF、PCF、NG-RAN等周边网络节点。  说明：  当网络中有任意一个UDM不支持Trace Data时，需要通过**LST NGMMFUNC**命令检查是否关闭了AMF向UDM查询或者订阅TraceData的开关，避免造成业务流程异常。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '设置SMF软件参数比特位。配置SMF是否向UDM单独获取和订阅Trace Data：  * DWORD1001 BIT31 控制无I-SMF场景下SMF是否向UDM单独获取和订阅Trace Data * DWORD1001 BIT32 控制I-SMF/V-SMF存在场景下SMF是否向UDM单独获取和订阅Trace Data'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwsoftparabits_list_1:
      type: items
      properties:
        DWORDNUM:
          name: 'DWORD参数索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARATYPE:
          name: '数据类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
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
    set_ngmmfunc_list_1:
      type: items
      properties:
        E2ESW:
          name: '全网跟踪开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '在本开关打开的情况下，AMF会从UDM获取全网跟踪的指示，并将获取到的全网跟踪的指示分发给SMF、PCF、NG-RAN等周边网络节点。  说明：  当网络中有任意一个UDM不支持Trace Data时，需要通过**LST NGMMFUNC**命令检查是否关闭了AMF向UDM查询或者订阅TraceData的开关，避免造成业务流程异常。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '设置SMF软件参数比特位。配置SMF是否向UDM单独获取和订阅Trace Data：  * DWORD1001 BIT31 控制无I-SMF场景下SMF是否向UDM单独获取和订阅Trace Data * DWORD1001 BIT32 控制I-SMF/V-SMF存在场景下SMF是否向UDM单独获取和订阅Trace Data'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwsoftparabits_list_2:
      type: items
      properties:
        DWORDNUM:
          name: 'DWORD参数索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARATYPE:
          name: '数据类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2ESTAM01'
      SWITCH: ENABLE
    set_fwsoftparabits_list:
    - DWORDNUM: 1601
      VALUE: BIT7：VALUE_1（1）
      POSITION: BIT7：7
      PARATYPE: ''
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2ESTAM01'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - E2ESW: YES（是）
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1001
      VALUE: VALUE_0
      POSITION: 31
    set_fwsoftparabits_list_1:
    - DWORDNUM: 1601
      VALUE: BIT7：VALUE_1（1）
      POSITION: BIT7：7
      PARATYPE: ''
    set_licenseswitch_list_6:
    - LICITEM: 'LKV2ESTAM01'
      SWITCH: ENABLE
    set_ngmmfunc_list_1:
    - E2ESW: YES（是）
    set_smfsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: 1001
      VALUE: VALUE_0
      POSITION: 31
    set_fwsoftparabits_list_2:
    - DWORDNUM: 1601
      VALUE: BIT7：VALUE_1（1）
      POSITION: BIT7：7
      PARATYPE: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 场景一：EMS直接下发

### 管理面下发跟踪任务，入口界面：监控 > 全网端到端信令跟踪 > 跟踪管理，添加>管理面创建（具体请参考图1）

### **图1** 登录界面

#### 1.1 打开本功能的License配置开关。

#### 在“MML命令行-UEG”窗口上执行：

##### 1.1.1 //打开端到端用户跟踪的License配置开关。

```jinja2
{%- if is_scenario_ems_direct -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 （可选）配置跟踪消息上报速率控制（建议使用默认值。如果修改，请联系华为技术支持）。

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_reporting_rate_control and is_scenario_ems_direct -%}
    {%- for item in set_fwsoftparabits_list -%}
        SET FWSOFTPARABITS:
        {#- --- 必选参数 --- -#}
        POSITION={{item.POSITION}},
        VALUE={{item.VALUE}},
        PARATYPE={{item.PARATYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PARATYPE=DWORD/DWORD_EX 时必选 --- -#}
        {%- if item.PARATYPE in ['DWORD', 'DWORD_EX'] -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 场景二：信令传播下发

### 风筝L L2组网模式下不支持该场景。

### 信令面下发跟踪任务，入口界面：监控 > 全网端到端信令跟踪 > 跟踪管理，添加>信令面创建（具体请参考图2）

### **图2** 登录界面

#### 2.1 UDM作为初始网元

##### 2.1.1 打开本功能的License配置开关。

##### 在“MML命令行-UEG”窗口上执行：

###### 2.1.1.1 //打开端到端用户跟踪的License配置开关。

```jinja2
{%- if is_scenario_signal_propagation and is_scenario_udm_initial -%}
    {%- for item in set_licenseswitch_list_3 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.2 配置AMF是否向UDM查询或者订阅TraceData。

##### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_scenario_signal_propagation and is_scenario_udm_initial -%}
    {%- for item in set_ngmmfunc_list -%}
        SET NGMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.E2ESW is not none -%}
            E2ESW={{item.E2ESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 当网络中有任意一个UDM不支持Trace Data时，需要通过**LST NGMMFUNC**命令检查**全网跟踪开关**是否为“否”，若开关开启，需要通过**SET NGMMFUNC**命令设置**E2ESW**参数为“否”，以关闭AMF向UDM查询或者订阅TraceData的开关，避免造成业务流程异常。

##### 2.1.3 配置SMF是否向UDM单独获取和订阅Trace Data。

##### 在“MML命令行-UEG”窗口上执行：

###### 2.1.3.1 //在无I-SMF（SMF直连AMF）场景下，关闭SMF向UDM单独获取和订阅Trace Data。

```jinja2
{%- if is_scenario_signal_propagation and is_scenario_udm_initial -%}
    {%- for item in set_smfsoftparaofbit_list -%}
        SET SMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            POSITION={{item.POSITION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.4 （可选）配置跟踪消息上报速率控制（建议使用默认值。如果修改，请联系华为技术支持）。

##### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_reporting_rate_control and is_scenario_signal_propagation and is_scenario_udm_initial -%}
    {%- for item in set_fwsoftparabits_list_1 -%}
        SET FWSOFTPARABITS:
        {#- --- 必选参数 --- -#}
        POSITION={{item.POSITION}},
        VALUE={{item.VALUE}},
        PARATYPE={{item.PARATYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PARATYPE=DWORD/DWORD_EX 时必选 --- -#}
        {%- if item.PARATYPE in ['DWORD', 'DWORD_EX'] -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 AMF作为初始网元

##### 2.2.1 打开本功能的License配置开关。

##### 在“MML命令行-UEG”窗口上执行：

###### 2.2.1.1 //打开端到端用户跟踪的License配置开关。

```jinja2
{%- if is_scenario_signal_propagation and is_scenario_amf_initial -%}
    {%- for item in set_licenseswitch_list_6 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 （可选）关闭AMF向UDM查询或者订阅TraceData的开关。

##### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_close_amf_udm_trace_switch and is_scenario_signal_propagation and is_scenario_amf_initial -%}
    {%- for item in set_ngmmfunc_list_1 -%}
        SET NGMMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.E2ESW is not none -%}
            E2ESW={{item.E2ESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 当网络中有任意一个UDM不支持Trace Data时，需要通过**LST NGMMFUNC**命令检查**全网跟踪开关**是否为“否”，若开关开启，需要通过**SET NGMMFUNC**命令设置**E2ESW**参数为“否”，以关闭AMF向UDM查询或者订阅TraceData的开关，避免造成业务流程异常。

##### 2.2.3 关闭SMF向UDM单独获取和订阅Trace Data，可通过软参控制（软参值设置为0）。

##### 在“MML命令行-UEG”窗口上执行：

###### 2.2.3.1 //在无I-SMF（SMF直连AMF）场景下，关闭SMF向UDM单独获取和订阅Trace Data。

```jinja2
{%- if is_scenario_signal_propagation and is_scenario_amf_initial -%}
    {%- for item in set_smfsoftparaofbit_list_1 -%}
        SET SMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            POSITION={{item.POSITION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.4 （可选）配置跟踪消息上报速率控制（建议使用默认值。如果修改，请联系华为技术支持）。

##### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_reporting_rate_control and is_scenario_signal_propagation and is_scenario_amf_initial -%}
    {%- for item in set_fwsoftparabits_list_2 -%}
        SET FWSOFTPARABITS:
        {#- --- 必选参数 --- -#}
        POSITION={{item.POSITION}},
        VALUE={{item.VALUE}},
        PARATYPE={{item.PARATYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PARATYPE=DWORD/DWORD_EX 时必选 --- -#}
        {%- if item.PARATYPE in ['DWORD', 'DWORD_EX'] -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

