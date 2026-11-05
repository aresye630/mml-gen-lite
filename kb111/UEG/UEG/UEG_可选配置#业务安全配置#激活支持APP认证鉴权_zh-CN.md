---
id: ''
name: 激活支持APP认证鉴权
ne_type: UEG
type: feature
description: PGW-U/UPF能力开放满足基本安全要求，包括API认证授权、传输加密，对APP进行认证鉴权时需要配置鉴权开关等信息。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","激活支持APP认证鉴权"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","业务安全配置","激活支持APP认证鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PGW-U/UPF能力开放满足基本安全要求，包括API认证授权、传输加密，对APP进行认证鉴权时需要配置鉴权开关等信息。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-023504 支持APP认证鉴权特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    set_apiauth_list:
      type: items
      properties:
        ISAUTH:
          name: '鉴权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '打开Oauth2.0鉴权开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mepauthmode_list:
      type: items
      properties:
        AUTHMODE:
          name: '授权模式'
          type: string
          enum:
          - BYAPPD
          - BYLOCALPARA
          - BYMM5PARA
          required: true
          description: '本参数设置为“BYLOCALPARA”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_authservlist_list:
      type: items
      properties:
        NAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_authserv_list:
      type: items
      properties:
        SERVICENAME:
          name: '授权服务名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: 'asr为UPF内部服务，APP服务名称由服务提供商提供。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICELISTNAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD AUTHSERVLIST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHVALIDTIME:
          name: '授权有效时间的截止时间'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: 'YYYY&MM&DD&HH&NN&SS'
    add_appauthinfo_list:
      type: items
      properties:
        APPID:
          name: 'APP标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APPID和APIKEY由APP侧提供。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APIKEY:
          name: 'APP访问凭证'
          type: string
          minLength: 0
          maxLength: 60
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICELISTNAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD AUTHSERVLIST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_authappinstance_list:
      type: items
      properties:
        APPINSTANCEID:
          name: 'APP实例ID'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPID:
          name: 'APP标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5APIG01'
      SWITCH: ENABLE
    set_apiauth_list:
    - ISAUTH: ENABLE
    set_mepauthmode_list:
    - AUTHMODE: BYLOCALPARA
    add_authservlist_list:
    - NAME: 'serviceList'
    add_authserv_list:
    - SERVICENAME: 'servicename'
      SERVICELISTNAME: 'serviceList'
      AUTHVALIDTIME: '2022&01&13&11&02&59'
    add_appauthinfo_list:
    - APPID: 'appid_123'
      APIKEY: 'keyjfljiosajfwefiofsaffsdfsfssaffsfsffsf'
      SERVICELISTNAME: 'serviceList'
    add_authappinstance_list:
    - APPINSTANCEID: 'appid_1232435'
      APPID: 'appid_123'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 打开API GW的Oauth2.0鉴权开关。

```jinja2
{%- for item in set_apiauth_list -%}
    SET APIAUTH:
    {#- --- 必选参数 --- -#}
    ISAUTH={{item.ISAUTH}},
    ;
{%- endfor -%}
```

### 3 配置API GW的鉴权模式。

### 采用APPID和APIKey进行Oauth2.0鉴权，“授权模式”设置为“BYLOCALPARA”。

```jinja2
{%- for item in set_mepauthmode_list -%}
    SET MEPAUTHMODE:
    {#- --- 必选参数 --- -#}
    AUTHMODE={{item.AUTHMODE}},
    ;
{%- endfor -%}
```

### 4 增加授权服务列表。

```jinja2
{%- for item in add_authservlist_list -%}
    ADD AUTHSERVLIST:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    ;
{%- endfor -%}
```

### 5 增加APP授权服务，其中“授权服务名称”需要由服务提供商提供。

```jinja2
{%- for item in add_authserv_list -%}
    ADD AUTHSERV:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    SERVICELISTNAME="{{item.SERVICELISTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHVALIDTIME is not none -%}
        AUTHVALIDTIME={{item.AUTHVALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加APP授权信息，包含鉴权的APPID、APIKey信息和授权服务。

```jinja2
{%- for item in add_appauthinfo_list -%}
    ADD APPAUTHINFO:
    {#- --- 必选参数 --- -#}
    APPID="{{item.APPID}}",
    APIKEY="{{item.APIKEY}}",
    SERVICELISTNAME="{{item.SERVICELISTNAME}}",
    ;
{%- endfor -%}
```

### 7 建议一个APP实例绑定一个APPID，即每个APP实例独享一个APPID身份，否则共享APPID之间的APP实例均存在互相仿冒身份的风险。

```jinja2
{%- for item in add_authappinstance_list -%}
    ADD AUTHAPPINSTANCE:
    {#- --- 必选参数 --- -#}
    APPINSTANCEID="{{item.APPINSTANCEID}}",
    APPID="{{item.APPID}}",
    ;
{%- endfor -%}
```

