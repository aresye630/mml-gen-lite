---
id: ''
name: 配置全局数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM网元时，完成5G全局数据的配置。  应急UDM从中心UDM/外置SFTP服务器同步用户数据，UDM全局数据参考本页面配置。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","参考：详细配置指导","配置UDM","配置全局数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM网元时，完成5G全局数据的配置。应急UDM从中心UDM/外置SFTP服务器同步用户数据，UDM全局数据参考本页面配置。

## 必备事项
前提条件

已完成配置UDM和USCDB对接配置（风筝M）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rst_module_list:
      type: items
      properties:
        MID:
          name: '模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT:
          name: '模块类型'
          type: string
          enum:
          - DPU
          - NDF
          - DBG
          - DSG
          - DRU
          - DSU
          - PGW
          - DMA
          - CAG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_syshlrsn_list:
      type: items
      properties:
        SYSHLRSN:
          name: '系统HLR序列号'
          type: string
          required: false
          description: '该参数取值与USCDB MML命令界面上的**SET SYSNO**命令配置的“SYSTEMNO”参数的取值相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HLRNAME:
          name: '系统HLR名称'
          type: string
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATUS:
          name: '状态'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_vhlrsn_list:
      type: items
      properties:
        SYSHLRSN:
          name: '系统HLR序列号'
          type: string
          required: false
          description: '统一规划。  规划虚拟HLR。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HLRSN:
          name: '虚拟HLR序列号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HLRNAME:
          name: '虚拟HLR名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mapserv_list:
      type: items
      properties:
        CBPASSWD:
          name: 'CB密码'
          type: string
          required: false
          description: '此处以用户的初始默认的CB密码为例。请根据运营商要求配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_hlrsn_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '该参数的取值需要与系统管理MML命令界面上的**ADD VHLRSN**命令配置的“HLRSN”的取值一一对应。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HLRNO:
          name: 'HLR号码'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATUS:
          name: '状态'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCODE:
          name: '国家码'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_udmserv_list:
      type: items
      properties:
        AUTHENTICATION_TYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_mapconf_list:
      type: items
      properties:
        SUPPORT_RANDOMKEY:
          name: '是否启用随机密钥'
          type: string
          required: false
          description: '启用随机密钥。随机密钥是对K2值进行加密保存。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_randomkey_list:
      type: items
      properties:
        KEYID:
          name: '密钥ID'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mapserv_list_1:
      type: items
      properties:
        DEFKEYID:
          name: '随机密钥默认ID'
          type: string
          required: false
          description: '该参数在**SET MAPCONF**命令的“是否启用随机密钥”参数为“TRUE”时生效。  采用**SET RANDOMKEY**命令定义的“密钥ID”参数值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_k2_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识HLR序列号。  该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        K2SNO:
          name: 'K2序列号'
          type: string
          required: false
          description: '用于标识K2序列号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEYTYPE:
          name: 'K2密钥输入方式'
          type: string
          required: false
          description: '用于标识K2密钥输入方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        K2VALUE:
          name: 'K2值'
          type: string
          required: false
          description: '用于标识K2密钥值。K2是用来给KI加密储存的密钥、对K2加密存储的KI值进行解密的密钥。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALGTYPE:
          name: '算法类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_defaultk2sno_list:
      type: items
      properties:
        TYPE:
          name: '类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        K2SNO:
          name: '缺省存储加密密钥索引'
          type: string
          required: false
          description: '该参数必须先由**ADD K2**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_opr_list:
      type: items
      properties:
        SYSHLRSN:
          name: '系统HLR序列号'
          type: string
          required: false
          description: '采用**ADD SYSHLRSN**命令定义的“SYSHLRSN”参数值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OPNAME:
          name: '操作员名称'
          type: string
          required: false
          description: '操作员登录时的名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '操作员描述'
          type: string
          required: false
          description: '便于识别账号的作用即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          required: false
          description: '密码字符集至少包含大写字母+小写字母+数字+特殊字符中的三类。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UG:
          name: '操作员级别'
          type: string
          required: false
          description: '用于指定操作员的级别。不同级别级别的权限详见MML。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STATUS:
          name: '操作员状态'
          type: string
          required: false
          description: '是否激活操作员，即是否允许操作员登录PGW系统。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ATP:
          name: '账号类型'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    rst_module_list:
    - MID: 7
      MT: PGW
    add_syshlrsn_list:
    - SYSHLRSN: '1'
      HLRNAME: HLR01
      STATUS: MASTER
    add_vhlrsn_list:
    - SYSHLRSN: '1'
      HLRSN: '1'
      HLRNAME: VHLR01
    set_mapserv_list:
    - CBPASSWD: '0000'
    add_hlrsn_list:
    - HLRSN: '1'
      HLRNO: '8613910000'
      STATUS: MASTER
      CCODE: '86'
    set_udmserv_list:
    - AUTHENTICATION_TYPE: AUTHENTICATION_TYPE_AUSF
    set_mapconf_list:
    - SUPPORT_RANDOMKEY: TRUE
    set_randomkey_list:
    - KEYID: '1'
    set_mapserv_list_1:
    - DEFKEYID: '1'
    add_k2_list:
    - HLRSN: '1'
      K2SNO: '100'
      KEYTYPE: ClearKey
      K2VALUE: '*****'
      ALGTYPE: AES128
    set_defaultk2sno_list:
    - TYPE: K2
      HLRSN: '1'
      K2SNO: '100'
    add_opr_list:
    - SYSHLRSN: '1'
      OPNAME: pgwuser
      DESC: To enterprise
      PWD: '*****'
      CFM: '*****'
      UG: OBSERVER
      STATUS: ACTIVE
      ATP: MAN-MACHINE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 重启PGW模块。

#### 1.1 登录“CSP MML命令”界面。

#### 1.2 重启PGW模块。如已重启过PGW模块，请跳过本步骤。

#### 重启PGW模块的操作需要在登录PGW Web LMT之前进行，否则PGW Web LMT界面的Service Management MML导航树显示为空。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MID={{item.MID}},
    MT={{item.MT}},
    ;
{%- endfor -%}
```

### 2 登录PGW Web LMT MML命令界面。

### 此处以完整模式HLR（输入“HLRSN”“用户名”、“登录密码”）登录PGW Web LMT为例，详细操作请参见登录与退出PGW Web LMT。

### 3 增加系统HLR。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_syshlrsn_list的变量区（command: ADD SYSHLRSN） -#}
<!-- MISSING_MACRO: command=ADD SYSHLRSN list_name=add_syshlrsn_list step_id=3 -->
```

### 4 增加虚拟HLR。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vhlrsn_list的变量区（command: ADD VHLRSN） -#}
<!-- MISSING_MACRO: command=ADD VHLRSN list_name=add_vhlrsn_list step_id=4 -->
```

### 5 登录“UDM业务管理”窗口。

### 6 设置CB密码。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list step_id=6 -->
```

### 7 增加HLR序列号。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_hlrsn_list的变量区（command: ADD HLRSN） -#}
<!-- MISSING_MACRO: command=ADD HLRSN list_name=add_hlrsn_list step_id=7 -->
```

### 8 设置UDM业务参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=8 -->
```

### 9 配置随机密钥。配置的随机密钥用于对K2值进行加密保存。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapconf_list的变量区（command: SET MAPCONF） -#}
<!-- MISSING_MACRO: command=SET MAPCONF list_name=set_mapconf_list step_id=9 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_randomkey_list的变量区（command: SET RANDOMKEY） -#}
<!-- MISSING_MACRO: command=SET RANDOMKEY list_name=set_randomkey_list step_id=9 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list_1的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list_1 step_id=9 -->
```

### 10 配置对KI加密的K2值。

#### 10.1 //K2是用来给KI加密储存的密钥、对K2加密存储的KI值进行解密的密钥。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_k2_list的变量区（command: ADD K2） -#}
<!-- MISSING_MACRO: command=ADD K2 list_name=add_k2_list step_id=10.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_defaultk2sno_list的变量区（command: SET DEFAULTK2SNO） -#}
<!-- MISSING_MACRO: command=SET DEFAULTK2SNO list_name=set_defaultk2sno_list step_id=10.1 -->
```

### 11 登录“系统管理”界面。

### 详细操作请参见登录PGW Web LMT MML命令界面。

### 12 增加账号，用于企业访问PGW。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_opr_list的变量区（command: ADD OPR） -#}
<!-- MISSING_MACRO: command=ADD OPR list_name=add_opr_list step_id=12 -->
```

