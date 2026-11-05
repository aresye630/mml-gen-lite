---
id: ''
name: 配置OSPFv3安全
ne_type: UDG
type: feature
description: 网络上对OSPFv3协议的攻击方法主要为伪造报文攻击，可以通过配置报文认证手段来识别并丢弃这些报文。  可能的攻击手段有：  * 修改报文老化时间到最大老化时间，导致所有UDG废弃这个报文。 * 发布合法的Max Sequence Number的LSA或者接近Max Seq Num的报文。 * 邻居UDG重启时复位其加密序列号状态的时机，更改序列号。 * 修改Hello报文中的邻居列表。  OSPF支持报文验证功能，只有通过验证的报文才能接收，否则将不能正常建立邻居关系。使用区域验证时，一个区域中所有的UDG在该区域下的验证模式和口令必须一致。例如，在Area0内所有UDG上配置验证模式为简单验证，口令为abc。接口验证方式用于在相邻的UDG之间设置验证模式和口令，优先级高于区域验证方式。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置OSPFv3安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网络上对OSPFv3协议的攻击方法主要为伪造报文攻击，可以通过配置报文认证手段来识别并丢弃这些报文。可能的攻击手段有：* 修改报文老化时间到最大老化时间，导致所有UDG废弃这个报文。* 发布合法的Max Sequence Number的LSA或者接近Max Seq Num的报文。* 邻居UDG重启时复位其加密序列号状态的时机，更改序列号。* 修改Hello报文中的邻居列表。OSPF支持报文验证功能，只有通过验证的报文才能接收，否则将不能正常建立邻居关系。使用区域验证时，一个区域中所有的UDG在该区域下的验证模式和口令必须一致。例如，在Area0内所有UDG上配置验证模式为简单验证，口令为abc。接口验证方式用于在相邻的UDG之间设置验证模式和口令，优先级高于区域验证方式。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3interface_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSTANCEID:
          name: '实例号'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_ospfv3interfaceauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-sha256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTMD5:
          name: '密文验证密码'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSTANCEID:
          name: '实例号'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ospfv3_list:
    - PROCID: OSPFv3进程号
      ROUTERID: '路由器标识'
    add_ospfv3area_list:
    - PROCID: OSPFv3进程号
      AREAID: '区域标识'
    add_ospfv3interface_list:
    - PROCID: OSPFv3进程号
      AREAID: '区域号'
      IFNAME: '接口名称'
      INSTANCEID: 实例号
    add_ospfv3interfaceauth_list:
    - PROCID: OSPFv3进程号
      AREAID: '区域号'
      IFNAME: '接口名'
      AUTHENMODE: 认证模式
      AUTHTEXTMD5: '密文验证密码'
      KEYID: 密文验证字标识符
      INSTANCEID: 实例号
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建OSPFv3进程。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_ospfv3_list -%}
    ADD OSPFV3:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ROUTERID="{{item.ROUTERID}}",
    ;
{%- endfor -%}
```

### 2 增加OSPFv3区域。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

### 3 增加运行OSPFv3协议的接口。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_ospfv3interface_list -%}
    ADD OSPFV3INTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INSTANCEID is not none -%}
        INSTANCEID={{item.INSTANCEID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“AREAID”（区域号）与步骤2中的“AREAID”的取值相一致。

### 4 配置OSPFv3接口验证参数。

### 在“MML命令行-UDG”窗口上执行：

```jinja2
{%- for item in add_ospfv3interfaceauth_list -%}
    ADD OSPFV3INTERFACEAUTH:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    AUTHENMODE={{item.AUTHENMODE}},
    AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
    KEYID={{item.KEYID}},
    INSTANCEID={{item.INSTANCEID}},
    ;
{%- endfor -%}
```

### 参数“AUTHENMODE”选择“HMAC-SHA256”。

