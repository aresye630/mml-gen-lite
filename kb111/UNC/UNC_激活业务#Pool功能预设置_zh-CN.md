---
id: ''
name: Pool功能预设置
ne_type: UNC
type: feature
description: 新建MME Pool时对本Pool的功能和参数按前期规划好的数据进行配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","新建部署","全网新建Pool","激活业务","Pool功能预设置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
新建MME Pool时对本Pool的功能和参数按前期规划好的数据进行配置。

## 必备事项
前提条件

* MME网元已经接入到U2020/MAE的操作维护系统，操作人员已经登录U2020/MAE服务器。

  U2020/MAE的操作步骤具体请参见《U2020 MBB网络管理系统 虚拟化产品文档》（“安装与调测 > U2020 虚拟化集群系统调测指南 > 集成核心网和无线接入网网元到U2020”章节）/《iMaster MAE产品文档》（“安装与调测 > MAE调测指南 > 调测MAE-Access > 集成核心网和无线接入网网元到MAE”章节）。
* 网元基础数据配置完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_mmeid_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码（起始值）'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    act_license_list:
      type: items
      properties:
        FN:
          name: 'License文件名称'
          type: string
          maxLength: 311
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sys_list:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_mmeid_list:
    - MCC: '123'
      MNC: '00'
      MMEGI: '8001'
      MMEC: '8'
    act_license_list:
    - FN: 'LIC4MMEPOOL.xml'
    set_licenseswitch_list:
    - LICITEM: 'LKV2POOL02'
      SWITCH: ENABLE
    set_sys_list:
    - CAP: 100
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在MME上增加MMEID。

```jinja2
{%- for item in add_mmeid_list -%}
    ADD MMEID:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

### 2 申请并加载具有MME Pool功能的License和具有MME Pool用户迁移功能（可选）的License。

```jinja2
{%- for item in act_license_list -%}
    ACT LICENSE:
    {#- --- 必选参数 --- -#}
    FN="{{item.FN}}",
    ;
{%- endfor -%}
```

### 3 在所有MME上打开MME Pool开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 在MME1上配置本MME的权重信息。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

