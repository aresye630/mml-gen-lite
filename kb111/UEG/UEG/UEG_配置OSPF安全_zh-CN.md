---
id: ''
name: 配置OSPF安全
ne_type: UEG
type: feature
description: 网络上对OSPF协议的攻击方法主要为伪造报文攻击，可以通过配置报文认证手段来识别并丢弃这些报文。  可能的攻击手段有：  * 修改报文老化时间到最大老化时间，导致所有FENIX设备废弃这个报文。 * 发布合法的Max Sequence Number的LSA或者接近Max Seq Num的报文。 * 邻居FENIX设备重启时复位其加密序列号状态的时机，更改序列号。 * 修改Hello报文中的邻居列表。  OSPF支持报文验证功能，只有通过验证的报文才能接收，否则将不能正常建立邻居关系。使用区域验证时，一个区域中所有的FENIX设备在该区域下的验证模式和口令必须一致。例如，在Area0内所有FENIX设备上配置验证模式为简单验证，口令为abc。接口验证方式用于在相邻的FENIX设备之间设置验证模式和口令，优先级高于区域验证方式。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置OSPF安全"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置OSPF安全"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置OSPF安全"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置OSPF安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网络上对OSPF协议的攻击方法主要为伪造报文攻击，可以通过配置报文认证手段来识别并丢弃这些报文。可能的攻击手段有：* 修改报文老化时间到最大老化时间，导致所有FENIX设备废弃这个报文。* 发布合法的Max Sequence Number的LSA或者接近Max Seq Num的报文。* 邻居FENIX设备重启时复位其加密序列号状态的时机，更改序列号。* 修改Hello报文中的邻居列表。OSPF支持报文验证功能，只有通过验证的报文才能接收，否则将不能正常建立邻居关系。使用区域验证时，一个区域中所有的FENIX设备在该区域下的验证模式和口令必须一致。例如，在Area0内所有FENIX设备上配置验证模式为简单验证，口令为abc。接口验证方式用于在相邻的FENIX设备之间设置验证模式和口令，优先级高于区域验证方式。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfinterface_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域标识'
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
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_ospfinterfaceauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
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
          - hmac-md5
          - hmac-sha256
          - keychain
          - md5
          - 'null'
          - simple
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTSIMPLE:
          name: '简单认证密码'
          type: string
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ospf_list:
    - PROCID: 进程号
    add_ospfarea_list:
    - PROCID: 进程号
      AREAID: '区域号'
    add_ospfinterface_list:
    - PROCID: 进程号
      AREAID: '区域标识'
      IFNAME: '接口名'
    add_ospfnetwork_list:
    - PROCID: 进程号
      AREAID: '区域号'
      IPADDRESS: 'IP地址'
      WILDCARDMASK: '掩码'
    mod_ospfinterfaceauth_list:
    - PROCID: OSPF进程号
      AREAID: '区域号'
      IFNAME: '接口名'
      AUTHENMODE: 认证模式
      AUTHTEXTSIMPLE: '简单认证密码'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 创建OSPF进程。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ;
{%- endfor -%}
```

### 2 增加OSPF区域。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

### 3 增加运行OSPF协议的接口。

### 选择执行如下步骤之一：

#### 3.1 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_ospfinterface -%}
    {%- for item in add_ospfinterface_list -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 参数“AREAID”（区域号）与步骤2中的“AREAID”的取值相一致。

#### 3.2 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- if is_scenario_ospfnetwork -%}
    {%- for item in add_ospfnetwork_list -%}
        ADD OSPFNETWORK:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        IPADDRESS="{{item.IPADDRESS}}",
        WILDCARDMASK="{{item.WILDCARDMASK}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果接口的IP地址在**ADD OSPFNETWORK**命令指定的网段范围内，接口就会自动运行OSPF协议。

#### 参数“AREAID”（区域号）与步骤2中的“AREAID”的取值相一致。

### 4 配置OSPF接口验证参数。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in mod_ospfinterfaceauth_list -%}
    MOD OSPFINTERFACEAUTH:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    AUTHENMODE={{item.AUTHENMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AUTHENMODE=simple 时可选 --- -#}
    {%- if item.AUTHENMODE == 'simple' -%}
        {%- if item.AUTHTEXTSIMPLE is not none -%}
            AUTHTEXTSIMPLE="{{item.AUTHTEXTSIMPLE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

