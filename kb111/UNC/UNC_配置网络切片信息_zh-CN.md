---
id: ''
name: 配置网络切片信息
ne_type: UNC
type: feature
description: 在基于切片部署组网内，需要配置切片选择数据，以保证5GC当初始AMF无法判断或者判断自己无法为UE提供切片服务，需要向NSSF进行查询获取切片配置信息，详细请参考配置切片选择数据。  可以配置候选AMF信息，如果当前AMF故障或其他不能提供服务的异常场景下，NSSF将切片信息返回至规划的候选AMF，保证业务正常，详细请参考配置候选AMF信息。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置NSSF","配置网络切片信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在基于切片部署组网内，需要配置切片选择数据，以保证5GC当初始AMF无法判断或者判断自己无法为UE提供切片服务，需要向NSSF进行查询获取切片配置信息，详细请参考配置切片选择数据。可以配置候选AMF信息，如果当前AMF故障或其他不能提供服务的异常场景下，NSSF将切片信息返回至规划的候选AMF，保证业务正常，详细请参考配置候选AMF信息。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_cfgsnssai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '配置运营商支持的切片配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISACTIVE:
          name: '激活状态'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tacgroupinnssf_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '配置跟踪区域分组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC起始字符'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACEND:
          name: 'TAC结束字符'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_amfsetid_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '配置AMF集合支持的切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGIONID:
          name: '区域ID'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: '跟踪区域码分组名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_candidateamf_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置候选AMF信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFINSTANCEID:
          name: 'AMF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGIONID:
          name: '区域ID'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cfgsnssai_list:
    - INDEX: 1
      MCC: '123'
      MNC: '03'
      SST: 1
      SD: '010101'
      ISACTIVE: TRUE
    add_tacgroupinnssf_list:
    - INDEX: 1
      TACGROUPNAME: 'TACGROUP01'
      TACSTART: '290100'
      TACEND: '290110'
    add_amfsetid_list:
    - INDEX: 1
      SST: 1
      SD: '010101'
      MCC: '123'
      MNC: '03'
      REGIONID: '01'
      AMFSETID: '001'
      TACGROUPNAME: 'TACGROUP01'
    add_candidateamf_list:
    - INDEX: 1
      AMFINSTANCEID: 'bdc3f6f6-69ac-4c06-bfe5-030101000001'
      MCC: '123'
      MNC: '03'
      REGIONID: '01'
      AMFSETID: '001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **配置切片选择数据**

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置运营商支持的切片信息。

```jinja2
{%- for item in add_cfgsnssai_list -%}
    ADD CFGSNSSAI:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    SST={{item.SST}},
    ISACTIVE={{item.ISACTIVE}},
    {#- --- 可选参数 --- -#}
    {%- if item.INDEX is not none -%}
        INDEX={{item.INDEX}},
    {%- endif -%}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置AMF集合支持的切片信息。

```jinja2
{%- for item in add_tacgroupinnssf_list -%}
    ADD TACGROUPINNSSF:
    {#- --- 必选参数 --- -#}
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACSTART="{{item.TACSTART}}",
    TACEND="{{item.TACEND}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INDEX is not none -%}
        INDEX={{item.INDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_amfsetid_list -%}
    ADD AMFSETID:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    REGIONID="{{item.REGIONID}}",
    AMFSETID="{{item.AMFSETID}}",
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INDEX is not none -%}
        INDEX={{item.INDEX}},
    {%- endif -%}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **配置候选AMF信息**

#### 2.1 **可选：**配置候选AMF信息。

```jinja2
{%- if is_optional_candidate_amf_info -%}
    {%- for item in add_candidateamf_list -%}
        ADD CANDIDATEAMF:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        AMFINSTANCEID="{{item.AMFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        REGIONID="{{item.REGIONID}}",
        AMFSETID="{{item.AMFSETID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

