---
id: ''
name: 配置SMF
ne_type: UNC
type: feature
description: 本操作用于指导在专网SMF上开启通用DNN漫游分流特性。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置通用DNN漫游分流","配置SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在专网SMF上开启通用DNN漫游分流特性。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        N16AUEIPSW:
          name: '通用DNN会话UE IP地址处理开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '-'
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
          description: '软参DWORD1039 BIT21用于控制5G用户接入时是否将左侧携带的selectedDNN作为用户请求DNN使用。取值为1时，将selectedDNN作为用户请求DNN使用。'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UEIPNATFUNC:
          name: '是否支持UE IP地址NAT转换功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '专网SMF会基于此参数的配置判定专网UPF是否支持NAT转换功能（对UE IP地址1：1替换），并基于该能力选择专网UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_smffunc_list:
    - N16AUEIPSW: Support
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1039
      VALUE: VALUE_1
      POSITION: 21
      BYTENUM: ''
      BYTEPOSITION: ''
    mod_upnode_list:
    - NFINSTANCENAME: '5EA7F228-47CC-2032-03A3-0E1313000001'
      UEIPNATFUNC: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开“公网会话UE IP地址处理开关。当N16a口携带了公网会话的UE IP地址（扩展私有字段），专网SMF会将公网会话的UE IP地址下发给专网会话的锚点UPF，指示专网UPF做UE IP地址NAT转换。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.N16AUEIPSW is not none -%}
        N16AUEIPSW={{item.N16AUEIPSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置左侧AMF或I-SMF携带的selectedDNN作为用户请求DNN使用。

```jinja2
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
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置UPF支持UE IP地址NAT转换功能。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UEIPNATFUNC is not none -%}
        UEIPNATFUNC={{item.UEIPNATFUNC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

