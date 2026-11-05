---
id: ''
name: 配置直播业务的媒体中继域名（直播域名）
ne_type: UDG
type: feature
description: 使用媒体中继业务时，需要配置媒体中继模板使用的媒体中继域名。本章节用于指导如何配置媒体中继模板使用的直播域名。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体服务商配置（基于OTT应用）","配置直播业务的媒体中继域名（直播域名）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
使用媒体中继业务时，需要配置媒体中继模板使用的媒体中继域名。本章节用于指导如何配置媒体中继模板使用的直播域名。

## 必备事项
前提条件

已参考增加媒体服务商基础配置完成媒体中继模板配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_relaydomain_list:
      type: items
      properties:
        RELAYTPLNAME:
          name: '媒体中继模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过ADD RELAYTEMPLATE完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RELAYDOMAINNAME:
          name: '媒体中继域名配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数与OTT为媒体中继业务规划的媒体中继域名保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        UESERVICEPROTO:
          name: 'UE业务请求协议'
          type: string
          enum:
          - BOTH
          - HTTP
          - HTTPS
          required: false
          description: '该参数用于设置UE请求支持的协议。'
          data_source: '全网规划'
          pattern: ''
          default: HTTPS
        ORIGINPULLPROTO:
          name: '业务回源协议'
          type: string
          enum:
          - HTTPS
          - HTTP
          - FLWUE
          required: false
          description: '该参数用于设置业务从CDN回源时使用的协议。'
          data_source: '全网规划'
          pattern: ''
          default: HTTPS
        SERVICETYPE:
          name: '业务服务类型'
          type: string
          enum:
          - VOD
          - LIVE
          - BOTH
          required: true
          description: '该参数用于设置媒体中继业务支持的业务服务类型。LIVE表示直播。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LIVEPROTOTYPE:
          name: '直播协议类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UNSPTMEDIAACT:
          name: '不支持的媒体访问动作'
          type: string
          enum:
          - REDIRECT
          - FORBIDDEN
          required: false
          description: '该参数用于配置对于无法识别出的媒体文件，UPF的处理原则。'
          data_source: '本端规划'
          pattern: ''
          default: REDIRECT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VODPROTOTYPE:
          name: '点播协议类型'
          type: string
          required: false
          description: '直播固定是FLV.'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DEFAULTVODSW:
          name: '缺省点播业务开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_relayauthkey_list:
      type: items
      properties:
        RELAYAUTHKEYNAME:
          name: '媒体中继鉴权密钥名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '用于配置URL鉴权使用的鉴权密钥名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MASTERAUTHKEY:
          name: '主鉴权密钥'
          type: string
          minLength: 6
          maxLength: 64
          required: true
          description: '由OTT规划，用于媒体中继UPF对终端APP携带URL鉴权参数进行校验。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MASTERKEYCONFIRM:
          name: '确认主鉴权密钥'
          type: string
          minLength: 6
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLAVEAUTHKEY:
          name: '备鉴权密钥'
          type: string
          minLength: 6
          maxLength: 64
          required: false
          description: '由OTT规划，用于媒体中继UPF对终端APP携带URL鉴权参数进行校验。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SLAVEKEYCONFIRM:
          name: '确认备鉴权密钥'
          type: string
          minLength: 6
          maxLength: 64
          required: false
          description: '与备鉴权密钥保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_relayurlauth_list:
      type: items
      properties:
        RELAYURLAUTHNM:
          name: '媒体中继URL鉴权名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '用于配置URL鉴权使用的鉴权方式名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RELAYAUTHKEYNM:
          name: '媒体中继鉴权密钥名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过ADD RELAYAUTHKEY命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        URLAUTHMETHOD:
          name: 'URL鉴权方法'
          type: string
          enum:
          - TYPEA
          - TYPEB
          - TYPEC1
          - TYPEC2
          - TYPED
          required: true
          description: '由OTT规划，用于媒体中继UPF对终端APP携带ULR鉴权参数进行校验。抖音通常使用TypeC2。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALGORITHM:
          name: '加密算法'
          type: string
          enum:
          - MD5
          - SHA256
          - HMAC_SHA1
          required: true
          description: '由OTT规划，用于媒体中继UPF对终端APP携带ULR鉴权参数进行校验。'
          data_source: '与对端协商'
          pattern: ''
          default: SHA256
        TIMESTAMPFMT:
          name: '时间戳格式'
          type: string
          enum:
          - DECSEC
          - HEXSEC
          - TIMESTAMP
          - DEFAULT
          required: false
          description: '由OTT规划，用于媒体中继UPF对终端APP携带ULR鉴权参数进行校验。'
          data_source: '与对端协商'
          pattern: ''
          default: DEFAULT
        AUTHFAILACT:
          name: '鉴权失败动作'
          type: string
          enum:
          - FORBIDDEN
          - REDIRECT
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: FORBIDDEN
        DASHAUTHEXTSW:
          name: 'Dash扩展鉴权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        AUTHFIELDNAME:
          name: '鉴权字段名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'auth_key'
        TIMESTAMPNAME:
          name: '时间戳字段名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'timestamp'
    mod_relaydomain_list:
      type: items
      properties:
        RELAYDOMAINNAME:
          name: '媒体中继域名配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过  ADD RELAYDOMAIN命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        URLAUTHNAME:
          name: 'URL鉴权名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过ADD RELAYURLAUTH完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_relayhttpmctl_list:
      type: items
      properties:
        HTTPMSGCTRLNAME:
          name: '媒体中继Http消息控制名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_relayhttpmhd_list:
      type: items
      properties:
        HTTPMSGCTRLNAME:
          name: 'HTTP消息控制名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过  ADD RELAYHTTPMCTL命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - UEHTTPRSP
          - CDNHTTPREQ
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HEADERNAME:
          name: '头域名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HEADERVALUE:
          name: '头域值'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_relaydomain_list_1:
      type: items
      properties:
        RELAYDOMAINNAME:
          name: '媒体中继域名配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPMSGCTRLNAME:
          name: '媒体中继Http消息控制名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_relaydomain_list:
    - RELAYTPLNAME: 'sp_relay_tpl'
      RELAYDOMAINNAME: 'sp_relay_dm_live_001'
      DOMAINVALUE: 'relay.spliving.com'
      UESERVICEPROTO: HTTPS
      ORIGINPULLPROTO: HTTPS
      SERVICETYPE: LIVE
      LIVEPROTOTYPE: FLV-1
      UNSPTMEDIAACT: REDIRECT
      PRIORITY: 1000
      VODPROTOTYPE: FLV-1
      DEFAULTVODSW: DISABLE
    add_relayauthkey_list:
    - RELAYAUTHKEYNAME: 'relay_ak_sp_live_001'
      MASTERAUTHKEY: '***'
      MASTERKEYCONFIRM: '***"，SLAVEAUTHKEY="***'
      SLAVEAUTHKEY: '***'
      SLAVEKEYCONFIRM: '***'
    add_relayurlauth_list:
    - RELAYURLAUTHNM: 'relay_ur_sp_live_001'
      RELAYAUTHKEYNM: 'relay_ak_sp_live_001'
      URLAUTHMETHOD: TYPEA
      ALGORITHM: SHA256
      TIMESTAMPFMT: DEFAULT
      AUTHFAILACT: FORBIDDEN
      DASHAUTHEXTSW: DISABLE
      AUTHFIELDNAME: 'auth_key'
      TIMESTAMPNAME: 'timestamp'
    mod_relaydomain_list:
    - RELAYDOMAINNAME: 'sp_relay_dm_live_001'
      URLAUTHNAME: 'relay_ur_sp_live_001'
    add_relayhttpmctl_list:
    - HTTPMSGCTRLNAME: 'sp_relay_hhd_live_001'
    add_relayhttpmhd_list:
    - HTTPMSGCTRLNAME: 'sp_relay_hhd_live_001'
      MSGTYPE: UEHTTPRSP
      HEADERNAME: 'Cache-Control'
      HEADERVALUE: 'no-cache'
    mod_relaydomain_list_1:
    - RELAYDOMAINNAME: 'sp_relay_dm_live_001'
      HTTPMSGCTRLNAME: 'sp_relay_hhd_live_001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //增加直播域名配置，支持FLV类型的直播为业务。

```jinja2
{%- for item in add_relaydomain_list -%}
    ADD RELAYDOMAIN:
    {#- --- 必选参数 --- -#}
    RELAYTPLNAME="{{item.RELAYTPLNAME}}",
    RELAYDOMAINNAME="{{item.RELAYDOMAINNAME}}",
    DOMAINVALUE="{{item.DOMAINVALUE}}",
    SERVICETYPE={{item.SERVICETYPE}},
    PRIORITY={{item.PRIORITY}},
    {#- --- 可选参数 --- -#}
    {%- if item.UESERVICEPROTO is not none -%}
        UESERVICEPROTO={{item.UESERVICEPROTO}},
    {%- endif -%}
    {%- if item.ORIGINPULLPROTO is not none -%}
        ORIGINPULLPROTO={{item.ORIGINPULLPROTO}},
    {%- endif -%}
    {%- if item.UNSPTMEDIAACT is not none -%}
        UNSPTMEDIAACT={{item.UNSPTMEDIAACT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SERVICETYPE=LIVE/BOTH 时必选 --- -#}
    {%- if item.SERVICETYPE in ['LIVE', 'BOTH'] -%}
        LIVEPROTOTYPE={{item.LIVEPROTOTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SERVICETYPE=VOD/BOTH 时必选 --- -#}
    {%- if item.SERVICETYPE in ['VOD', 'BOTH'] -%}
        VODPROTOTYPE={{item.VODPROTOTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SERVICETYPE=VOD/BOTH 时可选 --- -#}
    {%- if item.SERVICETYPE in ['VOD', 'BOTH'] -%}
        {%- if item.DEFAULTVODSW is not none -%}
            DEFAULTVODSW={{item.DEFAULTVODSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置直播URL鉴权规则。以鉴权算法为“TypeA"、加密算法为“SHA256为例。

```jinja2
{%- for item in add_relayauthkey_list -%}
    ADD RELAYAUTHKEY:
    {#- --- 必选参数 --- -#}
    RELAYAUTHKEYNAME="{{item.RELAYAUTHKEYNAME}}",
    MASTERAUTHKEY="{{item.MASTERAUTHKEY}}",
    MASTERKEYCONFIRM="{{item.MASTERKEYCONFIRM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SLAVEAUTHKEY is not none -%}
        SLAVEAUTHKEY="{{item.SLAVEAUTHKEY}}",
    {%- endif -%}
    {%- if item.SLAVEKEYCONFIRM is not none -%}
        SLAVEKEYCONFIRM="{{item.SLAVEKEYCONFIRM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_relayurlauth_list -%}
    ADD RELAYURLAUTH:
    {#- --- 必选参数 --- -#}
    RELAYURLAUTHNM="{{item.RELAYURLAUTHNM}}",
    RELAYAUTHKEYNM="{{item.RELAYAUTHKEYNM}}",
    URLAUTHMETHOD={{item.URLAUTHMETHOD}},
    ALGORITHM={{item.ALGORITHM}},
    {#- --- 可选参数 --- -#}
    {%- if item.TIMESTAMPFMT is not none -%}
        TIMESTAMPFMT={{item.TIMESTAMPFMT}},
    {%- endif -%}
    {%- if item.AUTHFAILACT is not none -%}
        AUTHFAILACT={{item.AUTHFAILACT}},
    {%- endif -%}
    {%- if item.DASHAUTHEXTSW is not none -%}
        DASHAUTHEXTSW={{item.DASHAUTHEXTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLAUTHMETHOD=TYPEA/TYPEC2/TYPED 时可选 --- -#}
    {%- if item.URLAUTHMETHOD in ['TYPEA', 'TYPEC2', 'TYPED'] -%}
        {%- if item.AUTHFIELDNAME is not none -%}
            AUTHFIELDNAME="{{item.AUTHFIELDNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：URLAUTHMETHOD=TYPEC2/TYPED 时可选 --- -#}
    {%- if item.URLAUTHMETHOD in ['TYPEC2', 'TYPED'] -%}
        {%- if item.TIMESTAMPNAME is not none -%}
            TIMESTAMPNAME="{{item.TIMESTAMPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_relaydomain_list -%}
    MOD RELAYDOMAIN:
    {#- --- 必选参数 --- -#}
    RELAYDOMAINNAME="{{item.RELAYDOMAINNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URLAUTHNAME is not none -%}
        URLAUTHNAME="{{item.URLAUTHNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置HTTP头域字段，并绑定到域名下。

```jinja2
{%- for item in add_relayhttpmctl_list -%}
    ADD RELAYHTTPMCTL:
    {#- --- 必选参数 --- -#}
    HTTPMSGCTRLNAME="{{item.HTTPMSGCTRLNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_relayhttpmhd_list -%}
    ADD RELAYHTTPMHD:
    {#- --- 必选参数 --- -#}
    HTTPMSGCTRLNAME="{{item.HTTPMSGCTRLNAME}}",
    MSGTYPE={{item.MSGTYPE}},
    HEADERNAME="{{item.HEADERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HEADERVALUE is not none -%}
        HEADERVALUE="{{item.HEADERVALUE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_relaydomain_list_1 -%}
    MOD RELAYDOMAIN:
    {#- --- 必选参数 --- -#}
    RELAYDOMAINNAME="{{item.RELAYDOMAINNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPMSGCTRLNAME is not none -%}
        HTTPMSGCTRLNAME="{{item.HTTPMSGCTRLNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

