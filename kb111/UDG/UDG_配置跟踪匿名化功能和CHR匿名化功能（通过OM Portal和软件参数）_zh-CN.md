---
id: ''
name: 配置跟踪匿名化功能和CHR匿名化功能（通过OM Portal和软件参数）
ne_type: UDG
type: feature
description: UDG支持通过OM Portal开启跟踪的匿名化功能。  为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","数据安全配置","配置跟踪匿名化功能和CHR匿名化功能（通过OM Portal和软件参数）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UDG支持通过OM Portal开启跟踪的匿名化功能。为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。

## 必备事项
前提条件

请仔细阅读个人隐私数据保护。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_rptencrypt_list:
      type: items
      properties:
        ENCRYMODE:
          name: '加密模式'
          type: string
          enum:
          - DEFAULT
          - USER_DEFINED
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENCRYALGORI:
          name: '业务报表加密算法'
          type: string
          enum:
          - AES256_CBC
          - AES256_CTR
          - AES256_GCM
          - SHA1
          - SHA256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDKEY:
          name: '密码'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDKEYCONFIRM:
          name: '确认密码'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_rptencrypt_list:
    - ENCRYMODE: USER\_DEFINED
      ENCRYALGORI: SHA256
      PSWDKEY: '\*\*\*\*\*'
      PSWDKEYCONFIRM: '\*\*\*\*\*'
    set_softpara_list:
    - DT: BIT
      BITNUM: 1588
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 通过OM Portal下载跟踪文件时，在弹出的“下载”界面中勾选“匿名化”。

#### 1.1 当UDG连接U2020/MAE之前，根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

#### 1.2 当UDG连接U2020/MAE之后，同步保存U2020/MAE上配置的假名化/匿名化功能状态及HMAC密钥信息：

##### 1.2.1 - 如果U2020/MAE上配置匿名化功能为开启，则强制做匿名化处理；

##### 1.2.2 - 如果U2020/MAE上配置匿名化功能为关闭，则根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

### 2 通过MML命令开启报表的假名化功能。

```jinja2
{%- for item in set_rptencrypt_list -%}
    SET RPTENCRYPT:
    {#- --- 必选参数 --- -#}
    ENCRYMODE={{item.ENCRYMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ENCRYMODE=USER_DEFINED 时必选 --- -#}
    {%- if item.ENCRYMODE == 'USER_DEFINED' -%}
        ENCRYALGORI={{item.ENCRYALGORI}},
    {%- endif -%}
    {#- --- 条件必选：ENCRYMODE=USER_DEFINED 时必选 --- -#}
    {%- if item.ENCRYMODE == 'USER_DEFINED' -%}
        PSWDKEY="{{item.PSWDKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYMODE=USER_DEFINED 时必选 --- -#}
    {%- if item.ENCRYMODE == 'USER_DEFINED' -%}
        PSWDKEYCONFIRM="{{item.PSWDKEYCONFIRM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 通过软件参数打开CHR的匿名化功能。

### 通过MML命令**SET SOFTPARA**设置软件参数“BIT1588”为1。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

