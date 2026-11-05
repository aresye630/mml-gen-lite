---
id: ''
name: 配置OCS Failover功能
ne_type: UNC
type: feature
description: 当用户激活后进行业务时，GGSN/PGW-C发送在线计费请求消息给OCS，同时启动Tx定时器，在指定的时间内未收到OCS的响应，即可判断OCS服务器状态异常，则执行CCFH进行failover处理。CCFH的动作设置请参见**ADD DCCTEMPLATE**命令，只有当动作设置为RETRY\_AND\_TERM或者CONTINUE时，才会执行failover动作。GGSN/PGW-C向备OCS组重发消息，如果备OCS组也没有响应或者备OCS因状态异常、消息发送速率超过wal值等导致不可用，可以根据情况配置阻塞用户业务或者转离线计费继续进行业务。  实现OCS服务器failover需要具备以下几个条件：  * 采用负荷分担或者主备OCS组网方式。 * GGSN/PGW-C本地配置支持failover功能。 * 主备OCS存在LOCALHOSTNAME相同的Diameter链路组。 * OCS支持failover，即在CCA消息中CC-Session-Failover AVP支持failover。 * OCS支持热备份功能，即OCS支持CC session的同步。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置OCS组网可靠性配置实例","配置OCS Failover功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户激活后进行业务时，GGSN/PGW-C发送在线计费请求消息给OCS，同时启动Tx定时器，在指定的时间内未收到OCS的响应，即可判断OCS服务器状态异常，则执行CCFH进行failover处理。CCFH的动作设置请参见**ADD DCCTEMPLATE**命令，只有当动作设置为RETRY\_AND\_TERM或者CONTINUE时，才会执行failover动作。GGSN/PGW-C向备OCS组重发消息，如果备OCS组也没有响应或者备OCS因状态异常、消息发送速率超过wal值等导致不可用，可以根据情况配置阻塞用户业务或者转离线计费继续进行业务。实现OCS服务器failover需要具备以下几个条件：* 采用负荷分担或者主备OCS组网方式。* GGSN/PGW-C本地配置支持failover功能。* 主备OCS存在LOCALHOSTNAME相同的Diameter链路组。* OCS支持failover，即在CCA消息中CC-Session-Failover AVP支持failover。* OCS支持热备份功能，即OCS支持CC session的同步。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
* 部署主备OCS组，且主OCS组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS的设备信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: '增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3868
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '支持failover和failback。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_dcctemplate_list_1:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '支持failover和failback。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_dcctemplate_list_2:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '支持failover和failback。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_dcctemplate_list_3:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '支持failover和failback。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_dcctemplate_list_4:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置主从OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FAILOVERSUP:
          name: '支持failover使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '支持failover和failback。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        CCFH:
          name: 'CCFH处理动作'
          type: string
          enum:
          - BLOCK
          - CONTINUE
          - INHERIT
          - RETRY_AND_TERM
          - TERMINATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        AUTOFAILBACK:
          name: 'failback使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    set_txtimer_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'Tx定时器。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TXTIMERFLAG:
          name: 'Tx定时器配置模式'
          type: string
          enum:
          - APP_RETRANSMIT
          - INHERIT
          - TXTIMER_VALUE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TXTIMER:
          name: 'Tx定时器时长（秒）'
          type: integer
          minimum:
          - 1
          - 4294967295
          maximum:
          - 20
          - 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRYTIMEOUT:
          name: '应用重传时间间隔（秒）'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RETRYTIMES:
          name: '应用重传次数'
          type: integer
          minimum: 0
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_holdingtime_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOLDINGTIME:
          name: '用户保持时长(分钟)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 2880
          - 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ocs_list:
    - OCSHOSTNAME: 'ocs_host1'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list:
    - HOSTNAME: 'ocs_host1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.11.21.59'
      PORT: 3868
      IPV6ADDRESS: ''
      SCTPENDPOINT: ''
    add_ocsgroup_list:
    - OCSGRPNAME: 'ocs-gra'
    add_ocsbinding_list:
    - OCSGRPNAME: 'ocs-gra'
      OCSHOSTNAME: 'ocs_host1'
    mod_dcctemplate_list:
    - DCCTMPLTNAME: ''
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
      FAILOVERSUP: ENABLE
      CCFH: RETRY_AND_TERM
      AUTOFAILBACK: ENABLE
    add_dcctemplate_list_1:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
      FAILOVERSUP: ENABLE
      CCFH: RETRY_AND_TERM
      AUTOFAILBACK: ENABLE
    add_dcctemplate_list_2:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
      FAILOVERSUP: ENABLE
      CCFH: RETRY_AND_TERM
      AUTOFAILBACK: ENABLE
    add_dcctemplate_list_3:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
      FAILOVERSUP: ENABLE
      CCFH: RETRY_AND_TERM
      AUTOFAILBACK: ENABLE
    add_dcctemplate_list_4:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs-gra'
      SECOCSGRPNAME: 'ocs-grb'
      FAILOVERSUP: ENABLE
      CCFH: RETRY_AND_TERM
      AUTOFAILBACK: ENABLE
    set_txtimer_list:
    - DCCTMPLTNAME: 'dcc-test'
      TXTIMERFLAG: TXTIMER_VALUE
      TXTIMER: 10
      RETRYTIMEOUT: ''
      RETRYTIMES: ''
    set_holdingtime_list:
    - DCCTMPLTNAME: ''
      HOLDINGTIME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置OCS信息。

#### 1.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- for item in add_ocs_list -%}
    ADD OCS:
    {#- --- 必选参数 --- -#}
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    ;
{%- endfor -%}
```

#### 1.2 配置Diameter链路对端的OCS地址信息。

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置OCS组。

```jinja2
{%- for item in add_ocsgroup_list -%}
    ADD OCSGROUP:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    ;
{%- endfor -%}
```

#### 1.4 配置OCS和OCS组的绑定关系。

```jinja2
{%- for item in add_ocsbinding_list -%}
    ADD OCSBINDING:
    {#- --- 必选参数 --- -#}
    OCSGRPNAME="{{item.OCSGRPNAME}}",
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    ;
{%- endfor -%}
```

### 2 配置DCC模板（配置主备OCS组、配置OCS服务器Failover功能）。

#### 2.1 配置DCC模板。

#### 全局模板：**MOD DCCTEMPLATE**

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

#### DCC模板：**ADD DCCTEMPLATE**

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置DCC模板的主从OCS组。

```jinja2
{%- for item in add_dcctemplate_list_1 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置DCC模板的Tx定时器超时后的处理方式。

```jinja2
{%- for item in add_dcctemplate_list_2 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“CCFH”用于其他方式下在线计费Tx定时器超时后的动作处理。

#### Tx定时器超时后有三种动作处理方式：

#### “TERMINATE”：表示去激活用户。

#### “RETRY\_AND\_TERM”：表示GGSN/PGW-C会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则去激活用户。

#### “CONTINUE”：表示GGSN/PGW-C会向备OCS重发一次请求消息，如果能收到响应，则与备OCS交互；如果Tx定时器超时仍然未得到响应，则转离线计费，继续进行业务。

#### 2.4 配置GGSN/PGW-C支持failover。

```jinja2
{%- for item in add_dcctemplate_list_3 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“FAILOVERSUP”和“AUTOFAILBACK”是协议定义的两种OCS故障容错方式：

#### “FAILOVERSUP”是指在主OCS故障的情况下，GGSN/PGW-C会发送DCC消息给备OCS服务器组进行处理。

#### “AUTOFAILBACK”是指当主OCS链路故障恢复后，DCC业务切换回到主OCS服务器上。

#### 2.5 配置在线计费和离线计费同时使能的用户进行在线计费时，发生CCFH之后是否在离线话单中添加CCFH标志位。

```jinja2
{%- for item in add_dcctemplate_list_4 -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.CCFH is not none -%}
        CCFH={{item.CCFH}},
    {%- endif -%}
    {%- if item.AUTOFAILBACK is not none -%}
        AUTOFAILBACK={{item.AUTOFAILBACK}},
    {%- endif -%}
    {%- if item.FAILOVERSUP is not none -%}
        FAILOVERSUP={{item.FAILOVERSUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 本命令只针对在线计费用户生效，且在配置离线/在线计费方式（GGSN/PGW-C）中根据用户归属属性配置的离线计费开关**SET CHARGECTRL**必须使能。

#### 2.6 配置Tx定时器的时长。

```jinja2
{%- for item in set_txtimer_list -%}
    SET TXTIMER:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    TXTIMERFLAG={{item.TXTIMERFLAG}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TXTIMERFLAG=TXTIMER_VALUE 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'TXTIMER_VALUE' -%}
        TXTIMER={{item.TXTIMER}},
    {%- endif -%}
    {#- --- 条件必选：TXTIMERFLAG=APP_RETRANSMIT 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'APP_RETRANSMIT' -%}
        RETRYTIMEOUT={{item.RETRYTIMEOUT}},
    {%- endif -%}
    {#- --- 条件必选：TXTIMERFLAG=APP_RETRANSMIT 时必选 --- -#}
    {%- if item.TXTIMERFLAG == 'APP_RETRANSMIT' -%}
        RETRYTIMES={{item.RETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 **可选：**配置业务持续时长。

#### 当Tx定时器超时后的处理方式为“CONTINUE”时，允许用户保持业务的时长，超出该时长则去激活用户。当配置为0分钟表示允许用户永久保持在线进行业务。

```jinja2
{%- if is_optional_business_holding_time -%}
    {%- for item in set_holdingtime_list -%}
        SET HOLDINGTIME:
        {#- --- 必选参数 --- -#}
        DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
        HOLDINGTIME={{item.HOLDINGTIME}},
        ;
    {%- endfor -%}
{%- endif -%}
```

