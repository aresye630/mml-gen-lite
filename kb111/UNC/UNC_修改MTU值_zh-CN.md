---
id: ''
name: 修改MTU值
ne_type: UNC
type: feature
description: 修改MTU值为**高危操作**，例如：  * MTU修改可能导致整网分片增多，其他网元的分片重组能力的限制可能导致业务受影响。 * 部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。  网元外联口MTU值和直连下一跳网关（DCGW/路由器等）的接口MTU值必须一致，默认值是1500，如果运营商没有特殊要求和组网要求，建议保持默认值。  如下几种场景下，可参考本页面修改MTU值：  * 配合整网规划修改Fabric平面MTU值时。 * 配合整网规划修改Tunnel接口MTU值时。 * 配合整网规划修改外联口MTU值时。  * 为保证系统正常通信，**网卡MTU****≥Fabric的MTU>主接口的MTU≥子接口的MTU**。 * 建议子接口的MTU和主接口的配置一致。 * 网元实例化完成后，Fabric平面的MTU可以通过命令**SET FABRICMTU**修改。 * 修改硬件网卡的MTU的操作步骤请参考相应的硬件产品手册进行。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","修改MTU值"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
修改MTU值为**高危操作**，例如：* MTU修改可能导致整网分片增多，其他网元的分片重组能力的限制可能导致业务受影响。* 部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。网元外联口MTU值和直连下一跳网关（DCGW/路由器等）的接口MTU值必须一致，默认值是1500，如果运营商没有特殊要求和组网要求，建议保持默认值。如下几种场景下，可参考本页面修改MTU值：* 配合整网规划修改Fabric平面MTU值时。* 配合整网规划修改Tunnel接口MTU值时。* 配合整网规划修改外联口MTU值时。* 为保证系统正常通信，**网卡MTU****≥Fabric的MTU>主接口的MTU≥子接口的MTU**。* 建议子接口的MTU和主接口的配置一致。* 网元实例化完成后，Fabric平面的MTU可以通过命令**SET FABRICMTU**修改。* 修改硬件网卡的MTU的操作步骤请参考相应的硬件产品手册进行。

## 必备事项
前提条件

请阅读并熟悉IPFD-010001 接口管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_fabricmtu_list:
      type: items
      properties:
        MTUVALUE:
          name: 'MTU值'
          type: integer
          minimum: 512
          maximum: 9600
          required: true
          description: '设置Fabric平面的MTU值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置Tunnel接口MTU值。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_autoconfig_list:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '自动化配置模板名称，可通过**LST AUTOSCALINGSERVICE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MTU:
          name: '最大传输单元'
          type: integer
          minimum:
          - 0
          - 46
          maximum:
          - 0
          - 9600
          required: false
          description: '与**MOD INTERFACE**命令设置的MTU值相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_autoconfig_list_1:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_fabricmtu_list:
    - MTUVALUE: 1800
    mod_interface_list:
    - IFNAME: 'Tunnel6'
      IFMTU: 1500
    set_ifipv6enable_list:
    - IFNAME: 'Tunnel6'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_1:
    - IFNAME: 'Ethernet64/0/4'
      IFMTU: 1500
    set_ifipv6enable_list_1:
    - IFNAME: 'Ethernet64/0/4'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_2:
    - IFNAME: 'Ethernet64/0/4.1'
      IFMTU: 1500
    set_ifipv6enable_list_2:
    - IFNAME: 'Ethernet64/0/4.1'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_3:
    - IFNAME: 'Eth-trunk1'
      IFMTU: 1500
    set_ifipv6enable_list_3:
    - IFNAME: 'Eth-trunk1'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_4:
    - IFNAME: 'Eth-trunk1.100'
      IFMTU: 1500
    set_ifipv6enable_list_4:
    - IFNAME: 'Eth-trunk1.100'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    mod_autoscalingservice_list:
    - SERVICENAME: 'ServName_test1'
      MTU: 1500
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 修改Fabric平面的MTU值

### Fabric平面的MTU值不满足要求时，修改Fabric平面的MTU值。

```jinja2
{%- for item in set_fabricmtu_list -%}
    SET FABRICMTU:
    {#- --- 必选参数 --- -#}
    MTUVALUE={{item.MTUVALUE}},
    ;
{%- endfor -%}
```

### 2 修改Tunnel接口的MTU值

### Tunnel接口的MTU值不满足要求时，修改Tunnel接口的MTU值。

#### 2.1 //IPv4 MTU

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in mod_interface_list -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 //IPv6 MTU

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 修改外联口的MTU值

### Ethernet接口组网时，修改外联口（Ethernet接口做外联口）的MTU值。

#### 3.1 修改外联口主接口的MTU值。

##### 3.1.1 //IPv4 MTU

```jinja2
{%- if is_scenario_ethernet and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_1 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 //IPv6 MTU

```jinja2
{%- if is_scenario_ethernet and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_1 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

##### 3.2.1 //IPv4 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_ethernet and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_2 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 //IPv6 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_ethernet and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 Eth-trunk接口组网时，修改外联口（Eth-trunk接口做外联口）的MTU值。

### Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

#### 4.1 修改外联口主接口的MTU值。

##### 4.1.1 //IPv4 MTU

```jinja2
{%- if is_scenario_eth_trunk and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_3 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 //IPv6 MTU

```jinja2
{%- if is_scenario_eth_trunk and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_3 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

##### 4.2.1 //IPv4 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_eth_trunk and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_4 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 //IPv6 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_eth_trunk and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_4 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 自动部署模式时，建议同步修改自动化配置模板中的MTU值。

### 执行本步骤，可避免后续因模板MTU值与接口实际MTU值不一致产生告警ALM-232398849 接口自动化配置失败；后续扩容场景，也可避免新扩容接口仍需参考步骤 3/步骤 4逐个修改MTU值。

#### 5.1 查询自动配置开关。

#### 自动配置开关，与修改前配置保持一致：

##### 5.1.1 “自动配置开关”取值为“是”，请依次执行步骤 5.b～步骤 5.d。

##### 5.1.2 “自动配置开关”取值为“否”，请只执行步骤 5.c，不执行其他步骤。

#### 5.2 关闭自动配置开关。

#### 执行**DSP OPSASSISTSTATE**命令，直到“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”或者查询无该脚本时，才能关闭自动配置开关。否则可能影响业务。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 修改自动化配置模板的MTU值。

```jinja2
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' and LST_AUTOCONFIG=='否' -%}
    {%- for item in mod_autoscalingservice_list -%}
        MOD AUTOSCALINGSERVICE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 开启自动配置开关。

```jinja2
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' -%}
    {%- for item in set_autoconfig_list_1 -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

