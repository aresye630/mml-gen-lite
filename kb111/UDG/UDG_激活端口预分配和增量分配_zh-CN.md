---
id: ''
name: 激活端口预分配和增量分配
ne_type: UDG
type: feature
description: 当运营商需要提高对用户数据的溯源效率，可以开启NAT端口预分配和增量分配功能。  系统初始已有端口预分配配置默认值，操作人员可参考本章节修改配置取值。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT基本功能","激活端口预分配和增量分配"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要提高对用户数据的溯源效率，可以开启NAT端口预分配和增量分配功能。系统初始已有端口预分配配置默认值，操作人员可参考本章节修改配置取值。

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
          description: '设置NAT转换地址池的名称。'
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
    nat-ratio_list:
      type: items
      properties:
        RATIO-VALUE:
          name: 'ratio-value'
          type: string
          required: false
          description: '设置NAT ratio值，该值表示一个公网IP可以映射的私网IP数。'
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
          description: '设置地址池的起始端口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT-END:
          name: 'port-end'
          type: string
          required: false
          description: '设置地址池的终止端口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    pba_block-size_list:
      type: items
      properties:
        PBA BLOCK-SIZE:
          name: 'pba block-size'
          type: string
          required: false
          description: '设置pba地址池的block size。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BLOCK-NUM:
          name: 'block-num'
          type: string
          required: false
          description: '设置pba地址池的最大block值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    section_list:
      type: items
      properties:
        SECTION-NUM:
          name: 'section-num'
          type: string
          required: false
          description: '设置地址段的编号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        START-IP-ADDRESS:
          name: 'start-ip-address'
          type: string
          required: false
          description: '配置NAT地址池的起始IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        END-IP-ADDRESS:
          name: 'end-ip-address'
          type: string
          required: false
          description: '配置NAT地址池的结束IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    quit_list:
      type: items
      properties: {}
  examples:
    system-view_list:
    - {}
    ip_pool_list:
    - POOL-NAME: pbaname
      MODE: pba
    vpn-instance_list:
    - VPN-INSTANCE-NAME: testvpn1
    nat-ratio_list:
    - RATIO-VALUE: '2'
    port_list:
    - PORT-START: '1024'
      PORT-END: '65535'
    pba_block-size_list:
    - PBA BLOCK-SIZE: '16'
      BLOCK-NUM: '2'
    section_list:
    - SECTION-NUM: '0'
      START-IP-ADDRESS: 10.10.11.10
      END-IP-ADDRESS: 10.10.11.254
    quit_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 2 配合NAT转换地址池。

#### 2.1 进入系统视图。

#### **sy****stem-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该system-view_list的变量区（command: system-view） -#}
<!-- MISSING_MACRO: command=system-view list_name=system-view_list step_id=2.1 -->
```

#### 2.2 配置pba模式地址池。

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

#### 2.4 配置端口预分配功能。

##### 2.4.1 配置单个公网对应的私网地址最大数。

##### **nat-ratio**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-ratio_list的变量区（command: nat-ratio） -#}
<!-- MISSING_MACRO: command=nat-ratio list_name=nat-ratio_list step_id=2.4.1 -->
```

##### 2.4.2 配置端口大段和端口小段的大小和小段个数。

##### **port**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该port_list的变量区（command: port） -#}
<!-- MISSING_MACRO: command=port list_name=port_list step_id=2.4.2 -->
```

##### 2.4.3 配置端口预分配和增量分配。

##### **pba block-size *X* max-block-num *X***

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该pba_block-size_list的变量区（command: pba block-size） -#}
<!-- MISSING_MACRO: command=pba block-size list_name=pba_block-size_list step_id=2.4.3 -->
```

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

