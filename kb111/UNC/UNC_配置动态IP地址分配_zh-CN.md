---
id: ''
name: 配置动态IP地址分配
ne_type: UNC
type: feature
description: 使用专网UPF为UE动态分配IP地址的方式，可参考本页面完成专网SMF侧配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置SMF","配置地址分配","配置动态IP地址分配"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
使用专网UPF为UE动态分配IP地址的方式，可参考本页面完成专网SMF侧配置。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_addressattr_list:
      type: items
      properties:
        ALLOCPRECEDENCE:
          name: 'UE地址分配属性'
          type: string
          enum:
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: '配置分配主体为UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upipdomain_list:
      type: items
      properties:
        UPNODE:
          name: 'UPF节点标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '该参数需要与**ADD PNFPROFILE**命令的“NF实例标识”参数取值保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPDOMAIN:
          name: 'IP地址段归属的域'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNSWITCH:
          name: 'DNN开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: 'APN/DNN实例应该全网规划，SMF配置的APN/DNN实例应该与UPF配置的APN/DNN实例一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_addressattr_list:
    - ALLOCPRECEDENCE: UPF_FIRST
    add_upipdomain_list:
    - UPNODE: '5EA7F228-47CC-2032-03A3-0E1313000001'
      IPDOMAIN: 'APP-HDNJIHzjSMFm005BHW-07AHW012.hz.zj.hzupfm001bhw.CMIOTSXSZNSYHYW.ZJ'
      DNNSWITCH: ENABLE
      DNN: 'stjwt.gd'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在SMF上配置优先使用UPF分配地址。

```jinja2
{%- for item in set_addressattr_list -%}
    SET ADDRESSATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCPRECEDENCE is not none -%}
        ALLOCPRECEDENCE={{item.ALLOCPRECEDENCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 （可选）在现网可能存在不同的UPF为不同的UE分配相同的私网IP地址的情况，为防止PCF误判UE的IP地址冲突，导致正常的PDU会话被释放，SMF侧建议配置UPF的IPdomain，并通过Npcf\_SMPolicyControl\_Update Request消息将IPdomain和UE的IP地址传递给PCF。

```jinja2
{%- if is_optional_upf_ipdomain -%}
    {%- for item in add_upipdomain_list -%}
        ADD UPIPDOMAIN:
        {#- --- 必选参数 --- -#}
        UPNODE="{{item.UPNODE}}",
        IPDOMAIN="{{item.IPDOMAIN}}",
        DNNSWITCH={{item.DNNSWITCH}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DNNSWITCH=ENABLE 时必选 --- -#}
        {%- if item.DNNSWITCH == 'ENABLE' -%}
            DNN="{{item.DNN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

