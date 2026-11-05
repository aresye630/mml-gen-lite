---
id: GWFD-030700
name: 配置N6侧免VxLAN隧道层二以太通信
ne_type: UEG
type: feature
description: UEG 裸机容器直连PE免交换组网+企业交换机不支持VXLAN隧道时，UPF支持基于N6层二以太通信（免VXLAN隧道方案），实现层二5G LAN跨UPF的终端互访或与N6侧服务器的互通业务。  该场景下，需要部署N6侧免VxLAN隧道层二以太通信。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-030700 5G LAN基本功能","可选功能","N6侧免VxLAN隧道层二以太通信","配置N6侧免VxLAN隧道层二以太通信"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG 裸机容器直连PE免交换组网+企业交换机不支持VXLAN隧道时，UPF支持基于N6层二以太通信（免VXLAN隧道方案），实现层二5G LAN跨UPF的终端互访或与N6侧服务器的互通业务。该场景下，需要部署N6侧免VxLAN隧道层二以太通信。

## 必备事项
前提条件

完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '层二5G LAN组时，必须设置为“ETHERNET”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PDNCONNECTTYPE:
          name: 'PDN连接类型'
          type: string
          enum:
          - VXLAN
          - ETHTERNET
          required: false
          description: 'N6侧免VxLAN隧道层二以太通信场景，使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VLANTYPE:
          name: 'VLAN类型'
          type: string
          enum:
          - UNIQUE
          - WHITELIST
          - QINQ
          - VLANMAP
          required: false
          description: '请根据实际需要进行规划。   * UNIQUE：插入唯一的VLAN。适用于终端报文不携带VLAN或携带VLAN0的场景。 * WHITELIST：基于白名单透传VLAN。适用于终端报文携带的VLAN ID（非VLAN0）与企业服务器所在VLAN 的VLAN ID相同的场景。 * QINQ：暂不支持。 * VLANMAP：将原有VLAN映射为新VLAN。适用于终端报文携带VLAN（非VLAN0）且与企业服务器所在VLAN ID不同的场景。该场景下，UPF不将终端报文的VLAN ID携带给企业服务器。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: false
          description: '“VLANTYPE”设置为“UNIQUE”时需要规划。  与企业服务器所在VLAN的VLAN ID相同，且企业服务器所在VLAN的VLAN ID不能为1。  UPF转发报文时携带该参数规划的VLAN信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ngvnvlanwl_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '表1中“VLANTYPE”设置为“WHITELIST”时需要规划。  一个5G LAN组只能配置一条VLAN白名单数据。  与层二5G LAN终端报文携带的VLAN ID相同，且层二5G LAN终端所在VLAN的VLAN ID不能为1。  与企业服务器所在VLAN的VLAN ID相同，且企业服务器所在VLAN的VLAN ID不能为1。  5G LAN组透传携带该参数规划的VLAN ID的报文。  层二5G LAN终端属于相同VLAN（正常VLAN且VLAN ID不为0），且与企业服务器所在VLAN ID相同时，可将“VLANTYPE”设置为“WHITELIST”及配置VLAN白名单数据。配置后，UPF将携带VLAN ID在VLAN白名单内的报文通过N6侧层二口转发。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ngvnvlanmap_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ORIGINALVLANID:
          name: '原始VLAN'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '5G LAN组接收的上行报文中的原始VLAN ID。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MAPPEDVLANID:
          name: '映射VLAN ID'
          type: integer
          minimum: 1
          maximum: 4094
          required: true
          description: '5G LAN组接收的上行报文中的原始VLAN ID映射后的VLAN ID。  映射VLAN ID与企业服务器所在VLAN的VLAN ID相同，且企业服务器所在VLAN的VLAN ID不能为1。  5G LAN层二终端属于相同VLAN（正常VLAN且VLAN ID不为0），且企业服务器所在VLAN与终端所在VLAN不同时，可配置VLAN映射数据。配置后，UPF将报文的VLAN ID（“原始VLAN”）映射成“映射VLAN ID”，然后通过N6侧层二口转发。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ifallowedvlan_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '传输N6层二报文的外联口名称。可通过**LST INTERFACE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFNAME2:
          name: '接口名称2'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANBEGIN:
          name: 'VLAN最小值'
          type: integer
          minimum: 2
          maximum: 4094
          required: true
          description: '表1中“VLANTYPE”设置为“WHITELIST”时时需要规划。  采用表2中的“VLAN ID”参数值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VLANEND:
          name: 'VLAN最大值'
          type: integer
          minimum: 2
          maximum: 4094
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      PDNCONNECTTYPE: ETHTERNET
      VLANTYPE: WHITELIST
      VLANID: 2000
    add_ngvnvlanwl_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VLANID: 2000
    add_ngvnvlanmap_list:
    - VNINSTANCE: '000003e9-460-08-01'
      ORIGINALVLANID: 500
      MAPPEDVLANID: 1000
    add_ifallowedvlan_list:
    - IFNAME: 'Ethernet64/0/7'
      IFNAME2: 'Ethernet64/0/8'
      VLANBEGIN: 2000
      VLANEND: 2000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置5G LAN基本配置。

### 详细配置请参见配置5G LAN基本功能，注意不能配置和VxLAN隧道相关的内容。

### 2 修改5G LAN组配置。

```jinja2
{%- for item in mod_ngvninstance_list -%}
    MOD NGVNINSTANCE:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNTYPE is not none -%}
        PDNTYPE={{item.PDNTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PDNCONNECTTYPE=ETHTERNET 时必选 --- -#}
    {%- if item.PDNCONNECTTYPE == 'ETHTERNET' -%}
        VLANTYPE={{item.VLANTYPE}},
    {%- endif -%}
    {#- --- 条件必选：VLANTYPE=UNIQUE/QINQ 时必选 --- -#}
    {%- if item.VLANTYPE in ['UNIQUE', 'QINQ'] -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.PDNCONNECTTYPE is not none -%}
            PDNCONNECTTYPE={{item.PDNCONNECTTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 “VLANTYPE”设置为“WHITELIST”时，配置VLAN白名单。

```jinja2
{%- if is_scenario_vlantype_whitelist -%}
    {%- for item in add_ngvnvlanwl_list -%}
        ADD NGVNVLANWL:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        VLANID={{item.VLANID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 “VLANTYPE”设置为“VLANMAP”时，配置VLAN映射数据。

```jinja2
{%- if is_scenario_vlantype_vlanmap -%}
    {%- for item in add_ngvnvlanmap_list -%}
        ADD NGVNVLANMAP:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        ORIGINALVLANID={{item.ORIGINALVLANID}},
        MAPPEDVLANID={{item.MAPPEDVLANID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置主接口允许通过的VLAN。

```jinja2
{%- for item in add_ifallowedvlan_list -%}
    ADD IFALLOWEDVLAN:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFNAME2="{{item.IFNAME2}}",
    VLANBEGIN={{item.VLANBEGIN}},
    VLANEND={{item.VLANEND}},
    ;
{%- endfor -%}
```

