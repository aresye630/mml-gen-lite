---
id: ''
name: 配置话单字段（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: 对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，GGSN/SGW-C/PGW-C支持自定义配置是否携带该字段，运营商可根据需要选择配置。  话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。  GGSN/SGW-C/PGW-C支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。  * 适用于SGW-C、PGW-C、GGSN。 * 系统升级时，需注意先升级CG，再升级GGSN/SGW-C/PGW-C，以防止GGSN/SGW-C/PGW-C先升级后话单中有CG不识别的字段。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置话单字段（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，GGSN/SGW-C/PGW-C支持自定义配置是否携带该字段，运营商可根据需要选择配置。话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。GGSN/SGW-C/PGW-C支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。* 适用于SGW-C、PGW-C、GGSN。* 系统升级时，需注意先升级CG，再升级GGSN/SGW-C/PGW-C，以防止GGSN/SGW-C/PGW-C先升级后话单中有CG不识别的字段。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '话单字段模板名'
          type: string
          maxLength: 63
          required: true
          description: '配置单字段模板，控制话单中是否携带对应字段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNETWORKID:
          name: 'apn-network-identifier'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含APN网络节点标识信息，默认值是**ENABLE**。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        MSTIMEZONE:
          name: 'ms-time-zone'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带ms-time-zone字段，默认值是**ENABLE**。'
          data_source: '与对端协商'
          pattern: ''
          default: ENABLE
        ULI:
          name: 'user-location-information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        RECORDEXTENTION:
          name: 'record-extensions开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RECORDEXTTYPE:
          name: '运营商record-extensions'
          type: string
          enum:
          - CCB
          - CMHK
          - COMM
          - DT
          - GLB
          - HP
          - TAG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CCB
        ULIWLAN:
          name: 'ULI携带WLAN地址信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_glbcdrfldtemp_list:
      type: items
      properties:
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: '配置全局绑定话单字段模板'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN，可以使用命令**LST APN**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '为APN实例绑定话单字段模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_cdrfieldtemp_list:
    - TEMPLATENAME: 'cdrfield-test'
      APNNETWORKID: DISABLE
      MSTIMEZONE: DISABLE
      ULI: ENABLE
      RECORDEXTENTION: DISABLE
      RECORDEXTTYPE: CCB
      ULIWLAN: DISABLE
    set_glbcdrfldtemp_list:
    - PGWCDRTEMPLATE: 'cdrfield-test'
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      PGWCDRTEMPLATE: 'cdrfield-test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置话单字段。

### GGSN/SGW-C/PGW-C默认携带话单可选字段，如果不需要携带某个字段，将对应字段设置为**DISABLE**。

```jinja2
{%- for item in add_cdrfieldtemp_list -%}
    ADD CDRFIELDTEMP:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APNNETWORKID is not none -%}
        APNNETWORKID={{item.APNNETWORKID}},
    {%- endif -%}
    {%- if item.MSTIMEZONE is not none -%}
        MSTIMEZONE={{item.MSTIMEZONE}},
    {%- endif -%}
    {%- if item.ULI is not none -%}
        ULI={{item.ULI}},
    {%- endif -%}
    {%- if item.RECORDEXTENTION is not none -%}
        RECORDEXTENTION={{item.RECORDEXTENTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RECORDEXTENTION=ENABLE 时必选 --- -#}
    {%- if item.RECORDEXTENTION == 'ENABLE' -%}
        RECORDEXTTYPE={{item.RECORDEXTTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ULI=ENABLE 时可选 --- -#}
    {%- if item.ULI == 'ENABLE' -%}
        {%- if item.ULIWLAN is not none -%}
            ULIWLAN={{item.ULIWLAN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.1 配置话单中携带用户信息字段，如表1所示。

#### **表1** 话单中用户信息字段

#### | 类别 | 话单字段 | 字段解释 |

#### | --- | --- | --- |

#### | **ADD CDRFIELDTEMP** | MSISDN字段 | 该字段记录用户的MSISDN号。 |

#### |  | served-imeisv字段 | 该字段记录用户的IMEISV号。 |

#### |  | CCSeletionMode字段 | 该字段记录计费属性Charging Characteristics的选择模式，是使用用户激活消息中所携带的SGSN/S-GW/MME计费属性，还是使用GGSN/SGW-C/PGW-C所配置的计费属性。 |

#### | **BIT836 控制是否携带华为CG的5G定制字段** | user5GFlag字段 | 该字段记录用户是否为5G用户。 说明：  当和华为CG对接时，此软参需设置为1，其他场景设置为0。 |

#### 1.2 配置话单中携带接入信息字段，如表2所示。

#### **表2** 话单中接入信息字段

#### | 类别 | 话单字段 | 字段解释 |

#### | --- | --- | --- |

#### | **ADD CDRFIELDTEMP** | ApnNetworkId字段 | 该字段记录APN中的网络节点标识信息。 |

#### |  | ApnSelectMode字段 | 该字段记录SGSN/MME的APN选择模式。 |

#### |  | PDPType字段 | 该字段记录PDP类型，IP或者PPP。 |

#### |  | SGSNSGWPLMNId字段 | 该字段记录SGSN/S-GW/MME的PLMN。 |

#### |  | ServedPDPAddr字段 | 该字段记录用户地址。 |

#### |  | DynAddrFlag字段 | 该字段标识用户地址是动态分配地址。  说明：  对于单栈用户，该字段用于标识IPv4或IPv6类型的动态地址。 |

#### |  | ULI字段 | 该字段记录3GPP用户位置信息。  说明：  3GPP用户接入时，只有SGSN/S-GW和SGW-C/PGW-C都支持user-location-information字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |

#### |  | RATType字段 | 该字段记录用户的无线接入技术类型，取值有**UTRAN**、**GERAN**、**GAN**、**UTRAN**和**HSPA Evolution**。  说明：  只有SGSN/S-GW/SGW-C/MME和PGW-C都支持携带RATType字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |

#### |  | MSTimeZone字段 | 该字段记录用户所在时区。  说明：  只有SGSN/S-GW/SGW-C和PGW-C都支持携带ms-time-zone字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |

#### |  | PGWAddressUsed字段 | 该字段记录P-GW的控制面地址，该字段记录IPv4地址。 |

#### |  | PGWAddressIPv6字段 | 该字段记录P-GW或S5/S8接口的IPv6地址。  说明：  该字段协议定义仅R9、R10版本的PGW-CDR支持。 |

#### |  | PGWPLMNId字段 | 该字段记录P-GW的PLMN。 |

#### |  | NodeId字段 | 该字段记录GGSN/SGW-C/PGW-C的节点标识，节点标识名称通过命令**SET OFCCDRPARA**进行设置。 |

#### |  | NetInitPDPCont | 该字段记录用户PDP上下文/EPS承载是由网络侧激活的。 |

#### |  | PDNConnectionId字段 | 该字段记录缺省承载的计费标识，以此可以识别出同一个PDN连接内的话单。  说明：  **ADD CDRFIELDTEMP**命令设置的字段对应于话单中的pdn-connection-charging-id字段。 |

#### |  | msiUnauthFlag字段 | 该字段记录用户的IMSI是否未鉴权。  说明：  通过GTPv2接入的紧急呼叫用户如果IMSI未鉴权，GGSN/SGW-C/PGW-C向CG上报R9及之后版本话单时携带该字段。 |

#### 1.3 配置话单中携带业务信息字段，如表3所示。

#### **表3** 话单中业务信息字段

#### | 类别 | 话单字段 | 字段解释 |

#### | --- | --- | --- |

#### | **SET OFCCDRPARA** | List of Traffic Volume | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR是否携带流量容器（ListOfTrafficVolume）。 |

#### |  | RAT Type | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带RAT Type。 |

#### |  | APN-AMBR | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带APN-AMBR。 |

#### | **ADD CDRFIELDTEMP** | LoTV字段 | 该字段记录用户上下行流量信息。 |

#### |  | LoSD字段 | 该字段记录业务上下行流量信息。  说明：  R6版本以后的eG-CDR话单中支持该字段。  R8版本以后的PGW-CDR和SGW-CDR话单中支持该字段。 |

#### |  | RecordExtention字段 | 该字段记录运营商或设备制造商定义的扩展信息。  说明：  内容计费G-CDR话单需要扩展RecordExtention字段，普通计费G-CDR话单不需要扩展该字段。R4及之后版本的G-CDR话单以及R6及之后版本的eG-CDR才支持该字段。  说明：  当参数“record-extensions-operator”设置为“glb”时：  * 若同时开启AAA RADIUS计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带RADIUS Acct-Session-ID、Termination-Cause字段。 * 若同时开启内容计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带各业务（RG+SID）上下行报文数。 |

#### |  | ImsSigContext字段 | 该字段用户标识是IMS信令专用上下文。 |

#### |  | StartTime字段 | 该字段记录PDP上下文/EPS承载激活的时间。 |

#### |  | StopTime字段 | 该字段记录PDP上下文/EPS承载去激活的时间。 |

#### 1.4 配置话单中其他信息字段，如表4所示。

#### **表4** 话单中其他信息字段

#### | 类别 | 话单字段 | 字段解释 |

#### | --- | --- | --- |

#### | **ADD CDRFIELDTEMP** | Diagnostics字段 | 该字段记录用户去激活的原因。 |

#### |  | RecSeqNumber字段 | 该字段记录同一PDP上下文/EPS承载中产生的话单的帧序列号。 |

#### |  | LocalRecSeqNum字段 | 该字段记录GGSN/SGW-C/PGW-C重启后分配的话单顺序号。 |

#### |  | PSFCI字段 | 该字段记录运营商或设备制造商定义的信息。 |

### 2 配置全局话单字段模板。

```jinja2
{%- for item in set_glbcdrfldtemp_list -%}
    SET GLBCDRFLDTEMP:
    {#- --- 可选参数 --- -#}
    {%- if item.PGWCDRTEMPLATE is not none -%}
        PGWCDRTEMPLATE="{{item.PGWCDRTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置APN实例的话单字段模板。

#### 3.1 配置APN实例。如已配置APN，请跳过该步骤。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 3.2 配置APN实例绑定话单字段模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PGWCDRTEMPLATE is not none -%}
        PGWCDRTEMPLATE="{{item.PGWCDRTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

