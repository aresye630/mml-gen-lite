---
id: ''
name: 激活个人应用防护
ne_type: UDG
type: feature
description: 为保护用户上网安全，免受网络恶意报文攻击，需要激活NAT个人应用防护功能。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT基本功能","激活个人应用防护"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为保护用户上网安全，免受网络恶意报文攻击，需要激活NAT个人应用防护功能。

## 必备事项
前提条件

* 已通过**ADD APN**完成APN的相关配置。
* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '打开NAT个人应用防护功能License开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    nap-view_list:
      type: items
      properties: {}
    nap-filter_list:
      type: items
      properties:
        NAP-FILTER-NAME:
          name: 'nap-filter-name'
          type: string
          required: false
          description: '设置过滤器的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34-PROTOCOL-VALUE:
          name: 'l34-protocol-value'
          type: string
          required: false
          description: '设置三四层协议类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    nap-filter-group_list:
      type: items
      properties:
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '设置过滤器组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-NAME:
          name: 'nap-filter-name'
          type: string
          required: false
          description: '设置过滤器名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    nap-refresh-service_list:
      type: items
      properties: {}
    packet-policy_list:
      type: items
      properties:
        PACKET-POLICY-NAME:
          name: 'packet-policy-name'
          type: string
          required: false
          description: '配置packet-policy的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置策略的过滤规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINK:
          name: 'uplink'
          type: string
          required: false
          description: '在上行方向配置包过滤。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTION:
          name: 'action'
          type: string
          required: false
          description: '配置包过滤默认动作：允许报文通过。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'priority'
          type: string
          required: false
          description: '配置策略优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    detect-policy_list:
      type: items
      properties:
        DETECT-POLICY-NAME:
          name: 'detect-policy-name'
          type: string
          required: false
          description: '配置detect-policy的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置策略的过滤规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINK:
          name: 'uplink'
          type: string
          required: false
          description: '配置上行方向有效。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'priority'
          type: string
          required: false
          description: '配置策略优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    aspf-policy_list:
      type: items
      properties:
        ASPF-POLICY-NAME:
          name: 'aspf-policy-name'
          type: string
          required: false
          description: '配置aspf-policy的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置策略的过滤规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINK:
          name: 'uplink'
          type: string
          required: false
          description: '对上行发起业务配置aspf包过滤策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTION:
          name: 'action'
          type: string
          required: false
          description: '配置包过滤默认动作：允许报文通过。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'priority'
          type: string
          required: false
          description: '配置策略优先级'
          data_source: '本端规划'
          pattern: ''
          default: ''
    long-link-policy_list:
      type: items
      properties:
        LONG-LINK-POLICY-NAME:
          name: 'long-link-policy-name'
          type: string
          required: false
          description: '配置long-link-policy的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置策略的过滤规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPLINK:
          name: 'uplink'
          type: string
          required: false
          description: '在上行方向配置包过滤。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'priority'
          type: string
          required: false
          description: '配置优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    nap-flow-node-agetime_list:
      type: items
      properties:
        TYPE-NAME:
          name: 'type-name'
          type: string
          required: false
          description: '配置流或报文类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIME-VALUE:
          name: 'time-value'
          type: string
          required: false
          description: '配置长连接流量的五元组老化时间。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    detect-protocol_list:
      type: items
      properties:
        FTP:
          name: 'ftp'
          type: string
          required: false
          description: '表示NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        H323:
          name: 'h323'
          type: string
          required: false
          description: '表示NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PPTP:
          name: 'pptp'
          type: string
          required: false
          description: '表示NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    packet-policy-default_list:
      type: items
      properties:
        UPLINK:
          name: 'uplink'
          type: string
          required: false
          description: '在上行方向配置包过滤。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACTION:
          name: 'action'
          type: string
          required: false
          description: '配置包过滤默认动作：允许报文通过。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    nap-flow-node-max_list:
      type: items
      properties:
        MAX-NUM:
          name: 'max-num'
          type: string
          required: false
          description: '配置单个用户五元组流节点的最大个数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV4EN4SCY01'
      SWITCH: ENABLE
    nap-view_list:
    - {}
    nap-filter_list:
    - NAP-FILTER-NAME: fhfilter
      L34-PROTOCOL-VALUE: udp
    nap-filter-group_list:
    - NAP-FILTER-GROUP-NAME: fhgfilter
      NAP-FILTER-NAME: fhfilter
    nap-refresh-service_list:
    - {}
    packet-policy_list:
    - PACKET-POLICY-NAME: name
      NAP-FILTER-GROUP-NAME: fhgfilter
      UPLINK: uplink
      ACTION: permit
      PRIORITY: '10'
    detect-policy_list:
    - DETECT-POLICY-NAME: dectname
      NAP-FILTER-GROUP-NAME: fhgfilter
      UPLINK: uplink
      PRIORITY: '10'
    aspf-policy_list:
    - ASPF-POLICY-NAME: test1-aspf
      NAP-FILTER-GROUP-NAME: fhgfilter
      UPLINK: uplink
      ACTION: permit
      PRIORITY: '10'
    long-link-policy_list:
    - LONG-LINK-POLICY-NAME: longlink
      NAP-FILTER-GROUP-NAME: fhgfilter
      UPLINK: uplink
      PRIORITY: '10'
    nap-flow-node-agetime_list:
    - TYPE-NAME: tcp
      TIME-VALUE: '600'
    detect-protocol_list:
    - FTP: ftp
      H323: h323
      PPTP: pptp
    packet-policy-default_list:
    - UPLINK: uplink
      ACTION: permit
    nap-flow-node-max_list:
    - MAX-NUM: '100'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License（内置安全增强）配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 3 配置个人应用防护过滤条件。

#### 3.1 进入nap视图。

#### **nap****-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=3.1 -->
```

#### 3.2 配置三四层NAT过滤条件。

#### **nap-filter** *xxx* **l34-protocol** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter_list的变量区（command: nap-filter） -#}
<!-- MISSING_MACRO: command=nap-filter list_name=nap-filter_list step_id=3.2 -->
```

#### 3.3 配置NAT过滤条件组，可绑定已配置的NAT filter。当配置了多个NAT filter时，满足其中一个过滤条件即可。

#### **nap-filter-group** *xxx* **nap-filter** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter-group_list的变量区（command: nap-filter-group） -#}
<!-- MISSING_MACRO: command=nap-filter-group list_name=nap-filter-group_list step_id=3.3 -->
```

#### 3.4 生效NAT过滤条件。

#### **nap-refresh-service**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-refresh-service_list的变量区（command: nap-refresh-service） -#}
<!-- MISSING_MACRO: command=nap-refresh-service list_name=nap-refresh-service_list step_id=3.4 -->
```

### 4 配置个人应用防护策略。

#### 4.1 配置数据包过滤策略，引用步骤3配置的过滤条件、以及配置的策略生效时间，并指定对报文的动作。

#### **packet-policy**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该packet-policy_list的变量区（command: packet-policy） -#}
<!-- MISSING_MACRO: command=packet-policy list_name=packet-policy_list step_id=4.1 -->
```

#### 4.2 配置用户自定义的STUN策略，引用步骤3配置的过滤条件。

#### **detect-policy**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该detect-policy_list的变量区（command: detect-policy） -#}
<!-- MISSING_MACRO: command=detect-policy list_name=detect-policy_list step_id=4.2 -->
```

#### 4.3 配置三元组ASPF策略，引用步骤3配置的过滤条件、指定对报文的动作。

#### **aspf-policy**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该aspf-policy_list的变量区（command: aspf-policy） -#}
<!-- MISSING_MACRO: command=aspf-policy list_name=aspf-policy_list step_id=4.3 -->
```

#### 4.4 配置长连接策略，引用步骤3配置的长连接过滤条件。

#### **long-link-policy**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该long-link-policy_list的变量区（command: long-link-policy） -#}
<!-- MISSING_MACRO: command=long-link-policy list_name=long-link-policy_list step_id=4.4 -->
```

#### 4.5 配置长连接流量的五元组老化时间。

#### **nap-flow-node-agetime**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-flow-node-agetime_list的变量区（command: nap-flow-node-agetime） -#}
<!-- MISSING_MACRO: command=nap-flow-node-agetime list_name=nap-flow-node-agetime_list step_id=4.5 -->
```

#### 4.6 配置L7 ASPF支持的应用层协议类型。

#### **detect-protocol**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该detect-protocol_list的变量区（command: detect-protocol） -#}
<!-- MISSING_MACRO: command=detect-protocol list_name=detect-protocol_list step_id=4.6 -->
```

#### 4.7 配置数据包的默认过滤动作。

#### **packet-policy-default**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该packet-policy-default_list的变量区（command: packet-policy-default） -#}
<!-- MISSING_MACRO: command=packet-policy-default list_name=packet-policy-default_list step_id=4.7 -->
```

#### 对于nap-template下的新建流的报文根据**packet-policy**的配置，确定报文是否可以通过。

#### 对于匹配上**packet-policy**配置的过滤规则的报文，按照配置的动作进行处理。

#### 对于未匹配上**packet-policy**配置的过滤规则的报文，则按照**packet-policy-default**配置的动作进行处理。

#### 若未配置**packet-policy-default**，则按系统的默认动作进行处理：上行报文允许通过，下行报文拒绝通过。

#### 4.8 配置五元组流节点最大个数。

#### **nap-flow-node-max**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-flow-node-max_list的变量区（command: nap-flow-node-max） -#}
<!-- MISSING_MACRO: command=nap-flow-node-max list_name=nap-flow-node-max_list step_id=4.8 -->
```

#### 该命令用于对单个用户的流数进行控制，防止单个用户建立过多的流数占用系统资源。数据报文达到时，NAT在新建流时首先判断该用户下的流数是否达到配置上限。

#### 如果达到上限，则丢弃报文。

#### 如果未达到上限，则创建流表，允许报文进行后续处理。

#### 针对手机后路由用户，如果开启了用户的流数控制，则该用户及手机后所有IP的总流数之和受**nap-flow-node-max**命令限制。

