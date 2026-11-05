---
id: ''
name: 配置内置NAT支持安全域路由
ne_type: UEG
type: feature
description: UEG使用内置NAT支持安全域路由功能时，需要通过本章配置内容进行激活。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC NAT功能专题（风筝S）","数据配置与调测","数据配置","配置内置NAT支持安全域路由"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG使用内置NAT支持安全域路由功能时，需要通过本章配置内容进行激活。

## 必备事项
前提条件

* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_routepolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '配置路由策略信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routepolicynode_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '已通过**ADD ROUTEPOLICY**命令配置，可以使**LST ROUTEPOLICY**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '配置路由策略的路由策略节点。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHMODE:
          name: '匹配模式'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_applynexthop_list:
      type: items
      properties:
        POLICYNAME:
          name: '路由策略名字'
          type: string
          maxLength: 200
          required: true
          description: '已通过**ADD ROUTEPOLICY**命令配置，可以使**LST ROUTEPOLICY**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODESEQUENCE:
          name: '路由策略节点号'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '已通过**ADD ROUTEPOLICYNODE**命令配置，可以使**LST ROUTEPOLICYNODE**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ISPEERADDRESS:
          name: '是否是对等体IP地址'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: '配置基于IPv4信息路由下一跳。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NEXTHOP:
          name: '下一跳地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_routepolicy_list:
    - POLICYNAME: 'a'
    add_routepolicynode_list:
    - POLICYNAME: 'a'
      NODESEQUENCE: 10
      MATCHMODE: permit
    add_applynexthop_list:
    - POLICYNAME: 'a'
      NODESEQUENCE: 10
      ISPEERADDRESS: FALSE
      NEXTHOP: '192.168.0.2'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 UEG上的数据配置

#### 1.1 配置路由策略名称。

```jinja2
{%- for item in add_routepolicy_list -%}
    ADD ROUTEPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

#### 1.2 添加路由策略节点。

```jinja2
{%- for item in add_routepolicynode_list -%}
    ADD ROUTEPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    NODESEQUENCE={{item.NODESEQUENCE}},
    MATCHMODE={{item.MATCHMODE}},
    ;
{%- endfor -%}
```

#### 1.3 设置路由下一跳。

#### IPv4时：**ADD APPLYNEXTHOP**

```jinja2
{%- for item in add_applynexthop_list -%}
    ADD APPLYNEXTHOP:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    NODESEQUENCE={{item.NODESEQUENCE}},
    ISPEERADDRESS={{item.ISPEERADDRESS}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ISPEERADDRESS=FALSE 时可选 --- -#}
    {%- if item.ISPEERADDRESS == 'FALSE' -%}
        {%- if item.NEXTHOP is not none -%}
            NEXTHOP="{{item.NEXTHOP}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 NAT上的数据配置

#### 2.1 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

#### 2.2 进入系统视图。

#### **system-view**

#### 2.3 进入TrafficLink视图。

#### **trafficlink-view**

#### 2.4 配置非匿名虚拟接口。

#### **sysvif name *xxx* ipv4** ***xxx*** **encaptype gtpu**

##### 2.4.1 相同名称的虚拟接口新配置会覆盖已有配置。使用**undo sysvif all**恢复默认值。

##### 2.4.2 虚拟接口配置的地址不能与对接网元的地址段重叠。

#### 2.5 配置TrafficLink。

#### **trafficlink *xxx* sysvif *xxx* srvvpn *xxx* upvpn *xxx* downvpn *xxx***

##### 2.5.1 方向VPN是由UpVPN和DownVPN构成，用于组网需要。使信任区域和非信任区域的用户报文不能直接互相转发，默认下一跳为NAT内部处理模块。信任区域侧上规划的VPN为UpVPN，非信任区域侧规划的VPN为DownVPN。不同VPN间路由隔离，通过引入BGP协议完成UpVPN和DownVPN的路由交互。

##### 2.5.2 绑定UpVPN，DownVPN和业务VPN。UpVPN和DownVPN来自于网络规划，VPN名称需要与VNRS的配置保持一致。

##### 2.5.3 U口、D口配置的VPN全局唯一，配置TrafficLink需要校验VPN是否已经存在，如果存在配置失败。如果冲突请排查

##### 2.5.4 允许**nat-policy**和TrafficLink配置相同的业务VPN，支持U口业务允许部分流量进行NAT处理，部分流量进行Trafficlink处理。

##### 2.5.5 Trafficlink配置规格为256。

#### 2.6 进入nap-view视图。

#### **nap-view**

#### 2.7 配置包过滤策略。

#### **packet-policy** ***xxx*** **nap-filter-group** ***xxx*** **vpn-instance *xxx* uplink action****permit****priority** ***x***

#### **packet-policy** ***xxx*** **nap-filter-group** ***xxx*** **vpn-instance *xxx* downlink action****permit****priority** ***x***

