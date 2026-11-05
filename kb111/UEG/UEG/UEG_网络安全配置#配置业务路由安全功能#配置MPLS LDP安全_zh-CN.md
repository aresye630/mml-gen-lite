---
id: ''
name: 配置MPLS LDP安全
ne_type: UEG
type: feature
description: MD5（Message-Digest Algorithm 5）是RFC 1321定义的国际标准摘要密码算法。MD5的典型应用是针对一段信息计算出对应的信息摘要，从而防止信息被篡改。MD5信息摘要是通过不可逆的字符串变换算法产生的，结果唯一。因此，不管信息内容在传输过程中发生任何形式的改变，只要重新计算就会产生不同的信息摘要，接收端就可以由此判定收到的是一个不正确的报文。  Keychain是一种增强型加密算法，类似于MD5，Keychain也是针对同一段信息计算出对应的信息摘要，实现LDP报文防篡改校验。Keychain允许用户定义一组密码，形成一个密码串，并且分别为每个密码指定加解密算法（包括MD5，SHA-1等）及密码使用的有效时间。  为了保证更好的安全性，建议不要使用MD5和SHA-1算法。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置MPLS LDP安全"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置MPLS LDP安全"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置MPLS LDP安全"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置MPLS LDP安全"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置MPLS LDP安全"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置MPLS LDP安全"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置MPLS LDP安全"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置MPLS LDP安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
MD5（Message-Digest Algorithm 5）是RFC 1321定义的国际标准摘要密码算法。MD5的典型应用是针对一段信息计算出对应的信息摘要，从而防止信息被篡改。MD5信息摘要是通过不可逆的字符串变换算法产生的，结果唯一。因此，不管信息内容在传输过程中发生任何形式的改变，只要重新计算就会产生不同的信息摘要，接收端就可以由此判定收到的是一个不正确的报文。Keychain是一种增强型加密算法，类似于MD5，Keychain也是针对同一段信息计算出对应的信息摘要，实现LDP报文防篡改校验。Keychain允许用户定义一组密码，形成一个密码串，并且分别为每个密码指定加解密算法（包括MD5，SHA-1等）及密码使用的有效时间。为了保证更好的安全性，建议不要使用MD5和SHA-1算法。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_ldpinstance_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSRID:
          name: '实例的LSR ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: 'LDP全局认证模式'
          type: string
          enum:
          - MODE_ENABLE
          - MODE_NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENTYPE:
          name: 'LDP全局认证类型'
          type: string
          enum:
          - KEYCHAIN
          - MD5
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MD5PASSWORD:
          name: 'LDP全局MD5密码'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_ldpinstance_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSRID:
          name: '实例的LSR ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: 'LDP全局认证模式'
          type: string
          enum:
          - MODE_ENABLE
          - MODE_NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENTYPE:
          name: 'LDP全局认证类型'
          type: string
          enum:
          - KEYCHAIN
          - MD5
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYCHAINNAME:
          name: 'LDP全局KeyChain名字'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_ldpinstance_list:
    - VRFNAME: 'VPN实例名称'
      LSRID: '实例的LSR ID'
      AUTHENMODE: MODE_ENABLE
      AUTHENTYPE: MD5
      MD5PASSWORD: 'LDP全局MD5密码'
    mod_ldpinstance_list_1:
    - VRFNAME: 'VPN实例名称'
      LSRID: '实例的LSR ID'
      AUTHENMODE: MODE_ENABLE
      AUTHENTYPE: KEYCHAIN
      KEYCHAINNAME: 'LDP全局KeyChain名字'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 对所有对等体配置LDP MD5认证。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_md5_auth -%}
    {%- for item in mod_ldpinstance_list -%}
        MOD LDPINSTANCE:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LSRID is not none -%}
            LSRID="{{item.LSRID}}",
        {%- endif -%}
        {%- if item.AUTHENMODE is not none -%}
            AUTHENMODE={{item.AUTHENMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTHENMODE=MODE_ENABLE 时必选 --- -#}
        {%- if item.AUTHENMODE == 'MODE_ENABLE' -%}
            AUTHENTYPE={{item.AUTHENTYPE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHENTYPE=MD5 时必选 --- -#}
        {%- if item.AUTHENTYPE == 'MD5' -%}
            MD5PASSWORD="{{item.MD5PASSWORD}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 对所有对等体配置Keychain认证。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_keychain_auth -%}
    {%- for item in mod_ldpinstance_list_1 -%}
        MOD LDPINSTANCE:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LSRID is not none -%}
            LSRID="{{item.LSRID}}",
        {%- endif -%}
        {%- if item.AUTHENMODE is not none -%}
            AUTHENMODE={{item.AUTHENMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTHENMODE=MODE_ENABLE 时必选 --- -#}
        {%- if item.AUTHENMODE == 'MODE_ENABLE' -%}
            AUTHENTYPE={{item.AUTHENTYPE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHENTYPE=KEYCHAIN 时必选 --- -#}
        {%- if item.AUTHENTYPE == 'KEYCHAIN' -%}
            KEYCHAINNAME="{{item.KEYCHAINNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

