---
id: ''
name: 配置Ga接口数据
ne_type: UDG
type: feature
description: 该任务用于指导工程师完成Ga口的IP资源数据的配置。该章节仅针对于组网场景有Ga接口的计费方案。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","NCG配置","配置Ga接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于指导工程师完成Ga口的IP资源数据的配置。该章节仅针对于组网场景有Ga接口的计费方案。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该命令用于创建指定的VPN实例。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
    add_cdrproc_list:
      type: items
      properties:
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '该命令用于增加话单处理所需要的格式引擎包。'
          data_source: ''
          pattern: ''
          default: ''
        PRFNAME:
          name: '格式引擎包名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHAREFILECSN:
          name: '共享第二份最终话单文件序列号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEQNUMMODE:
          name: '序列号模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_module_list:
      type: items
      properties:
        MNAME:
          name: '模块名'
          type: string
          required: false
          description: '该命令用于配置实现话单接收，分拣，转换，存储功能的模块。'
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cdrstor_list:
      type: items
      properties:
        CDRSTORID:
          name: '话单存储标识'
          type: string
          required: false
          description: '该命令用于配置原始话单、第一份最终话单以及第二份最终话单以及可能重复帧的存储规则。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILETYPE:
          name: '话单文件类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYS:
          name: 'FSTORDAYS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FCMRRULE:
          name: 'FCMRRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: 'AGID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: 'CHLNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLOSEFILECOND:
          name: 'CLOSEFILECOND'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SFCDRSIZE:
          name: 'SFCDRSIZE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAMINGRULE:
          name: 'NAMINGRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'Ga-test'
    add_cdrproc_list:
    - AGID: group1
      PRFNAME: PS_R9_V940_huawei_test.tar.gz
      SHAREFILECSN: OFF
      SEQNUMMODE: IE
    add_module_list:
    - MNAME: AP64_1
      AGID: group1
    add_cdrstor_list:
    - CDRSTORID: OriginalCDR
      ISSINGLEBI: No
      FILETYPE: Original
      FSTORDAYS: '8'
      FCMRRULE: GZIP
      AGID: PS_GROUP_1
      CHLNAME: All
      CLOSEFILECOND: BySize
      SFCDRSIZE: '2048'
      NAMINGRULE: bABC%08L%A.dat
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置Ga接口信令的VPN。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 2 配置Ga接口话单处理，加载格式引擎包。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrproc_list的变量区（command: ADD CDRPROC） -#}
<!-- MISSING_MACRO: command=ADD CDRPROC list_name=add_cdrproc_list step_id=2 -->
```

### 3 配置Ga接口接入网元分组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_module_list的变量区（command: ADD MODULE） -#}
<!-- MISSING_MACRO: command=ADD MODULE list_name=add_module_list step_id=3 -->
```

### MNAME目前仅支持APXX\_Y命名，XX为RUID。

### 4 配置话单存储规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrstor_list的变量区（command: ADD CDRSTOR） -#}
<!-- MISSING_MACRO: command=ADD CDRSTOR list_name=add_cdrstor_list step_id=4 -->
```

### 存储天数和文件命名规则要根据规划填写，以上只是样例。

