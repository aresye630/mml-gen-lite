---
id: ''
name: 配置漫游用户数据
ne_type: UNC
type: feature
description: 执行该任务的场景如下：  * 开局 * 扩容 * 现网引入新HLR * 业务调整
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置移动性管理","配置漫游用户数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
执行该任务的场景如下：* 开局* 扩容* 现网引入新HLR* 业务调整

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
* 本局7号信令与SG数据已经配置完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置互联PLMN。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_imsigt_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '配置IMSI-GT转换关系。'
          data_source: ''
          pattern: ''
          default: ''
        GT:
          name: '国家代码_网络接入号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_connectplmn_list:
    - MCC: '460'
      MNC: '11'
      CC: '86'
      SM: YES
      SMS: YES
      MAXSMNUM: 11
      SMSCR: NO
    add_imsigt_list:
    - IMSIPRE: '46011'
      GT: '86111'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置互联PLMN。

```jinja2
{%- for item in add_connectplmn_list -%}
    ADD CONNECTPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置IMSI-GT转换关系。

```jinja2
{%- for item in add_imsigt_list -%}
    ADD IMSIGT:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    GT="{{item.GT}}",
    ;
{%- endfor -%}
```

