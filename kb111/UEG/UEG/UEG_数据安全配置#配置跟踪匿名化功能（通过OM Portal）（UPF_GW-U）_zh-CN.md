---
id: ''
name: 配置跟踪匿名化功能（通过OM Portal）（UPF/GW-U）
ne_type: UEG
type: feature
description: UEG支持通过OM Portal开启跟踪的匿名化功能。  为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","数据安全配置","配置跟踪匿名化功能（通过OM Portal）（UPF/GW-U）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","数据安全配置","配置跟踪匿名化功能（通过OM Portal）（UPF/GW-U）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","数据安全配置","配置跟踪匿名化功能（通过OM Portal）（UPF/GW-U）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","可选配置","数据安全配置","配置跟踪匿名化功能（通过OM Portal）（UPF/GW-U）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG支持通过OM Portal开启跟踪的匿名化功能。为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。

## 必备事项
前提条件

请仔细阅读个人隐私数据保护。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 通过OM Portal下载跟踪文件时，在弹出的“下载”界面中勾选“匿名化”。

#### 1.1 当UEG连接MAE之前，根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

#### 1.2 当UEG连接MAE之后，同步保存MAE上配置的假名化/匿名化功能状态及HMAC密钥信息：

##### 1.2.1 - 如果MAE上配置匿名化功能为开启，则强制做匿名化处理；

##### 1.2.2 - 如果MAE上配置匿名化功能为关闭，则根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。

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
    ;
{%- endfor -%}
```

