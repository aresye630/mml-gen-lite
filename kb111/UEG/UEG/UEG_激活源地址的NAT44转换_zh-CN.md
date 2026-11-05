---
id: ''
name: 激活源地址的NAT44转换
ne_type: UEG
type: feature
description: 当运营商给用户分配了私网IPv4地址，用户需要访问公网Internet业务时，需要激活源地址的NAT44特性。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC NAT功能专题（风筝S）","数据配置与调测","数据配置","配置NAT基本功能","激活源地址的NAT44转换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商给用户分配了私网IPv4地址，用户需要访问公网Internet业务时，需要激活源地址的NAT44特性。

## 必备事项
前提条件

* 已通过**ADD APN**完成APN的相关配置。
* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '配置地址池的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'mode'
          type: string
          required: false
          description: '配置NAT转换地址池的模式，有三种：No-PAT、NAPT和PBA。'
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
          description: '配置VPN实例名称，该VPN是数据转发相关的VPN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    pod-max-ip-number_list:
      type: items
      properties: {}
    section_list:
      type: items
      properties:
        SECTION-NUM:
          name: 'section-num'
          type: string
          required: false
          description: '配置地址段的编号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        START-IP-ADDRESS:
          name: 'start-ip-address'
          type: string
          required: false
          description: '配置地址段的起始IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        END-IP-ADDRESS:
          name: 'end-ip-address'
          type: string
          required: false
          description: '配置地址段的结束IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    quit_list:
      type: items
      properties: {}
    nap-view_list:
      type: items
      properties: {}
    nap-filter_list:
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
          description: '配置三四层协议类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    nap-filter-group_list:
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
    nat-policy_list:
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
          description: '针对IPv4的报文做源NAT44转换，配置NAT转换使用的IPv4源地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY-VALUE:
          name: 'priority-value'
          type: string
          required: false
          description: '配置该策略的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    system-view_list:
    - {}
    ip_pool_list:
    - POOL-NAME: testpool
      MODE: pba
    vpn-instance_list:
    - VPN-INSTANCE-NAME: testvpn1
    pod-max-ip-number_list:
    - {}
    section_list:
    - SECTION-NUM: '0'
      START-IP-ADDRESS: 10.10.10.2
      END-IP-ADDRESS: 10.10.10.254
    quit_list:
    - {}
    nap-view_list:
    - {}
    nap-filter_list:
    - NAP-FILTER-NAME: testnapfilter
      L34-PROTOCOL-VALUE: tcp
    nap-filter-group_list:
    - NAP-FILTER-GROUP-NAME: testfiltergroupname
      NAP-FILTER-NAME: testnapfilter
    nap-refresh-service_list:
    - {}
    nat-policy_list:
    - NAT-POLICY-NAME: testpolicy
      NAP-FILTER-GROUP-NAME: testfiltergroupname
      VPN-INSTANCE-NAME: srvvpn
      SOURCE-NAT NAT-ADDRESS-POOL: testpool
      PRIORITY-VALUE: '5'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 2 配置NAT转换地址池。

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

#### 2.3 配置NAT地址池所属的VPN实例。

#### **vpn-instance**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该vpn-instance_list的变量区（command: vpn-instance） -#}
<!-- MISSING_MACRO: command=vpn-instance list_name=vpn-instance_list step_id=2.3 -->
```

#### 2.4 **可选：**配置NAT地址池下pod最大地址个数。

#### **pod-max-ip-number**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该pod-max-ip-number_list的变量区（command: pod-max-ip-number） -#}
<!-- MISSING_MACRO: command=pod-max-ip-number list_name=pod-max-ip-number_list step_id=2.4 -->
```

#### * 21.5.0之前版本建议使用**vm-max-ip-number**进行该配置操作。

#### * 该配置仅适用于**NAPT**和**PBA**类型地址池。

#### * 该配置修改会引起回收/分配地址资源，影响当前业务，建议按照现网规划进行对应配置。

#### 2.5 配置NAT地址池的地址段。

#### **section**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该section_list的变量区（command: section） -#}
<!-- MISSING_MACRO: command=section list_name=section_list step_id=2.5 -->
```

#### 2.6 返回系统视图。

#### **quit**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该quit_list的变量区（command: quit） -#}
<!-- MISSING_MACRO: command=quit list_name=quit_list step_id=2.6 -->
```

### 3 配置NAT过滤条件。

#### 3.1 进入nap视图。

#### **nap****-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=3.1 -->
```

#### 3.2 配置三四层NAT过滤条件。

#### **nap-filter** *xxx* **l34-protocol** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter_list的变量区（command: nap-filter） -#}
<!-- MISSING_MACRO: command=nap-filter list_name=nap-filter_list step_id=3.2 -->
```

#### 3.3 配置NAT过滤条件组，可绑定已配置的NAT filter。当配置了多个NAT filter时，满足其中一个过滤条件即可。

#### **nap-filter-group** *xxx* **nap-filter** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter-group_list的变量区（command: nap-filter-group） -#}
<!-- MISSING_MACRO: command=nap-filter-group list_name=nap-filter-group_list step_id=3.3 -->
```

#### 3.4 生效NAT过滤条件。

#### **nap-refresh-service**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-refresh-service_list的变量区（command: nap-refresh-service） -#}
<!-- MISSING_MACRO: command=nap-refresh-service list_name=nap-refresh-service_list step_id=3.4 -->
```

### 4 配置NAT策略。

### **nat-policy** *xxx* **nap-filter-group** *xxx* **vpn-instance** *xxx* **action source-nat nat-address-pool** *xxx* **priority** *x*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-policy_list的变量区（command: nat-policy） -#}
<!-- MISSING_MACRO: command=nat-policy list_name=nat-policy_list step_id=4 -->
```

### 此处VPN需要与业务VPN实例名称保持一致。

