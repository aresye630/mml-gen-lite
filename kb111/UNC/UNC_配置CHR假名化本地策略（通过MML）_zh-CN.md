---
id: ''
name: 配置CHR假名化本地策略（通过MML）
ne_type: UNC
type: feature
description: UNC支持通过MML命令设置CHR假名化本地策略。  为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","数据安全配置","配置CHR假名化本地策略（通过MML）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持通过MML命令设置CHR假名化本地策略。为保证个人隐私数据的安全性，建议开启该功能。请运营商遵从所在国家的相关法律开启该功能。

## 必备事项
前提条件

请仔细阅读个人隐私数据保护。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
    set_pseudonypolicy_list:
    - LOCALPOLICY: ON
      KEY: '*****'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 执行MML命令**SET PSEUDONYPOLICY**开启本地CHR假名化功能，并配置假名化口令。假名化口令为密码类型，长度必须为偶数（最小16位，最大30位），且只能输入0-9、A-F、a-f。

```jinja2
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
```

#### 1.1 当UNC未连接U2020/MAE，或已连接U2020/MAE但U2020/MAE上未进行假名化/匿名化功能设置时，根据UNC上MML命令配置判断是否做假名化处理。

#### 1.2 当UNC已连接U2020/MAE，且U2020/MAE上已有假名化/匿名化功能配置时，根据U2020/MAE上配置的假名化/匿名化功能状态判断是否做假名化处理。

