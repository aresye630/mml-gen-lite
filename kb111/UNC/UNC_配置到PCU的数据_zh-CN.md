---
id: ''
name: 配置到PCU的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增BSC或SGSN时，在配置完成SGSN到BSC的路由数据后，可通过配置Gb接口数据建立SGSN到BSC的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到PCU的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增BSC或SGSN时，在配置完成SGSN到BSC的路由数据后，可通过配置Gb接口数据建立SGSN到BSC的逻辑连接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '增加业务IP。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nse_list:
      type: items
      properties:
        OTHERNODE:
          name: 'NSE连接方向'
          type: string
          maxLength: 29
          required: true
          description: '配置NSE链路数据。'
          data_source: ''
          pattern: ''
          default: ''
        SGSNINDEX:
          name: 'SGSN索引'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        NSEI:
          name: 'NSE标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSID:
          name: 'BSS编号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PFC:
          name: '是否支持PFC'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SPID:
          name: '是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ARP:
          name: '是否携带ARP信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RACAP:
          name: '是否携带RA Capability信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_gbiplocendpt_list:
      type: items
      properties:
        NSEI:
          name: 'NSE标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LIPV4:
          name: '本端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LUP:
          name: '本端UDP端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LIPV6:
          name: '本端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbiprmtendpt_list:
      type: items
      properties:
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIPV4:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RUP:
          name: '对端UDP端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSEI:
          name: 'NSE标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIPV6:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gb_list:
      type: items
      properties:
        AUTO:
          name: '启用Gb动态over IP自动配置功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbeppool_list:
      type: items
      properties:
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'vpn名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gblocportrge_list:
      type: items
      properties:
        PORTBGN:
          name: '起始端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGINPRECFGPORT:
          name: '起始预置端口'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          maxLength: 33
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_bssgp_list:
      type: items
      properties:
        BSSIDRULE:
          name: 'BSSID与NSEI的对应关系'
          type: string
          enum:
          - NSEI
          - NSEI_EXCLUDE_FIRST_2_DIGITS
          - NSEI_EXCLUDE_FIRST_3_DIGITS
          - NSEI_EXCLUDE_FIRST_DIGIT
          - NSEI_EXCLUDE_LAST_2_DIGITS
          - NSEI_EXCLUDE_LAST_3_DIGITS
          - NSEI_EXCLUDE_LAST_DIGIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbnsecfgpara_list:
      type: items
      properties:
        PARAINDEX:
          name: '模板索引'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPNUM:
          name: '本端端点个数'
          type: string
          enum:
          - FIVE
          - FOUR
          - NUMBER_OF_GB_IP_IN_SYSTEM
          - ONE
          - SIX
          - THREE
          - TWO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NUMBER_OF_GB_IP_IN_SYSTEM
    add_gbnsegrp_list:
      type: items
      properties:
        GRPINDEX:
          name: '关联索引'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSEIBGN:
          name: '起始NSEI'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSEIEND:
          name: '结束NSEI'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARAINDEX:
          name: '关联的NSE属性模板索引'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_bssidfornsei_list:
      type: items
      properties:
        NSEI:
          name: '起始NSE标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSIDRULE:
          name: 'BSSID与NSEI的对应关系'
          type: string
          enum:
          - NSEI
          - NSEI_EXCLUDE_FIRST_2_DIGITS
          - NSEI_EXCLUDE_FIRST_3_DIGITS
          - NSEI_EXCLUDE_FIRST_DIGIT
          - NSEI_EXCLUDE_LAST_2_DIGITS
          - NSEI_EXCLUDE_LAST_3_DIGITS
          - NSEI_EXCLUDE_LAST_DIGIT
          - NSEI_MAP_SPECIFIC_BSSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSID:
          name: 'BSS标识'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.80.130'
      VPNINSTNAME: 'VRF_Access'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_nse_list:
    - OTHERNODE: 'PCU1'
      SGSNINDEX: 0
      NSEI: 2740
      BSSID: 2740
      PFC: YES
      SPID: NO
      ARP: NO
      RACAP: NO
    add_gbiplocendpt_list:
    - NSEI: 2740
      IPT: IPV4
      LIPV4: '10.10.80.130'
      LUP: 12740
      VPNNAME: 'VRF_Access'
      LIPV6: ''
    add_gbiprmtendpt_list:
    - IPT: IPV4
      RIPV4: '10.10.10.1'
      RUP: 2704
      NSEI: 2740
      RIPV6: ''
    set_gb_list:
    - AUTO: YES
    add_gbeppool_list:
    - IPTYPE: IPV4
      IPV4: '10.10.80.130'
      VPNNAME: 'VRF_Access'
      GROUPID: 1
      IPV6: ''
    set_gblocportrge_list:
    - PORTBGN: 1024
      PORTEND: 10000
      BEGINPRECFGPORT: 2000
      DESC: 'DEFAULT'
    set_bssgp_list:
    - BSSIDRULE: NSEI
    add_gbnsecfgpara_list:
    - PARAINDEX: 1
      EPNUM: ONE
    add_gbnsegrp_list:
    - GRPINDEX: 1
      NSEIBGN: 2740
      NSEIEND: 2740
      PARAINDEX: 1
    add_bssidfornsei_list:
    - NSEI: 2740
      BSSIDRULE: NSEI_MAP_SPECIFIC_BSSID
      BSSID: 200
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置Gb接口业务IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置NSE链路数据。

#### 3.1 静态配置

##### 3.1.1 配置到每个PCU的NSE，IP承载的NSE配置类型为静态配置。

```jinja2
{%- if is_scenario_static_config -%}
    {%- for item in add_nse_list -%}
        ADD NSE:
        {#- --- 必选参数 --- -#}
        OTHERNODE="{{item.OTHERNODE}}",
        NSEI={{item.NSEI}},
        BSSID={{item.BSSID}},
        {#- --- 可选参数 --- -#}
        {%- if item.SGSNINDEX is not none -%}
            SGSNINDEX={{item.SGSNINDEX}},
        {%- endif -%}
        {%- if item.PFC is not none -%}
            PFC={{item.PFC}},
        {%- endif -%}
        {%- if item.SPID is not none -%}
            SPID={{item.SPID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PFC=YES 时可选 --- -#}
        {%- if item.PFC == 'YES' -%}
            {%- if item.ARP is not none -%}
                ARP={{item.ARP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PFC=YES 时可选 --- -#}
        {%- if item.PFC == 'YES' -%}
            {%- if item.RACAP is not none -%}
                RACAP={{item.RACAP}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 配置不同NSE下的本端端点。

```jinja2
{%- if is_scenario_static_config -%}
    {%- for item in add_gbiplocendpt_list -%}
        ADD GBIPLOCENDPT:
        {#- --- 必选参数 --- -#}
        NSEI={{item.NSEI}},
        IPT={{item.IPT}},
        LUP={{item.LUP}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            LIPV4="{{item.LIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            LIPV6="{{item.LIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.3 配置对端端点。

```jinja2
{%- if is_scenario_static_config -%}
    {%- for item in add_gbiprmtendpt_list -%}
        ADD GBIPRMTENDPT:
        {#- --- 必选参数 --- -#}
        IPT={{item.IPT}},
        RUP={{item.RUP}},
        NSEI={{item.NSEI}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            RIPV4="{{item.RIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            RIPV6="{{item.RIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 动态自动配置。

##### 3.2.1 打开自动配置开关。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in set_gb_list -%}
        SET GB:
        {#- --- 可选参数 --- -#}
        {%- if item.AUTO is not none -%}
            AUTO={{item.AUTO}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 添加IP地址到GB地址池。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in add_gbeppool_list -%}
        ADD GBEPPOOL:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            IPV6="{{item.IPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置本端端点端口范围，端口范围内的端口必须可用。起始预置端口(起始预置端口)用于指定动态流程上报的预配置端口，进行动态流程协商时发送使用，配置时预置端口范围需在对端配置的端口范围内。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in set_gblocportrge_list -%}
        SET GBLOCPORTRGE:
        {#- --- 可选参数 --- -#}
        {%- if item.PORTBGN is not none -%}
            PORTBGN={{item.PORTBGN}},
        {%- endif -%}
        {%- if item.PORTEND is not none -%}
            PORTEND={{item.PORTEND}},
        {%- endif -%}
        {%- if item.BEGINPRECFGPORT is not none -%}
            BEGINPRECFGPORT={{item.BEGINPRECFGPORT}},
        {%- endif -%}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.4 配置全局动态NSE与BSSID对应关系。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in set_bssgp_list -%}
        SET BSSGP:
        {#- --- 可选参数 --- -#}
        {%- if item.BSSIDRULE is not none -%}
            BSSIDRULE={{item.BSSIDRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.5 配置NSE属性模板，指定NSE的属性时，需要与对端网元协商，保持RIM/PFC/INR/LCS/CBL等参数与对端网元能力的一致性，否则小区上报失败。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in add_gbnsecfgpara_list -%}
        ADD GBNSECFGPARA:
        {#- --- 必选参数 --- -#}
        PARAINDEX={{item.PARAINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.EPNUM is not none -%}
            EPNUM={{item.EPNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.6 关联NSE到NSE属性模板。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in add_gbnsegrp_list -%}
        ADD GBNSEGRP:
        {#- --- 必选参数 --- -#}
        GRPINDEX={{item.GRPINDEX}},
        NSEIBGN={{item.NSEIBGN}},
        NSEIEND={{item.NSEIEND}},
        PARAINDEX={{item.PARAINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.7 配置NSEI和BSSID的对应关系。

```jinja2
{%- if is_scenario_dynamic_auto_config -%}
    {%- for item in add_bssidfornsei_list -%}
        ADD BSSIDFORNSEI:
        {#- --- 必选参数 --- -#}
        NSEI={{item.NSEI}},
        {#- --- 可选参数 --- -#}
        {%- if item.BSSIDRULE is not none -%}
            BSSIDRULE={{item.BSSIDRULE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：BSSIDRULE=NSEI_MAP_SPECIFIC_BSSID 时必选 --- -#}
        {%- if item.BSSIDRULE == 'NSEI_MAP_SPECIFIC_BSSID' -%}
            BSSID={{item.BSSID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

