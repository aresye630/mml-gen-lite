---
id: ''
name: 安装后配置
ne_type: UEG
type: feature
description: VNF安装完成后，需要配置部分数据，确保系统正常工作。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG软件安装（风筝M）","安装MPF（独立部署）","基于NFVO安装MPF（非SDN）","安装后配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
VNF安装完成后，需要配置部分数据，确保系统正常工作。

## 必备事项
前提条件

已实例化网元。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_virtualip_list:
      type: items
      properties:
        IPTYPE:
          name: '浮动IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4GW:
          name: 'IPv4网关'
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
  examples:
    mod_virtualip_list:
    - IPTYPE: IPv4
      IPV4ADDR: '10.145.27.173'
      IPV4GW: '10.145.27.1'
      NETMASK: '255.255.255.0'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UEG OM portal。

### 2 请参见《UEG安全配置》，对系统进行安全配置，修改系统默认帐号密码。

### 3 在UEG OM portal，选择“监控分析 > 告警管理 > 活动告警”，查看系统是否上报告警“ALM-135301 PaasBroker和FusionStage的通信失败”。

#### 3.1 是 => 步骤4。

#### 3.2 否 => 步骤5。

### 4 处理ALM-135301 PaasBroker和FusionStage的通信失败告警。

### 5 **仅当**网元已经实例化，且OM操作维护IP（即OM浮动IP）的规划值已被更改时，才需要修改OM操作维护IP地址。示例如下：

```jinja2
{%- for item in mod_virtualip_list -%}
    MOD VIRTUALIP:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4GW="{{item.IPV4GW}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        NETMASK="{{item.NETMASK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 执行该命令会导致UEG OM Portal的连接中断。

### 此时需要调整本地PC IP，与新的UEG的OM操作维护IP正常通信后，再重新登录UEG OM Portal。

### 对于同网段IP，可以使用MOD VIRTUALIP/SET OMIP修改OM IP；对于不同网段的OM IP调整，请联系华为技术支持工程师处理或参考《修改OMU IP指导书》。

