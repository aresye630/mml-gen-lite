---
id: ''
name: 修改网元基本信息
ne_type: UEG
type: feature
description: 软件安装阶段，已完成网元名称和浮动IP地址的配置。在生产预安装场景或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称和浮动IP地址。  * 网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。 * 修改浮动IP时，请参考网元的改造OM网络方案改造OM网络。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置基础数据（虚机容器）","修改网元基本信息"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置基础数据（虚机容器）","修改网元基本信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
软件安装阶段，已完成网元名称和浮动IP地址的配置。在生产预安装场景或者现网使用时，如果需要修改，可参考本页面调整登录网元OM Portal的网元名称和浮动IP地址。* 网元名称、浮动IP地址需要与网管上配置的名称和IP地址属性一致，如果本端修改了网元名称和浮动IP地址，需要在网管上同步修改该网元的名称和IP地址属性。* 修改浮动IP时，请参考网元的改造OM网络方案改造OM网络。

## 必备事项
前提条件

前提条件

* 已经确认现网规划的网元名称、浮动IP地址与网元生产预安装的预设参数值不同。
* 调测PC需要能够与修改前浮动IP地址通信，已登录网元OM Portal。
* 已从网管侧获取网管登录信息。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          description: '从“5G Core LLD文档 > 业务IP对接设计”页签获取。  在“虚拟机类型”为“OMU”且“IP类别”为“Floating IP”的行，可获取规划的浮动IP地址、子网掩码和默认网关参数值。'
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
          description: '从“5G Core LLD文档 > 业务IP对接设计”页签获取。  在“虚拟机类型”为“OMU”且“IP类别”为“Floating IP”的行，可获取规划的浮动IP地址、子网掩码和默认网关参数值。'
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
          description: '物理IP地址需要与浮动IP地址在同一网段。  从“5G Core LLD文档 > 业务IP对接设计”页签获取。  在“虚拟机类型”为“OMU”且“IP类别”为“External IP”的行，可获取规划的物理IP参数值。'
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
    mod_me_list:
    - MEID: 0
      MENAME: 'APP'
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

### 2 执行**MOD ME**将网元名称修改为现网规划的网元名称，脚本示例如下。

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

### 3 执行**LST OMIP**查询系统是否已配置物理IP地址且符合现网规划的IP地址。

### 4 执行**SET OMIP**设置系统IP地址。

#### 4.1 如果系统已配置物理IP地址且符合现网规划的IP地址，执行**SET OMIP**将浮动IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_physical_ip_configured_matched -%}
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

#### 4.2 如果系统未配置物理IP地址或已配置的物理IP地址与现网规划的IP地址不符，执行**SET OMIP**将浮动IP地址、物理IP地址修改为现网规划的IP地址，脚本示例如下。

```jinja2
{%- if is_scenario_physical_ip_unconfigured_mismatched -%}
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

### 5 如果已在网管上创建网元，则需要登录网管客户端，修改网管上网元名称、IP地址属性为现网规划的信息。

### 操作方法请参见MAE产品文档，“操作与维护 > MAE-Access操作与维护 > 拓扑管理 > 维护拓扑对象 > 修改拓扑对象”。

