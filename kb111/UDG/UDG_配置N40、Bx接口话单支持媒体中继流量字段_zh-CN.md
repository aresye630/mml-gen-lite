---
id: ''
name: 配置N40、Bx接口话单支持媒体中继流量字段
ne_type: UDG
type: feature
description: 在N40计费场景下，当运营商需要核对话单流量时，请参考本章节进行配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置CHF","配置N40、Bx接口话单支持媒体中继流量字段"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在N40计费场景下，当运营商需要核对话单流量时，请参考本章节进行配置。

## 必备事项
前提条件

* 请提前了解话单流量核对方案。
* CHF已升级到20.16.2及后续版本。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ncgsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          required: false
          description: '停止N40接口话单接收功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    stp_cdrreceive_list:
      type: items
      properties:
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '停止Ga接口话单接收功能。此处的"**PS\_X**"通过**LST CDRPROC**命令查询，选择234G业务的接入网元分组标识（不是以“PS\_R15”开头的格式引擎包名对应的接入网元分组标识）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ncgsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          required: false
          description: '配置话单携带媒体中继Relay字段。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_fmtpkgcfg_list:
      type: items
      properties:
        PRFNAME:
          name: '格式引擎包名'
          type: string
          required: false
          description: '此处的格式引擎包名"**PS\_R15\_VF80\_NorthChina\_CMCC.tar.gz**"通过**LST CDRPROC**命令查询，接入网元分组标识为“**PS\_X**”的格式引擎包名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFGNAME:
          name: '格式引擎包软参名称'
          type: string
          required: false
          description: '此参数控制格式引擎包加载的后存盘补丁名称。此处填写“r15\_vf80\_cmcc\_relay”，支持媒体中继功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CFGTYPE:
          name: '格式引擎软参类型'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        CFG_STR_VALUE:
          name: '格式引擎软参值'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        CFG_UINT_VALUE:
          name: 'CFG_UINT_VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cdrdistr_list:
      type: items
      properties:
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRANSMODE:
          name: '分发方式'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          required: false
          description: '模块名参数若当前配置了BI收敛可以直接设置为“ALL”。若没有配置BI收敛，则配置为具体的模块名，可通过**LST MODULE**命令查询，填写“接入网元分组标识”为“**PS\_X**”的模块名。此情况下，每个模块名的每一条通道都需要配置本地话单分发。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISCUTOMDISTR:
          name: '是否自定义分发'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SOURCECHL:
          name: '通道名称'
          type: string
          required: false
          description: '通道名称，可执行**DSP FEMPACKET**命令查询当前引擎包的通道信息；若当前省份为北京，则此处的通道名称可以选择北京以外的省份通道，如“Tianjin”；如此设置分发的通道名称参数，是因为该分发只用于查询浏览界面中观测Relay通道下生成的话单文件，所以设置的通道名称对应的目录下不能存在话单文件，故而选择其余省份的通道名称。  其余通道，如“ZERO”等通道，对应设置即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESTPATH:
          name: '目的路径'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ISADDAPNAME:
          name: '是否增加模块名到目的路径'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ISADDCHLNAME:
          name: '是否增加通道名到目的路径'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TRANSPER:
          name: '分发周期'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CMRRULE:
          name: '分发话单压缩方式'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LOGAUDIT:
          name: '是否开启日志稽核功能'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    rst_vnfc_list:
      type: items
      properties:
        ISFORCEOPER:
          name: '强制操作标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SERVICEINSTANCE:
          name: '服务实例'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ncgsoftparaofbit_list_2:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          required: false
          description: '恢复N40接口话单接收功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_ncgsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: '4'
      VALUE: VALUE_1
      POSITION: '24'
    stp_cdrreceive_list:
    - AGID: PS_X
    set_ncgsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: '23'
      VALUE: VALUE_1
      POSITION: '32'
    add_fmtpkgcfg_list:
    - PRFNAME: PS_R15_VF80_NorthChina_CMCC.tar.gz
      CFGNAME: BackSavePatchName
      CFGTYPE: FEM_PARA_STRING
      CFG_STR_VALUE: r15_vf80_cmcc_relay
      CFG_UINT_VALUE: '0'
    add_cdrdistr_list:
    - CDRDISTRID: task_offline
      ISSINGLEBI: NO
      TRANSMODE: LOCAL
      AGID: PS_X
      MNAME: ALL
      ISCUTOMDISTR: NO
      SOURCECHL: Tianjin/OFFLINE
      DESTPATH: ./Relay/OFFLINE
      ISADDAPNAME: YES
      ISADDCHLNAME: YES
      TRANSPER: EVERYDAY
      CMRRULE: UNCOMPRESS
      LOGAUDIT: NO
    rst_vnfc_list:
    - ISFORCEOPER: FALSE
      SERVICEINSTANCE: 'CG_VNFC_999'
    set_ncgsoftparaofbit_list_2:
    - DT: Dw
      DWORDNUM: '4'
      VALUE: VALUE_0
      POSITION: '24'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 停止N40口业务，执行**SET NCGSOFTPARAOFBIT**命令停止话单接收功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ncgsoftparaofbit_list的变量区（command: SET NCGSOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SET NCGSOFTPARAOFBIT list_name=set_ncgsoftparaofbit_list step_id=1 -->
```

### 2 停止Ga口业务，执行**STP CDRRECEIVE**命令停止话单接收功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该stp_cdrreceive_list的变量区（command: STP CDRRECEIVE） -#}
<!-- MISSING_MACRO: command=STP CDRRECEIVE list_name=stp_cdrreceive_list step_id=2 -->
```

### 3 查看停止接收话单是否成功。

### DSP CCL命令结果显示”原始话单采集速度”和”原始话单保存速度”均为0时，表示停止接收话单成功。

### 4 打开控制话单是否携带媒体中继Relay字段的软参。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ncgsoftparaofbit_list_1的变量区（command: SET NCGSOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SET NCGSOFTPARAOFBIT list_name=set_ncgsoftparaofbit_list_1 step_id=4 -->
```

### 5 添加格式引擎包软参配置媒体中继功能后存盘补丁、生成的Relay通道下的话单格式和话单是否压缩。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fmtpkgcfg_list的变量区（command: ADD FMTPKGCFG） -#}
<!-- MISSING_MACRO: command=ADD FMTPKGCFG list_name=add_fmtpkgcfg_list step_id=5 -->
```

### 6 添加本地话单分发，用于观测Relay目录下生成的话单。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrdistr_list的变量区（command: ADD CDRDISTR） -#}
<!-- MISSING_MACRO: command=ADD CDRDISTR list_name=add_cdrdistr_list step_id=6 -->
```

### 7 执行**RST VNFC**命令使添加的引擎包软参生效。

```jinja2
{%- for item in rst_vnfc_list -%}
    RST VNFC:
    {#- --- 必选参数 --- -#}
    SERVICEINSTANCE="{{item.SERVICEINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ISFORCEOPER is not none -%}
        ISFORCEOPER={{item.ISFORCEOPER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 等待3-5分支，执行DSP SERVICE命令查看模块是否处于激活状态，激活则加载成功。

### 9 恢复N40口业务，执行**SET NCGSOFTPARAOFBIT**命令恢复接收话单功能。

### Ga口业务在7执行**RST VNFC**后直接恢复，无需单独恢复。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ncgsoftparaofbit_list_2的变量区（command: SET NCGSOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SET NCGSOFTPARAOFBIT list_name=set_ncgsoftparaofbit_list_2 step_id=9 -->
```

