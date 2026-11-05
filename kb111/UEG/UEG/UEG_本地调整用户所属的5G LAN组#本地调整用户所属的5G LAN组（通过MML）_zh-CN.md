---
id: ''
name: 本地调整用户所属的5G LAN组（通过MML）
ne_type: UEG
type: feature
description: 企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。  产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需要灵活调整时，可本地调整用户所属的5G LAN组。  本地调整用户所属的5G LAN组，指的是在SMF（UEG-L）上修改用户的5G LAN组。对于风筝L，优先使用SMF上设置的用户的5G LAN组。  * 仅UEG 风筝L支持本地调整用户所属的5G LAN组。 * 必须在UDM上先完成用户的5G LAN组签约，才支持本地调整该用户所属的5G LAN组。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","5G LAN用户本地签约配置（风筝L，通过WebPortal或MML调整）","本地调整用户所属的5G LAN组","本地调整用户所属的5G LAN组（通过MML）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需要灵活调整时，可本地调整用户所属的5G LAN组。本地调整用户所属的5G LAN组，指的是在SMF（UEG-L）上修改用户的5G LAN组。对于风筝L，优先使用SMF上设置的用户的5G LAN组。* 仅UEG 风筝L支持本地调整用户所属的5G LAN组。* 必须在UDM上先完成用户的5G LAN组签约，才支持本地调整该用户所属的5G LAN组。

## 必备事项
前提条件

* 5G LAN业务已交付且运行正常。
* 5G LAN用户在UDM上已完成5G LAN组签约，且存在调整所属5G LAN组的诉求。
* 操作员拥有相关MML的配置权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_rdsstaticippara_list:
      type: items
      properties:
        IMSI:
          name: '用户IMSI号'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: 'CPE（5G模组）/5G LAN终端（5G模组）的IMSI信息。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'CPE（5G模组）/5G LAN终端（5G模组）签约的APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV4V6
          - Ethernet
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: false
          description: '此处规划的是调整后的5G LAN组ID。   * 5G LAN用户激活在风筝L上时，在风筝L上执行**LST NGVNINSTANCE**获取5G LAN组ID（获取的5GLAN组ID来自UEG风筝L的UPF上已配置5GLAN组ID）。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_rdsstaticippara_list:
    - IMSI: '46000876543210'
      APN: 'dnn5glan01'
      ADDRTYPE: Ethernet
      GROUPID: '000003e9-460-08-01'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal。

### 2 进入“MML命令行-UEG”窗口。

#### 2.1 5G LAN用户已存在本地签约5G LAN组ID时，如需再次调整本地签约的5G LAN组ID，则须先删除用户本地签约的5G LAN组ID，然后再重新设置用户本地签约的5G LAN组ID。

#### 2.2 可参考验证方法中的1~2进行查询及删除。

### 3 执行**ADD RDSSTATICIPPARA**命令，设置用户本地签约的5G LAN组ID。

#### 3.1 //采用数据中的样例值时，配置脚本如下：

```jinja2
{%- for item in add_rdsstaticippara_list -%}
    ADD RDSSTATICIPPARA:
    {#- --- 必选参数 --- -#}
    IMSI="{{item.IMSI}}",
    APN="{{item.APN}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 5G LAN组ID: 条件必选(地址类型=Ethernet) / 条件可选(地址类型=IPV4|IPV6|IPV4V6) --- -#}
    {%- if (item.ADDRTYPE == 'Ethernet') -%}
        GROUPID="{{item.GROUPID}}",
    {%- elif (item.ADDRTYPE in ['IPV4', 'IPV6', 'IPV4V6']) -%}
        {%- if item.GROUPID is not none -%}
            GROUPID="{{item.GROUPID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 联系企业运维人员，将修改本地签约的5G LAN组ID的5G LAN用户重新接入网络。

### 修改本地签约的5G LAN组ID后，5G LAN用户必须重新接入网络，否则本地签约的5G LAN组ID不生效。

