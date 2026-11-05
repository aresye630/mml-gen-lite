---
id: ''
name: 配置N19接口
ne_type: UNC
type: feature
description: 两个负荷分担关系的UPF对接同一对VxLAN交换机/DCGW或对接不同对VxLAN交换机/DCGW时，本特性支持通过UPF间的N19接口为不同UPF下层二终端组的成员之间提供以太类型的通信服务。  * 两个UPF是负荷分担关系，且连接到同一对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF间的VxLAN隧道实现或通过UPF间的N19接口实现。 * 两个UPF是负荷分担关系，且连接到不同对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF与DCGW之间的VxLAN隧道实现或通过UPF间的N19接口实现。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","5G LAN解决方案","WSFD-225003 5G LAN业务基本功能","配置N19接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
两个负荷分担关系的UPF对接同一对VxLAN交换机/DCGW或对接不同对VxLAN交换机/DCGW时，本特性支持通过UPF间的N19接口为不同UPF下层二终端组的成员之间提供以太类型的通信服务。* 两个UPF是负荷分担关系，且连接到同一对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF间的VxLAN隧道实现或通过UPF间的N19接口实现。* 两个UPF是负荷分担关系，且连接到不同对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF与DCGW之间的VxLAN隧道实现或通过UPF间的N19接口实现。

## 必备事项
前提条件

已完成配置5G LAN业务基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nglanfunc_list:
      type: items
      properties:
        UECHKSW:
          name: '是否发起SMF内5G Lan组内会话数量核查'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPCHKSW:
          name: '是否发起向UPF的组会话核查'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_grpnglanfunc_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N19SUPPORT:
          name: '是否支持N19通信'
          type: string
          enum:
          - INHERIT
          - SUPPORT
          - NOTSUPPORT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MULTICAST:
          name: '是否创建组播PDR规则'
          type: string
          enum:
          - INHERIT
          - SUPPORT
          - NOTSUPPORT
          required: false
          description: '说明：  当企业需要开启组播功能时，将此参数配置为Support。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N6BROADCASTSW:
          name: '是否支持N6侧上行广播'
          type: string
          enum:
          - INHERIT
          - SUPPORT
          - NOTSUPPORT
          required: false
          description: '说明：  当企业需要开启N6侧上行广播功能时，将此参数配置为Support。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PKTELIMINATESSW:
          name: '是否支持报文增殖消除'
          type: string
          enum:
          - INHERIT
          - SUPPORT
          - NOTSUPPORT
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MACPROCMODE:
          name: 'MAC地址处理模式'
          type: string
          enum:
          - SINGLE
          - FULL
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MACASSEMMODE:
          name: 'MAC地址组装模式'
          type: string
          enum:
          - SINGLE
          - FULL
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
          description: ''
          data_source: ''
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
  examples:
    set_nglanfunc_list:
    - UECHKSW: Support
      GROUPCHKSW: Support
    add_grpnglanfunc_list:
    - GROUPID: 'A0000001-460-003-A000000001'
      N19SUPPORT: SUPPORT
      MULTICAST: SUPPORT
      N6BROADCASTSW: SUPPORT
      PKTELIMINATESSW: SUPPORT
      MACPROCMODE: FULL
      MACASSEMMODE: FULL
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1020
      VALUE: VALUE_1
      POSITION: 22
      BYTENUM: ''
      BYTEPOSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //开启5G LAN核查功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.UECHKSW is not none -%}
        UECHKSW={{item.UECHKSW}},
    {%- endif -%}
    {%- if item.GROUPCHKSW is not none -%}
        GROUPCHKSW={{item.GROUPCHKSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置UPF间基于N19通信，开启组播、N6侧上行广播和报文增殖消除功能，并设置MAC地址的上报处理和下发处理方式。

```jinja2
{%- for item in add_grpnglanfunc_list -%}
    ADD GRPNGLANFUNC:
    {#- --- 必选参数 --- -#}
    GROUPID="{{item.GROUPID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.N19SUPPORT is not none -%}
        N19SUPPORT={{item.N19SUPPORT}},
    {%- endif -%}
    {%- if item.MULTICAST is not none -%}
        MULTICAST={{item.MULTICAST}},
    {%- endif -%}
    {%- if item.N6BROADCASTSW is not none -%}
        N6BROADCASTSW={{item.N6BROADCASTSW}},
    {%- endif -%}
    {%- if item.PKTELIMINATESSW is not none -%}
        PKTELIMINATESSW={{item.PKTELIMINATESSW}},
    {%- endif -%}
    {%- if item.MACPROCMODE is not none -%}
        MACPROCMODE={{item.MACPROCMODE}},
    {%- endif -%}
    {%- if item.MACASSEMMODE is not none -%}
        MACASSEMMODE={{item.MACASSEMMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //创建广播PDR规则。

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

