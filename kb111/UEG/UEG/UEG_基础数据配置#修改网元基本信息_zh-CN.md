---
id: ''
name: 修改网元基本信息
ne_type: UEG
type: feature
description: 软件安装阶段，已完成网元名称和浮动IP地址的配置以及OM物理端口设置。在开局阶段或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称、浮动IP地址、OM物理端口。  网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","UEG初始配置（风筝S）","参考：详细配置指导","基础数据配置","修改网元基本信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
软件安装阶段，已完成网元名称和浮动IP地址的配置以及OM物理端口设置。在开局阶段或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称、浮动IP地址、OM物理端口。网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。

## 必备事项
前提条件

* 已经确认现网规划的网元名称、浮动IP地址与网元生产预安装的预设参数值不同。
* 已登录网元OM Portal。

  硬件服务器可通过192.168.6.10登录：

  将调测PC连接到服务器的级联网口，并将调测PC的IP配置为192.168.6.10/24同网段的IP，登录网元OM Portal。例如将调测PC的IP配置为192.168.6.11/24，通过https://192.168.6.10:31943登录OM Portal。
* 已从网管侧获取网管登录信息。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_instpara_list:
      type: items
      properties:
        PARATYPE:
          name: '参数类型'
          type: string
          enum:
          - OMPORT
          required: true
          description: '调整OM物理端口时需要规划，否则不需要规划。'
          data_source: '固定取值'
          pattern: ''
          default: OMPORT
        SERVERNAME:
          name: '服务器名称'
          type: string
          maxLength: 64
          required: true
          description: '执行**LST INSTPARA**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORTTYPE:
          name: '网口类型'
          type: string
          enum:
          - '0'
          - '1'
          required: true
          description: '规划的OM物理端口采用bond口时需要规划。'
          data_source: '固定取值'
          pattern: ''
          default: '0'
        PORTNAME:
          name: '网口名称'
          type: string
          maxLength: 9
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUBPORT:
          name: '子网口'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BONDMODE:
          name: 'bond模式'
          type: string
          enum:
          - '4'
          - '1'
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: '4'
        LACPRATE:
          name: '网卡存活检测'
          type: string
          enum:
          - '1'
          - '0'
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: '1'
        HASHPOLICY:
          name: 'HASH策略'
          type: string
          enum:
          - '0'
          - '1'
          - '2'
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: '1'
    set_instpara_list_1:
      type: items
      properties:
        PARATYPE:
          name: '参数类型'
          type: string
          enum:
          - OMPORT
          required: true
          description: '调整OM物理端口时需要规划，否则不需要规划。'
          data_source: '固定取值'
          pattern: ''
          default: OMPORT
        SERVERNAME:
          name: '服务器名称'
          type: string
          maxLength: 64
          required: true
          description: '执行**LST INSTPARA**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORTTYPE:
          name: '网口类型'
          type: string
          enum:
          - '0'
          - '1'
          required: true
          description: '规划的OM物理端口采用单端口时需要规划。'
          data_source: '固定取值'
          pattern: ''
          default: '0'
        PORTNAME:
          name: '网口名称'
          type: string
          maxLength: 9
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_me_list:
      type: items
      properties:
        MEID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '-'
          data_source: '执行**LST ME**查询'
          pattern: ''
          default: ''
        MENAME:
          name: '网元名称'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_network_list:
      type: items
      properties:
        IPTYPE:
          name: 'IP类型'
          type: string
          required: false
          description: '-'
          data_source: '执行**LST NETWORK**查询'
          pattern: ''
          default: ''
        NWNAME:
          name: '网络名称'
          type: string
          required: false
          description: ''
          data_source: '执行**LST NETWORK**查询'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLANID'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONFIRM:
          name: 'CONFIRM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_omip_list:
      type: items
      properties:
        OMIPTYPE:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '通过**LST OMIP**查询的物理IP1与浮动IP相同，则定义为“OM IP模式”为“精简”模式。   * “OM IP模式”是“精简”模式时，可不配置物理IP1或将物理IP1地址设置为与浮动IP地址相同。 * “OM IP模式”不是“精简”模式时，需规划1个物理IP，且物理IP1须与浮动IP在同一网段。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        OMSETTYPE:
          name: 'IP设置类型'
          type: string
          enum:
          - SET_IP
          - DELETE_PHYSICAL_IP
          - DELETE_FLOAT_IP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: SET_IP
        OMFIPADDR:
          name: '浮动IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMNETMASK:
          name: '子网掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMIPV4GATEWAY:
          name: '默认网关'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_omip_list_1:
      type: items
      properties:
        OMIPTYPE:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '通过**LST OMIP**查询的物理IP1与浮动IP相同，则定义为“OM IP模式”为“精简”模式。   * “OM IP模式”是“精简”模式时，可不配置物理IP1或将物理IP1地址设置为与浮动IP地址相同。 * “OM IP模式”不是“精简”模式时，需规划1个物理IP，且物理IP1须与浮动IP在同一网段。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        OMSETTYPE:
          name: 'IP设置类型'
          type: string
          enum:
          - SET_IP
          - DELETE_PHYSICAL_IP
          - DELETE_FLOAT_IP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: SET_IP
        OMFIPADDR:
          name: '浮动IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMNETMASK:
          name: '子网掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMIPV4GATEWAY:
          name: '默认网关'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMHOST1IPV4:
          name: '物理IP1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_omnicswapswitch_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: 'UEG直连DCGW场景，支持备OM口进行业务容灾时，使用样例值，否则设置为OFF。'
          data_source: '本端规划'
          pattern: ''
          default: OFF
  examples:
    set_instpara_list:
    - PARATYPE: OMPORT
      SERVERNAME: 'paas-192-168-2-2'
      PORTTYPE: '1'
      PORTNAME: 'Eth-trunk1'
      SUBPORT: 'eth11:eth21'
      BONDMODE: '4'
      LACPRATE: '1'
      HASHPOLICY: '1'
    set_instpara_list_1:
    - PARATYPE: OMPORT
      SERVERNAME: 'paas-192-168-2-2'
      PORTTYPE: '0'
      PORTNAME: 'eth93'
    mod_me_list:
    - MEID: 0
      MENAME: 'APP'
    mod_network_list:
    - IPTYPE: IPV4
      NWNAME: OM
      VLANID: '2002'
      CONFIRM: Y
    set_omip_list:
    - OMIPTYPE: IPV4
      OMSETTYPE: SET_IP
      OMFIPADDR: '10.145.27.173'
      OMNETMASK: '255.255.255.0'
      OMIPV4GATEWAY: '10.145.27.1'
    set_omip_list_1:
    - OMIPTYPE: IPV4
      OMSETTYPE: SET_IP
      OMFIPADDR: '10.145.27.173'
      OMNETMASK: '255.255.255.0'
      OMIPV4GATEWAY: '10.145.27.1'
      OMHOST1IPV4: '10.145.27.174'
    set_omnicswapswitch_list:
    - SWITCH: ON
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录网元OM Portal，选择“应用管理 > MML”。

### 2 调整OM物理端口。仅UEG采用刀片式服务器2U硬件时，支持调整OM物理端口。

#### 2.1 执行**SET INSTPARA**调整OM物理端口。

#### 执行**SET INSTPARA**命令前，请跳转到该命令仔细阅读该命令的注意事项。

#### 该命令若执行不当，会导致所有业务中断。请确认参数正确后，再执行此操作。

#### 调整OM物理端口后需重启对应的单板。

##### 2.1.1 //规划的OM物理端口采用bonding口时：

```jinja2
{%- if is_scenario_bonding_port -%}
    {%- for item in set_instpara_list -%}
        SET INSTPARA:
        {#- --- 必选参数 --- -#}
        PARATYPE={{item.PARATYPE}},
        SERVERNAME="{{item.SERVERNAME}}",
        PORTTYPE={{item.PORTTYPE}},
        PORTNAME="{{item.PORTNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PORTTYPE=1 时必选 --- -#}
        {%- if item.PORTTYPE == '1' -%}
            SUBPORT="{{item.SUBPORT}}",
        {%- endif -%}
        {#- --- 条件必选：PORTTYPE=1 时必选 --- -#}
        {%- if item.PORTTYPE == '1' -%}
            BONDMODE={{item.BONDMODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：BONDMODE=4 时可选 --- -#}
        {%- if item.BONDMODE == '4' -%}
            {%- if item.LACPRATE is not none -%}
                LACPRATE={{item.LACPRATE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：BONDMODE=4 时可选 --- -#}
        {%- if item.BONDMODE == '4' -%}
            {%- if item.HASHPOLICY is not none -%}
                HASHPOLICY={{item.HASHPOLICY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.2 //规划的OM物理端口采用单端口时：

```jinja2
{%- if is_scenario_single_port -%}
    {%- for item in set_instpara_list_1 -%}
        SET INSTPARA:
        {#- --- 必选参数 --- -#}
        PARATYPE={{item.PARATYPE}},
        SERVERNAME="{{item.SERVERNAME}}",
        PORTTYPE={{item.PORTTYPE}},
        PORTNAME="{{item.PORTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 重启调整后的OM物理端口所在的单板。

#### 重启单板的详细操作请参见管理刀片服务器。

#### 2.3 重新登录OM Portal，并重新对接网管。

#### 执行**SET INSTPARA**命令后可能会导致OM Portal断链以及网管断链，重启单板后需重新登录OM Portal，并重新对接网管。

### 3 执行**MOD ME**将网元名称修改为现网规划的网元名称，脚本示例如下。

```jinja2
{%- for item in mod_me_list -%}
    MOD ME:
    {#- --- 必选参数 --- -#}
    MEID={{item.MEID}},
    {#- --- 可选参数 --- -#}
    {%- if item.MENAME is not none -%}
        MENAME="{{item.MENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 执行**LST NETWORK**检查VLANID是否配置正确。

### VLANID配置正确 ，执行6。

### VLANID配置不正确，执行5。

### 5 执行**MOD NETWORK**修改系统网络的网卡VLANID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_network_list的变量区（command: MOD NETWORK） -#}
<!-- MISSING_MACRO: command=MOD NETWORK list_name=mod_network_list step_id=5 -->
```

### 修改扩展域VLANID后需重启节点生效。

### 6 执行**LST OMIP**检查物理IP地址、浮动IP地址等与网设规划的数据是否一致。

### 一致，执行8。

### 不一致，执行7。

### 7 执行**SET OMIP**设置系统IP地址。

### “OM IP模式”是“精简”模式：浮动IP地址不正确时，执行**SET OMIP**将浮动IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_simple_mode -%}
    {%- for item in set_omip_list -%}
        SET OMIP:
        {#- --- 可选参数 --- -#}
        {%- if item.OMIPTYPE is not none -%}
            OMIPTYPE={{item.OMIPTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OMIPTYPE=IPV4 时可选 --- -#}
        {%- if item.OMIPTYPE == 'IPV4' -%}
            {%- if item.OMSETTYPE is not none -%}
                OMSETTYPE={{item.OMSETTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMFIPADDR is not none -%}
                OMFIPADDR="{{item.OMFIPADDR}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMNETMASK is not none -%}
                OMNETMASK="{{item.OMNETMASK}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMIPV4GATEWAY is not none -%}
                OMIPV4GATEWAY="{{item.OMIPV4GATEWAY}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### “OM IP模式”是“精简”模式时，可不配置物理IP1或将物理IP1地址设置为与浮动IP地址相同。若配置的物理IP1与浮动IP取值不同，则命令执行失败。此处以不配置物理IP1为例。

### “OM IP模式”不是“精简”模式：未配置物理IP地址或已配置的物理IP地址与现网规划的IP地址不一致，执行**SET OMIP**将浮动IP地址、物理IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_non_simple_mode -%}
    {%- for item in set_omip_list_1 -%}
        SET OMIP:
        {#- --- 可选参数 --- -#}
        {%- if item.OMIPTYPE is not none -%}
            OMIPTYPE={{item.OMIPTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OMIPTYPE=IPV4 时可选 --- -#}
        {%- if item.OMIPTYPE == 'IPV4' -%}
            {%- if item.OMSETTYPE is not none -%}
                OMSETTYPE={{item.OMSETTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMFIPADDR is not none -%}
                OMFIPADDR="{{item.OMFIPADDR}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMNETMASK is not none -%}
                OMNETMASK="{{item.OMNETMASK}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMIPV4GATEWAY is not none -%}
                OMIPV4GATEWAY="{{item.OMIPV4GATEWAY}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMHOST1IPV4 is not none -%}
                OMHOST1IPV4="{{item.OMHOST1IPV4}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### “OM IP模式”不是“精简”模式时，物理IP1须与浮动IP在同一网段。

### 8 如果已在网管上创建网元，则需要登录网管客户端，修改网管上网元名称、IP地址属性为现网规划的信息。

### 操作方法请参见MAE产品文档，“操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象”。

### 9 UEG直连DCGW场景，执行**SET OMNICSWAPSWITCH**命令，支持备OM口进行业务容灾。

```jinja2
{%- if is_scenario_direct_to_dcgw -%}
    {%- for item in set_omnicswapswitch_list -%}
        SET OMNICSWAPSWITCH:
        {#- --- 必选参数 --- -#}
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

