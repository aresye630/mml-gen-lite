---
id: ''
name: 配置5G服务区域
ne_type: UNC
type: feature
description: 指定UPF支持的服务范围时需要以服务区域为粒度进行分配，因此需增加UPF服务区域，以及UPF服务区名称绑定的5G TAI范围，最后规划对端UPF实例支持的为SMF提供服务区域的信息，将对应的跟踪区添加到UPF的服务区中，使得SMF可以正确选择UPF。若SMF不配置UPF服务区，则不会将对应的跟踪区绑定到UPF，最终导致SMF没有可用UPF资源，附着失败。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","配置SMF","配置5G服务区域"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
指定UPF支持的服务范围时需要以服务区域为粒度进行分配，因此需增加UPF服务区域，以及UPF服务区名称绑定的5G TAI范围，最后规划对端UPF实例支持的为SMF提供服务区域的信息，将对应的跟踪区添加到UPF的服务区中，使得SMF可以正确选择UPF。若SMF不配置UPF服务区，则不会将对应的跟踪区绑定到UPF，最终导致SMF没有可用UPF资源，附着失败。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF位置区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '增加UPF服务区名称绑定的5G TAI范围。该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为N2TAI。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: 'TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: 'TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置用户面节点为SMF提供的服务区域。“SMFSERVINGAREA”与**ADD UPAREA中的**“AREANAME”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_locbindarea_list:
      type: items
      properties:
        LOCALITY:
          name: 'UPF位置区'
          type: string
          minLength: 0
          maxLength: 150
          required: true
          description: '配置UPF位置信息与该UPF优选支持的服务区的绑定关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_uparea_list:
    - AREANAME: 'area1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'area1'
      N2BEGINTAI: '12300000001'
      N2ENDTAI: '1230000001F'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_1'
      SMFSERVINGAREA: 'area1'
    add_locbindarea_list:
    - LOCALITY: 'locality1'
      AREANAME: 'area1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UPF Service Area。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

### 2 配置UPF Service Area对应的TAI。

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

### 3 配置UPF服务的SMF Service Area。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 4 配置UPF位置信息与该UPF优选支持的服务区的绑定关系。

```jinja2
{%- for item in add_locbindarea_list -%}
    ADD LOCBINDAREA:
    {#- --- 必选参数 --- -#}
    LOCALITY="{{item.LOCALITY}}",
    AREANAME="{{item.AREANAME}}",
    ;
{%- endfor -%}
```

