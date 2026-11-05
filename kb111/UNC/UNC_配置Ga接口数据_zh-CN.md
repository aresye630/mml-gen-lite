---
id: ''
name: 配置Ga接口数据
ne_type: UNC
type: feature
description: 该任务用于指导工程师完成Ga口的IP资源数据的配置。该章节仅针对于组网场景有Ga接口的计费方案。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","NCG配置","配置Ga接口数据"]
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
          minLength: 1
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
          maxLength: 32
          required: true
          description: '该命令用于增加话单处理所需要的格式引擎包。'
          data_source: ''
          pattern: ''
          default: ''
        PRFNAME:
          name: '格式引擎包名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHAREFILECSN:
          name: '共享第二份最终话单文件序列号'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        SEQNUMMODE:
          name: '序列号模式'
          type: string
          enum:
          - HEAD
          - IE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IE
    add_module_list:
      type: items
      properties:
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: true
          description: '该命令用于配置实现话单接收，分拣，转换，存储功能的模块。'
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: true
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
          maxLength: 32
          required: true
          description: '该命令用于配置原始话单、第一份最终话单以及第二份最终话单以及可能重复帧的存储规则。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - No
          - Yes
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: No
        FILETYPE:
          name: '话单文件类型'
          type: string
          enum:
          - AllCDRFiles
          - FirstFinal
          - Original
          - PotentialDup
          - SecondFinal
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYS:
          name: '第一份最终话单文件保存天数'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 7
        FCMRRULE:
          name: '第一份最终话单文件压缩方式'
          type: string
          enum:
          - GZIP
          - UNCOMPRESS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GZIP
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
        CLOSEFILECOND:
          name: '话单文件关闭方式'
          type: string
          enum:
          - ByInterval
          - ByNumber
          - BySize
          - Unspecify
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Unspecify
        SFCDRSIZE:
          name: '按大小生成最终话单文件(KB)'
          type: integer
          minimum: 64
          maximum: 51200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1024
        NAMINGRULE:
          name: '最终话单文件名命名规则'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BIFILETYPE:
          name: '话单文件类型'
          type: string
          enum:
          - AllCDRFiles
          - FirstFinal
          - Original
          - PotentialDup
          - SecondFinal
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRATTIME:
          name: '在指定时间点生成最终话单文件'
          type: string
          maxLength: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRINTERV:
          name: '按时间间隔生成最终话单文件(秒)'
          type: integer
          minimum: 5
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        CDRNUMBER:
          name: '按话单条数生成最终话单文件'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CDRSIZE:
          name: '按大小生成原始话单文件(KB)'
          type: integer
          minimum: 512
          maximum: 20480
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1024
        CDRSTORDELTASKSLEEPTIME:
          name: '删除任务休眠时间'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        CDRSTORDELTASKSTARTTIME:
          name: '删除任务开始时间'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '02:00'
        CMRRULE:
          name: '原始话单文件压缩方式'
          type: string
          enum:
          - UNCOMPRESS
          - ZLIB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ZLIB
        EMPTYFILE:
          name: '是否生成空话单文件'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ENDSN:
          name: '最终话单文件名的最大序列号'
          type: integer
          minimum: 0
          maximum: 999999999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 999999999
        FSTORDAYSRULE:
          name: '第一份最终话单文件保存天数方式'
          type: string
          enum:
          - ByAbsoluteDays
          - ByRelativeDays
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ByRelativeDays
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NUMSCHSN:
          name: '序列号编号规则'
          type: string
          enum:
          - DAY
          - MONTH
          - NO
          - YEAR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        PDDESTPATH:
          name: '可能重复帧保存路径'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SFCMRRULE:
          name: '第二份最终话单文件压缩方式'
          type: string
          enum:
          - GZIP
          - UNCOMPRESS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: UNCOMPRESS
        SFSTORDAYS:
          name: '第二份最终话单文件保存天数'
          type: integer
          minimum: 0
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SFSTORDAYSRULE:
          name: '第二份最终话单文件保存天数方式'
          type: string
          enum:
          - ByAbsoluteDays
          - ByRelativeDays
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ByRelativeDays
        STARTSN:
          name: '最终话单文件名的起始序列号'
          type: integer
          minimum: 0
          maximum: 999999999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
        STORDAYS:
          name: '原始话单文件保存天数'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 7
        STORDAYSRULE:
          name: '原始话单文件保存天数方式'
          type: string
          enum:
          - ByAbsoluteDays
          - ByRelativeDays
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ByRelativeDays
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'Ga-test'
    add_cdrproc_list:
    - AGID: 'group1'
      PRFNAME: 'PS_R9_V940_huawei_test.tar.gz'
      SHAREFILECSN: OFF
      SEQNUMMODE: IE
    add_module_list:
    - MNAME: 'AP64_1'
      AGID: 'group1'
    add_cdrstor_list:
    - CDRSTORID: 'OriginalCDR'
      ISSINGLEBI: No
      FILETYPE: Original
      FSTORDAYS: 8
      FCMRRULE: GZIP
      AGID: 'PS_GROUP_1'
      CHLNAME: 'All'
      CLOSEFILECOND: BySize
      SFCDRSIZE: 2048
      NAMINGRULE: 'bABC%08L%A.dat'
      BIFILETYPE: ''
      CDRATTIME: ''
      CDRINTERV: 1800
      CDRNUMBER: ''
      CDRSIZE: 1024
      CDRSTORDELTASKSLEEPTIME: 20
      CDRSTORDELTASKSTARTTIME: '02:00'
      CMRRULE: ZLIB
      EMPTYFILE: NO
      ENDSN: 999999999
      FSTORDAYSRULE: ByRelativeDays
      MNAME: ''
      NUMSCHSN: NO
      PDDESTPATH: ''
      SFCMRRULE: UNCOMPRESS
      SFSTORDAYS: ''
      SFSTORDAYSRULE: ByRelativeDays
      STARTSN: 1
      STORDAYS: 7
      STORDAYSRULE: ByRelativeDays
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
{%- for item in add_cdrproc_list -%}
    ADD CDRPROC:
    {#- --- 必选参数 --- -#}
    AGID="{{item.AGID}}",
    PRFNAME="{{item.PRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SHAREFILECSN is not none -%}
        SHAREFILECSN={{item.SHAREFILECSN}},
    {%- endif -%}
    {%- if item.SEQNUMMODE is not none -%}
        SEQNUMMODE={{item.SEQNUMMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Ga接口接入网元分组。

```jinja2
{%- for item in add_module_list -%}
    ADD MODULE:
    {#- --- 必选参数 --- -#}
    MNAME="{{item.MNAME}}",
    AGID="{{item.AGID}}",
    ;
{%- endfor -%}
```

### MNAME目前仅支持APXX\_Y命名，XX为RUID。

### 4 配置话单存储规则。

```jinja2
{%- for item in add_cdrstor_list -%}
    ADD CDRSTOR:
    {#- --- 必选参数 --- -#}
    CDRSTORID="{{item.CDRSTORID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ISSINGLEBI is not none -%}
        ISSINGLEBI={{item.ISSINGLEBI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ISSINGLEBI=No 时必选 --- -#}
    {%- if item.ISSINGLEBI == 'No' -%}
        FILETYPE={{item.FILETYPE}},
    {%- endif -%}
    {#- --- 条件必选：BIFILETYPE=SecondFinal/PotentialDup 时必选 --- -#}
    {%- if item.BIFILETYPE in ['SecondFinal', 'PotentialDup'] -%}
        AGID="{{item.AGID}}",
    {#- --- 条件必选：FILETYPE=SecondFinal/PotentialDup 时必选 --- -#}
    {%- elif item.FILETYPE in ['SecondFinal', 'PotentialDup'] -%}
        AGID="{{item.AGID}}",
    {%- endif -%}
    {#- --- 条件必选：ISSINGLEBI=Yes 时必选 --- -#}
    {%- if item.ISSINGLEBI == 'Yes' -%}
        BIFILETYPE={{item.BIFILETYPE}},
    {%- endif -%}
    {#- --- 条件必选：BIFILETYPE=PotentialDup 时必选 --- -#}
    {%- if item.BIFILETYPE == 'PotentialDup' -%}
        PDDESTPATH="{{item.PDDESTPATH}}",
    {#- --- 条件必选：FILETYPE=PotentialDup 时必选 --- -#}
    {%- elif item.FILETYPE == 'PotentialDup' -%}
        PDDESTPATH="{{item.PDDESTPATH}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BIFILETYPE=FirstFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'FirstFinal' -%}
        {%- if item.FSTORDAYS is not none -%}
            FSTORDAYS={{item.FSTORDAYS}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=FirstFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'FirstFinal' -%}
        {%- if item.FSTORDAYS is not none -%}
            FSTORDAYS={{item.FSTORDAYS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=FirstFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'FirstFinal' -%}
        {%- if item.FCMRRULE is not none -%}
            FCMRRULE={{item.FCMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=FirstFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'FirstFinal' -%}
        {%- if item.FCMRRULE is not none -%}
            FCMRRULE={{item.FCMRRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.CHLNAME is not none -%}
            CHLNAME="{{item.CHLNAME}}",
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.CHLNAME is not none -%}
            CHLNAME="{{item.CHLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.CLOSEFILECOND is not none -%}
            CLOSEFILECOND={{item.CLOSEFILECOND}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.CLOSEFILECOND is not none -%}
            CLOSEFILECOND={{item.CLOSEFILECOND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.SFCDRSIZE is not none -%}
            SFCDRSIZE={{item.SFCDRSIZE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.SFCDRSIZE is not none -%}
            SFCDRSIZE={{item.SFCDRSIZE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.NAMINGRULE is not none -%}
            NAMINGRULE="{{item.NAMINGRULE}}",
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.NAMINGRULE is not none -%}
            NAMINGRULE="{{item.NAMINGRULE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.CDRATTIME is not none -%}
            CDRATTIME="{{item.CDRATTIME}}",
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.CDRATTIME is not none -%}
            CDRATTIME="{{item.CDRATTIME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.CDRINTERV is not none -%}
            CDRINTERV={{item.CDRINTERV}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.CDRINTERV is not none -%}
            CDRINTERV={{item.CDRINTERV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.CDRNUMBER is not none -%}
            CDRNUMBER={{item.CDRNUMBER}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.CDRNUMBER is not none -%}
            CDRNUMBER={{item.CDRNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=Original 时可选 --- -#}
    {%- if item.BIFILETYPE == 'Original' -%}
        {%- if item.CDRSIZE is not none -%}
            CDRSIZE={{item.CDRSIZE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=Original 时可选 --- -#}
    {%- elif item.FILETYPE == 'Original' -%}
        {%- if item.CDRSIZE is not none -%}
            CDRSIZE={{item.CDRSIZE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=AllCDRFiles 时可选 --- -#}
    {%- if item.BIFILETYPE == 'AllCDRFiles' -%}
        {%- if item.CDRSTORDELTASKSLEEPTIME is not none -%}
            CDRSTORDELTASKSLEEPTIME={{item.CDRSTORDELTASKSLEEPTIME}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=AllCDRFiles 时可选 --- -#}
    {%- elif item.FILETYPE == 'AllCDRFiles' -%}
        {%- if item.CDRSTORDELTASKSLEEPTIME is not none -%}
            CDRSTORDELTASKSLEEPTIME={{item.CDRSTORDELTASKSLEEPTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=AllCDRFiles 时可选 --- -#}
    {%- if item.BIFILETYPE == 'AllCDRFiles' -%}
        {%- if item.CDRSTORDELTASKSTARTTIME is not none -%}
            CDRSTORDELTASKSTARTTIME="{{item.CDRSTORDELTASKSTARTTIME}}",
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=AllCDRFiles 时可选 --- -#}
    {%- elif item.FILETYPE == 'AllCDRFiles' -%}
        {%- if item.CDRSTORDELTASKSTARTTIME is not none -%}
            CDRSTORDELTASKSTARTTIME="{{item.CDRSTORDELTASKSTARTTIME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=Original 时可选 --- -#}
    {%- if item.BIFILETYPE == 'Original' -%}
        {%- if item.CMRRULE is not none -%}
            CMRRULE={{item.CMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=Original 时可选 --- -#}
    {%- elif item.FILETYPE == 'Original' -%}
        {%- if item.CMRRULE is not none -%}
            CMRRULE={{item.CMRRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.EMPTYFILE is not none -%}
            EMPTYFILE={{item.EMPTYFILE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.EMPTYFILE is not none -%}
            EMPTYFILE={{item.EMPTYFILE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.ENDSN is not none -%}
            ENDSN={{item.ENDSN}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.ENDSN is not none -%}
            ENDSN={{item.ENDSN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=FirstFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'FirstFinal' -%}
        {%- if item.FSTORDAYSRULE is not none -%}
            FSTORDAYSRULE={{item.FSTORDAYSRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=FirstFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'FirstFinal' -%}
        {%- if item.FSTORDAYSRULE is not none -%}
            FSTORDAYSRULE={{item.FSTORDAYSRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.NUMSCHSN is not none -%}
            NUMSCHSN={{item.NUMSCHSN}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.NUMSCHSN is not none -%}
            NUMSCHSN={{item.NUMSCHSN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.SFCMRRULE is not none -%}
            SFCMRRULE={{item.SFCMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.SFCMRRULE is not none -%}
            SFCMRRULE={{item.SFCMRRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.FILETYPE == 'SecondFinal' -%}
        {%- if item.SFSTORDAYS is not none -%}
            SFSTORDAYS={{item.SFSTORDAYS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.SFSTORDAYSRULE is not none -%}
            SFSTORDAYSRULE={{item.SFSTORDAYSRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.SFSTORDAYSRULE is not none -%}
            SFSTORDAYSRULE={{item.SFSTORDAYSRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=SecondFinal 时可选 --- -#}
    {%- if item.BIFILETYPE == 'SecondFinal' -%}
        {%- if item.STARTSN is not none -%}
            STARTSN={{item.STARTSN}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.STARTSN is not none -%}
            STARTSN={{item.STARTSN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=Original 时可选 --- -#}
    {%- if item.BIFILETYPE == 'Original' -%}
        {%- if item.STORDAYS is not none -%}
            STORDAYS={{item.STORDAYS}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=Original 时可选 --- -#}
    {%- elif item.FILETYPE == 'Original' -%}
        {%- if item.STORDAYS is not none -%}
            STORDAYS={{item.STORDAYS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BIFILETYPE=Original 时可选 --- -#}
    {%- if item.BIFILETYPE == 'Original' -%}
        {%- if item.STORDAYSRULE is not none -%}
            STORDAYSRULE={{item.STORDAYSRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=Original 时可选 --- -#}
    {%- elif item.FILETYPE == 'Original' -%}
        {%- if item.STORDAYSRULE is not none -%}
            STORDAYSRULE={{item.STORDAYSRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 模块名: 条件必选(话单文件类型=PotentialDup; 话单文件类型=PotentialDup) / 条件可选(话单文件类型=SecondFinal) --- -#}
    {%- if (item.BIFILETYPE == 'PotentialDup') or (item.FILETYPE == 'PotentialDup') -%}
        MNAME="{{item.MNAME}}",
    {%- elif (item.FILETYPE == 'SecondFinal') -%}
        {%- if item.MNAME is not none -%}
            MNAME="{{item.MNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 存储天数和文件命名规则要根据规划填写，以上只是样例。

