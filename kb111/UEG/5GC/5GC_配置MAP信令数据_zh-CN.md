---
id: ''
name: 配置MAP信令数据
ne_type: UEG
type: feature
description: 本页面用于指导操作员配置HLR（UDM）通过MAP信令与对端网元的对接数据。适用于如下场景：  * HLR（UDM）和SMSC之间通过C接口对接。 * HLR（UDM）和IP-SM-GW之间通过J接口对接。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置MAP信令数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置MAP信令数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置MAP信令数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本页面用于指导操作员配置HLR（UDM）通过MAP信令与对端网元的对接数据。适用于如下场景：* HLR（UDM）和SMSC之间通过C接口对接。* HLR（UDM）和IP-SM-GW之间通过J接口对接。

## 必备事项
前提条件

* 已完成配置UDM基础数据。
* HLR（UDM）和SMSC/IP-SM-GW之间外联口通信正常。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_m3le_list:
      type: items
      properties:
        LENM:
          name: '本地实体名称'
          type: string
          maxLength: 32
          required: true
          description: '规划多条数据时，该参数不能重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: '该参数必须先由**SET OFI**命令定义，然后在此处引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: NAT
        OPC:
          name: '本地实体信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '本端实体（如：HLR）对应的本局信令点编码。  该参数必须先由**SET OFI**命令定义，然后在此处引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - SG
          - AS
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_m3de_list:
      type: items
      properties:
        DENM:
          name: '目的实体名称'
          type: string
          maxLength: 32
          required: true
          description: '规划多条数据时，该参数不能重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LENM:
          name: '本地实体名称'
          type: string
          maxLength: 32
          required: false
          description: '该参数必须先由**ADD M3LE**命令定义，然后才能在此处引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NAT
        DPC:
          name: '目的实体信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '对接网元的信令点编码，从对端设备获取。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STPF:
          name: 'STP标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: '此处以默认值为例。'
          data_source: '本端规划'
          pattern: ''
          default: B1111
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - SP
          - SG
          - AS
          required: true
          description: '对接的目的实体类型，与对接网元类型有关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '本端实体与目的实体直联时，该参数取值为“TRUE”。'
          data_source: '固定取值'
          pattern: ''
          default: TRUE
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EXNI:
          name: '外部网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_m3lks_list:
      type: items
      properties:
        LSNM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADNM:
          name: '相邻实体名称'
          type: string
          maxLength: 32
          required: true
          description: '采用**ADD M3DE**定义的“DENM”参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: '此处以默认值为例。'
          data_source: '本端规划'
          pattern: ''
          default: B1111
        TM:
          name: '业务模式'
          type: string
          enum:
          - OVERRIDE
          - LOADSHARE
          required: false
          description: '推荐使用样例值。与对端的业务模式一致。'
          data_source: '与对端协商'
          pattern: ''
          default: LOADSHARE
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - SGP
          - IPSP
          required: true
          description: '与对端的工作模式一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_m3rt_list:
      type: items
      properties:
        RTNM:
          name: '路由名称'
          type: string
          maxLength: 32
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DENM:
          name: '目的实体名称'
          type: string
          maxLength: 32
          required: true
          description: '采用**ADD M3DE**定义的“DENM”参数值。'
          data_source: '已规划数据中索引'
          pattern: ''
          default: ''
        LSNM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: true
          description: '采用**ADD M3LKS**定义的“LSNM”参数值。'
          data_source: '已规划数据中索引'
          pattern: ''
          default: ''
    add_m3lnk_list:
      type: items
      properties:
        LNKNM:
          name: '链路名称'
          type: string
          maxLength: 32
          required: true
          description: '规划多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '用于指定本局侧分发M3UA协议消息的FE端口的IP地址类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCIPV4IP1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '用于指定本局侧分发M3UA协议消息的FE端口的地址，通过**ADD IPADDR**命令配置，在此引用。  采用表2中规划的IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCIPV4IP2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '255.255.255.255'
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: true
          description: '表示HLR侧（Client端）M3UA链路的SCTP端口号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERIPV4IP1:
          name: '对端IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '对端用于SIGTRAN协议的地址。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PEERIPV4IP2:
          name: '对端IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: '对端用于SIGTRAN协议的地址。'
          data_source: '从对端获取'
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: true
          description: '对端（Server端）M3UA链路的SCTP端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        CS:
          name: '客户端/服务器端模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: '通常将HLR侧配置成客户端，MSC侧配置为服务器端。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LSNM:
          name: '链路集名称'
          type: string
          maxLength: 32
          required: true
          description: '采用**ADD M3LKS**定义的“LSNM”参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        QOS:
          name: 'QOS值'
          type: string
          enum:
          - TOS
          - DSCP
          required: false
          description: '此处以默认值为例。'
          data_source: '全网规划'
          pattern: ''
          default: TOS
    add_sccpdsp_list:
      type: items
      properties:
        DPNM:
          name: '目的信令点名称'
          type: string
          maxLength: 32
          required: true
          description: '存在多条数据中，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '对端实体的信令点编码，从对端设备获取。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OPC:
          name: '源信令点编码'
          type: string
          maxLength: 11
          required: false
          description: '本端实体的信令点编码。  该参数必须先由**SET OFI**命令定义，然后在此处引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_sccpssn_list:
      type: items
      properties:
        SSNNM:
          name: 'SSN名称'
          type: string
          maxLength: 32
          required: true
          description: '规划多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SSN:
          name: 'SSN'
          type: string
          enum:
          - UNDEF
          - SCMG
          - RESERVED
          - ISUP
          - OMAP
          - MAP
          - HLR
          - VLR
          - MSC
          - EIR
          - AUC
          - MC
          - OTAF
          - SCP
          - GMLC
          - CAP
          - GSMSCF
          - SGSN
          - GGSN
          - MPC
          - GS
          - BSSAP/INAP
          - SSN13
          - SSN15
          - SSN16
          - SSN17
          - SSN18
          - SSN19
          - SSN20
          - SSN21
          - SSN22
          - SSN23
          - SSN24
          - SSN25
          - SSN26
          - SSN27
          - SSN28
          - SSN29
          - SSN30
          - SSN31
          - SSN32
          - SSN33
          - SSN34
          - SSN35
          - SSN36
          - SSN37
          - SSN38
          - SSN39
          - SSN40
          - SSN41
          - SSN42
          - SSN43
          - SSN44
          - SSN45
          - SSN46
          - SSN47
          - SSN48
          - SSN49
          - SSN50
          - SSN51
          - SSN52
          - SSN53
          - SSN54
          - SSN55
          - SSN56
          - SSN57
          - SSN58
          - SSN59
          - SSN60
          - SSN61
          - SSN62
          - SSN63
          - SSN64
          - SSN65
          - SSN66
          - SSN67
          - SSN68
          - SSN69
          - SSN70
          - SSN71
          - SSN72
          - SSN73
          - SSN74
          - SSN75
          - SSN76
          - SSN77
          - SSN78
          - SSN79
          - SSN80
          - SSN81
          - SSN82
          - SSN83
          - SSN84
          - SSN85
          - SSN86
          - SSN87
          - SSN88
          - SSN89
          - SSN90
          - SSN91
          - SSN92
          - SSN93
          - SSN94
          - SSN95
          - SSN96
          - SSN97
          - SSN98
          - SSN99
          - SSN100
          - SSN101
          - SSN102
          - SSN103
          - SSN104
          - SSN105
          - SSN106
          - SSN107
          - SSN108
          - SSN109
          - SSN110
          - SSN111
          - SSN112
          - SSN113
          - SSN114
          - SSN115
          - SSN116
          - SSN117
          - SSN118
          - SSN119
          - SSN120
          - SSN121
          - SSN122
          - SSN123
          - SSN124
          - SSN125
          - SSN126
          - SSN127
          - SSN128
          - SSN129
          - SSN130
          - SSN131
          - SSN132
          - SSN133
          - SSN134
          - SSN135
          - SSN136
          - SSN137
          - SSN138
          - SSN139
          - SSN140
          - SSN141
          - SSN142
          - SSN143
          - SSN144
          - SSN148
          - SSN151
          - SSN152
          - SSN153
          - SSN154
          - SSN155
          - SSN156
          - SSN157
          - SSN158
          - SSN159
          - SSN160
          - SSN161
          - SSN162
          - SSN163
          - SSN164
          - SSN165
          - SSN166
          - SSN167
          - SSN168
          - SSN169
          - SSN170
          - SSN171
          - SSN172
          - SSN173
          - SSN174
          - SSN175
          - SSN176
          - SSN177
          - SSN178
          - SSN179
          - SSN180
          - SSN181
          - SSN182
          - SSN183
          - SSN184
          - SSN185
          - SSN186
          - SSN187
          - SSN188
          - SSN189
          - SSN190
          - SSN191
          - SSN192
          - SSN193
          - SSN194
          - SSN195
          - SSN196
          - SSN197
          - SSN198
          - SSN199
          - SSN200
          - SSN201
          - SSN202
          - SSN203
          - SSN204
          - SSN205
          - SSN206
          - SSN207
          - SSN208
          - SSN209
          - SSN210
          - SSN211
          - SSN212
          - SSN213
          - SSN214
          - SSN215
          - SSN216
          - SSN217
          - SSN218
          - SSN219
          - SSN220
          - SSN221
          - SSN222
          - SSN223
          - SSN224
          - SSN225
          - SSN226
          - SSN227
          - SSN228
          - SSN229
          - SSN230
          - SSN231
          - SSN232
          - SSN233
          - SSN234
          - SSN235
          - SSN236
          - SSN237
          - SSN238
          - SSN239
          - SSN240
          - SSN241
          - SSN242
          - SSN243
          - SSN244
          - SSN245
          - SSN246
          - SSN247
          - SSN248
          - SSN249
          - SSN251
          - SSN253
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '对端：远端SCCP信令点编码。  该参数必须先由**ADD SCCPDSP**命令定义，然后才能在此处索引。  本端：本地SCCP信令点编码。  该参数必须先由**SET OFI**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OPC:
          name: '源信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '该参数就是本局信令点编码。  必须先由**SET OFI**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_sccpssn_list_2:
      type: items
      properties:
        SSNNM:
          name: 'SSN名称'
          type: string
          maxLength: 32
          required: true
          description: '规划多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SSN:
          name: 'SSN'
          type: string
          enum:
          - UNDEF
          - SCMG
          - RESERVED
          - ISUP
          - OMAP
          - MAP
          - HLR
          - VLR
          - MSC
          - EIR
          - AUC
          - MC
          - OTAF
          - SCP
          - GMLC
          - CAP
          - GSMSCF
          - SGSN
          - GGSN
          - MPC
          - GS
          - BSSAP/INAP
          - SSN13
          - SSN15
          - SSN16
          - SSN17
          - SSN18
          - SSN19
          - SSN20
          - SSN21
          - SSN22
          - SSN23
          - SSN24
          - SSN25
          - SSN26
          - SSN27
          - SSN28
          - SSN29
          - SSN30
          - SSN31
          - SSN32
          - SSN33
          - SSN34
          - SSN35
          - SSN36
          - SSN37
          - SSN38
          - SSN39
          - SSN40
          - SSN41
          - SSN42
          - SSN43
          - SSN44
          - SSN45
          - SSN46
          - SSN47
          - SSN48
          - SSN49
          - SSN50
          - SSN51
          - SSN52
          - SSN53
          - SSN54
          - SSN55
          - SSN56
          - SSN57
          - SSN58
          - SSN59
          - SSN60
          - SSN61
          - SSN62
          - SSN63
          - SSN64
          - SSN65
          - SSN66
          - SSN67
          - SSN68
          - SSN69
          - SSN70
          - SSN71
          - SSN72
          - SSN73
          - SSN74
          - SSN75
          - SSN76
          - SSN77
          - SSN78
          - SSN79
          - SSN80
          - SSN81
          - SSN82
          - SSN83
          - SSN84
          - SSN85
          - SSN86
          - SSN87
          - SSN88
          - SSN89
          - SSN90
          - SSN91
          - SSN92
          - SSN93
          - SSN94
          - SSN95
          - SSN96
          - SSN97
          - SSN98
          - SSN99
          - SSN100
          - SSN101
          - SSN102
          - SSN103
          - SSN104
          - SSN105
          - SSN106
          - SSN107
          - SSN108
          - SSN109
          - SSN110
          - SSN111
          - SSN112
          - SSN113
          - SSN114
          - SSN115
          - SSN116
          - SSN117
          - SSN118
          - SSN119
          - SSN120
          - SSN121
          - SSN122
          - SSN123
          - SSN124
          - SSN125
          - SSN126
          - SSN127
          - SSN128
          - SSN129
          - SSN130
          - SSN131
          - SSN132
          - SSN133
          - SSN134
          - SSN135
          - SSN136
          - SSN137
          - SSN138
          - SSN139
          - SSN140
          - SSN141
          - SSN142
          - SSN143
          - SSN144
          - SSN148
          - SSN151
          - SSN152
          - SSN153
          - SSN154
          - SSN155
          - SSN156
          - SSN157
          - SSN158
          - SSN159
          - SSN160
          - SSN161
          - SSN162
          - SSN163
          - SSN164
          - SSN165
          - SSN166
          - SSN167
          - SSN168
          - SSN169
          - SSN170
          - SSN171
          - SSN172
          - SSN173
          - SSN174
          - SSN175
          - SSN176
          - SSN177
          - SSN178
          - SSN179
          - SSN180
          - SSN181
          - SSN182
          - SSN183
          - SSN184
          - SSN185
          - SSN186
          - SSN187
          - SSN188
          - SSN189
          - SSN190
          - SSN191
          - SSN192
          - SSN193
          - SSN194
          - SSN195
          - SSN196
          - SSN197
          - SSN198
          - SSN199
          - SSN200
          - SSN201
          - SSN202
          - SSN203
          - SSN204
          - SSN205
          - SSN206
          - SSN207
          - SSN208
          - SSN209
          - SSN210
          - SSN211
          - SSN212
          - SSN213
          - SSN214
          - SSN215
          - SSN216
          - SSN217
          - SSN218
          - SSN219
          - SSN220
          - SSN221
          - SSN222
          - SSN223
          - SSN224
          - SSN225
          - SSN226
          - SSN227
          - SSN228
          - SSN229
          - SSN230
          - SSN231
          - SSN232
          - SSN233
          - SSN234
          - SSN235
          - SSN236
          - SSN237
          - SSN238
          - SSN239
          - SSN240
          - SSN241
          - SSN242
          - SSN243
          - SSN244
          - SSN245
          - SSN246
          - SSN247
          - SSN248
          - SSN249
          - SSN251
          - SSN253
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '对端：远端SCCP信令点编码。  该参数必须先由**ADD SCCPDSP**命令定义，然后才能在此处索引。  本端：本地SCCP信令点编码。  该参数必须先由**SET OFI**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OPC:
          name: '源信令点编码'
          type: string
          maxLength: 11
          required: true
          description: '该参数就是本局信令点编码。  必须先由**SET OFI**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_sccpgt_list:
      type: items
      properties:
        GTNM:
          name: '全局翻译码名称'
          type: string
          maxLength: 32
          required: false
          description: '规划多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NAT
        GTI:
          name: '全局翻译码类型'
          type: string
          enum:
          - GT1
          - GT2
          - GT3
          - GT4
          - GT5
          - GT6
          required: false
          description: '与运营商协商。此处以默认值为例。'
          data_source: '全网规划'
          pattern: ''
          default: GT4
        TRANTYP:
          name: '翻译类型'
          type: string
          maxLength: 2
          required: false
          description: '根据运营商要求配置。此处以默认值为例。'
          data_source: '全网规划'
          pattern: ''
          default: '00@0'
        ADDR:
          name: '全局翻译码地址信息'
          type: string
          maxLength: 20
          required: true
          description: '与运营商协商输出。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESULTT:
          name: '翻译结果类型'
          type: string
          enum:
          - STP1
          - LSPC1
          - STP2
          - LSPC2
          - STP3
          - STP4
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 11
          required: false
          description: '该参数必须先由**ADD SCCPDSP**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_sccpgt_list_1:
      type: items
      properties:
        GTNM:
          name: '全局翻译码名称'
          type: string
          maxLength: 32
          required: false
          description: '规划多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NI:
          name: '网络指示'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NAT
        GTI:
          name: '全局翻译码类型'
          type: string
          enum:
          - GT1
          - GT2
          - GT3
          - GT4
          - GT5
          - GT6
          required: false
          description: '与运营商协商。此处以默认值为例。'
          data_source: '全网规划'
          pattern: ''
          default: GT4
        TRANTYP:
          name: '翻译类型'
          type: string
          maxLength: 2
          required: false
          description: '根据运营商要求配置。此处以默认值为例。'
          data_source: '全网规划'
          pattern: ''
          default: '00@0'
        ADDR:
          name: '全局翻译码地址信息'
          type: string
          maxLength: 20
          required: true
          description: '与运营商协商输出。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESULTT:
          name: '翻译结果类型'
          type: string
          enum:
          - STP1
          - LSPC1
          - STP2
          - LSPC2
          - STP3
          - STP4
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 11
          required: false
          description: '该参数必须先由**ADD SCCPDSP**命令定义，然后才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
  examples:
    add_m3le_list:
    - LENM: 'HLR_0'
      NI: NAT
      OPC: '111111'
      LET: AS
    add_m3de_list:
    - DENM: 'M3DE_MSC3_0'
      LENM: 'HLR_0'
      NI: NAT
      DPC: '333333'
      STPF: FALSE
      SLSSM: B1111
      DET: AS
      ADJF: TRUE
      RC: 0
      EXNI: NAT
    add_m3lks_list:
    - LSNM: 'M3LKS_MSC3_0'
      ADNM: 'M3DE_MSC3_0'
      SLSM: B1111
      TM: LOADSHARE
      WM: IPSP
    add_m3rt_list:
    - RTNM: 'M3RT_MSC3_0'
      DENM: 'M3DE_MSC3_0'
      LSNM: 'M3LKS_MSC3_0'
    add_m3lnk_list:
    - LNKNM: 'M3LNK_MSC3_8'
      IPVER: IPV4
      LOCIPV4IP1: '10.200.200.98'
      LOCIPV4IP2: '10.200.200.99'
      LOCPORT: 3000
      PEERIPV4IP1: '172.16.1.94'
      PEERIPV4IP2: '172.17.1.94'
      PEERPORT: 5000
      CS: C
      LSNM: 'M3LKS_MSC3_0'
      QOS: TOS
    add_sccpdsp_list:
    - DPNM: 'SCCPDSP_MSC3_0'
      NI: NAT
      DPC: '333333'
      OPC: '111111'
    add_sccpssn_list:
    - SSNNM: 'SCCPSSN_MSC3_0'
      NI: NAT
      SSN: SCMG
      SPC: '333333'
      OPC: '111111'
    add_sccpssn_list_2:
    - SSNNM: 'SCCPSSN_HLR_0'
      NI: NAT
      SSN: SCMG
      SPC: '111111'
      OPC: '111111'
    add_sccpgt_list:
    - GTNM: 'GT_MSC3_0'
      NI: NAT
      GTI: GT4
      TRANTYP: '00'
      ADDR: 'K''8613901601234'
      RESULTT: LSPC2
      SPC: '333333'
    add_sccpgt_list_1:
    - GTNM: 'GT_HLR_0'
      NI: NAT
      GTI: GT4
      TRANTYP: '00'
      ADDR: 'K''8613902701234'
      RESULTT: LSPC2
      SPC: '111111'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 增加M3UA本地实体。

```jinja2
{%- for item in add_m3le_list -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LENM="{{item.LENM}}",
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.NI is not none -%}
        NI={{item.NI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加M3UA目的实体。

```jinja2
{%- for item in add_m3de_list -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DENM="{{item.DENM}}",
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.LENM is not none -%}
        LENM="{{item.LENM}}",
    {%- endif -%}
    {%- if item.NI is not none -%}
        NI={{item.NI}},
    {%- endif -%}
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.EXNI is not none -%}
        EXNI={{item.EXNI}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DET=AS/SG 时可选 --- -#}
    {%- if item.DET in ['AS', 'SG'] -%}
        {%- if item.ADJF is not none -%}
            ADJF={{item.ADJF}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DET=AS 时可选 --- -#}
    {%- if item.DET == 'AS' -%}
        {%- if item.RC is not none -%}
            RC={{item.RC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加M3UA链路集。

```jinja2
{%- for item in add_m3lks_list -%}
    ADD M3LKS:
    {#- --- 必选参数 --- -#}
    LSNM="{{item.LSNM}}",
    ADNM="{{item.ADNM}}",
    WM={{item.WM}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSM is not none -%}
        SLSM={{item.SLSM}},
    {%- endif -%}
    {%- if item.TM is not none -%}
        TM={{item.TM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加M3UA路由。

```jinja2
{%- for item in add_m3rt_list -%}
    ADD M3RT:
    {#- --- 必选参数 --- -#}
    DENM="{{item.DENM}}",
    LSNM="{{item.LSNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RTNM is not none -%}
        RTNM="{{item.RTNM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加M3UA链路。

```jinja2
{%- for item in add_m3lnk_list -%}
    ADD M3LNK:
    {#- --- 必选参数 --- -#}
    LNKNM="{{item.LNKNM}}",
    IPVER={{item.IPVER}},
    LOCPORT={{item.LOCPORT}},
    PEERPORT={{item.PEERPORT}},
    CS={{item.CS}},
    LSNM="{{item.LSNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QOS is not none -%}
        QOS={{item.QOS}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        LOCIPV4IP1="{{item.LOCIPV4IP1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        PEERIPV4IP1="{{item.PEERIPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.LOCIPV4IP2 is not none -%}
            LOCIPV4IP2="{{item.LOCIPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.PEERIPV4IP2 is not none -%}
            PEERIPV4IP2="{{item.PEERIPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 增加SCCP目的信令点。

```jinja2
{%- for item in add_sccpdsp_list -%}
    ADD SCCPDSP:
    {#- --- 必选参数 --- -#}
    DPNM="{{item.DPNM}}",
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OPC is not none -%}
        OPC="{{item.OPC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 增加SCCP子系统。

#### 8.1 增加远端子系统。

```jinja2
{%- for item in add_sccpssn_list -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNNM="{{item.SSNNM}}",
    NI={{item.NI}},
    SSN={{item.SSN}},
    SPC="{{item.SPC}}",
    OPC="{{item.OPC}}",
    ;
{%- endfor -%}
```

#### 8.2 增加本地子系统。

```jinja2
{%- for item in add_sccpssn_list_2 -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNNM="{{item.SSNNM}}",
    NI={{item.NI}},
    SSN={{item.SSN}},
    SPC="{{item.SPC}}",
    OPC="{{item.OPC}}",
    ;
{%- endfor -%}
```

#### 直联组网情况下，需要为每个目的信令点增加SCMG子系统。

#### 本地还需要配置MSC子系统和HLR子系统。

#### 远端还需要配置HLR子系统。

### 9 增加SCCP全局翻译码。

#### 9.1 增加对端实体的全局翻译码。

```jinja2
{%- for item in add_sccpgt_list -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    ADDR=K'{{item.ADDR}},
    RESULTT={{item.RESULTT}},
    {#- --- 可选参数 --- -#}
    {%- if item.GTNM is not none -%}
        GTNM="{{item.GTNM}}",
    {%- endif -%}
    {%- if item.NI is not none -%}
        NI={{item.NI}},
    {%- endif -%}
    {%- if item.GTI is not none -%}
        GTI={{item.GTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RESULTT=STP1/LSPC1/STP2/LSPC2 时必选 --- -#}
    {%- if item.RESULTT in ['STP1', 'LSPC1', 'STP2', 'LSPC2'] -%}
        SPC="{{item.SPC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTI=GT2/GT3/GT4/GT5/GT6 时可选 --- -#}
    {%- if item.GTI in ['GT2', 'GT3', 'GT4', 'GT5', 'GT6'] -%}
        {%- if item.TRANTYP is not none -%}
            TRANTYP="{{item.TRANTYP}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.2 增加本端实体的全局翻译码。

```jinja2
{%- for item in add_sccpgt_list_1 -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    ADDR=K'{{item.ADDR}},
    RESULTT={{item.RESULTT}},
    {#- --- 可选参数 --- -#}
    {%- if item.GTNM is not none -%}
        GTNM="{{item.GTNM}}",
    {%- endif -%}
    {%- if item.NI is not none -%}
        NI={{item.NI}},
    {%- endif -%}
    {%- if item.GTI is not none -%}
        GTI={{item.GTI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RESULTT=STP1/LSPC1/STP2/LSPC2 时必选 --- -#}
    {%- if item.RESULTT in ['STP1', 'LSPC1', 'STP2', 'LSPC2'] -%}
        SPC="{{item.SPC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTI=GT2/GT3/GT4/GT5/GT6 时可选 --- -#}
    {%- if item.GTI in ['GT2', 'GT3', 'GT4', 'GT5', 'GT6'] -%}
        {%- if item.TRANTYP is not none -%}
            TRANTYP="{{item.TRANTYP}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

