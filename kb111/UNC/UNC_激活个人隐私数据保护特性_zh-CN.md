---
id: ''
name: 激活个人隐私数据保护特性
ne_type: UNC
type: feature
description: 为保证个人隐私数据的安全性，建议运营商遵从所在国家的相关法律开启假名化/匿名化功能，对跟踪、日志、CHR中使用的用户个人标识进行保护。  适用于SGSN、MME、GGSN、SGW\_C、PGW\_C、AMF、SMF、NRF、NSSF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","安全管理功能","WSFD-010305 个人隐私数据保护","激活个人隐私数据保护特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为保证个人隐私数据的安全性，建议运营商遵从所在国家的相关法律开启假名化/匿名化功能，对跟踪、日志、CHR中使用的用户个人标识进行保护。适用于SGSN、MME、GGSN、SGW\_C、PGW\_C、AMF、SMF、NRF、NSSF。

## 必备事项
前提条件

请仔细阅读WSFD-010305 个人隐私数据保护特性概述。
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
    set_pseudonypolicy_list:
      type: items
      properties:
        LOCALPOLICY:
          name: 'CHR假名化本地策略开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEY:
          name: 'CHR假名化本地策略口令'
          type: string
          minLength: 20
          maxLength: 36
          required: false
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
    set_pseudonypolicy_list:
    - LOCALPOLICY: ON
      KEY: '*****'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置跟踪匿名化功能。

### | Option | Description |

### | --- | --- |

### | **通过网管** | 详细操作步骤请参见U2020/MAE产品文档的“假名化策略管理”。  须知：  + U2020/MAE上假名化/匿名化开关默认开启，建议运营商遵从所在国家的相关法律。 + 为更好地保护用户个人隐私，请定期更新并妥善保存HMAC密钥，避免被他人获取。密钥的长度建议符合安全要求，提升安全性。 |

### | **通过OM Portal** | + 当UNC未连接U2020/MAE之前，根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。 + 当UNC连接U2020/MAE之后，同步保存U2020/MAE上配置的假名化/匿名化功能状态及HMAC密钥信息：   - 如果U2020/MAE上配置匿名化功能为开启，则强制做匿名化处理；   - 如果U2020/MAE上配置匿名化功能为关闭，则根据OM Portal跟踪“下载”界面的“匿名化”选项状态判断是否做匿名化处理。 |

### 2 配置日志匿名化功能。

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

### 3 配置CHR假名化功能。

### | Option | Description |

### | --- | --- |

### | **通过网管** | 详细操作步骤请参见U2020/MAE产品文档的“假名化策略管理”。  须知：  + U2020/MAE上假名化/匿名化开关默认开启，建议运营商遵从所在国家的相关法律。 + 为更好地保护用户个人隐私，请定期更新并妥善保存HMAC密钥，避免被他人获取。密钥的长度建议符合安全要求，提升安全性。 |

### | **通过MML** | 执行MML命令**SET PSEUDONYPOLICY**开启本地CHR假名化功能，并配置假名化口令。假名化口令为密码类型，长度必须为偶数（最小16位，最大30位），且只能输入0-9、A-F、a-f。   ``` SET PSEUDONYPOLICY: LOCALPOLICY=ON, KEY="*****"; ```  + 当UNC未连接U2020/MAE，或已连接U2020/MAE但U2020/MAE上未进行假名化/匿名化功能设置时，根据UNC上MML命令配置判断是否做假名化处理。 + 当UNC已连接U2020/MAE，且U2020/MAE上已有假名化/匿名化功能配置时，根据U2020/MAE上配置的假名化/匿名化功能状态判断是否做假名化处理。 |

```jinja2
{%- if is_scenario_mml -%}
    {%- for item in set_pseudonypolicy_list -%}
        SET PSEUDONYPOLICY:
        {#- --- 必选参数 --- -#}
        LOCALPOLICY={{item.LOCALPOLICY}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOCALPOLICY=ON 时必选 --- -#}
        {%- if item.LOCALPOLICY == 'ON' -%}
            KEY="{{item.KEY}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

