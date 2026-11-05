---
id: GWFD-010102
name: 配置GTP/PFCP路径管理参数
ne_type: UDG
type: feature
description: 当运营商在部署分组交换网，新增UDG时，需配置GTP/PFCP路径管理参数。通过GTP/PFCP路径管理，UDG可以进行到对端网元的路径管理，并控制路径中断后对已激活上下文的处理方式。  * 非N4/Sxb接口的GTP路径管理应用以下对接网元之间。   + eNodeB与SGW-U之间。   + SGW-U与PGW-U之间。   + eNodeB/GnGp-SGSN和PGW-U之间。   + UPF和UPF之间。   + R(AN)和UPF之间。 * N4/Sxb接口的GTP路径管理应用以下对接网元之间。   + PGW-C和PGW-U之间。   + SMF和UPF之间。 * PFCP路径管理应用以下对接网元之间。   + SGW-C和SGW-U之间。   + PGW-C和PGW-U之间。   + SMF和UPF之间。 * 路径管理在UDG和对端网元间是双向的，如果一方开启了本功能，为节省网络带宽资源，可以关闭另外一端的Echo消息开关。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010102 路径管理","配置GTP/PFCP路径管理参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增UDG时，需配置GTP/PFCP路径管理参数。通过GTP/PFCP路径管理，UDG可以进行到对端网元的路径管理，并控制路径中断后对已激活上下文的处理方式。* 非N4/Sxb接口的GTP路径管理应用以下对接网元之间。  + eNodeB与SGW-U之间。  + SGW-U与PGW-U之间。  + eNodeB/GnGp-SGSN和PGW-U之间。  + UPF和UPF之间。  + R(AN)和UPF之间。* N4/Sxb接口的GTP路径管理应用以下对接网元之间。  + PGW-C和PGW-U之间。  + SMF和UPF之间。* PFCP路径管理应用以下对接网元之间。  + SGW-C和SGW-U之间。  + PGW-C和PGW-U之间。  + SMF和UPF之间。* 路径管理在UDG和对端网元间是双向的，如果一方开启了本功能，为节省网络带宽资源，可以关闭另外一端的Echo消息开关。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-010102 路径管理。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_upgtppath_list:
      type: items
      properties:
        V1DATAECHOSW:
          name: 'V1数据路径Echo开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '参数用于设置GTP路径维护模式。需要进行GTP路径管理时，请使能GTP隧道两端网元的Echo消息开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ECHOINTERVAL:
          name: '发送GTP心跳请求的间隔时间'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: '发送Echo请求消息的间隔时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        T3RESPONSE:
          name: 'GTP请求消息的重发时间间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: 'Echo请求消息未收到响应的重发时间间隔。如果对端在本时间间隔内收到响应消息，则启动“ECHOINTERVAL”定时器。定时器超时后发送Echo请求。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N3REQUEST:
          name: 'GTP请求消息的最大尝试发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: 'Echo请求消息未收到响应的重发次数。如果重发Echo消息达到最大尝试发送次数“N3REQUEST”后仍未收到响应，则UDG上报ALM-81018 数据路径断告警，并认为eNodeB/(R)AN/UPF/SGW-U等设备已不可用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '是否去活路径上已激活的上下文'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '上报ALM-81018 数据路径断告警启动“ECHOINTERVAL”定时器。定时器超时后发送Echo请求，当发送Echo消息次数达“ECHOTIME”后仍未收到响应且“DEACTIVEFLAG”参数为“ENABLE”，则去激活此路径上控制面和用户面的所有上下文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ECHOTIME:
          name: '路径断告警后发送echo消息的次数'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICINFTYPE:
          name: '逻辑接口类型'
          type: string
          required: false
          description: '仅针对N9c接口间的路径启动路径探测功能。  执行**LST LOGICINF**确认已配置独立的n9cif接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upn4upath_list:
      type: items
      properties:
        N4ECHOSW:
          name: 'N4接口数据路径Echo开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '参数用于设置N4接口的GTP路径维护模式。需要进行GTP路径管理时，请使能GTP隧道两端网元的Echo消息开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4ECHOINTERVAL:
          name: 'N4接口发送GTP心跳请求的间隔时间'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: '发送Echo请求消息的间隔时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4T3RESPONSE:
          name: 'N4接口的GTP请求消息的重发时间间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: 'Echo请求消息未收到响应的重发时间间隔。如果对端在本时间间隔内收到响应消息，则启动“N4ECHOINTERVAL”定时器。定时器超时后发送Echo请求。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4N3REQUEST:
          name: 'N4接口的GTP请求消息的最大尝试发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: 'Echo请求消息未收到响应的重发次数。如果重发Echo消息达到最大尝试发送次数“N4N3REQUEST”后仍未收到响应，则UDG上报ALM-81018 数据路径断告警，并认为UPF/PGW-U等设备已不可用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '是否去活N4 GTP-U路径上已激活的上下文'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '上报ALM-81018 数据路径断告警启动“N4ECHOINTERVAL”定时器。定时器超时后发送Echo请求，当发送Echo消息次数达“N4ECHOTIME”后仍未收到响应且“DEACTIVEFLAG”参数为“ENABLE”，则去激活此路径上控制面和用户面的所有上下文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4ECHOTIME:
          name: 'N4接口的GTP-U路径断告警后发送echo消息的次数'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_uppfcppath_list:
      type: items
      properties:
        HEARTBEATINTERVAL:
          name: '发送PFCP心跳请求的间隔时间'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: '发送PFCP心跳请求消息的间隔时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        T3RESPONSE:
          name: 'PFCP请求消息的重发时间间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: 'PFCP心跳请求消息未收到响应的重发时间间隔。如果对端在本时间间隔内收到响应消息，则启动“HEARTBEATINTERVAL”定时器。定时器超时后发送PFCP请求。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N3REQUEST:
          name: 'PFCP请求消息的最大尝试发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: 'PFCP心跳请求消息未收到响应的重发次数。如果重发PFCP心跳消息达到最大尝试发送次数“N3REQUEST”后仍未收到响应，则UDG上报ALM-81017 PFCP路径断告警，并认为UPF/SGW-U/PGW-U/SMF/SGW-C/PGW-C等设备已不可用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '是否去活路径上已激活的上下文'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '上报ALM-81017 PFCP路径断告警启动“HEARTBEATINTERVAL”定时器。定时器超时后发送PFCP心跳请求，当发送PFCP心跳消息次数达“HEARTBEATTIME”后仍未收到响应且“DEACTIVEFLAG”参数为“ENABLE”，则去激活此路径上控制面和用户面的所有上下文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEARTBEATTIME:
          name: '路径断告警后发送心跳消息的次数'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERTYPE:
          name: '用户类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_upgtppath_list:
    - V1DATAECHOSW: ENABLE
      ECHOINTERVAL: 60
      T3RESPONSE: 10
      N3REQUEST: 5
      DEACTIVEFLAG: ENABLE
      ECHOTIME: 20
      LOGICINFTYPE: N9c
    set_upn4upath_list:
    - N4ECHOSW: ENABLE
      N4ECHOINTERVAL: 60
      N4T3RESPONSE: 3
      N4N3REQUEST: 5
      DEACTIVEFLAG: ENABLE
      N4ECHOTIME: 0
    set_uppfcppath_list:
    - HEARTBEATINTERVAL: 60
      T3RESPONSE: 3
      N3REQUEST: 5
      DEACTIVEFLAG: ENABLE
      HEARTBEATTIME: 30
      USERTYPE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置非N4接口的GTP路径管理参数。

### 设置UDG上的Echo开关属性及请求间隔，设置Echo消息的重发时间间隔和最大尝试发送次数，配置GTP路径断开后UDG对该路径上已激活PDP上下文/EPS承载/PDU Session的处理。

```jinja2
{%- for item in set_upgtppath_list -%}
    SET UPGTPPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.V1DATAECHOSW is not none -%}
        V1DATAECHOSW={{item.V1DATAECHOSW}},
    {%- endif -%}
    {%- if item.ECHOINTERVAL is not none -%}
        ECHOINTERVAL={{item.ECHOINTERVAL}},
    {%- endif -%}
    {%- if item.T3RESPONSE is not none -%}
        T3RESPONSE={{item.T3RESPONSE}},
    {%- endif -%}
    {%- if item.N3REQUEST is not none -%}
        N3REQUEST={{item.N3REQUEST}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEACTIVEFLAG=ENABLE 时必选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        ECHOTIME={{item.ECHOTIME}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：V1DATAECHOSW=ENABLE 时可选 --- -#}
    {%- if item.V1DATAECHOSW == 'ENABLE' -%}
        {%- if item.LOGICINFTYPE is not none -%}
            LOGICINFTYPE={{item.LOGICINFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 只有在UDG启动路径管理功能时，才需执行本配置。

### 通过配置**SET UPGTPPATH**的“LOGICINFTYPE”参数，可以针对指定类型接口间的路径启动路径探测功能，包括N3、S1-U、S11-U、N9c、S5-S\S8-S、Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U)接口。如果N3和S1-U接口合一为Saif抽象接口时，则仅能针对Saif抽象接口启动路径探测功能；如果N9c和S5-S/S8-S接口合一为Scif抽象接口时，则仅能针对Scif接口启动路径探测功能。如果N3、S1-U、S11-U、N9c、S5-S\S8-S需要启动独立接口间的路径探测功能，则必须按照独立接口配置。

### 不配置**SET UPGTPPATH**的“LOGICINFTYPE”参数时，则针对所有非N4/Sxb接口间的路径启动路径探测功能。

### 2 配置N4接口的GTP路径管理参数。

### 设置UDG上的Echo开关属性及请求间隔，设置Echo消息的重发时间间隔和最大尝试发送次数，配置GTP路径断开后UDG对该路径上已激活PDU Session的处理。

```jinja2
{%- for item in set_upn4upath_list -%}
    SET UPN4UPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.N4ECHOSW is not none -%}
        N4ECHOSW={{item.N4ECHOSW}},
    {%- endif -%}
    {%- if item.N4ECHOINTERVAL is not none -%}
        N4ECHOINTERVAL={{item.N4ECHOINTERVAL}},
    {%- endif -%}
    {%- if item.N4T3RESPONSE is not none -%}
        N4T3RESPONSE={{item.N4T3RESPONSE}},
    {%- endif -%}
    {%- if item.N4N3REQUEST is not none -%}
        N4N3REQUEST={{item.N4N3REQUEST}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEACTIVEFLAG=ENABLE 时必选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        N4ECHOTIME={{item.N4ECHOTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 只有在UDG启动路径管理功能时，才需执行本配置。

### 3 配置PFCP路径管理参数。

### 设置UDG上的PFCP开关属性及请求间隔，设置PFCP Heartbeat消息的重发时间间隔和最大尝试发送次数，配置PFCP路径断开后UDG对该路径上已激活PDP上下文/EPS承载/PDU Session的处理。

```jinja2
{%- for item in set_uppfcppath_list -%}
    SET UPPFCPPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.HEARTBEATINTERVAL is not none -%}
        HEARTBEATINTERVAL={{item.HEARTBEATINTERVAL}},
    {%- endif -%}
    {%- if item.T3RESPONSE is not none -%}
        T3RESPONSE={{item.T3RESPONSE}},
    {%- endif -%}
    {%- if item.N3REQUEST is not none -%}
        N3REQUEST={{item.N3REQUEST}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEACTIVEFLAG=ENABLE 时必选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        HEARTBEATTIME={{item.HEARTBEATTIME}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEACTIVEFLAG=ENABLE 时可选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        {%- if item.USERTYPE is not none -%}
            USERTYPE={{item.USERTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

