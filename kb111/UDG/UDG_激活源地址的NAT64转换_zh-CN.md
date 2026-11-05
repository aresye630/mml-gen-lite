---
id: ''
name: 激活源地址的NAT64转换
ne_type: UDG
type: feature
description: 当运营商给用户分配了私网IPv6地址，用户需要访问IPv4 Internet业务（默认公网业务）时，需要在NAT app上激活支持NAT64功能。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT基本功能","激活源地址的NAT64转换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商给用户分配了私网IPv6地址，用户需要访问IPv4 Internet业务（默认公网业务）时，需要在NAT app上激活支持NAT64功能。

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
    lock_list:
      type: items
      properties: {}
    nat-ratio_list:
      type: items
      properties:
        RATIO-VALUE:
          name: 'ratio-value'
          type: string
          required: false
          description: '配置NATratio值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    port_list:
      type: items
      properties:
        PORT-START:
          name: 'port-start'
          type: string
          required: false
          description: '配置地址池的起始端口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORT-END:
          name: 'port-end'
          type: string
          required: false
          description: '配置地址池的终止端口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    pba_block-size_list:
      type: items
      properties:
        PBABLOCK-SIZE:
          name: 'pbablock-size'
          type: string
          required: false
          description: '配置pba地址池的blocksize的值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BLOCK-NUM:
          name: 'block-num'
          type: string
          required: false
          description: '配置pba地址池的最大block值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    unlock_list:
      type: items
      properties: {}
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAT-ADDRESS-POOL-NAME:
          name: 'nat-address-pool-name'
          type: string
          required: false
          description: '针对IPv4的报文做源NAT44转换，指定NAT转换使用的IPv4源地址池。'
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
    nat64_prefix_list:
      type: items
      properties:
        PREFIX-ADDRESS:
          name: 'prefix-address'
          type: string
          required: false
          description: '配置nat64地址的前缀地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    nap-well-known-port_list:
      type: items
      properties:
        PORT-NAME:
          name: 'port-name'
          type: string
          required: false
          description: '配置知名端口名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOL-NAME:
          name: 'protocol-name'
          type: string
          required: false
          description: '配置子协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRANS-PROTO:
          name: 'trans-proto'
          type: string
          required: false
          description: '配置传输层协议时TCP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPERATORPORT:
          name: 'operatorport'
          type: string
          required: false
          description: '配置端口范围。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY-VALUE:
          name: 'priority-value'
          type: string
          required: false
          description: '配置协议识别匹配时优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    detect-protocol_list:
      type: items
      properties:
        FTP:
          name: 'ftp'
          type: string
          required: false
          description: '配置NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        H323:
          name: 'h323'
          type: string
          required: false
          description: '配置NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PPTP:
          name: 'pptp'
          type: string
          required: false
          description: '配置NAT ALG/七层ASPF功能支持的协议类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    debug_pfom_set_nat64-mode_1_list:
      type: items
      properties: {}
  examples:
    system-view_list:
    - {}
    ip_pool_list:
    - POOL-NAME: testpool1
      MODE: pba
    vpn-instance_list:
    - VPN-INSTANCE-NAME: downvpn
    pod-max-ip-number_list:
    - {}
    section_list:
    - SECTION-NUM: '0'
      START-IP-ADDRESS: 10.10.11.0
      END-IP-ADDRESS: 10.10.11.250
    lock_list:
    - {}
    nat-ratio_list:
    - RATIO-VALUE: '2'
    port_list:
    - PORT-START: '1024'
      PORT-END: '2048'
    pba_block-size_list:
    - PBABLOCK-SIZE: '1024'
      BLOCK-NUM: '10'
    unlock_list:
    - {}
    quit_list:
    - {}
    nap-view_list:
    - {}
    nap-filter_list:
    - NAP-FILTER-NAME: fnat64
      L34-PROTOCOL-VALUE: any
    nap-filter-group_list:
    - NAP-FILTER-GROUP-NAME: gnat64
      NAP-FILTER-NAME: fnat64
    nap-refresh-service_list:
    - {}
    nat-policy_list:
    - NAT-POLICY-NAME: pnat64
      NAP-FILTER-GROUP-NAME: gnat64
      VPN-INSTANCE-NAME: srvvpn
      NAT-ADDRESS-POOL-NAME: testpool1
      PRIORITY-VALUE: '8'
    nat64_prefix_list:
    - PREFIX-ADDRESS: '2001:db8:: 32'
    nap-well-known-port_list:
    - PORT-NAME: testknownport-ftp
      PROTOCOL-NAME: ftp
      TRANS-PROTO: tcp
      OPERATORPORT: eq 21
      PRIORITY-VALUE: '20'
    detect-protocol_list:
    - FTP: ftp
      H323: h323
      PPTP: pptp
    debug_pfom_set_nat64-mode_1_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 2 配合NAT64转换地址池。

#### 2.1 进入系统视图。

#### **sy****stem-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该system-view_list的变量区（command: system-view） -#}
<!-- MISSING_MACRO: command=system-view list_name=system-view_list step_id=2.1 -->
```

#### 2.2 配置NAT64地址池，有三种模式：No-PAT、NAPT和PBA。

#### **ip pool**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该ip_pool_list的变量区（command: ip pool） -#}
<!-- MISSING_MACRO: command=ip pool list_name=ip_pool_list step_id=2.2 -->
```

#### 2.3 配置NAT64地址池所属的VPN实例。

#### **vpn-instance**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该vpn-instance_list的变量区（command: vpn-instance） -#}
<!-- MISSING_MACRO: command=vpn-instance list_name=vpn-instance_list step_id=2.3 -->
```

#### 2.4 **可选：**配置NAT64地址池下pod最大地址个数。

#### **pod-max-ip-number**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该pod-max-ip-number_list的变量区（command: pod-max-ip-number） -#}
<!-- MISSING_MACRO: command=pod-max-ip-number list_name=pod-max-ip-number_list step_id=2.4 -->
```

#### * 20.8.2之前版本建议使用**vm-max-ip-number**进行该配置操作。

#### 该配置仅适用于NAPT和PBA类型地址池。

#### 该配置修改会引起回收/分配地址资源，影响当前业务，建议按照现网规划进行对应配置。

#### 2.5 配置NAT64地址池的地址段。

#### **section**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该section_list的变量区（command: section） -#}
<!-- MISSING_MACRO: command=section list_name=section_list step_id=2.5 -->
```

#### 2.6 **可选：**配置pba地址池的相关信息。

#### 该步骤为可选，仅配置端口预分配功能时需完成该步骤。

##### 2.6.1 锁定地址池。

##### **lock**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该lock_list的变量区（command: lock） -#}
<!-- MISSING_MACRO: command=lock list_name=lock_list step_id=2.6.1 -->
```

##### 2.6.2 配置NAT地址池的ratio值。

##### **nat-ratio**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-ratio_list的变量区（command: nat-ratio） -#}
<!-- MISSING_MACRO: command=nat-ratio list_name=nat-ratio_list step_id=2.6.2 -->
```

##### 2.6.3 配置地址池的起始端口和终止端口。

##### **port**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该port_list的变量区（command: port） -#}
<!-- MISSING_MACRO: command=port list_name=port_list step_id=2.6.3 -->
```

##### 2.6.4 配置pba地址池的blocksize和max-block-num 。

##### **pba block-size**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该pba_block-size_list的变量区（command: pba block-size） -#}
<!-- MISSING_MACRO: command=pba block-size list_name=pba_block-size_list step_id=2.6.4 -->
```

##### 2.6.5 解除锁定的地址池。

##### **unlock**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该unlock_list的变量区（command: unlock） -#}
<!-- MISSING_MACRO: command=unlock list_name=unlock_list step_id=2.6.5 -->
```

#### 2.7 返回系统视图。

#### **quit**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该quit_list的变量区（command: quit） -#}
<!-- MISSING_MACRO: command=quit list_name=quit_list step_id=2.7 -->
```

### 3 配置NAT64过滤条件。生效NAT64过滤条件。

#### 3.1 进入nap视图。

#### **nap****-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=3.1 -->
```

#### 3.2 配置三四层NAT64过滤条件。

#### **nap-filter** *xxx*  **ipv6 l34-protocol** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-filter_list的变量区（command: nap-filter） -#}
<!-- MISSING_MACRO: command=nap-filter list_name=nap-filter_list step_id=3.2 -->
```

#### 3.3 配置NAT64过滤条件组，可绑定已配置的NAT filter。当配置了多个NAT filter时，满足其中一个过滤条件即可。

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

### 4 配置NAT64策略。

### **nat-policy** *xxx* **nap-filter-group** *xxx* **vpn-instance** *xxx* **action nat64 source-nat nat-address-pool** *xxx* **priority** *x*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-policy_list的变量区（command: nat-policy） -#}
<!-- MISSING_MACRO: command=nat-policy list_name=nat-policy_list step_id=4 -->
```

### 此处VPN需要与业务VPN实例名称保持一致。

### 5 配置IPv6前缀。

### 使用**nat64 prefix**的配置内容作为IPv6前缀。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat64_prefix_list的变量区（command: nat64 prefix） -#}
<!-- MISSING_MACRO: command=nat64 prefix list_name=nat64_prefix_list step_id=5 -->
```

### 6 配置NAT-ALG七层协议识别。

### 为了确保NAT-ALG功能正常运行，需要配置七层协议识别。NAT支持基于知名端口方式识别用户报文七层协议。如果七层协议具有知名端口特征(如FTP协议对应的知名端口为21和20)，建议配置知名端口可最大限度的保证NAT处理正确，用户业务正常。

#### 6.1 采用知名端口识别协议，配置知名端口识别。

#### **nap-well-known-port**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-well-known-port_list的变量区（command: nap-well-known-port） -#}
<!-- MISSING_MACRO: command=nap-well-known-port list_name=nap-well-known-port_list step_id=6.1 -->
```

#### 6.2 配置NAT-ALG支持的应用层协议类型。

#### **detect-protocol**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该detect-protocol_list的变量区（command: detect-protocol） -#}
<!-- MISSING_MACRO: command=detect-protocol list_name=detect-protocol_list step_id=6.2 -->
```

### 7 配置NAT64支持私网目的IP的地址转换功能开关。

### **debug pfom set nat64-mode 1**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该debug_pfom_set_nat64-mode_1_list的变量区（command: debug pfom set nat64-mode 1） -#}
<!-- MISSING_MACRO: command=debug pfom set nat64-mode 1 list_name=debug_pfom_set_nat64-mode_1_list step_id=7 -->
```

### 该步骤为可选，仅需要访问私网目的地址时需完成该步骤。

