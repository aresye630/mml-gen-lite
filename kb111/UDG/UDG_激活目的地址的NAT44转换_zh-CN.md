---
id: ''
name: 激活目的地址的NAT44转换
ne_type: UDG
type: feature
description: 当运营商的公网用户需要访问私网服务器时，需要激活目的地址的NAT44转换特性。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT基本功能","激活目的地址的NAT44转换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商的公网用户需要访问私网服务器时，需要激活目的地址的NAT44转换特性。

## 必备事项
前提条件

* 已通过**ADD APN**完成APN的相关配置。
* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    system-view_list:
      type: items
      properties: {}
    ip_pool_list:
      type: items
      properties:
        POOL-NAME:
          name: 'pool-name'
          type: string
          required: false
          description: '设置源地址NAT转换地址池的名称为poolnat1。  设置目的地址NAT转换地址池的名称为poolnat2。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'mode'
          type: string
          required: false
          description: '源地址NAT转换地址池poolnat1的模式为PBA。  目的地址NAT转换地址池poolnat2的模式为No-PAT。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    section_list:
      type: items
      properties:
        SECTION-NUM:
          name: 'section-num'
          type: string
          required: false
          description: '地址段的编号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        START-IP-ADDRESS:
          name: 'start-ip-address'
          type: string
          required: false
          description: '* 源地址NAT转换地址池poolnat1的起始IPv4地址为10.1.1.1。 * 目的地址NAT转换地址池poolnat2的起始IPv4地址为192.168.1.1。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        END-IP-ADDRESS:
          name: 'end-ip-address'
          type: string
          required: false
          description: '* 源地址NAT转换地址池poolnat1的结束IPv4地址为10.1.1.10。 * 目的地址NAT转换地址池poolnat2的结束IPv4地址为192.168.1.10。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    quit_list:
      type: items
      properties: {}
    system-view_list_1:
      type: items
      properties: {}
    ip_pool_list_1:
      type: items
      properties:
        POOL-NAME:
          name: 'pool-name'
          type: string
          required: false
          description: '设置源地址NAT转换地址池的名称为poolnat1。  设置目的地址NAT转换地址池的名称为poolnat2。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'mode'
          type: string
          required: false
          description: '源地址NAT转换地址池poolnat1的模式为PBA。  目的地址NAT转换地址池poolnat2的模式为No-PAT。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    vpn-instance_list:
      type: items
      properties:
        VPN-INSTANCE-NAME:
          name: 'vpn-instance-name'
          type: string
          required: false
          description: 'VPN实例名称，该VPN是数据转发相关的VPN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    dnat_list:
      type: items
      properties:
        ENABLE:
          name: 'enable'
          type: string
          required: false
          description: '配置目的地址NAT转换地址池使能DNAT功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    section_list_1:
      type: items
      properties:
        SECTION-NUM:
          name: 'section-num'
          type: string
          required: false
          description: '地址段的编号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        START-IP-ADDRESS:
          name: 'start-ip-address'
          type: string
          required: false
          description: '* 源地址NAT转换地址池poolnat1的起始IPv4地址为10.1.1.1。 * 目的地址NAT转换地址池poolnat2的起始IPv4地址为192.168.1.1。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        END-IP-ADDRESS:
          name: 'end-ip-address'
          type: string
          required: false
          description: '* 源地址NAT转换地址池poolnat1的结束IPv4地址为10.1.1.10。 * 目的地址NAT转换地址池poolnat2的结束IPv4地址为192.168.1.10。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    quit_list_1:
      type: items
      properties: {}
    nap-view_list:
      type: items
      properties: {}
    nap-filter_l34-protocol_list:
      type: items
      properties:
        NAP-FILTER-NAME:
          name: 'nap-filter-name'
          type: string
          required: false
          description: '配置过滤器的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34-PROTOCOL-VALUE:
          name: 'l34-protocol-value'
          type: string
          required: false
          description: '设置三四层协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    nap-filter-group_nap-filter_list:
      type: items
      properties:
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置过滤器组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-NAME:
          name: 'nap-filter-name'
          type: string
          required: false
          description: '配置过滤器名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    nap-refresh-service_list:
      type: items
      properties: {}
    nat-policy_nap-filter-group_vpn-instance_action_source-nat_nat-address-pool_destination-nat_nat-address-pool_priority_list:
      type: items
      properties:
        NAT-POLICY-NAME:
          name: 'nat-policy-name'
          type: string
          required: false
          description: '配置策略的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAP-FILTER-GROUP-NAME:
          name: 'nap-filter-group-name'
          type: string
          required: false
          description: '配置策略的过滤规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPN-INSTANCE-NAME:
          name: 'vpn-instance-name'
          type: string
          required: false
          description: '配置生效的VPN，该VPN是用户激活的VPN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SOURCE-NAT NAT-ADDRESS-POOL:
          name: 'source-nat nat-address-pool'
          type: string
          required: false
          description: '针对IPv4的报文做源NAT44转换，指定NAT转换使用的IPv4源地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTINATION-NAT NAT-ADDRESS-POOL:
          name: 'destination-nat nat-address-pool'
          type: string
          required: false
          description: '针对IPv4的报文做目的NAT44转换，指定NAT转换使用的IPv4目的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY-VALUE:
          name: 'priority-value'
          type: string
          required: false
          description: '指定该策略的优先级，值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    system-view_list:
    - {}
    ip_pool_list:
    - POOL-NAME: poolnat1
      MODE: pba
    section_list:
    - SECTION-NUM: '0'
      START-IP-ADDRESS: 10.1.1.1
      END-IP-ADDRESS: 10.1.1.10
    quit_list:
    - {}
    system-view_list_1:
    - {}
    ip_pool_list_1:
    - POOL-NAME: poolnat1
      MODE: pba
    vpn-instance_list:
    - VPN-INSTANCE-NAME: vpn1
    dnat_list:
    - ENABLE: disable
    section_list_1:
    - SECTION-NUM: '0'
      START-IP-ADDRESS: 10.1.1.1
      END-IP-ADDRESS: 10.1.1.10
    quit_list_1:
    - {}
    nap-view_list:
    - {}
    nap-filter_l34-protocol_list:
    - NAP-FILTER-NAME: nap-testfilter
      L34-PROTOCOL-VALUE: any
    nap-filter-group_nap-filter_list:
    - NAP-FILTER-GROUP-NAME: testfiltergroupname
      NAP-FILTER-NAME: nap-testfilter
    nap-refresh-service_list:
    - {}
    nat-policy_nap-filter-group_vpn-instance_action_source-nat_nat-address-pool_destination-nat_nat-address-pool_priority_list:
    - NAT-POLICY-NAME: testpolicyname
      NAP-FILTER-GROUP-NAME: testfiltergroupname
      VPN-INSTANCE-NAME: vpn1
      SOURCE-NAT NAT-ADDRESS-POOL: poolnat1
      DESTINATION-NAT NAT-ADDRESS-POOL: poolnat2
      PRIORITY-VALUE: '5'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 2 配置源地址NAT转换地址池。

#### 2.1 进入系统视图。

#### **sy****stem-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该system-view_list的变量区（command: system-view） -#}
<!-- MISSING_MACRO: command=system-view list_name=system-view_list step_id=2.1 -->
```

#### 2.2 配置NAT地址池，有三种模式：No-PAT、NAPT和PBA。

#### **ip pool**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该ip_pool_list的变量区（command: ip pool） -#}
<!-- MISSING_MACRO: command=ip pool list_name=ip_pool_list step_id=2.2 -->
```

#### 2.3 配置NAT地址池的地址段。

#### **section**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该section_list的变量区（command: section） -#}
<!-- MISSING_MACRO: command=section list_name=section_list step_id=2.3 -->
```

#### 2.4 返回系统视图。

#### **quit**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该quit_list的变量区（command: quit） -#}
<!-- MISSING_MACRO: command=quit list_name=quit_list step_id=2.4 -->
```

### 3 配置目的地址NAT转换地址池。

#### 3.1 进入系统视图。

#### **sy****stem-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该system-view_list_1的变量区（command: system-view） -#}
<!-- MISSING_MACRO: command=system-view list_name=system-view_list_1 step_id=3.1 -->
```

#### 3.2 配置NAT地址池

#### **ip pool**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该ip_pool_list_1的变量区（command: ip pool） -#}
<!-- MISSING_MACRO: command=ip pool list_name=ip_pool_list_1 step_id=3.2 -->
```

#### 当前目的地址的NAT转换地址池仅支持配置为No-PAT模式。

#### 3.3 配置NAT地址池所属的VPN实例。

#### **vpn-instance**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该vpn-instance_list的变量区（command: vpn-instance） -#}
<!-- MISSING_MACRO: command=vpn-instance list_name=vpn-instance_list step_id=3.3 -->
```

#### 3.4 配置地址池使能DNAT功能。

#### **dnat**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该dnat_list的变量区（command: dnat） -#}
<!-- MISSING_MACRO: command=dnat list_name=dnat_list step_id=3.4 -->
```

#### 3.5 配置NAT地址池的地址段。

#### **section**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该section_list_1的变量区（command: section） -#}
<!-- MISSING_MACRO: command=section list_name=section_list_1 step_id=3.5 -->
```

#### 3.6 返回系统视图。

#### **quit**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该quit_list_1的变量区（command: quit） -#}
<!-- MISSING_MACRO: command=quit list_name=quit_list_1 step_id=3.6 -->
```

### 4 配置NAT过滤条件

#### 4.1 进入nap视图。

#### **nap****-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=4.1 -->
```

#### 4.2 配置三四层NAT过滤条件。

#### **nap-filter** *xxx* **l34-protocol** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter_l34-protocol_list的变量区（command: nap-filter l34-protocol） -#}
<!-- MISSING_MACRO: command=nap-filter l34-protocol list_name=nap-filter_l34-protocol_list step_id=4.2 -->
```

#### 4.3 配置NAT过滤条件组，可绑定已配置的NAT filter。当配置了多个NAT filter时，满足其中一个过滤条件即可。

#### **nap-filter-group** *xxx* **nap-filter** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter-group_nap-filter_list的变量区（command: nap-filter-group nap-filter） -#}
<!-- MISSING_MACRO: command=nap-filter-group nap-filter list_name=nap-filter-group_nap-filter_list step_id=4.3 -->
```

#### 4.4 生效NAT过滤条件。

#### **nap-refresh-service**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-refresh-service_list的变量区（command: nap-refresh-service） -#}
<!-- MISSING_MACRO: command=nap-refresh-service list_name=nap-refresh-service_list step_id=4.4 -->
```

### 5 配置NAT策略。

### **nat-policy** *xxx* **nap-filter-group** *xxx* **vpn-instance** *xxx* **action source-nat nat-address-pool** *xxx* **destination-nat nat-address-pool** *xxx* **priority** *x*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-policy_nap-filter-group_vpn-instance_action_source-nat_nat-address-pool_destination-nat_nat-address-pool_priority_list的变量区（command: nat-policy nap-filter-group vpn-instance action source-nat nat-address-pool destination-nat nat-address-pool priority） -#}
<!-- MISSING_MACRO: command=nat-policy nap-filter-group vpn-instance action source-nat nat-address-pool destination-nat nat-address-pool priority list_name=nat-policy_nap-filter-group_vpn-instance_action_source-nat_nat-address-pool_destination-nat_nat-address-pool_priority_list step_id=5 -->
```

### 此处VPN需要与业务VPN实例名称保持一致。

