---
id: ''
name: 离线计费配置（5G）
ne_type: UEG
type: feature
description: 该任务用于指导操作人员完成融合计费中的离线计费对接话单处理参数。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置基础业务","离线计费功能配置（基于服务化接口）","NCG配置","离线计费配置（5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务用于指导操作人员完成融合计费中的离线计费对接话单处理参数。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cdrproc_list:
      type: items
      properties:
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRFNAME:
          name: '格式引擎包名'
          type: string
          required: false
          description: '+ 格式引擎包文件全名，包括后缀名。例如，“PS\_R15\_VF80.tar.gz”。 + 不同的局点话单处理规则不同，需要根据实际情况配置相应的格式引擎包。 + 该参数只能由字母、数字、下划线、点组成。'
          data_source: ''
          pattern: ''
          default: ''
        SHAREFILECSN:
          name: 'SHAREFILECSN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEQNUMMODE:
          name: 'SEQNUMMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_fmtpkgcfg_list:
      type: items
      properties:
        PRFNAME:
          name: '格式引擎包名'
          type: string
          required: false
          description: '“PRFNAME”可以通过**LST CDRPROC**命令查询获取。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFGNAME:
          name: '格式引擎包软参名称'
          type: string
          required: false
          description: '“CFGNAME”可以通过**DSP FMTSOFTPARA**命令获取，其他名称无法生效。  说明：  不同的格式引擎包对软参的支持情况可能不同，可以通过**DSP FMTSOFTPARA**命令查询对应格式引擎包可配置的软参。'
          data_source: ''
          pattern: ''
          default: ''
        CFGTYPE:
          name: '格式引擎软参类型'
          type: string
          required: false
          description: '该参数需与“CFGNAME”对应的“格式引擎包软参类型”匹配，“格式引擎包软参类型”可以通过**DSP FMTSOFTPARA**命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        CFG_UINT_VALUE:
          name: '格式引擎软参值'
          type: string
          required: false
          description: '“CFG\_UINT\_VALUE”在“CFGNAME”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过**DSP FMTSOFTPARA**命令查询获取。  说明：  软参取值请根据业务实际需要进行配置。'
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
          description: '+ 首先执行**LST SERVICERUSTATE**命令，查询出当前的RUID。该参数输入格式固定为''AP''接RUID\_APID，APID值为1~4。例如：RUID为64时，该参数可以是“AP64\_1”、“AP64\_2”、“AP64\_3”、“AP64\_4”。 + 不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '+ 该值需要执行**LST CDRPROC**命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行**ADD CDRPROC**命令增加。 不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
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
          description: '不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: 'ISSINGLEBI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILETYPE:
          name: 'FILETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STORDAYS:
          name: '原始话单文件保存天数'
          type: string
          required: false
          description: '+ 原始话单储存天数。超过此期限的话单，CG会将其删除。需根据当前局点要求，对此参数进行修改。 + 删除原始话单之前，系统会检查一下该话单是否被处理过，如果没有被处理，超过了期限的话单也不会被删除掉。但是原始话单文件保存天数方式为“按绝对天数”时，没有被处理但是超过期限也会被删除，因此原始话单文件保存天数方式为“按绝对天数”时，原始话单保存天数不允许小于3天。 + 当磁盘剩余空间小于自动清理话单的磁盘空间阈值时，系统为了保证业务的正常运行，会自动清理话单。清理的顺序为首先清理第一份最终话单，之后清理原始话单。但是清理之后，第一份最终话单和原始话单最少保证各有七天的话单。   - 当系统为单分区版本时，话单清理的磁盘剩余空间阈值为800MB。   - 当系统为多分区版本时，话单清理的磁盘剩余空间阈值为600MB。'
          data_source: ''
          pattern: ''
          default: ''
        STORDAYSRULE:
          name: 'STORDAYSRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMRRULE:
          name: 'CMRRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYS:
          name: '第一份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        SFSTORDAYS:
          name: '第二份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        NAMINGRULE:
          name: '最终话单文件名命名规则'
          type: string
          required: false
          description: '+ 默认最终话单文件名的配置为“b%08L.dat”，默认的话单文件名为b00000001.dat～b99999999.dat。 + 当“第二份最终话单文件压缩方式”的值为“GZIP”时，需要手动地增加压缩后缀，否则，第二份最终话单文件名中不显示压缩后缀。 + 该参数不能包含“/、\、\*、>、<、|”。 + 最终话单文件的命名规则建议默认增加 "%B" 的描述，否则BOSS获取话单存在重名风险。 + 当本地备份分发ADD CDRDISTR的可选项ISADDAPNAME选否以及模块名填 "AP\_ALL"，第二份最终话单的命名规则必须是带有"%B"的正则表达式。 + 不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: ''
          pattern: ''
          default: ''
    add_cdrstor_list_1:
      type: items
      properties:
        CDRSTORID:
          name: '话单存储标识'
          type: string
          required: false
          description: '不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: 'ISSINGLEBI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILETYPE:
          name: 'FILETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYS:
          name: '第一份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYSRULE:
          name: 'FSTORDAYSRULE'
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
        STORDAYS:
          name: '原始话单文件保存天数'
          type: string
          required: false
          description: '+ 原始话单储存天数。超过此期限的话单，CG会将其删除。需根据当前局点要求，对此参数进行修改。 + 删除原始话单之前，系统会检查一下该话单是否被处理过，如果没有被处理，超过了期限的话单也不会被删除掉。但是原始话单文件保存天数方式为“按绝对天数”时，没有被处理但是超过期限也会被删除，因此原始话单文件保存天数方式为“按绝对天数”时，原始话单保存天数不允许小于3天。 + 当磁盘剩余空间小于自动清理话单的磁盘空间阈值时，系统为了保证业务的正常运行，会自动清理话单。清理的顺序为首先清理第一份最终话单，之后清理原始话单。但是清理之后，第一份最终话单和原始话单最少保证各有七天的话单。   - 当系统为单分区版本时，话单清理的磁盘剩余空间阈值为800MB。   - 当系统为多分区版本时，话单清理的磁盘剩余空间阈值为600MB。'
          data_source: ''
          pattern: ''
          default: ''
        SFSTORDAYS:
          name: '第二份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        NAMINGRULE:
          name: '最终话单文件名命名规则'
          type: string
          required: false
          description: '+ 默认最终话单文件名的配置为“b%08L.dat”，默认的话单文件名为b00000001.dat～b99999999.dat。 + 当“第二份最终话单文件压缩方式”的值为“GZIP”时，需要手动地增加压缩后缀，否则，第二份最终话单文件名中不显示压缩后缀。 + 该参数不能包含“/、\、\*、>、<、|”。 + 最终话单文件的命名规则建议默认增加 "%B" 的描述，否则BOSS获取话单存在重名风险。 + 当本地备份分发ADD CDRDISTR的可选项ISADDAPNAME选否以及模块名填 "AP\_ALL"，第二份最终话单的命名规则必须是带有"%B"的正则表达式。 + 不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: ''
          pattern: ''
          default: ''
    add_cdrstor_list_2:
      type: items
      properties:
        CDRSTORID:
          name: '话单存储标识'
          type: string
          required: false
          description: '不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: 'ISSINGLEBI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILETYPE:
          name: 'FILETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          required: false
          description: '与**ADD MODULE**中配置保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        SFSTORDAYS:
          name: '第二份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        SFSTORDAYSRULE:
          name: 'SFSTORDAYSRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SFCMRRULE:
          name: 'SFCMRRULE'
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
        EMPTYFILE:
          name: 'EMPTYFILE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAMINGRULE:
          name: '最终话单文件名命名规则'
          type: string
          required: false
          description: '+ 默认最终话单文件名的配置为“b%08L.dat”，默认的话单文件名为b00000001.dat～b99999999.dat。 + 当“第二份最终话单文件压缩方式”的值为“GZIP”时，需要手动地增加压缩后缀，否则，第二份最终话单文件名中不显示压缩后缀。 + 该参数不能包含“/、\、\*、>、<、|”。 + 最终话单文件的命名规则建议默认增加 "%B" 的描述，否则BOSS获取话单存在重名风险。 + 当本地备份分发ADD CDRDISTR的可选项ISADDAPNAME选否以及模块名填 "AP\_ALL"，第二份最终话单的命名规则必须是带有"%B"的正则表达式。 + 不能输入的特殊字符请参考NCG产品文档对应MML帮助。'
          data_source: ''
          pattern: ''
          default: ''
        ENDSN:
          name: 'ENDSN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NUMSCHSN:
          name: 'NUMSCHSN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STORDAYS:
          name: '原始话单文件保存天数'
          type: string
          required: false
          description: '+ 原始话单储存天数。超过此期限的话单，CG会将其删除。需根据当前局点要求，对此参数进行修改。 + 删除原始话单之前，系统会检查一下该话单是否被处理过，如果没有被处理，超过了期限的话单也不会被删除掉。但是原始话单文件保存天数方式为“按绝对天数”时，没有被处理但是超过期限也会被删除，因此原始话单文件保存天数方式为“按绝对天数”时，原始话单保存天数不允许小于3天。 + 当磁盘剩余空间小于自动清理话单的磁盘空间阈值时，系统为了保证业务的正常运行，会自动清理话单。清理的顺序为首先清理第一份最终话单，之后清理原始话单。但是清理之后，第一份最终话单和原始话单最少保证各有七天的话单。   - 当系统为单分区版本时，话单清理的磁盘剩余空间阈值为800MB。   - 当系统为多分区版本时，话单清理的磁盘剩余空间阈值为600MB。'
          data_source: ''
          pattern: ''
          default: ''
        FSTORDAYS:
          name: '第一份最终话单文件保存天数'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cdrproc_list:
    - AGID: PS1
      PRFNAME: PS_R15_VF80.tar.gz
      SHAREFILECSN: OFF
      SEQNUMMODE: IE
    add_fmtpkgcfg_list:
    - PRFNAME: PS_R15_VF80.tar.gz
      CFGNAME: MergeSwitch
      CFGTYPE: FEM_PARA_UINT
      CFG_UINT_VALUE: '0'
    add_module_list:
    - MNAME: AP64_1
      AGID: PS1
    add_cdrstor_list:
    - CDRSTORID: Original1
      ISSINGLEBI: No
      FILETYPE: Original
      STORDAYS: '7'
      STORDAYSRULE: ByRelativeDays
      CMRRULE: ZLIB
      FSTORDAYS: '30'
      SFSTORDAYS: '30'
      MNAME: AP64_1
      AGID: PS1
      NAMINGRULE: SMF000000000001_%Y%m%d%H%M%S_%08L.dat
    add_cdrstor_list_1:
    - CDRSTORID: first1
      ISSINGLEBI: No
      FILETYPE: FirstFinal
      FSTORDAYS: '30'
      FSTORDAYSRULE: ByRelativeDays
      FCMRRULE: GZIP
      STORDAYS: '7'
      SFSTORDAYS: '30'
      MNAME: AP64_1
      AGID: PS1
      NAMINGRULE: SMF000000000001_%Y%m%d%H%M%S_%08L.dat
    add_cdrstor_list_2:
    - CDRSTORID: 5G_second64_1
      ISSINGLEBI: No
      FILETYPE: SecondFinal
      AGID: PS1
      MNAME: AP64_1
      SFSTORDAYS: '30'
      SFSTORDAYSRULE: ByRelativeDays
      SFCMRRULE: UNCOMPRESS
      CLOSEFILECOND: Unspecify
      EMPTYFILE: NO
      NAMINGRULE: SMF000000000001_%Y%m%d%H%M%S_%08L.dat
      ENDSN: '99999999'
      NUMSCHSN: NO
      STORDAYS: '7'
      FSTORDAYS: '30'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置5G话单处理的格式引擎包。

#### 1.1 配置格式引擎包。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrproc_list的变量区（command: ADD CDRPROC） -#}
<!-- MISSING_MACRO: command=ADD CDRPROC list_name=add_cdrproc_list step_id=1.1 -->
```

#### 1.2 **可选：**配置格式引擎包相关软参。

#### 不同的格式引擎包对软参的支持情况可能不同，可以通过**DSP FMTSOFTPARA**命令查询对应格式引擎包可配置的软参。

#### 软参取值请根据业务实际需要进行配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fmtpkgcfg_list的变量区（command: ADD FMTPKGCFG） -#}
<!-- MISSING_MACRO: command=ADD FMTPKGCFG list_name=add_fmtpkgcfg_list step_id=1.2 -->
```

### 2 配置5G业务处理模块。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_module_list的变量区（command: ADD MODULE） -#}
<!-- MISSING_MACRO: command=ADD MODULE list_name=add_module_list step_id=2 -->
```

### 3 配置话单处理相关配置。

#### 3.1 原始话单参考如下命令进行配置，默认保存7天。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrstor_list的变量区（command: ADD CDRSTOR） -#}
<!-- MISSING_MACRO: command=ADD CDRSTOR list_name=add_cdrstor_list step_id=3.1 -->
```

#### 3.2 第一份最终话单参考如下命令进行配置，保存为30天。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrstor_list_1的变量区（command: ADD CDRSTOR） -#}
<!-- MISSING_MACRO: command=ADD CDRSTOR list_name=add_cdrstor_list_1 step_id=3.2 -->
```

#### 3.3 第二份最终话单文件命名可以参考如下命令进行配置，相关文件命名需要根据现场规范进行配置。

#### “MNAME”来源于步骤2中**ADD MODULE**命令，“MNAME”个数与**LST SERVICERUSTATE**命令查询出的RU个数一致。当“MNAME”有多个时**ADD CDRSTOR**命令需要配置多条。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrstor_list_2的变量区（command: ADD CDRSTOR） -#}
<!-- MISSING_MACRO: command=ADD CDRSTOR list_name=add_cdrstor_list_2 step_id=3.3 -->
```

