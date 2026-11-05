---
id: ''
name: 配置BGP安全
ne_type: UNC
type: feature
description: 网络上对BGP协议的攻击方法主要有DoS攻击、注入大量BGP路由、构造错误BGP协议报文、网络报文攻击，为了提升安全性，需要进行BGP的安全加固配置。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网络上对BGP协议的攻击方法主要有DoS攻击、注入大量BGP路由、构造错误BGP协议报文、网络报文攻击，为了提升安全性，需要进行BGP的安全加固配置。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_bgppeer_list:
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
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDTYPE:
          name: '密码类型'
          type: string
          enum:
          - cipher
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDCIPHERTEXT:
          name: '密码'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeer_list_1:
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
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYCHAINNAME:
          name: 'Keychain名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeer_list_2:
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
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALIDTTLHOPS:
          name: '需要检测的TTL跳数值'
          type: integer
          minimum: 1
          maximum: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeeraf_list:
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
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv4vpn
          - ipv6uni
          - ipv6vpn
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMIT:
          name: '路由超限阈值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDPATHMODE:
          name: 'add-path模式'
          type: string
          enum:
          - both
          - 'null'
          - receive
          - send
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVADDPATHNUM:
          name: '向邻居发布多少条add-path路由'
          type: integer
          minimum:
          - 0
          - 2
          maximum:
          - 0
          - 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVBESTEXTERNAL:
          name: '是否发布bestExternal路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVERTISECOMMUNITY:
          name: '团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADVERTISEEXTCOMMUNITY:
          name: '扩展团体属性发布'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPENABLE:
          name: '允许AS号重复'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALLOWASLOOPLIMIT:
          name: '允许AS号重复数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVENABLE:
          name: '允许缺省路由通告'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTADVPOLICY:
          name: '缺省路由通告策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRTMATCHMODE:
          name: '带条件匹配缺省路由发布'
          type: string
          enum:
          - matchall
          - matchany
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCARDEXTCOMMUNITY:
          name: '扩展团体属性丢弃'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACL6NAMEORNUM:
          name: '发布路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTACLNAMEORNUM:
          name: '发布路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTASPATHFILTER:
          name: '发布路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREF6FILTNAME:
          name: '发布IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTPREFFILTNAME:
          name: '发布前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPORTRTPOLICYNAME:
          name: '发布路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACL6NAMEORNUM:
          name: '接收路由ACL6规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTACLNAMEORNUM:
          name: '接收路由ACL规则标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTASPATHFILTER:
          name: '接收路由AS Path过滤'
          type: string
          maxLength: 51
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREF6FILTNAME:
          name: '引入IPv6前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPREFFILTNAME:
          name: '引入前缀过滤策略'
          type: string
          maxLength: 169
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTRTPOLICYNAME:
          name: '引入路由策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INCLUDEPEERAS:
          name: '不忽略BGP邻居的AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSOURELAYNEIGHINTER:
          name: '迭代多源邻居源接口'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALLROUTES:
          name: '全局路由更新保存'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOPCONFIGURE:
          name: '下一跳处理模式'
          type: string
          enum:
          - invariable
          - local
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERGROUPNAME:
          name: '所属对等体组名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERREDVALUE:
          name: '路由首选值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLY:
          name: '仅携带公有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYFORCE:
          name: '强制删除私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYLIMITED:
          name: '删除左边的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PUBLICASONLYREPLACE:
          name: '用本地AS号替换所有的私有AS号'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REFLECTCLIENT:
          name: '路由反射器客户'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITIDLETIMEOUT:
          name: '超时定时器（min）'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITPERCENT:
          name: '路由超限百分比'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMITTYPE:
          name: '路由超限告警类型'
          type: string
          enum:
          - alertOnly
          - idleForever
          - idleTimeout
          - noparameter
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RTUPDTINTERVAL:
          name: '路由更新时间（s）'
          type: integer
          minimum: 0
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSTITUTEASENABLE:
          name: '替换AS Path属性'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_bgppeer_list:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      PSWDTYPE: 密码类型
      PSWDCIPHERTEXT: '密码'
      ADDRESSTYPE: ''
    mod_bgppeer_list_1:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      KEYCHAINNAME: 'Keychain名称'
      ADDRESSTYPE: ''
    mod_bgppeer_list_2:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      VALIDTTLHOPS: 指定需要检测的TTL跳数值
      ADDRESSTYPE: ''
    mod_bgppeeraf_list:
    - VRFNAME: 'VPN实例名称'
      AFTYPE: 地址族类型
      REMOTEADDRESS: 'IPv4对等体地址'
      ROUTELIMIT: 路由超限阈值
      ADDRESSTYPE: ''
      ADDPATHMODE: ''
      ADVADDPATHNUM: ''
      ADVBESTEXTERNAL: ''
      ADVERTISECOMMUNITY: ''
      ADVERTISEEXTCOMMUNITY: ''
      ALLOWASLOOPENABLE: ''
      ALLOWASLOOPLIMIT: ''
      DEFAULTRTADVENABLE: ''
      DEFAULTRTADVPOLICY: ''
      DEFAULTRTMATCHMODE: ''
      DISCARDEXTCOMMUNITY: ''
      EXPORTACL6NAMEORNUM: ''
      EXPORTACLNAMEORNUM: ''
      EXPORTASPATHFILTER: ''
      EXPORTPREF6FILTNAME: ''
      EXPORTPREFFILTNAME: ''
      EXPORTRTPOLICYNAME: ''
      IMPORTACL6NAMEORNUM: ''
      IMPORTACLNAMEORNUM: ''
      IMPORTASPATHFILTER: ''
      IMPORTPREF6FILTNAME: ''
      IMPORTPREFFILTNAME: ''
      IMPORTRTPOLICYNAME: ''
      INCLUDEPEERAS: ''
      ISSOURELAYNEIGHINTER: ''
      KEEPALLROUTES: ''
      NEXTHOPCONFIGURE: ''
      PEERGROUPNAME: ''
      PREFERREDVALUE: ''
      PUBLICASONLY: ''
      PUBLICASONLYFORCE: ''
      PUBLICASONLYLIMITED: ''
      PUBLICASONLYREPLACE: ''
      REFLECTCLIENT: ''
      ROUTELIMITIDLETIMEOUT: ''
      ROUTELIMITPERCENT: ''
      ROUTELIMITTYPE: ''
      RTUPDTINTERVAL: ''
      SUBSTITUTEASENABLE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置MD5认证

### BGP的MD5认证只是为TCP连接设置MD5认证密码，由TCP完成认证。如果认证失败，则不建立TCP连接。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.PSWDTYPE is not none -%}
            PSWDTYPE={{item.PSWDTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PSWDTYPE=cipher 时可选 --- -#}
    {%- if item.PSWDTYPE == 'cipher' -%}
        {%- if item.PSWDCIPHERTEXT is not none -%}
            PSWDCIPHERTEXT="{{item.PSWDCIPHERTEXT}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 为了保证更好的安全性，建议不要使用MD5算法。

### 2 配置Keychain认证

### BGP对等体两端必须都配置Keychain认证，且配置的Keychain必须使用相同的加密算法和密码，才能正常建立TCP连接，交互BGP消息。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list_1 -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.KEYCHAINNAME is not none -%}
            KEYCHAINNAME="{{item.KEYCHAINNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置BGP GTSM功能

### 配置GTSM功能，通过检测IP报文头中的TTL值是否在一个预先定义好的特定范围内来对设备进行保护。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list_2 -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRESSTYPE is not none -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.VALIDTTLHOPS is not none -%}
            VALIDTTLHOPS={{item.VALIDTTLHOPS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置BGP路由超限

### BGP使用邻居路由限定为一个BGP路由器设置允许从其对等体收到的最大路由数量，超限路由被直接丢弃。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in mod_bgppeeraf_list -%}
    MOD BGPPEERAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv4' -%}
        REMOTEADDRESS="{{item.REMOTEADDRESS}}",
    {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        REMOTEADDRESS="{{item.REMOTEADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
    {%- if item.AFTYPE == 'ipv6uni' -%}
        ADDRESSTYPE={{item.ADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ROUTELIMIT is not none -%}
            ROUTELIMIT={{item.ROUTELIMIT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ROUTELIMIT is not none -%}
            ROUTELIMIT={{item.ROUTELIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ADDPATHMODE is not none -%}
            ADDPATHMODE={{item.ADDPATHMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ADVADDPATHNUM is not none -%}
            ADVADDPATHNUM={{item.ADVADDPATHNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ADVBESTEXTERNAL is not none -%}
            ADVBESTEXTERNAL={{item.ADVBESTEXTERNAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ADVERTISECOMMUNITY is not none -%}
            ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ADVERTISECOMMUNITY is not none -%}
            ADVERTISECOMMUNITY={{item.ADVERTISECOMMUNITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
            ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.ADVERTISEEXTCOMMUNITY is not none -%}
            ADVERTISEEXTCOMMUNITY={{item.ADVERTISEEXTCOMMUNITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ALLOWASLOOPENABLE is not none -%}
            ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ALLOWASLOOPENABLE is not none -%}
            ALLOWASLOOPENABLE={{item.ALLOWASLOOPENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ALLOWASLOOPLIMIT is not none -%}
            ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ALLOWASLOOPLIMIT is not none -%}
            ALLOWASLOOPLIMIT={{item.ALLOWASLOOPLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.DEFAULTRTADVENABLE is not none -%}
            DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.DEFAULTRTADVENABLE is not none -%}
            DEFAULTRTADVENABLE={{item.DEFAULTRTADVENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.DEFAULTRTADVPOLICY is not none -%}
            DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.DEFAULTRTADVPOLICY is not none -%}
            DEFAULTRTADVPOLICY="{{item.DEFAULTRTADVPOLICY}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.DEFAULTRTMATCHMODE is not none -%}
            DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.DEFAULTRTMATCHMODE is not none -%}
            DEFAULTRTMATCHMODE={{item.DEFAULTRTMATCHMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.DISCARDEXTCOMMUNITY is not none -%}
            DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.DISCARDEXTCOMMUNITY is not none -%}
            DISCARDEXTCOMMUNITY={{item.DISCARDEXTCOMMUNITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.EXPORTACL6NAMEORNUM is not none -%}
            EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv6vpn' -%}
        {%- if item.EXPORTACL6NAMEORNUM is not none -%}
            EXPORTACL6NAMEORNUM="{{item.EXPORTACL6NAMEORNUM}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
        {%- if item.EXPORTACLNAMEORNUM is not none -%}
            EXPORTACLNAMEORNUM="{{item.EXPORTACLNAMEORNUM}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.EXPORTASPATHFILTER is not none -%}
            EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.EXPORTASPATHFILTER is not none -%}
            EXPORTASPATHFILTER="{{item.EXPORTASPATHFILTER}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.EXPORTPREF6FILTNAME is not none -%}
            EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv6vpn' -%}
        {%- if item.EXPORTPREF6FILTNAME is not none -%}
            EXPORTPREF6FILTNAME="{{item.EXPORTPREF6FILTNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
        {%- if item.EXPORTPREFFILTNAME is not none -%}
            EXPORTPREFFILTNAME="{{item.EXPORTPREFFILTNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.EXPORTRTPOLICYNAME is not none -%}
            EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.EXPORTRTPOLICYNAME is not none -%}
            EXPORTRTPOLICYNAME="{{item.EXPORTRTPOLICYNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.IMPORTACL6NAMEORNUM is not none -%}
            IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv6vpn' -%}
        {%- if item.IMPORTACL6NAMEORNUM is not none -%}
            IMPORTACL6NAMEORNUM="{{item.IMPORTACL6NAMEORNUM}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
        {%- if item.IMPORTACLNAMEORNUM is not none -%}
            IMPORTACLNAMEORNUM="{{item.IMPORTACLNAMEORNUM}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.IMPORTASPATHFILTER is not none -%}
            IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.IMPORTASPATHFILTER is not none -%}
            IMPORTASPATHFILTER="{{item.IMPORTASPATHFILTER}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.IMPORTPREF6FILTNAME is not none -%}
            IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv6vpn' -%}
        {%- if item.IMPORTPREF6FILTNAME is not none -%}
            IMPORTPREF6FILTNAME="{{item.IMPORTPREF6FILTNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn 时可选 --- -#}
    {%- if item.AFTYPE in ['ipv4uni', 'ipv4vpn'] -%}
        {%- if item.IMPORTPREFFILTNAME is not none -%}
            IMPORTPREFFILTNAME="{{item.IMPORTPREFFILTNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.IMPORTRTPOLICYNAME is not none -%}
            IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.IMPORTRTPOLICYNAME is not none -%}
            IMPORTRTPOLICYNAME="{{item.IMPORTRTPOLICYNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.INCLUDEPEERAS is not none -%}
            INCLUDEPEERAS={{item.INCLUDEPEERAS}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.INCLUDEPEERAS is not none -%}
            INCLUDEPEERAS={{item.INCLUDEPEERAS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv4' -%}
        {%- if item.ISSOURELAYNEIGHINTER is not none -%}
            ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.ISSOURELAYNEIGHINTER is not none -%}
            ISSOURELAYNEIGHINTER={{item.ISSOURELAYNEIGHINTER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.KEEPALLROUTES is not none -%}
            KEEPALLROUTES={{item.KEEPALLROUTES}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.KEEPALLROUTES is not none -%}
            KEEPALLROUTES={{item.KEEPALLROUTES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.NEXTHOPCONFIGURE is not none -%}
            NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.NEXTHOPCONFIGURE is not none -%}
            NEXTHOPCONFIGURE={{item.NEXTHOPCONFIGURE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PEERGROUPNAME is not none -%}
            PEERGROUPNAME="{{item.PEERGROUPNAME}}",
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PEERGROUPNAME is not none -%}
            PEERGROUPNAME="{{item.PEERGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PREFERREDVALUE is not none -%}
            PREFERREDVALUE={{item.PREFERREDVALUE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PREFERREDVALUE is not none -%}
            PREFERREDVALUE={{item.PREFERREDVALUE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PUBLICASONLY is not none -%}
            PUBLICASONLY={{item.PUBLICASONLY}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PUBLICASONLY is not none -%}
            PUBLICASONLY={{item.PUBLICASONLY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PUBLICASONLYFORCE is not none -%}
            PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PUBLICASONLYFORCE is not none -%}
            PUBLICASONLYFORCE={{item.PUBLICASONLYFORCE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PUBLICASONLYLIMITED is not none -%}
            PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PUBLICASONLYLIMITED is not none -%}
            PUBLICASONLYLIMITED={{item.PUBLICASONLYLIMITED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.PUBLICASONLYREPLACE is not none -%}
            PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.PUBLICASONLYREPLACE is not none -%}
            PUBLICASONLYREPLACE={{item.PUBLICASONLYREPLACE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.REFLECTCLIENT is not none -%}
            REFLECTCLIENT={{item.REFLECTCLIENT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.REFLECTCLIENT is not none -%}
            REFLECTCLIENT={{item.REFLECTCLIENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
            ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ROUTELIMITIDLETIMEOUT is not none -%}
            ROUTELIMITIDLETIMEOUT={{item.ROUTELIMITIDLETIMEOUT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ROUTELIMITPERCENT is not none -%}
            ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ROUTELIMITPERCENT is not none -%}
            ROUTELIMITPERCENT={{item.ROUTELIMITPERCENT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ROUTELIMITTYPE is not none -%}
            ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ROUTELIMITTYPE is not none -%}
            ROUTELIMITTYPE={{item.ROUTELIMITTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.RTUPDTINTERVAL is not none -%}
            RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni 时可选 --- -#}
    {%- elif item.AFTYPE == 'ipv4uni' -%}
        {%- if item.RTUPDTINTERVAL is not none -%}
            RTUPDTINTERVAL={{item.RTUPDTINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ADDRESSTYPE=ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv6' -%}
        {%- if item.SUBSTITUTEASENABLE is not none -%}
            SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.SUBSTITUTEASENABLE is not none -%}
            SUBSTITUTEASENABLE={{item.SUBSTITUTEASENABLE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

