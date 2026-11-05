---
id: ''
name: 配置跟踪和日志匿名化功能（通过OM Portal和软件参数）
ne_type: UNC
type: feature
description: UNC支持通过OM Portal开启跟踪的匿名化功能，通过软件参数开启日志的匿名化功能。  为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","数据安全配置","配置跟踪和日志匿名化功能（通过OM Portal和软件参数）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持通过OM Portal开启跟踪的匿名化功能，通过软件参数开启日志的匿名化功能。为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。

## 必备事项
前提条件

请仔细阅读个人隐私数据保护。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_commonsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - DwCom
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDCOMNUM:
          name: 'Common Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwsoftparabits_list:
      type: items
      properties:
        PARATYPE:
          name: '数据类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWORD参数索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_commonsoftparaofbit_list:
    - DT: DwCom
      DWORDCOMNUM: 1
      VALUE: '0'
      POSITION: 1
    set_fwsoftparabits_list:
    - PARATYPE: DWORD
      DWORDNUM: 1601
      VALUE: VALUE_0
      POSITION: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 通过OM Portal打开跟踪的匿名化功能：通过OM Portal下载跟踪文件时，在弹出的“下载”界面中勾选“匿名化”。

#### 1.1 当UNC未连接U2020/MAE之前，根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

#### 1.2 当UNC连接U2020/MAE之后，同步保存U2020/MAE上配置的假名化/匿名化功能状态及HMAC密钥信息：

##### 1.2.1 - 如果U2020/MAE上配置匿名化功能为开启，则强制做匿名化处理；

##### 1.2.2 - 如果U2020/MAE上配置匿名化功能为关闭，则根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

### 2 通过软件参数打开日志的匿名化功能。

### 通过MML命令**SET COMMONSOFTPARAOFBIT**设置软件参数DWORD1 BIT1为0。

### 通过MML命令**SET FWSOFTPARABITS**设置软件参数DWORD1601 BIT1为0。

```jinja2
{%- for item in set_commonsoftparaofbit_list -%}
    SET COMMONSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=DwCom 时必选 --- -#}
    {%- if item.DT == 'DwCom' -%}
        DWORDCOMNUM={{item.DWORDCOMNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_fwsoftparabits_list -%}
    SET FWSOFTPARABITS:
    {#- --- 必选参数 --- -#}
    PARATYPE={{item.PARATYPE}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PARATYPE=DWORD/DWORD_EX 时必选 --- -#}
    {%- if item.PARATYPE in ['DWORD', 'DWORD_EX'] -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

