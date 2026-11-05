---
id: ''
name: 配置直播业务的安全认证策略
ne_type: UDG
type: feature
description: 在媒体中继业务中，媒体中继UPF使用HTTPS方式进行通信时，在不同场景下分别承担着不同的角色。在和终端APP通信时，媒体中继UPF作为服务端，而当和CDN进行通信时，媒体中继UPF则作为客户端。  本章节主要介绍针对直播业务，媒体中继UPF使用HTTPS方式进行通信时，如何配置TLS证书作为业务的安全认证策略。  适用于UPF。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体服务商配置（基于OTT应用）","配置直播业务的安全认证策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在媒体中继业务中，媒体中继UPF使用HTTPS方式进行通信时，在不同场景下分别承担着不同的角色。在和终端APP通信时，媒体中继UPF作为服务端，而当和CDN进行通信时，媒体中继UPF则作为客户端。本章节主要介绍针对直播业务，媒体中继UPF使用HTTPS方式进行通信时，如何配置TLS证书作为业务的安全认证策略。适用于UPF。

## 必备事项
前提条件

已获取证书：商用证书，由客户申请。
已参考配置直播业务的媒体中继域名（直播域名）完成媒体中继域名配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_srvcertscene_list:
      type: items
      properties:
        SCENE:
          name: '证书使用场景名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '场景类型'
          type: string
          enum:
          - SCENE_CA
          - SCENE_NE
          required: true
          description: '-'
          data_source: '固定取值   * 设备证书固定取值为SCENE\_NE。 * CA证书固定取值SCENE\_CA。'
          pattern: ''
          default: ''
        CNDESC:
          name: '证书使用场景中文描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_srvtlsply_list:
      type: items
      properties:
        PLYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '* relay\_tls\_s\_sp\_live\_001：本端实体作为服务端时的策略名称。relay\_tls\_c\_sp\_live\_001：本端实体作为客户端时的策略名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '实体类型'
          type: string
          enum:
          - CLIENT
          - SERVER
          required: true
          description: '* “Client（客户端）”：本端实体作为Client。和终端APP通信，媒体中继UPF作为服务器端，终端APP作为客户端。 * “Server（服务端）”：本端实体作为Server。 和CDN通信，UPF作为客户端，CDN作为服务器端。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议版本'
          type: string
          required: true
          description: '* “TLS1\_2（传输层安全性协议版本v1.2）”：TLS1\_2表示使用传输层安全性协议版本v1.2。 * “TLS1\_3（传输层安全性协议版本v1.3）”：TLS1\_3表示使用传输层安全性协议版本v1.3。 * 如果只配一条，需要和对端协议版本保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIPHER:
          name: '加密套件集合'
          type: string
          required: true
          description: '* "PROTOCOL"参数选中TLS1\_2，"CIPHER"选中的算法必须有TLS1\_2支持的算法，否则命令会执行失败； * "PROTOCOL"参数选中TLS1\_3，"CIPHER"未选中TLS1\_3的算法命令不会执行失败，系统会使用默认的TLS1\_3算法； * TLS1\_2选中TLS1\_3的算法不生效，同样TLS1\_3选中TLS1\_2的算法也不会生效。 * 算法需要和对端协议版本保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '与ADD SRVCERTSCENE命令中配置的设备证书场景的“SCENE”参数值保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '与ADD SRVCERTSCENE命令中配置的CA证书场景的“SCENE”参数值保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '验证对端证书'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '* Yes：开启校验对端证书。 * No：关闭校验对端证书。当参数设置为“No”时，不校验对端证书合法性，存在安全风险。'
          data_source: '本端规划'
          pattern: ''
          default: YES
        CRLFLAG:
          name: '吊销证书列表'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: '* CRL\_OFF：关闭吊销证书列表。 * CRL\_ON：开启吊销证书列表。 * 若启用CRL，即吊销证书列表，则需上传CRL文件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VDEPTH:
          name: '验证对端证书'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: '系统默认100。'
          data_source: '本端规划'
          pattern: ''
          default: 100
    add_srvtlsply_list_1:
      type: items
      properties:
        PLYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '* relay\_tls\_s\_sp\_live\_001：本端实体作为服务端时的策略名称。relay\_tls\_c\_sp\_live\_001：本端实体作为客户端时的策略名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TYPE:
          name: '实体类型'
          type: string
          enum:
          - CLIENT
          - SERVER
          required: true
          description: '* “Client（客户端）”：本端实体作为Client。和终端APP通信，媒体中继UPF作为服务器端，终端APP作为客户端。 * “Server（服务端）”：本端实体作为Server。 和CDN通信，UPF作为客户端，CDN作为服务器端。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议版本'
          type: string
          required: true
          description: '* “TLS1\_2（传输层安全性协议版本v1.2）”：TLS1\_2表示使用传输层安全性协议版本v1.2。 * “TLS1\_3（传输层安全性协议版本v1.3）”：TLS1\_3表示使用传输层安全性协议版本v1.3。 * 如果只配一条，需要和对端协议版本保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIPHER:
          name: '加密套件集合'
          type: string
          required: true
          description: '* "PROTOCOL"参数选中TLS1\_2，"CIPHER"选中的算法必须有TLS1\_2支持的算法，否则命令会执行失败； * "PROTOCOL"参数选中TLS1\_3，"CIPHER"未选中TLS1\_3的算法命令不会执行失败，系统会使用默认的TLS1\_3算法； * TLS1\_2选中TLS1\_3的算法不生效，同样TLS1\_3选中TLS1\_2的算法也不会生效。 * 算法需要和对端协议版本保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '与ADD SRVCERTSCENE命令中配置的设备证书场景的“SCENE”参数值保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '与ADD SRVCERTSCENE命令中配置的CA证书场景的“SCENE”参数值保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '验证对端证书'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '* Yes：开启校验对端证书。 * No：关闭校验对端证书。当参数设置为“No”时，不校验对端证书合法性，存在安全风险。'
          data_source: '本端规划'
          pattern: ''
          default: YES
        CRLFLAG:
          name: '吊销证书列表'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: '* CRL\_OFF：关闭吊销证书列表。 * CRL\_ON：开启吊销证书列表。 * 若启用CRL，即吊销证书列表，则需上传CRL文件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VDEPTH:
          name: '验证对端证书'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: '系统默认100。'
          data_source: '本端规划'
          pattern: ''
          default: 100
    add_relaytlscfg_list:
      type: items
      properties:
        TLSCONFIGNAME:
          name: 'TLS配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UETLSPLYNAME:
          name: '与UE认证策略'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '* 该参数来源于ADD SRVTLSPLY命令的“PLYNM”参数，可通过LST SRVTLSPLY命令查询获取。  * 该参数用于指定Relay作为服务端与UE客户端使用HTTPS方式连接时使用的TLS认证策略名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CDNTLSPLYNAME:
          name: '与CDN认证策略'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '* 该参数来源于ADD SRVTLSPLY命令的“PLYNM”参数，可通过LST SRVTLSPLY命令查询获取。 * 该参数用于指定Relay作为客户端与CDN服务端使用HTTPS方式连接时使用的TLS认证策略名称。 * Relay与CDN之间使用HTTPS时必须配置否则TLS协商失败。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_relaydomain_list:
      type: items
      properties:
        RELAYDOMAINNAME:
          name: '媒体中继域名配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过ADD RELAYTEMPLATE完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TLSCFGNAME:
          name: 'TLS配置名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_srvcertscene_list:
    - SCENE: 'relay_sc_ne_sp_live_001'
      TYPE: SCENE_NE
      CNDESC: 'Relay_NE'
    add_srvtlsply_list:
    - PLYNAME: 'relay_tls_s_sp_live_001'
      TYPE: SERVER
      PROTOCOL: TLS1_2-1&TLS1_3-1
      CIPHER: TLS_DHE_RSA_WITH_AES128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES128_CCM-1&TLS_DHE_RSA_WITH_AES256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES256_CCM-1&TLS_AES128_GCM_SHA256-1&TLS_AES256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_AES_128_CCM_SHA256-1
      NESCENE: 'relay_sc_ne_sp_live_001'
      CASCENE: 'relay_sc_ca_sp_live_001'
      VERIFYPEER: Yes
      CRLFLAG: CRL_ON
      VDEPTH: 100
    add_srvtlsply_list_1:
    - PLYNAME: 'relay_tls_c_sp_live_001'
      TYPE: Client
      PROTOCOL: TLS1_2-1&TLS1_3-1
      CIPHER: TLS_DHE_RSA_WITH_AES128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES128_CCM-1&TLS_DHE_RSA_WITH_AES256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES256_CCM-1&TLS_AES128_GCM_SHA256-1&TLS_AES256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_AES_128_CCM_SHA256-1
      NESCENE: 'relay_sc_ne_sp_live_001'
      CASCENE: 'relay_sc_ca_sp_live_001'
      VERIFYPEER: Yes
      CRLFLAG: CRL_ON
      VDEPTH: 100
    add_relaytlscfg_list:
    - TLSCONFIGNAME: 'relay_tls_cfg_sp_live_001'
      UETLSPLYNAME: 'relay_tls_s_sp_live_001'
      CDNTLSPLYNAME: 'relay_tls_c_sp_live_001'
    mod_relaydomain_list:
    - RELAYDOMAINNAME: 'sp_relay_dm_live_001'
      TLSCFGNAME: 'relay_tls_cfg_sp_live_001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //增加UPF的TLS证书场景。

```jinja2
{%- for item in add_srvcertscene_list -%}
    ADD SRVCERTSCENE:
    {#- --- 必选参数 --- -#}
    SCENE="{{item.SCENE}}",
    TYPE={{item.TYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CNDESC is not none -%}
        CNDESC="{{item.CNDESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //增加UPF作为服务器端的TLS认证策略配置。即UPF作为服务器端，UE作为客户端。

```jinja2
{%- for item in add_srvtlsply_list -%}
    ADD SRVTLSPLY:
    {#- --- 必选参数 --- -#}
    PLYNAME="{{item.PLYNAME}}",
    TYPE={{item.TYPE}},
    PROTOCOL={{item.PROTOCOL}},
    CIPHER={{item.CIPHER}},
    {#- --- 可选参数 --- -#}
    {%- if item.VERIFYPEER is not none -%}
        VERIFYPEER={{item.VERIFYPEER}},
    {%- endif -%}
    {%- if item.CRLFLAG is not none -%}
        CRLFLAG={{item.CRLFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TYPE=SERVER/CLIENT 时可选 --- -#}
    {%- if item.TYPE in ['SERVER', 'CLIENT'] -%}
        {%- if item.CASCENE is not none -%}
            CASCENE="{{item.CASCENE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFYPEER=YES 时可选 --- -#}
    {%- if item.VERIFYPEER == 'YES' -%}
        {%- if item.VDEPTH is not none -%}
            VDEPTH={{item.VDEPTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 设备证书场景: 条件必选(实体类型=SERVER) / 条件可选(实体类型=CLIENT) --- -#}
    {%- if (item.TYPE == 'SERVER') -%}
        NESCENE="{{item.NESCENE}}",
    {%- elif (item.TYPE == 'CLIENT') -%}
        {%- if item.NESCENE is not none -%}
            NESCENE="{{item.NESCENE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //增加UPF作为客户端的TLS认证策略配置。即UPF作为客户端，CDN作为服务器端。

```jinja2
{%- for item in add_srvtlsply_list_1 -%}
    ADD SRVTLSPLY:
    {#- --- 必选参数 --- -#}
    PLYNAME="{{item.PLYNAME}}",
    TYPE={{item.TYPE}},
    PROTOCOL={{item.PROTOCOL}},
    CIPHER={{item.CIPHER}},
    {#- --- 可选参数 --- -#}
    {%- if item.VERIFYPEER is not none -%}
        VERIFYPEER={{item.VERIFYPEER}},
    {%- endif -%}
    {%- if item.CRLFLAG is not none -%}
        CRLFLAG={{item.CRLFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TYPE=SERVER/CLIENT 时可选 --- -#}
    {%- if item.TYPE in ['SERVER', 'CLIENT'] -%}
        {%- if item.CASCENE is not none -%}
            CASCENE="{{item.CASCENE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFYPEER=YES 时可选 --- -#}
    {%- if item.VERIFYPEER == 'YES' -%}
        {%- if item.VDEPTH is not none -%}
            VDEPTH={{item.VDEPTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 设备证书场景: 条件必选(实体类型=SERVER) / 条件可选(实体类型=CLIENT) --- -#}
    {%- if (item.TYPE == 'SERVER') -%}
        NESCENE="{{item.NESCENE}}",
    {%- elif (item.TYPE == 'CLIENT') -%}
        {%- if item.NESCENE is not none -%}
            NESCENE="{{item.NESCENE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置媒体中继业务绑定TLS策略配置。

```jinja2
{%- for item in add_relaytlscfg_list -%}
    ADD RELAYTLSCFG:
    {#- --- 必选参数 --- -#}
    TLSCONFIGNAME="{{item.TLSCONFIGNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UETLSPLYNAME is not none -%}
        UETLSPLYNAME="{{item.UETLSPLYNAME}}",
    {%- endif -%}
    {%- if item.CDNTLSPLYNAME is not none -%}
        CDNTLSPLYNAME="{{item.CDNTLSPLYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //安全认证策略绑定到媒体中继模板。

```jinja2
{%- for item in mod_relaydomain_list -%}
    MOD RELAYDOMAIN:
    {#- --- 必选参数 --- -#}
    RELAYDOMAINNAME="{{item.RELAYDOMAINNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TLSCFGNAME is not none -%}
        TLSCFGNAME="{{item.TLSCFGNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

