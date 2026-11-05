---
id: ''
name: 离线计费配置（2/3G）
ne_type: UNC
type: feature
description: 配置2/3G离线计费（NCG通过Ga接口和GGSN-C对接）话单处理参数。该章节仅针对于组网场景有Ga接口的计费方案。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","NCG配置","离线计费配置（2/3G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
配置2/3G离线计费（NCG通过Ga接口和GGSN-C对接）话单处理参数。该章节仅针对于组网场景有Ga接口的计费方案。

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
    add_cdrproc_list:
      type: items
      properties:
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRFNAME:
          name: '格式引擎包名'
          type: string
          maxLength: 255
          required: true
          description: '+ 格式引擎包文件全名，包括后缀名。例如，“PS\_R6\_V660\_CMCC\_NEW.tar.gz”。 + 不同的局点话单处理规则不同，需要根据实际情况配置相应的格式引擎包。 + 该参数只能由字母、数字、下划线、点组成。'
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
    add_fmtpkgcfg_list:
      type: items
      properties:
        PRFNAME:
          name: '格式引擎包名'
          type: string
          maxLength: 255
          required: true
          description: '“PRFNAME”可以通过**LST CDRPROC**命令查询获取。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFGNAME:
          name: '格式引擎包软参名称'
          type: string
          maxLength: 255
          required: true
          description: '“CFGNAME”可以通过**DSP FMTSOFTPARA**命令获取，其他名称无法生效。  说明：  不同的格式引擎包对软参的支持情况可能不同，可以通过**DSP FMTSOFTPARA**命令查询对应格式引擎包可配置的软参。'
          data_source: ''
          pattern: ''
          default: ''
        CFGTYPE:
          name: '格式引擎软参类型'
          type: string
          enum:
          - FEM_PARA_ENUM
          - FEM_PARA_IPADDR
          - FEM_PARA_STRING
          - FEM_PARA_UINT
          required: true
          description: '需与“CFGNAME”对应的“格式引擎包软参类型”匹配，“格式引擎包软参类型”可以通过**DSP FMTSOFTPARA**命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        CFG_UINT_VALUE:
          name: '格式引擎软参值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '“CFG\_UINT\_VALUE”在“CFGNAME”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过**DSP FMTSOFTPARA**命令查询获取。  说明：  软参取值请根据业务实际需要进行配置。'
          data_source: ''
          pattern: ''
          default: 0
        CFG_BOOL_VALUE:
          name: '格式引擎软参值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CFG_IP_VALUE:
          name: '格式引擎软参值'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFG_STR_VALUE:
          name: '格式引擎软参值'
          type: string
          maxLength: 512
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
          maxLength: 15
          required: true
          description: '首先执行**LST SERVICERUSTATE**命令，查询出当前的RUID。该参数输入格式固定为''AP''接RUID\_APID，APID值为1~4。例如：RUID为64时，该参数可以是“AP64\_1”、“AP64\_2”、“AP64\_3”、“AP64\_4”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: true
          description: '+ 该值需要执行**LST CDRPROC**命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行**ADD CDRPROC**命令增加。'
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
          description: '-'
          data_source: '本端规划'
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
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
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
        NAMINGRULE:
          name: '最终话单文件名命名规则'
          type: string
          maxLength: 128
          required: false
          description: '+ 默认最终话单文件名的配置为“b%08L.dat”，默认的话单文件名为b00000001.dat～b99999999.dat。 + 当“第二份最终话单文件压缩方式”的值为“GZIP”时，需要手动地增加压缩后缀，否则，第二份最终话单文件名中不显示压缩后缀。 + 该参数不能包含“/、\、\*、>、<、|”。 + 最终话单文件的命名规则建议默认增加 "%B" 的描述，否则BOSS获取话单存在重名风险。 + 当本地备份分发ADD CDRDISTR的可选项ISADDAPNAME选否以及模块名填 "AP\_ALL"，第二份最终话单的命名规则必须是带有"%B"的正则表达式。 + 不能输入的特殊字符请参考**ADD CDRSTOR**命令的“**特殊字符表**”。'
          data_source: ''
          pattern: ''
          default: ''
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
        STORDAYS:
          name: '原始话单文件保存天数'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: '+ 原始话单储存天数。超过此期限的话单，CG会将其删除。需根据当前局点要求，对此参数进行修改。 + 删除原始话单之前，系统会检查一下该话单是否被处理过，如果没有被处理，超过了期限的话单也不会被删除掉。但是原始话单文件保存天数方式为“按绝对天数”时，没有被处理但是超过期限也会被删除，因此原始话单文件保存天数方式为“按绝对天数”时，原始话单保存天数不允许小于3天。 + 当磁盘剩余空间小于自动清理话单的磁盘空间阈值时，系统为了保证业务的正常运行，会自动清理话单。清理的顺序为首先清理第一份最终话单，之后清理原始话单。但是清理之后，第一份最终话单和原始话单最少保证各有七天的话单。   - 当系统为单分区版本时，话单清理的磁盘剩余空间阈值为800MB。   - 当系统为多分区版本时，话单清理的磁盘剩余空间阈值为600MB。'
          data_source: ''
          pattern: ''
          default: 7
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
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
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
        PDDESTPATH:
          name: '可能重复帧保存路径'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_actrl_list:
      type: items
      properties:
        ACID:
          name: '接入控制标识'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: true
          description: '与**ADD MODULE**，**ADD CDRSTOR**中配置保持一致。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        IPRID:
          name: 'IP资源标识'
          type: string
          maxLength: 32
          required: true
          description: '与**ADD IPRESOURCE**中配置保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: '建议配置的端口号大于1024，防止和操作系统使用的端口号冲突。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_cdrproc_list:
    - AGID: 'PS3'
      PRFNAME: 'PS_R6_V660_CMCC_NEW.tar.gz'
      SHAREFILECSN: OFF
      SEQNUMMODE: IE
    add_fmtpkgcfg_list:
    - PRFNAME: 'PS_R6_V660_CMCC_NEW.tar.gz'
      CFGNAME: 'MaxDuration'
      CFGTYPE: FEM_PARA_UINT
      CFG_UINT_VALUE: 0
      CFG_BOOL_VALUE: ''
      CFG_IP_VALUE: ''
      CFG_STR_VALUE: ''
    add_module_list:
    - MNAME: 'AP64_3'
      AGID: 'PS3'
    add_cdrstor_list:
    - CDRSTORID: '2G_second64_3'
      ISSINGLEBI: No
      FILETYPE: SecondFinal
      AGID: 'PS3'
      MNAME: 'AP64_3'
      SFSTORDAYS: 30
      SFSTORDAYSRULE: ByRelativeDays
      SFCMRRULE: UNCOMPRESS
      CLOSEFILECOND: Unspecify
      EMPTYFILE: NO
      NAMINGRULE: 'SGSN000000000001_%Y%m%d%H%M%S_%08L.dat'
      ENDSN: 99999999
      NUMSCHSN: NO
      STORDAYS: 30
      BIFILETYPE: ''
      CDRATTIME: ''
      CDRINTERV: 1800
      CDRNUMBER: ''
      CDRSIZE: 1024
      CDRSTORDELTASKSLEEPTIME: 20
      CDRSTORDELTASKSTARTTIME: '02:00'
      CHLNAME: 'All'
      CMRRULE: ZLIB
      FCMRRULE: GZIP
      FSTORDAYS: 7
      FSTORDAYSRULE: ByRelativeDays
      PDDESTPATH: ''
      SFCDRSIZE: 1024
      STARTSN: 1
      STORDAYSRULE: ByRelativeDays
    add_actrl_list:
    - ACID: 'R6CDR'
      AGID: 'group2'
      IPRID: 'ga'
      PORT: 3387
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置3G话单处理的格式引擎包及对应软参。

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

### 2 **可选：**配置格式引擎包对应的软参。

### 不同的格式引擎包对软参的支持情况可能不同，可以通过**DSP FMTSOFTPARA**命令查询对应格式引擎包可配置的软参。

### 软参取值请根据业务实际需要进行配置。

```jinja2
{%- if is_optional_fmtpkg_softparam -%}
    {%- for item in add_fmtpkgcfg_list -%}
        ADD FMTPKGCFG:
        {#- --- 必选参数 --- -#}
        PRFNAME="{{item.PRFNAME}}",
        CFGNAME="{{item.CFGNAME}}",
        CFGTYPE={{item.CFGTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CFGTYPE=FEM_PARA_UINT 时必选 --- -#}
        {%- if item.CFGTYPE == 'FEM_PARA_UINT' -%}
            CFG_UINT_VALUE={{item.CFG_UINT_VALUE}},
        {%- endif -%}
        {#- --- 条件必选：CFGTYPE=FEM_PARA_ENUM 时必选 --- -#}
        {%- if item.CFGTYPE == 'FEM_PARA_ENUM' -%}
            CFG_BOOL_VALUE={{item.CFG_BOOL_VALUE}},
        {%- endif -%}
        {#- --- 条件必选：CFGTYPE=FEM_PARA_IPADDR 时必选 --- -#}
        {%- if item.CFGTYPE == 'FEM_PARA_IPADDR' -%}
            CFG_IP_VALUE="{{item.CFG_IP_VALUE}}",
        {%- endif -%}
        {#- --- 条件必选：CFGTYPE=FEM_PARA_STRING 时必选 --- -#}
        {%- if item.CFGTYPE == 'FEM_PARA_STRING' -%}
            CFG_STR_VALUE="{{item.CFG_STR_VALUE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置2/3G业务处理模块。

```jinja2
{%- for item in add_module_list -%}
    ADD MODULE:
    {#- --- 必选参数 --- -#}
    MNAME="{{item.MNAME}}",
    AGID="{{item.AGID}}",
    ;
{%- endfor -%}
```

### MNAME格式为APXX\_YY，XX为RUID（从64开始递增），YY为模块ID（4G业务处理模块ID固定为2），国漫的消息量很小，为了简化配置和计费对接，建议只在前两个虚机添加业务模块。

### 4 话单处理相关配置。

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
        {%- if item.SFCMRRULE is not none -%}
            SFCMRRULE={{item.SFCMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.SFCMRRULE is not none -%}
            SFCMRRULE={{item.SFCMRRULE}},
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
        {%- if item.ENDSN is not none -%}
            ENDSN={{item.ENDSN}},
        {%- endif -%}
    {#- --- 条件可选：FILETYPE=SecondFinal 时可选 --- -#}
    {%- elif item.FILETYPE == 'SecondFinal' -%}
        {%- if item.ENDSN is not none -%}
            ENDSN={{item.ENDSN}},
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

### 5 配置3G Ga接口本端接入网元分组的接入控制。

```jinja2
{%- for item in add_actrl_list -%}
    ADD ACTRL:
    {#- --- 必选参数 --- -#}
    ACID="{{item.ACID}}",
    AGID="{{item.AGID}}",
    IPRID="{{item.IPRID}}",
    PORT={{item.PORT}},
    ;
{%- endfor -%}
```

