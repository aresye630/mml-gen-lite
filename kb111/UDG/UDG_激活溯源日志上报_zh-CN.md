---
id: ''
name: 激活溯源日志上报
ne_type: UDG
type: feature
description: UDG支持将NAT上报至日志服务器，其中日志服务器可以为CloudUDN产品，也可以是其他Log Server，UDG与CloudUDN之间基于Natlog协议传输NAT日志，与其他Log Server间基于Syslog协议传输NAT日志。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT溯源日志","激活溯源日志上报"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UDG支持将NAT上报至日志服务器，其中日志服务器可以为CloudUDN产品，也可以是其他Log Server，UDG与CloudUDN之间基于Natlog协议传输NAT日志，与其他Log Server间基于Syslog协议传输NAT日志。

## 必备事项
前提条件

* 已完成NAT基本功能的数据配置，UDG能够正常进行NAT转换。
* 已配置完成UDG到CloudUDN或其他Log Server的路由数据。
* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    nap-view_list:
      type: items
      properties: {}
    natlog-view_list:
      type: items
      properties: {}
    natlog-client_list:
      type: items
      properties:
        ADDRESS:
          name: 'address'
          type: string
          required: false
          description: '日志客户端的IP地址，即NAT自身的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    natlog-server_list:
      type: items
      properties:
        SERVER-NAME:
          name: 'server-name'
          type: string
          required: false
          description: '备用日志服务器名称，此处取值样例为备用其他Log Server的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'address'
          type: string
          required: false
          description: '备用日志服务器的IP地址，此处取值样例为备用其他Log Server的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    natlog-carbon-copy_list:
      type: items
      properties: {}
    natlog-switch_list:
      type: items
      properties: {}
    nap-view_list_1:
      type: items
      properties: {}
    natlog-view_list_1:
      type: items
      properties: {}
    natlog-syslog_list:
      type: items
      properties: {}
    natlog-netflow_list:
      type: items
      properties: {}
    nat-policy_list:
      type: items
      properties: {}
    natlog-client_list_1:
      type: items
      properties:
        ADDRESS:
          name: 'address'
          type: string
          required: false
          description: '日志客户端的IP地址，即NAT自身的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    natlog-server_list_2:
      type: items
      properties:
        SERVER-NAME:
          name: 'server-name'
          type: string
          required: false
          description: '备用日志服务器名称，此处取值样例为备用其他Log Server的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRESS:
          name: 'address'
          type: string
          required: false
          description: '备用日志服务器的IP地址，此处取值样例为备用其他Log Server的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    natlog-carbon-copy_list_1:
      type: items
      properties: {}
    natlog-switch_list_1:
      type: items
      properties: {}
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV4NATLOG01'
      SWITCH: ENABLE
    nap-view_list:
    - {}
    natlog-view_list:
    - {}
    natlog-client_list:
    - ADDRESS: 192.168.10.2
    natlog-server_list:
    - SERVER-NAME: srv2
      ADDRESS: 192.168.15.13
    natlog-carbon-copy_list:
    - {}
    natlog-switch_list:
    - {}
    nap-view_list_1:
    - {}
    natlog-view_list_1:
    - {}
    natlog-syslog_list:
    - {}
    natlog-netflow_list:
    - {}
    nat-policy_list:
    - {}
    natlog-client_list_1:
    - ADDRESS: 192.168.10.2
    natlog-server_list_2:
    - SERVER-NAME: srv2
      ADDRESS: 192.168.15.13
    natlog-carbon-copy_list_1:
    - {}
    natlog-switch_list_1:
    - {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 全部展开

### 配置溯源日志上报功能License开关

#### 1.1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置溯源日志上报至CloudUDN

#### 2.1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

#### 2.2 进入natlog-view视图。

#### **nap-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=2.2 -->
```

#### **natlog-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-view_list的变量区（command: natlog-view） -#}
<!-- MISSING_MACRO: command=natlog-view list_name=natlog-view_list step_id=2.2 -->
```

#### 2.3 配置natlog-client，日志上报的客户端IP地址和名称。

#### **natlog-client address *xxx* clientname *xxx***

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-client_list的变量区（command: natlog-client） -#}
<!-- MISSING_MACRO: command=natlog-client list_name=natlog-client_list step_id=2.3 -->
```

#### 2.4 配置natlog-server，日志上报服务器。

#### **natlog-server**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-server_list的变量区（command: natlog-server） -#}
<!-- MISSING_MACRO: command=natlog-server list_name=natlog-server_list step_id=2.4 -->
```

#### 此处IP地址CloudUDN IP地址，端口配置为CloudUDN的通信端口，请以CloudUDN配套版本的通信矩阵中端口描述为准。

#### 如果需要配置日志主备抄送，则需要配置两个server服务器，同时使用natlog-carbon-copy命令打开主备抄送的开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-carbon-copy_list的变量区（command: natlog-carbon-copy） -#}
<!-- MISSING_MACRO: command=natlog-carbon-copy list_name=natlog-carbon-copy_list step_id=2.4 -->
```

#### 2.5 打开natlog日志上报给CloudUDN的开关。

#### **natlog-switch global binary allocate default**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-switch_list的变量区（command: natlog-switch） -#}
<!-- MISSING_MACRO: command=natlog-switch list_name=natlog-switch_list step_id=2.5 -->
```

### 3 配置溯源日志上报至其他Log Server

#### 3.1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

#### 3.2 配置自定义日志上报内容。

##### 3.2.1 进入natlog-view视图。

##### **nap-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list_1的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list_1 step_id=3.2.1 -->
```

##### **natlog-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-view_list_1的变量区（command: natlog-view） -#}
<!-- MISSING_MACRO: command=natlog-view list_name=natlog-view_list_1 step_id=3.2.1 -->
```

##### 3.2.2 配置自定义日志上报内容。

###### 3.2.2.1 日志格式为syslog：

###### **natlog-syslog template syslog format**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-syslog_list的变量区（command: natlog-syslog） -#}
<!-- MISSING_MACRO: command=natlog-syslog list_name=natlog-syslog_list step_id=3.2.2.1 -->
```

###### 3.2.2.2 日志格式为netflow：

###### **natlog-netflow template ipv4**（NAT44场景）

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-netflow_list的变量区（command: natlog-netflow） -#}
<!-- MISSING_MACRO: command=natlog-netflow list_name=natlog-netflow_list step_id=3.2.2.2 -->
```

#### 3.3 将激活源地址的NAT44转换中已经配置的策略绑定到syslog template，全局natlog开关。

#### **nat-policy** *xxx* **nap-filter-group** *xxx* **vpn-instance** *xxx* **action source-nat nat-address-pool** *xxx* **priority** *x* **syslog-template** *xxx*

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nat-policy_list的变量区（command: nat-policy） -#}
<!-- MISSING_MACRO: command=nat-policy list_name=nat-policy_list step_id=3.3 -->
```

#### 3.4 配置natlog-client，日志上报的客户端IP。

#### **natlog-client**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-client_list_1的变量区（command: natlog-client） -#}
<!-- MISSING_MACRO: command=natlog-client list_name=natlog-client_list_1 step_id=3.4 -->
```

##### 3.4.1 该命令中配置的VPN需要根据网络规划，与UDG配置用来和其他Log Server通信的VPN保持一致。

##### 3.4.2 此处IP地址为NAT本端的IP地址。

#### 3.5 配置natlog-server，日志上报服务器。

#### **natlog-server**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-server_list_2的变量区（command: natlog-server） -#}
<!-- MISSING_MACRO: command=natlog-server list_name=natlog-server_list_2 step_id=3.5 -->
```

##### 3.5.1 此处IP地址为Log Server IP地址，端口配置为Log Server的通信端口，请以Log Server配套版本的通信矩阵中端口描述为准。

##### 3.5.2 如果需要配置日志主备抄送，则需要配置两个server服务器，同时使用natlog-carbon-copy命令打开主备抄送的开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-carbon-copy_list_1的变量区（command: natlog-carbon-copy） -#}
<!-- MISSING_MACRO: command=natlog-carbon-copy list_name=natlog-carbon-copy_list_1 step_id=3.5 -->
```

#### 3.6 配置步骤2中对应策略的natlog开关。

#### **natlog-switch**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-switch_list_1的变量区（command: natlog-switch） -#}
<!-- MISSING_MACRO: command=natlog-switch list_name=natlog-switch_list_1 step_id=3.6 -->
```

