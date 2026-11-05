---
id: ''
name: 修改网元基本信息
ne_type: UEG
type: feature
description: 软件安装阶段，已完成网元名称和浮动IP地址的配置。在生产预安装场景或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称和浮动IP地址。  网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置基础数据（裸机容器）","修改网元基本信息"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置基础数据（裸机容器）","修改网元基本信息"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","基础数据配置","修改网元基本信息"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","基础数据配置","修改网元基本信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
软件安装阶段，已完成网元名称和浮动IP地址的配置。在生产预安装场景或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称和浮动IP地址。网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。

## 必备事项
前提条件

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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: OMPORT
        SERVERNAME:
          name: '服务器名称'
          type: string
          maxLength: 64
          required: true
          description: '-'
          data_source: '执行**LST INSTPARA**查询'
          pattern: ''
          default: ''
        PORTTYPE:
          name: '网口类型'
          type: string
          enum:
          - '0'
          - '1'
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: '0'
        PORTNAME:
          name: '网口名称'
          type: string
          maxLength: 9
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBPORT:
          name: '子网口'
          type: string
          maxLength: 32
          required: false
          description: '-'
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
          description: '-'
          data_source: '本端规划'
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
          enum:
          - IPV4
          - IPV6
          - IPV4/IPV6
          required: true
          description: '-'
          data_source: '执行**LST NETWORK**查询'
          pattern: ''
          default: ''
        NWNAME:
          name: '网络名称'
          type: string
          maxLength: 512
          required: true
          description: ''
          data_source: '执行**LST NETWORK**查询'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLANID'
          type: integer
          minimum: 0
          maximum: 4094
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '-'
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
          description: '-'
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
          description: '物理IP地址需要与浮动IP地址在同一网段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OMHOST2IPV4:
          name: '物理IP2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_instpara_list:
    - PARATYPE: OMPORT
      SERVERNAME: 'paas-192-168-2-3'
      PORTTYPE: '1'
      PORTNAME: 'bond1'
      SUBPORT: 'eth60:eth61'
      BONDMODE: '4'
      LACPRATE: '1'
      HASHPOLICY: '1'
    mod_me_list:
    - MEID: 0
      MENAME: 'APP'
    mod_network_list:
    - IPTYPE: IPV4
      NWNAME: 'OM'
      VLANID: 2002
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
      OMHOST2IPV4: '10.145.27.175'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录网元OM Portal，选择“应用管理 > MML”。

### 2 执行**SET INSTPARA**设置安装参数。

### 该命令执行后可能会导致OM Portal断链以及网管断链，执行后需重新登录OM Portal，并重新对接网管。该命令若执行不当，会导致所有业务中断。请确认参数正确后，再执行此操作。

```jinja2
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
```

### 当单板故障或现网网络调整时，可通过该命令设置安装参数。

### 执行完此命令之后，需要重启对应的单板。

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
{%- for item in mod_network_list -%}
    MOD NETWORK:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    NWNAME="{{item.NWNAME}}",
    VLANID={{item.VLANID}},
    ;
{%- endfor -%}
```

### 修改扩展域VLANID后需重启节点生效。

### 6 执行**LST OMIP**查询系统是否已配置物理IP地址且符合现网规划的IP地址。

### 7 执行**SET OMIP**设置系统IP地址。

#### 7.1 如果系统已配置物理IP地址且符合现网规划的IP地址，执行**SET OMIP**将浮动IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_physical_ip_configured -%}
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

#### 若DeployTool工具安装参数“OM IP模式”配置为“精简”，则浮动IP地址与物理IP地址取值相同，无需执行该步骤。

#### 7.2 如果系统未配置物理IP地址或已配置的物理IP地址与现网规划的IP地址不符，执行**SET OMIP**将浮动IP地址、物理IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_physical_ip_not_configured -%}
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
        {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
        {%- if item.OMSETTYPE == 'SET_IP' -%}
            {%- if item.OMHOST2IPV4 is not none -%}
                OMHOST2IPV4="{{item.OMHOST2IPV4}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 若DeployTool工具安装参数“OM IP模式”配置为“精简”，则需配置浮动IP地址与物理IP地址取值相同，否则命令执行失败，返回错误码。

### 8 如果已在网管上创建网元，则需要登录网管客户端，修改网管上网元名称、IP地址属性为现网规划的信息。

### 操作方法请参见MAE产品文档，“操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象”。

