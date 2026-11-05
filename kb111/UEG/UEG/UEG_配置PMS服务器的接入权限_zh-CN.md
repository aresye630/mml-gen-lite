---
id: ''
name: 配置PMS服务器的接入权限
ne_type: UEG
type: feature
description: 客户端通过IP地址与PMS服务器进行连接时，为了确保PMS的数据安全，需要支持通过客户端IP地址对客户端进行鉴权，只有鉴权通过的客户端才允许接入到PMS服务器。  客户端包括以下三种：  * UPCF Web UI：提供业务策略配置、通知发送等功能。 * POP：POP生成策略脚本时，会通过该接口发送SOAP消息通知到UPCF。 * CLI客户端：通过CLI/SCLI接口提供UPCF策略数据配置功能。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置PMS服务器的接入权限"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
客户端通过IP地址与PMS服务器进行连接时，为了确保PMS的数据安全，需要支持通过客户端IP地址对客户端进行鉴权，只有鉴权通过的客户端才允许接入到PMS服务器。客户端包括以下三种：* UPCF Web UI：提供业务策略配置、通知发送等功能。* POP：POP生成策略脚本时，会通过该接口发送SOAP消息通知到UPCF。* CLI客户端：通过CLI/SCLI接口提供UPCF策略数据配置功能。

## 必备事项
前提条件

向系统管理员获取OM Portal帐号的密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_pmsadminip_list:
      type: items
      properties:
        IPID:
          name: 'IP地址索引'
          type: integer
          minimum: 1
          maximum: 256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NETMASK:
          name: '子网掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 48
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pmsadminip_list:
    - IPID: IP地址索引
      IPVER: IPV4
      IP: 'IPv4地址'
      NETMASK: '子网掩码'
      DESCRIPTION: '描述'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 配置UPCF Web UI接入PMS服务器的权限。

### 执行**ADD PMSADMINIP**命令，添加允许接入PMS服务器的IP地址。以参数“IPVER”值为“IPV4”为例：

```jinja2
{%- for item in add_pmsadminip_list -%}
    ADD PMSADMINIP:
    {#- --- 必选参数 --- -#}
    IPID={{item.IPID}},
    IPVER={{item.IPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.NETMASK is not none -%}
            NETMASK="{{item.NETMASK}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

