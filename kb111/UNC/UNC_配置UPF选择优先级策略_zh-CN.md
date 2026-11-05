---
id: ''
name: 配置UPF选择优先级策略
ne_type: UNC
type: feature
description: SMF/PGW-C/SGW-C/GGSN选择UPF先根据选择UPF的**必选条件**选择UPF，再根据选择UPF的**优选条件**选择UPF，确定最终选择的UPF。  更多UPF选择内容请参考UPF选择专题。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置和UPF的对接（N4/Sxa/Sxb）","配置N4接口","配置UPF选择优先级策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
SMF/PGW-C/SGW-C/GGSN选择UPF先根据选择UPF的**必选条件**选择UPF，再根据选择UPF的**优选条件**选择UPF，确定最终选择的UPF。更多UPF选择内容请参考UPF选择专题。

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
    set_upselectflag_list:
      type: items
      properties:
        LOCALITYFLAG:
          name: '位置区UPF优选开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置UPF选择条件开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upselectflag_list_1:
      type: items
      properties:
        PSAPOSPRIFLAG:
          name: '基于位置优选主锚点UPF开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upselectpri_list:
      type: items
      properties:
        FIRSTPRIORITY:
          name: '第一优先级'
          type: string
          enum:
          - Combined
          - LocS11Priority
          - Load
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDPRIORITY:
          name: '第二优先级'
          type: string
          enum:
          - Combined
          - LocS11Priority
          - Load
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THIRDPRIORITY:
          name: '第三优先级'
          type: string
          enum:
          - Combined
          - LocS11Priority
          - Load
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_upselectflag_list:
    - LOCALITYFLAG: ENABLE
    set_upselectflag_list_1:
    - PSAPOSPRIFLAG: ENABLE
    set_upselectpri_list:
    - FIRSTPRIORITY: Combined
      SECONDPRIORITY: LocS11Priority
      THIRDPRIORITY: Load
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UPF选择优先级(5G)。

#### 1.1 //（可选）配置UPF服务的位置区域关联关系。

### 对于省内部署了多个覆盖全省或者覆盖多个地市的中心UPF，但是每个UPF又规划为针对单个地市做位置优选时，才可以采用该locality方式做位置优选。

### 针对SMF/PGW-C/SGW-C/GGSN对PGW-U和GGSN-U的位置优选，推荐LOCALITY绑定方式。SMF直接基于LOCALITY优选锚点UPF的前提是ADD PNFSMFSERAREA、ADD UPAREABINDLAI、ADD UPAREABINDS1TAI、ADD UPAREABINDN2TAI配置了各个地市UPF的覆盖服务范围。

```jinja2
{%- if is_optional_upf_service_location_area_association -%}
    {%- for item in set_upselectflag_list -%}
        SET UPSELECTFLAG:
        {#- --- 可选参数 --- -#}
        {%- if item.LOCALITYFLAG is not none -%}
            LOCALITYFLAG={{item.LOCALITYFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置SMF/PGW-C/SGW-C/GGSN选择锚点UPF时根据位置区做优选，包括4G激活时选择PGW-U，以及2G激活时选择GGSN-U。

```jinja2
{%- for item in set_upselectflag_list_1 -%}
    SET UPSELECTFLAG:
    {#- --- 可选参数 --- -#}
    {%- if item.PSAPOSPRIFLAG is not none -%}
        PSAPOSPRIFLAG={{item.PSAPOSPRIFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SMF/PGW-C/SGW-C/GGSN选择UPF的优先级。

```jinja2
{%- for item in set_upselectpri_list -%}
    SET UPSELECTPRI:
    {#- --- 可选参数 --- -#}
    {%- if item.FIRSTPRIORITY is not none -%}
        FIRSTPRIORITY={{item.FIRSTPRIORITY}},
    {%- endif -%}
    {%- if item.SECONDPRIORITY is not none -%}
        SECONDPRIORITY={{item.SECONDPRIORITY}},
    {%- endif -%}
    {%- if item.THIRDPRIORITY is not none -%}
        THIRDPRIORITY={{item.THIRDPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

