---
id: ''
name: 增加媒体服务商基础配置
ne_type: UDG
type: feature
description: 使用媒体中继业务时，需要基于媒体服务商（OTT）规划媒体中继业务使用的IP地址及媒体中继模板等全局配置。本章节用于指导如何增加媒体中继服务商相关的基础配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体服务商配置（基于OTT应用）","增加媒体服务商基础配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
使用媒体中继业务时，需要基于媒体服务商（OTT）规划媒体中继业务使用的IP地址及媒体中继模板等全局配置。本章节用于指导如何增加媒体中继服务商相关的基础配置。

## 必备事项
前提条件

* 已完成License加载。
* 已完成框间级联部署及扩容。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_relayipinfo_list:
      type: items
      properties:
        RELAYIPNAME:
          name: '媒体中继IP地址名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该参数为媒体中继UPF与终端APP交互时使用的Relay IP名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPSERVICETYPE:
          name: 'IP业务类型'
          type: string
          enum:
          - GROUPIP
          - REDIRECTIP
          required: true
          description: '配置媒体中继Relay IP时，必须配置组级IP。'
          data_source: '固定取值'
          pattern: ''
          default: GROUPIP
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '媒体中继UPF作为DNS代理时，与终端交互使用的Relay IP地址。该地址不能与终端用户地址重复，不能与已配置的媒体中继相关IP地址重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: '媒体中继UPF作为DNS代理时，与终端交互使用的Relay IP地址。该地址不能与终端用户地址重复，不能与已配置的媒体中继相关IP地址重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该参数需要与使用媒体中继的用户VPN相同。如果存在多个，需要提供多个VPN，最多支持2个。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INSTID:
          name: '实例ID'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_relaytemplate_list:
      type: items
      properties:
        RELAYTPLNAME:
          name: '媒体中继模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSCNAME:
          name: 'DNS规范名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '该参数由OTT提供，用于配置媒体中继UPF做DNS代理时，在DNS响应中携带的CNAME名称。终端APP根据此名称识别用户为媒体中继用户。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DNSIPNOTMTACT:
          name: 'DNS IP不匹配操作'
          type: string
          enum:
          - BYPASS
          - RETNOTFOUND
          required: false
          description: '该参数用于控制双栈用户访问业务，发起DNS请求的IP类型与媒体中继IP地址类型不一致时，UPF的处理原则。'
          data_source: '本端规划'
          pattern: ''
          default: BYPASS
        UNKNOWNDMACT:
          name: 'UE访问未知域名处理动作'
          type: string
          enum:
          - REDIRECT
          - FORBIDDEN
          required: false
          description: '该参数用于控制当用户实际业务访问的域名不是媒体中继对应的域名时，UPF的处理原则。'
          data_source: '本端规划'
          pattern: ''
          default: FORBIDDEN
        VENDORID:
          name: '厂商ID'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: '该参数用于设置媒体厂商ID，用于进行差异化控制。当前可设置为0或1，0表示通用处理，1表示抖音。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        MEDIAAGETIME:
          name: '媒体文件老化时间（小时）'
          type: integer
          minimum: 1
          maximum: 720
          required: false
          description: '该参数用于设置点播资源老化时间。'
          data_source: '全网规划'
          pattern: ''
          default: 168
        MEDIAAUTHTIME:
          name: '媒体文件有效性校验时长（分钟）'
          type: integer
          minimum: 5
          maximum: 1440
          required: false
          description: '该参数用于配置UPF随业务流向CDN发起URL定时校验的间隔。'
          data_source: '全网规划'
          pattern: ''
          default: 15
        MEDIAAUTHMETHOD:
          name: '媒体文件有效性校验方式'
          type: string
          enum:
          - GET
          - HEAD
          required: false
          description: '该参数用于配置UPF随业务流向CDN发起URL定时校验的校验方式。'
          data_source: '全网规划'
          pattern: ''
          default: HEAD
        LIVESRVFAILCODE:
          name: '直播业务失败返回码'
          type: string
          enum:
          - REDIRECT
          - BADREQUEST
          - NOTFOUND
          - INTERNALSERVERERROR
          - SERVICEUNABAILABLE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: REDIRECT
        VODSRVFAILCODE:
          name: '点播业务失败返回码'
          type: string
          enum:
          - REDIRECT
          - BADREQUEST
          - NOTFOUND
          - INTERNALSERVERERROR
          - SERVICEUNABAILABLE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: REDIRECT
    add_relayipbinding_list:
      type: items
      properties:
        RELAYTPLNAME:
          name: '媒体中继模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD RELAYTEMPLATE**完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RELAYIPNAME:
          name: '媒体中继IP地址名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD RELAYIPINFO**完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_relayippoolbd_list:
      type: items
      properties:
        RELAYTPLNAME:
          name: '媒体中继模板名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD RELAYTEMPLATE**完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPPOOLNAME:
          name: 'ip地址池名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过  **ADD RELAYIPPOOL**完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_protocolgroup_list:
      type: items
      properties:
        PROTGROUPNAME:
          name: '协议组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_appperfstat_list:
      type: items
      properties:
        APPNAME:
          name: '应用名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERMODE:
          name: '过滤器模式'
          type: string
          enum:
          - PROTOCOLGROUP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTGROUPNAME:
          name: '协议组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '此参数为签约媒体中继套餐的预定义规则组，需要与PCF、SMF配置的签约套餐名称保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'Alias Marking使能标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        DDOSCHECK:
          name: '防DDOS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        LOCRPTSWITCH:
          name: '实时位置上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
  examples:
    add_relayipinfo_list:
    - RELAYIPNAME: 'sp_relay_ip_001'
      IPSERVICETYPE: GROUPIP
      IPV4ADDR: '10.100.5.100'
      IPV6ADDR: '2409:892B:A80:1000:1000:1000:1000:0001'
      VPNINSTANCE: 'VRF_Internet'
      INSTID: ''
    add_relaytemplate_list:
    - RELAYTPLNAME: 'sp_relay_tpl'
      DNSCNAME: 'www.3gpp.eupf.com'
      DNSIPNOTMTACT: RETNOTFOUND
      UNKNOWNDMACT: FORBIDDEN
      VENDORID: 1
      MEDIAAGETIME: 168
      MEDIAAUTHTIME: 5
      MEDIAAUTHMETHOD: GET
      LIVESRVFAILCODE: NOTFOUND
      VODSRVFAILCODE: SERVICEUNABAILABLE
    add_relayipbinding_list:
    - RELAYTPLNAME: 'sp_relay_tpl'
      RELAYIPNAME: 'sp_relay_ip_001'
    set_relayippoolbd_list:
    - RELAYTPLNAME: 'sp_relay_tpl'
      IPPOOLNAME: 'relay_ip_pool_cmnet'
    add_protocolgroup_list:
    - PROTGROUPNAME: 'proto_group_douyin_live'
      PROTOCOLNAME: 'tiktok_live'
    add_appperfstat_list:
    - APPNAME: 'app_douyin_live'
      FILTERMODE: PROTOCOLGROUP
      PROTGROUPNAME: 'proto_group_douyin_live'
      PRIORITY: 1001
    add_userprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      LOCRPTSWITCH: INHERIT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置Relay服务的IP地址。

```jinja2
{%- for item in add_relayipinfo_list -%}
    ADD RELAYIPINFO:
    {#- --- 必选参数 --- -#}
    RELAYIPNAME="{{item.RELAYIPNAME}}",
    IPSERVICETYPE={{item.IPSERVICETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR is not none -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {%- if item.IPV6ADDR is not none -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPSERVICETYPE=REDIRECTIP 时必选 --- -#}
    {%- if item.IPSERVICETYPE == 'REDIRECTIP' -%}
        INSTID={{item.INSTID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //配置Relay模板信息。

```jinja2
{%- for item in add_relaytemplate_list -%}
    ADD RELAYTEMPLATE:
    {#- --- 必选参数 --- -#}
    RELAYTPLNAME="{{item.RELAYTPLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DNSCNAME is not none -%}
        DNSCNAME="{{item.DNSCNAME}}",
    {%- endif -%}
    {%- if item.DNSIPNOTMTACT is not none -%}
        DNSIPNOTMTACT={{item.DNSIPNOTMTACT}},
    {%- endif -%}
    {%- if item.UNKNOWNDMACT is not none -%}
        UNKNOWNDMACT={{item.UNKNOWNDMACT}},
    {%- endif -%}
    {%- if item.VENDORID is not none -%}
        VENDORID={{item.VENDORID}},
    {%- endif -%}
    {%- if item.MEDIAAGETIME is not none -%}
        MEDIAAGETIME={{item.MEDIAAGETIME}},
    {%- endif -%}
    {%- if item.MEDIAAUTHTIME is not none -%}
        MEDIAAUTHTIME={{item.MEDIAAUTHTIME}},
    {%- endif -%}
    {%- if item.MEDIAAUTHMETHOD is not none -%}
        MEDIAAUTHMETHOD={{item.MEDIAAUTHMETHOD}},
    {%- endif -%}
    {%- if item.LIVESRVFAILCODE is not none -%}
        LIVESRVFAILCODE={{item.LIVESRVFAILCODE}},
    {%- endif -%}
    {%- if item.VODSRVFAILCODE is not none -%}
        VODSRVFAILCODE={{item.VODSRVFAILCODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置Relay服务的IP信息绑定到Relay模板下。

```jinja2
{%- for item in add_relayipbinding_list -%}
    ADD RELAYIPBINDING:
    {#- --- 必选参数 --- -#}
    RELAYTPLNAME="{{item.RELAYTPLNAME}}",
    RELAYIPNAME="{{item.RELAYIPNAME}}",
    ;
{%- endfor -%}
```

### 4 //配置Relay服务的地址池绑定到Relay模板下。

```jinja2
{%- for item in set_relayippoolbd_list -%}
    SET RELAYIPPOOLBD:
    {#- --- 必选参数 --- -#}
    RELAYTPLNAME="{{item.RELAYTPLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPPOOLNAME is not none -%}
        IPPOOLNAME="{{item.IPPOOLNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //增加基于APP观测指标。

### 开启前准备：

### 需要先将知识库版本升级到“SA signature database package V100R020C00SPH295”（01.0002.1688.01）及以上版本。

### 需要在MAE上提前下发测量对象。

```jinja2
{%- for item in add_protocolgroup_list -%}
    ADD PROTOCOLGROUP:
    {#- --- 必选参数 --- -#}
    PROTGROUPNAME="{{item.PROTGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PROTOCOLNAME is not none -%}
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_appperfstat_list -%}
    ADD APPPERFSTAT:
    {#- --- 必选参数 --- -#}
    APPNAME="{{item.APPNAME}}",
    FILTERMODE={{item.FILTERMODE}},
    PRIORITY={{item.PRIORITY}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FILTERMODE=PROTOCOLGROUP 时必选 --- -#}
    {%- if item.FILTERMODE == 'PROTOCOLGROUP' -%}
        PROTGROUPNAME="{{item.PROTGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //增加签约媒体中继套餐配置。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALIASMARKFLAG is not none -%}
        ALIASMARKFLAG={{item.ALIASMARKFLAG}},
    {%- endif -%}
    {%- if item.DDOSCHECK is not none -%}
        DDOSCHECK={{item.DDOSCHECK}},
    {%- endif -%}
    {%- if item.LOCRPTSWITCH is not none -%}
        LOCRPTSWITCH={{item.LOCRPTSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

