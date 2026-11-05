---
id: ''
name: 配置切片业务数据（UPF）
ne_type: UEG
type: feature
description: 本场景用于在UPF上配置切片相关的业务数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 网络切片发放（专网，入驻式）","通过CN NSSMF发放","切片发放操作","普通创建（新建NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（UPF）"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 网络切片发放（专线，共享式）","通过CN NSSMF发放","切片发放操作","普通创建（新建NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（UPF）"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 网络切片发放（云网，带计算）","通过CN NSSMF发放","切片发放操作","普通创建（新建NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在UPF上配置切片相关的业务数据。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_snssai_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置UPF支持的切片。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssaiupintf_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置切片和逻辑接口的绑定关系。   * 仅当需要支持N3接口隔离时需要配置。 * 参数“N3LOGICINF”不能为缺省N3口：n3if1/1/0。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N3LOGICINF:
          name: 'N3逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    lck_nf_list:
      type: items
      properties:
        LOCKSWITCH:
          name: 'NF锁定状态开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '当配置UPF锁定状态时，需执行此命令解锁UPF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_snssai_list:
    - SST: 1
      SD: '131313'
    add_snssaiupintf_list:
    - SST: 1
      SD: '131313'
      N3LOGICINF: 'N3IF1/1/1'
    lck_nf_list:
    - LOCKSWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置切片信息。

```jinja2
{%- for item in add_snssai_list -%}
    ADD SNSSAI:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 （可选）配置切片和N3接口绑定。

```jinja2
{%- if is_optional_snssai_n3_interface_binding -%}
    {%- for item in add_snssaiupintf_list -%}
        ADD SNSSAIUPINTF:
        {#- --- 必选参数 --- -#}
        SST={{item.SST}},
        N3LOGICINF="{{item.N3LOGICINF}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 （可选）配置UPF解锁状态。

```jinja2
{%- if is_optional_upf_unlock_state -%}
    {%- for item in lck_nf_list -%}
        LCK NF:
        {#- --- 必选参数 --- -#}
        LOCKSWITCH={{item.LOCKSWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

