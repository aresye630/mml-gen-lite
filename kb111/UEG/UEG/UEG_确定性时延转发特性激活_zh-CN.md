---
id: GWFD-031102
name: 确定性时延转发特性激活
ne_type: UEG
type: feature
description: 在UEG需要控制确定性时延转发，需要配置低时延转发功能。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-031102 确定性时延转发","GWFD-031102 确定性时延转发","确定性时延转发特性激活"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG需要控制确定性时延转发，需要配置低时延转发功能。适用于UPF。

## 必备事项
前提条件

前提条件

* 请仔细阅读确定性时延转发特性概述。
* UEG完成与周边网元的对接。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    set_deepisosw_list:
      type: items
      properties:
        SWITCH:
          name: '转发线程深度隔离开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '指定系统转发核是否需要开启转发线程深度隔离。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_batchpara_list:
      type: items
      properties:
        STAGENAME:
          name: '数据转发阶段名称'
          type: string
          enum:
          - FASTSTAGE
          - CPLXSTAGE
          - SQTLSTAGE
          required: true
          description: '指定数据转发阶段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXREADTIMES:
          name: '最大读取报文次数'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '设置最大读取报文次数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXREADNUM:
          name: '最大读取报文数目'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '设置最大读取报文数目。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5DLAF01'
      SWITCH: ENABLE
    set_deepisosw_list:
    - SWITCH: ENABLE
    set_batchpara_list:
    - STAGENAME: FASTSTAGE
      MAXREADTIMES: 2
      MAXREADNUM: 128
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

### **SET LICENSESWITCH**

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 打开转发线程深度隔离开关。

### **SET DEEPISOSW**

```jinja2
{%- for item in set_deepisosw_list -%}
    SET DEEPISOSW:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 确认转发线程深度隔离开关已开启。

### **DSP DEEPISOSWINFO**

### 请在执行**DSP DEEPISOSWINFO**后3分钟左右再进行下一步。

### 4 重启设备。该操作请联系华为技术支持。

### 5 （可选）设置批量处理的报文数量。

### **SET BATCHPARA**

```jinja2
{%- if is_optional_set_batch_packet_count -%}
    {%- for item in set_batchpara_list -%}
        SET BATCHPARA:
        {#- --- 必选参数 --- -#}
        STAGENAME={{item.STAGENAME}},
        {#- --- 可选参数 --- -#}
        {%- if item.MAXREADTIMES is not none -%}
            MAXREADTIMES={{item.MAXREADTIMES}},
        {%- endif -%}
        {%- if item.MAXREADNUM is not none -%}
            MAXREADNUM={{item.MAXREADNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 批量处理的报文数量越小，对CPU影响越大，请根据具体使用场景合理设置转发报文数量。

