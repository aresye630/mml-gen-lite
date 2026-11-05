---
id: ''
name: 配置业务发放系统的安全接入策略
ne_type: UEG
type: feature
description: 当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置业务发放系统的安全接入策略。  业务发放系统的安全策略包括以下两方面：  * 当局点只使用MML协议接入业务发放系统，建议关闭SOAP协议接入的端口。 * 当局点只使用SOAP协议接入业务发放系统，建议关闭MML协议接入的端口。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置业务发放系统的安全接入策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置业务发放系统的安全接入策略。业务发放系统的安全策略包括以下两方面：* 当局点只使用MML协议接入业务发放系统，建议关闭SOAP协议接入的端口。* 当局点只使用SOAP协议接入业务发放系统，建议关闭MML协议接入的端口。

## 必备事项
前提条件

已获取OM Portal的帐号和密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_port_list:
      type: items
      properties:
        PORTNO:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPE:
          name: '端口类型'
          type: string
          enum:
          - PORT_FOR_WEBLMT
          - PORT_FOR_PROV
          - PORT_FOR_DMSWEB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPENAME:
          name: '端口子类型'
          type: string
          enum:
          - PORT_FOR_CLIENT
          - PORT_FOR_LMT_MML
          - PORT_FOR_SOAP
          - PORT_FOR_MML
          - PORT_FOR_REDIRECT
          - PORT_FOR_DMSWEB
          - PORT_FOR_REST
          - PORT_FOR_HTTP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISABLEPORT:
          name: '是否屏蔽本端口'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTBUSSTYPE:
          name: '端口业务类型'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_port_list_1:
      type: items
      properties:
        PORTNO:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPE:
          name: '端口类型'
          type: string
          enum:
          - PORT_FOR_WEBLMT
          - PORT_FOR_PROV
          - PORT_FOR_DMSWEB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPENAME:
          name: '端口子类型'
          type: string
          enum:
          - PORT_FOR_CLIENT
          - PORT_FOR_LMT_MML
          - PORT_FOR_SOAP
          - PORT_FOR_MML
          - PORT_FOR_REDIRECT
          - PORT_FOR_DMSWEB
          - PORT_FOR_REST
          - PORT_FOR_HTTP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISABLEPORT:
          name: '是否屏蔽本端口'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTBUSSTYPE:
          name: '端口业务类型'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_module_list:
      type: items
      properties:
        MID:
          name: '模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT:
          name: '模块类型'
          type: string
          enum:
          - DPU
          - NDF
          - DBG
          - DSG
          - DRU
          - DSU
          - PGW
          - DMA
          - CAG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_port_list:
    - PORTNO: 端口号
      PORTTYPE: PORT_FOR_PROV
      PORTTYPENAME: PORT_FOR_SOAP
      DISABLEPORT: YES
      PORTBUSSTYPE: '端口业务类型'
    mod_port_list_1:
    - PORTNO: 端口号
      PORTTYPE: PORT_FOR_WEBLMT
      PORTTYPENAME: PORT_FOR_LMT_MML
      DISABLEPORT: YES
      PORTBUSSTYPE: '端口业务类型'
    rst_module_list:
    - MID: 模块号
      MT: PGW
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

#### 1.1 若该局点只使用MML协议接入营帐，则关闭SOAP协议接入的端口：

##### 1.1.1 执行**LST PORT**命令查询所有“端口类型”为“PORT\_FOR\_PROV”， “端口子类型”为“PORT\_FOR\_SOAP”的端口。

##### 1.1.2 执行**MOD PORT**命令将该端口的“是否屏蔽本端口”置为“YES”。

```jinja2
{%- if is_scenario_mml_only -%}
    {%- for item in mod_port_list -%}
        MOD PORT:
        {#- --- 必选参数 --- -#}
        PORTNO={{item.PORTNO}},
        PORTTYPE={{item.PORTTYPE}},
        PORTTYPENAME={{item.PORTTYPENAME}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时必选 --- -#}
        {%- if item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
            PORTBUSSTYPE="{{item.PORTBUSSTYPE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_LMT_MML/PORT_FOR_CLIENT 时可选 --- -#}
        {%- if item.PORTTYPENAME in ['PORT_FOR_LMT_MML', 'PORT_FOR_CLIENT'] -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时可选 --- -#}
        {%- elif item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_DMSWEB 时可选 --- -#}
        {%- elif item.PORTTYPENAME == 'PORT_FOR_DMSWEB' -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 若该局点只使用SOAP协议接入营帐，关闭MML协议接入的端口：

##### 1.2.1 执行**LST PORT**命令查询所有“端口类型”为“PORT\_FOR\_WEBLMT”， “端口子类型”为“PORT\_FOR\_LMT\_MML”的端口。

##### 1.2.2 执行**MOD PORT**命令将该端口的“是否屏蔽本端口”置为“YES”。

```jinja2
{%- if is_scenario_soap_only -%}
    {%- for item in mod_port_list_1 -%}
        MOD PORT:
        {#- --- 必选参数 --- -#}
        PORTNO={{item.PORTNO}},
        PORTTYPE={{item.PORTTYPE}},
        PORTTYPENAME={{item.PORTTYPENAME}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时必选 --- -#}
        {%- if item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
            PORTBUSSTYPE="{{item.PORTBUSSTYPE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_LMT_MML/PORT_FOR_CLIENT 时可选 --- -#}
        {%- if item.PORTTYPENAME in ['PORT_FOR_LMT_MML', 'PORT_FOR_CLIENT'] -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时可选 --- -#}
        {%- elif item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {#- --- 条件可选：PORTTYPENAME=PORT_FOR_DMSWEB 时可选 --- -#}
        {%- elif item.PORTTYPENAME == 'PORT_FOR_DMSWEB' -%}
            {%- if item.DISABLEPORT is not none -%}
                DISABLEPORT={{item.DISABLEPORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 重启PGW进程会导致短暂的业务发放指令执行失败，因此推荐此操作在夜间执行，请运营商客户提前做好准备。

### 重启所有PGW模块使修改生效。

#### 2.1 执行**LST MODULE**命令查出所有PGW模块号。

#### 2.2 按查询得到的PGW模块号依次执行**RST MODULE**命令重启模块。连续的命令间请间隔一分钟，以等待上一模块启动后再重启下一模块。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MID={{item.MID}},
    MT={{item.MT}},
    ;
{%- endfor -%}
```

