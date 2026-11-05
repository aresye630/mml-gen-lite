---
id: ''
name: 配置Restful接口数据
ne_type: UEG
type: feature
description: 统一定义5G网络激活与UDM能力接口的设计原则、交互场景、接口方法和参数模型等，实现5G网络激活与UDM能力标准化，支持集约管理和业务快速上线。  5G核心网网元能力接口由设备厂商按Restful接口规范标准封装，通过接收5G业务激活请求，实现5G核心网网元激活。  UDM网元支持Restful接口协议，当需要与对端业务发放系统的Restful接口对接时，参考本页面内容对Restful接口进行适配。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置UDM","配置Restful接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
统一定义5G网络激活与UDM能力接口的设计原则、交互场景、接口方法和参数模型等，实现5G网络激活与UDM能力标准化，支持集约管理和业务快速上线。5G核心网网元能力接口由设备厂商按Restful接口规范标准封装，通过接收5G业务激活请求，实现5G核心网网元激活。UDM网元支持Restful接口协议，当需要与对端业务发放系统的Restful接口对接时，参考本页面内容对Restful接口进行适配。

## 必备事项
前提条件

* 具有访问http://support.huawei.com网站及下载软件包的权限。
* 已完成软件安装及基础数据配置。
* 已完成配置PGW与业务发放系统的对接数据（风筝M）。
* 已获取营帐适配指导书。
* 已获取营帐适配包。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    lod_pkg_list:
      type: items
      properties:
        FNM:
          name: '文件名称'
          type: string
          maxLength: 128
          required: true
          description: '与实际获取的营帐适配包名称一致。'
          data_source: ''
          pattern: ''
          default: ''
    lod_adpplug_list:
      type: items
      properties:
        UPFILENAME:
          name: '适配插件包名称'
          type: string
          maxLength: 128
          required: true
          description: '与实际获取的营帐适配包名称一致。'
          data_source: ''
          pattern: ''
          default: ''
    add_port_list:
      type: items
      properties:
        PORTNO:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '指定增加的PGW开放给业务发放系统和Web LMT使用的端口的编号。当参数“端口类型”为“PORT\_FOR\_PROV”时，端口号取值范围为：1～65535，建议端口范围为1025～65535。由运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        PORTTYPE:
          name: '端口类型'
          type: string
          enum:
          - PORT_FOR_WEBLMT
          - PORT_FOR_PROV
          required: true
          description: 'PGW开放给业务发放系统的端口。'
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
          - PORT_FOR_REST
          - PORT_FOR_HTTP
          required: true
          description: 'PGW开放给业务发放系统的REST服务端口。'
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
          description: '系统不对此端口进行屏蔽，端口可正常工作。'
          data_source: ''
          pattern: ''
          default: NO
        PORTBUSSTYPE:
          name: '端口业务类型'
          type: string
          maxLength: 128
          required: false
          description: '用于指定PGW开放给业务发放系统的端口对应的业务类型。'
          data_source: ''
          pattern: ''
          default: ''
        HEADERAUTH:
          name: '是否使用头域鉴权'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '此参数需要根据对端的业务发放系统的要求进行设置。NO表示PGW不需要对SOAP或REST消息头域中携带的登录信息进行登录鉴权。'
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
          description: '指定待复位的模块。根据现网实际规划配置。需要重启所有的PGW模块。'
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
    lod_pkg_list:
    - FNM: 'AdpConfig_HSS9860_XXXX_REST_V500R020C20.tar'
    lod_adpplug_list:
    - UPFILENAME: 'AdpConfig_HSS9860_XXXX_REST_V500R020C20.tar'
    add_port_list:
    - PORTNO: 8002
      PORTTYPE: PORT_FOR_PROV
      PORTTYPENAME: PORT_FOR_REST
      DISABLEPORT: NO
      PORTBUSSTYPE: 'HSS9860'
      HEADERAUTH: NO
    rst_module_list:
    - MID: 7
      MT: PGW
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 上传获取的营帐适配包到“CGPLite文件 > SOFTWARE PACKAGE”目录下。上传的详细操作请参见文件传输。

### 3 在“CSP MML命令”界面，执行**LOD PKG**命令加载包文件。

```jinja2
{%- for item in lod_pkg_list -%}
    LOD PKG:
    {#- --- 必选参数 --- -#}
    FNM="{{item.FNM}}",
    ;
{%- endfor -%}
```

### 4 执行**LST PKG**查询包文件是否加载成功。

### 5 在“USCDB MML命令”界面，执行**LOD ADPPLUG**命令添加适配插件。

```jinja2
{%- for item in lod_adpplug_list -%}
    LOD ADPPLUG:
    {#- --- 必选参数 --- -#}
    UPFILENAME="{{item.UPFILENAME}}",
    ;
{%- endfor -%}
```

### 6 执行**ADD PORT**命令添加PGW业务消息端口。

```jinja2
{%- for item in add_port_list -%}
    ADD PORT:
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
    {#- --- 条件可选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_MML/PORT_FOR_REST/PORT_FOR_HTTP 时可选 --- -#}
    {%- if item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_MML', 'PORT_FOR_REST', 'PORT_FOR_HTTP'] -%}
        {%- if item.DISABLEPORT is not none -%}
            DISABLEPORT={{item.DISABLEPORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PORTTYPENAME=PORT_FOR_SOAP/PORT_FOR_REST 时可选 --- -#}
    {%- if item.PORTTYPENAME in ['PORT_FOR_SOAP', 'PORT_FOR_REST'] -%}
        {%- if item.HEADERAUTH is not none -%}
            HEADERAUTH={{item.HEADERAUTH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 执行**RST MODULE**命令复位模块。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MID={{item.MID}},
    MT={{item.MT}},
    ;
{%- endfor -%}
```

### 此处重启模块的“MID”仅作为样例，需要重启所有的PGW模块。

### 8 重启完成后，执行**DSP ADPPLUG**命令查看PGW模块均为“加载成功”状态，则表示适配包加载成功。

### RETCODE = 0  操作成功

### 操作结果如下

### ------------

### 模块号  =  7

### 适配文件加载状态  =  加载成功

### 定制插件包加载状态  =  加载成功

### 融合插件包加载状态  =   NULL

### 适配包文件名  =  AdpConfig_HSS9860_XXXX_REST_V500R020C20.tar

### OMU加载的适配包描述  =  NULL

### OMU加载的适配包版本  =  NULL

### PGW加载的适配包描述  =  NULL

### PGW加载的适配包版本  =  NULL

### (结果个数 = 1)

### ---    END

